# Master Data Files

This directory holds the project's master data — the validated knowledge graph that survives audits and ships with the final deliverable.

## Files

| File | Owner | Schema source |
|------|-------|---------------|
| `nodes.csv` | Graph Builder | `00_project_instructions/core/ontology_definition.md` §2 |
| `edges.csv` | Graph Builder | `00_project_instructions/core/ontology_definition.md` §3 |
| `sources.csv` | Graph Builder | `00_project_instructions/core/ontology_definition.md` §7 |
| `disputed_claims.csv` | Graph Builder | `00_project_instructions/core/ontology_definition.md` §8 |
| `trunk_lineages/trunk_N_lineage.json` | Graph Builder | Per-trunk subset of the master files, for standalone use |

## Status (v1.0)

All four CSVs exist with the correct headers and zero data rows. The Graph Builder will append validated rows after each batch passes its Micro-Audit (Gate 1).

## Append rules

- Only the Graph Builder writes to these files.
- Only append rows; do not overwrite (unless explicitly told to revise a specific row).
- Preserve column order exactly. The header row in each file is authoritative.
- Quote any field containing a comma, a quote, or a newline (standard CSV escaping).
- After every commit, update `07_exports/changelog.md` with a one-line summary of what was added.
- After every commit, validate referential integrity: every `source_ids` reference must resolve to `sources.csv`; every `from_node` / `to_node` must resolve to `nodes.csv`.

## Validation script (pseudo-code)

Run before every commit (see `chat_specific/graph_builder_instructions.md` for the full reference):

```
node_ids = {row.node_id for row in nodes.csv}
source_ids = {row.source_id for row in sources.csv}

for row in new_nodes:
    for sid in row.source_ids.split(','):
        assert sid.strip() in source_ids, f"Node {row.node_id} cites unknown source {sid}"

for row in new_edges:
    assert row.from_node in node_ids
    assert row.to_node in node_ids
    for sid in row.source_ids.split(','):
        assert sid.strip() in source_ids
```

If any assertion fails, do not commit. Return to the Extractor.
