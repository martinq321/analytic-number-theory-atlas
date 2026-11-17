from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]
x=json.loads((p/'data/source-atlas.json').read_text())
ids=[n['id'] for n in x['nodes']]
assert len(ids)==len(set(ids))
for e in x['edges']:
 assert e['output'] in ids, e['id']
 assert all(i in ids for i in e['inputs']),e['id']
for f in ['index.html','style.css','app.js','config.js','data/atlas.js']:
 assert (p/f).is_file(),f
print(f'Passed: {len(ids)} unique records, {len(x["edges"])} rules with valid endpoints, required assets present.')
