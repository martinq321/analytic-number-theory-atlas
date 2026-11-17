from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]
x=json.loads((p/'data/source-atlas.json').read_text())
(p/'data/atlas.js').write_text('window.ATLAS_DATA = '+json.dumps(x,ensure_ascii=False)+';',encoding='utf-8')
