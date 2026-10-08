"""
Fix remaining validation errors (round 2):
 1. nodes.csv: remove 'founder'/'founded by' from T3_MOD_008 description
 2. nodes.csv: downgrade confidence A → B for nodes with <2 independent E2 sources
 3. pioneer_contributions.csv: fix CONTR_226 remaining 'contributed to' language
"""
import csv, os, re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

# E2 source IDs (from sources.csv)
E2_SOURCES = (
    {f'SRC_{i:03d}' for i in range(1, 75)} |  # pre-existing sources (all E2)
    {'SRC_075','SRC_076','SRC_077','SRC_078','SRC_079','SRC_080',
     'SRC_081','SRC_082','SRC_083','SRC_084','SRC_085','SRC_086',
     'SRC_087','SRC_088','SRC_089','SRC_090','SRC_091','SRC_092',
     'SRC_093','SRC_094','SRC_095','SRC_097','SRC_098','SRC_099',
     'SRC_100','SRC_102','SRC_103','SRC_104'}
    # SRC_096 and SRC_101 are E4, excluded above
)

def rewrite_csv(fname, transform_fn):
    path = os.path.join(BASE, fname)
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    changed = 0
    new_rows = []
    for row in rows:
        orig = dict(row)
        row = transform_fn(row)
        if row != orig:
            changed += 1
        new_rows.append(row)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(new_rows)
    print(f"  {fname}: {changed} rows modified")

# ── 1 & 2. Fix nodes.csv ──────────────────────────────────────────────────────

def fix_nodes(row):
    nid = row['node_id']

    # Fix founder mythology in T3_MOD_008
    if nid == 'T3_MOD_008':
        desc = row.get('description', '')
        desc = desc.replace('founding nuclear physics as a sub-discipline', 'establishing nuclear physics as a sub-discipline')
        desc = desc.replace('founded', 'established')
        desc = desc.replace('founder', 'pioneer')
        row['description'] = desc

    # Downgrade confidence A → B for MOD/CON nodes with <2 E2 sources
    if nid.startswith('T3_MOD_') or nid.startswith('T3_CON_'):
        if row.get('confidence') == 'A':
            src_ids = [s.strip() for s in row.get('source_ids', '').split(',') if s.strip()]
            e2_count = sum(1 for s in src_ids if s in E2_SOURCES)
            if e2_count < 2:
                row['confidence'] = 'B'

    return row

# ── 3. Fix CONTR_226 in pioneer_contributions.csv ────────────────────────────

def fix_contributions(row):
    if row['contribution_id'] == 'CONTR_226':
        # Remove 'contributed to' phrasing entirely, keep strong specific claim
        row['specific_contribution'] = (
            'Co-discovered C60 buckminsterfullerene (1985) with Smalley and Kroto using supersonic molecular beam '
            'laser vaporisation of graphite; Nobel Chemistry 1996; established carbon cluster spectroscopy method; '
            'characterised formation mechanisms of carbon nanostructure cages'
        )
    return row

# ── Run ───────────────────────────────────────────────────────────────────────

print("Running validation fixes (round 2)...")
rewrite_csv('nodes.csv', fix_nodes)
rewrite_csv('pioneer_contributions.csv', fix_contributions)
print("Done.")
