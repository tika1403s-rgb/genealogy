"""
validation.py — Knowledge Genealogy Master Data Validator

Maps directly to audit_framework.md v1.1 (three-tier audit system).
Run before every Graph Builder commit (Gate 1) and during Phase/Macro Audits.

Usage:
    python validation.py [data_dir]          # full validation + macro metrics
    python validation.py [data_dir] --schema # schema only
    python validation.py [data_dir] --refs   # referential integrity only
    python validation.py [data_dir] --quality # quality rules only
    python validation.py [data_dir] --metrics # macro metrics only

Default data_dir: 04_nodes_edges (relative to working directory, or absolute path).

Exit code 0 = PASS (no errors), 1 = FAIL (errors present).
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ─────────────────────────────────────────────────────────────────────────────
# Constants from ontology_definition.md
# ─────────────────────────────────────────────────────────────────────────────

VALID_EVENT_TYPES = {
    "first_problem_tradition",
    "conceptual_breakthrough",
    "named_field",
    "institutionalized_field",
    "modern_formulation",
}

VALID_NODE_TYPES = {
    "knowledge_tradition",
    "field",
    "subfield",
    "method",
    "theoretical_framework",
    "instrument_enabled_practice",
}

# §4a: only these 10 types go in edges.csv (node-to-node)
VALID_EDGE_RELATION_TYPES = {
    "emerged_from",
    "split_from",
    "merged_with",
    "renamed_as",
    "formalized_by",
    "mathematized_by",
    "institutionalized_as",
    "method_imported_from",
    "instrument_enabled",
    "problem_domain_shared_with",
}

VALID_CONFIDENCE = {"A", "B", "C", "D", "X"}
VALID_EVIDENCE_TYPES = {"E1", "E2", "E3", "E4", "E5", "E6"}
VALID_DATE_PRECISION = {"year", "decade", "century", "era"}

VALID_REGIONS = {
    "Greek", "Hellenistic", "Chinese", "Indian", "Islamic",
    "European", "African", "Indigenous", "Global",
}
NON_EUROPEAN_REGIONS = {"Greek", "Hellenistic", "Chinese", "Indian", "Islamic", "African", "Indigenous", "Global"}

VALID_TRUNK_IDS = {str(i) for i in range(1, 11)}

VALID_BREAKTHROUGH_TYPES = {
    "discovery", "invention", "concept", "method", "instrument", "formalization",
}

VALID_CONTRIBUTION_TYPES = {
    "foundational_idea",
    "mathematical_formulation",
    "experimental_demonstration",
    "institutionalization",
    "synthesis",
    "critique",
    "methodological_innovation",
    "instrumental_advance",
}

VALID_BREAKTHROUGH_RELATION_TYPES = {"enabled_by", "transformed_by", "contributed_to"}

VALID_IMPACT_LEVELS = {"foundational", "major", "significant", "contributory"}

# never_do_this.md rule 2: forbidden in label for pre-1700 nodes without controversies
MODERN_LABELS_FORBIDDEN_PRE_1700 = {
    "physics", "chemistry", "biology", "psychology",
    "sociology", "economics", "computer science",
}

# Era boundary cutoffs (date_start)
ANCIENT_MEDIEVAL_CUTOFF = 1500   # ≤1500 = ancient or medieval
MEDIEVAL_START = 500
MEDIEVAL_END = 1500
MODERN_ERA_START = 1800          # ≥1800 = modern or contemporary (for breakthrough check)
CONTEMPORARY_START = 1950        # ≥1950 = contemporary (for cross-trunk check)

# Vague phrases banned in pioneer_contributions.specific_contribution
VAGUE_CONTRIBUTION_PHRASES = [
    "worked on",
    "contributed to",
    "influenced",
    "involved in",
    "helped with",
    "participated in",
    "studied",
    "researched",
]

# ID format patterns (§15)
NODE_ID_RE = re.compile(r"^T\d+_(ANC|MED|EMD|MOD|CON)_\d{3}$")
EDGE_ID_RE = re.compile(r"^T\d+_E_\d{3}$")
PION_ID_RE = re.compile(r"^PION_\d{3}$")
BRKTH_ID_RE = re.compile(r"^BRKTH_\d{3}$")
SRC_ID_RE = re.compile(r"^SRC_\d{3}$")
CONTR_ID_RE = re.compile(r"^CONTR_\d{3}$")
DEP_ID_RE = re.compile(r"^DEP_\d{3}$")
DISP_ID_RE = re.compile(r"^DISP_\d{3}$")


# ─────────────────────────────────────────────────────────────────────────────
# Issue tracking
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Issue:
    severity: str    # "ERROR" | "WARNING" | "INFO"
    category: str    # audit check name
    entity_id: str   # which row triggered the issue
    message: str


@dataclass
class ValidationReport:
    issues: list[Issue] = field(default_factory=list)

    def error(self, category: str, entity_id: str, message: str) -> None:
        self.issues.append(Issue("ERROR", category, entity_id, message))

    def warn(self, category: str, entity_id: str, message: str) -> None:
        self.issues.append(Issue("WARNING", category, entity_id, message))

    def info(self, category: str, entity_id: str, message: str) -> None:
        self.issues.append(Issue("INFO", category, entity_id, message))

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "ERROR"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "WARNING"]

    def summary(self) -> str:
        e = len(self.errors)
        w = len(self.warnings)
        return f"Validation: {e} error(s), {w} warning(s)"

    def passed(self) -> bool:
        """True iff no errors (Gate 1 equivalent)."""
        return len(self.errors) == 0

    def print_report(self) -> None:
        print(self.summary())
        if self.errors:
            print("\n=== ERRORS (block commit) ===")
            for i in self.errors:
                print(f"  [{i.category}] {i.entity_id}: {i.message}")
        if self.warnings:
            print("\n=== WARNINGS (review required) ===")
            for i in self.warnings:
                print(f"  [{i.category}] {i.entity_id}: {i.message}")


# ─────────────────────────────────────────────────────────────────────────────
# CSV loading helpers
# ─────────────────────────────────────────────────────────────────────────────

def _load_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _split_ids(value: str) -> list[str]:
    """Split a comma-separated ID field, stripping whitespace, skipping blanks."""
    if not value or not value.strip():
        return []
    return [s.strip() for s in value.split(",") if s.strip()]


def _to_int(value: str) -> Optional[int]:
    try:
        return int(str(value).strip())
    except (ValueError, AttributeError, TypeError):
        return None


def _check_duplicate_ids(rows: list[dict], id_field: str, table: str, report: ValidationReport) -> None:
    seen: Counter = Counter(r.get(id_field, "").strip() for r in rows)
    for id_val, count in seen.items():
        if count > 1 and id_val:
            report.error(
                "referential_integrity",
                id_val,
                f"Duplicate {id_field} in {table} ({count} rows). Pioneers and breakthroughs are globally unique.",
            )


# ─────────────────────────────────────────────────────────────────────────────
# 1. Schema compliance  (ontology_definition.md §2–§14, §15)
# ─────────────────────────────────────────────────────────────────────────────

def check_schema_compliance(data_dir: Path, report: ValidationReport) -> None:
    """
    Verify every row matches its schema from ontology_definition.md.
    Covers required fields, enum values, ID format patterns, date logic, JSON validity.
    """
    _check_nodes_schema(_load_csv(data_dir / "nodes.csv"), report)
    _check_edges_schema(_load_csv(data_dir / "edges.csv"), report)
    _check_pioneers_schema(_load_csv(data_dir / "pioneers.csv"), report)
    _check_breakthroughs_schema(_load_csv(data_dir / "breakthroughs.csv"), report)
    _check_pioneer_contribs_schema(_load_csv(data_dir / "pioneer_contributions.csv"), report)
    _check_breakthrough_deps_schema(_load_csv(data_dir / "breakthrough_dependencies.csv"), report)
    _check_sources_schema(_load_csv(data_dir / "sources.csv"), report)
    _check_disputes_schema(_load_csv(data_dir / "disputed_claims.csv"), report)


def _check_nodes_schema(nodes: list[dict], report: ValidationReport) -> None:
    required = [
        "node_id", "label", "type", "trunk_id", "date_start", "date_end",
        "date_precision", "creation_event_type", "region",
        "description", "core_idea", "source_ids", "confidence", "evidence_type",
    ]
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", nid, f"Missing required field '{f}'")

        if not NODE_ID_RE.match(nid):
            report.error("schema", nid, f"node_id '{nid}' must match T{{trunk}}_{{ERA}}_{{NNN}} (e.g. T3_ANC_001)")

        _check_enum(row, "type", VALID_NODE_TYPES, nid, report)
        _check_enum(row, "creation_event_type", VALID_EVENT_TYPES, nid, report)
        _check_enum(row, "confidence", VALID_CONFIDENCE, nid, report)
        _check_enum(row, "date_precision", VALID_DATE_PRECISION, nid, report)

        trunk = row.get("trunk_id", "").strip()
        if trunk and trunk not in VALID_TRUNK_IDS:
            report.error("schema", nid, f"trunk_id '{trunk}' must be 1–10")

        for reg in _split_ids(row.get("region", "")):
            if reg not in VALID_REGIONS:
                report.warn("schema", nid, f"Unrecognized region value '{reg}'")

        for et in _split_ids(row.get("evidence_type", "")):
            if et not in VALID_EVIDENCE_TYPES:
                report.error("schema", nid, f"Invalid evidence_type '{et}' (must be E1–E6)")

        _check_date_range(row, nid, report)


def _check_edges_schema(edges: list[dict], report: ValidationReport) -> None:
    required = [
        "edge_id", "from_node", "to_node", "relation_type",
        "explanation", "source_ids", "confidence", "evidence_type",
    ]
    for row in edges:
        eid = row.get("edge_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", eid, f"Missing required field '{f}'")

        if not EDGE_ID_RE.match(eid):
            report.error("schema", eid, f"edge_id '{eid}' must match T{{trunk}}_E_{{NNN}} (e.g. T3_E_017)")

        rt = row.get("relation_type", "").strip()
        if rt and rt not in VALID_EDGE_RELATION_TYPES:
            report.error(
                "schema", eid,
                f"Invalid relation_type '{rt}'. Use one of the 10 approved node-to-node types. "
                "Pioneer/breakthrough relations go in join tables, not edges.csv."
            )

        _check_enum(row, "confidence", VALID_CONFIDENCE, eid, report)
        _check_enum(row, "date_precision", VALID_DATE_PRECISION, eid, report, required=False)

        for et in _split_ids(row.get("evidence_type", "")):
            if et not in VALID_EVIDENCE_TYPES:
                report.error("schema", eid, f"Invalid evidence_type '{et}'")


def _check_pioneers_schema(pioneers: list[dict], report: ValidationReport) -> None:
    required = [
        "pioneer_id", "name", "contributions_summary",
        "key_ideas_json", "representative_works_json",
        "source_ids", "confidence", "evidence_type",
    ]
    for row in pioneers:
        pid = row.get("pioneer_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", pid, f"Missing required field '{f}'")

        if not PION_ID_RE.match(pid):
            report.error("schema", pid, f"pioneer_id '{pid}' must match PION_NNN (e.g. PION_001)")

        _check_enum(row, "confidence", VALID_CONFIDENCE, pid, report)

        for json_field in ("key_ideas_json", "representative_works_json"):
            _check_json_field(row, json_field, pid, report)

        for et in _split_ids(row.get("evidence_type", "")):
            if et not in VALID_EVIDENCE_TYPES:
                report.error("schema", pid, f"Invalid evidence_type '{et}'")


def _check_breakthroughs_schema(breakthroughs: list[dict], report: ValidationReport) -> None:
    required = [
        "breakthrough_id", "name", "type", "date_or_range", "date_precision",
        "description", "source_ids", "confidence", "evidence_type",
    ]
    for row in breakthroughs:
        bid = row.get("breakthrough_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", bid, f"Missing required field '{f}'")

        if not BRKTH_ID_RE.match(bid):
            report.error("schema", bid, f"breakthrough_id '{bid}' must match BRKTH_NNN (e.g. BRKTH_001)")

        _check_enum(row, "type", VALID_BREAKTHROUGH_TYPES, bid, report)
        _check_enum(row, "confidence", VALID_CONFIDENCE, bid, report)
        _check_enum(row, "date_precision", VALID_DATE_PRECISION, bid, report)

        for et in _split_ids(row.get("evidence_type", "")):
            if et not in VALID_EVIDENCE_TYPES:
                report.error("schema", bid, f"Invalid evidence_type '{et}'")

        _check_json_field(row, "representative_publication_json", bid, report, required=False)


def _check_pioneer_contribs_schema(rows: list[dict], report: ValidationReport) -> None:
    required = [
        "contribution_id", "pioneer_id", "node_id",
        "contribution_type", "specific_contribution", "key_work",
        "date", "impact_level", "source_ids",
    ]
    for row in rows:
        cid = row.get("contribution_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", cid, f"Missing required field '{f}'")

        if not CONTR_ID_RE.match(cid):
            report.error("schema", cid, f"contribution_id '{cid}' must match CONTR_NNN")

        _check_enum(row, "contribution_type", VALID_CONTRIBUTION_TYPES, cid, report)
        _check_enum(row, "impact_level", VALID_IMPACT_LEVELS, cid, report)


def _check_breakthrough_deps_schema(rows: list[dict], report: ValidationReport) -> None:
    required = [
        "dependency_id", "breakthrough_id", "node_id",
        "relationship_type", "mechanism", "source_ids",
    ]
    for row in rows:
        did = row.get("dependency_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", did, f"Missing required field '{f}'")

        if not DEP_ID_RE.match(did):
            report.error("schema", did, f"dependency_id '{did}' must match DEP_NNN")

        _check_enum(row, "relationship_type", VALID_BREAKTHROUGH_RELATION_TYPES, did, report)


def _check_sources_schema(sources: list[dict], report: ValidationReport) -> None:
    required = [
        "source_id", "title", "author", "year",
        "publisher_or_journal", "evidence_type",
    ]
    for row in sources:
        sid = row.get("source_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", sid, f"Missing required field '{f}'")

        if not SRC_ID_RE.match(sid):
            report.error("schema", sid, f"source_id '{sid}' must match SRC_NNN (e.g. SRC_001)")

        for et in _split_ids(row.get("evidence_type", "")):
            if et not in VALID_EVIDENCE_TYPES:
                report.error("schema", sid, f"Invalid evidence_type '{et}'")


def _check_disputes_schema(rows: list[dict], report: ValidationReport) -> None:
    required = ["dispute_id", "related_node_or_edge_id", "question", "position_a", "status"]
    for row in rows:
        did = row.get("dispute_id", "UNKNOWN").strip()

        for f in required:
            if not row.get(f, "").strip():
                report.error("schema", did, f"Missing required field '{f}'")

        if not DISP_ID_RE.match(did):
            report.error("schema", did, f"dispute_id '{did}' must match DISP_NNN")


# Schema sub-helpers

def _check_enum(
    row: dict,
    field: str,
    valid_set: set[str],
    entity_id: str,
    report: ValidationReport,
    required: bool = True,
) -> None:
    val = row.get(field, "").strip()
    if not val:
        return  # required-field check is handled separately
    if val not in valid_set:
        severity = report.error if required else report.warn
        severity("schema", entity_id, f"Invalid {field} '{val}' (valid: {sorted(valid_set)})")


def _check_date_range(row: dict, entity_id: str, report: ValidationReport) -> None:
    ds = _to_int(row.get("date_start", ""))
    de_raw = row.get("date_end", "").strip()

    if row.get("date_start", "").strip() and ds is None:
        report.error("schema", entity_id, "date_start must be a signed integer (e.g. -600, 1687)")

    if de_raw and de_raw != "present":
        de = _to_int(de_raw)
        if de is None:
            report.error("schema", entity_id, "date_end must be a signed integer or 'present'")
        elif ds is not None and de is not None and de < ds:
            report.error("schema", entity_id, f"date_end ({de}) is before date_start ({ds})")


def _check_json_field(
    row: dict,
    field: str,
    entity_id: str,
    report: ValidationReport,
    required: bool = True,
) -> None:
    raw = row.get(field, "").strip()
    if not raw:
        return
    try:
        json.loads(raw)
    except json.JSONDecodeError as e:
        report.error("schema", entity_id, f"Invalid JSON in '{field}': {e}")


# ─────────────────────────────────────────────────────────────────────────────
# 2. Referential integrity  (ontology_definition.md §15; 04_nodes_edges/README.md)
# ─────────────────────────────────────────────────────────────────────────────

def check_referential_integrity(data_dir: Path, report: ValidationReport) -> None:
    """
    Verify every foreign-key reference resolves to an existing entity.
    Blocks commit if any reference is broken (Gate 1 enforcement).
    """
    nodes = _load_csv(data_dir / "nodes.csv")
    edges = _load_csv(data_dir / "edges.csv")
    pioneers = _load_csv(data_dir / "pioneers.csv")
    breakthroughs = _load_csv(data_dir / "breakthroughs.csv")
    pioneer_contribs = _load_csv(data_dir / "pioneer_contributions.csv")
    breakthrough_deps = _load_csv(data_dir / "breakthrough_dependencies.csv")
    sources = _load_csv(data_dir / "sources.csv")

    node_ids = {r.get("node_id", "").strip() for r in nodes} - {""}
    pioneer_ids = {r.get("pioneer_id", "").strip() for r in pioneers} - {""}
    breakthrough_ids = {r.get("breakthrough_id", "").strip() for r in breakthroughs} - {""}
    source_ids = {r.get("source_id", "").strip() for r in sources} - {""}

    # Duplicate-ID checks (never_do_this.md rule 13)
    _check_duplicate_ids(nodes, "node_id", "nodes.csv", report)
    _check_duplicate_ids(edges, "edge_id", "edges.csv", report)
    _check_duplicate_ids(pioneers, "pioneer_id", "pioneers.csv", report)
    _check_duplicate_ids(breakthroughs, "breakthrough_id", "breakthroughs.csv", report)
    _check_duplicate_ids(pioneer_contribs, "contribution_id", "pioneer_contributions.csv", report)
    _check_duplicate_ids(breakthrough_deps, "dependency_id", "breakthrough_dependencies.csv", report)
    _check_duplicate_ids(sources, "source_id", "sources.csv", report)

    def _src_refs(row: dict, eid: str) -> None:
        for sid in _split_ids(row.get("source_ids", "")):
            if sid not in source_ids:
                report.error("referential_integrity", eid, f"Unknown source_id '{sid}' (not in sources.csv)")

    def _id_refs(raw: str, eid: str, ref_set: set[str], ref_type: str) -> None:
        for ref in _split_ids(raw):
            if ref not in ref_set:
                report.error("referential_integrity", eid, f"Unknown {ref_type} '{ref}'")

    # nodes.csv foreign keys
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        _src_refs(row, nid)
        _id_refs(row.get("pioneer_ids", ""), nid, pioneer_ids, "pioneer_id in nodes.pioneer_ids")
        _id_refs(row.get("enabling_breakthrough_ids", ""), nid, breakthrough_ids, "breakthrough_id in nodes.enabling_breakthrough_ids")
        _id_refs(row.get("transforming_breakthrough_ids", ""), nid, breakthrough_ids, "breakthrough_id in nodes.transforming_breakthrough_ids")

    # edges.csv foreign keys
    for row in edges:
        eid = row.get("edge_id", "UNKNOWN").strip()
        _src_refs(row, eid)
        fn = row.get("from_node", "").strip()
        tn = row.get("to_node", "").strip()
        if fn and fn not in node_ids:
            report.error("referential_integrity", eid, f"from_node '{fn}' not in nodes.csv")
        if tn and tn not in node_ids:
            report.error("referential_integrity", eid, f"to_node '{tn}' not in nodes.csv")

    # pioneers.csv foreign keys
    for row in pioneers:
        pid = row.get("pioneer_id", "UNKNOWN").strip()
        _src_refs(row, pid)
        # NOTE: pioneers.fields_influenced is free-text (human-readable field names,
        # not node_ids). Structured linkage is via pioneer_contributions.csv.

    # breakthroughs.csv foreign keys
    for row in breakthroughs:
        bid = row.get("breakthrough_id", "UNKNOWN").strip()
        _src_refs(row, bid)
        _id_refs(row.get("enabling_factors", ""), bid, breakthrough_ids, "breakthrough_id in breakthroughs.enabling_factors")
        # NOTE: pioneers_involved is free-text (human-readable names, not PION_NNN IDs).
        # Structured linkage is via pioneer_contributions.csv.
        _id_refs(row.get("fields_enabled", ""), bid, node_ids, "node_id in breakthroughs.fields_enabled")
        _id_refs(row.get("fields_transformed", ""), bid, node_ids, "node_id in breakthroughs.fields_transformed")

    # pioneer_contributions.csv foreign keys
    for row in pioneer_contribs:
        cid = row.get("contribution_id", "UNKNOWN").strip()
        _src_refs(row, cid)
        pid = row.get("pioneer_id", "").strip()
        nid = row.get("node_id", "").strip()
        if pid and pid not in pioneer_ids:
            report.error("referential_integrity", cid, f"pioneer_id '{pid}' not in pioneers.csv")
        if nid and nid not in node_ids:
            report.error("referential_integrity", cid, f"node_id '{nid}' not in nodes.csv")

    # breakthrough_dependencies.csv foreign keys
    for row in breakthrough_deps:
        did = row.get("dependency_id", "UNKNOWN").strip()
        _src_refs(row, did)
        bid = row.get("breakthrough_id", "").strip()
        nid = row.get("node_id", "").strip()
        if bid and bid not in breakthrough_ids:
            report.error("referential_integrity", did, f"breakthrough_id '{bid}' not in breakthroughs.csv")
        if nid and nid not in node_ids:
            report.error("referential_integrity", did, f"node_id '{nid}' not in nodes.csv")


# ─────────────────────────────────────────────────────────────────────────────
# 3. Quality rules  (audit_framework.md §3 checks 1–9; evolving_rules/)
# ─────────────────────────────────────────────────────────────────────────────

def check_quality_rules(data_dir: Path, report: ValidationReport) -> None:
    """
    Enforce behavioral rules from audit_framework.md, always_do_this.md, never_do_this.md.
    Maps to the nine Micro-Audit checks (§3).
    """
    nodes = _load_csv(data_dir / "nodes.csv")
    pioneers = _load_csv(data_dir / "pioneers.csv")
    pioneer_contribs = _load_csv(data_dir / "pioneer_contributions.csv")
    sources = _load_csv(data_dir / "sources.csv")

    check_presentism(nodes, report)
    check_founder_mythology(nodes, report)
    check_date_precision(nodes, report)
    check_confidence_inflation(nodes, pioneers, sources, report)
    check_evidence_type_rules(nodes, report)
    check_geographic_bias(nodes, report)
    check_source_completeness(nodes, report)
    check_pioneer_coverage(nodes, report)
    check_pioneer_contribution_specificity(pioneer_contribs, report)
    check_breakthrough_coverage(nodes, report)


def check_presentism(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 1 / never_do_this.md rule 2:
    Modern field names on ancient/medieval nodes require a controversies flag.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        ds = _to_int(row.get("date_start", ""))
        label = row.get("label", "").lower()
        controversies = row.get("controversies", "").strip()

        if ds is None:
            continue

        if ds <= ANCIENT_MEDIEVAL_CUTOFF:
            for forbidden in MODERN_LABELS_FORBIDDEN_PRE_1700:
                if forbidden in label and not controversies:
                    report.error(
                        "presentism", nid,
                        f"Modern label '{forbidden}' on pre-1501 node with no controversies flag. "
                        "Use a period-appropriate term (e.g. 'natural philosophy' not 'physics') "
                        "or note the anachronism in 'controversies'."
                    )
        elif ds < 1700:
            for forbidden in MODERN_LABELS_FORBIDDEN_PRE_1700:
                if forbidden in label and not controversies:
                    report.warn(
                        "presentism", nid,
                        f"Modern label '{forbidden}' on pre-1700 node without retrospection note in 'controversies'."
                    )


def check_founder_mythology(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 2 / never_do_this.md rule 1 / always_do_this.md rules 6–7, 11:
    - Forbidden language: 'founder', 'founded'.
    - Single pioneer entries flagged.
    - Target: 3+ pioneer_ids per node.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        pioneers_text = row.get("pioneers", "").lower()
        description_text = row.get("description", "").lower()
        pioneer_ids_raw = _split_ids(row.get("pioneer_ids", ""))
        controversies = row.get("controversies", "").strip().lower()

        for text_field, text in [("pioneers", pioneers_text), ("description", description_text)]:
            if "founded by" in text or "founder of" in text or "the founder" in text:
                report.error(
                    "founder_mythology", nid,
                    f"Forbidden language in '{text_field}': 'founder'/'founded by'. "
                    "Use 'associated pioneers' (plural)."
                )

        # Fewer than 3 pioneers (rule 11): warn unless exception documented
        documented_exception = any(kw in controversies for kw in ("attribution gap", "no named", "fewer", "single"))
        if len(pioneer_ids_raw) < 3 and not documented_exception:
            if len(pioneer_ids_raw) == 0:
                report.warn(
                    "founder_mythology", nid,
                    "No pioneer_ids. Target: 3+ per node. Document exceptions in 'controversies'."
                )
            else:
                report.warn(
                    "founder_mythology", nid,
                    f"Only {len(pioneer_ids_raw)} pioneer_id(s); target is 3+. "
                    "Document exceptions in 'controversies'."
                )


def check_date_precision(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 3 / never_do_this.md rule 6 / always_do_this.md rule 3:
    - date_precision required on every node.
    - 'year' precision for pre-1500 events requires institutional or publication evidence.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        ds = _to_int(row.get("date_start", ""))
        precision = row.get("date_precision", "").strip()

        if not precision:
            report.error("date_precision", nid, "date_precision is required on every node (year/decade/century/era)")
            continue

        if ds is not None and ds < 1500 and precision == "year":
            inst = row.get("institutional_markers", "").strip()
            rep_works = row.get("representative_works", "").strip()
            if not inst and not rep_works:
                report.warn(
                    "date_precision", nid,
                    f"'year' precision on pre-1500 node without institutional_markers or representative_works. "
                    "Consider 'century' or 'era' (never_do_this.md rule 6)."
                )


def check_confidence_inflation(
    nodes: list[dict],
    pioneers: list[dict],
    sources: list[dict],
    report: ValidationReport,
) -> None:
    """
    Micro-Audit check 4 / never_do_this.md rule 4 / always_do_this.md rule 1:
    Confidence A requires at least two independent E2 sources.
    """
    source_evidence: dict[str, str] = {
        r.get("source_id", "").strip(): r.get("evidence_type", "").strip()
        for r in sources
        if r.get("source_id", "").strip()
    }

    def _e2_count(source_ids_raw: str) -> int:
        return sum(
            1 for sid in _split_ids(source_ids_raw)
            if "E2" in source_evidence.get(sid, "")
        )

    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        if row.get("confidence", "").strip() == "A" and _e2_count(row.get("source_ids", "")) < 2:
            report.error(
                "confidence_inflation", nid,
                "Confidence A requires ≥2 independent E2 sources. "
                "Downgrade to B or add more scholarly sources."
            )

    for row in pioneers:
        pid = row.get("pioneer_id", "UNKNOWN").strip()
        if row.get("confidence", "").strip() == "A" and _e2_count(row.get("source_ids", "")) < 2:
            report.error(
                "confidence_inflation", pid,
                "Pioneer confidence A requires ≥2 independent E2 sources."
            )


def check_evidence_type_rules(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 5 / never_do_this.md rule 5:
    E6 (classification system) must never be the sole evidence type.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        et_list = _split_ids(row.get("evidence_type", ""))
        if et_list == ["E6"]:
            report.error(
                "evidence_type", nid,
                "E6 (OECD/UNESCO/LoC classification) is the only evidence type. "
                "Add E2 or E3 scholarly sources. E6 is never sufficient alone."
            )


def check_geographic_bias(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 6 / never_do_this.md rule 12 / always_do_this.md rule 4:
    Every node must have a non-empty region field.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        if not row.get("region", "").strip():
            report.error(
                "geographic_bias", nid,
                "region field is required. Assign one or more of: "
                "Greek, Hellenistic, Chinese, Indian, Islamic, European, African, Indigenous, Global."
            )


def check_source_completeness(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 7 / always_do_this.md rule 2:
    Every node needs source_ids. Target: 2+ distinct sources.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        src_ids = _split_ids(row.get("source_ids", ""))
        if not src_ids:
            report.error(
                "source_completeness", nid,
                "No source_ids. Every node requires at least one cited source."
            )
        elif len(src_ids) == 1:
            report.warn(
                "source_completeness", nid,
                "Only 1 source cited. Target 2+ distinct sources for better coverage."
            )


def check_pioneer_coverage(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 8 / always_do_this.md rule 11 / never_do_this.md rule 15:
    Every node should have 3+ pioneer_ids, or document the gap in controversies.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        pioneer_ids_raw = _split_ids(row.get("pioneer_ids", ""))
        controversies = row.get("controversies", "").strip().lower()
        documented = any(kw in controversies for kw in ("attribution gap", "no named", "fewer", "single", "record is thin"))

        if len(pioneer_ids_raw) < 3 and not documented:
            report.warn(
                "pioneer_coverage", nid,
                f"{len(pioneer_ids_raw)} pioneer_id(s) found; target is 3+. "
                "Document exceptions in 'controversies' (e.g. 'attribution gap — historical record is thin')."
            )


def check_pioneer_contribution_specificity(pioneer_contribs: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 8 (specificity sub-check) / never_do_this.md rule 14 / always_do_this.md rule 12:
    Pioneer contributions must be specific and dated — no vague language.
    """
    for row in pioneer_contribs:
        cid = row.get("contribution_id", "UNKNOWN").strip()
        contrib = row.get("specific_contribution", "").lower()

        for phrase in VAGUE_CONTRIBUTION_PHRASES:
            if phrase in contrib:
                report.error(
                    "pioneer_specificity", cid,
                    f"Vague contribution language ('{phrase}') in specific_contribution. "
                    "Required: a one-sentence dated claim citing a specific work or result. "
                    "Example: 'Formulated three laws of motion in Principia (1687)' — not 'worked on mechanics'."
                )
                break  # one error per row is enough


