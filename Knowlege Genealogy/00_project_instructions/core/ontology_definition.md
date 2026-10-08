# Ontology Definition

**Version:** 2.0
**Last Updated:** 2026-05-20
**Status:** Active
**Affected chats:** all (canonical schema for nodes, edges, pioneers, breakthroughs, contributions, dependencies, sources, disputes)

## Change Log
- v1.0 (2026-05-20): Initial version — node schema, edge schema, 5 event types, 10 relation types, A/B/C/D/X confidence, E1–E6 evidence.
- v2.0 (2026-05-20): **Major bump.** Added pioneers as first-class entities (§11); added breakthroughs as first-class entities (§12); added pioneer_contributions and breakthrough_dependencies join tables (§13, §14); added four new edge relation types — `contributed_by`, `enabled_by`, `transformed_by`, `contributed_to` (§4). Node schema gained `pioneer_ids`, `enabling_breakthrough_ids`, `transforming_breakthrough_ids`, `critical_works`, `critical_instruments` fields (§2). Trigger: addressing the "Gap Identified: Pioneers, Ideas, and Enabling Factors" — the v1.0 ontology represented fields and their relationships well but did not give first-class structure to the *people* and *enabling discoveries* that made fields possible. Snapshot of v1.0 preserved at `version_history/v1.0_initial/`; snapshot of v2.0 changes at `version_history/v1.1_pioneers_breakthroughs/`.

---

This document defines the data model for the knowledge graph: what counts as a node, what counts as an edge, what fields they carry, and how to score them.

## 1. Event Type Taxonomy

Every node is tagged with one `creation_event_type`. These describe the *kind of historical transition* the node represents. Not all fields pass through all stages, and a tradition can sit at one stage for centuries before advancing.

| Event Type | Meaning | Example |
|------------|---------|---------|
| `first_problem_tradition` | People begin asking recognizable questions, even if no "field" exists | Ancient geometry; ancient star observation |
| `conceptual_breakthrough` | A key idea or method appears that reframes the inquiry | Newtonian mechanics; natural selection |
| `named_field` | The inquiry receives a recognizable name still in use | "Sociology"; "biochemistry"; "cybernetics" |
| `institutionalized_field` | Journals, departments, professional societies appear | Psychology labs (Wundt 1879); first economics chairs |
| `modern_formulation` | The field reaches its contemporary form | Molecular biology; computer science; AI |

**Rule:** Do not collapse stages. A tradition can have a `first_problem_tradition` node in antiquity AND a separate `named_field` node millennia later. They are different events and should be linked by an edge (typically `renamed_as` or `formalized_by`).

## 2. Node Schema

CSV header (and master JSON shape):

```
node_id, label, type, trunk_id, parent_candidate, date_start, date_end,
date_precision, creation_event_type, region, description, core_idea,
pioneers, representative_works, institutional_markers, source_ids,
confidence, evidence_type, controversies,
pioneer_ids, enabling_breakthrough_ids, transforming_breakthrough_ids,
critical_works, critical_instruments
```

**v2.0 additions to nodes.csv** (last five columns above):
- **pioneer_ids** — comma-separated `PION_NNN` references into `pioneers.csv`. The free-text `pioneers` column remains for human-readable summary; `pioneer_ids` is the structured link.
- **enabling_breakthrough_ids** — comma-separated `BRKTH_NNN` references for breakthroughs that *made this field possible*.
- **transforming_breakthrough_ids** — comma-separated `BRKTH_NNN` references for breakthroughs that fundamentally *changed an existing field* (without enabling its initial emergence).
- **critical_works** — short list of canonical publications/experiments. Free text; cite formally in `pioneers.csv` and `breakthroughs.csv` rows.
- **critical_instruments** — short list of instruments essential to this field's practice. Free text; full provenance in `breakthroughs.csv` for instrument-type breakthroughs.

### Field definitions

