import html, json, sys
W,H=1080,1350
BG="#0a0e16"
C=dict(main="#e8ebf2",olduy="#c9b48a",oghur="#c3a6ff",kip="#56d4dd",kar="#f5c451",oghuz="#ff7b72",arghu="#f19bd2",sib="#79b8ff",ots="#7ee787",dim="#8b94a7",faint="#2a3140")
# ---- rows
ROWS=[ # key, name, ref, group
("danube","Danube Bulgar","oghur/danube-bulgar","oghur"),
("chuvash","Chuvash","oghur/chuvash","oghur"),
("tatar","Tatar","kipchak/tatar","kip"),
("bashkir","Bashkir","kipchak/bashkir","kip"),
("crimean","Crimean Tatar","kipchak/crimean-tatar","kip"),
("kazakh","Kazakh","kipchak/kazakh","kip"),
("kyrgyz","Kyrgyz","kipchak/kyrgyz","kip"),
("uzbek","Uzbek","karluk/uzbek","kar"),
("uyghur","Uyghur","karluk/uyghur","kar"),
("yugur","Western Yugur","old-uyghur/yugur","olduy"),
("turkmen","Turkmen","oghuz/turkmen","oghuz"),
("azeri","Azerbaijani","oghuz/azerbaijani","oghuz"),
("turkish","Turkish","oghuz/turkish","oghuz"),
("gagauz","Gagauz","oghuz/gagauz","oghuz"),
("khalaj","Khalaj","arghu/khalaj","arghu"),
("khakas","Khakas","siberian/khakas","sib"),
("altai","Altai","siberian/altai","sib"),
("tuvan","Tuvan","siberian/tuvan","sib"),
("sakha","Sakha (Yakut)","siberian/sakha","sib"),
]
GROUPS=dict(oghur=("OGHUR","Bulgharic · r-Turkic"),kip=("KIPCHAK","Northwestern"),kar=("KARLUK","Southeastern"),olduy=("OLD UYGHUR","Old Turkic line"),oghuz=("OGHUZ","Southwestern"),arghu=("ARGHU","Khalaj"),sib=("SIBERIAN","Northeastern"))
Y0=254; PITCH=50; GAP=22
RY={}; y=Y0; prev=None; GY={}
for k,n,r,g in ROWS:
    if prev and g!=prev: y+=GAP
    RY[k]=y; GY.setdefault(g,[]).append(y); prev=g; y+=PITCH
YB=y-PITCH
def ry(v):
    if isinstance(v,(int,float)): return v
    if '+' in v:
        a,b=v.split('+'); return (RY[a]+RY[b])/2
    return RY[v]
SX=2.2
BP=[(a,46+(b-46)*SX) for a,b in [(-300,46),(500,170),(1000,410),(1500,625),(1900,750),(2026,835)]]
def X(yr):
    for (a,xa),(b,xb) in zip(BP,BP[1:]):
        if yr<=b: return xa+(yr-a)/(b-a)*(xb-xa)
    return BP[-1][1]
