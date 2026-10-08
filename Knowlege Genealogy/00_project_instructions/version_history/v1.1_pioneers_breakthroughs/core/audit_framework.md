# Audit Framework

**Version:** 1.1
**Last Updated:** 2026-05-20
**Status:** Active
**Affected chats:** Historian-Critic (Tier I), Red-Team Reviewer (Tiers II & III), all chats (Macro-Audit sign-off)

## Change Log
- v1.0 (2026-05-20): Initial version — three-tier audit system, gate enforcement, six quantitative metrics with thresholds.
- v1.1 (2026-05-20): Extended to cover pioneers and breakthroughs (per ontology v2.0). Added Micro-Audit Checks #8 and #9; added two failure modes to Phase-Audit §4 (pioneer-orphan nodes, missing enabling breakthroughs); added three new quantitative metrics to Macro-Audit §6 (pioneer coverage, breakthrough coverage, cross-trunk enabler completeness). Trigger: pioneers and breakthroughs were promoted to first-class data objects and need first-class audit coverage. Snapshot of v1.1 changes at `version_history/v1.1_pioneers_breakthroughs/`.

---

Quality control for this project is built into the workflow as a three-tier audit system with enforced gates. This document is canonical. Conflicts between this document and a chat instruction file are resolved in favor of this document.

## 1. The three tiers

