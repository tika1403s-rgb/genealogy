# Ontology Definition

**Version:** 1.0
**Last Updated:** 2026-05-20
**Status:** Active
**Affected chats:** all (canonical schema for nodes, edges, sources, disputes)

## Change Log
- v1.0 (2026-05-20): Initial version — node schema, edge schema, 5 event types, 10 relation types, A/B/C/D/X confidence, E1–E6 evidence.

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
confidence, evidence_type, controversies
```

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

**Rule:** Edges are typed. A vague "influenced" edge does not exist. If you cannot pick one of these ten, escalate to the Taxonomy Architect chat to consider adding a new type.

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
