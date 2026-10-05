#!/usr/bin/env python3
"""Build the Goldfib Capital blog.

    python3 tools/build.py

Reads content/blog/*.md (YAML front matter + Markdown, with ```viz blocks for
charts) and writes blog/<slug>/index.html, blog/index.html, sitemap.xml,
feed.xml and llms.txt. Commit the generated files: GitHub Pages serves them as-is.
"""
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

import markdown
import yaml

sys.path.insert(0, str(Path(__file__).parent))
import thumbs  # noqa: E402
import viz  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "blog"
SITE = "https://goldfibcapital.in"
EMAIL = "partners@goldfibcapital.in"
AUTHOR = {"@type": "Organization", "name": "Goldfib Capital Research", "url": f"{SITE}/"}

CLUSTERS = {
    "research": ("Institutional Research, Decoded",
                 "How buy-side-quality research on Indian companies is actually built: standards, sources, signals and valuation."),
    "automation": ("Research Automation",
                   "Where software and AI take the grunt work out of research, and where analyst judgement still has to do the job."),
    "family-office": ("Family Office Playbook",
                      "How Indian family offices organise research, write investment memos and evaluate managers and deals."),
    "investor-tax": ("Investor Tax & Accounts",
                     "Capital gains, ESOPs, AIS and demat mechanics for Indian investors: the paperwork behind every portfolio."),
    "markets": ("Markets & Macro, Explained",
                "Recessions, GDP, inflation, bear markets and volatility, explained with Indian data and what they mean for portfolios."),
    "talent": ("The Student Research Model",
               "Why student-led desks work, how quality is controlled, and the skills that make an analyst useful on day one."),
}

LEVELS = {"beginner": "Beginner", "intermediate": "Intermediate", "advanced": "Advanced"}
SCRIPTS = '<script src="/assets/site.js" defer></script>\n<script src="/assets/mail.js" defer></script>\n<script src="/assets/walkthrough.js?v=ebook1" defer></script>\n'
WT_URL = "/blog/walkthrough/"
CTA_TEXT = "See how automation helps your institutional research"
HI_TEXT = "Say hi to Goldfib Capital"
CTA_BTN = f'<a class="btn" href="{WT_URL}" data-walkthrough-open>{CTA_TEXT} →</a>'

esc = html.escape


def level(a):
    lv = a.get("level", "intermediate")
    return f'<span class="level level-{lv}">{LEVELS[lv]}</span>'


def load(path):
    raw = path.read_text()
    _, fm, body = raw.split("---", 2)
    meta = yaml.safe_load(fm)
    meta["body"] = body
    meta["date"] = str(meta["date"])
    return meta


def render_body(md):
    blocks = []

    def take(m):
        blocks.append(viz.render(yaml.safe_load(m.group(1))))
        return f"\n\nVIZBLOCK{len(blocks) - 1}\n\n"

    md = re.sub(r"^```viz\n(.*?)^```\s*$", take, md, flags=re.S | re.M)
    md = re.sub(r"^:::\s*(\w+)\s*(.*?)\n(.*?)^:::\s*$",
                lambda m: f'<div class="callout {m.group(1)}" markdown="1">\n'
                          + (f'<div class="callout-title">{esc(m.group(2))}</div>\n' if m.group(2) else "")
                          + f"\n{m.group(3)}\n</div>",
                md, flags=re.S | re.M)
    out = markdown.markdown(md, extensions=["tables", "toc", "md_in_html", "attr_list", "sane_lists", "smarty"])
    out = re.sub(r"<p>VIZBLOCK(\d+)</p>", lambda m: blocks[int(m.group(1))], out)
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return out


def mailto(subject, body=""):
    q = f"subject={quote(subject)}"
    if body:
        q += f"&body={quote(body)}"
    return f"mailto:{EMAIL}?{q}"


