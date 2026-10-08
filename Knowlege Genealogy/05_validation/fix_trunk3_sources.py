"""
Add second source to the 11 nodes that currently have only 1 source_id.
This clears source_completeness warnings and improves source diversity metric.
"""
import csv, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

# Maps node_id → second source to add
EXTRA_SOURCE = {
    'T3_MOD_002': 'SRC_085',  # Chemical Atomism in the 19C
    'T3_MOD_003': 'SRC_085',  # Chemical Atomism in the 19C
    'T3_MOD_004': 'SRC_076',  # Ideas in Chemistry: History of the Science
    'T3_MOD_005': 'SRC_082',  # Maxwell on Heat and Statistical Mechanics
    'T3_MOD_007': 'SRC_083',  # The Maxwellians
    'T3_MOD_010': 'SRC_078',  # Quantum: Einstein, Bohr, and the Great Debate
    'T3_CON_003': 'SRC_102',  # Intermetallic Compounds: Principles and Practice
    'T3_CON_005': 'SRC_079',  # Quantum Generations: Physics in the 20C
    'T3_CON_008': 'SRC_093',  # When Condensed-matter Physics Became King
    'T3_CON_009': 'SRC_097',  # Electronic Structure of Matter (Kohn Nobel)
    'T3_CON_012': 'SRC_079',  # Quantum Generations
}

def rewrite_csv(fname, transform_fn):
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

def fix_nodes(row):
    nid = row['node_id']
    if nid in EXTRA_SOURCE:
        current = row.get('source_ids', '').strip()
        new_src = EXTRA_SOURCE[nid]
        if new_src not in current:
            row['source_ids'] = f"{current}, {new_src}" if current else new_src
    return row

print("Adding second sources to single-source nodes...")
rewrite_csv('nodes.csv', fix_nodes)
print("Done.")
