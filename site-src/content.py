# Content for each clickable branch. Reuses the wording of hero-image-src/map.py and the
# research in research-and-repo-audit.md. Images: Wikimedia Commons, file name + license + author
# as recorded on the file page (checked 2026-11-20).

GROUP_INFO = {
    'oghur': ('Oghur', 'Bulgharic or "r-Turkic". The first branch to split off, around the 1st century BCE.'),
    'kip': ('Kipchak', 'Northwestern Turkic, from the Black Sea steppe to the Altai.'),
    'kar': ('Karluk', 'Southeastern Turkic, heir to the Karakhanid and Chagatai literary tradition.'),
    'olduy': ('Old Uyghur line', 'The eastern Old Turkic line of the Uyghur Khaganate and the Qocho kingdom.'),
    'oghuz': ('Oghuz', 'Southwestern Turkic, carried west by the Seljuks from the 11th century.'),
    'arghu': ('Arghu', 'A branch of its own, represented today only by Khalaj.'),
    'sib': ('Siberian', 'Northeastern Turkic. A regional grouping: Sakha split off early, and only South Siberian forms a clear unit.'),
    'main': ('main', 'The shared trunk.'),
    'ots': ('turkic-states', 'An octopus merge of independent states.'),
}

def I(file, lic, author, caption):
    return dict(file=file, lic=lic, author=author, caption=caption)