def cta_box(a, end=False):
    c = a.get("cta", {})
    head = c.get("heading", "Want this done for your portfolio?")
    text = c.get("body", "Goldfib builds institutional-grade research and automation for family offices and investment teams at a fraction of the cost of an in-house desk.")
    subj = c.get("subject", f"Research enquiry: {a['title']}")
    body = f"Hi Goldfib team,\n\nI read \"{a['title']}\" and would like to talk about:\n\n- \n\nName / organisation:\n"
    cls = "cta cta-end" if end else "cta"
    return (f'<aside class="{cls}"><span class="eyebrow">{"Work with Goldfib" if end else "Talk to us"}</span>'
            f'<h3>{esc(head)}</h3><p>{esc(text)}</p>'
            f'<div class="cta-row">{CTA_BTN}<a class="btn ghost" href="{esc(mailto(subj, body))}">{HI_TEXT} →</a>'
            f'<span class="cta-note">A real person replies within one working day. No sales sequence.</span></div></aside>')


NAV = ('<header class="nav"><div class="nav-inner"><a class="brand" href="/"><img src="/assets/logo.svg" alt="" width="30" height="30">Goldfib <span>Capital</span></a>'
       '<ul class="nav-links"><li><a href="/#offering">Offering</a></li><li><a href="/#process">Process</a></li><li><a href="/blog/">Research</a></li></ul>'
       f'<a class="btn nav-cta" href="{WT_URL}" data-walkthrough-open><span class="long">{CTA_TEXT}</span><span class="short">See how automation helps</span> →</a>'
       '<button class="nav-toggle" aria-label="Menu" aria-expanded="false">&#9776;</button></div></header>')

FOOT = ('<footer><div class="container"><div class="foot"><a class="brand" href="/"><img src="/assets/logo.svg" alt="" width="30" height="30">Goldfib <span>Capital</span></a>'
        f'<nav><a href="/#offering">Offering</a><a href="/blog/">Research</a><a href="/feed.xml">RSS</a><a href="mailto:{EMAIL}">Contact</a></nav><span>© 2026 Goldfib Capital</span></div>'
        '<p class="disclaimer"><b>Disclaimer:</b> Goldfib Capital provides information and insights for educational purposes only. We are not registered with SEBI as an investment advisor, research analyst, portfolio manager, or any other regulated entity. Nothing here is investment advice or a recommendation to buy, sell or hold any financial instrument. Figures marked illustrative are worked examples, not forecasts. Regulations and tax rules change; verify current rules with the regulator or a qualified professional before acting.</p>'
        '</div></footer>')


def head(title, desc, url, extra="", og_type="article"):
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Goldfib Capital">
<meta property="og:locale" content="en_IN">
<meta property="og:image" content="{SITE}/assets/logo.svg">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="Goldfib Capital Research" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/article.css">
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
        c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "x1wdvvovcj");
</script>
{extra}</head>"""


def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>\n'


def human_date(d):
    return dt.date.fromisoformat(d).strftime("%-d %b %Y")


def build_article(a, all_articles):
    url = f"{SITE}/blog/{a['slug']}/"
    body = render_body(a["body"])
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    a["minutes"] = max(4, round(words / 220))
    h2s = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)

    # mid-article CTA: explicit marker, else before the middle H2
    if "<p>CTA</p>" in body:
        body = body.replace("<p>CTA</p>", cta_box(a), 1)
    elif len(h2s) >= 3:
        mid = h2s[len(h2s) // 2][0]
        body = body.replace(f'<h2 id="{mid}">', cta_box(a) + f'<h2 id="{mid}">', 1)

    toc = "".join(f'<li><a href="#{i}"><span>{n:02d}</span>{re.sub("<[^>]+>", "", t)}</a></li>' for n, (i, t) in enumerate(h2s, 1))
    faq_html = "".join(f'<details><summary>{esc(f["q"])}</summary><p>{esc(f["a"])}</p></details>' for f in a.get("faq", []))
    takeaways = "".join(f"<li>{esc(t)}</li>" for t in a.get("takeaways", []))
    cname = CLUSTERS[a["cluster"]][0]

    same = [x for x in all_articles if x["cluster"] == a["cluster"] and x["slug"] != a["slug"]]
    same.sort(key=lambda x: (not x.get("pillar"), x["title"]))
    others = [x for x in all_articles if x["cluster"] != a["cluster"] and x.get("pillar")]
    related = (same[:3] + others)[:5]
    rel_html = "".join(f'<a class="rel" href="/blog/{r["slug"]}/"><span class="eyebrow">{esc(CLUSTERS[r["cluster"]][0])}</span>'
                       f'<b>{esc(r["title"])}</b><span class="muted">{esc(r["description"][:110])}…</span></a>' for r in related)

    schema = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["description"],
         "datePublished": a["date"], "dateModified": a.get("updated", a["date"]), "author": AUTHOR,
         "publisher": {"@type": "Organization", "name": "Goldfib Capital", "url": f"{SITE}/", "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo.svg"}},
         "mainEntityOfPage": url, "keywords": ", ".join(a.get("keywords", [])), "articleSection": cname,
         "about": a.get("keywords", [])[:3], "inLanguage": "en-IN", "wordCount": words,
         "isPartOf": {"@type": "Blog", "name": "Goldfib Capital Research", "url": f"{SITE}/blog/"}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Research", "item": f"{SITE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
    ]
    if a.get("faq"):
        schema.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in a["faq"]]})

    widgets = '<script src="/assets/widgets.js" defer></script>\n' if "data-widget=" in body else ""
    page = head(a.get("seo_title", a["title"]), a["description"], url,
                extra="".join(ld(s) for s in schema) + f'<meta property="article:published_time" content="{a["date"]}">\n' + widgets + SCRIPTS)
    page += f"""
