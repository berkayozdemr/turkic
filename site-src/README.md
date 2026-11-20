# Interactive site

`python3 build_site.py` writes `../index.html`, a single self-contained page (no build tools, no dependencies).

- `graph_gen.py` reuses `hero/gen.py` + `hero/data.py` (the researched hero image) and tags each drawn element with its branch.
- `content.py` holds the text per branch (self-name, where they live, brief, key dates, Wikipedia links) and the Wikimedia Commons images with author and licence.
- `template.html` is the page: click a branch, a name, an event or a chip to open the side panel. Deep links work: `index.html#tatar`.

Images are hotlinked from upload.wikimedia.org (allowed by Wikimedia), each shown with author, licence and a link to its file page.
This `gh-pages` branch holds only the website; GitHub Pages serves `index.html` from its root. The history itself lives on `main` and the other branches.
