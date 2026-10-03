---
name: goldfib-article
description: Write and publish a Goldfib Capital research-library article (goldfibcapital.in/blog) in the house format — front matter, short answer, SVG viz blocks, mid-article "Talk to us" CTA, FAQ schema, internal links — then rebuild the archive, sitemap, feed and llms.txt. Use for any new or rewritten blog article on this site.
---

# Goldfib article generator

Every article is one Markdown file in `content/blog/<slug>.md`. `python3 tools/build.py` turns it into
`blog/<slug>/index.html` and regenerates `blog/index.html` (archive), the homepage research cards,
`sitemap.xml`, `feed.xml` and `llms.txt`. Never hand-edit generated HTML.

## 1. Pick the topic

- Read `content/blog/*.md` front matter first. No duplicate angles; each article must answer one
  question a buyer (family office CIO, investment team, analyst) actually types into Google or asks an AI.
- India-specific: SEBI, NSE/BSE, Indian filings, ₹ lakh/crore, Indian tax rules.
- Reference material (Proflex, Embark) sets the quality bar only. Never copy it; take a different angle.
- Assign one `cluster` from `CLUSTERS` in `tools/build.py` (`research`, `automation`, `family-office`,
  `talent`). Adding a cluster means editing `CLUSTERS` there.

## 2. Front matter (all fields required unless marked optional)

```yaml
---
slug: kebab-case-matching-filename
title: "Plain, specific headline"            # H1
seo_title: "≤60 chars, keyword first"
short: "≤45 char card label"
description: "≤160 chars meta description with the main keyword"
cluster: research | automation | family-office | talent
level: beginner | intermediate | advanced
order: 1                                      # tiebreak within a publish date
date: YYYY-MM-DD
pillar: true                                  # optional: one per cluster, the hub article
keywords: [6 to 8 real search phrases]
answer: "40–80 word direct answer. This is the AEO snippet; it must stand alone."
takeaways: ["3–5 one-sentence takeaways"]
faq:                                          # ≥3, phrased as real questions; becomes FAQPage schema
  - q: "..."
    a: "2–4 sentence answer"
cta:
  heading: "Question-form hook tied to this article's problem"
  body: "One or two sentences on what Goldfib would do for the reader here."
  subject: "Pre-filled email subject"
---
```

## 3. Body structure

1. Two or three short opening paragraphs that state the problem. No throat-clearing.
2. `##` sections (they build the TOC). 1,200–2,000 words total.
3. At least two ```` ```viz ```` blocks. Types (see `tools/viz.py`): `bars`, `columns`, `stacked`,
   `line`, `heatmap`, `tree`, `flow`, `funnel`, `quadrant`, `timeline`, `donut`, `radar`, `waterfall`,
   `stats`, `widget`. Use `widget` + `name:` for interactive calculators in `assets/widgets.js`
   (`desk-cost`, `dcf-explorer`, `fee-drag`); add a new `W['name']` there if the article needs one.
   Copy the spec shape from an existing article that uses the same type.
4. Every chart gets a `caption:`. Anything not from a cited source says "Illustrative" in the title or
   caption and states its assumptions. No raster images.
5. Callouts: `::: note Title`, `::: warn Title`, `::: example Title` … `:::`.
6. At least two internal links to other `/blog/<slug>/` articles, in running text.
7. The build inserts the mid-article "Talk to us" box (from `cta`) and the closing walkthrough CTA
   ("See how automation helps your institutional research" / "Say hi to Goldfib Capital"). Don't add
   your own CTA blocks.

## 4. Writing rules

- Short plain sentences. Concrete numbers, worked examples in ₹. No em-dash chains, no hype words.
- Regulatory and tax figures (SEBI minimums, lock-ins, capital gains rates) must be current; flag any
  you could not verify to the user.
- Byline is `AUTHOR` in `tools/build.py`; don't set it per article.

## 5. Build, check, publish

```
pip install markdown pyyaml
python3 tools/build.py
```

Then check:
- `blog/<slug>/index.html` exists and renders without console errors at 1280px and 390px, no
  horizontal scroll.
- No broken internal links (every `/blog/<slug>/` referenced exists).
- The article appears in `blog/index.html` under its cluster, and in `sitemap.xml` and `feed.xml`.
- `__pycache__/` is not staged.

Commit source `.md` plus all generated files to `main` and push; GitHub Pages deploys automatically.