<body>
<div class="progress" id="progress"></div>
{NAV}
<main>
<header class="art-head"><div class="container narrow">
  <nav class="crumbs" aria-label="breadcrumb"><a href="/">Goldfib</a><span>/</span><a href="/blog/">Research</a><span>/</span><a href="/blog/#{a['cluster']}">{esc(cname)}</a></nav>
  <div class="meta-row">{level(a)}<span class="tag">{esc(cname)}</span>{'<span class="tag ghost">Pillar guide</span>' if a.get('pillar') else ''}<span>{a['minutes']} min read</span><span>{human_date(a['date'])}</span></div>
  <h1>{esc(a['title'])}</h1>
  <p class="dek">{esc(a.get('dek', a['description']))}</p>
  <div class="answer"><span class="eyebrow">Short answer</span><p>{esc(a['answer'])}</p></div>
</div></header>
<div class="container layout">
  <aside class="toc"><div class="toc-inner"><p class="eyebrow">Contents</p><ol>{toc}</ol>
  <a class="btn ghost small" href="{esc(mailto(a.get('cta', {}).get('subject', 'Research enquiry: ' + a['title'])))}">{HI_TEXT} →</a>
  <a class="toc-wt" href="{WT_URL}" data-walkthrough-open><span class="eyebrow">&#9733; 5-step walkthrough</span>{CTA_TEXT} →</a></div></aside>
  <article class="prose">
    {f'<div class="takeaways"><p class="eyebrow">Key takeaways</p><ul>{takeaways}</ul></div>' if takeaways else ''}
    {body}
    {f'<section class="faq" id="faq"><h2>Frequently asked questions</h2>{faq_html}</section>' if faq_html else ''}
    {cta_box(a, end=True)}
    <section class="related"><h2>Keep reading</h2><div class="rel-grid">{rel_html}</div></section>
  </article>
