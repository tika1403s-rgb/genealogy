"""
fix_viz_filters.py — Patch viz_interactive_T3.html to fix all filter bugs.

Problems fixed:
  1. Era filter missing Modern and Contemporary buttons
  2. Time slider max=1500 permanently hides all MOD/CON nodes (date_start > 1500)
  3. timeYear defaults to 1500 — same effect even when no slider interaction
  4. applyFilters() doesn't cascade hide/show to pioneer/breakthrough satellites
  5. Missing "Global" region filter button (all CON nodes have region=Global)
"""
import re, os

VIZ = "/Users/shs/Documents/Claude/Projects/Knowlege Genealogy/07_exports/viz_interactive_T3.html"

def replace_once(text, old, new):
    """Return (new_text, count) — count is 1 if replaced, 0 if not found."""
    if old in text:
        return text.replace(old, new, 1), 1
    return text, 0

with open(VIZ, 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

# ────────────────────────────────────────────────────────────────────
# 1. Add MOD and CON era buttons (after EMD button)
# ────────────────────────────────────────────────────────────────────
old_era = (
    '    <button class="filter-btn" data-filter="era" data-val="EMD">Early Modern</button>\n'
    '  </div>'
)
new_era = (
    '    <button class="filter-btn" data-filter="era" data-val="EMD">Early Modern</button>\n'
    '    <button class="filter-btn" data-filter="era" data-val="MOD">Modern</button>\n'
    '    <button class="filter-btn" data-filter="era" data-val="CON">Contemporary</button>\n'
    '  </div>'
)
html, n1 = replace_once(html, old_era, new_era)
print(f"  Era buttons:   {'✓ added MOD+CON' if n1 else '✗ pattern not found'}")

# ────────────────────────────────────────────────────────────────────
# 2. Add "Global" region filter button (after European)
# ────────────────────────────────────────────────────────────────────
old_region = (
    '    <button class="filter-btn" style="color:#9B70C8" data-filter="region" data-val="European">European</button>\n'
    '  </div>'
)
new_region = (
    '    <button class="filter-btn" style="color:#9B70C8" data-filter="region" data-val="European">European</button>\n'
    '    <button class="filter-btn" style="color:#4ABFBF" data-filter="region" data-val="Global">Global</button>\n'
    '  </div>'
)
html, n2 = replace_once(html, old_region, new_region)
print(f"  Global button: {'✓ added' if n2 else '✗ pattern not found'}")

# ────────────────────────────────────────────────────────────────────
# 3. Fix time slider: extend max to 2025, default to 2025
# ────────────────────────────────────────────────────────────────────
old_slider = 'min="-600" max="1500" value="1500" step="10"'
new_slider = 'min="-600" max="2025" value="2025" step="10"'
html, n3 = replace_once(html, old_slider, new_slider)
print(f"  Time slider:   {'✓ max+default → 2025' if n3 else '✗ pattern not found'}")

# ────────────────────────────────────────────────────────────────────
# 4. Fix timeYear default (1500 → 9999 sentinel = "all time")
# ────────────────────────────────────────────────────────────────────
old_ty = 'let timeYear = 1500;'
new_ty = 'let timeYear = 9999;  // 9999 = sentinel for "all time" (slider at max)'
html, n4 = replace_once(html, old_ty, new_ty)
print(f"  timeYear init: {'✓ 1500 → 9999 (all-time sentinel)' if n4 else '✗ pattern not found'}")

# ────────────────────────────────────────────────────────────────────
# 5. Replace the full applyFilters() + onTimeSlide() + resetTime()
#    block with a corrected version that:
#      a) Only applies time filter when slider < 2025 (not at sentinel 9999)
#      b) Cascades satellite visibility from parent tradition node
# ────────────────────────────────────────────────────────────────────
old_filter_block = '''\
function applyFilters() {
  cy.nodes("node[node_type='tradition']").forEach(n => {
    const d = n.data();
    let show = true;
    if(activeFilters.era !== 'ALL' && d.era !== activeFilters.era) show = false;
    if(activeFilters.region !== 'ALL') {
      const reg = d.region || '';
      if(!reg.includes(activeFilters.region)) show = false;
    }
    if(activeFilters.conf !== 'ALL' && d.confidence !== activeFilters.conf) show = false;
    // time filter
    if(d.date_start > timeYear) show = false;
    n.style('display', show ? 'element' : 'none');
    n.style('opacity', show ? 1 : 0);
  });
  // hide edges whose endpoints are hidden
  cy.edges("edge[edge_type='tradition']").forEach(e => {
    const sv = e.source().style('display'), tv = e.target().style('display');
    e.style('display', sv === 'none' || tv === 'none' ? 'none' : 'element');
  });
}

/* ===== TIME SLIDER ======================================================== */
function onTimeSlide(val) {
  timeYear = parseInt(val);
  const lbl = timeYear < 0 ? `${Math.abs(timeYear)} BCE` : `${timeYear} CE`;
  document.getElementById('time-display').textContent = lbl;
  applyFilters();
}
function resetTime() {
  timeYear = 1500;
  document.getElementById('time-slider').value = 1500;
  document.getElementById('time-display').textContent = 'All time';
  applyFilters();
}'''

new_filter_block = '''\
function applyFilters() {
  // ── 1. Determine tradition-node visibility ──────────────────────────
  cy.nodes("node[node_type='tradition']").forEach(n => {
    const d = n.data();
    let show = true;
    if (activeFilters.era !== 'ALL' && d.era !== activeFilters.era) show = false;
    if (activeFilters.region !== 'ALL') {
      const reg = d.region || '';
      if (!reg.includes(activeFilters.region)) show = false;
    }
    if (activeFilters.conf !== 'ALL' && d.confidence !== activeFilters.conf) show = false;
    // Time filter: only active when slider is below the "all time" sentinel
    if (timeYear < 9999 && d.date_start > timeYear) show = false;
    n.style('display', show ? 'element' : 'none');
    n.style('opacity', show ? 1 : 0);
  });

  // ── 2. Tradition edges follow their endpoints ───────────────────────
  cy.edges("edge[edge_type='tradition']").forEach(e => {
    const sv = e.source().style('display'), tv = e.target().style('display');
    e.style('display', (sv === 'none' || tv === 'none') ? 'none' : 'element');
  });

  // ── 3. Satellite nodes/edges follow their parent tradition node ──────
  ['pioneer', 'breakthrough'].forEach(type => {
    if (!layerState[type]) return;   // layer is off — leave as-is
    cy.nodes(`node[node_type='${type}']`).forEach(n => {
      const parent = cy.getElementById(n.data('parent_node'));
      const parentVisible = parent.length > 0 && parent.style('display') !== 'none';
      n.style('display', parentVisible ? 'element' : 'none');
    });
    cy.edges(`edge[edge_type='${type}']`).forEach(e => {
      const sv = e.source().style('display'), tv = e.target().style('display');
      e.style('display', (sv === 'none' || tv === 'none') ? 'none' : 'element');
    });
  });
}

/* ===== TIME SLIDER ======================================================== */
function onTimeSlide(val) {
  const v = parseInt(val);
  if (v >= 2025) {
    timeYear = 9999;  // sentinel = no time restriction
    document.getElementById('time-display').textContent = 'All time';
  } else {
    timeYear = v;
    document.getElementById('time-display').textContent =
      timeYear < 0 ? `${Math.abs(timeYear)} BCE` : `${timeYear} CE`;
  }
  applyFilters();
}
function resetTime() {
  timeYear = 9999;
  document.getElementById('time-slider').value = 2025;
  document.getElementById('time-display').textContent = 'All time';
  applyFilters();
}'''

html, n5 = replace_once(html, old_filter_block, new_filter_block)
print(f"  applyFilters:  {'✓ replaced with fixed version' if n5 else '✗ pattern not found'}")

# ────────────────────────────────────────────────────────────────────
# Write patched file
# ────────────────────────────────────────────────────────────────────
if all([n1, n2, n3, n4, n5]):
    with open(VIZ, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\nPatched {os.path.basename(VIZ)} successfully ({len(html):,} chars, was {original_len:,})")
else:
    print("\nERROR: one or more patterns not found — file NOT written")
    raise SystemExit(1)
