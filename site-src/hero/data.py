M=C['main']; T=C['ots']
HEAD=f'''
<text x="46" y="92" style="font-size:50px;font-weight:800;letter-spacing:-1.6px">The Turkic family, as a <tspan fill="{T}">git graph</tspan></text>
<text x="47" y="130" class="mono" style="font-size:16px;fill:#8b94a7"><tspan fill="{T}">$</tspan> git log --graph --all <tspan fill="#5d6779"># c. 2,000 years · 6 branches + the Old Uyghur line</tspan></text>
<text x="47" y="166" style="font-size:15.5px;fill:#b6bdcb">One proto-language on the eastern steppe: forked, archived and merged across Eurasia.</text>
'''
O=C['oghur'];K=C['kip'];A=C['kar'];U=C['olduy'];Z=C['oghuz'];G=C['arghu'];S=C['sib']
# ---------- main trunk
line('yugur',-300,840,M,3.8)
line('yugur',840,2026,U,2.6)
# ---------- oghur (trunk on chuvash row)
curve('yugur',-60,'chuvash',330,O); line('chuvash',330,2026,O)
curve('chuvash',640,'danube',700,O); line('danube',700,900,O)
# ---------- siberian
curve('yugur',450,'sakha',590,S); line('sakha',590,2026,S)
curve('yugur',520,'altai',640,S); line('altai',640,2026,S)
curve('altai',740,'khakas',810,S); line('khakas',810,2026,S)
curve('altai',740,'tuvan',810,S); line('tuvan',810,2026,S)
# ---------- arghu
curve('yugur',590,'khalaj',690,G); line('khalaj',690,2026,G,2.6)
# ---------- oghuz (trunk on azerbaijani row)
curve('yugur',740,'azeri',790,Z); line('azeri',790,2026,Z)
curve('azeri',950,'turkmen',1000,Z); line('turkmen',1000,2026,Z)
curve('azeri',1071,'turkish',1120,Z); line('turkish',1120,2026,Z)
curve('turkish',1250,'gagauz',1330,Z,2.4,dash="6 5"); line('gagauz',1330,1812,Z,2.4,dash="6 5"); line('gagauz',1812,2026,Z)
# ---------- karluk
curve('yugur',700,'uzbek+uyghur',766,A); line('uzbek+uyghur',766,1450,A)
curve('uzbek+uyghur',1450,'uzbek',1500,A); line('uzbek',1500,2026,A)
curve('uzbek+uyghur',1450,'uyghur',1500,A); line('uyghur',1500,2026,A)
# ---------- kipchak (trunk on crimean row)
curve('yugur',850,'crimean',930,K); line('crimean',930,2026,K)
for k in ['tatar','bashkir','kazakh','kyrgyz']:
    curve('crimean',1370,k,1430,K); line(k,1430,2026,K)