| Tier | When it runs | Who owns it | Purpose | Output location |
|------|--------------|-------------|---------|-----------------|
| **Micro-Audit** | After every extraction batch (5–10 nodes) | Historian-Critic chat | Catch issues immediately, before they enter master CSVs | `05_validation/micro_audits/` |
| **Phase-Audit** | At the end of each era layer (ancient, medieval, early modern, modern, contemporary) | Red-Team Reviewer chat | Validate the era as a whole before advancing | `05_validation/phase_audits/` |
| **Macro-Audit** | Before final pilot delivery (and before each subsequent trunk's delivery) | Red-Team Reviewer chat, with sign-off from all 7 chats | Comprehensive quality check; gate to publication | `05_validation/macro_audit/` |

## 2. Gate enforcement

**These gates are hard. Do not bypass.**

- **Gate 1 — Micro-Audit:** Graph Builder may not commit nodes/edges to master CSVs until the Historian-Critic returns a PASS on the batch.
- **Gate 2 — Phase-Audit:** No extraction work may begin on the next era until the Red-Team Reviewer returns PASS on the current era's Phase-Audit.
- **Gate 3 — Macro-Audit:** No deliverable (profile, visualization, export) may be released until the Macro-Audit returns APPROVED FOR DELIVERY.

Gate decisions are recorded in the corresponding audit document and logged in `07_exports/changelog.md`.

## 3. Tier I — Micro-Audit (Historian-Critic)

Runs continuously inside the extraction workflow. The Historian-Critic uses `05_validation/audit_templates/micro_audit_template.md` and writes results to `05_validation/micro_audits/{trunk}_{era}_batch_{N}_audit.md`.

### Checklist (nine checks — v1.1)

1. **Presentism check** — modern field names projected onto ancient practices? If yes, mark in `controversies`.
2. **Founder mythology check** — single pioneers where collective work is more accurate?
3. **Date precision check** — false precision? Does `date_precision` match the evidence?
4. **Confidence inflation check** — do A scores have multiple E2 sources?
5. **Evidence type match check** — E1 only for primary texts; E4 only for institutional records; E6 only for modern taxonomy?
6. **Geographic bias check** — non-European contributions proportional? Transmission routes explicit?
7. **Source completeness check** — every node has `source_ids`; sources diversified; every claim traceable?
8. **Pioneer coverage check** *(v1.1)* — does each node in the batch have at least 3 `pioneer_ids` (or a defensible exception)? Does every cited pioneer have a `pioneers.csv` row with `key_ideas_json` populated? Are pioneer contributions specific (e.g., "formulated three laws of motion in *Principia* 1687") rather than vague (e.g., "worked on mechanics")?
9. **Breakthrough coverage check** *(v1.1)* — does each node have at least 2 `enabling_breakthrough_ids` (or a defensible exception)? For each enabling breakthrough, does the `breakthroughs.csv` row identify pioneers, date, and at least one `fields_enabled` link? For modern/contemporary nodes that depend on cross-trunk enablers (e.g., AI enabled by Trunks 1, 3, 9), are those cross-trunk links explicit?

### Workflow integration

```
1. Extractor produces a batch (5–10 nodes / 8–15 edges)
2. Historian-Critic runs Micro-Audit → returns flagged items
3. Extractor revises flagged items
4. Historian-Critic re-audits → PASS or another revision cycle
5. Graph Builder commits to master CSVs ONLY after PASS
6. Micro-audit document filed in 05_validation/micro_audits/
```

A Micro-Audit document is filed for every batch — even ones that pass on first review. The audit trail is required.

## 4. Tier II — Phase-Audit (Red-Team Reviewer)

Runs once at the end of each era of each trunk. Uses `05_validation/audit_templates/phase_audit_template.md`. Output saved to `05_validation/phase_audits/{trunk}_{era}_phase_audit.md`.

### Checklist categories

1. **Structural integrity** — every node has predecessor connections; no orphans; split/merge events use multiple edges; relation types accurate.
2. **Narrative coherence** — story flows from previous era; no unexplained gaps; no false continuities; dead ends marked.
3. **Cross-validation** — claims appear in 3+ sources; contradictions documented in `disputed_claims.csv`; institutional evidence verified.
4. **Failure mode scan** — explicit checks for presentism, founder mythology, taxonomy bias (using OECD/UNESCO as historical truth), **pioneer-orphan nodes** *(v1.1: nodes with no `pioneer_ids` or only one)*, **missing enabling breakthroughs** *(v1.1: nodes with empty `enabling_breakthrough_ids` despite era and field type suggesting enabling tech/methods existed)*, **missing cross-trunk enabler edges** *(v1.1: contemporary nodes that obviously depend on other-trunk breakthroughs but lack the links — e.g., AI without GPU/transistor/statistics edges)*.
5. **Confidence distribution** — majority B/C; flag if >50% A (overconfident) or >30% D (weak sourcing).
6. **Geographic balance** — region counts computed; for medieval era, Islamic contribution should be substantial; post-medieval >80% European requires justification.
7. **Dispute documentation** — all contested claims in `disputed_claims.csv`; competing interpretations represented; consensus not forced.

### Decision output

The Phase-Audit returns one of:

- **PASS** — Advance to the next era.
- **REVISE** — Fix specific issues, then re-audit. Adds 1–2 days delay.
- **EXPAND** — Coverage is too thin (orphan eras, missing geographic regions). Source Librarian + Extractor add nodes; re-audit. Adds 3–4 days delay.

## 5. Tier III — Macro-Audit (Red-Team Reviewer + all chats)

Runs once per trunk, before final delivery. Uses `05_validation/audit_templates/macro_audit_template.md`. Output saved to `05_validation/macro_audit/{trunk}_macro_audit_report.md`, with companion files `{trunk}_metrics.json` and `{trunk}_sign_off.md`.

### Seven sections of the Macro-Audit

1. **Data integrity** (Graph Builder leads) — schema compliance, referential integrity, completeness.
2. **Historical accuracy** (Historian-Critic leads) — source quality audit, date reliability audit, pioneer attribution audit.
3. **Epistemological rigor** (Red-Team Reviewer leads) — presentism deep scan, false continuity scan, taxonomy bias scan, founder mythology deep scan.
4. **Visualization validation** (Visualization Builder leads) — timeline accuracy, network correctness, Sankey logic, filter functionality.
5. **Documentation completeness** (Source Librarian leads) — bibliography quality, trunk profile completeness, methodology transparency, changelog completeness.
6. **Failure mode final check** (all chats) — sample 30 nodes per failure mode; quantitative scoring against thresholds (see Section 6).
7. **External validation** (optional but recommended) — expert review of 5 most contested claims; cross-chat consistency check.

### Sign-off requirement

`{trunk}_sign_off.md` must contain explicit sign-off from all seven chats:

- Taxonomy Architect — ontology correctly applied
- Source Librarian — sources authoritative and properly cited
- Extractor — extraction follows guidelines
- Historian-Critic — historical accuracy validated
- Graph Builder — data integrity confirmed
- Visualization Builder — visualizations accurate
- Red-Team Reviewer — quality standards met

A missing sign-off blocks delivery.

## 6. Quantitative metrics (mandatory for delivery)

The Macro-Audit computes nine metrics (six original + three v1.1 additions). All values are saved to `{trunk}_metrics.json` for trend analysis across trunks.

| Metric | Definition | Target | Critical | Fail |
|--------|------------|--------|----------|------|
| **Presentism score** | % of ancient/medieval nodes using modern field labels (without controversies flag) | <10% | <15% | ≥15% |
| **Founder mythology score** | % of nodes with single pioneer | <30% | <40% | ≥40% |
| **Taxonomy bias score** | % of nodes where E6 is the only evidence type | 0% | <5% | ≥5% |
| **Source diversity score** | % of nodes with 2+ distinct sources | >90% | >80% | ≤80% |
| **Confidence realism** | B+C combined as % of all nodes | 50–70% | 40–80% | A>50% OR D>40% |
| **Geographic diversity (medieval)** | % of medieval-era nodes with non-European region | >40% | >30% | ≤30% |
| **Pioneer coverage score** *(v1.1)* | % of nodes with ≥3 `pioneer_ids` (or documented exception) | >85% | >70% | ≤70% |
| **Breakthrough coverage score** *(v1.1)* | % of nodes (modern + contemporary eras) with ≥2 `enabling_breakthrough_ids` | >80% | >65% | ≤65% |
| **Cross-trunk enabler completeness** *(v1.1)* | % of contemporary nodes whose `enabling_breakthrough_ids` include at least one breakthrough originating in another trunk | >60% | >40% | ≤40% |

Notes on the new metrics:
- **Pioneer coverage** is computed across all nodes. Ancient first_problem_traditions may legitimately have fewer named pioneers (the historical record is thin) — those count as "documented exceptions" if `controversies` notes the attribution gap.
- **Breakthrough coverage** is restricted to modern + contemporary because pre-modern fields often have no single identifiable enabling technology — they emerged through long traditions. Restricting the denominator avoids unfair pressure on the ancient/medieval layers.
- **Cross-trunk enabler completeness** is the most important v1.1 metric. It directly measures whether the project is representing knowledge as a graph (with cross-trunk edges) rather than as a forest of independent trees. Contemporary AI without GPU + transistor + statistics enablers is the kind of gap this catches.

### Approval rules

- **All six metrics in Target range** → APPROVED FOR DELIVERY.
- **Any metric in Critical range** → CONDITIONAL APPROVAL (deliver with documented limitations).
- **Any metric in Fail range** → REVISE BEFORE DELIVERY.

The metrics are computed by Graph Builder using scripts in `05_validation/audit_templates/` (to be authored as Python helpers once master CSVs exist).

## 7. Output structure

```
05_validation/
├── micro_audits/                           ← per-batch
│   ├── t3_ancient_batch_1_audit.md
│   ├── t3_ancient_batch_2_audit.md
│   └── ...
├── phase_audits/                           ← per-era
│   ├── t3_ancient_phase_audit.md
│   ├── t3_medieval_phase_audit.md
│   └── ...
├── macro_audit/                            ← per-trunk
│   ├── t3_macro_audit_report.md
│   ├── t3_metrics.json
│   └── t3_sign_off.md
├── revision_logs/                          ← what was changed in response to audits
│   ├── t3_ancient_revisions.md
│   └── ...
└── audit_templates/
    ├── micro_audit_template.md
    ├── phase_audit_template.md
    └── macro_audit_template.md
```

Naming convention: lowercase trunk code (`t3`) + era + audit type. Each audit document is named once and updated in place across revision cycles, with cycle markers inside.

## 8. Updated delivery timeline

| Week | Milestone | Audit Gate |
|------|-----------|-----------|
| 2 | Ancient layer | Phase-Audit: Ancient |
| 4 | Medieval layer | Phase-Audit: Medieval |
| 6 | Early Modern | Phase-Audit: Early Modern |
| 8 | Modern | Phase-Audit: Modern |
| 10 | Contemporary | Phase-Audit: Contemporary |
| 11 | Pre-delivery | **MACRO-AUDIT** |
| 12 | Final delivery | Macro-Audit must be APPROVED |

## 9. What changed from the original plan

The original plan had a single end-of-pilot quality audit. This framework replaces that with:

- Three tiers with explicit roles.
- Hard gates between eras and before delivery.
- Quantitative thresholds tied to failure modes (presentism, founder mythology, taxonomy bias).
- Required sign-off from all seven chats.
- Audit documentation as a first-class deliverable, not an afterthought.

Quality control is now built into the process, not bolted on at the end.