def check_breakthrough_coverage(nodes: list[dict], report: ValidationReport) -> None:
    """
    Micro-Audit check 9 / always_do_this.md rule 13 / never_do_this.md rule 15:
    Modern and contemporary nodes (date_start ≥ 1800) require 2+ enabling_breakthrough_ids.
    """
    for row in nodes:
        nid = row.get("node_id", "UNKNOWN").strip()
        ds = _to_int(row.get("date_start", ""))
        if ds is None or ds < MODERN_ERA_START:
            continue

        bids = _split_ids(row.get("enabling_breakthrough_ids", ""))
        controversies = row.get("controversies", "").strip().lower()
        documented = "no discrete enabling" in controversies or "long tradition" in controversies

        if len(bids) < 2 and not documented:
            report.warn(
                "breakthrough_coverage", nid,
                f"{len(bids)} enabling_breakthrough_id(s); target is 2+ for modern/contemporary nodes. "
                "Document exceptions in 'controversies' (e.g. 'no discrete enabling technology — emerged through long tradition')."
            )


# ─────────────────────────────────────────────────────────────────────────────
# 4. Macro-Audit quantitative metrics  (audit_framework.md §6)
# ─────────────────────────────────────────────────────────────────────────────

def compute_macro_metrics(data_dir: Path) -> dict:
    """
    Compute the 9 quantitative Macro-Audit metrics from audit_framework.md §6.
    Returns a dict suitable for saving as {trunk}_metrics.json.

    Note on cross-trunk enabler completeness (metric 9): this function checks
    whether contemporary nodes have *any* enabling_breakthrough_ids. Full cross-trunk
    verification requires knowing which trunk each breakthrough belongs to, which
    requires inspecting breakthrough node_id prefixes or a trunk field. Flag any
    contemporary node with zero enablers; full cross-trunk audit is manual.
    """
    nodes = _load_csv(data_dir / "nodes.csv")
    sources = _load_csv(data_dir / "sources.csv")

    if not nodes:
        return {"error": "No nodes found. Metrics cannot be computed."}

    total = len(nodes)

    am_nodes = [n for n in nodes if _era_is_ancient_medieval(n)]
    med_nodes = [n for n in nodes if _era_is_medieval(n)]
    mod_con_nodes = [n for n in nodes if _era_is_modern_or_contemporary(n)]
    con_nodes = [n for n in nodes if _era_is_contemporary(n)]

    # 1. Presentism score
    presentism_violations = sum(1 for n in am_nodes if _has_presentism_violation(n))
    presentism_score = (presentism_violations / len(am_nodes) * 100) if am_nodes else 0.0

    # 2. Founder mythology score
    single_pioneer_nodes = sum(
        1 for n in nodes if len(_split_ids(n.get("pioneer_ids", ""))) == 1
    )
    founder_mythology_score = (single_pioneer_nodes / total * 100) if total else 0.0

    # 3. Taxonomy bias score
    e6_only_nodes = sum(1 for n in nodes if _split_ids(n.get("evidence_type", "")) == ["E6"])
    taxonomy_bias_score = (e6_only_nodes / total * 100) if total else 0.0

    # 4. Source diversity score
    two_plus_sources = sum(1 for n in nodes if len(_split_ids(n.get("source_ids", ""))) >= 2)
    source_diversity_score = (two_plus_sources / total * 100) if total else 0.0

    # 5. Confidence realism (B+C %)
    confidence_counts: Counter = Counter(n.get("confidence", "").strip() for n in nodes)
    bc_count = confidence_counts["B"] + confidence_counts["C"]
    confidence_realism = (bc_count / total * 100) if total else 0.0
    a_pct = (confidence_counts["A"] / total * 100) if total else 0.0
    d_pct = (confidence_counts["D"] / total * 100) if total else 0.0

    # 6. Geographic diversity (medieval)
    non_european_med = sum(1 for n in med_nodes if _has_non_european_region(n))
    geographic_diversity_medieval = (non_european_med / len(med_nodes) * 100) if med_nodes else 0.0

    # 7. Pioneer coverage
    pioneer_covered = sum(1 for n in nodes if _has_adequate_pioneer_coverage(n))
    pioneer_coverage_score = (pioneer_covered / total * 100) if total else 0.0

    # 8. Breakthrough coverage (modern + contemporary only)
    breakthrough_covered = sum(
        1 for n in mod_con_nodes if len(_split_ids(n.get("enabling_breakthrough_ids", ""))) >= 2
    )
    breakthrough_coverage_score = (breakthrough_covered / len(mod_con_nodes) * 100) if mod_con_nodes else 0.0

    # 9. Cross-trunk enabler completeness (contemporary nodes with ≥1 enabler)
    con_with_any_enabler = sum(
        1 for n in con_nodes if len(_split_ids(n.get("enabling_breakthrough_ids", ""))) > 0
    )
    cross_trunk_score = (con_with_any_enabler / len(con_nodes) * 100) if con_nodes else 100.0

    return {
        "presentism_score_pct": round(presentism_score, 1),
        "founder_mythology_score_pct": round(founder_mythology_score, 1),
        "taxonomy_bias_score_pct": round(taxonomy_bias_score, 1),
        "source_diversity_score_pct": round(source_diversity_score, 1),
        "confidence_realism_bc_pct": round(confidence_realism, 1),
        "confidence_a_pct": round(a_pct, 1),
        "confidence_d_pct": round(d_pct, 1),
        "geographic_diversity_medieval_pct": round(geographic_diversity_medieval, 1),
        "pioneer_coverage_score_pct": round(pioneer_coverage_score, 1),
        "breakthrough_coverage_score_pct": round(breakthrough_coverage_score, 1),
        "cross_trunk_enabler_completeness_pct": round(cross_trunk_score, 1),
        "cross_trunk_note": (
            "Metric 9 counts contemporary nodes with ≥1 enabling_breakthrough_id. "
            "Full cross-trunk verification (that enablers span multiple trunks) requires manual review."
        ),
        "totals": {
            "all_nodes": total,
            "ancient_medieval": len(am_nodes),
            "medieval": len(med_nodes),
            "modern_contemporary": len(mod_con_nodes),
            "contemporary": len(con_nodes),
        },
    }