# ---------- merges (dashed)
curve('chuvash',1290,'tatar',1438,O,2,dash="5 5")
curve('kazakh',1440,'uzbek',1503,K,2,dash="5 5")
curve('yugur',1440,'uyghur',1500,U,2,dash="5 5")
x0,y0=X(1570),RY['kyrgyz']
add(f'<path d="M{x0-20},{y0+22} C{x0-8},{y0+22} {x0-8},{y0} {x0},{y0}" stroke="{S}" stroke-width="2" fill="none" stroke-dasharray="5 5"/>')
# ---------- dots & labels
dot('yugur',-300,M,kind='tag')
txt('yugur',-300,'main',M,pos='b',dx=-3,dy=4,cls='ev yr')
txt('yugur',-300,'Proto-Turkic',pos='b',dx=-3,dy=21)
txt('yugur',-300,'eastern Inner Asia',pos='b',dx=-3,dy=36)
dot('yugur',-60,M)
txt('yugur',-60,f'<tspan class="yr" fill="{O}">c. 1st c. BCE</tspan>',cls='ev',dx=92,dy=-128)
txt('yugur',-60,'Oghur splits off:',cls='ev',dx=92,dy=-112)
txt('yugur',-60,'the oldest fork',cls='ev',dx=92,dy=-96)
dot('yugur',552,M,kind='tag'); dot('yugur',732,M)
txt('yugur',700,f'<tspan class="yr" fill="{M}">552</tspan> Göktürk Khaganate',cls='ev',anchor='end',dx=-6,dy=-16)
txt('yugur',700,f'<tspan class="yr" fill="{M}">732</tspan> Orkhon inscriptions',cls='ev',anchor='end',dx=-6,dy=0)
dot('yugur',840,M,'Uyghur Khaganate falls',kind='tag',pos='b',dx=-8,anchor='start')
dot('yugur',1000,U,'Qocho & Gansu Uyghurs',yrlab='c. 850',dx=-18,anchor='start')
# oghur
dot('chuvash',463,O,'Oghurs on the Pontic steppe',pos='b',dx=-8,anchor='start')
dot('chuvash',632,O,'Old Great Bulgaria',dx=-4,anchor='end',yrlab='c. 632')
dot('danube',681,O,'Danube Bulgar state',dx=14,anchor='start',dy=-1)
dot('danube',900,O,kind='x')
txt('danube',900,f'<tspan class="yr" fill="{O}">c. 900</tspan> Slavic-speaking: branch archived',cls='ev',dx=13,dy=15)
dot('chuvash',922,O,'Volga Bulgaria adopts Islam',dx=-10)
dot('chuvash',1236,O,'Mongol conquest',dx=-8,anchor='start')
# kipchak
dot('crimean',1050,K,'Cuman-Kipchak steppe',yrlab='c. 1050',dx=-46,anchor='start')
dot('crimean',1242,K,'Golden Horde',yrlab='1240s',dx=48,anchor='end',pos='b',dy=-2)
dot('tatar',1438,K,'Khanate of Kazan',kind='m',dx=10,anchor='start')
txt('tatar',1438,'+ Volga Bulgar heritage (weight debated)',O,dx=-34,dy=-12,anchor='end')
dot('bashkir',1557,K,'Muscovite rule',dx=10,anchor='start',yrlab='1550s')
dot('crimean',1441,K,'Khanate',dx=9,anchor='start')
dot('crimean',1944,K,'deportation',dx=47,anchor='end')
dot('kazakh',1465,K,'Kazakh Khanate',dx=9,anchor='start',yrlab='c. 1465')
dot('kyrgyz',1570,K,'Tian Shan Kyrgyz',kind='m',dx=10,yrlab='c. 1500',anchor='start')
txt('kyrgyz',1570,'+ Yenisei Kyrgyz (debated)',S,pos='b',dx=10,dy=-1)
# karluk
dot('uzbek+uyghur',960,A,'Karakhanids',yrlab='c. 960',dx=-14,anchor='start')
dot('uzbek+uyghur',1074,A,"al-Kashgari's Dīwān",yrlab='1072-74',pos='b',dx=-40,anchor='start',dy=-2)
txt('uzbek+uyghur',1535,'both continue Chagatai',A,dx=0,dy=15)
dot('uzbek',1503,A,'Shaybanid Uzbeks',kind='m',dx=10,anchor='start',yrlab='1500-07')
txt('uzbek',1503,'+ Kipchak-speaking Uzbek ulus',K,dx=-24,dy=-6,anchor='end')
dot('uyghur',1500,A,kind='m')
dot('uyghur',1921,A,"name revived",dx=5,anchor='end',pos='b',dy=-2)
# oghuz
dot('azeri',790,Z,'Oghuz Yabgu',yrlab='c. 770',pos='b',dx=6,anchor='start',dy=-2)
dot('turkmen',1000,Z,"'Türkmen' first attested",yrlab='c. 987',dx=9,anchor='start')
dot('azeri',1040,Z,'Seljuks',dx=-2,anchor='start')
dot('azeri',1071,Z,kind='tag')
txt('azeri',1120,f'<tspan class="yr" fill="{Z}">1071</tspan> Manzikert',cls='ev',pos='b',dx=6,dy=-3)
dot('azeri',1501,Z,'Safavids')
dot('azeri',1918,Z,'republic',dx=5,anchor='end')
dot('turkish',1299,Z,'Ottomans',yrlab='c. 1299',dx=8,anchor='start')
dot('turkish',1923,Z,'Republic',kind='tag',dx=4,anchor='end')
dot('gagauz',1812,Z,'Gagauz settle in Bessarabia',dx=6,anchor='end',yrlab='from 1812',pos='b',dy=-2)
txt('gagauz',1330,'earlier origins debated',Z,dx=8)
# arghu
dot('khalaj',1074,G,"'Arghu' in al-Kashgari",yrlab='1070s',dx=-8,anchor='start')
dot('khalaj',1968,G,'Doerfer: its own branch',dx=5,anchor='end',yrlab='1970s')
# siberian
dot('khakas',840,S,'Yenisei Kyrgyz take Ordu-Baliq',dx=-6,anchor='start')
dot('khakas',1703,S,'Dzungar resettlement',dx=0,yrlab='c. 1703')
dot('tuvan',1921,S,"Tuvan People's Republic",dx=5,anchor='end')
dot('sakha',1400,S,'migration north to the Lena',yrlab='13th-15th c.',dx=8,anchor='end')
dot('sakha',1632,S,'Yakutsk',dx=9,anchor='start')
txt('turkmen',1991,f'<tspan class="yr" fill="{Z}">1991</tspan> independence',cls='ev',anchor='end',dx=-10)
# 1991
for k,col in [('kazakh',K),('kyrgyz',K),('uzbek',A),('turkmen',Z),('azeri',Z)]:
    dot(k,1991,col,kind='tag')
