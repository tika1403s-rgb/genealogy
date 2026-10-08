# Genealogy of Knowledge & Science

A historically rigorous, source-backed knowledge graph tracing the evolution of 10 major knowledge lineages from antiquity to the present.

## Project status

**Stage:** Full bootstrap complete at v1.1 — three-tier audit framework, instruction evolution system, trunk definitions, ontology v2.0 (with pioneers + breakthroughs as first-class entities), and seeded master CSVs all in place (Week 1 of 36).
**Next:** Set up the 8 specialized chats (paste each `chat_specific/*_instructions.md` into a new Claude conversation). Then begin Trunk 3 ancient-layer research with the Source Librarian.

## Folder structure

```
Knowlege Genealogy/
├── README.md                                  ← this file
│
├── 00_project_instructions/
│   ├── core/                                  ← canonical, version-controlled foundation
│   │   ├── project_charter.md           v1.0
│   │   ├── ontology_definition.md       v2.0  (pioneers + breakthroughs as 1st-class)
│   │   ├── audit_framework.md           v1.1  (9 metrics; pioneer/breakthrough checks)
│   │   ├── workflow_procedures.md       v1.0  (stub)
│   │   ├── quality_guidelines.md        v1.0  (stub)
│   │   └── trunk_definitions.md         v1.1
│   │
│   ├── chat_specific/                         ← system prompts for the 8 specialized chats
│   │   ├── taxonomy_architect_instructions.md         v1.0
│   │   ├── source_librarian_instructions.md           v1.1
│   │   ├── extractor_instructions.md                  v1.1
│   │   ├── historian_critic_instructions.md           v1.1
│   │   ├── graph_builder_instructions.md              v1.1
│   │   ├── visualization_builder_instructions.md      v1.1
│   │   ├── red_team_reviewer_instructions.md          v1.1
│   │   └── instruction_curator_instructions.md        v1.0
│   │
│   ├── evolving_rules/                        ← living rules updated through execution
│   │   ├── always_do_this.md            v1.1  (15 rules)
│   │   ├── never_do_this.md             v1.1  (16 rules)
│   │   ├── common_mistakes.md           v1.0  (empty; fills as audits surface patterns)
│   │   └── best_practices.md            v1.0  (empty; fills as discoveries land)
│   │
│   ├── evolution_tracking/                    ← Curator's running logs
│   │   ├── evolution_tracker.json             (version + mistake-count history)
│   │   ├── user_feedback_log.md               (every user preference captured)
│   │   ├── instruction_update_history.md      (instruction-file changelog)
│   │   └── effectiveness_analysis.md          (do updates reduce errors?)
│   │
│   ├── templates/                             ← will hold extraction/edge templates
│   │
│   └── version_history/
│       ├── v1.0_initial/                      ← snapshot of all instruction files at bootstrap
│       └── v1.1_pioneers_breakthroughs/       ← snapshot of v1.1-changed files (14 files)
│
├── 01_sources/                                ← raw source material organized by type
│   ├── classification_systems/                (OECD FORD, UNESCO, LoC)
│   ├── encyclopedias/                         (Stanford, Cambridge, Oxford)
│   ├── bibliometric_data/                     (OpenAlex exports)
│   ├── histories_of_science/                  (Cambridge History, discipline histories)
│   └── primary_texts/                         (Aristotle, Newton, Darwin, etc.)
│
├── 02_source_notes/                           ← per-source extraction notes, by trunk + era
│   └── trunk_3/{ancient, medieval, early_modern, modern, contemporary}/
│
├── 03_extractions/                            ← candidate nodes/edges before validation
│   ├── trunk_3/
│   └── validation_reports/
│
├── 04_nodes_edges/                            ← MASTER DATA (after validation; 8 files)
│   ├── README.md                              (append rules + v1.1 validation script)
│   ├── nodes.csv                              (24 cols, headers ready, 0 rows)
│   ├── edges.csv                              (12 cols, headers ready, 0 rows)
│   ├── sources.csv                            (10 cols, headers ready, 0 rows)
│   ├── disputed_claims.csv                    (11 cols, headers ready, 0 rows)
│   ├── pioneers.csv                           (16 cols, headers ready, 0 rows) — v2.0
│   ├── breakthroughs.csv                      (15 cols, headers ready, 0 rows) — v2.0
│   ├── pioneer_contributions.csv              ( 9 cols, headers ready, 0 rows) — v2.0
│   ├── breakthrough_dependencies.csv          ( 7 cols, headers ready, 0 rows) — v2.0
│   └── trunk_lineages/
│
├── 05_validation/                             ← three-tier audit system
│   ├── micro_audits/                          (per-batch, Historian-Critic)
│   ├── phase_audits/                          (per-era, Red-Team Reviewer)
│   ├── macro_audit/                           (per-trunk, all chats sign off)
│   ├── revision_logs/                         (changes made in response to audits)
│   └── audit_templates/                       (micro / phase / macro templates)
│
├── 06_visualizations/                         ← interactive HTML visualizations
│   └── assets/
│
└── 07_exports/                                ← finished documents for sharing
    ├── bibliography.md                        (to author after first batch)
    ├── changelog.md                           ✓ (initialized; data changes log here)
    ├── methodology_note.md                    (to author at trunk completion)
    └── trunk_profiles/
```