def evaluate_macro_metrics(metrics: dict) -> dict[str, str]:
    """
    Map computed metric values to TARGET / CRITICAL / FAIL status per audit_framework.md §6.
    Returns {metric_name: status_string}.
    """
    if "error" in metrics:
        return {}

    def lower_better(val: float, target_max: float, critical_max: float) -> str:
        if val < target_max:
            return "TARGET"
        if val < critical_max:
            return "CRITICAL"
        return "FAIL"

    def higher_better(val: float, target_min: float, critical_min: float) -> str:
        if val > target_min:
            return "TARGET"
        if val > critical_min:
            return "CRITICAL"
        return "FAIL"

    bc = metrics["confidence_realism_bc_pct"]
    a = metrics["confidence_a_pct"]
    d = metrics["confidence_d_pct"]
    if 50 <= bc <= 70:
        confidence_status = "TARGET"
    elif a > 50 or d > 40:
        confidence_status = "FAIL"
    elif 40 <= bc <= 80:
        confidence_status = "CRITICAL"
    else:
        confidence_status = "FAIL"

    return {
        "presentism_score": lower_better(metrics["presentism_score_pct"], 10, 15),
        "founder_mythology": lower_better(metrics["founder_mythology_score_pct"], 30, 40),
        "taxonomy_bias": lower_better(metrics["taxonomy_bias_score_pct"], 0.001, 5),
        "source_diversity": higher_better(metrics["source_diversity_score_pct"], 90, 80),
        "confidence_realism": confidence_status,
        "geographic_diversity_medieval": higher_better(metrics["geographic_diversity_medieval_pct"], 40, 30),
        "pioneer_coverage": higher_better(metrics["pioneer_coverage_score_pct"], 85, 70),
        "breakthrough_coverage": higher_better(metrics["breakthrough_coverage_score_pct"], 80, 65),
        "cross_trunk_enabler": higher_better(metrics["cross_trunk_enabler_completeness_pct"], 60, 40),
    }