# OTS rail
xo=X(2012)
add(f'<path d="M{xo},{RY["kazakh"]} V{RY["turkish"]}" stroke="{T}" stroke-width="2.6" stroke-linecap="round"/>')
for k in ['kazakh','kyrgyz','uzbek','azeri','turkish']:
    add(f'<circle cx="{xo}" cy="{RY[k]}" r="5.2" fill="{BG}" stroke="{T}" stroke-width="2.6"/>')
add(f'<text x="{xo+7}" y="{RY["kazakh"]-13}" text-anchor="end" class="ev yr" style="fill:{T}">2009</text>')
# legend (top-left empty area)
lx,ly=166,RY['tatar']+6
def leg(i,sym,t):
    yy=ly+i*21
    return f'<g transform="translate({lx},{yy})">{sym}<text x="26" y="4" style="font-size:11.8px;fill:#aab2c2">{t}</text></g>'
D="#aab2c2"
legend=''.join([
 f'<text x="{lx}" y="{ly-22}" class="mono" style="font-size:10.5px;font-weight:700;letter-spacing:2px;fill:#6f7a8f">HOW TO READ</text>',
 leg(0,f'<circle cx="8" cy="0" r="4.2" fill="{D}"/>','commit: an event'),
 leg(1,f'<circle cx="8" cy="0" r="7.5" fill="none" stroke="{D}" stroke-width="1.2" opacity=".6"/><circle cx="8" cy="0" r="4" fill="{D}"/>','tag: a milestone'),
 leg(2,f'<circle cx="8" cy="0" r="5.4" fill="{BG}" stroke="{D}" stroke-width="2.4"/>','merge: two lines join'),
 leg(3,f'<path d="M-2,0 H18" stroke="{D}" stroke-width="2" stroke-dasharray="5 4"/>','contact or debated link'),
 leg(4,f'<path d="M3,-5 l10,10 m0,-10 l-10,10" stroke="{D}" stroke-width="2.4" stroke-linecap="round"/>','archived branch'),
 leg(5,f'<path d="M8,-8 V8" stroke="{T}" stroke-width="2.6"/><circle cx="8" cy="0" r="4.4" fill="{BG}" stroke="{T}" stroke-width="2.2"/>','octopus merge: Turkic States'),
])
add(legend)
fy=YB+60
FOOT=f'''
<path d="M46,{fy-28} H{W-33}" stroke="#1b2230"/>
<text x="46" y="{fy}" class="mono" style="font-size:13px;fill:{T};font-weight:700">turkic-states</text>
<text x="166" y="{fy}" style="font-size:13px;fill:#c9cfdb">2009 octopus merge: Türkiye, Azerbaijan, Kazakhstan, Kyrgyzstan (+ Uzbekistan 2019) form the Turkic Council,</text>
<text x="166" y="{fy+18}" style="font-size:13px;fill:#c9cfdb">since 2021 the Organization of Turkic States. Cooperation between sovereign states, not one state.</text>
<text x="46" y="{fy+50}" style="font-size:11.8px;fill:#8b94a7">A teaching metaphor. Branches follow the linguistic classification of the languages (after Johanson 1998), not ancestry or politics. Fork points are</text>
<text x="46" y="{fy+66}" style="font-size:11.8px;fill:#8b94a7">approximate (mostly first attestations); “Siberian” is a regional grouping, not a proven single branch. Peoples mixed far more than a graph shows.</text>
'''
