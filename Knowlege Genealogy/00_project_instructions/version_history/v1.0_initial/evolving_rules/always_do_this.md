# Always Do This — User Preferences and Standing Rules

**Version:** 1.0
**Last Updated:** 2026-05-20
**Status:** Active
**Owner:** Instruction Curator
**Applies to:** all chats

## Change Log
- v1.0 (2026-05-20): Initial version. Seeded with rules already implicit in `core/ontology_definition.md` and `core/audit_framework.md`. Future additions come from user feedback and audit findings.

---

These are positive rules — things every chat must do. They accumulate over the life of the project. Most are user preferences captured during work ("from now on, always do X"). A small initial set is seeded from the founding documents.

Each rule has a number, a date added, a reason, and (after it's been in force a while) an effectiveness note.

## Confidence and evidence

1. **Always default to confidence B.** Use A only when at least two independent E2 sources agree, ideally plus E4. (Added 2026-05-20 from ontology_definition.md §5. Reason: anti-inflation.)
2. **Always populate `source_ids` on every node and edge.** No claim without a source. (Added 2026-05-20 from extractor_instructions.md. Reason: anti-fabrication.)
3. **Always specify `date_precision`.** Year, decade, century, or era — never leave implicit. (Added 2026-05-20 from ontology_definition.md §9. Reason: honest uncertainty.)

## Geographic coverage

4. **Always populate the `region` field on every node.** Greek, Hellenistic, Chinese, Indian, Islamic, European, African, Indigenous, or Global. Comma-separated if multiple. (Added 2026-05-20 from ontology_definition.md §2. Reason: global inclusivity.)
5. **Always include at least one non-European tradition in ancient and medieval era batches** where the historical record supports it. (Added 2026-05-20 from extractor_instructions.md and audit_framework.md §6. Reason: counter default Eurocentrism.)

## Pioneers and attribution

6. **Always list multiple pioneers** (3+ where the historical record supports it). Single-pioneer entries get flagged in Micro-Audit. (Added 2026-05-20 from extractor_instructions.md. Reason: founder-mythology prevention.)
7. **Always use "associated pioneers"** language, never "founder" or "founded by." (Added 2026-05-20 from project_charter.md anti-patterns. Reason: revolutions are collective.)

## Process

8. **Always file a Micro-Audit document for every batch**, even ones that pass first review. The audit trail is a deliverable. (Added 2026-05-20 from audit_framework.md §3. Reason: process transparency.)
9. **Always wait for the relevant gate to PASS** before advancing — Graph Builder commits only after Micro-Audit PASS; next era extraction only after Phase-Audit PASS; delivery only after Macro-Audit APPROVED + 7 sign-offs. (Added 2026-05-20 from audit_framework.md §2. Reason: hard quality control.)
10. **Always update the changelog** in `07_exports/changelog.md` after any commit to master CSVs. (Added 2026-05-20 from graph_builder_instructions.md. Reason: traceability.)

---

## Format for new entries

When the Curator adds a rule:

```markdown
N. **Always [imperative].** [one-sentence elaboration if needed]
   (Added YYYY-MM-DD from {user feedback | audit finding | process discovery}.
    Reason: [one phrase].
    Affected chats: [list]
    Effectiveness: [after first re-audit, add: "verified — N violations dropped to M"])
```

## How chats use this file

Every chat must skim this file before producing output. The Micro-Audit checklist (in `audit_templates/micro_audit_template.md`) verifies adherence to the numbered rules here.
