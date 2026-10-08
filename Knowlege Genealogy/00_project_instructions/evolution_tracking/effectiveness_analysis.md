# Instruction Effectiveness Analysis

**Owner:** Instruction Curator
**Cadence:** updated after every Phase-Audit; full review at every Macro-Audit
**Last updated:** 2026-05-20

---

This document answers: *Are the instruction updates we're making actually reducing the errors they targeted?*

A rule that's added but doesn't change behavior is worse than no rule — it creates the illusion of having addressed a problem. After each Phase-Audit, the Curator compares violation counts for tracked failure modes against the audits prior to the rule landing.

## Status legend

- **EFFECTIVE** — Target mistake count dropped to zero (or near zero) for at least three consecutive audits after rule landed.
- **PARTIALLY EFFECTIVE** — Target mistake count dropped but did not reach zero.
- **INEFFECTIVE** — Target mistake count did not drop, or dropped only briefly and returned. The rule didn't address the root cause; needs revision.
- **PENDING** — Rule landed too recently to evaluate; needs ≥2 more audits.

## Tracked failure modes

| Failure mode | Rule(s) addressing it | Status | Notes |
|--------------|----------------------|--------|-------|
| Presentism (modern labels on ancient practices) | `never_do_this.md` #2; `extractor_instructions.md` extraction rules | PENDING | No batches extracted yet |
| Founder mythology (single-pioneer attribution) | `never_do_this.md` #1; `always_do_this.md` #6 | PENDING | — |
| Taxonomy bias (E6 as sole evidence) | `never_do_this.md` #3, #5; `audit_framework.md` §6c | PENDING | — |
| False date precision | `never_do_this.md` #6; `always_do_this.md` #3 | PENDING | — |
| Eurocentric bias | `always_do_this.md` #4, #5; Phase-Audit §6 geographic balance | PENDING | — |
| Confidence inflation | `never_do_this.md` #4; `always_do_this.md` #1 | PENDING | — |
| Source fabrication | `never_do_this.md` #7; `source_librarian_instructions.md` anti-fabrication discipline | PENDING | — |

## Phase-by-phase comparison

To be populated by the Curator after each Phase-Audit. Sample row format:

```
| Phase | Presentism violations | Founder mythology | Taxonomy bias | ... | Curator notes |
|-------|----------------------|-------------------|---------------|-----|---------------|
| t3 Ancient cycle 1 | 8/30 | 5/30 | 0/30 | ... | High presentism; rule applied at end of cycle |
| t3 Ancient cycle 2 | 1/30 | 0/30 | 0/30 | ... | Presentism rule effective |
| t3 Medieval         | 0/30 | 0/30 | 0/30 | ... | All rules effective in this phase |
```

## Ineffective rules

Rules currently flagged as needing revision:

*(none yet)*

When a rule moves to INEFFECTIVE, the Curator opens a revision proposal: either sharpen the rule's wording, change which file it lives in, or address the root cause differently (e.g. add a workflow change rather than just a prohibition).

## Major-version-bump review

At each Macro-Audit, the Curator answers four questions:

1. Which rules have proven EFFECTIVE? (Promote to "stable" status; consider for cross-trunk inheritance.)
2. Which rules are PARTIALLY EFFECTIVE? (Sharpen wording or add a workflow change.)
3. Which rules are INEFFECTIVE? (Either remove or rewrite from a different angle.)
4. What new failure modes appeared this trunk that should be tracked going forward?

Answers feed into the v{N}.0 instruction set that the next trunk will start with.
