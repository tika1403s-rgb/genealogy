"""
fix_viz_uiux.py — Uniformise pioneer and breakthrough overlay UI/UX.

Changes applied:
  1.  Add shared CSS: .overlay-meta-row, .overlay-contribution,
      #overlay-backdrop, .badge-era-MOD, .badge-era-CON
  2.  Normalise #brkth-overlay border  → #2A5070 (was #2A4A7A)
  3.  Normalise #brkth-overlay-header bg → #0F2235 (was #0E1E30)
  4.  Normalise #brkth-overlay h3 color → #E0F0FF (was #B8D8F0)
  5.  Normalise #pion-overlay border   → #2A5070 (was #2A5A7A)
  6.  Normalise #pion-overlay-header bg → #0F2235 (was #102030)
  7.  Normalise .pioneer-card bg       → #0E1E2E (was #102030)
  8.  Add <div id="overlay-backdrop"> HTML element
  9.  Rewrite showPioneerOverlay(): structured sections, BCE dates, backdrop
  10. Rewrite showBrkthOverlay(): overlay-meta-row, overlay-contribution,
      map highlighting of primary node, backdrop
  11. Update closePionOverlay(): hide backdrop, clear all node/edge classes
  12. Update closeBrkthOverlay(): hide backdrop, clear map highlighting
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

# ── 1. Add shared overlay CSS ─────────────────────────────────────────────────
OLD_TOAST_END = """#toast.show{opacity:1}
</style>"""

NEW_TOAST_END = """#toast.show{opacity:1}
/* overlay shared utilities */
.overlay-meta-row{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:10px}
.overlay-contribution{background:#0E1E2E;border-left:3px solid #5BA8D0;padding:8px 10px;border-radius:4px;color:#B0D0E8;font-size:11px;line-height:1.6}
#overlay-backdrop{position:fixed;inset:0;background:#000000AA;z-index:90;display:none}
#overlay-backdrop.show{display:block}
.badge-era-MOD{border-color:#9575CD;color:#9575CD;background:#1A1040}
.badge-era-CON{border-color:#F06292;color:#F06292;background:#2A0020}
</style>"""

html, r = replace_once(html, OLD_TOAST_END, NEW_TOAST_END, "Add overlay shared CSS")
ok.append(r)

# ── 2. Normalise #brkth-overlay border ───────────────────────────────────────
OLD_BRKTH_BORDER = "  width:380px;max-height:70vh;background:#0D1E30;border:1px solid #2A4A7A;"
NEW_BRKTH_BORDER = "  width:380px;max-height:70vh;background:#0D1E30;border:1px solid #2A5070;"
html, r = replace_once(html, OLD_BRKTH_BORDER, NEW_BRKTH_BORDER, "#brkth-overlay border → #2A5070")
ok.append(r)

# ── 3. Normalise #brkth-overlay-header background ────────────────────────────
OLD_BRKTH_HDR = "  padding:12px 14px;background:#0E1E30;border-bottom:1px solid #1A3045;"
NEW_BRKTH_HDR = "  padding:12px 14px;background:#0F2235;border-bottom:1px solid #1A3045;"
html, r = replace_once(html, OLD_BRKTH_HDR, NEW_BRKTH_HDR, "#brkth-overlay-header bg → #0F2235")
ok.append(r)

# ── 4. Normalise #brkth-overlay h3 color ─────────────────────────────────────
OLD_BRKTH_H3 = "#brkth-overlay h3{font-size:13px;color:#B8D8F0;font-weight:700}"
NEW_BRKTH_H3 = "#brkth-overlay h3{font-size:13px;color:#E0F0FF;font-weight:700}"
html, r = replace_once(html, OLD_BRKTH_H3, NEW_BRKTH_H3, "#brkth-overlay h3 color → #E0F0FF")
ok.append(r)

# ── 5. Normalise #pion-overlay border ────────────────────────────────────────
OLD_PION_BORDER = "  width:380px;max-height:70vh;background:#0D1E30;border:1px solid #2A5A7A;"
NEW_PION_BORDER = "  width:380px;max-height:70vh;background:#0D1E30;border:1px solid #2A5070;"
html, r = replace_once(html, OLD_PION_BORDER, NEW_PION_BORDER, "#pion-overlay border → #2A5070")
ok.append(r)

# ── 6. Normalise #pion-overlay-header background ─────────────────────────────
OLD_PION_HDR = "  padding:12px 14px;background:#102030;border-bottom:1px solid #1A3045;"
NEW_PION_HDR = "  padding:12px 14px;background:#0F2235;border-bottom:1px solid #1A3045;"
html, r = replace_once(html, OLD_PION_HDR, NEW_PION_HDR, "#pion-overlay-header bg → #0F2235")
ok.append(r)

# ── 7. Normalise .pioneer-card background ────────────────────────────────────
OLD_PCARD = """.pioneer-card{
  background:#102030;border:1px solid #1E3A50;border-radius:6px;"""
NEW_PCARD = """.pioneer-card{
  background:#0E1E2E;border:1px solid #1E3A50;border-radius:6px;"""
html, r = replace_once(html, OLD_PCARD, NEW_PCARD, ".pioneer-card bg → #0E1E2E")
ok.append(r)

# ── 8. Add overlay-backdrop HTML element ─────────────────────────────────────
OLD_TOAST_DIV = """<!-- ── TOAST ──────────────────────────────────────────────────────────────── -->
<div id="toast"></div>"""

NEW_TOAST_DIV = """<!-- ── OVERLAY BACKDROP ──────────────────────────────────────────────────── -->
<div id="overlay-backdrop" onclick="closePionOverlay();closeBrkthOverlay()"></div>

<!-- ── TOAST ──────────────────────────────────────────────────────────────── -->
<div id="toast"></div>"""

html, r = replace_once(html, OLD_TOAST_DIV, NEW_TOAST_DIV, "Add #overlay-backdrop HTML element")
ok.append(r)

# ── 9. Rewrite showPioneerOverlay() ──────────────────────────────────────────
OLD_PION_FN = """/* ===== PIONEER OVERLAY ==================================================== */
function showPioneerOverlay(d) {
  document.getElementById('pion-overlay-name').textContent = d.name || d.label || 'Pioneer';
  const body = document.getElementById('pion-overlay-body');
  const birth = d.birth || d.birth_year || '';
  const death = d.death || d.death_year || '';
  const dates = (birth || death) ? `${birth}–${death} CE` : '';
  body.innerHTML = `
    ${dates ? `<p style="color:#7EC8E3;margin-bottom:8px">${dates} · ${d.nationality||''}</p>` : ''}
    ${d.primary_fields ? `<p style="color:#90A8B8;margin-bottom:8px"><b>Fields:</b> ${d.primary_fields}</p>` : ''}
    ${d.bio ? `<p style="margin-bottom:10px">${d.bio}</p>` : ''}
    ${d.specific ? `<div style="background:#102030;border-left:3px solid #5BA8D0;padding:8px;border-radius:4px;color:#B0D0E8;font-size:11px">${d.specific}</div>` : ''}
    ${d.key_work ? `<p style="margin-top:8px;color:#A0C8D8"><b>Key work:</b> <i>${d.key_work}</i></p>` : ''}
    ${d.contribution_type ? `<p style="margin-top:4px;color:#7EC8E3"><b>Contribution type:</b> ${d.contribution_type.replace(/_/g,' ')}</p>` : ''}
  `;

  // Highlight this pioneer's nodes on map
  cy.nodes().removeClass('dimmed highlighted');
  ELEMENTS.nodes.filter(n => n.data.node_type === 'tradition').forEach(n => {
    const hasPion = (n.data.pioneers||[]).some(p => p.name === (d.name||d.label));
    const el = cy.$(`#${n.data.id}`);
    if(hasPion) el.addClass('highlighted');
    else el.addClass('dimmed');
  });

  document.getElementById('pion-overlay').classList.add('show');
}"""

NEW_PION_FN = """/* ===== PIONEER OVERLAY ==================================================== */
function showPioneerOverlay(d) {
  document.getElementById('pion-overlay-name').textContent = d.name || d.label || 'Pioneer';
  const body = document.getElementById('pion-overlay-body');

  // BCE-aware year formatter
  function fmtYear(y) {
    const n = parseInt(y);
    if (!y && y !== 0) return '';
    return n < 0 ? `${Math.abs(n)} BCE` : `${n} CE`;
  }
  const birth = d.birth || d.birth_year || '';
  const death = d.death || d.death_year || '';
  const dateStr = (birth || death)
    ? [fmtYear(birth), fmtYear(death)].filter(Boolean).join(' – ')
    : '';

  let h = '';

  // Meta badges row
  const badges = [];
  if (d.era)
    badges.push(`<span class="badge badge-era-${d.era}">${d.era}</span>`);
  if (d.contribution_type)
    badges.push(`<span class="badge" style="border-color:#5BA8D0;color:#5BA8D0;background:#001020;font-size:9px">${d.contribution_type.replace(/_/g,' ')}</span>`);
  if (d.impact_level)
    badges.push(`<span class="badge" style="border-color:#FFA726;color:#FFA726;background:#2A1A00;font-size:9px">${d.impact_level}</span>`);
  if (badges.length) h += `<div class="overlay-meta-row">${badges.join('')}</div>`;

  // Date · Nationality
  if (dateStr || d.nationality)
    h += `<p style="color:#7EC8E3;margin-bottom:8px">${[dateStr, d.nationality].filter(Boolean).join(' · ')}</p>`;

  // Fields
  if (d.primary_fields)
    h += `<div class="panel-section"><h3>Fields</h3><p>${d.primary_fields}</p></div>`;

  // Key Contribution
  if (d.specific)
    h += `<div class="panel-section"><h3>Key Contribution</h3><div class="overlay-contribution">${d.specific}</div></div>`;

  // Key Work
  if (d.key_work)
    h += `<div class="panel-section"><h3>Key Work</h3><p style="color:#A0C8D8"><i>${d.key_work}</i></p></div>`;

  // Biography
  if (d.bio)
    h += `<div class="panel-section"><h3>Biography</h3><p>${d.bio}</p></div>`;

  body.innerHTML = h;

  // Highlight this pioneer's tradition nodes on map; clear prior classification
  cy.nodes().removeClass('dimmed highlighted ancestor descendant');
  cy.edges().removeClass('ancestor-edge descendant-edge');
  ELEMENTS.nodes.filter(n => n.data.node_type === 'tradition').forEach(n => {
    const hasPion = (n.data.pioneers||[]).some(p => p.name === (d.name||d.label));
    const el = cy.$(`#${n.data.id}`);
    if (hasPion) el.addClass('highlighted');
    else el.addClass('dimmed');
  });

  document.getElementById('overlay-backdrop').classList.add('show');
  document.getElementById('pion-overlay').classList.add('show');
}"""

html, r = replace_once(html, OLD_PION_FN, NEW_PION_FN, "Rewrite showPioneerOverlay()")
ok.append(r)

# ── 10. Rewrite showBrkthOverlay() ───────────────────────────────────────────
OLD_BRKTH_FN = """function showBrkthOverlay(d) {
  // Merge with full node data from ELEMENTS if available
  const nodeData = (ELEMENTS.nodes.find(n =>
    n.data.node_type === 'breakthrough' &&
    (n.data.id === d.breakthrough_id || n.data.id === d.id || n.data.label === d.name)
  ) || {}).data || {};

  const name    = d.name   || d.label  || nodeData.label  || 'Breakthrough';
  const type    = d.type   || d.btype  || nodeData.btype  || '';
  const date    = d.date   || nodeData.date   || '';
  const era     = d.era    || nodeData.era    || '';
  const region  = d.region || nodeData.region || '';
  const conf    = d.confidence || nodeData.confidence || '';
  const rel     = d.relationship || '';
  const desc    = d.description || nodeData.description || '';
  const mech    = d.mechanism   || nodeData.mechanism   || '';
  const impact  = d.impact      || nodeData.impact      || '';
  const pioneers= d.pioneers    || nodeData.pioneers    || '';
  const primary = d.primary_node|| nodeData.primary_node|| '';

  document.getElementById('brkth-overlay-name').textContent = name;
  const body = document.getElementById('brkth-overlay-body');

  let h = '';

  // Meta row
  const metaParts = [type, date, era, region].filter(Boolean);
  if(metaParts.length)
    h += `<p style="color:#42A5F5;font-size:10.5px;margin-bottom:10px">${metaParts.join(' · ')}</p>`;

  // Confidence + relationship badges
  const badges = [];
  if(conf) badges.push(`<span class="badge badge-conf-${conf}" style="font-size:9px">${conf}</span>`);
  if(rel)  badges.push(`<span class="badge" style="border-color:#5BA8D0;color:#5BA8D0;background:#001020;font-size:9px">${rel.replace(/_/g,' ')}</span>`);
  if(badges.length) h += `<div style="display:flex;gap:5px;flex-wrap:wrap;margin-bottom:10px">${badges.join('')}</div>`;

  // Description
  if(desc)
    h += `<div class="panel-section"><h3>Description</h3><p>${desc}</p></div>`;

  // Mechanism
  if(mech)
    h += `<div class="panel-section"><h3>Mechanism</h3>
      <div style="background:#102030;border-left:3px solid #5BA8D0;padding:8px;border-radius:4px;color:#B0D0E8;font-size:11px;line-height:1.5">${mech}</div>
    </div>`;

  // Cascading Impact
  if(impact)
    h += `<div class="panel-section"><h3>Cascading Impact</h3><p style="color:#A8C8A0">${impact}</p></div>`;

  // Pioneers
  if(pioneers)
    h += `<div class="panel-section"><h3>Pioneers Involved</h3><p style="color:#B8C8D0">${pioneers}</p></div>`;

  // Primary node
  if(primary) {
    const pLabel = (ELEMENTS.nodes.find(n => n.data.id === primary) || {data:{label:primary}}).data.label;
    h += `<div class="panel-section"><h3>Primary Node</h3>
      <div class="conn-item" onclick="closeBrkthOverlay();jumpTo('${primary}')" style="cursor:pointer">
        <span class="conn-name">${pLabel}</span>
      </div>
    </div>`;
  }

  body.innerHTML = h;
  document.getElementById('brkth-overlay').classList.add('show');
}"""

NEW_BRKTH_FN = """function showBrkthOverlay(d) {
  // Merge with full node data from ELEMENTS if available
  const nodeData = (ELEMENTS.nodes.find(n =>
    n.data.node_type === 'breakthrough' &&
    (n.data.id === d.breakthrough_id || n.data.id === d.id || n.data.label === d.name)
  ) || {}).data || {};

  const name    = d.name   || d.label  || nodeData.label  || 'Breakthrough';
  const type    = d.type   || d.btype  || nodeData.btype  || '';
  const date    = d.date   || nodeData.date   || '';
  const era     = d.era    || nodeData.era    || '';
  const region  = d.region || nodeData.region || '';
  const conf    = d.confidence || nodeData.confidence || '';
  const rel     = d.relationship || '';
  const desc    = d.description || nodeData.description || '';
  const mech    = d.mechanism   || nodeData.mechanism   || '';
  const impact  = d.impact      || nodeData.impact      || '';
  const pioneers= d.pioneers    || nodeData.pioneers    || '';
  const primary = d.primary_node|| nodeData.primary_node|| '';

  document.getElementById('brkth-overlay-name').textContent = name;
  const body = document.getElementById('brkth-overlay-body');

  let h = '';

  // Meta row: type · date · era · region
  const metaParts = [type, date, era, region].filter(Boolean);
  if (metaParts.length)
    h += `<p style="color:#42A5F5;font-size:10.5px;margin-bottom:8px">${metaParts.join(' · ')}</p>`;

  // Confidence + relationship badges (shared overlay-meta-row class)
  const badges = [];
  if (conf) badges.push(`<span class="badge badge-conf-${conf}" style="font-size:9px">${conf}</span>`);
  if (rel)  badges.push(`<span class="badge" style="border-color:#5BA8D0;color:#5BA8D0;background:#001020;font-size:9px">${rel.replace(/_/g,' ')}</span>`);
  if (badges.length) h += `<div class="overlay-meta-row">${badges.join('')}</div>`;

  // Description
  if (desc)
    h += `<div class="panel-section"><h3>Description</h3><p>${desc}</p></div>`;

  // Mechanism (shared overlay-contribution class)
  if (mech)
    h += `<div class="panel-section"><h3>Mechanism</h3><div class="overlay-contribution">${mech}</div></div>`;

  // Cascading Impact
  if (impact)
    h += `<div class="panel-section"><h3>Cascading Impact</h3><p style="color:#A8C8A0">${impact}</p></div>`;

  // Pioneers
  if (pioneers)
    h += `<div class="panel-section"><h3>Pioneers Involved</h3><p style="color:#B8C8D0">${pioneers}</p></div>`;

  // Primary node
  if (primary) {
    const pLabel = (ELEMENTS.nodes.find(n => n.data.id === primary) || {data:{label:primary}}).data.label;
    h += `<div class="panel-section"><h3>Primary Node</h3>
      <div class="conn-item" onclick="closeBrkthOverlay();jumpTo('${primary}')" style="cursor:pointer">
        <span class="conn-name">${pLabel}</span>
      </div>
    </div>`;
  }

  body.innerHTML = h;

  // Highlight primary tradition node on map; clear prior classification
  if (primary) {
    cy.nodes().removeClass('dimmed highlighted ancestor descendant');
    cy.edges().removeClass('ancestor-edge descendant-edge');
    cy.nodes("node[node_type='tradition']").forEach(n => {
      if (n.id() === primary) n.addClass('highlighted');
      else n.addClass('dimmed');
    });
  }

  document.getElementById('overlay-backdrop').classList.add('show');
  document.getElementById('brkth-overlay').classList.add('show');
}"""

html, r = replace_once(html, OLD_BRKTH_FN, NEW_BRKTH_FN, "Rewrite showBrkthOverlay()")
ok.append(r)

# ── 11. Update closePionOverlay() ────────────────────────────────────────────
OLD_CLOSE_PION = """function closePionOverlay() {
  document.getElementById('pion-overlay').classList.remove('show');
  cy.nodes().removeClass('dimmed highlighted');
}"""

NEW_CLOSE_PION = """function closePionOverlay() {
  document.getElementById('pion-overlay').classList.remove('show');
  document.getElementById('overlay-backdrop').classList.remove('show');
  cy.nodes().removeClass('dimmed highlighted ancestor descendant');
  cy.edges().removeClass('ancestor-edge descendant-edge');
}"""

html, r = replace_once(html, OLD_CLOSE_PION, NEW_CLOSE_PION, "Update closePionOverlay()")
ok.append(r)

# ── 12. Update closeBrkthOverlay() ───────────────────────────────────────────
OLD_CLOSE_BRKTH = """function closeBrkthOverlay() {
  document.getElementById('brkth-overlay').classList.remove('show');
}"""

NEW_CLOSE_BRKTH = """function closeBrkthOverlay() {
  document.getElementById('brkth-overlay').classList.remove('show');
  document.getElementById('overlay-backdrop').classList.remove('show');
  cy.nodes().removeClass('dimmed highlighted ancestor descendant');
  cy.edges().removeClass('ancestor-edge descendant-edge');
}"""

html, r = replace_once(html, OLD_CLOSE_BRKTH, NEW_CLOSE_BRKTH, "Update closeBrkthOverlay()")
ok.append(r)

# ── Write ─────────────────────────────────────────────────────────────────────
if all(ok):
    with open(VIZ, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\n✓ All {len(ok)} patches applied — {os.path.basename(VIZ)} updated ({len(html):,} chars)")
else:
    print(f"\n✗ {ok.count(False)} pattern(s) not found — file NOT written")
    raise SystemExit(1)
