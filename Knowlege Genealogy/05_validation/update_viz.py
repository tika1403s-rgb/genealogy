"""update_viz.py v2 — Regenerates ELEMENTS data in viz_interactive_T3.html.

Fixed in v2:
  • Adds node_type='tradition' to all tradition nodes
  • Adds edge_type='tradition' to all tradition edges
  • Computes position:{x,y} for every tradition node (preset layout requires it)
  • Creates separate Cytoscape nodes for pioneer and breakthrough satellites
  • Creates pioneer and breakthrough edges (edge_type='pioneer'/'breakthrough')
  • Updates ERA_COL in the HTML to include EMD, MOD, CON
"""
import csv, json, os, re, math
from collections import defaultdict

BASE = "/Users/shs/Documents/Claude/Projects/Knowlege Genealogy"
DATA = os.path.join(BASE, "04_nodes_edges")
VIZ  = os.path.join(BASE, "07_exports", "viz_interactive_T3.html")

# ── CSV helpers ──────────────────────────────────────────────
def read_csv_dict(filename):
    fp = os.path.join(DATA, filename)
    with open(fp, 'r', newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def split_ids(s):
    return [x.strip() for x in s.split(',') if x.strip()] if s else []

def safe_int(v, default=0):
    try:
        return int(v) if v else default
    except (ValueError, TypeError):
        return default

# ── Load CSVs ────────────────────────────────────────────────
nodes_list  = read_csv_dict('nodes.csv')
nodes       = {r['node_id']: r for r in nodes_list}
pioneers    = {r['pioneer_id']: r for r in read_csv_dict('pioneers.csv')}
brkths      = {r['breakthrough_id']: r for r in read_csv_dict('breakthroughs.csv')}
contribs    = read_csv_dict('pioneer_contributions.csv')
deps        = read_csv_dict('breakthrough_dependencies.csv')
edges_csv   = read_csv_dict('edges.csv')

# Index by node_id
node_contribs = defaultdict(list)
for c in contribs:
    node_contribs[c['node_id']].append(c)

node_deps = defaultdict(list)
for d in deps:
    node_deps[d['node_id']].append(d)

# ── Color constants ──────────────────────────────────────────
ERA_COLOR = {
    'ANC': '#2166AC',
    'MED': '#1A9850',
    'EMD': '#D95F02',
    'MOD': '#7570B3',
    'CON': '#E7298A',
}

BTYPE_COL = {
    'concept':       '#64B5F6',
    'method':        '#A5D6A7',
    'instrument':    '#FFD54F',
    'discovery':     '#FF8A65',
    'invention':     '#F48FB1',
    'formalization': '#CE93D8',
}

def pioneer_color(nationality):
    nat = (nationality or '').lower()
    if 'greek' in nat:    return '#2166AC'
    if 'islamic' in nat:  return '#1B7837'
    if 'chinese' in nat:  return '#C0392B'
    if 'indian' in nat:   return '#D95F02'
    if 'roman' in nat or 'byzantine' in nat: return '#8E6DBB'
    return '#7B2D8B'   # European / other

def node_era(nid):
    parts = nid.split('_')
    return parts[1] if len(parts) >= 2 else 'ANC'

# ── Tradition-node position layout ──────────────────────────
def compute_positions(nodes_dict):
    """Return {node_id: {x, y}} for every tradition node.

    Layout: era swim-bands on the x-axis, region swim-lanes on y.
    Large same-era/same-region groups wrap into two rows.
    """
    # Region Y lanes (centre of each horizontal band)
    REGION_Y = {
        'Greek':              150,
        'Greek (Ionian)':     150,
        'Hellenistic':        300,
        'Greek, Hellenistic': 200,
        'Roman':              200,
        'Islamic':            480,
        'Chinese':            680,
        'Indian':             880,
        'Byzantine':          380,
        'Greek, European':    380,
        'European':          1080,
        'Global':            1280,
    }
    DEFAULT_Y = 1080

    # X-centre of each era band
    ERA_X = {
        'ANC':  600,
        'MED': 1800,
        'EMD': 3300,
        'MOD': 4800,
        'CON': 6200,
    }

    # Group nodes by (era, region) and sort by date_start
    groups = defaultdict(list)
    for nid, n in nodes_dict.items():
        era    = node_era(nid)
        region = n.get('region', 'European')
        ds     = safe_int(n.get('date_start'))
        groups[(era, region)].append((ds, nid))

    for key in groups:
        groups[key].sort()

    NODE_SPACING = 220   # px between nodes in same row
    ROW_SPACING  = 200   # px between rows when group wraps

    positions = {}
    for (era, region), items in groups.items():
        count   = len(items)
        cx      = ERA_X.get(era, 3300)
        base_y  = REGION_Y.get(region, DEFAULT_Y)

        # Wrap into 2 rows for groups > 6
        row_size = count if count <= 6 else math.ceil(count / 2)

        total_w = (row_size - 1) * NODE_SPACING
        xs = [cx - total_w / 2 + col * NODE_SPACING for col in range(row_size)]

        for i, (ds, nid) in enumerate(items):
            row = i // row_size
            col = i %  row_size
            positions[nid] = {
                'x': round(xs[col]),
                'y': round(base_y + row * ROW_SPACING),
            }

    return positions

# ── Main build loop ──────────────────────────────────────────
positions = compute_positions(nodes)

all_cyto_nodes = []
all_cyto_edges = []

for nid, n in nodes.items():
    pos  = positions.get(nid, {'x': 0, 'y': 0})
    era  = node_era(nid)
    px_c = pos['x']
    py_c = pos['y']

    # ── Build embedded pioneer objects ────────────────────────
    pids = split_ids(n.get('pioneer_ids', ''))
    pioneer_objs = []
    for pid in pids:
        p       = pioneers.get(pid, {})
        c_match = next((c for c in node_contribs[nid] if c['pioneer_id'] == pid), None)
        raw_bio = p.get('contributions_summary', '')
        bio     = (raw_bio[:400] + '...') if len(raw_bio) > 400 else raw_bio
        pioneer_objs.append({
            'pioneer_id':        pid,
            'name':              p.get('name', pid),
            'nationality':       p.get('nationality', ''),
            'birth_year':        p.get('birth_year', ''),
            'death_year':        p.get('death_year', ''),
            'primary_fields':    p.get('primary_fields', ''),
            'contribution_type': c_match['contribution_type']      if c_match else '',
            'impact_level':      c_match['impact_level']           if c_match else '',
            'specific':          c_match['specific_contribution']  if c_match else '',
            'key_work':          c_match['key_work']               if c_match else '',
            'date':              c_match['date']                   if c_match else '',
            'bio':               bio,
        })

    # ── Build embedded breakthrough objects ───────────────────
    enable_ids    = split_ids(n.get('enabling_breakthrough_ids', ''))
    transform_ids = split_ids(n.get('transforming_breakthrough_ids', ''))
    brkth_objs = []
    for bid, rel in [(b, 'enabled_by') for b in enable_ids] + \
                    [(b, 'transformed_by') for b in transform_ids]:
        b       = brkths.get(bid, {})
        d_match = next((d for d in node_deps[nid] if d['breakthrough_id'] == bid), None)
        brkth_objs.append({
            'breakthrough_id': bid,
            'name':            b.get('name', bid),
            'type':            b.get('type', ''),
            'date':            b.get('date_or_range', ''),
            'relationship':    rel,
            'description':     b.get('description', ''),
            'mechanism':       d_match['mechanism'] if d_match else '',
            'cascading_impact': b.get('cascading_impact', ''),
        })

    # ── Tradition node ─────────────────────────────────────────
    color = ERA_COLOR.get(era, '#888888')
    all_cyto_nodes.append({
        'data': {
            'id':                   nid,
            'label':                n.get('label', ''),
            'era':                  era,
            'region':               n.get('region', ''),
            'color':                color,
            'date_start':           safe_int(n.get('date_start')),
            'date_end':             safe_int(n.get('date_end')),
            'confidence':           n.get('confidence', 'B'),
            'description':          n.get('description', ''),
            'core_idea':            n.get('core_idea', ''),
            'pioneers':             pioneer_objs,
            'breakthroughs':        brkth_objs,
            'controversies':        n.get('controversies', ''),
            'institutional_markers': n.get('institutional_markers', ''),
            'critical_works':       n.get('critical_works', ''),
            'critical_instruments': n.get('critical_instruments', ''),
            'node_type':            'tradition',
        },
        'position': pos,
    })

    # ── Pioneer satellite nodes & edges ───────────────────────
    n_p = len(pioneer_objs)
    for i, p_obj in enumerate(pioneer_objs):
        angle = -math.pi / 2 + i * (2 * math.pi / n_p)
        pid   = p_obj['pioneer_id']
        nat   = p_obj.get('nationality', '')
        all_cyto_nodes.append({
            'data': {
                'id':                f'pion_{pid}_{nid}',
                'node_type':         'pioneer',
                'label':             p_obj['name'],
                'name':              p_obj['name'],
                'nationality':       nat,
                'birth_year':        p_obj.get('birth_year', ''),
                'death_year':        p_obj.get('death_year', ''),
                'primary_fields':    p_obj.get('primary_fields', ''),
                'bio':               p_obj.get('bio', ''),
                'specific':          p_obj.get('specific', ''),
                'key_work':          p_obj.get('key_work', ''),
                'contribution_type': p_obj.get('contribution_type', ''),
                'impact_level':      p_obj.get('impact_level', ''),
                'date':              p_obj.get('date', ''),
                'parent_node':       nid,
                'color':             pioneer_color(nat),
            },
            'position': {
                'x': round(px_c + 120 * math.cos(angle)),
                'y': round(py_c + 120 * math.sin(angle)),
            },
        })
        all_cyto_edges.append({
            'data': {
                'id':        f'ep_{pid}_{nid}',
                'edge_type': 'pioneer',
                'source':    f'pion_{pid}_{nid}',
                'target':    nid,
            }
        })

    # ── Breakthrough satellite nodes & edges ──────────────────
    n_b = len(brkth_objs)
    for i, b_obj in enumerate(brkth_objs):
        angle = math.pi / 4 + i * (2 * math.pi / n_b)
        bid   = b_obj['breakthrough_id']
        btype = b_obj.get('type', 'concept')
        full_b = brkths.get(bid, {})
        all_cyto_nodes.append({
            'data': {
                'id':              f'brkth_{bid}_{nid}',
                'node_type':       'breakthrough',
                'label':           b_obj['name'],
                'name':            b_obj['name'],
                'breakthrough_id': bid,
                'btype':           btype,
                'date':            b_obj.get('date', ''),
                'relationship':    b_obj.get('relationship', ''),
                'description':     b_obj.get('description', ''),
                'mechanism':       b_obj.get('mechanism', ''),
                'impact':          b_obj.get('cascading_impact', ''),
                'pioneers':        full_b.get('pioneers_involved', ''),
                'era':             era,
                'region':          n.get('region', ''),
                'confidence':      full_b.get('confidence', 'B'),
                'primary_node':    nid,
                'parent_node':     nid,
                'color':           BTYPE_COL.get(btype, '#64B5F6'),
            },
            'position': {
                'x': round(px_c + 180 * math.cos(angle)),
                'y': round(py_c + 180 * math.sin(angle)),
            },
        })
        all_cyto_edges.append({
            'data': {
                'id':        f'eb_{bid}_{nid}',
                'edge_type': 'breakthrough',
                'source':    f'brkth_{bid}_{nid}',
                'target':    nid,
            }
        })

# ── Tradition edges ──────────────────────────────────────────
for e in edges_csv:
    all_cyto_edges.append({
        'data': {
            'id':                e['edge_id'],
            'source':            e['from_node'],
            'target':            e['to_node'],
            'relation':          e['relation_type'],
            'label':             e['relation_type'].replace('_', ' '),
            'explanation':       e.get('explanation', ''),
            'pioneers_involved': e.get('pioneers_involved', ''),
            'confidence':        e.get('confidence', 'B'),
            'edge_type':         'tradition',
        }
    })

# ── Serialise ────────────────────────────────────────────────
elements = {'nodes': all_cyto_nodes, 'edges': all_cyto_edges}
elements_json = json.dumps(elements, ensure_ascii=False, separators=(',', ':'))

# ── Patch HTML ───────────────────────────────────────────────
with open(VIZ, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace ELEMENTS const
pattern = r'const ELEMENTS = \{.*?\};'
new_html, count = re.subn(
    pattern,
    f'const ELEMENTS = {elements_json};',
    html, count=1, flags=re.DOTALL
)
if count == 0:
    print("ERROR: Could not find 'const ELEMENTS = {...};' in HTML")
    raise SystemExit(1)

# 2. Update ERA_COL to include EMD / MOD / CON
new_html = re.sub(
    r"const ERA_COL = \{[^}]*\};",
    "const ERA_COL = {ANC:'#FFA726',MED:'#42A5F5',EMD:'#FF7043',MOD:'#9575CD',CON:'#F06292'};",
    new_html,
)

with open(VIZ, 'w', encoding='utf-8') as f:
    f.write(new_html)

# ── Stats ────────────────────────────────────────────────────
n_trad   = sum(1 for nd in all_cyto_nodes if nd['data'].get('node_type') == 'tradition')
n_pion   = sum(1 for nd in all_cyto_nodes if nd['data'].get('node_type') == 'pioneer')
n_brkth  = sum(1 for nd in all_cyto_nodes if nd['data'].get('node_type') == 'breakthrough')
n_t_edge = sum(1 for ed in all_cyto_edges if ed['data'].get('edge_type') == 'tradition')
n_p_edge = sum(1 for ed in all_cyto_edges if ed['data'].get('edge_type') == 'pioneer')
n_b_edge = sum(1 for ed in all_cyto_edges if ed['data'].get('edge_type') == 'breakthrough')

print("Updated viz_interactive_T3.html:")
print(f"  Tradition nodes : {n_trad}")
print(f"  Pioneer nodes   : {n_pion}")
print(f"  Breakthrough nodes: {n_brkth}")
print(f"  Total nodes     : {len(all_cyto_nodes)}")
print(f"  Tradition edges : {n_t_edge}")
print(f"  Pioneer edges   : {n_p_edge}")
print(f"  Breakthrough edges: {n_b_edge}")
print(f"  Total edges     : {len(all_cyto_edges)}")
print(f"  ELEMENTS JSON   : {len(elements_json):,} chars")