def overall_macro_decision(statuses: dict[str, str]) -> str:
    """APPROVED / CONDITIONAL APPROVAL / REVISE BEFORE DELIVERY."""
    if not statuses:
        return "INSUFFICIENT DATA"
    if all(s == "TARGET" for s in statuses.values()):
        return "APPROVED FOR DELIVERY"
    if any(s == "FAIL" for s in statuses.values()):
        return "REVISE BEFORE DELIVERY"
    return "CONDITIONAL APPROVAL"


# ─────────────────────────────────────────────────────────────────────────────
# Metric helper predicates
# ─────────────────────────────────────────────────────────────────────────────

def _era_is_ancient_medieval(node: dict) -> bool:
    ds = _to_int(node.get("date_start", ""))
    return ds is not None and ds <= ANCIENT_MEDIEVAL_CUTOFF


def _era_is_medieval(node: dict) -> bool:
    ds = _to_int(node.get("date_start", ""))
    return ds is not None and MEDIEVAL_START <= ds <= MEDIEVAL_END


def _era_is_modern_or_contemporary(node: dict) -> bool:
    ds = _to_int(node.get("date_start", ""))
    return ds is not None and ds >= MODERN_ERA_START


def _era_is_contemporary(node: dict) -> bool:
    ds = _to_int(node.get("date_start", ""))
    return ds is not None and ds >= CONTEMPORARY_START


