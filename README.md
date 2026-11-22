# turkic-git

The history of the Turkic peoples, told as a git repository.

## Explore

- **[Interactive graph](https://berkayozdemr.github.io/turkic/)**: the whole family on one screen. Click a branch to read about that people.
- **Every branch has its own README** with a short summary of that people: their own name, where they live today, the events on the branch, images and links to Wikipedia. Switch branch on GitHub, or follow a link:

| Group | Branches |
|---|---|
| Oghur | [`oghur/trunk`](https://github.com/berkayozdemr/turkic/tree/oghur/trunk) · [`oghur/chuvash`](https://github.com/berkayozdemr/turkic/tree/oghur/chuvash) · [`oghur/danube-bulgar`](https://github.com/berkayozdemr/turkic/tree/oghur/danube-bulgar) · [`oghur/volga-bulgar`](https://github.com/berkayozdemr/turkic/tree/oghur/volga-bulgar) |
| Kipchak | [`kipchak/trunk`](https://github.com/berkayozdemr/turkic/tree/kipchak/trunk) · [`kipchak/bashkir`](https://github.com/berkayozdemr/turkic/tree/kipchak/bashkir) · [`kipchak/crimean-tatar`](https://github.com/berkayozdemr/turkic/tree/kipchak/crimean-tatar) · [`kipchak/kazakh`](https://github.com/berkayozdemr/turkic/tree/kipchak/kazakh) · [`kipchak/kyrgyz`](https://github.com/berkayozdemr/turkic/tree/kipchak/kyrgyz) · [`kipchak/tatar`](https://github.com/berkayozdemr/turkic/tree/kipchak/tatar) |
| Karluk | [`karluk/trunk`](https://github.com/berkayozdemr/turkic/tree/karluk/trunk) · [`karluk/uyghur`](https://github.com/berkayozdemr/turkic/tree/karluk/uyghur) · [`karluk/uzbek`](https://github.com/berkayozdemr/turkic/tree/karluk/uzbek) |
| Old Uyghur line | [`old-uyghur`](https://github.com/berkayozdemr/turkic/tree/old-uyghur) |
| Oghuz | [`oghuz/trunk`](https://github.com/berkayozdemr/turkic/tree/oghuz/trunk) · [`oghuz/azerbaijani`](https://github.com/berkayozdemr/turkic/tree/oghuz/azerbaijani) · [`oghuz/gagauz`](https://github.com/berkayozdemr/turkic/tree/oghuz/gagauz) · [`oghuz/seljuk`](https://github.com/berkayozdemr/turkic/tree/oghuz/seljuk) · [`oghuz/turkish`](https://github.com/berkayozdemr/turkic/tree/oghuz/turkish) · [`oghuz/turkmen`](https://github.com/berkayozdemr/turkic/tree/oghuz/turkmen) |
| Siberian | [`siberian/trunk`](https://github.com/berkayozdemr/turkic/tree/siberian/trunk) · [`siberian/altai`](https://github.com/berkayozdemr/turkic/tree/siberian/altai) · [`siberian/khakas`](https://github.com/berkayozdemr/turkic/tree/siberian/khakas) · [`siberian/sakha`](https://github.com/berkayozdemr/turkic/tree/siberian/sakha) · [`siberian/tuvan`](https://github.com/berkayozdemr/turkic/tree/siberian/tuvan) · [`siberian/yenisei-kyrgyz`](https://github.com/berkayozdemr/turkic/tree/siberian/yenisei-kyrgyz) |
| Organization of Turkic States | [`turkic-states`](https://github.com/berkayozdemr/turkic/tree/turkic-states) |


- `main` is the common Proto-Turkic / Common Turkic trunk. It ends in 840 CE, when the Uyghur Khaganate falls and the steppe trunk breaks apart.
- Branches follow the standard linguistic grouping: `oghur/*` (Bulghar, today only Chuvash), `oghuz/*` (Turkish, Azerbaijani, Turkmen, Gagauz), `kipchak/*` (Kazakh, Kyrgyz, Tatar, Bashkir, Crimean Tatar), `karluk/*` (Uzbek, Uyghur) and `siberian/*` (Sakha, Tuvan, Khakas, Altai).
- Merge commits mark peoples that formed from more than one line, for example Volga Bulgars + Kipchaks (Kazan Tatars), Karluk + Kipchak (Uzbeks), Yenisei Kyrgyz + Kipchak-speaking tribes (Kyrgyz).
- `oghur/danube-bulgar` is an archived branch: the Danube Bulgars became Slavic-speaking.
- `turkic-states` is an octopus merge for the Organization of Turkic States: cooperation between independent countries, not one state.

## Reading the dates

Git cannot store dates before 1970, so every commit's real historical year is in the subject line (`552 CE: ...`) and in a `Historical-Date:` trailer. The git timestamps are a scaled stand-in (one day per historical year, starting from 1970) that keeps the commits in the right order. "c." marks approximate dates.

## Try it

```
git log --graph --oneline --all
git log --oneline kipchak/kazakh
git log --merges --oneline --all
git tag -n1
```

## Caveats

This is a teaching metaphor. Peoples don't split as cleanly as branches: languages, dynasties and populations mixed constantly, and several origins here (Kazan Tatars, Kyrgyz, Gagauz) are still debated. The branches follow linguistic classification, not genetics or politics.
