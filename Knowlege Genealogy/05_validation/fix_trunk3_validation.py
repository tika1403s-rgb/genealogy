"""
Fix all validation errors introduced by trunk3 additions:
 1. breakthroughs.csv:
    a) enabling_factors: replace free text with actual BRKTH IDs (or empty)
    b) type: fix 'experimental_demonstration' → 'discovery' for BRKTH_086/094/106/115/116
 2. pioneers.csv:
    confidence A → B for all PION_144-253 that have <2 source_ids
 3. pioneer_contributions.csv:
    a) contribution_type 'discovery' → 'experimental_demonstration' for CONTR_225-227
    b) Fix vague language in CONTR_226 specific_contribution
"""
import csv, os, io

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

def rewrite_csv(fname, transform_fn):
    """Read, transform each row, write back."""
    path = os.path.join(BASE, fname)
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    changed = 0
    new_rows = []
    for row in rows:
        orig = dict(row)
        row = transform_fn(row)
        if row != orig:
            changed += 1
        new_rows.append(row)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(new_rows)
    print(f"  {fname}: {changed} rows modified")

# ── 1. Fix breakthroughs.csv ──────────────────────────────────────────────────

# Map of correct enabling_factors (BRKTH IDs only) for our new breakthroughs
ENABLING_FACTORS_FIX = {
    'BRKTH_065': '',
    'BRKTH_066': 'BRKTH_065',
    'BRKTH_067': '',
    'BRKTH_068': '',
    'BRKTH_069': 'BRKTH_065, BRKTH_066',
    'BRKTH_070': '',
    'BRKTH_071': 'BRKTH_067',
    'BRKTH_072': 'BRKTH_081, BRKTH_082',
    'BRKTH_073': 'BRKTH_070, BRKTH_072',
    'BRKTH_074': 'BRKTH_071',
    'BRKTH_075': 'BRKTH_070',
    'BRKTH_076': 'BRKTH_073, BRKTH_075',
    'BRKTH_077': 'BRKTH_076',
    'BRKTH_078': 'BRKTH_076',
    'BRKTH_079': 'BRKTH_071, BRKTH_076',
    'BRKTH_080': '',
    'BRKTH_081': '',
    'BRKTH_082': '',
    'BRKTH_083': '',
    'BRKTH_084': '',
    'BRKTH_085': '',
    'BRKTH_086': 'BRKTH_081, BRKTH_082',
    'BRKTH_087': 'BRKTH_081',
    'BRKTH_088': 'BRKTH_083',
    'BRKTH_089': '',
    'BRKTH_090': '',
    'BRKTH_091': 'BRKTH_064',
    'BRKTH_092': '',
    'BRKTH_093': '',
    'BRKTH_094': 'BRKTH_086, BRKTH_089',
    'BRKTH_095': 'BRKTH_076, BRKTH_079',
    'BRKTH_096': '',
    'BRKTH_097': 'BRKTH_076',
    'BRKTH_098': '',
    'BRKTH_099': 'BRKTH_076',
    'BRKTH_100': 'BRKTH_079, BRKTH_095',
    'BRKTH_101': 'BRKTH_095',
    'BRKTH_102': 'BRKTH_097',
    'BRKTH_103': 'BRKTH_076',
    'BRKTH_104': 'BRKTH_103',
    'BRKTH_105': '',
    'BRKTH_106': '',
    'BRKTH_107': 'BRKTH_070, BRKTH_076',
    'BRKTH_108': 'BRKTH_076',
    'BRKTH_109': '',
    'BRKTH_110': '',
    'BRKTH_111': 'BRKTH_096',
    'BRKTH_112': '',
    'BRKTH_113': 'BRKTH_088',
    'BRKTH_114': '',
    'BRKTH_115': 'BRKTH_107',
    'BRKTH_116': 'BRKTH_097, BRKTH_105',
}

# Types to fix: experimental_demonstration → discovery
TYPE_FIX = {
    'BRKTH_086': 'discovery',
    'BRKTH_094': 'discovery',
    'BRKTH_106': 'discovery',
    'BRKTH_115': 'discovery',
    'BRKTH_116': 'discovery',
}

def fix_breakthroughs(row):
    bid = row['breakthrough_id']
    if bid in ENABLING_FACTORS_FIX:
        row['enabling_factors'] = ENABLING_FACTORS_FIX[bid]
    if bid in TYPE_FIX:
        row['type'] = TYPE_FIX[bid]
    return row

# ── 2. Fix pioneers.csv ───────────────────────────────────────────────────────

def fix_pioneers(row):
    pid = row['pioneer_id']
    if pid < 'PION_144':
        return row
    sources = [s.strip() for s in row.get('source_ids', '').split(',') if s.strip()]
    if row.get('confidence') == 'A' and len(sources) < 2:
        row['confidence'] = 'B'
    return row

# ── 3. Fix pioneer_contributions.csv ─────────────────────────────────────────

CONTR_TYPE_FIX = {
    'CONTR_225': 'experimental_demonstration',
    'CONTR_226': 'experimental_demonstration',
    'CONTR_227': 'experimental_demonstration',
}

CONTR_TEXT_FIX = {
    'CONTR_226': ('Co-discovered C60 buckminsterfullerene (1985) with Smalley and Kroto using laser vaporisation of graphite; '
                  'Nobel Chemistry 1996; carbon cluster research using supersonic molecular beam techniques; '
                  'contributed to understanding of carbon nanostructure formation mechanisms'),
}

def fix_contributions(row):
    cid = row['contribution_id']
    if cid in CONTR_TYPE_FIX:
        row['contribution_type'] = CONTR_TYPE_FIX[cid]
    if cid in CONTR_TEXT_FIX:
        row['specific_contribution'] = CONTR_TEXT_FIX[cid]
    return row

# ── Run all fixes ─────────────────────────────────────────────────────────────

print("Running validation fixes...")
rewrite_csv('breakthroughs.csv', fix_breakthroughs)
rewrite_csv('pioneers.csv', fix_pioneers)
rewrite_csv('pioneer_contributions.csv', fix_contributions)
print("All fixes applied.")