</div>
</main>
{FOOT}
</body>
</html>
"""
    out = ROOT / "blog" / a["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return words


def build_index(arts):
    url = f"{SITE}/blog/"
    present = [k for k in CLUSTERS if any(x["cluster"] == k for x in arts)]

    def card(x, n, cls="card"):
        k = x["cluster"]
        words = " ".join([x["title"], x["description"], x.get("short", ""), CLUSTERS[k][0], " ".join(x.get("keywords", []) or [])])
        return (f'<a class="{cls}" href="/blog/{x["slug"]}/" data-cluster="{k}" data-level="{x.get("level", "intermediate")}" data-search="{esc(words.lower())}">'
                f'<div class="thumb">{thumbs.thumb(x["slug"], f"{cls[0]}{n}")}</div>'
                f'<div class="card-body"><span class="eyebrow">{esc(CLUSTERS[k][0])}</span><h3>{esc(x["title"])}</h3>'
                + ('' if cls == "start" else f'<p>{esc(x["description"])}</p><span class="card-meta">{level(x)}<span>{x["minutes"]} min read</span></span>')
                + '</div></a>')

    sections, n = "", 0
    for k in present:
        name, blurb = CLUSTERS[k]
        items = sorted([x for x in arts if x["cluster"] == k], key=lambda x: (not x.get("pillar"), ["beginner", "intermediate", "advanced"].index(x.get("level", "intermediate")), x["title"]))
        cards = ""
        for x in items:
            n += 1
            cards += card(x, n)
        sections += (f'<section class="cluster" id="{k}"><div class="cluster-head"><h2>{esc(name)}</h2>'
                     f'<p>{esc(blurb)} <span class="count">{len(items)} articles</span></p></div><div class="card-grid">{cards}</div></section>')

    by_slug = {a["slug"]: a for a in arts}
    starters = [by_slug[s] for s in ("institutional-grade-equity-research-india", "research-desk-cost-india") if s in by_slug]
    start_cards = (f'<a class="start special" href="{WT_URL}" data-walkthrough-open><div class="thumb">{thumbs.walkthrough("sw")}</div>'
                   f'<div class="card-body"><span class="eyebrow">&#9733; 5-step walkthrough</span><h3>{CTA_TEXT}</h3></div></a>'
                   + "".join(card(x, i, "start") for i, x in enumerate(starters)))

    schema = {"@context": "https://schema.org", "@type": "Blog", "name": "Goldfib Capital Research", "url": url,
              "description": "Research guides on Indian equities, research automation and family office investing.",
              "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{SITE}/blog/{a['slug']}/", "datePublished": a["date"]} for a in arts]}
    page = head("Research · Goldfib Capital", "Guides on institutional-grade equity research in India, research automation, family office investing and the student research model.", url, extra=ld(schema) + SCRIPTS, og_type="website")
    pills = ('<div class="pills" role="toolbar" aria-label="Filter by topic"><button class="pill on" data-filter="all" aria-pressed="true">All topics<span>' + str(len(arts)) + '</span></button>'
             + "".join(f'<button class="pill" data-filter="{k}" aria-pressed="false">{esc(CLUSTERS[k][0])}<span>{sum(x["cluster"] == k for x in arts)}</span></button>' for k in present)
             + f'<a class="pill special" href="{WT_URL}" data-walkthrough-open>&#9733; 5-step walkthrough</a></div>')
    levels = ('<div class="levels" role="toolbar" aria-label="Filter by level"><button class="lv on" data-level="all">All levels</button>'
              + "".join(f'<button class="lv" data-level="{k}">{v}</button>' for k, v in LEVELS.items()) + '</div>')
    page += f"""
<body class="library">
{NAV}
<main>
<header class="lib-head"><div class="container">
  <h1>Goldfib <em>Research</em></h1>
  <p class="dek">Deeply researched guides on institutional-grade equity research in India, research automation, family office investing and the student research model, organised from Beginner to Advanced. Search for a question, or pick a topic and start at the top.</p>
  <div class="cta-row center">{CTA_BTN}<a class="btn ghost" href="{mailto('Hello from the Goldfib research library')}">{HI_TEXT}</a></div>
  <label class="search"><span class="sr">Search the guides</span><input type="search" id="lib-q" placeholder="Search {len(arts)} guides: try &ldquo;DCF&rdquo;, &ldquo;promoter pledge&rdquo;, &ldquo;PMS&rdquo;" autocomplete="off"></label>
  <p class="start-label">New here? Start with</p>
  <div class="start-grid">{start_cards}</div>
  {pills}
  {levels}
</div></header>
<div class="container">
  {sections}
  <p class="no-results" hidden>No guide matches that yet. <a href="{mailto('Research question')}">Ask us the question</a> and we may write it next.</p>
  <aside class="cta cta-end"><span class="eyebrow">Work with Goldfib</span><h3>Need research done, not just read about?</h3><p>We build investment theses, initiation-style equity research and research automation for family offices, at a fraction of the cost of an in-house desk.</p><div class="cta-row">{CTA_BTN}<a class="btn ghost" href="{mailto('Family Office Partnership')}">{HI_TEXT} →</a></div></aside>
