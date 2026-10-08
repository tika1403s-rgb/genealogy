# Project Charter: Genealogy of Knowledge & Science

**Version:** 1.0
**Last Updated:** 2026-05-20
**Status:** Active
**Affected chats:** all

## Change Log
- v1.0 (2026-05-20): Initial version — mission, principles, success criteria, timeline.

---

## Mission

Build a historically rigorous, source-backed knowledge graph that traces the evolution of 10 major knowledge lineages ("trunks") from ancient origins through contemporary specializations. The graph treats knowledge as a *process* of branching, merging, renaming, and cross-pollination — not as a static inventory of fields by era.

## Core Principles

1. **Knowledge as process, not inventory.** Trace how fields evolve through time. A "field" is a moving target with fuzzy boundaries.
2. **Source-backed authority.** Claude is a research assistant, not an oracle. Every claim must cite a source with an evidence type (E1–E6).
3. **Graph, not tree.** Fields split, merge, rename, borrow methods, and cross-pollinate. The data model is a directed graph with rich edge semantics.
4. **Anti-presentism.** Never project modern categories backward onto ancient practices. When using modern labels for historical activities, mark them as retrospective.
5. **Honest uncertainty.** Every node and edge carries a confidence score (A/B/C/D/X) and a date precision marker (year/decade/century/era). False precision is worse than acknowledged uncertainty.
6. **Geographic inclusivity.** Greek, Chinese, Indian, Islamic, African, and Indigenous contributions are tracked explicitly via a required `region` field. Transmission routes between traditions are first-class edges.
7. **No founder mythology.** Use "associated pioneers" (plural). Revolutions are collective; foundings are rarely single events.
8. **Disputes stay visible.** Where historians disagree, record competing interpretations in the `controversies` field and the `disputed_claims.csv` log. Do not force consensus.

## Key Methodological Innovation: Trunk Lineages

Instead of horizontal era slices (ancient / medieval / modern), the project traces **10 vertical knowledge lineages** from antiquity to the present. Each trunk is a continuous tradition of inquiry that branches, merges, and evolves across 2500+ years. The 10 trunks are defined in `trunk_definitions.md` (to be authored in a later session).

## The Pilot

Trunk 3 — **Material Investigation** — is the pilot. It traces the evolution of inquiry into matter, substances, and physical reality: ancient natural philosophy → medieval alchemy → early modern chemistry/physics → modern disciplinary split → contemporary merges (physical chemistry, materials science, condensed matter physics). It is chosen because it forces the project to handle every difficult case: splits, merges, non-European contributions, instrument-enabled discoveries, and contested boundaries (alchemy vs. chemistry).

## Pilot Success Criteria

- 40–60 nodes spanning ancient → contemporary.
- 80–120 edges covering all 10 relation types at least once.
- All 5 event types represented.
- 50+ sources cited across all six evidence types.
- Confidence distribution skewed toward B/C (honest uncertainty, not inflated A grades).
- At least 3 disputed claims documented.
- Functional interactive timeline and network visualizations.
- Red-team audit passes (no major presentism or founder mythology).
- Non-European contributions visibly represented.

## Full Project Success Criteria

- 500+ nodes across all 10 trunks.
- 1000+ edges including cross-trunk connections (e.g., mathematics → physics, logic → computer science).
- 300+ sources.
- Comprehensive bibliography.
- All trunks profiled in `07_exports/trunk_profiles/`.
- Global interactive map.
- Exportable data in CSV, JSON, and GraphML.

## Timeline

| Phase | Weeks | Output |
|-------|-------|--------|
| Setup | 1 | Project scaffolding, 7 chats configured |
| Trunk 3 pilot | 2–12 | 40–60 nodes, full visualizations, profile |
| Trunks 1, 5, 9 | 13–24 | Three additional lineages; cross-trunk edges begin |
| Remaining 6 trunks | 25–32 | All 10 trunks complete |
| Integration | 33–36 | Global map, cross-trunk analysis, final docs |

## Workflow Pattern (per trunk, per era)

1. **Source Librarian** finds authoritative sources for the era.
2. **Extractor** converts sources into candidate nodes and edges (CSV/JSON).
3. **Historian-Critic** red-teams the extraction for presentism, founder mythology, dating, geographic bias.
4. **Graph Builder** merges validated nodes/edges into master CSVs in `04_nodes_edges/`.
5. **Visualization Builder** updates timeline, network, and Sankey views in `06_visualizations/`.
6. **Red-Team Reviewer** audits confidence scores and evidence types after each era is complete.

The **Taxonomy Architect** is consulted whenever the ontology itself needs revision (new edge type, new event type, schema change).

## Anti-Patterns to Avoid

- "Aristotle founded biology." → Aristotle contributed to natural history (a `first_problem_tradition`); biology as a `named_field` emerged c. 1800s.
- Single precise date with no institutional event. → Use date ranges with precision marker.
- Linear tree structure. → Network with splits, merges, cross-pollination, renames.
- Western-only narrative. → Global knowledge traditions with transmission tracking.
- Treating OECD/UNESCO as historical truth. → Use only as modern taxonomic reference (E6).
