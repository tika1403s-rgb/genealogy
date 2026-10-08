# Phase-Audit — {TRUNK} {ERA}

**Owner:** Red-Team Reviewer
**Date:** YYYY-MM-DD
**Cycle:** 1 of N
**Era scope:** date range covered, e.g. "Ancient (≤500 CE)"
**Nodes in scope:** T{X}_{ERA}_{NNN} through T{X}_{ERA}_{NNN} ({total} nodes)
**Edges in scope:** all edges with at least one endpoint in this era's node set ({total} edges)

---

## Verdict

`[ ] PASS — next era extraction may begin`
`[ ] REVISE — specific issues to fix (1–2 day delay)`
`[ ] EXPAND — coverage too thin; need more sources/nodes (3–4 day delay)`

---

## Section 1 — Structural integrity

- [ ] Every node in this era has predecessor edges (orphan check)
- [ ] No orphan nodes (no connection to previous era, where applicable)
- [ ] Split events have multiple outgoing edges; merge events have multiple incoming edges
- [ ] `relation_type` accurately reflects the historical relationship

**Findings:**
- ...

## Section 2 — Narrative coherence

- [ ] Story flows clearly from previous era
- [ ] No unexplained gaps (a field doesn't appear without precursors)
- [ ] No false continuities (tradition forced to descend from an unrelated ancestor)
- [ ] Dead ends explicitly marked (traditions that don't continue)

**Findings:**
- ...

## Section 3 — Cross-validation

- [ ] All claims appear in 3+ independent sources OR are flagged with lower confidence
- [ ] Contradictory dates across sources logged in `disputed_claims.csv`
- [ ] Institutional evidence (E4) verified against historical records
- [ ] Sample of 5 random claims verified against cited sources

**Sample verification:**

| Claim | Cited source | Verified? | Notes |
|-------|--------------|-----------|-------|
| ... | ... | yes/partial/no | ... |

## Section 4 — Failure mode scan

### Presentism
- Sample 10 random nodes from this era.
- Count using modern category labels without retrospection notes: __ / 10
- Target: ≤1 / 10
- **Result:** PASS / FAIL

### Founder mythology
- Sample 10 random nodes from this era.
- Count with single-pioneer attribution that isn't clearly defensible: __ / 10
- Target: ≤3 / 10
- **Result:** PASS / FAIL

### Taxonomy bias
- Filter nodes/edges where `evidence_type` includes E6.
- Count where E6 is the only evidence type: __
- Target: 0
- **Result:** PASS / FAIL

### Pioneer-orphan nodes *(v1.1)*
- Sample 10 random nodes from this era.
- Count with 0 or 1 `pioneer_ids` and no `controversies` note explaining: __ / 10
- Target: ≤2 / 10
- **Result:** PASS / FAIL

### Missing enabling breakthroughs *(v1.1)*
- For modern/contemporary nodes in this era: count those with empty `enabling_breakthrough_ids`: __
- Target: 0 (or each has a `controversies` justification)
- **Result:** PASS / FAIL

### Missing cross-trunk enablers *(v1.1, contemporary phases only)*
- For each contemporary node, count whether `enabling_breakthrough_ids` includes at least one breakthrough from another trunk.
- % of contemporary nodes with cross-trunk enabler: __%
- Target: >60%
- **Result:** PASS / FLAG / FAIL

## Section 5 — Confidence distribution

| Confidence | Count | % of era |
|------------|-------|----------|
| A | X | X% |
| B | X | X% |
| C | X | X% |
| D | X | X% |

- Expected: majority B + C combined
- Red flag: >50% A → suggests overconfidence; downgrade or add sources
- Red flag: >30% D → suggests weak sourcing; expand bibliography

**Result:** PASS / FLAG / FAIL

## Section 6 — Geographic balance

| Region | Node count | % of era |
|--------|------------|----------|
| Greek | X | X% |
| Islamic | X | X% |
| Chinese | X | X% |
| Indian | X | X% |
| European | X | X% |
| Other | X | X% |

- **Medieval era:** Islamic should be substantial (typically 25–40% of medieval nodes). Current: __%
- **Post-medieval:** If >80% European, justify in `controversies` or add nodes.
- **All eras:** check that transmission edges exist where transmission is well-documented.

**Result:** PASS / FLAG / FAIL

## Section 7 — Dispute documentation

- [ ] All contested claims in this era are recorded in `disputed_claims.csv`
- [ ] Competing interpretations represented fairly (not strawmanned)
- [ ] Consensus not forced where historians disagree

**Disputes opened this era:** DISP_NNN, DISP_NNN, ...

---

## Summary

- Total nodes in era: X
- Total edges in era (within + crossing from prior era): Y
- Sources cited (new this era): Z
- Failure mode pass/fail summary: presentism __; founder mythology __; taxonomy bias __
- Confidence distribution OK? Y/N
- Geographic balance OK? Y/N

## Action items

If verdict is REVISE:
1. Item — owner — deadline
2. ...

If verdict is EXPAND:
- Source Librarian: find sources for ... (specific gap)
- Extractor: add nodes for ... (specific topic)

## Revision cycle log

- **Cycle 1 (YYYY-MM-DD):** Verdict — REVISE. Issues listed above.
- **Cycle 2 (YYYY-MM-DD):** Verdict — PASS. All issues addressed.