</div>
</main>
{FOOT}
</body>
</html>
"""
    (ROOT / "blog" / "index.html").write_text(page)


def build_walkthrough():
    url = f"{SITE}{WT_URL}"
    title = "See how automation helps your institutional research: a 5-step study"
    desc = "Interactive 5-step walkthrough: price an in-house equity research desk for your Indian coverage list and see what automation does to cost per report."
    faq = [
        ("How much does an in-house equity research desk cost in India?",
         "Using the illustrative defaults in this walkthrough, a two-analyst desk costs about ₹81 lakh a year once data seats, overheads and senior review are included. Salaries are only around 54% of that. At 24 full reports a year, that is roughly ₹3.4 lakh per report."),
        ("How does automation change the cost per report?",
         "Automation mostly removes mechanical work: collecting filings, extracting tables and updating models. In the illustrative model, analysis time rises from 8 to 20 hours a week, so each analyst completes about twice as many reports and the cost per report falls even after adding tooling costs."),
        ("Are the walkthrough numbers a quote?",
         "No. They are illustrative assumptions drawn from Goldfib's research desk cost and automation guides. Replace them with your own salary, data and output figures. Email partners@goldfibcapital.in for a scoped plan."),
    ]
    steps = [("01", "Your coverage", "Choose how many companies and where they sit: large caps, small and mid caps, or unlisted."),
             ("02", "The in-house desk", "Analysts needed at about 12 full reports each, with data, overheads and senior review added in."),
             ("03", "Where the hours go", "A 50-hour analyst week before and after automating collection, extraction and model updates."),
             ("04", "Cost per report", "Manual and automated desks plotted across coverage sizes, with your list marked."),
             ("05", "Your research plan", "Initiations, quarterly notes and governance checks for a year, sent to us as a plan.")]
    schema = [{"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "url": url, "inLanguage": "en-IN",
               "isPartOf": {"@type": "Blog", "name": "Goldfib Capital Research", "url": f"{SITE}/blog/"}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                  {"@type": "ListItem", "position": 2, "name": "Research", "item": f"{SITE}/blog/"},
                  {"@type": "ListItem", "position": 3, "name": "5-step walkthrough", "item": url}]},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                  {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    page = head(title, desc, url, extra="".join(ld(x) for x in schema) + SCRIPTS, og_type="website")
    page += f"""
<body>
<div class="progress" id="progress"></div>
{NAV}
<main>
<header class="art-head"><div class="container narrow">
  <nav class="crumbs" aria-label="breadcrumb"><a href="/">Goldfib</a><span>/</span><a href="/blog/">Research</a><span>/</span><span>Walkthrough</span></nav>
  <div class="meta-row"><span class="level level-beginner">Beginner</span><span class="tag">Interactive guide</span><span>5 steps · 3 min</span></div>
  <h1>See how automation helps your institutional research</h1>
  <p class="dek">A 5-step study on your own coverage list. We cost the in-house desk, show where analyst hours go, and what automating the mechanical work does to cost per report.</p>
  <div class="answer"><span class="eyebrow">Short answer</span><p>{esc(faq[0][1])}</p></div>
  <div class="wt-page" data-walkthrough-inline></div>
</div></header>
<div class="container narrow">
  <article class="prose">
    <h2 id="study">The study behind the walkthrough</h2>
    <p>We modelled one analyst's 50-hour week covering Indian listed companies and split it into six tasks: collecting filings and extracting tables, updating models, reading, analysis and thesis work, writing, and verification. We then built a desk around that week (salary, data seats, overheads and a senior reviewer's time) and costed it for a coverage list.</p>
    <p>Next we re-ran the same week with collection, extraction and model updates automated, and added an explicit verification step. Mechanical work falls from about 27 hours to 6, analysis time rises from 8 to 20 hours, and each analyst finishes about twice as many full reports a year (24 instead of 12). The walkthrough applies that result to the list you choose.</p>
    <p>It is a model built from stated assumptions, not a survey of firms. Every assumption is printed under the walkthrough so you can replace it with your own.</p>
    <h2 id="steps">What each step shows</h2>
    <div class="steps-explained">{"".join(f'<div><span class="eyebrow">Step {n}</span><b>{esc(t)}</b><p>{esc(x)}</p></div>' for n, t, x in steps)}</div>
    <p>The cost model follows <a href="/blog/research-desk-cost-india/">what a research desk really costs</a>, and the hours split follows <a href="/blog/ai-investment-research-automation-india/">AI and research automation: what works</a>. For where uncovered companies sit, see <a href="/blog/coverage-gap-indian-small-caps/">the small-cap coverage gap</a>.</p>
    <section class="faq" id="faq"><h2>Frequently asked questions</h2>{"".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq)}</section>
    {cta_box({"title": "5-step research walkthrough", "cta": {"subject": "Research plan enquiry"}}, end=True).replace(CTA_BTN, '')}
  </article>