## How to use the 8 chat instruction files

The project runs as a multi-agent workflow across 8 dedicated Claude chats. Each has a narrow role and a stable system prompt. To set up a chat:

1. Open a new Claude conversation.
2. Paste the contents of the corresponding file from `00_project_instructions/chat_specific/` as the first message (or as project instructions if using Claude Projects).
3. Begin work in that chat with role-appropriate tasks only.

The 8 roles and when to use each:

| Chat | Use when |
|------|----------|
| **Taxonomy Architect** | A proposed node/edge doesn't fit the schema; you need to add or revise an ontology element |
| **Source Librarian** | You need a bibliography of authoritative sources for a trunk + era |
| **Extractor** | You have sources and need them converted into structured nodes/edges |
| **Historian-Critic** | The Extractor has produced candidates; needs adversarial Micro-Audit before commit |
| **Graph Builder** | Validated nodes/edges need to be merged into the master CSVs |
| **Visualization Builder** | The master CSVs have been updated; visualizations need a refresh |
| **Red-Team Reviewer** | An era is complete (Phase-Audit) or a trunk is complete (Macro-Audit) |
| **Instruction Curator** | Capture a user preference, encode a recurring audit finding into rules, version an instruction file, prepare cross-trunk inheritance |

## Standard workflow (per trunk, per era)

```
1. Source Librarian       → produces a source list (saves to 02_source_notes/)
2. Extractor              → produces candidate nodes/edges JSON (saves to 03_extractions/)
3. Historian-Critic       → MICRO-AUDIT: reviews batch, returns PASS or REVISE
4. Extractor              → applies revisions until Micro-Audit returns PASS  [GATE 1]
5. Graph Builder          → commits to 04_nodes_edges/ master CSVs + updates changelog
6. Visualization Builder  → refreshes visualizations in 06_visualizations/
7. Red-Team Reviewer      → PHASE-AUDIT at era end: PASS / REVISE / EXPAND   [GATE 2]
                            (must PASS before next era extraction begins)

After all eras of a trunk are complete:
8. Red-Team Reviewer      → MACRO-AUDIT: APPROVED / CONDITIONAL / REVISE     [GATE 3]
9. All eight chats        → sign-off (recorded in 05_validation/macro_audit/)
10. Final delivery        → only after Macro-Audit is APPROVED + 8 sign-offs complete
11. Instruction Curator   → compiles trunk's learnings into v{N+1}.0 instructions
                            (snapshot in version_history/) — next trunk starts from there
```

## Audit framework (three tiers, three gates)

Quality control is built into the workflow as three hard gates. The canonical specification is `00_project_instructions/core/audit_framework.md`. Templates for filling out each audit live in `05_validation/audit_templates/`.

| Tier | Frequency | Owner | Gate enforced |
|------|-----------|-------|---------------|
| **Micro-Audit** | Every 5–10 nodes | Historian-Critic | Graph Builder cannot commit until PASS |
| **Phase-Audit** | End of each era | Red-Team Reviewer | Next era cannot begin until PASS |
| **Macro-Audit** | Pre-delivery, per trunk | Red-Team Reviewer + all chats | No delivery until APPROVED + 8 sign-offs |

The Macro-Audit computes **nine** quantitative metrics with explicit pass/fail thresholds (v1.1):
- Presentism score, founder mythology score, taxonomy bias score, source diversity, confidence realism, geographic diversity (original six)
- Pioneer coverage, breakthrough coverage, cross-trunk enabler completeness (v1.1 additions)

See `core/audit_framework.md` Section 6 for the thresholds.

## Data model summary (v2.0)

The graph has **four primary entity types** plus two join tables:

