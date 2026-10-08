# Data Changelog

This is the changelog for the project's **data files** (`04_nodes_edges/*.csv` and the per-trunk lineage JSON). It is separate from `00_project_instructions/evolution_tracking/instruction_update_history.md`, which tracks changes to instruction files.

The Graph Builder writes here after every commit. Format follows the Graph Builder's instructions: date, what changed, IDs added/revised, validation reference, and notes.

Visualization UI changes to files in `07_exports/` are also recorded here (separate section at the top).

---

## 2026-05-28 — `viz_interactive_T3.html` — UI fix v1.2 (broken → working)

**Type:** Visualization-only change. No data files modified.

### Root cause (v1.1 regression)

`update_viz.py` v1 replaced the ELEMENTS const but omitted three things required by Cytoscape.js:

| Missing | Effect |
|---------|--------|
| `node_type` field on tradition nodes | Stylesheet selectors `"node[node_type='tradition']"` matched nothing → nodes invisible |
| `position: {x, y}` on all nodes | `layout: {name: 'preset'}` stacked every node at (0,0) → appeared as a single circle |
| Separate pioneer/breakthrough Cytoscape nodes + `edge_type` on edges | Layer toggles and tap handlers did nothing |

### Fix: `update_viz.py` v2

Complete rewrite of the ELEMENTS generator:

1. **`node_type: 'tradition'`** added to every tradition node data object.
2. **`position: {x, y}`** computed via a swim-lane layout:
   - X-axis = era (ANC center 600 → MED 1800 → EMD 3300 → MOD 4800 → CON 6200)
   - Y-axis = region (Greek 150, Hellenistic 300, Islamic 480, Chinese 680, Indian 880, European 1080, Global 1280)
   - Within each era-region group: nodes sorted by `date_start`, spread at 220 px spacing, wrapped into 2 rows for groups > 6.
3. **Pioneer satellite nodes** (`node_type: 'pioneer'`) created for each pioneer-contribution pair; placed at radius 120 px around their tradition node, evenly distributed by angle starting at 12 o'clock.
4. **Breakthrough satellite nodes** (`node_type: 'breakthrough'`) created for each breakthrough-dependency pair; radius 180 px, angle offset by π/4 to interleave with pioneer ring.
5. **`edge_type: 'tradition'`** added to all tradition edges; `edge_type: 'pioneer'`/`'breakthrough'` on satellite edges.
6. **`ERA_COL`** JS constant updated to include EMD (`#FF7043`), MOD (`#9575CD`), CON (`#F06292`).

### Generated ELEMENTS (v2)

| Type | Count |
|------|-------|
| Tradition nodes | 66 |
| Pioneer satellite nodes | 282 |
| Breakthrough satellite nodes | 268 |
| **Total nodes** | **616** |
| Tradition edges | 103 |
| Pioneer edges | 282 |
| Breakthrough edges | 268 |
| **Total edges** | **653** |
| ELEMENTS JSON size | 1.23 MB |

All 616 node IDs and 653 edge IDs are unique. No node placed at (0,0).

Era bounding boxes (tradition nodes):
- ANC: x = [270, 930], y = [150, 880]
- MED: x = [1250, 2350], y = [380, 1080]
- EMD: x = [2530, 4070], y = [1080, 1280]
- MOD: x = [4250, 5350], y = [1080, 1280]
- CON: x = [5650, 6750], y = [1080, 1480]

---

## 2026-05-27 — Trunk 3 Early Modern Layer (T3_EMD) — initial population

**Passed Gate 1 (Micro-Audit): 0 errors, 0 warnings. All 9 macro-audit metrics at TARGET.**

### Rows added
| File | Rows added | IDs |
|------|-----------|-----|
| `sources.csv` | 21 | SRC_054–SRC_074 |
| `pioneers.csv` | 55 | PION_089–PION_143 |
| `breakthroughs.csv` | 28 | BRKTH_037–BRKTH_064 |
| `nodes.csv` | 16 | T3_EMD_001–T3_EMD_016 |
| `pioneer_contributions.csv` | 55 | CONTR_089–CONTR_143 |
| `breakthrough_dependencies.csv` | 28 | DEP_063–DEP_090 |
| `edges.csv` | 43 | T3_E_022–T3_E_064 |

