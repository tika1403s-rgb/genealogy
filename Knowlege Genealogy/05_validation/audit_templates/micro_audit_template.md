# Micro-Audit — {TRUNK} {ERA} Batch {N}

**Owner:** Historian-Critic
**Date:** YYYY-MM-DD
**Cycle:** 1 of N
**Batch contents:** Nodes T{X}_{ERA}_{NNN} through T{X}_{ERA}_{NNN}; Edges T{X}_E_{NNN} through T{X}_E_{NNN}
**Source set referenced:** SRC_{NNN}, SRC_{NNN}, ...

---

## Verdict

`[ ] PASS — Graph Builder may commit`
`[ ] REVISE — see issues below; return to Extractor`

---

## Check 1 — Presentism

For each node/edge in this batch, ask: *Would practitioners of this era recognize this label?* If no → must be marked retrospective in `controversies`.

- [ ] No modern field names projected onto ancient practices
- [ ] All retrospective labels flagged in `controversies` field

**Flags:**
- *(node_id) — issue — recommendation*

## Check 2 — Founder mythology

- [ ] All nodes have ≥3 pioneers OR single pioneer is genuinely defensible
- [ ] No "founded by X" language; uses "associated pioneers"
- [ ] Revolutionary claims tempered (revolutions are collective/gradual)

**Flags:**
- *(node_id) — issue — recommendation*

## Check 3 — Date precision

- [ ] `date_precision = year` only used where an institutional/publication event justifies it
- [ ] Gradual transitions use date ranges (start + end)
- [ ] No precision tighter than the evidence supports

**Flags:**
- *(node_id) — issue — recommendation*

## Check 4 — Confidence inflation

- [ ] Every `A` confidence backed by ≥2 independent E2 sources (ideally + E4)
- [ ] Contested claims downgraded to B or C
- [ ] Uncertainties noted in `controversies`

**Flags:**
- *(node_id) — issue — recommendation*

## Check 5 — Evidence type match

- [ ] E1 used only for primary texts
- [ ] E2 used for scholarly historical sources
- [ ] E3 (encyclopedias) not misclassified as E2
- [ ] E4 used only for institutional records
- [ ] E6 used sparingly (modern taxonomy reference only)

**Flags:**
- *(node_id or edge_id) — issue — recommendation*

## Check 6 — Geographic bias

- [ ] Non-European traditions represented where era allows
- [ ] Transmission routes documented as explicit edges (not implied)
- [ ] No Eurocentric framing of non-European work as "parallel" or "precursor"

**Flags:**
- *(node_id or edge_id) — issue — recommendation*

## Check 7 — Source completeness

- [ ] Every node has at least one `source_ids` entry
- [ ] Sources are diversified (not all from same reference work)
- [ ] Primary sources balanced with scholarly interpretation
- [ ] Every claim is traceable to a cited source

**Flags:**
- *(node_id or edge_id) — issue — recommendation*

## Check 8 — Pioneer coverage *(v1.1)*

- [ ] Every node has ≥3 `pioneer_ids` OR `controversies` documents why fewer
- [ ] Every cited pioneer has a row in `pioneers.csv` with `key_ideas_json` populated
- [ ] Every `pioneer_contributions` row has a specific, dated contribution (not "worked on X")
- [ ] Pioneers already in `pioneers.csv` are referenced by ID, not duplicated
- [ ] Attribution disputes flagged in `controversies`
- [ ] Non-Western pioneers represented where the historical record supports it

**Flags:**
- *(node_id or pioneer_id) — issue — recommendation*

## Check 9 — Breakthrough coverage *(v1.1)*

- [ ] Every modern/contemporary node has ≥2 `enabling_breakthrough_ids`
- [ ] Every cited breakthrough has a row in `breakthroughs.csv` with `pioneers_involved`, `date_or_range`, and at least one of `fields_enabled` / `fields_transformed`
- [ ] Breakthrough cascades are date-consistent (an enabling factor predates its dependent)
- [ ] Contemporary nodes include at least one cross-trunk enabler where the historical record supports it
- [ ] Every `breakthrough_dependencies.mechanism` field is genuinely explanatory (1–3 sentences, not a tautology)

**Flags:**
- *(node_id or breakthrough_id) — issue — recommendation*

---

## Summary

- Items reviewed: X nodes, Y edges
- Items accepted as-is: A
- Items needing revision: B
- Items needing rejection or major rework: C
- Most common issue this batch: ...
- Pattern flag (if any): ... *(e.g., "Extractor is over-using `emerged_from` where `mathematized_by` is correct")*

## Revision cycle log

- **Cycle 1 (YYYY-MM-DD):** Verdict REVISE. X items flagged.
- **Cycle 2 (YYYY-MM-DD):** Verdict PASS. Y items revised; revisions verified.
