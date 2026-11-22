"""Write a README.md for every history branch, from the same content the website uses.

Usage: python3 branch_readmes.py OUT_DIR [REMOTE]
Writes OUT_DIR/<branch with / replaced by -->.md for each branch. Each README is then committed
on top of its own branch (see the README in this folder). REMOTE defaults to "origin".
"""
import os, subprocess, sys, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import P, GROUP_INFO, FLAGS

OUT = sys.argv[1]
REMOTE = sys.argv[2] if len(sys.argv) > 2 else 'origin'
SITE = 'https://berkayozdemr.github.io/turkic/'
REPO = 'https://github.com/berkayozdemr/turkic'
WIKI = 'https://en.wikipedia.org/wiki/'

# branch -> key in content.P
PEOPLE = {
    'oghur/chuvash': 'chuvash', 'oghur/danube-bulgar': 'danube',
    'kipchak/tatar': 'tatar', 'kipchak/bashkir': 'bashkir', 'kipchak/crimean-tatar': 'crimean',
    'kipchak/kazakh': 'kazakh', 'kipchak/kyrgyz': 'kyrgyz',
    'karluk/uzbek': 'uzbek', 'karluk/uyghur': 'uyghur', 'old-uyghur': 'yugur',
    'oghuz/turkmen': 'turkmen', 'oghuz/azerbaijani': 'azeri', 'oghuz/turkish': 'turkish', 'oghuz/gagauz': 'gagauz',
    'siberian/khakas': 'khakas', 'siberian/altai': 'altai', 'siberian/tuvan': 'tuvan', 'siberian/sakha': 'sakha',
    'turkic-states': 'ots',
}
TITLE = {'old-uyghur': 'Old Uyghur line and the Western Yugurs'}
WHERE_LABEL = {'danube': 'Where they lived', 'ots': 'Members'}

