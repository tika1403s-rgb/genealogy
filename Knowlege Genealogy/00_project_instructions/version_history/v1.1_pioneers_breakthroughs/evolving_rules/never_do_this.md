# Never Do This — Forbidden Patterns

**Version:** 1.1
**Last Updated:** 2026-05-20
**Status:** Active
**Owner:** Instruction Curator
**Applies to:** all chats

## Change Log
- v1.0 (2026-05-20): Initial version. Seeded with prohibitions already implicit in `core/ontology_definition.md`, `core/audit_framework.md`, and `core/project_charter.md`. Future additions come from user feedback and audit findings.
- v1.1 (2026-05-20): Added prohibitions 13–16 for the v2.0 pioneer + breakthrough data model.

---

These are negative rules — patterns that must never appear in project output. Violations are tracked. Each rule shows its current violation count, which should trend to zero after the rule is in place.

## Language and framing

1. **Never use "founded" or "founder."** Use "associated pioneers" (plural). (Added 2026-05-20. Source: project_charter.md anti-patterns. Violation count: 0.)
2. **Never use modern field names for pre-1700 nodes** without an explicit retrospection note in `controversies`. Forbidden in the `label` field of pre-1700 nodes: "physics," "chemistry," "biology," "psychology," "sociology," "economics," "computer science." Use period-appropriate terms: natural philosophy, alchemy, natural history, moral philosophy, political economy, etc. (Added 2026-05-20. Source: project_charter.md and audit_framework.md §6a. Violation count: 0.)
3. **Never treat OECD/UNESCO/Library of Congress as historical evidence.** E6 sources may anchor modern taxonomy structure only. They are never sufficient evidence for historical emergence claims. (Added 2026-05-20. Source: project_charter.md and ontology_definition.md §6. Violation count: 0.)

## Confidence and evidence

4. **Never assign confidence A without at least two independent E2 sources.** (Added 2026-05-20. Source: ontology_definition.md §5 and audit_framework.md §6. Violation count: 0.)
5. **Never use E6 as the only evidence type on a node or edge.** Macro-Audit fails if any node has E6 as sole evidence. (Added 2026-05-20. Source: audit_framework.md §6c. Violation count: 0.)
6. **Never claim `year` date precision for pre-1500 events** unless tied to a specific dated publication or recorded institutional event. (Added 2026-05-20. Source: audit_framework.md Phase-Audit template. Violation count: 0.)

## Schema and process

7. **Never invent sources.** If a citation cannot be verified, say so. Do not fabricate plausible-sounding monographs. (Added 2026-05-20. Source: source_librarian_instructions.md. Violation count: 0.)
8. **Never commit to master CSVs without Micro-Audit PASS.** Graph Builder is blocked at Gate 1. (Added 2026-05-20. Source: audit_framework.md §2. Violation count: 0.)
9. **Never begin extraction for the next era** until the current era's Phase-Audit returns PASS. Gate 2 enforcement. (Added 2026-05-20. Source: audit_framework.md §2. Violation count: 0.)
10. **Never release a deliverable** without Macro-Audit APPROVED + all 7 sign-offs. Gate 3 enforcement. (Added 2026-05-20. Source: audit_framework.md §2. Violation count: 0.)
11. **Never use an edge `relation_type` not in the approved ontology.** The 10 types in `ontology_definition.md` §4 are the full set. If none fit, escalate to Taxonomy Architect rather than inventing. (Added 2026-05-20. Source: extractor_instructions.md. Violation count: 0.)
12. **Never leave the `region` field empty** on a node. Every node gets a region. (Added 2026-05-20. Source: ontology_definition.md §2. Violation count: 0.)

## Pioneers and breakthroughs (v1.1)

13. **Never duplicate a pioneer or breakthrough that already exists in master CSVs.** Reference the existing `PION_NNN` or `BRKTH_NNN`. Adding a second row for the same person fragments the join tables. (Added 2026-05-20. Source: extractor_instructions v1.1. Violation count: 0.)
14. **Never write vague pioneer contributions** in `pioneer_contributions.specific_contribution`. Forbidden: "worked on X," "contributed to Y," "influenced Z." Required: a one-sentence dated claim citing a specific work or result. (Added 2026-05-20. Source: audit_framework v1.1 Check #8. Violation count: 0.)
15. **Never leave `enabling_breakthrough_ids` empty** for modern/contemporary nodes unless `controversies` documents the justification (e.g., the field emerged through tradition with no discrete enabling technology). Empty fields will fail Macro-Audit §6h. (Added 2026-05-20. Source: audit_framework v1.1 §6h. Violation count: 0.)
16. **Never omit cross-trunk enablers** from contemporary nodes whose dependence on other-trunk breakthroughs is well-documented. AI without statistics, transistor, GPU, neural-net-model fails Macro-Audit §6i. (Added 2026-05-20. Source: audit_framework v1.1 §6i. Violation count: 0.)

---

## Format for new entries

```markdown
N. **Never [forbidden action].** [one-sentence elaboration if needed]
   (Added YYYY-MM-DD. Source: {user feedback | audit finding | process discovery}.
    Reason: [one phrase].
    Violation count: 0 [updated by Curator after each audit])
```

## Violation tracking

Each Micro-Audit and Phase-Audit reports any violations of rules here. The Curator updates the violation count for each rule after every audit. A rule whose violation count is zero for three consecutive phases can be considered stable.

A rule whose violation count remains nonzero after multiple audits is *ineffective* — the rule didn't address the root cause. The Curator flags it in `evolution_tracking/effectiveness_analysis.md` for revision.