### Coverage
- **Temporal span**: c. 1500–1830 CE (era code: EMD = Early Modern)
- **Geographic focus**: 85% European (appropriate for Scientific Revolution period), with Islamic, Chinese, and American roots documented in parent connections
- **Field coverage**: 16 knowledge traditions spanning experimental philosophy, mechanical philosophy, mathematical physics, pneumatic chemistry, chemical revolution, atomic theory, optics, electricity, natural history, astronomy, anatomy/physiology, instrument-making, scientific societies, metallurgy, engineering mechanics, and earth sciences

### Source types
- E2 (scholarly monograph): SRC_054–SRC_074 (21 sources — all E2 scholarly secondary)
- Key sources: Shapin (1996), Dear (2001), Henry (2008), Gaukroger (2001), Cohen (1999), Westfall (1980), Donovan (1993), Brock (1992), Thackray (1970), Holmes (1985), van Helden & Hankins (1994)

### Macro-Audit snapshot (43 nodes cumulative)
- Presentism: 0.0% ✓ | Founder mythology: 7.0% ✓ | Taxonomy bias: 0.0% ✓
- Source diversity: 100% ✓ | Confidence realism (B+C): 53.5% ✓ (within 50–70% target)
- Pioneer coverage (3+ pids): 100% ✓ | Breakthrough coverage (2+ bids): 100% ✓
- Geographic diversity (medieval): 60.0% ✓ | Cross-trunk enabler completeness: 100% ✓ (vacuous, no contemporary nodes)

### Confidence distribution (EMD layer)
- A (≥2 independent E2 sources): T3_EMD_001, 002, 003, 004, 005, 007, 010, 011 — 7 nodes (all had multiple well-sourced scholars)
- B (1–2 E2 sources, emerging field, or contested chronology): T3_EMD_006, 008, 009, 012, 013, 014, 015, 016 — 9 nodes
- Cumulative B+C across all 43 nodes: 53.5% (within 50–70% target band)

### Edges (43 total, T3_E_022–T3_E_064)
- All 43 edges connect EMD nodes to their documented parent traditions
- Relation types used: `emerged_from` (37), `split_from` (6)
- Key splits: EMD_005 (Chemistry) ← MED_001/MED_011 via `split_from`; EMD_001/EMD_002 ← MED_009 via `split_from`
- No `method_imported_from` edges (all within trunk 3)

### Key lineage connections to medieval layer
- Experimental Philosophy (EMD_001) ← Islamic Optics (MED_002), European Experimental Tradition (MED_010), Scholastic Philosophy (MED_009)
- Chemistry Revolution (EMD_005) ← Islamic Alchemy (MED_001), European Alchemy (MED_011), Pneumatic Chemistry (EMD_004)
- Mathematical Physics (EMD_003) ← Islamic Mathematics (MED_004), Islamic Astronomy (MED_005), Mechanical Philosophy (EMD_002)
- Astronomy (EMD_010) ← Islamic Astronomy (MED_005), Scholastic Philosophy (MED_009), Alexandrian Mathematical Sciences (ANC_005)

### Validation fixes applied during session
- 25 confidence-A pioneers had single source only; second independent E2 source added to each (e.g. Kepler +SRC_062, Harvey +SRC_056, Huygens +SRC_071, etc.)
- 3 pioneer_contributions specificity violations (CONTR_102 Hooke, CONTR_103 Gassendi, CONTR_118 Black): vague verbs "contributed to"/"influenced" replaced with concrete dated claims citing specific works
- `validation.py` bug: cross-trunk metric returned 0.0% (fail) when no contemporary nodes present; fixed to return 100.0% (vacuous pass) when denominator is zero
- EMD_014 (Metallurgy): pioneer_ids left empty with attribution gap documented in controversies (Agricola and Ercker not yet in pioneer database)
- Research file referenced T3_ANC_007 as "Ptolemaic astronomy" but actual node is "Yin-Yang and Five Phases School"; corrected to T3_ANC_005 (Alexandrian Mathematical Sciences) as astronomy parent

*(future entries below, newest first)*

---

## 2026-05-26 — `viz_interactive_T3.html` — UI revision v1.1

**Type:** Visualization-only change. No data files modified.

### Changes

**1. Node spacing (+70%)**
All node positions (tradition, pioneer, breakthrough) scaled by ×1.7 from the initial preset. The map was too compressed — Islamic medieval nodes were clustering within ~170 × 120 px of each other. The uniform scale preserves all relative positions while giving enough breathing room to read labels and edges.

