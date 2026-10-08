# Macro-Audit — Trunk {N}

**Owner:** Red-Team Reviewer (orchestrating); all seven chats participate
**Date:** YYYY-MM-DD
**Cycle:** 1 of N
**Trunk scope:** Trunk {N} — {Trunk Name}
**Total nodes:** X across {Y} eras
**Total edges:** Z (intra-trunk: __; cross-trunk: __)
**Total sources:** S

---

## Top-level verdict

`[ ] APPROVED FOR DELIVERY — proceed to final packaging`
`[ ] CONDITIONAL APPROVAL — deliver with documented limitations (see Section 8)`
`[ ] REVISE BEFORE DELIVERY — see revision plan (Section 9)`

---

## Section 1 — Data integrity (Graph Builder leads)

### 1a. Schema compliance
- [ ] All required fields populated in `nodes.csv`
- [ ] All `relation_type` values come from the approved ontology
- [ ] Date format consistent (BCE negative, CE positive, integer years)
- [ ] No duplicate `node_id` or `edge_id`

### 1b. Referential integrity
- [ ] All `from_node` / `to_node` resolve to existing `node_id`
- [ ] All `source_ids` resolve to existing `source_id`
- [ ] All disputed-claim references resolve to `disputed_claims.csv` rows

### 1c. Completeness
- [ ] All 5 event types represented
- [ ] All 10 relation types used at least once *(if applicable to trunk)*
- [ ] All 5 eras covered (where historically applicable)
- [ ] Cross-era edges present

**Section 1 result:** PASS / FAIL — *(notes)*

## Section 2 — Historical accuracy (Historian-Critic leads)

### 2a. Source quality audit
- Total sources: S
- Distribution: E1 __% | E2 __% | E3 __% | E4 __% | E5 __% | E6 __%
- Red flag: E6 > 20% (over-reliance on modern taxonomy)
- Red flag: E1 > 40% (over-reliance on primary texts, needs more interpretation)
- Ideal: E2 should be 40–60%
- **Result:** ...

### 2b. Date reliability audit
- Sampled: 20 random nodes with `date_precision = year`
- Each verified against an institutional event in the cited source(s)
- Failures: __ / 20
- **Result:** ...

### 2c. Pioneer attribution audit
- Sampled: 20 nodes
- Single-name pioneers: __ / 20
- Of these, defensible single-attributions: __
- Non-Western pioneers across sample: __
- **Result:** ...

**Section 2 result:** PASS / FAIL — *(notes)*

## Section 3 — Epistemological rigor (Red-Team Reviewer leads)

### 3a. Presentism deep scan
- Exported all node `label` values for ancient + medieval eras
- Nodes containing "physics," "chemistry," "biology," "science": __
- Of these, with proper retrospection note in `controversies`: __
- **Result:** ...

### 3b. False continuity scan
- Traced 5 random lineages ancient → contemporary
- Edges where retrospective construction (not genuine continuity): __
- **Result:** ...

### 3c. Taxonomy bias scan
- Nodes where E6 is in `evidence_type`: __
- Nodes where E6 is the ONLY evidence type: __
- Target: 0
- **Result:** ...

### 3d. Founder mythology deep scan
- Nodes with confidence A AND single pioneer AND single representative work: __
- For each: do E2 sources support individual credit? Y/N
- **Result:** ...

**Section 3 result:** PASS / FAIL — *(notes)*

## Section 4 — Visualization validation (Visualization Builder leads)

### 4a. Timeline accuracy
- [ ] Node positions match `date_start`
- [ ] Overlapping time periods correctly displayed
- [ ] No backward-in-time edges

### 4b. Network graph
- [ ] All edges rendered
- [ ] Clusters meaningful (related fields grouped)
- [ ] Isolate nodes expected (or missing edges flagged)

### 4c. Sankey flow
- [ ] Flow widths represent meaningful quantity
- [ ] Ancient → contemporary paths traceable
- [ ] Merge events shown as 2 flows → 1

### 4d. Filter functionality
- [ ] Confidence filter works
- [ ] Region filter works
- [ ] Event-type filter works
- [ ] Relation-type filter works

**Section 4 result:** PASS / FAIL — *(notes)*

## Section 5 — Documentation completeness (Source Librarian leads)

### 5a. Bibliography
- [ ] All sources in `sources.csv` have full citations
- [ ] DOI/URL provided where available
- [ ] Evidence types correctly classified
- [ ] Paywalled sources noted

### 5b. Trunk profile
- [ ] `trunk_{N}_profile.md` has all required sections
- [ ] Statistics accurate
- [ ] Key transitions clearly explained
- [ ] Disputed claims documented with competing views

### 5c. Methodology
- [ ] `methodology_note.md` covers: date choices, confidence scoring, geographic decisions, exclusions, known limitations

### 5d. Changelog
- [ ] All commits documented
- [ ] Reasons for changes recorded
- [ ] Validation gate decisions logged

**Section 5 result:** PASS / FAIL — *(notes)*

## Section 6 — Failure mode final check (all chats participate)

Sample sizes: 30 nodes per failure mode, randomly drawn across all eras.