- **node_id** — Stable identifier. Convention: `T{trunk}_{ERA}_{NNN}`, e.g. `T3_ANC_001`, `T3_MED_004`. Era codes: ANC, MED, EMD (early modern), MOD, CON.
- **label** — Human-readable name as used at the time, or modern label if the node represents a present-day field. If the label is anachronistic, note this in `controversies`.
- **type** — Coarse category: `knowledge_tradition`, `field`, `subfield`, `method`, `theoretical_framework`, `instrument_enabled_practice`. Default to `field` when unsure.
- **trunk_id** — Integer 1–10. Enables lineage filtering. (Defined in `trunk_definitions.md`.)
- **parent_candidate** — Optional informal note about likely predecessor; the authoritative parents are encoded via edges, not this field.
- **date_start, date_end** — ISO-style numeric years. Negative for BCE: `-600` = 600 BCE. `date_end` may be `present`.
- **date_precision** — One of: `year`, `decade`, `century`, `era`. Acknowledges uncertainty.
- **creation_event_type** — One of the 5 event types above.
- **region** — One or more of: `Greek`, `Hellenistic`, `Chinese`, `Indian`, `Islamic`, `European`, `African`, `Indigenous`, `Global`. Comma-separated if multiple.
- **description** — One- to three-sentence summary of what the node represents.
- **core_idea** — The central conceptual content in one sentence.
- **pioneers** — Comma-separated names. Prefer multiple names; flag single-pioneer entries for review (founder mythology check).
- **representative_works** — Canonical texts/results associated with the node.
- **institutional_markers** — Journals, departments, societies, conferences. Empty for pre-institutional nodes.
- **source_ids** — Comma-separated references into `sources.csv` (e.g., `SRC_001, SRC_018`).
- **confidence** — One of A/B/C/D/X. See section 5.
- **evidence_type** — One or more of E1–E6, comma-separated. See section 6.
- **controversies** — Free text noting disputes, alternative datings, retrospective-label warnings.

## 3. Edge Schema

CSV header:

```
edge_id, from_node, to_node, relation_type, date_start, date_end,
date_precision, explanation, pioneers_involved, source_ids,
confidence, evidence_type
```

- **edge_id** — Convention: `T{trunk}_E_{NNN}`, e.g. `T3_E_017`. Cross-trunk edges use the lower-numbered trunk's prefix.
- **from_node, to_node** — node_ids. Direction is "predecessor → successor" for most relations; for `merged_with` direction is symbolic (both parents point to the merged child).
- **relation_type** — See section 4.
- **explanation** — Two to four sentences describing what changed, why, how. This is the historical narrative compressed into a sentence.
- **pioneers_involved** — Names associated specifically with this transition (may differ from the pioneers of either node).

## 4. Relation Types

### 4a. Node-to-node relations (the original 10)

| Relation | Meaning | When to use |
|----------|---------|-------------|
| `emerged_from` | General derivation with broad continuity | Default for ancestor → descendant when no sharper relation fits |
| `split_from` | Explicit divergence into a distinct field | Alchemy → chemistry (gradual but real split) |
| `merged_with` | Fusion of previously distinct fields | Physics + chemistry → physical chemistry |
| `renamed_as` | Same content, new label | "Natural philosophy" → "physics" |
| `formalized_by` | A tradition is transformed by formal/methodological systematization | Aristotelian logic → mathematical logic |
| `mathematized_by` | Specifically the application of mathematical methods | Natural philosophy → Newtonian mechanics |
| `institutionalized_as` | A social/organizational formalization | "Experimental psychology" → "Psychology departments" |
| `method_imported_from` | A cross-trunk influence — a method borrowed wholesale | Statistical methods imported into biology (biostatistics) |
| `instrument_enabled` | A new instrument creates a new line of inquiry | Telescope → observational astronomy; spectroscope → astrophysics |
| `problem_domain_shared_with` | Parallel traditions addressing similar questions | Chinese and Greek atomism, conceptually parallel but not derivative |

### 4b. Pioneer- and breakthrough-related relations (v2.0 additions)

| Relation | Direction | Meaning | When to use |
|----------|-----------|---------|-------------|
| `contributed_by` | pioneer → node | A pioneer's work contributed to a field | Newton → Newtonian Mechanics |
| `enabled_by` | breakthrough → node | A breakthrough made this field possible | Transistor → Computer Science |
| `transformed_by` | breakthrough → node | A breakthrough fundamentally changed an existing field | Quantum mechanics → Physics |
| `contributed_to` | breakthrough → node | A breakthrough influenced field development without enabling or transforming it | Statistical methods → Experimental Psychology |

Pioneer-node and breakthrough-node relations are stored in dedicated join tables (`pioneer_contributions.csv` and `breakthrough_dependencies.csv`) rather than in `edges.csv`. This keeps `edges.csv` focused on the node-to-node graph; the join tables carry richer relationship-specific metadata.