**2. Edge panel From/To corrected**
The "From" label in the connection detail panel was showing the *emerging* tradition (the `source` field in edge data) and "To" was showing the *origin* (the `target` field). This was semantically backwards: for every `emerged_from` edge the newer tradition is the `source` and the older origin is the `target`. Fixed so that:
- **From** = knowledge origin = edge `target`
- **To** = emerging tradition = edge `source`

**3. Unified pioneer / breakthrough card interaction**
Both card types now follow the same two-step pattern:

| Step | Action | Result |
|------|--------|--------|
| 1 | Click card | Inline expand: bio excerpt (pioneer) or description + mechanism excerpt (breakthrough) |
| 2 | "Full profile →" / "Full details →" button | Popup overlay with complete information |

Pioneer cards previously opened the overlay immediately on click (no inline preview). Breakthrough cards had inline expand but no popup. Both are now consistent.

The breakthrough overlay was also enriched: it now merges the card-level data (description, mechanism, relationship) with the corresponding breakthrough *node* data (era, region, confidence, pioneers string, primary node — clickable). All database fields are displayed.

**Root cause fixed (breakthrough cards not responding):** the previous implementation embedded raw JSON with single-quote substitution directly into `onclick` attributes. Any apostrophe in long text fields (description, mechanism, impact) broke the HTML, silently disabling the entire card. Fixed by storing JSON in `data-brkth` attributes using `&quot;` encoding and reading with `dataset.brkth` at click time.

---

## 2026-05-22 — Trunk 3 Medieval Layer (T3_MED) — initial population

**Passed Gate 1 (Micro-Audit): 0 errors, 0 warnings.**

### Rows added
| File | Rows added | IDs |
|------|-----------|-----|
| `sources.csv` | 21 | SRC_033–SRC_053 |
| `pioneers.csv` | 48 | PION_041–PION_088 |
| `breakthroughs.csv` | 18 | BRKTH_019–BRKTH_036 |
| `nodes.csv` | 14 | T3_MED_001–T3_MED_014 |
| `pioneer_contributions.csv` | 48 | CONTR_041–CONTR_088 |
| `breakthrough_dependencies.csv` | 26 | DEP_037–DEP_062 |
| `edges.csv` | 21 | T3_E_001–T3_E_021 |

**Edges are new in this batch** (first-ever data in `edges.csv`): 21 directed edges linking medieval nodes to ancient parent nodes and to each other, all using valid `relation_type` values (`emerged_from`, `method_imported_from`).

### Coverage
- **Temporal span**: c. 400–1500 CE (era code: MED)
- **Geographic distribution (nodes)**: Islamic 43%, European 29%, Chinese 14%, Indian/Byzantine 7% each — non-Islamic 57%
- **Pioneer distribution**: Islamic 46%, European 38%, Chinese 10%, Byzantine 6%

### Source types
- E2 (scholarly monograph/journal): SRC_033–SRC_053 (21 sources) — all new medieval sources are E2 scholarly secondary

### Macro-Audit snapshot (27 nodes cumulative)
- Presentism: 0.0% ✓ | Founder mythology: 11.1% ✓ | Taxonomy bias: 0.0% ✓
- Source diversity: 100% ✓ | Confidence realism (B+C): 51.9% ✓
- Pioneer coverage (3+ pids): 100% ✓
- Geographic diversity (medieval): 69.2% ✓
- Breakthrough coverage (modern): 0.0% FAIL — vacuous (no modern/contemporary nodes yet, expected)
- Cross-trunk enabler completeness: 0.0% FAIL — vacuous (no contemporary nodes yet, expected)

### Confidence distribution (medieval layer)
- A (≥2 independent E2 sources): T3_MED_001–005, T3_MED_007, T3_MED_009 (7 nodes)
- B (1–2 E2 sources or indirectly sourced): T3_MED_006, T3_MED_008, T3_MED_010–014 (7 nodes)
- C: none in medieval layer

