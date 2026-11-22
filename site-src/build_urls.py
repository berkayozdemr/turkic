"""Wikimedia Commons URLs and licence links for the images in content.py."""
import hashlib, urllib.parse
from content import P

# Files whose original is no wider than the 960px thumbnail bucket: link the original.
ORIGINAL = {'Mosque "Kul Sharif".jpg', 'Old Chuvash men.jpg', 'Chuvash woman in traditional attire.jpg', 'Gagauz-children.jpg',
            'Azerigirls.JPG', 'Ashiqs in Tabriz.jpg', 'Altaian horseman.jpg', 'Yakut Sakha hunter.jpg'}
ORIGINAL |= {k for k in [x['file'] for v in P.values() if v for x in v['images']] if k.startswith('Khalaj coin')}
LIC = {'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0/', 'CC BY-SA 3.0': 'https://creativecommons.org/licenses/by-sa/3.0/',
       'CC BY-SA 2.0': 'https://creativecommons.org/licenses/by-sa/2.0/', 'CC BY 4.0': 'https://creativecommons.org/licenses/by/4.0/',
       'CC BY 3.0': 'https://creativecommons.org/licenses/by/3.0/', 'CC BY 2.0': 'https://creativecommons.org/licenses/by/2.0/',
       'CC0': 'https://creativecommons.org/publicdomain/zero/1.0/', 'GFDL': 'https://www.gnu.org/licenses/fdl-1.3.html', 'Public domain': ''}

def image_urls(f):
    n = f.replace(' ', '_'); h = hashlib.md5(n.encode()).hexdigest(); q = urllib.parse.quote(n)
    base = f'https://upload.wikimedia.org/wikipedia/commons'
    src = f'{base}/{h[0]}/{h[:2]}/{q}' if f in ORIGINAL else f'{base}/thumb/{h[0]}/{h[:2]}/{q}/960px-{q}'
    return src, f'https://commons.wikimedia.org/wiki/File:{q}'