| Entity | Master file | Purpose |
|--------|-------------|---------|
| **Nodes** | `nodes.csv` | Fields, traditions, disciplines |
| **Edges** | `edges.csv` | Node-to-node relations (10 types: emerged_from, split_from, merged_with, renamed_as, formalized_by, mathematized_by, institutionalized_as, method_imported_from, instrument_enabled, problem_domain_shared_with) |
| **Pioneers** | `pioneers.csv` | People whose work shaped one or more fields |
| **Breakthroughs** | `breakthroughs.csv` | Discoveries, inventions, concepts, methods, instruments, formalizations |
| Pioneer contributions | `pioneer_contributions.csv` | Many-to-many: which pioneer contributed what to which node |
| Breakthrough dependencies | `breakthrough_dependencies.csv` | Many-to-many: which breakthrough `enabled_by` / `transformed_by` / `contributed_to` which node |

Plus `sources.csv` (every cited source) and `disputed_claims.csv` (controversies).

The canonical example the v1.1 audit metrics protect against: an AI node that lists only "AI researchers" as pioneers and has empty `enabling_breakthrough_ids`. The required form is an AI node that references the transistor (Trunk 3/8), statistical methods (Trunk 1), Boolean logic (Trunk 9), Turing machine (Trunk 9), information theory (Trunk 9), neural network model (Trunk 4/9), backpropagation algorithm, large datasets, and GPU computing as enablers — making the cross-trunk graph structure visible.

## Instruction evolution system

The project's instructions are living documents — they improve through execution rather than being frozen at the start. The Instruction Curator (chat #8) owns this system.

**Three feedback sources update instructions:**

1. **User feedback** — "always do X" / "never do Y" → captured to `evolving_rules/always_do_this.md` or `never_do_this.md`, propagated into the relevant chat instruction file, logged in `evolution_tracking/user_feedback_log.md`.
2. **Recurring audit findings** — a mistake appearing in 3+ Micro-Audits or 2+ Phase-Audits triggers an instruction update; pattern logged in `common_mistakes.md`.
3. **Process discoveries** — a chat finds a better way of working → logged to `best_practices.md` and (when proven) promoted into `workflow_procedures.md`.

**Versioning:**

- Patch (1.0 → 1.1): adding a rule, clarifying wording.
- Minor (1.1 → 1.2): adding sections, tightening thresholds.
- Major (1.x → 2.0): restructuring, cross-trunk inheritance event. Triggers a snapshot in `version_history/`.

**Cross-trunk inheritance:**

Each trunk begins with the previous trunk's final-version instructions. By Trunk 10 the chats are operating on instructions refined by nine prior trunks of execution. Trunk 3 starts at v1.0 → expected to end at v2.0; Trunk 1 begins at v2.0; and so on.

## The 10 trunks

1. **Mathematical Sciences** — geometry, algebra, calculus, statistics, computer science
2. **Celestial Studies** — astronomy, cosmology, astrophysics
3. **Material Investigation** — natural philosophy, alchemy, chemistry, physics, materials science **(PILOT)**
4. **Life Studies** — natural history, medicine, biology, molecular biology
5. **Mind & Society** — philosophy, psychology, sociology, economics
6. **Language & Meaning** — grammar, logic, linguistics, NLP
7. **Historical Inquiry** — historiography, archaeology, anthropology
8. **Practical Arts** — engineering, applied sciences
9. **Formal Reasoning** — logic, mathematical logic, computer science
10. **Earth & Environment** — geography, geology, climate science

Full trunk definitions will be authored in `00_project_instructions/core/trunk_definitions.md` in a future session.

## What to do next

1. **Set up the 8 chats** — open 8 new Claude conversations and paste the contents of each `00_project_instructions/chat_specific/*_instructions.md` as the first message (or as project instructions if using Claude Projects).
2. **Begin Phase 1, Step 1:** In the Source Librarian chat, request a bibliography for Trunk 3's ancient layer. Target: 5 E1 primary texts, 8 E2 scholarly sources, 2 E3 encyclopedia entries; at least 3 covering non-European traditions (Chinese wu xing, Indian Vaisheshika, etc.).
3. **Hand off to the Extractor** once the Source Librarian's bibliography is in `02_source_notes/trunk_3/ancient/` and the source rows have been added to `sources.csv` via the Graph Builder.
4. **Run the first Micro-Audit (Gate 1)** in the Historian-Critic chat once the Extractor produces its first batch of ancient nodes.

## Reading order for a new collaborator

1. `00_project_instructions/core/project_charter.md` — what we're doing and why
2. `00_project_instructions/core/ontology_definition.md` — the data model
3. `00_project_instructions/core/audit_framework.md` — three-tier audit gates (required for Historian-Critic and Red-Team Reviewer; recommended for all)
4. `00_project_instructions/evolving_rules/always_do_this.md` and `never_do_this.md` — current behavioral rules
5. The `chat_specific/*_instructions.md` file for whichever role they're playing
6. The current state of `07_exports/changelog.md` (once it exists) — what's happened lately
# genealogy
