# goldfibcapital.in

Static site served by GitHub Pages.

## Blog

Articles live in `content/blog/*.md` (YAML front matter + Markdown). Charts are ```` ```viz ```` blocks rendered to inline SVG by `tools/viz.py`; interactive calculators live in `assets/widgets.js`.

To add or edit a post:

```
pip install markdown pyyaml
python3 tools/build.py
```

This regenerates `blog/<slug>/index.html`, `blog/index.html` (with the topic map), `sitemap.xml`, `feed.xml` and `llms.txt`. Commit the generated files.
