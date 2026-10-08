# Workflow Procedures

**Version:** 1.0
**Last Updated:** 2026-05-20
**Status:** Active (stub)
**Affected chats:** all

## Change Log
- v1.0 (2026-05-20): Initial stub. Points to authoritative workflow documentation in `README.md` and `core/audit_framework.md`. Will be expanded into a standalone reference once Trunk 3 execution surfaces enough best practices to justify it.

---

## What this document is

The canonical, single-page reference for *how the work flows* — order of operations, hand-offs between chats, parallelism opportunities, where artifacts live at each step. It is owned by the Instruction Curator and revised as `evolving_rules/best_practices.md` discoveries get promoted into standard procedure.

## Current authoritative content

At v1.0 the workflow is described in two places, and this document points to them rather than duplicating:

- **`README.md`** — the "Standard workflow (per trunk, per era)" section gives the ten-step pipeline (Source Librarian → Extractor → Historian-Critic → Graph Builder → Visualization Builder → Phase-Audit → Macro-Audit).
- **`core/audit_framework.md`** — defines the three gates and decision logic at each gate.

For now, those two documents are authoritative. This file exists to hold the workflow once it grows beyond what fits in the README.

## When this file will be expanded

The Instruction Curator will populate this file substantively when:

- A best practice in `evolving_rules/best_practices.md` is promoted to standard (e.g., iterative-batch extraction, parallel source compilation for next era).
- A workflow change touches multiple chats and needs a single source of truth.
- Cross-trunk inheritance kicks in (Trunk 1 onward inherits learnings from Trunk 3).

At that point this file gets a 2.0 bump and a real body.

## Until then

If you want to know what step comes next, look at the README's workflow pipeline. If you want to know when a gate fires, look at `audit_framework.md`. If you've discovered a better way to do something, log it to `evolving_rules/best_practices.md` and notify the Curator.
