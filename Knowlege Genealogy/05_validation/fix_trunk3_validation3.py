"""Fix last founder_mythology error in T3_MOD_008 description."""
import csv, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '04_nodes_edges')

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
    if row['node_id'] == 'T3_MOD_008':
        row['description'] = (
            'Study of atom internal structure, radioactivity, and nuclear reactions. '
            'Established through X-ray and radioactivity discoveries (1895-1898), electron identification (1897), '
            'nuclear atom model (1911), culminating in nuclear fission (1938-1942). '
            'Spans atomic spectroscopy, nuclear structure, and particle physics precursors.'
        )
    return row

rewrite_csv('nodes.csv', fix_nodes)
print("Done.")