# Branches that are not one living people: group trunks and historical lines.
# branch -> (title, group, where label, where, brief, [(wiki title, slug)], [child branches])
EXTRA = {
    'oghur/trunk': ('Oghur (Bulgharic) branch', 'oghur', 'Where it was spoken',
        'From the eastern steppe to the Pontic steppe, the Danube and the middle Volga; today only Chuvashia',
        'The first branch to split from the rest of the Turkic family, around the 1st century BCE. Oghur languages have '
        '"r" and "l" where all other Turkic languages have "z" and "sh", which is why the branch is also called "r-Turkic". '
        'Oghur-speaking tribes reached the Pontic steppe by the 5th century and founded Old Great Bulgaria around 632. '
        'Chuvash is the only Oghur language still spoken.',
        [('Oghuric languages', 'Oghuric_languages'), ('Old Great Bulgaria', 'Old_Great_Bulgaria')],
        ['oghur/volga-bulgar', 'oghur/danube-bulgar', 'oghur/chuvash']),
    'oghur/volga-bulgar': ('Volga Bulgars', 'oghur', 'Where they lived',
        "The middle Volga and Kama rivers, in today's Tatarstan and Chuvashia, Russia",
        'Bulgar groups who moved north to the middle Volga after Old Great Bulgaria broke up in the 7th century. '
        'Their state, Volga Bulgaria, adopted Islam in 922, the year of Ibn Fadlan\'s embassy, and was a trading power '
        'between the forest zone and the steppe until the Mongol conquest of 1236. Volga Bulgar was an Oghur language; '
        'Chuvash is its closest living relative, and Volga Bulgar heritage is also part of the history of the Kazan Tatars.',
        [('Volga Bulgaria', 'Volga_Bulgaria'), ('Bulgar language', 'Bulgar_language')],
        ['oghur/chuvash', 'kipchak/tatar']),
    'oghuz/trunk': ('Oghuz branch', 'oghuz', 'Where it is spoken',
        'From Turkmenistan and north-eastern Iran across Azerbaijan and Türkiye to the Balkans and Moldova',
        'Southwestern Turkic. The Oghuz confederation formed in the 8th century and built the Oghuz Yabgu state between '
        'the Caspian and Aral seas. From the 11th century the Seljuks carried Oghuz speakers west into Iran, the Caucasus '
        'and Anatolia. Turkish, Azerbaijani, Turkmen and Gagauz are the main Oghuz languages today.',
        [('Oghuz Turks', 'Oghuz_Turks'), ('Oghuz languages', 'Oghuz_languages'), ('Oghuz Yabgu State', 'Oghuz_Yabgu_State')],
        ['oghuz/seljuk', 'oghuz/turkmen', 'oghuz/azerbaijani', 'oghuz/turkish', 'oghuz/gagauz']),
    'oghuz/seljuk': ('Seljuks', 'oghuz', 'Where they ruled',
        'From Central Asia across Iran and Iraq to Anatolia',
        'A dynasty from the Qiniq tribe of the Oghuz. Tughril and Chaghri Beg founded the Great Seljuk state in 1037 and '
        'defeated the Ghaznavids at Dandanaqan in 1040. The victory at Manzikert in 1071 opened Anatolia to Turkic '
        'settlement, and the Sultanate of Rum ruled there from 1077 to the early 14th century. The Oghuz who came west '
        'with the Seljuks are the linguistic ancestors of today\'s Turks and Azerbaijanis.',
        [('Seljuk dynasty', 'Seljuk_dynasty'), ('Seljuk Empire', 'Seljuk_Empire'), ('Sultanate of Rum', 'Sultanate_of_Rum')],
        ['oghuz/azerbaijani', 'oghuz/turkish']),
    'kipchak/trunk': ('Kipchak branch', 'kip', 'Where it is spoken',
        'From Crimea and the Volga-Ural region across Kazakhstan to the Tian Shan',
        'Northwestern Turkic. The Kipchaks appear in the Kimek confederation on the Irtysh and, together with the Cumans, '
        'dominated the steppe from the Irtysh to the Danube between the 11th and 13th centuries. After the Mongol conquest '
        'the Golden Horde became largely Kipchak-speaking, and the khanates that followed it shaped the Tatars, Bashkirs, '
        'Crimean Tatars, Kazakhs and Kyrgyz of today.',
        [('Kipchaks', 'Kipchaks'), ('Kipchak languages', 'Kipchak_languages'), ('Golden Horde', 'Golden_Horde')],
        ['kipchak/tatar', 'kipchak/bashkir', 'kipchak/crimean-tatar', 'kipchak/kazakh', 'kipchak/kyrgyz']),
    'karluk/trunk': ('Karluk branch', 'kar', 'Where it is spoken',
        'Uzbekistan and its neighbours, and the Tarim Basin in Xinjiang, China',
        'Southeastern Turkic. The Karluk tribes are first mentioned in the 7th century between the Altai and the Tian Shan. '
        'The Kara-Khanid Khanate, which grew out of the Karluk confederation, was the first Turkic dynasty to adopt Islam, '
        'around 960, and Mahmud al-Kashgari wrote his dictionary of the Turkic languages in that world in 1072-74. '
        'Under the Timurids, Chagatai became the literary language of Central Asia. Uzbek and Uyghur both continue it.',
        [('Karluks', 'Karluks'), ('Karluk languages', 'Karluk_languages'), ('Kara-Khanid Khanate', 'Kara-Khanid_Khanate'),
         ('Chagatai language', 'Chagatai_language')],
        ['karluk/uzbek', 'karluk/uyghur']),
    'siberian/trunk': ('Siberian branch', 'sib', 'Where it is spoken',
        'The Altai, the Sayan mountains, the upper Yenisei and the Lena basin, Russia',
        'Northeastern Turkic. This is a regional grouping more than a proven single branch: the Sakha (Yakut) line probably '
        'separated early from the rest of Common Turkic, while Tuvan, Khakas and the Altai varieties form a clearer South '
        'Siberian unit. These languages stayed closest to the old Turkic homeland and kept many archaic features.',
        [('Siberian Turkic languages', 'Siberian_Turkic_languages')],
        ['siberian/yenisei-kyrgyz', 'siberian/khakas', 'siberian/altai', 'siberian/tuvan', 'siberian/sakha']),
    'siberian/yenisei-kyrgyz': ('Yenisei Kyrgyz', 'sib', 'Where they lived',
        "The upper Yenisei and the Minusinsk Basin, in today's Khakassia, Russia",
        'A people of the upper Yenisei known from Chinese and Old Turkic sources. In 840 they overthrew the Uyghur Khaganate '
        'and sacked its capital Ordu-Baliq, though their own steppe power faded within a century. Many were resettled in the '
        '18th century under Dzungar and Qing rule. The Khakas live in their old heartland; today\'s Kyrgyz carry the name and '
        'descend from them only in part, by a path that is still debated.',
        [('Yenisei Kyrgyz', 'Yenisei_Kyrgyz')],
        ['siberian/khakas', 'kipchak/kyrgyz']),
}