### 6a. Presentism score
- Nodes using modern labels without retrospection: __ / 30 = __%
- Target: <10% | Critical: <15% | Fail: ≥15%
- **Result:** PASS / CONDITIONAL / FAIL

### 6b. Founder mythology score
- Nodes with single-pioneer attribution (not clearly defensible): __ / 30 = __%
- Target: <30% | Critical: <40% | Fail: ≥40%
- **Result:** PASS / CONDITIONAL / FAIL

### 6c. Taxonomy bias score
- Nodes where E6 is the only evidence type: __ / total = __%
- Target: 0% | Critical: <5% | Fail: ≥5%
- **Result:** PASS / CONDITIONAL / FAIL

### 6d. Source diversity score
- Nodes with 2+ distinct sources: __ / total = __%
- Target: >90% | Critical: >80% | Fail: ≤80%
- **Result:** PASS / CONDITIONAL / FAIL

### 6e. Confidence realism
- B+C combined as % of total: __%
- A as % of total: __%
- D as % of total: __%
- Target: B+C = 50–70% | Critical: B+C = 40–80% | Fail: A>50% OR D>40%
- **Result:** PASS / CONDITIONAL / FAIL

### 6f. Geographic diversity (medieval era)
- Medieval-era nodes with non-European region: __ / total medieval = __%
- Target: >40% | Critical: >30% | Fail: ≤30%
- **Result:** PASS / CONDITIONAL / FAIL

### 6g. Pioneer coverage *(v1.1)*
- Nodes with ≥3 `pioneer_ids` (or documented exception): __ / total = __%
- Target: >85% | Critical: >70% | Fail: ≤70%
- **Result:** PASS / CONDITIONAL / FAIL

### 6h. Breakthrough coverage *(v1.1, modern + contemporary nodes only)*
- Modern+contemporary nodes with ≥2 `enabling_breakthrough_ids`: __ / total modern+contemporary = __%
- Target: >80% | Critical: >65% | Fail: ≤65%
- **Result:** PASS / CONDITIONAL / FAIL

### 6i. Cross-trunk enabler completeness *(v1.1, contemporary nodes only)*
- Contemporary nodes whose `enabling_breakthrough_ids` include ≥1 breakthrough from another trunk: __ / total contemporary = __%
- Target: >60% | Critical: >40% | Fail: ≤40%
- **Result:** PASS / CONDITIONAL / FAIL

## Section 7 — External validation *(optional but recommended)*

- [ ] Expert review obtained from a historian of science
- [ ] 5 most controversial claims reviewed; feedback in `disputed_claims.csv`
- [ ] Cross-chat consistency: Extractor reviewed Graph Builder; Historian-Critic reviewed Visualization Builder

---

## Section 8 — Quantitative summary

Saved as companion file `{trunk}_metrics.json`:

```json
{
  "trunk_id": N,
  "audit_date": "YYYY-MM-DD",
  "node_count": X,
  "edge_count": Y,
  "source_count": Z,
  "metrics": {
    "presentism_score":              {"value": 0.00, "status": "PASS"},
    "founder_mythology_score":       {"value": 0.00, "status": "PASS"},
    "taxonomy_bias_score":           {"value": 0.00, "status": "PASS"},
    "source_diversity_score":        {"value": 0.00, "status": "PASS"},
    "confidence_realism_b_plus_c":   {"value": 0.00, "status": "PASS"},
    "geographic_diversity_medieval": {"value": 0.00, "status": "PASS"},
    "pioneer_coverage_score":        {"value": 0.00, "status": "PASS"},
    "breakthrough_coverage_score":   {"value": 0.00, "status": "PASS"},
    "cross_trunk_enabler_score":     {"value": 0.00, "status": "PASS"}
  },
  "evidence_distribution": {
    "E1": 0.00, "E2": 0.00, "E3": 0.00, "E4": 0.00, "E5": 0.00, "E6": 0.00
  },
  "verdict": "APPROVED | CONDITIONAL | REVISE"
}
```

---

## Section 9 — Revision plan *(only if verdict is not APPROVED)*

| Issue | Severity | Owner | Action | Deadline |
|-------|----------|-------|--------|----------|
| ... | high/med/low | chat name | what to do | YYYY-MM-DD |

Re-audit scheduled: YYYY-MM-DD

---

## Section 10 — Sign-offs

Required for delivery. Recorded in `{trunk}_sign_off.md`. Each chat owner signs after reviewing the audit and confirming their domain.

- [ ] Taxonomy Architect — ontology correctly applied
- [ ] Source Librarian — sources authoritative and properly cited
- [ ] Extractor — extraction follows guidelines
- [ ] Historian-Critic — historical accuracy validated
- [ ] Graph Builder — data integrity confirmed
- [ ] Visualization Builder — visualizations accurate
- [ ] Red-Team Reviewer — quality standards met

## Revision cycle log

- **Cycle 1 (YYYY-MM-DD):** Verdict — REVISE.
- **Cycle 2 (YYYY-MM-DD):** Verdict — APPROVED. All issues resolved.
