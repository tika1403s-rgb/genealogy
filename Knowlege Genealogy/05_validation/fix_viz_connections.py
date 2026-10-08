"""
fix_viz_connections.py — Add forward-connection visibility to the viz.

Changes:
  1. Cytoscape stylesheet: add .ancestor (orange) and .descendant (teal) node styles
     + matching edge classes for ancestor-edge / descendant-edge
  2. Canvas click handler: classify and colour ancestors vs descendants separately
     (clear background tap also clears new classes)
  3. Panel "Connections" section: replace single flat list with two clearly labelled
     sections — "Origins" (what led here) and "Led to" (what came next)
  4. CSS: .conn-past / .conn-future left-border colours in the HTML panel
"""
import os

VIZ = "/Users/shs/Documents/Claude/Projects/Knowlege Genealogy/07_exports/viz_interactive_T3.html"

def replace_once(text, old, new, label):
    if old in text:
        result = text.replace(old, new, 1)
        print(f"  ✓ {label}")
        return result, True
    print(f"  ✗ NOT FOUND: {label}")
    return text, False

with open(VIZ, 'r', encoding='utf-8') as f:
    html = f.read()

ok = []

# ── 1. Cytoscape stylesheet: add ancestor + descendant node/edge classes ──────
OLD_DIMMED = """    { selector: '.dimmed', style: {
      'opacity': 0.18,
    }},
    { selector: '.faded-time', style: {
      'opacity': 0.12,
    }},"""

NEW_DIMMED = """    { selector: '.dimmed', style: {
      'opacity': 0.18,
    }},
    { selector: '.faded-time', style: {
      'opacity': 0.12,
    }},
    { selector: '.ancestor', style: {
      'border-color': '#FFA040', 'border-width': 2.5,
      'background-opacity': 1, 'shadow-blur': 18, 'shadow-color': '#FFA04088',
    }},
    { selector: '.descendant', style: {
      'border-color': '#40E0C0', 'border-width': 2.5,
      'background-opacity': 1, 'shadow-blur': 18, 'shadow-color': '#40E0C088',
    }},
    { selector: ".ancestor-edge", style: {
      'line-color': '#FFA040', 'target-arrow-color': '#FFA040',
      'opacity': 0.85, 'width': 2.5,
    }},
    { selector: ".descendant-edge", style: {
      'line-color': '#40E0C0', 'target-arrow-color': '#40E0C0',
      'opacity': 0.85, 'width': 2.5,
    }},"""

html, r = replace_once(html, OLD_DIMMED, NEW_DIMMED, "Cytoscape ancestor/descendant styles")
ok.append(r)

# ── 2a. Panel CSS: add conn-past / conn-future coloured left borders ───────────
OLD_CONN_CSS = """.conn-item:hover{border-color:#3A7A9C;background:#122030}
.conn-name{color:#B0D0E8}
.conn-rel{font-size:9px;color:#5BA8D0}"""

NEW_CONN_CSS = """.conn-item:hover{border-color:#3A7A9C;background:#122030}
.conn-name{color:#B0D0E8}
.conn-rel{font-size:9px;color:#5BA8D0}
.conn-past{border-left:3px solid #FFA040 !important}
.conn-future{border-left:3px solid #40E0C0 !important}"""

html, r = replace_once(html, OLD_CONN_CSS, NEW_CONN_CSS, "Panel conn-past/conn-future CSS")
ok.append(r)

# ── 2b. Canvas tap handler: classify ancestors vs descendants ─────────────────
OLD_TAP = """cy.on('tap', "node[node_type='tradition']", function(e) {
  const n = e.target;
  cy.nodes().removeClass('highlighted dimmed');
  n.addClass('highlighted');
  // highlight neighbours
  n.neighborhood().nodes().addClass('highlighted');
  n.neighborhood().nodes("node[node_type!='tradition']").addClass('highlighted');
  n.neighborhood().complement(n.neighborhood()).nodes("node[node_type='tradition']").addClass('dimmed');
  openPanel(n.data());
});"""

NEW_TAP = """cy.on('tap', "node[node_type='tradition']", function(e) {
  const n = e.target;
  cy.nodes().removeClass('highlighted dimmed ancestor descendant');
  cy.edges().removeClass('ancestor-edge descendant-edge');
  n.addClass('highlighted');

  // Outgoing: n is the source — targets are ANCESTORS (what this came from)
  const ancEdges  = n.outgoers("edge[edge_type='tradition']");
  const ancNodes  = ancEdges.targets("node[node_type='tradition']");
  ancEdges.addClass('ancestor-edge');
  ancNodes.addClass('ancestor');

  // Incoming: n is the target — sources are DESCENDANTS (what came from this)
  const descEdges = n.incomers("edge[edge_type='tradition']");
  const descNodes = descEdges.sources("node[node_type='tradition']");
  descEdges.addClass('descendant-edge');
  descNodes.addClass('descendant');

  // Satellite nodes of connected tradition nodes stay visible/highlighted
  ancNodes.union(descNodes).union(n)
    .neighborhood().nodes("node[node_type!='tradition']").addClass('highlighted');

  // Dim every other tradition node
  cy.nodes("node[node_type='tradition']").not(n).not(ancNodes).not(descNodes)
    .addClass('dimmed');

  openPanel(n.data());
});"""