XE=BP[-1][1]; XL=XE+22; W=int(XL+223)
o=[]
def add(s): o.append(s)
def esc(s): return html.escape(s,quote=False)
def line(lane,y1,y2,col,w=3,dash=None,op=1):
    yy=ry(lane); add(f'<path d="M{X(y1):.1f},{yy:.1f} H{X(y2):.1f}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round" opacity="{op}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def curve(l1,yr1,l2,yr2,col,w=3,dash=None,op=1):
    x1,x2=X(yr1),X(yr2); a,b=ry(l1),ry(l2); xm=(x1+x2)/2
    add(f'<path d="M{x1:.1f},{a:.1f} C{xm:.1f},{a:.1f} {xm:.1f},{b:.1f} {x2:.1f},{b:.1f}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round" opacity="{op}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
LAB=[]
def dot(lane,yr,col,label=None,yrlab=None,pos='t',dx=0,dy=0,kind='c',anchor='middle'):
    x,yy=X(yr),ry(lane)
    if kind=='m':
        add(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="6.2" fill="{BG}" stroke="{col}" stroke-width="2.6"/>')
    elif kind=='tag':
        add(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="8.5" fill="none" stroke="{col}" stroke-width="1.3" opacity=".55"/><circle cx="{x:.1f}" cy="{yy:.1f}" r="4.6" fill="{col}" stroke="{BG}" stroke-width="1.5"/>')
    elif kind=='x':
        add(f'<path d="M{x-5:.1f},{yy-5:.1f} l10,10 m0,-10 l-10,10" stroke="{col}" stroke-width="2.6" stroke-linecap="round"/>')
    else:
        add(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="4.4" fill="{col}" stroke="{BG}" stroke-width="1.6"/>')
    if label is not None:
        ty=yy-11+dy if pos=='t' else yy+20+dy
        yl=yrlab if yrlab is not None else (('c. ' if False else '')+str(yr))
        LAB.append(f'<text x="{x+dx:.1f}" y="{ty:.1f}" text-anchor="{anchor}" class="ev"><tspan class="yr" fill="{col}">{esc(yl)}</tspan> {esc(label)}</text>')
def txt(lane,yr,text,col="#9aa3b5",pos='t',dx=0,dy=0,anchor='start',cls='note'):
    x,yy=X(yr),ry(lane); ty=yy-11+dy if pos=='t' else yy+20+dy
    LAB.append(f'<text x="{x+dx:.1f}" y="{ty:.1f}" text-anchor="{anchor}" class="{cls}" fill="{col}">{text}</text>')
exec(open(sys.argv[1]).read())
# ---- labels column
lab=[]
for k,n,r,g in ROWS:
    yy=RY[k]; col=C[g]
    lab.append(f'<path d="M{XE+4},{yy} H{XL-8}" stroke="{col}" stroke-width="1.2" stroke-dasharray="1.5 3.5" opacity=".7"/>')
    lab.append(f'<text x="{XL}" y="{yy-1.5}" class="nm">{esc(n)}</text><text x="{XL}" y="{yy+14.5}" class="ref" fill="{col}">{esc(r)}</text>')
for g,ys in GY.items():
    col=C[g]; a,b=min(ys)-15,max(ys)+18
    lab.append(f'<rect x="{W-33}" y="{a}" width="3" height="{b-a}" rx="1.5" fill="{col}"/>')
    t,s=GROUPS[g]
    if len(ys)>1:
        lab.append(f'<text transform="translate({W-14},{(a+b)/2}) rotate(90)" text-anchor="middle" class="grp" fill="{col}">{t}</text>')
ticks=[]
for yr,l in [(1,'1 CE'),(500,'500'),(1000,'1000'),(1500,'1500'),(1900,'1900'),(1991,'1991')]:
    ticks.append(f'<path d="M{X(yr):.1f},{Y0-34} V{YB+30}" stroke="#1b2230" stroke-width="1"/><text x="{X(yr):.1f}" y="{Y0-42}" text-anchor="middle" class="tick">{l}</text>')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><radialGradient id="g" cx="20%" cy="0%" r="90%"><stop offset="0" stop-color="#131b2b"/><stop offset="1" stop-color="{BG}"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="url(#g)"/>
{HEAD}
{''.join(ticks)}
{''.join(o)}
{''.join(LAB)}
{''.join(lab)}
{FOOT}
</svg>'''
page=f'''<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet"><style>
html,body{{margin:0;background:{BG}}} svg{{display:block}}
text{{font-family:Inter,sans-serif;fill:#e8ebf2}}
.ev{{font-size:12.8px;font-weight:500;fill:#dfe3ec;paint-order:stroke;stroke:{BG};stroke-width:4px;stroke-linejoin:round}}
.yr{{font-family:'JetBrains Mono','DejaVu Sans Mono',monospace;font-weight:700;font-size:12px;stroke:{BG}}}
.nm{{font-size:18px;font-weight:650}}
.ref{{font-family:'JetBrains Mono','DejaVu Sans Mono',monospace;font-size:11.2px;opacity:.95}}
.grp{{font-family:'JetBrains Mono','DejaVu Sans Mono',monospace;font-size:10.5px;font-weight:700;letter-spacing:2.2px}}
.tick{{font-family:'JetBrains Mono','DejaVu Sans Mono',monospace;font-size:11px;fill:#6f7a8f}}
.mono{{font-family:'JetBrains Mono','DejaVu Sans Mono',monospace}}
.note{{font-size:11.6px;font-style:italic;paint-order:stroke;stroke:{BG};stroke-width:4px}}
</style></head><body>{svg}</body></html>'''
open(sys.argv[2],'w').write(page)