**Rule:** Edges are typed. A vague "influenced" edge does not exist. If you cannot pick one of the existing types, escalate to the Taxonomy Architect chat to consider adding a new type.

## 5. Confidence Scoring

| Score | Meaning | Required evidence |
|-------|---------|------|
| **A** | Multiple scholarly sources agree; well-established | At least two independent E2 sources, ideally plus E4 institutional evidence |
| **B** | Strong but somewhat simplified; minor debate | At least one E2 source; details may be smoothed |
| **C** | Plausible but interpretation-dependent | One scholarly source or strong inference; flag in `controversies` |
| **D** | Weak, retrospective, or metaphorical | Use sparingly; mostly for ancient practices labeled with modern terms |
| **X** | Disputed only — excluded from main narrative | Recorded in `disputed_claims.csv`, not in main nodes/edges |

**Anti-inflation rule:** Default to B. Use A only when you have receipts. The Red-Team Reviewer chat will downgrade unsupported A scores.

## 6. Evidence Type Classification

| Type | Source kind | Examples |
|------|-------------|----------|
| **E1** | Primary text | Euclid's *Elements*, Newton's *Principia*, Lavoisier's *Traité* |
| **E2** | Scholarly historical source | *Cambridge History of Science*; academic monographs and peer-reviewed history-of-science papers |
| **E3** | Encyclopedia / reference | Stanford Encyclopedia of Philosophy; Oxford companions |
| **E4** | Institutional record | Journal founding dates, university department creation, society formation |
| **E5** | Bibliometric evidence | OpenAlex, Crossref, Semantic Scholar; citation network patterns |
| **E6** | Classification system | OECD FORD, UNESCO nomenclature, Library of Congress classification |

### Research protocol

1. Start with E2 / E3 for the historical overview.
2. Validate key claims with E1 (primary texts).
3. Confirm field emergence with E4 (institutional evidence).
4. Cross-check modern fields with E5 (bibliometric patterns).
5. Use E6 only as a structural reference for *modern* taxonomy — never as historical evidence.

## 7. Sources Schema

`sources.csv` columns:

```
source_id, title, author, year, publisher_or_journal, url_or_doi,
evidence_type, region_coverage, era_coverage, notes
```

Every `source_ids` reference in nodes/edges must resolve to a row here.

## 8. Disputed Claims Schema

`disputed_claims.csv` columns:

```
dispute_id, related_node_or_edge_id, question, position_a, position_a_sources,
position_b, position_b_sources, position_c, position_c_sources, status, notes
```

Use this when there is genuine scholarly disagreement (e.g., when alchemy "became" chemistry; whether Islamic alchemy was experimental or theoretical). The main graph reflects the most defensible position; the dispute log preserves the alternatives.

## 9. Date Conventions

