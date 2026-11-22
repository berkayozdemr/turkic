"""Build site/index.html: python3 build_site.py  (run from site-src/)"""
import json, hashlib, subprocess, os, sys, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import P, GROUP_INFO, FLAGS, flag_urls

svg_path = os.path.join(HERE, 'graph.svg')
subprocess.run([sys.executable, os.path.join(HERE, 'graph_gen.py'), os.path.join(HERE, 'hero'), svg_path], check=True)
svg = open(svg_path).read()

from build_urls import image_urls as urls, LIC

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
