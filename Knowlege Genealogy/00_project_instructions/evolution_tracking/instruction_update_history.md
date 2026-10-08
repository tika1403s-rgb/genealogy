# Instruction Update History

**Owner:** Instruction Curator
**Status:** Active changelog (instruction files only — separate from `07_exports/changelog.md`, which tracks data changes)
**Last updated:** 2026-05-20

---

Chronological record of every change to an instruction file. Each entry lists the file, the version bump, the trigger, and the rationale.

## Entry format

```markdown
### YYYY-MM-DD — [file_path] v{old} → v{new}
**Trigger:** {user feedback | micro-audit pattern | phase-audit finding | macro-audit finding | process discovery | taxonomy architect change}
**Change:** [what was added/modified/removed]
**Rationale:** [why]
**Affected chats:** [list]
**Snapshot:** [if major version bump: link to version_history/ snapshot folder]
```

---

### 2026-05-20 — project bootstrap, all instruction files at v1.0
**Trigger:** initial scaffolding
**Change:** all instruction and rule files created at v1.0.
**Rationale:** establish baseline; subsequent updates begin from here.
**Affected chats:** all
**Snapshot:** `version_history/v1.0_initial/`

---

### 2026-05-20 — Pioneers + Breakthroughs as first-class entities (v1.1 across multiple files)
**Trigger:** user feedback ("Include the following in the plan for the Gap Identified: Pioneers, Ideas, and Enabling Factors") — see `user_feedback_log.md` entry of same date.
**Change:** the v1.0 ontology represented fields and node-to-node relations well, but did not give first-class structure to (1) the *people* whose ideas shaped fields, or (2) the *enabling discoveries* (transistor, statistics, neural-net model, GPU, etc.) that made fields possible. Two new first-class entity types added (pioneers, breakthroughs) plus two join tables (pioneer_contributions, breakthrough_dependencies). Four new edge relation types added (`contributed_by`, `enabled_by`, `transformed_by`, `contributed_to`). Audit framework gained three new quantitative metrics (pioneer coverage, breakthrough coverage, cross-trunk enabler completeness). The "AI without listing statistics + transistor + GPU enablers" coverage gap is the canonical failure case the new audit metrics catch.

**File-by-file changes:**
- `core/ontology_definition.md`: v1.0 → **v2.0** (major bump — fundamental data-model expansion; added §11–§15)
- `core/audit_framework.md`: v1.0 → v1.1 (added Micro-Audit Checks #8–#9; Phase-Audit failure-mode additions; three new Macro-Audit metrics)
- `core/trunk_definitions.md`: v1.0 → v1.1 (added cross-trunk breakthrough enabler patterns; v1.1 extraction scope note)
- `chat_specific/extractor_instructions.md`: v1.0 → v1.1 (extraction now produces 6 JSON arrays; pioneer + breakthrough extraction rules; example sketches)
- `chat_specific/graph_builder_instructions.md`: v1.0 → v1.1 (maintains 8 master CSVs; extended validation script; commit ordering)
- `chat_specific/source_librarian_instructions.md`: v1.0 → v1.1 (biographical + history-of-technology source targets; cross-trunk source flagging)
- `chat_specific/historian_critic_instructions.md`: v1.0 → v1.1 (added §8 pioneer coverage check, §9 breakthrough coverage check)
- `chat_specific/red_team_reviewer_instructions.md`: v1.0 → v1.1 (extended quantitative metric thresholds table from 6 to 9)
- `chat_specific/visualization_builder_instructions.md`: v1.0 → v1.1 (added pioneer view, breakthrough timeline, comprehensive view specs)
- `evolving_rules/always_do_this.md`: v1.0 → v1.1 (added rules 11–15)
- `evolving_rules/never_do_this.md`: v1.0 → v1.1 (added prohibitions 13–16)
- `05_validation/audit_templates/micro_audit_template.md`: added Checks 8 and 9
- `05_validation/audit_templates/phase_audit_template.md`: added pioneer-orphan, missing-enabler, cross-trunk-enabler scans
- `05_validation/audit_templates/macro_audit_template.md`: added §6g–§6i and 3 new metric JSON fields

**Files unchanged at v1.0:** project_charter, quality_guidelines, workflow_procedures, taxonomy_architect_instructions, instruction_curator_instructions, common_mistakes, best_practices, all evolution_tracking files (they accept the changes via their schema).

**Affected chats:** all 8 (with Extractor, Graph Builder, Historian-Critic, Red-Team Reviewer, Visualization Builder, Source Librarian receiving instruction updates; Taxonomy Architect and Instruction Curator unchanged but should review).

**Master data files added:** `04_nodes_edges/pioneers.csv` (16 cols), `breakthroughs.csv` (15 cols), `pioneer_contributions.csv` (9 cols), `breakthrough_dependencies.csv` (7 cols). `nodes.csv` expanded from 19 to 24 columns.

**Snapshot:** `version_history/v1.1_pioneers_breakthroughs/`

---

### 2026-05-26 — `chat_specific/visualization_builder_instructions.md` v1.1 → v1.2
**Trigger:** user feedback (three UI change requests on `viz_interactive_T3.html` — see `user_feedback_log.md` entries of same date).
**Change:** expanded "Required interactivity" section with three new locked-in patterns:
1. **Two-step card interaction** — pioneer and breakthrough cards must use inline expand on first click + popup overlay on "Full profile / Full details" button. Rule also specifies what each overlay must contain (pioneer overlay fields; breakthrough overlay must merge card data with node data and show all fields including primary node as a clickable jump link).
2. **Edge direction labeling** — "From" = knowledge origin (edge `target`); "To" = emerging tradition (edge `source`). Explicit note that semantic direction ≠ raw field names for `emerged_from` / `method_imported_from` relations.
3. **Safe data embedding** — prohibition on embedding raw JSON in inline `onclick` attributes; mandated pattern: `data-*` attribute with `&quot;` encoding + `dataset.attrName` read at click time.
4. **Node spacing floor** — minimum 200 px between regional cluster nodes at default zoom; ×1.7 scale factor as reference baseline for preset layouts.
**Rationale:** patterns discovered through `viz_interactive_T3.html` iteration should be codified so future visualizations start from the correct baseline rather than repeating the same mistakes.
**Affected chats:** Visualization Builder.
**Snapshot:** none (minor bump).

---

*(future entries below as updates occur)*