def _has_presentism_violation(node: dict) -> bool:
    label = node.get("label", "").lower()
    controversies = node.get("controversies", "").strip()
    return any(f in label for f in MODERN_LABELS_FORBIDDEN_PRE_1700) and not controversies


def _has_non_european_region(node: dict) -> bool:
    return any(r in NON_EUROPEAN_REGIONS for r in _split_ids(node.get("region", "")))


def _has_adequate_pioneer_coverage(node: dict) -> bool:
    """3+ pioneer_ids, or a documented exception in controversies."""
    pids = _split_ids(node.get("pioneer_ids", ""))
    if len(pids) >= 3:
        return True
    controversies = node.get("controversies", "").strip().lower()
    return any(kw in controversies for kw in ("attribution gap", "no named", "fewer", "single", "record is thin"))


# ─────────────────────────────────────────────────────────────────────────────
# 5. Combined entry points
# ─────────────────────────────────────────────────────────────────────────────

def validate_all(data_dir: str | Path, verbose: bool = True) -> ValidationReport:
    """
    Run schema compliance + referential integrity + quality rules.
    Returns a ValidationReport; call report.passed() for Gate 1 decision.
    """
    data_dir = Path(data_dir)
    report = ValidationReport()
    check_schema_compliance(data_dir, report)
    check_referential_integrity(data_dir, report)
    check_quality_rules(data_dir, report)
    if verbose:
        report.print_report()
    return report


