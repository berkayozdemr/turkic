"""Build site/index.html: python3 build_site.py  (run from site-src/)"""
import json, hashlib, subprocess, os, sys, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import P, GROUP_INFO, FLAGS, flag_urls

svg_path = os.path.join(HERE, 'graph.svg')
subprocess.run([sys.executable, os.path.join(HERE, 'graph_gen.py'), os.path.join(HERE, 'hero'), svg_path], check=True)
svg = open(svg_path).read()

# Files whose original is no wider than the 960px thumbnail bucket: link the original.
ORIGINAL = {'Mosque "Kul Sharif".jpg', 'Old Chuvash men.jpg', 'Chuvash woman in traditional attire.jpg', 'Gagauz-children.jpg',
            'Azerigirls.JPG', 'Ashiqs in Tabriz.jpg', 'Altaian horseman.jpg', 'Yakut Sakha hunter.jpg'}
ORIGINAL |= {k for k in [x['file'] for v in P.values() if v for x in v['images']] if k.startswith('Khalaj coin')}
LIC = {'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0/', 'CC BY-SA 3.0': 'https://creativecommons.org/licenses/by-sa/3.0/',
       'CC BY-SA 2.0': 'https://creativecommons.org/licenses/by-sa/2.0/', 'CC BY 4.0': 'https://creativecommons.org/licenses/by/4.0/',
       'CC BY 3.0': 'https://creativecommons.org/licenses/by/3.0/', 'CC BY 2.0': 'https://creativecommons.org/licenses/by/2.0/',
       'CC0': 'https://creativecommons.org/publicdomain/zero/1.0/', 'GFDL': 'https://www.gnu.org/licenses/fdl-1.3.html', 'Public domain': ''}

def urls(f):
    n = f.replace(' ', '_'); h = hashlib.md5(n.encode()).hexdigest(); q = urllib.parse.quote(n)
    base = f'https://upload.wikimedia.org/wikipedia/commons'
    src = f'{base}/{h[0]}/{h[:2]}/{q}' if f in ORIGINAL else f'{base}/thumb/{h[0]}/{h[:2]}/{q}/960px-{q}'
    return src, f'https://commons.wikimedia.org/wiki/File:{q}'

data = {}
for k, v in P.items():
    if not v: continue
    d = dict(v)
    d['groupName'], d['groupDesc'] = GROUP_INFO[v['group']]
    d['wiki'] = [(t, 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(s)) for t, s in v['wiki']]
    d['images'] = []
    for im in v['images']:
        src, page = urls(im['file'])
        d['images'].append(dict(src=src, page=page, lic=im['lic'], licUrl=LIC[im['lic']], author=im['author'], caption=im['caption']))
    if k in FLAGS:
        fs, fp = flag_urls(FLAGS[k][0])
        d['flag'] = dict(src=fs, page=fp, label=FLAGS[k][1])
    data[k] = d

tpl = open(os.path.join(HERE, 'template.html')).read()
out = tpl.replace('<!--GRAPH-->', svg).replace('/*DATA*/', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
open(os.path.join(HERE, '..', 'index.html'), 'w').write(out)
print('index.html', len(out), 'bytes,', len(data), 'entries,', sum(len(d['images']) for d in data.values()), 'images')
