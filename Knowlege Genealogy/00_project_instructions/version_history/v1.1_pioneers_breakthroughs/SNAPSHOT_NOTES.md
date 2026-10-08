# Snapshot: v1.1_pioneers_breakthroughs

**Date:** 2026-05-20
**Trigger:** User feedback addressing the "Gap Identified: Pioneers, Ideas, and Enabling Factors" — pioneers and breakthroughs promoted to first-class data objects.
**Snapshotted by:** Instruction Curator (per `chat_specific/instruction_curator_instructions.md` major-bump snapshot rule).

## What this snapshot contains

Frozen copies of every instruction, evolving-rule, and audit-template file that changed in the v1.1 update. The unchanged files are not duplicated here — they remain as snapshotted in `v1.0_initial/`.

**Core (3 files):**
- `ontology_definition.md` — **v2.0** (the only file with a major bump in this round; added §11 Pioneer Schema, §12 Breakthrough Schema, §13 Pioneer Contributions, §14 Breakthrough Dependencies, §15 ID conventions across all entity types; added 4 new edge relation types in §4b; expanded node schema in §2 with 5 new fields)
- `audit_framework.md` — v1.1 (added Micro-Audit Checks #8–#9; Phase-Audit failure-mode scans; 3 new Macro-Audit metrics)
- `trunk_definitions.md` — v1.1 (added cross-trunk breakthrough enabler patterns section)

**Chat-specific (6 files at v1.1):**
- `extractor_instructions.md` (largest change — extraction now produces 6 JSON arrays)
- `graph_builder_instructions.md` (8 master CSVs; extended validator)
- `source_librarian_instructions.md` (biographical + history-of-tech source targets)
- `historian_critic_instructions.md` (added §8 and §9 to its checklist)
- `visualization_builder_instructions.md` (added pioneer, breakthrough, comprehensive views)
- `red_team_reviewer_instructions.md` (9 metrics instead of 6)

**Evolving rules (2 files at v1.1):**
- `always_do_this.md` (added rules 11–15)
- `never_do_this.md` (added prohibitions 13–16)

**Audit templates (all 3, extended):**
- `micro_audit_template.md` (added Checks 8 and 9)
- `phase_audit_template.md` (added pioneer-orphan, missing-enabler, cross-trunk-enabler scans)
- `macro_audit_template.md` (added §6g–§6i and three metric JSON fields)

## What this snapshot does NOT contain

- Files unchanged in v1.1: `project_charter.md`, `quality_guidelines.md`, `workflow_procedures.md`, `taxonomy_architect_instructions.md`, `instruction_curator_instructions.md`, `common_mistakes.md`, `best_practices.md`. Their v1.0 snapshots in `v1.0_initial/` remain authoritative.
- Evolution tracking files (running logs).
- Master data CSVs (their schema is captured in `ontology_definition.md` v2.0; the empty files in `04_nodes_edges/` carry the v2.0 headers).

## Master data files added in v1.1

(For reference — these live in `04_nodes_edges/`, not in this snapshot.)

- `pioneers.csv` — 16 columns, per ontology §11
- `breakthroughs.csv` — 15 columns, per ontology §12
- `pioneer_contributions.csv` — 9 columns, per ontology §13
- `breakthrough_dependencies.csv` — 7 columns, per ontology §14
- `nodes.csv` — expanded from 19 to 24 columns (added `pioneer_ids`, `enabling_breakthrough_ids`, `transforming_breakthrough_ids`, `critical_works`, `critical_instruments`)

## How to compare v1.0 vs v1.1 for any file

```
diff version_history/v1.0_initial/core/ontology_definition.md \
     version_history/v1.1_pioneers_breakthroughs/core/ontology_definition.md
```

## When the next snapshot will happen

The expected next snapshot is `v2.0_trunk_3_complete/` — produced by the Instruction Curator when Trunk 3's Macro-Audit returns APPROVED FOR DELIVERY. That snapshot will incorporate any further mid-pilot revisions (e.g., new rules added to `always_do_this.md`, common mistakes identified during execution, best practices discovered).