- Use signed integers for years: `-300` = 300 BCE; `1687` = 1687 CE.
- Always pair with `date_precision`:
  - `year` only for well-attested events (publication of *Principia*: 1687, precision=year).
  - `decade` for institutional emergence (Wundt's lab: 1879, precision=decade is fine).
  - `century` for ancient traditions.
  - `era` for very long-duration traditions (ancient metallurgy: -3000 to 1500, precision=era).
- For ongoing fields, set `date_end = present`.
- For date ranges in edges (transitions take time), use both `date_start` and `date_end` to mark the transition window.

## 10. Node ID Conventions

| Trunk | Prefix | Trunk Name |
|-------|--------|------------|
| 1 | T1 | Mathematical Sciences |
| 2 | T2 | Celestial Studies |
| 3 | T3 | Material Investigation (pilot) |
| 4 | T4 | Life Studies |
| 5 | T5 | Mind & Society |
| 6 | T6 | Language & Meaning |
| 7 | T7 | Historical Inquiry |
| 8 | T8 | Practical Arts |
| 9 | T9 | Formal Reasoning |
| 10 | T10 | Earth & Environment |

Era codes within a trunk: `ANC` (ancient, ≤500 CE), `MED` (medieval, 500–1500), `EMD` (early modern, 1500–1800), `MOD` (modern, 1800–1950), `CON` (contemporary, 1950–present). Era boundaries are conventional; assign by the node's `date_start`.

## 11. Pioneer Schema (v2.0)

Pioneers are people whose work materially shaped one or more fields. The pioneers table captures their biographical anchor, the structured set of ideas they contributed, the works that document those ideas, and the network of contemporaries they worked with or against.

`pioneers.csv` columns:

```
pioneer_id, name, birth_year, death_year, nationality, primary_fields,
contributions_summary, key_ideas_json, representative_works_json,
fields_influenced, cross_trunk_impact, contemporaries, controversies,
source_ids, confidence, evidence_type
```

### Field definitions

- **pioneer_id** — Stable identifier of the form `PION_NNN`, zero-padded to 3 digits. Globally unique across all trunks (a pioneer can contribute to multiple trunks; they get one row).
- **name** — Common scholarly form of the name. For multi-author pseudonymous corpora (e.g. "Jabirian corpus"), use the corpus name and note multiple-authorship in `controversies`.
- **birth_year, death_year** — Signed integer years; use empty when unknown. For approximate dates, use the most defensible single year and note the uncertainty in `controversies` (the precision conventions in §9 also apply).
- **nationality** — Best-fit modern term, but flag when modern nationality is anachronistic (e.g., Avicenna as "Persian/Islamic" not "Iranian"). Note ambiguities in `controversies`.
- **primary_fields** — Free-text list of fields (e.g., "Natural Philosophy, Mathematics"). For structured field linkage use `pioneer_contributions.csv` (§13).
- **contributions_summary** — One- to three-sentence overview of what this pioneer is known for.
- **key_ideas_json** — JSON array of `{idea, date, description, work, impact}` objects. Each key idea is its own object. This is the structured spine of the pioneer's intellectual legacy. Quote the JSON literal in the CSV field.
- **representative_works_json** — JSON array of `{title, year, significance, nodes_influenced}` objects.
- **fields_influenced** — Comma-separated `node_id` list (mirrors the `pioneer_contributions.csv` join, kept here for quick reference).
- **cross_trunk_impact** — Free-text list of cross-trunk influences (e.g., "Trunk 1: developed calculus; Trunk 3: mathematized natural philosophy"). Structured cross-trunk edges live in `pioneer_contributions.csv`.
- **contemporaries** — Comma-separated `PION_NNN` references plus a short tag indicating the relationship (collaborator, rival, student, teacher). Example: `PION_002 (rival – priority dispute), PION_003 (collaborator)`.
- **controversies** — Anachronism flags, attribution disputes (e.g., Jabirian corpus authorship), credit allocation problems.
- **source_ids, confidence, evidence_type** — Same conventions as nodes (§2, §5, §6).

### JSON sub-structures (illustrative)

```json
"key_ideas_json": [
  {
    "idea": "Universal gravitation",
    "date": 1687,
    "description": "All matter attracts all other matter with force proportional to masses and inversely proportional to distance squared.",
    "work": "Philosophiae Naturalis Principia Mathematica",
    "impact": "Unified celestial and terrestrial mechanics."
  }
]
```

```json
"representative_works_json": [
  {
    "title": "Philosophiae Naturalis Principia Mathematica",
    "year": 1687,
    "significance": "Foundation of classical mechanics",
    "nodes_influenced": ["T3_EMD_003", "T1_EMD_002"]
  }
]
```

## 12. Breakthrough Schema (v2.0)

Breakthroughs are specific discoveries, inventions, concepts, methods, instruments, or formalizations that transformed fields. They are typically tied to one or more pioneers and to one or more nodes that they enabled, transformed, or contributed to.

`breakthroughs.csv` columns:

```
breakthrough_id, name, type, date_or_range, date_precision,
pioneers_involved, description, enabling_factors, fields_enabled,
fields_transformed, representative_publication_json, cascading_impact,
source_ids, confidence, evidence_type
```

### Field definitions

- **breakthrough_id** — Stable identifier `BRKTH_NNN`, zero-padded.
- **name** — Common scholarly name (e.g., "Transistor", "Backpropagation Algorithm", "Boolean Logic").
- **type** — One of:
  - `discovery` — empirical finding (DNA structure, radioactivity)
  - `invention` — new technology (telescope, transistor, PCR)
  - `concept` — new idea/framework (evolution, quantum mechanics, information theory)
  - `method` — new technique (calculus, statistical inference, sequencing)
  - `instrument` — tool enabling new observations (microscope, particle accelerator)
  - `formalization` — mathematical/logical framework (Boolean algebra, set theory)
- **date_or_range** — Either a single signed integer year (`1947`) or a range (`1900-1930`). Use ranges when the breakthrough is collective or accreted over time.
- **date_precision** — As in §9.
- **pioneers_involved** — Comma-separated `PION_NNN` references.
- **description** — One- to three-sentence summary of what the breakthrough is.
- **enabling_factors** — Comma-separated `BRKTH_NNN` references (this breakthrough's predecessors). Captures the cascade structure: Transistor's enabling factors include Quantum Mechanics and Semiconductor Physics.
- **fields_enabled** — Comma-separated `node_id` list (nodes for which the breakthrough was a precondition).
- **fields_transformed** — Comma-separated `node_id` list (existing nodes the breakthrough changed without enabling).
- **representative_publication_json** — JSON object `{title, authors, journal_or_publisher, year, doi}`.
- **cascading_impact** — Free-text description of downstream consequences (e.g., "→ Integrated circuits (1958) → Microprocessors (1971) → PCs (1980s) → Internet → AI revolution (2010s)").
- **source_ids, confidence, evidence_type** — Same as elsewhere.

## 13. Pioneer Contributions Schema (v2.0)

Many-to-many join table linking pioneers to the specific nodes they contributed to, with metadata about each contribution.

`pioneer_contributions.csv` columns:

```
contribution_id, pioneer_id, node_id, contribution_type,
specific_contribution, key_work, date, impact_level, source_ids
```

- **contribution_id** — Identifier `CONTR_NNN`.
- **pioneer_id** — `PION_NNN`.
- **node_id** — The field the contribution lands in.
- **contribution_type** — One of: `foundational_idea`, `mathematical_formulation`, `experimental_demonstration`, `institutionalization`, `synthesis`, `critique`, `methodological_innovation`, `instrumental_advance`.
- **specific_contribution** — One-sentence specific claim (e.g., "Formulated three laws of motion in *Principia* (1687)" — *not* "worked on physics").
- **key_work** — Citation pointing to one row in `pioneers.csv`'s `representative_works_json` (use the title verbatim).
- **date** — Year the contribution landed (signed integer; can be a range like `1665-1687`).
- **impact_level** — One of: `foundational`, `major`, `significant`, `contributory`. Helps visualization scale node weight.
- **source_ids** — Per usual.

The `contributed_by` edge relation (§4b) is the conceptual relation; this table is its storage.

## 14. Breakthrough Dependencies Schema (v2.0)

Many-to-many join table linking breakthroughs to the nodes they affect, with the relationship type and mechanism.

`breakthrough_dependencies.csv` columns:

```
dependency_id, breakthrough_id, node_id, relationship_type,
mechanism, quantitative_impact, source_ids
```

- **dependency_id** — `DEP_NNN`.
- **breakthrough_id** — `BRKTH_NNN`.
- **node_id** — Field this dependency targets.
- **relationship_type** — One of the three breakthrough-related relations (§4b): `enabled_by`, `transformed_by`, `contributed_to`.
- **mechanism** — One- to three-sentence explanation of *how* the breakthrough affected the field (e.g., "Transistors replaced vacuum tubes, enabling miniaturization, reliability, and cost reductions that made practical computing possible").
- **quantitative_impact** — Where measurable, a one-line quantitative statement (e.g., "Enabled computer size reduction by 100x, power by 1000x, cost by 10x"). Empty when not applicable.
- **source_ids** — Per usual.

## 15. ID conventions across all entity types

| Entity | Prefix | Example |
|--------|--------|---------|
| Node | `T{trunk}_{ERA}_{NNN}` | `T3_EMD_003` |
| Edge (node→node) | `T{trunk}_E_{NNN}` | `T3_E_017` |
| Source | `SRC_NNN` | `SRC_045` |
| Dispute | `DISP_NNN` | `DISP_005` |
| Pioneer | `PION_NNN` | `PION_198` |
| Breakthrough | `BRKTH_NNN` | `BRKTH_015` |
| Pioneer contribution (join) | `CONTR_NNN` | `CONTR_042` |
| Breakthrough dependency (join) | `DEP_NNN` | `DEP_073` |

All `NNN` numbers are zero-padded to 3 digits. Pioneers and breakthroughs are not trunk-prefixed because they routinely cross trunks. Cross-trunk node→node edges use the lower-numbered trunk's prefix.