</div>
</main>
{FOOT}
</body>
</html>
"""
    out = ROOT / "blog" / "walkthrough" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)


def build_feeds(arts):
    today = dt.date.today().isoformat()
    static = [("/", today), ("/about/", None), ("/blog/", today), (WT_URL, today)]
    urls = "".join(f"<url><loc>{SITE}{p}</loc>{f'<lastmod>{d}</lastmod>' if d else ''}</url>\n" for p, d in static)
    urls += "".join(f"<url><loc>{SITE}/blog/{a['slug']}/</loc><lastmod>{a.get('updated', a['date'])}</lastmod></url>\n" for a in arts)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

    rfc = lambda d: dt.datetime.fromisoformat(d).strftime("%a, %d %b %Y 00:00:00 +0530")
    items = "".join(f"<item><title>{esc(a['title'])}</title><link>{SITE}/blog/{a['slug']}/</link><guid>{SITE}/blog/{a['slug']}/</guid>"
                    f"<pubDate>{rfc(a['date'])}</pubDate><description>{esc(a['description'])}</description></item>\n" for a in arts)
    (ROOT / "feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Goldfib Capital Research</title>'
                                   f'<link>{SITE}/blog/</link><description>Institutional-grade research on Indian markets, automation and family office investing.</description><language>en-in</language>\n{items}</channel></rss>\n')

    lines = ["# Goldfib Capital", "",
             "> Goldfib Capital is a student-led research desk that delivers investment theses, institutional-grade equity research on Indian markets, "
             "and research automation to family offices at a fraction of the cost of an in-house team. Contact: " + EMAIL, ""]
    for k, (name, blurb) in CLUSTERS.items():
        if not any(a["cluster"] == k for a in arts):
            continue
        lines += [f"## {name}", ""]
        lines += [f"- [{a['title']}]({SITE}/blog/{a['slug']}/): {a['answer']}" for a in arts if a["cluster"] == k]
        lines.append("")
    lines += ["## Interactive", "", f"- [5-step research desk walkthrough]({SITE}{WT_URL}): Price an in-house equity research desk for an Indian coverage list and compare cost per report with an automated workflow.", ""]
    lines += ["## Company", "", f"- [Home]({SITE}/): Offering, process and founder", ""]
    (ROOT / "llms.txt").write_text("\n".join(lines))


def build_home(arts):
    """Refresh the research cards on the homepage between the research:start/end markers."""
    by_slug = {a["slug"]: a for a in arts}
    picks = [by_slug[s] for s in ("institutional-grade-equity-research-india", "research-desk-cost-india", "family-office-research-function-india") if s in by_slug]
    cards = "".join(f'<a class="rcard reveal" href="/blog/{a["slug"]}/"><div class="thumb">{thumbs.thumb(a["slug"], f"h{i}")}</div>'
                    f'<div class="b"><span class="eyebrow">{esc(CLUSTERS[a["cluster"]][0])}</span><h3>{esc(a["title"])}</h3></div></a>' for i, a in enumerate(picks))
    home = ROOT / "index.html"
    html_ = re.sub(r"<!-- research:start -->.*?<!-- research:end -->",
                   lambda m: f'<!-- research:start --><div class="rgrid">{cards}</div><!-- research:end -->', home.read_text(), flags=re.S)
    home.write_text(html_)


def main():
    arts = [load(p) for p in sorted(SRC.glob("*.md"))]
    slugs = [a["slug"] for a in arts]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    arts.sort(key=lambda a: (a["date"], a.get("order", 99)), reverse=True)
    for a in arts:
        w = build_article(a, arts)
        t = a.get("seo_title", a["title"])
        warn = []
        if len(t) > 62: warn.append(f"title {len(t)}c")
        if not 110 <= len(a["description"]) <= 160: warn.append(f"desc {len(a['description'])}c")
        if not 30 <= len(a["answer"].split()) <= 70: warn.append(f"answer {len(a['answer'].split())}w")
        print(f"  {a['slug']:<48} {w:>5} words {a['minutes']:>2} min  {' '.join(warn)}")
    build_index(arts)
    build_walkthrough()
    build_feeds(arts)
    build_home(arts)
    print(f"built {len(arts)} articles")


if __name__ == "__main__":
    main()