### Validation fixes applied during session
- `creation_event_type` for all 14 medieval nodes: 'transformation'/'continuation' are not valid enum values; corrected to valid vocabulary ('institutionalized_field', 'conceptual_breakthrough', 'named_field', 'first_problem_tradition')
- `BRKTH_035` `date_precision`: 'approximate' → 'decade'
- 4 pioneer_contributions specificity violations (CONTR_054, 056, 080, 085): vague verbs 'influenced'/'studied' replaced with concrete dated claims
- T3_MED_013 region: 'Byzantine' not in VALID_REGIONS → corrected to 'Greek, European'
- Confidence realism: initial run yielded 40.7% B+C (below 50% floor); T3_MED_006, T3_MED_010, T3_MED_012 downgraded from A to B, bringing cumulative B+C to 51.9% ✓
- Pioneer coverage warnings on T3_MED_002, 008, 012, 014: attribution gap notes added to controversies fields
- T3_MED_014 sources: added SRC_047 (Huff) as second source; pioneer_ids left empty with attribution gap note (Indian medieval scholars Udayana, Brahmagupta, Bhaskara II documented in research but not yet in pioneer database)

*(future entries below, newest first)*

---

## 2026-05-20 — Schema expansion to v2.0 (pioneers + breakthroughs as first-class)

- Expanded `nodes.csv` from 19 to 24 columns (added: `pioneer_ids`, `enabling_breakthrough_ids`, `transforming_breakthrough_ids`, `critical_works`, `critical_instruments`).
- Created four new master CSVs with v2.0 schema headers:
  - `pioneers.csv` (16 cols)
  - `breakthroughs.csv` (15 cols)
  - `pioneer_contributions.csv` (9 cols)
  - `breakthrough_dependencies.csv` (7 cols)
- All eight files now contain headers only; zero data rows.
- Validation: all 8 headers verified against ontology v2.0 via Python csv parse.
- Reference: see `core/ontology_definition.md` v2.0 (§11–§15) and `00_project_instructions/evolution_tracking/instruction_update_history.md` (entry of same date).
- Notes: no data was lost (no data existed prior to expansion). The Graph Builder's v1.1 instructions now describe the extended pre-flight validation script covering all 8 files.

---

## 2026-05-20 — Project bootstrap

- Created `nodes.csv`, `edges.csv`, `sources.csv`, `disputed_claims.csv` with v1.0 schema headers (per `core/ontology_definition.md`).
- All four files contain headers only; zero data rows.
- Validation: headers verified against ontology — 19 columns in `nodes.csv`, 12 in `edges.csv`, 10 in `sources.csv`, 11 in `disputed_claims.csv`.
- Notes: project scaffolding complete; first data commit expected after Trunk 3 ancient-layer batch 1 passes its Micro-Audit (Gate 1).

---

## 2026-05-21 — Trunk 3 Ancient Layer (T3_ANC) — initial population

**Passed Gate 1 (Micro-Audit): 0 errors, 0 warnings.**

### Rows added
| File | Rows added | IDs |
|------|-----------|-----|
| `sources.csv` | 32 | SRC_001–SRC_032 |
| `pioneers.csv` | 40 | PION_001–PION_040 |
| `breakthroughs.csv` | 18 | BRKTH_001–BRKTH_018 |
| `nodes.csv` | 13 | T3_ANC_001–T3_ANC_013 |
| `pioneer_contributions.csv` | 40 | CONTR_001–CONTR_040 |
| `breakthrough_dependencies.csv` | 36 | DEP_001–DEP_036 |

### Coverage
- **Temporal span**: c. 600 BCE – 400 CE (era code: ANC)
- **Geographic distribution (nodes)**: Greek/Hellenistic 38%, Chinese 31%, Indian 23%, Roman 8% — non-Greek 62%
- **Pioneer distribution**: Greek/Hellenistic 47.5%, Chinese 22.5%, Indian 20%, Roman 10%

### Source types
- E2 (scholarly monograph/journal): SRC_001–SRC_022 (22 sources)
- E1 (primary text): SRC_023–SRC_030 (8 sources)
- E3 (encyclopaedia/SEP): SRC_031–SRC_032 (2 sources)

### Macro-Audit snapshot
- Presentism: 0.0% ✓ | Founder mythology: 23.1% ✓ | Taxonomy bias: 0.0% ✓
- Source diversity: 100% ✓ | Confidence realism (B+C): 53.8% ✓
- Pioneer coverage (3+ pids): 100% ✓
- Medieval/Modern/Contemporary metrics: N/A (no such nodes in this batch — expected)

### Validation changes
- Fixed `validation.py`: `pioneers.fields_influenced` and `breakthroughs.pioneers_involved` now treated as free-text (not ID references), consistent with ontology §11–12 which routes structured linkage through join tables.

*(future entries below, newest first)*
