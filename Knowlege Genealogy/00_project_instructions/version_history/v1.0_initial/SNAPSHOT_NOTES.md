# Snapshot: v1.0_initial

**Date:** 2026-05-20
**Trigger:** Project bootstrap
**Snapshotted by:** Initial setup (no Curator yet — see `instruction_update_history.md`)

## What this snapshot contains

Frozen copies of every instruction and evolving-rules file at the moment the project was first scaffolded, before any execution work began.

- `core/` — project_charter, ontology_definition, audit_framework (5 of 5 planned; workflow_procedures and quality_guidelines were deferred and will land in a later snapshot)
- `chat_specific/` — all 8 chat instruction files
- `evolving_rules/` — always_do_this (seeded with 10 rules), never_do_this (seeded with 12 rules), common_mistakes (empty), best_practices (empty)

## What this snapshot does NOT contain

- Evolution tracking files (`evolution_tracker.json`, `user_feedback_log.md`, `instruction_update_history.md`, `effectiveness_analysis.md`) — these are running logs and are never snapshotted; their history is preserved in-place.
- Audit templates (`05_validation/audit_templates/`) — separately versioned.
- Master data files (`04_nodes_edges/`) — separately versioned via `07_exports/changelog.md`.

## How to use a snapshot

If you need to see what the v1.0 rules said before later modifications, read the files in this folder. To compare v1.0 vs current, diff the matching paths:

```
diff version_history/v1.0_initial/chat_specific/extractor_instructions.md \
     chat_specific/extractor_instructions.md
```

## When the next snapshot will happen

By policy in `chat_specific/instruction_curator_instructions.md`:
- Patch and minor version bumps (1.x → 1.y) do NOT create new snapshots.
- Major version bumps (1.x → 2.0, etc.) DO create a new snapshot folder.

The expected next snapshot is `v2.0_trunk_3_complete/` — produced by the Instruction Curator when Trunk 3's Macro-Audit returns APPROVED FOR DELIVERY.
