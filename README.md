# turkic-git

The history of the Turkic peoples, told as a git repository.

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