html, r = replace_once(html, OLD_TAP, NEW_TAP, "Canvas tap handler with ancestor/descendant classification")
ok.append(r)

# ── 2c. Background tap: clear new classes too ─────────────────────────────────
OLD_BG_TAP = """cy.on('tap', function(e) {
  if(e.target === cy) {
    cy.nodes().removeClass('highlighted dimmed');
    closePanel();
  }
});"""

NEW_BG_TAP = """cy.on('tap', function(e) {
  if(e.target === cy) {
    cy.nodes().removeClass('highlighted dimmed ancestor descendant');
    cy.edges().removeClass('ancestor-edge descendant-edge');
    closePanel();
  }
});"""

html, r = replace_once(html, OLD_BG_TAP, NEW_BG_TAP, "Background tap clears new classes")
ok.append(r)

# ── 3. Panel: replace flat Connections section with two labelled sections ──────
OLD_CONN_PANEL = """  // Connected nodes
  const n = cy.$(`#${d.id}`);
  const outgoing = n.outgoers("edge[edge_type='tradition']");
  const incoming = n.incomers("edge[edge_type='tradition']");
  if(outgoing.length + incoming.length > 0) {
    html += `<div class="panel-section"><h3>Connections</h3><div class="conn-list">`;
    incoming.forEach(e => {
      const src = e.source().data();
      html += `<div class="conn-item" onclick="jumpTo('${src.id}')">
        <span class="conn-name">← ${src.label}</span>
        <span class="conn-rel">${e.data('relation').replace(/_/g,' ')}</span>
      </div>`;
    });
    outgoing.forEach(e => {
      const tgt = e.target().data();
      html += `<div class="conn-item" onclick="jumpTo('${tgt.id}')">
        <span class="conn-name">→ ${tgt.label}</span>
        <span class="conn-rel">${e.data('relation').replace(/_/g,' ')}</span>
      </div>`;
    });
    html += `</div></div>`;
  }"""

NEW_CONN_PANEL = """  // Connected nodes — split into Origins (past) and Led-to (future)
  const n = cy.$(`#${d.id}`);
  const outgoing = n.outgoers("edge[edge_type='tradition']");  // sources ARE this node → targets = ancestors
  const incoming = n.incomers("edge[edge_type='tradition']");  // targets ARE this node → sources = descendants

  // ── Origins: what knowledge / fields directly preceded and enabled this one ──
  if (outgoing.length > 0) {
    html += `<div class="panel-section">
      <h3 style="color:#FFA040">▲ Origins — what led here (${outgoing.length})</h3>
      <div class="conn-list">`;
    outgoing.forEach(e => {
      const tgt = e.target().data();
      const era = tgt.era || '';
      html += `<div class="conn-item conn-past" onclick="jumpTo('${tgt.id}')">
        <span class="conn-name">${tgt.label} <span style="font-size:9px;color:#8A9AAA">[${era}]</span></span>
        <span class="conn-rel">${e.data('relation').replace(/_/g,' ')}</span>
      </div>`;
    });
    html += `</div></div>`;
  }

  // ── Led to: fields, methods, or disciplines that grew out of this one ────────
  if (incoming.length > 0) {
    html += `<div class="panel-section">
      <h3 style="color:#40E0C0">▼ Led to — knowledge and fields that followed (${incoming.length})</h3>
      <div class="conn-list">`;
    incoming.forEach(e => {
      const src = e.source().data();
      const era = src.era || '';
      html += `<div class="conn-item conn-future" onclick="jumpTo('${src.id}')">
        <span class="conn-name">${src.label} <span style="font-size:9px;color:#8A9AAA">[${era}]</span></span>
        <span class="conn-rel">${e.data('relation').replace(/_/g,' ')}</span>
      </div>`;
    });
    html += `</div></div>`;
  }"""

html, r = replace_once(html, OLD_CONN_PANEL, NEW_CONN_PANEL, "Panel connections — Origins / Led-to sections")
ok.append(r)

# ── Write ─────────────────────────────────────────────────────────────────────
if all(ok):
    with open(VIZ, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\n✓ All {len(ok)} patches applied — {os.path.basename(VIZ)} updated ({len(html):,} chars)")
else:
    print(f"\n✗ {ok.count(False)} pattern(s) not found — file NOT written")
    raise SystemExit(1)
