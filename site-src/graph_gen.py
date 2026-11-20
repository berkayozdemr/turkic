"""Build the interactive graph SVG for the website.

Reuses the hero image's layout code (hero-image-src/gen.py) and data (hero-image-src/data.py)
unchanged, and tags every drawn element with data-l="<lane>" so the page can highlight a branch.
Usage: python3 graph_gen.py ../hero-image-src out.svg
"""
import sys, os, re, html

SRC = sys.argv[1]
gen = open(os.path.join(SRC, 'gen.py')).read()
top = gen.split("exec(open(sys.argv[1]).read())")[0]
ns = {}
exec(top, ns)
C, o, LAB = ns['C'], ns['o'], ns['LAB']
M, U = C['main'], C['olduy']

# lanes that share a row with another lane's early history
def tag_for(lane, yr, col):
    if lane == 'yugur':
        return 'main' if (col != U and yr <= 840) else 'yugur'
    if lane == 'uzbek+uyghur':
        return 'karluk'
    return lane

def wrap(fn, lane_idx, yr_idx, col_idx, lane_override=None):
    def w(*a, **k):
        n_o, n_l = len(o), len(LAB)
        fn(*a, **k)
        lane = a[lane_idx] if lane_override is None else a[lane_override]
        yr = a[yr_idx] if lane_override is None else a[lane_override + 1]
        col = a[col_idx] if len(a) > col_idx else k.get('col', '#9aa3b5')
        t = tag_for(lane, yr, col)
        if lane_override is None and fn.__name__ == 'curve':
            pass
        for L in (o, LAB):
            start = n_o if L is o else n_l
            for i in range(start, len(L)):
                L[i] = f'<g data-l="{t}">{L[i]}</g>'
    return w

orig_curve = ns['curve']
def curve(l1, yr1, l2, yr2, col, *a, **k):
    n = len(o)
    orig_curve(l1, yr1, l2, yr2, col, *a, **k)
    t = tag_for(l2, yr2, col)
    if l1 == 'yugur' and l2 == 'uyghur':
        t = 'uyghur'
    for i in range(n, len(o)):
        o[i] = f'<g data-l="{t}">{o[i]}</g>'
ns['curve'] = curve
ns['line'] = wrap(ns['line'], 0, 1, 3)
ns['dot'] = wrap(ns['dot'], 0, 1, 2)
ns['txt'] = wrap(ns['txt'], 0, 1, 3)

exec(open(os.path.join(SRC, 'data.py')).read(), ns)

S, T = C['sib'], C['ots']
for i, s in enumerate(o):
    if 'data-l=' in s:
        continue
    if f'stroke="{S}"' in s and 'stroke-dasharray' in s:
        o[i] = s.replace('<path', '<path data-l="kyrgyz"', 1)
    elif (f'stroke="{T}"' in s or f'fill:{T}' in s) and 'translate' not in s:
        o[i] = re.sub(r'^<(\w+)', r'<\1 data-l="ots"', s, count=1)
    elif 'HOW TO READ' in s or 'translate(' in s:
        o[i] = f'<g class="legend">{s}</g>'

RY, X, ROWS, W, XE, XL = ns['RY'], ns['X'], ns['ROWS'], ns['W'], ns['XE'], ns['XL']
Y0, YB, GY, GROUPS, esc = ns['Y0'], ns['YB'], ns['GY'], ns['GROUPS'], ns['esc']

# where each lane's own line starts (for the invisible click band)
START = dict(danube=681, chuvash=330, tatar=1430, bashkir=1430, crimean=930, kazakh=1430, kyrgyz=1430,
             uzbek=1500, uyghur=1500, yugur=840, turkmen=1000, azeri=790, turkish=1120, gagauz=1330,
             khalaj=690, khakas=810, altai=640, tuvan=810, sakha=590)
hits = []
for k, n, r, g in ROWS:
    x0 = X(START[k]) - 10; yy = RY[k]
    hits.append(f'<rect class="hit" data-l="{k}" x="{x0:.1f}" y="{yy-17}" width="{W-40-x0:.1f}" height="34"/>')
hits.append(f'<rect class="hit" data-l="main" x="{X(-300)-14:.1f}" y="{RY["yugur"]-17}" width="{X(840)-X(-300)+20:.1f}" height="34"/>')

lab = []
for k, n, r, g in ROWS:
    yy = RY[k]; col = C[g]
    lab.append(f'<g class="row" data-l="{k}" tabindex="0" role="button" aria-label="{esc(n)}: show details">'
               f'<rect class="rowbg" x="{XL-12}" y="{yy-24}" width="{W-40-XL+6}" height="46" rx="8"/>'
               f'<path d="M{XE+4},{yy} H{XL-8}" stroke="{col}" stroke-width="1.2" stroke-dasharray="1.5 3.5" opacity=".7"/>'
               f'<text x="{XL}" y="{yy-1.5}" class="nm">{esc(n)}</text><text x="{XL}" y="{yy+14.5}" class="ref" fill="{col}">{esc(r)}</text></g>')
for g, ys in GY.items():
    col = C[g]; a, b = min(ys) - 15, max(ys) + 18
    lab.append(f'<rect x="{W-33}" y="{a}" width="3" height="{b-a}" rx="1.5" fill="{col}"/>')
    t, s = GROUPS[g]
    if len(ys) > 1:
        lab.append(f'<text transform="translate({W-14},{(a+b)/2}) rotate(90)" text-anchor="middle" class="grp" fill="{col}">{t}</text>')
ticks = []
for yr, l in [(1, '1 CE'), (500, '500'), (1000, '1000'), (1500, '1500'), (1900, '1900'), (1991, '1991')]:
    ticks.append(f'<path d="M{X(yr):.1f},{Y0-34} V{YB+30}" stroke="var(--grid)" stroke-width="1"/><text x="{X(yr):.1f}" y="{Y0-42}" text-anchor="middle" class="tick">{l}</text>')

vy = Y0 - 62; vh = YB + 40 - vy
svg = (f'<svg id="graph" xmlns="http://www.w3.org/2000/svg" viewBox="0 {vy} {W} {vh}" role="img" '
       f'aria-label="Git-style branch graph of the Turkic peoples from Proto-Turkic to today">'
       + ''.join(ticks) + '<g class="hits">' + ''.join(hits) + '</g>'
       + '<g class="draw">' + ''.join(o) + ''.join(LAB) + '</g>' + ''.join(lab) + '</svg>')
open(sys.argv[2], 'w').write(svg)
print('ok', len(svg), 'bytes; untagged:', sum(1 for s in o + LAB if 'data-l' not in s and 'legend' not in s))