def lineage(branch):
    f = f"lineages/{branch.replace('/', '--')}.md"
    r = subprocess.run(['git', 'show', f'{REMOTE}/{branch}:{f}'], capture_output=True, text=True, cwd=os.path.join(HERE, '..'))
    if r.returncode != 0:
        return f, []
    return f, [l for l in r.stdout.splitlines() if l.startswith('- ')]

def blink(b):
    return f'[`{b}`]({REPO}/tree/{b})'

def common_tail(branch, key=None):
    f, events = lineage(branch)
    o = []
    if events:
        o += ['## Commits on this branch', '', 'Each commit is one historical event.', ''] + events + ['',
              f'Run `git log --oneline {branch}` to see them together with the history they build on. '
              f'The same list is in [`{f}`]({f}).', '']
    return o

def footer(extra=''):
    return ['---', '',
            f'Part of [turkic-git]({REPO}#readme), the history of the Turkic peoples told as a git repository. '
            f'See every branch in the [interactive graph]({SITE}). ' + extra +
            'This is a teaching metaphor: branches follow the linguistic classification of the languages, not ancestry or '
            'politics, and peoples mixed far more than a graph shows.', '']

def people_readme(branch, key):
    d = P[key]; g, gdesc = GROUP_INFO[d['group']]
    title = TITLE.get(branch, d['name'])
    # No hotlinked images here: Wikimedia answers GitHub's image proxy with HTTP 429, so they would show as broken.
    brief = d['brief'].replace(' In the graph this row also carries the shared Oghuz trunk.', '')
    o = [f'# {title}', '', f'`{branch}`', '',
         '| | |', '|---|---|',
         f"| **{'Name' if key == 'ots' else 'Self-name'}** | {d['endonym']} |",
         f"| **{WHERE_LABEL.get(key, 'Where they live today')}** | {d['where']} |"]
    if key != 'ots':
        o.append(f'| **Branch** | {g}: {gdesc} |')
    o += ['', brief, '']
    o += common_tail(branch, key)
    o += ['## Read more', '']
    o += [f'- [{t}]({WIKI}{urllib.parse.quote(s)}) on Wikipedia' for t, s in d['wiki']]
    o += [f'- [Open this branch in the interactive graph]({SITE}#{key}) for photos' + (' and the flag' if key in FLAGS else ''), '']
    o += footer()
    return '\n'.join(o)

def extra_readme(branch):
    title, group, wl, where, brief, wiki, kids = EXTRA[branch]
    g, gdesc = GROUP_INFO[group]
    o = [f'# {title}', '', f'`{branch}`', '', '| | |', '|---|---|',
         f'| **{wl}** | {where} |', f'| **Branch** | {g}: {gdesc} |', '', brief, '']
    o += common_tail(branch)
    o += ['## Branches that continue from here', ''] + [f'- {blink(k)}' for k in kids] + ['']
    o += ['## Read more', ''] + [f'- [{t}]({WIKI}{urllib.parse.quote(s)}) on Wikipedia' for t, s in wiki]
    o += [f'- [Interactive graph]({SITE})', '']
    o += footer()
    return '\n'.join(o)

os.makedirs(OUT, exist_ok=True)
n = 0
for b, k in PEOPLE.items():
    open(os.path.join(OUT, b.replace('/', '--') + '.md'), 'w').write(people_readme(b, k)); n += 1
for b in EXTRA:
    open(os.path.join(OUT, b.replace('/', '--') + '.md'), 'w').write(extra_readme(b)); n += 1
print(n, 'READMEs written to', OUT)