P = {}
P['main'] = dict(
    name='Proto-Turkic and the steppe trunk', group='main', ref='main',
    endonym='Türk (Old Turkic 𐱅𐰇𐰼𐰰)',
    where='Eastern Inner Asia: Mongolia, the Sayan-Altai and the Ordos-to-Altai belt are the candidate homelands',
    brief=('Every branch goes back to one Proto-Turkic speech community on the eastern steppe, roughly 2,000 years ago. '
           'The Göktürk Khaganate (552) was the first state to carry the name "Türk", and its Orkhon inscriptions of the 730s, '
           'with the slightly older Tonyukuk stele, are among the oldest long Turkic texts. Old Turkic is the earliest written '
           'form of Common Turkic, not the parent of every branch, and the order in which the Common Turkic branches split is not settled.'),
    moments=[('c. 1st c. BCE', 'Oghur splits off: the oldest fork'), ('552', 'Göktürk Khaganate founded'),
             ('732-735', 'Orkhon inscriptions (Kül Tegin, Bilge Qaghan)'), ('840', 'The Uyghur Khaganate falls; the steppe trunk breaks apart')],
    wiki=[('Proto-Turkic language', 'Proto-Turkic_language'), ('Göktürks', 'Göktürks'), ('Orkhon inscriptions', 'Orkhon_inscriptions')],
    images=[I('Kultigin Monument of Orkhon Inscriptions.jpeg', 'CC BY-SA 4.0', 'Vezirtonyukuk', 'The Kül Tegin stele (732), one of the Orkhon inscriptions, Mongolia'),
            I('Turkic Head of Koltegin Statue (35324303410).jpg', 'CC0', 'Gary Todd', 'Head of a statue of Kül Tegin, National Museum of Mongolia')],
)
P['danube'] = dict(
    name='Danube Bulgars', group='oghur', ref='oghur/danube-bulgar', endonym='Bulgar (archived branch)',
    where="Historically the lower Danube, today's Bulgaria",
    brief=('Turkic-speaking founders of the Bulgar state on the Danube in 681. Over the following centuries the ruling '
           'Bulgars merged with the Slavic-speaking majority, and by about 900 the state used a Slavic language. '
           'The name Bulgaria survives; the Oghur language does not, which is why this branch is drawn as archived.'),
    moments=[('c. 632', 'Old Great Bulgaria on the Pontic steppe'), ('681', 'Danube Bulgar state founded'),
             ('864', 'Christianisation under Boris I'), ('c. 900', 'Slavic-speaking: the branch is archived')],
    wiki=[('Bulgars', 'Bulgars'), ('First Bulgarian Empire', 'First_Bulgarian_Empire')],
    images=[I('JEŹDZIEC Z MADARY.JPG', 'Public domain', 'Dom2002', 'The Madara Rider, an early medieval rock relief in north-east Bulgaria'),
            I('Pliska-svik.jpg', 'CC BY-SA 3.0', 'Wikimedia Commons contributor', 'Pliska, the first capital of the Danube Bulgar state')],
)
P['chuvash'] = dict(
    name='Chuvash', group='oghur', ref='oghur/chuvash', endonym='Chăvash · Чӑваш',
    where='Chuvashia on the middle Volga, Russia, and neighbouring regions',
    brief=('About a million speakers of the only living Oghur language, the closest living relative of Volga Bulgar. '
           'Chuvash keeps the "r" and "l" where other Turkic languages have "z" and "sh", the feature that gives the branch '
           'the name "r-Turkic". Most Chuvash are Orthodox Christian.'),
    moments=[('463', 'Oghurs on the Pontic steppe'), ('922', 'Volga Bulgaria adopts Islam'), ('1236', 'Mongol conquest of Volga Bulgaria')],
    wiki=[('Chuvash people', 'Chuvash_people'), ('Chuvash language', 'Chuvash_language')],
    images=[I('Chuvash woman in traditional attire.jpg', 'Public domain', 'Vasily (William) Carrick', 'Chuvash woman in traditional dress, Simbirsk province, 1870s'),
            I('Old Chuvash men.jpg', 'Public domain', 'Ivan Zelenov', 'Chuvash men, Kazan province, early 20th century')],
)
P['tatar'] = dict(
    name='Tatars (Volga Tatars)', group='kip', ref='kipchak/tatar', endonym='Tatar · Татар',
    where='Tatarstan (Kazan), the Volga-Ural region and Siberia, Russia',
    brief=('The largest Turkic people of Russia and its second-largest ethnic group, with Kazan as the cultural centre. '
           'Their language is Kipchak; their heritage also draws on Volga Bulgaria, and how much weight each side carries '
           'is still debated. The Khanate of Kazan (1438) was conquered by Muscovy in 1552.'),
    moments=[('922', 'Volga Bulgaria adopts Islam'), ('1240s', 'Golden Horde'), ('1438', 'Khanate of Kazan'), ('1552', 'Conquest of Kazan by Muscovy')],
    wiki=[('Volga Tatars', 'Volga_Tatars'), ('Tatar language', 'Tatar_language')],
    images=[I('Mosque "Kul Sharif".jpg', 'CC BY 2.0', 'Ilya Tsvetkov', 'Kul Sharif mosque in the Kazan Kremlin'),
            I('Bolgar. White Mosque P6270610 2575.jpg', 'CC BY-SA 4.0', 'Alexxx1979', 'The White Mosque at Bolgar, the old Volga Bulgar capital')],
)
P['bashkir'] = dict(
    name='Bashkirs', group='kip', ref='kipchak/bashkir', endonym='Bashqort · Башҡорт',
    where='Bashkortostan in the southern Urals, Russia',
    brief=('Close linguistic neighbours of the Tatars, described already by Ibn Fadlan in the 10th century. '
           'Bashkir clans came under Muscovite rule in the 1550s; whether by agreement or conquest is debated. '
           'Known for a strong tradition of horse breeding, wild-hive beekeeping and epic poetry such as Ural-batyr.'),
    moments=[('c. 922', 'Bashkirs described by Ibn Fadlan'), ('1550s', 'Bashkir clans come under Muscovy')],
    wiki=[('Bashkirs', 'Bashkirs'), ('Bashkir language', 'Bashkir_language')],
    images=[I('Holiday Bashkir national costume 52.jpg', 'CC BY-SA 4.0', 'Рөстәм Нурыев', 'Bashkir festive national costume'),
            I('Mausoleum of Turahan.jpg', 'CC BY 3.0', 'Andrey Kudryashov', 'Mausoleum of Turahan, 14th century, Bashkortostan')],
)
P['crimean'] = dict(
    name='Crimean Tatars', group='kip', ref='kipchak/crimean-tatar', endonym='Qırımtatar · Qırımlı',
    where='Crimea; large communities in Türkiye, Uzbekistan and Romania',
    brief=('The indigenous Turkic people of Crimea. Their language is Kipchak, with a southern dialect of Oghuz origin. '
           'The Crimean Khanate lasted from 1441 to 1783. In 1944 the whole people was deported to Central Asia; most '
           'were able to return only from the late 1980s.'),
    moments=[('c. 1050', 'Cuman-Kipchak steppe'), ('1240s', 'Golden Horde'), ('1441', 'Crimean Khanate'), ('1944', 'Deportation')],
    wiki=[('Crimean Tatars', 'Crimean_Tatars'), ('Crimean Tatar language', 'Crimean_Tatar_language')],
    images=[I('Carlo Bossoli Khanpalast von Bachcisaraj 1857.jpg', 'Public domain', 'Carlo Bossoli', "The Khan's Palace in Bakhchisaray, painted in 1857"),
            I('Мечеть Узбека.JPG', 'CC BY-SA 3.0', 'Kiyanka', 'The Mosque of Uzbek Khan (1314) in Stary Krym')],
)
P['kazakh'] = dict(
    name='Kazakhs', group='kip', ref='kipchak/kazakh', endonym='Qazaq · Қазақ',
    where='Kazakhstan; also Xinjiang (China), western Mongolia and Uzbekistan',
    brief=('Heirs of the steppe nomads, traditionally organised in three zhuz (hordes). The Kazakh Khanate formed around 1465 '
           'when groups broke away from the same Uzbek ulus whose remainder later went south with Shaybani. '
           'Kazakhstan, independent since 1991, is the largest Turkic state by area.'),
    moments=[('c. 1465', 'Kazakh Khanate'), ('1991', 'Independence'), ('2009', 'Founding member of the Turkic Council')],
    wiki=[('Kazakhs', 'Kazakhs'), ('Kazakh language', 'Kazakh_language')],
    images=[I('Kazakh Eagle Hunters.JPG', 'CC BY-SA 3.0', 'Altaihunters', 'Kazakh eagle hunters with their golden eagles'),
            I('Huang Qing Zhigong Tu, 1769, Kazakh leader and his wife.jpg', 'Public domain', 'Huang Qing Zhigong Tu (1769)', 'A Kazakh leader and his wife, Qing album of 1769')],
)
P['kyrgyz'] = dict(
    name='Kyrgyz', group='kip', ref='kipchak/kyrgyz', endonym='Kyrgyz · Кыргыз',
    where='Kyrgyzstan and the Tian Shan; also Xinjiang and Tajikistan',
    brief=('Mountain pastoralists of the Tian Shan. Their language is classed as Kipchak, while the name links them to the '
           'medieval Yenisei Kyrgyz; how far the modern people descend from them is debated. The Manas epic is among the '
           'longest oral epics in the world.'),
    moments=[('c. 1500', 'Kyrgyz established in the Tian Shan'), ('1991', 'Independence'), ('2009', 'Founding member of the Turkic Council')],
    wiki=[('Kyrgyz people', 'Kyrgyz_people'), ('Kyrgyz language', 'Kyrgyz_language')],
    images=[I('Ala-Bel pass, Kyrgyzstan (29561433347).jpg', 'CC BY 2.0', 'Ninara', 'Yurts at the Ala-Bel pass, Kyrgyzstan'),
            I('Kyrgyz man with ak-kalpak hat (ак-калпак шапкa).jpg', 'CC BY-SA 4.0', 'Petar Milošević', 'A Kyrgyz man in an ak-kalpak felt hat')],
)
P['uzbek'] = dict(
    name='Uzbeks', group='kar', ref='karluk/uzbek', endonym='Oʻzbek',
    where='Uzbekistan; also Afghanistan, Tajikistan, Kyrgyzstan and Kazakhstan',
    brief=('The most numerous people of Central Asia. Uzbek continues the Karluk speech of the oasis cities and the Chagatai '
           'literary culture of Samarkand and Bukhara. The name comes from the Kipchak-speaking Shaybanid Uzbeks who arrived '
           'around 1500 and assimilated to the Karluk-speaking majority.'),
    moments=[('c. 960', 'Karakhanids'), ('1072-74', "al-Kashgari's Dīwān"), ('1500-07', 'Shaybanid Uzbeks'), ('1991', 'Independence')],
    wiki=[('Uzbeks', 'Uzbeks'), ('Uzbek language', 'Uzbek_language')],
    images=[I('Registan 01.jpg', 'CC0', 'Bernard Gagnon', 'The Registan, Samarkand'),
            I('Khiva, Uzbekistan 74 (161).jpg', 'CC BY-SA 4.0', 'Jaan Künnap', 'Itchan Kala, the walled old town of Khiva')],
)
P['uyghur'] = dict(
    name='Uyghurs', group='kar', ref='karluk/uyghur', endonym='Uyghur · ئۇيغۇر',
    where='Xinjiang Uyghur Autonomous Region, China; also Kazakhstan and Kyrgyzstan',
    brief=('The oasis-city people of the Tarim Basin (Kashgar, Turpan, Hotan), writing in an Arabic-based script. '
           'Modern Uyghur continues the Karluk speech of the Kara-Khanid realm and the Chagatai tradition, not Old Uyghur '
           'directly; the old name was revived for the modern people in 1921.'),
    moments=[('c. 960', 'Karakhanids'), ('1072-74', "al-Kashgari's Dīwān"), ('c. 1500', 'Old Uyghur heritage absorbed'), ('1921', 'The name "Uyghur" revived')],
    wiki=[('Uyghurs', 'Uyghurs'), ('Uyghur language', 'Uyghur_language')],
    images=[I('Uyghur Meshrep.jpg', 'CC BY-SA 2.0', 'travelingmipo (Flickr)', 'Musicians at a meshrep gathering, Yarkand'),
            I('KashgarNaan.jpg', 'CC BY-SA 3.0', 'Doron', 'Baking naan in Kashgar')],
)
P['yugur'] = dict(
    name='Western Yugurs', group='olduy', ref='old-uyghur/yugur', endonym='Sarïg Yogïr',
    where='Sunan Yugur Autonomous County, Gansu, China',
    brief=('A few thousand speakers, mostly Buddhist. Western Yugur is usually named as the living descendant of Old Uyghur, '
           'the language of the Uyghur Khaganate and the Qocho and Gansu Uyghur kingdoms, though its exact placement is debated. '
           'Some Yugurs speak a Mongolic language instead (Eastern Yugur).'),
    moments=[('840', 'Uyghur Khaganate falls'), ('c. 850', 'Qocho and Gansu Uyghur kingdoms'), ('today', 'Western Yugur in Gansu')],
    wiki=[('Yugurs', 'Yugur_people'), ('Western Yugur language', 'Western_Yugur_language'), ('Old Uyghur language', 'Old_Uyghur')],
    images=[I('Pair of Uyghur donors from the Bezeklik Caves.jpg', 'CC BY 4.0', 'Unknown artist', 'Old Uyghur donors, Bezeklik cave mural, Turpan (Qocho kingdom)'),
            I('Sunan gate on Chinese Yugur Scenic Corridor.jpg', 'CC BY-SA 2.0', 'Terry Wu', 'Sunan, the Yugur county in Gansu')],
)
P['turkmen'] = dict(
    name='Turkmens', group='oghuz', ref='oghuz/turkmen', endonym='Türkmen',
    where='Turkmenistan; also north-eastern Iran and northern Afghanistan',
    brief=('The Oghuz who stayed east of the Caspian. The name "Türkmen" is first recorded in the 10th century for Muslim '
           'Oghuz in general; the modern people consolidated later. Known for tribal carpets, the Akhal-Teke horse and the poet Magtymguly.'),
    moments=[('c. 770', 'Oghuz Yabgu state'), ('c. 987', '"Türkmen" first attested'), ('1991', 'Independence')],
    wiki=[('Turkmens', 'Turkmens'), ('Turkmen language', 'Turkmen_language')],
    images=[I('Gorskii 20005u.jpg', 'Public domain', 'Sergei Prokudin-Gorsky', 'Men on a carpet in front of a yurt, Russian Turkestan; early colour photo, c. 1905-1915'),
            I("Traditional turkmen embroidery for women's dress.jpg", 'CC BY-SA 4.0', 'Bayram A', "Traditional Turkmen embroidery for a woman's dress")],
)
P['azeri'] = dict(
    name='Azerbaijanis', group='oghuz', ref='oghuz/azerbaijani', endonym='Azərbaycanlı',
    where='Azerbaijan and north-western Iran; also Georgia, Russia and Türkiye',
    brief=('An Oghuz people of the South Caucasus and north-western Iran, whose Turkification ran from the Seljuk 11th century '
           'to the Safavid 16th. Divided between two states since the 19th century, more Azerbaijanis live in Iran than in Azerbaijan. '
           'In the graph this row also carries the shared Oghuz trunk.'),
    moments=[('c. 770', 'Oghuz Yabgu state'), ('1040', 'Seljuks'), ('1501', 'Safavids'), ('1918', 'First republic'), ('1991', 'Independence')],
    wiki=[('Azerbaijanis', 'Azerbaijanis'), ('Azerbaijani language', 'Azerbaijani_language')],
    images=[I('Ashiqs in Tabriz.jpg', 'GFDL', 'Vivas', 'Ashiqs, travelling bards, in Tabriz'),
            I('Azerigirls.JPG', 'CC BY-SA 3.0', 'Oleg Litvin', 'Azerbaijani folk dancers')],
)
P['turkish'] = dict(
    name='Turks', group='oghuz', ref='oghuz/turkish', endonym='Türk',
    where='Türkiye and Northern Cyprus; the Balkans; diaspora in western Europe',
    brief=('The largest Turkic people, with about 85 million speakers. Heirs of the Oghuz who entered Anatolia after Manzikert '
           '(1071), of the Seljuks of Rum and of the Ottoman state. The Republic of Türkiye was founded in 1923 and switched to a '
           'Latin alphabet in 1928.'),
    moments=[('1071', 'Manzikert'), ('c. 1299', 'Ottomans'), ('1923', 'Republic of Türkiye'), ('2009', 'Founding member of the Turkic Council')],
    wiki=[('Turkish people', 'Turkish_people'), ('Turkish language', 'Turkish_language')],
    images=[I('Süleymaniye Mosque - Istanbul, Turkey - October 11, 2025.jpg', 'CC BY-SA 4.0', 'Giorgio Galeotti', 'Süleymaniye Mosque, Istanbul'),
            I('Eskisehir Odunpazarı tour in 2018 8523.jpg', 'CC BY-SA 4.0', 'Dosseman', 'Ottoman-era houses in Odunpazarı, Eskişehir')],
)
P['gagauz'] = dict(
    name='Gagauz', group='oghuz', ref='oghuz/gagauz', endonym='Gagauz',
    where='Gagauzia in southern Moldova; south-western Ukraine',
    brief=('Around 150,000 Orthodox Christian speakers of an Oghuz language close to Turkish. They settled in Bessarabia from 1812, '
           'coming from what is now north-eastern Bulgaria; their earlier origins are debated, with several competing theories. '
           'Gagauzia has been an autonomous region of Moldova since 1994.'),
    moments=[('from 1812', 'Gagauz settle in Bessarabia'), ('1994', 'Autonomy within Moldova')],
    wiki=[('Gagauz people', 'Gagauz_people'), ('Gagauz language', 'Gagauz_language')],
    images=[I('Hederlez in Chișinău, May 7 2017 (15).jpg', 'CC0', 'Gikü', 'Gagauz celebrating Hederlez in Chișinău'),
            I('Gagauz-children.jpg', 'Public domain', 'Danyalov', 'Gagauz family, early 20th century')],
)
P['khalaj'] = dict(
    name='Khalaj', group='arghu', ref='arghu/khalaj', endonym='Xalaj',
    where='Villages between Qom and Tafresh (Markazi province), central Iran',
    brief=('A small, endangered language community of roughly 19,000 speakers, many of whom are shifting to Persian. '
           'Khalaj keeps archaic features lost everywhere else, such as initial h- (hadaq "foot"), and Gerhard Doerfer showed '
           'in the 1970s that it is a branch of its own, not a dialect of Azerbaijani.'),
    moments=[('1070s', "al-Kashgari records the Arghu dialect, held to be Khalaj's ancestor"), ('1970s', 'Doerfer: an independent branch')],
    wiki=[('Khalaj people', 'Khalaj_people'), ('Khalaj language', 'Khalaj_language')],
    images=[I('Tafresh city Markazi Province Iran Mostafa Meraji 01.jpg', 'CC BY-SA 4.0', 'Mostafa Meraji', 'Tafresh, Markazi province, near the Khalaj-speaking villages'),
            I('Khalaj coin. 8th century CE. Imitating Sasanian king Peroz I (438-457). Crowned bust right. Shiva standing facing, holding trident, to left χαλαγγ or χαλασσ in Bactrian.jpg',
              'CC BY-SA 3.0', 'CNG Coins', 'A Khalaj coin from 8th-century Afghanistan; the link to today\'s Khalaj is debated')],
)
P['khakas'] = dict(
    name='Khakas', group='sib', ref='siberian/khakas', endonym='Tadar · Хакас',
    where='Khakassia on the upper Yenisei, Russia',
    brief=('A South Siberian people formed from several Yenisei groups; the name Khakas was adopted in the 1920s. '
           'They live in the old heartland of the Yenisei Kyrgyz, who overthrew the Uyghur Khaganate in 840. '
           'Fuyu Kyrgyz in north-east China is linguistically closest to Khakas.'),
    moments=[('840', 'Yenisei Kyrgyz take Ordu-Baliq'), ('18th c.', 'Dzungar and Qing resettlements of Yenisei Kyrgyz')],
    wiki=[('Khakas', 'Khakas'), ('Khakas language', 'Khakas_language')],
    images=[I('Хакасы.JPG', 'Public domain', 'Unknown photographer', 'Khakas musicians, early 20th century'),
            I('Хакаски с детьми.JPG', 'Public domain', 'Unknown photographer', 'Khakas women with children, early 20th century')],
)
P['altai'] = dict(
    name='Altaians', group='sib', ref='siberian/altai', endonym='Altay-kizhi · Алтай',
    where='Altai Republic, Russia',
    brief=('Peoples of the Altai mountains, the region often seen as the cradle of the early Türks. Southern Altai is close to '
           'Kipchak by vocabulary, Northern Altai to the other South Siberian languages. The area became the Oyrot Autonomous '
           'Oblast in 1922 and has been the Altai Republic since 1992.'),
    moments=[('1922', 'Oyrot Autonomous Oblast'), ('1992', 'Named the Altai Republic')],
    wiki=[('Altaians', 'Altaians'), ('Altai language', 'Altai_language')],
    images=[I('Altai Ail - traditional dwelling.jpg', 'CC BY-SA 4.0', 'Alexandr Frolov', 'An ail, the traditional Altai dwelling'),
            I('Altaian horseman.jpg', 'CC BY-SA 2.0', 'P. Filatov', 'Altaian horseman in national costume')],
)
P['tuvan'] = dict(
    name='Tuvans', group='sib', ref='siberian/tuvan', endonym='Tyva · Тыва',
    where='Tuva, Russia; also western Mongolia and Xinjiang',
    brief=('Mostly Buddhist herders at the headwaters of the Yenisei, famous for throat singing (khöömei). '
           'Tuvan belongs to the Sayan group of South Siberian Turkic. Tuva was nominally independent as the Tuvan People\'s '
           'Republic from 1921 and joined the Soviet Union in 1944.'),
    moments=[('1921', "Tuvan People's Republic"), ('1944', 'Joins the Soviet Union')],
    wiki=[('Tuvans', 'Tuvans'), ('Tuvan language', 'Tuvan_language')],
    images=[I('Тувинские мастера хоомея.jpg', 'CC BY-SA 4.0', 'Agilight', 'Masters of khöömei (throat singing), Kyzyl'),
            I('Tuvan wrestlers 2.jpg', 'CC BY 2.0', 'Dmitriy Stepanov', 'Tuvan khuresh wrestlers')],
)
P['sakha'] = dict(
    name='Sakha (Yakuts)', group='sib', ref='siberian/sakha', endonym='Sakha · Саха',
    where='Sakha Republic (Yakutia), north-eastern Siberia, Russia',
    brief=('The northernmost Turkic people: horse and cattle breeders in one of the coldest inhabited regions on Earth. '
           'The Sakha-Dolgan line probably separated early from the rest of Common Turkic; the people moved north to the Lena '
           'between the 13th and 15th centuries. Their summer festival is Yhyakh.'),
    moments=[('13th-15th c.', 'Migration north to the Lena'), ('1632', 'Yakutsk founded by Russian Cossacks')],
    wiki=[('Yakuts', 'Yakuts'), ('Yakut language', 'Yakut_language')],
    images=[I('Yhyakh dancers, Sangar, Yakutia.jpg', 'CC BY-SA 4.0', 'Tenebroid', 'Dancers at the Yhyakh summer festival, Sangar'),
            I('Yakut Sakha hunter.jpg', 'CC BY-SA 4.0', 'Somogotto', 'A Sakha hunter, early 20th century')],
)
P['ots'] = dict(
    name='Organization of Turkic States', group='ots', ref='turkic-states', endonym='Türk Devletleri Teşkilatı and others',
    where='Members: Azerbaijan, Kazakhstan, Kyrgyzstan, Türkiye, Uzbekistan. Secretariat in Istanbul',
    brief=('In 2009 four independent states (Azerbaijan, Kazakhstan, Kyrgyzstan and Türkiye) signed the Nakhchivan Agreement '
           'and formed the Turkic Council. Uzbekistan joined in 2019, and in 2021 it was renamed the Organization of Turkic States. '
           'It is cooperation between sovereign countries, not one state: the octopus merge in the graph.'),
    moments=[('2009', 'Nakhchivan Agreement: the Turkic Council'), ('2019', 'Uzbekistan joins'), ('2021', 'Renamed Organization of Turkic States')],
    wiki=[('Organization of Turkic States', 'Organization_of_Turkic_States')],
    images=[I('Headquarter of The Organization of Turkic States in 2022 (1).jpg', 'CC BY-SA 4.0', 'Mehman Ibragimov', 'Secretariat of the Organization of Turkic States, Istanbul')],
)
P['karluk'] = None  # shared Karluk trunk: handled in the page (opens Uzbek)
