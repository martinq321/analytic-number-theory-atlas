# Analytic Number Theory Atlas

A community reference in development, founded by Martin Belton. Searchable statements, conditional implications and research contribution forms.

## Run
Open index.html directly, or run `python3 -m http.server 8000`. No build or package installation is needed. Data is bundled; no runtime API is required.

## GitHub Pages
Upload all files at repository root. In Settings → Pages choose Deploy from a branch, main, /(root). Enable Issues. Set `repository` in config.js to your owner/repository if you change the name. All proposal links use that setting. GitHub account required to submit proposals. Forms prepare a draft and require a final user submission on GitHub; they do not silently publish.

## Data
4 classical nodes and 6 published implication records imported from the existing public RH atlas, 17 November 2026. `data/source-atlas.json` contains only four classical statements and public bibliographic sources. The broader research dataset is excluded. `data/atlas.js` is its browser wrapper. Original status labels are not a fresh independent audit. Community review starts pending. Review complete records and sources before relying on them.

After editing JSON, regenerate the wrapper: `python3 scripts/build_data.py`.
Run `python3 scripts/check.py` and `node --check app.js` before a release.

## Contributing
See CONTRIBUTING.md and the issue templates. Use issue status labels or a project board for submitted, under review, changes requested, accepted. Accepted changes require a reviewed commit; this static site has no backend or automatic moderation.

## Rights
Original sources retain their rights. No blanket licence is asserted over imported material. Before soliciting reusable third-party content, adopt explicit code/data licences and contribution terms with contributors. This initial repository provides attribution and source provenance.