def print_macro_audit(data_dir: str | Path) -> None:
    """Print the 9 Macro-Audit metrics with TARGET/CRITICAL/FAIL status and overall decision."""
    data_dir = Path(data_dir)
    metrics = compute_macro_metrics(data_dir)

    if "error" in metrics:
        print(metrics["error"])
        return

    statuses = evaluate_macro_metrics(metrics)
    decision = overall_macro_decision(statuses)

    t = metrics["totals"]
    print("\n=== MACRO-AUDIT METRICS (audit_framework.md §6) ===")
    print(f"  Nodes: {t['all_nodes']} total  |  "
          f"{t['ancient_medieval']} ancient/medieval  |  "
          f"{t['modern_contemporary']} modern+contemporary  |  "
          f"{t['contemporary']} contemporary")
    print()

    rows = [
        ("Presentism score",              f"{metrics['presentism_score_pct']}%",              statuses["presentism_score"],             "<10%  / <15%  / ≥15%"),
        ("Founder mythology score",       f"{metrics['founder_mythology_score_pct']}%",       statuses["founder_mythology"],            "<30%  / <40%  / ≥40%"),
        ("Taxonomy bias (E6-only)",       f"{metrics['taxonomy_bias_score_pct']}%",           statuses["taxonomy_bias"],                "0%   / <5%   / ≥5%"),
        ("Source diversity (2+ sources)", f"{metrics['source_diversity_score_pct']}%",        statuses["source_diversity"],             ">90% / >80% / ≤80%"),
        ("Confidence realism (B+C %)",    f"{metrics['confidence_realism_bc_pct']}%",         statuses["confidence_realism"],           "50-70% / 40-80% / A>50% or D>40%"),
        ("Geographic diversity (medieval)",f"{metrics['geographic_diversity_medieval_pct']}%", statuses["geographic_diversity_medieval"],">40% / >30% / ≤30%"),
        ("Pioneer coverage (3+ pids)",    f"{metrics['pioneer_coverage_score_pct']}%",        statuses["pioneer_coverage"],             ">85% / >70% / ≤70%"),
        ("Breakthrough coverage (2+ bids)",f"{metrics['breakthrough_coverage_score_pct']}%",  statuses["breakthrough_coverage"],        ">80% / >65% / ≤65%"),
        ("Cross-trunk enabler completeness",f"{metrics['cross_trunk_enabler_completeness_pct']}%", statuses["cross_trunk_enabler"],    ">60% / >40% / ≤40%"),
    ]

    header = f"  {'STATUS':10s}  {'METRIC':42s}  {'VALUE':8s}  THRESHOLDS (target/critical/fail)"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for name, value, status, thresholds in rows:
        print(f"  {status:10s}  {name:42s}  {value:8s}  {thresholds}")

    print()
    print(f"  OVERALL: {decision}")
    if metrics.get("cross_trunk_note"):
        print(f"\n  Note (metric 9): {metrics['cross_trunk_note']}")


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]
    data_dir_arg = "04_nodes_edges"
    mode = "all"

    for arg in args:
        if arg.startswith("--"):
            mode = arg.lstrip("-")
        else:
            data_dir_arg = arg

    data_dir = Path(data_dir_arg)
    if not data_dir.exists():
        print(f"Error: data directory '{data_dir}' not found.")
        sys.exit(1)

    report = ValidationReport()

    if mode in ("all", "schema"):
        check_schema_compliance(data_dir, report)
    if mode in ("all", "refs"):
        check_referential_integrity(data_dir, report)
    if mode in ("all", "quality"):
        check_quality_rules(data_dir, report)

    if mode not in ("metrics",):
        report.print_report()

    if mode in ("all", "metrics"):
        print_macro_audit(data_dir)

    sys.exit(0 if report.passed() else 1)
