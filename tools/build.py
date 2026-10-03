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
    "talent": ("The Student Research Model",
               "Why student-led desks work, how quality is controlled, and the skills that make an analyst useful on day one."),
}

LEVELS = {"beginner": "Beginner", "intermediate": "Intermediate", "advanced": "Advanced"}
SCRIPTS = '<script src="/assets/site.js" defer></script>\n<script src="/assets/walkthrough.js" defer></script>\n'
WT_URL = "/blog/walkthrough/"

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
    wt = f'<a class="btn ghost" href="{WT_URL}" data-walkthrough-open>Try the 5-step walkthrough</a>' if end else ""
    return (f'<aside class="{cls}"><span class="eyebrow">{"Work with Goldfib" if end else "Talk to us"}</span>'
            f'<h3>{esc(head)}</h3><p>{esc(text)}</p>'
            f'<div class="cta-row"><a class="btn" href="{esc(mailto(subj, body))}">Email {EMAIL} →</a>{wt}'
            f'<span class="cta-note">A real person replies within one working day. No sales sequence.</span></div></aside>')


NAV = ('<header class="nav"><div class="nav-inner"><a class="brand" href="/"><img src="/assets/logo.svg" alt="" width="30" height="30">Goldfib <span>Capital</span></a>'
       '<ul class="nav-links"><li><a href="/#offering">Offering</a></li><li><a href="/#process">Process</a></li><li><a href="/blog/">Research</a></li></ul>'
       f'<a class="btn" href="{mailto("Family Office Partnership")}">Talk to us</a>'
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
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/article.css">
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
  <a class="btn ghost small" href="{esc(mailto(a.get('cta', {}).get('subject', 'Research enquiry: ' + a['title'])))}">Talk to us →</a>
  <a class="toc-wt" href="{WT_URL}" data-walkthrough-open><span class="eyebrow">Interactive</span>Price a research desk in 5 steps →</a></div></aside>
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
    root = {"label": "Goldfib Research", "children": [
        {"label": CLUSTERS[k][0], "href": f"#{k}", "children": [
            {"label": a["short"], "href": f"/blog/{a['slug']}/", "hl": a.get("pillar")}
            for a in sorted([x for x in arts if x["cluster"] == k], key=lambda x: not x.get("pillar"))]}
        for k in CLUSTERS if any(x["cluster"] == k for x in arts)]}
    tree = viz.tree({"type": "tree", "root": root, "node_width": 196, "col_gap": 40,
                     "caption": "Every article sits in one of four clusters. Gold-outlined nodes are the pillar guides. Click any node to open it."})
    sections = ""
    for k, (name, blurb) in CLUSTERS.items():
        items = sorted([x for x in arts if x["cluster"] == k], key=lambda x: (not x.get("pillar"), x["title"]))
        if not items:
            continue
        cards = "".join(f'<a class="rel{" pillar" if x.get("pillar") else ""}" href="/blog/{x["slug"]}/" data-category="{k}">'
                        f'<span class="rel-top">{level(x)}<span class="eyebrow">{"Pillar guide · " if x.get("pillar") else ""}{x["minutes"]} min</span></span>'
                        f'<b>{esc(x["title"])}</b><span class="muted">{esc(x["description"])}</span></a>' for x in items)
        sections += f'<section class="cluster" id="{k}"><h2>{esc(name)}</h2><p class="muted">{esc(blurb)}</p><div class="rel-grid">{cards}</div></section>'
    schema = {"@context": "https://schema.org", "@type": "Blog", "name": "Goldfib Capital Research", "url": url,
              "description": "Research guides on Indian equities, research automation and family office investing.",
              "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{SITE}/blog/{a['slug']}/", "datePublished": a["date"]} for a in arts]}
    page = head("Research · Goldfib Capital", "Guides on institutional-grade equity research in India, research automation, family office investing and the student research model.", url, extra=ld(schema) + SCRIPTS, og_type="website")
    present = [k for k in CLUSTERS if any(x["cluster"] == k for x in arts)]
    tabs = ('<div class="tabs" role="toolbar" aria-label="Filter by topic"><button class="tab on" data-filter="all" aria-pressed="true">All topics<span>' + str(len(arts)) + '</span></button>'
            + f'<a class="tab special" href="{WT_URL}" data-walkthrough-open>&#9733; 5-step walkthrough</a>'
            + "".join(f'<button class="tab" data-filter="{k}" aria-pressed="false">{esc(CLUSTERS[k][0])}<span>{sum(x["cluster"] == k for x in arts)}</span></button>' for k in present)
            + '</div>')
    page += f"""
<body>
{NAV}
<main>
<header class="art-head"><div class="container">
  <span class="eyebrow">Goldfib Research</span>
  <h1>Institutional-grade research, explained in the open.</h1>
  <p class="dek">{len(arts)} guides on how serious research on Indian markets gets done, how to automate the repetitive parts, and how family offices can get it without building a full desk.</p>
  <div class="cta-row"><a class="btn" href="{WT_URL}" data-walkthrough-open>Start the 5-step walkthrough →</a><a class="btn ghost" href="{mailto('Family Office Partnership')}">Talk to us</a><a class="btn ghost" href="#map">See the topic map</a></div>
</div></header>
<div class="container">
  {tabs}
  <div data-hide-filtered>{FEATURED}</div>
  <section id="map" class="map" data-hide-filtered><h2>Topic map</h2>{tree}</section>
  {sections}
  <aside class="cta cta-end"><span class="eyebrow">Work with Goldfib</span><h3>Need research done, not just read about?</h3><p>We build investment theses, initiation-style equity research and research automation for family offices, at a fraction of the cost of an in-house desk.</p><div class="cta-row"><a class="btn" href="{mailto('Family Office Partnership')}">Email {EMAIL} →</a></div></aside>
</div>
</main>
{FOOT}
</body>
</html>
"""
    (ROOT / "blog" / "index.html").write_text(page)


FEATURED = f"""<a class="featured" href="{WT_URL}" data-walkthrough-open="featured">
  <div class="f-copy"><span class="eyebrow">&#9733; Interactive guide · 5 steps · 3 min</span>
    <h2>Price a research desk for your coverage list</h2>
    <p>Pick how many Indian companies you want covered. The walkthrough builds the in-house desk, shows where analyst hours go, and what automation does to cost per report.</p>
    <ol><li><span>01</span>Your coverage list</li><li><span>02</span>The in-house desk, fully costed</li><li><span>03</span>Where the hours go</li><li><span>04</span>Cost per report, manual vs automated</li><li><span>05</span>Your research plan</li></ol>
    <span class="btn" style="align-self:flex-start">Start the walkthrough →</span></div>
  <div class="f-art" aria-hidden="true"><svg viewBox="0 0 360 240">
    <g fill="#b8965a" opacity=".85"><rect class="f-bar" x="24" y="70" width="34" height="140" rx="4" style="animation-delay:.1s"/><rect class="f-bar" x="70" y="118" width="34" height="92" rx="4" style="animation-delay:.25s"/><rect class="f-bar" x="116" y="150" width="34" height="60" rx="4" style="animation-delay:.4s"/><rect class="f-bar" x="162" y="168" width="34" height="42" rx="4" style="animation-delay:.55s"/><rect class="f-bar" x="208" y="178" width="34" height="32" rx="4" style="animation-delay:.7s"/></g>
    <path class="f-line" d="M24,60 C90,96 130,140 200,156 S300,176 340,180" fill="none" stroke="#e8e4dc" stroke-width="2.5"/>
    <path class="f-line" d="M24,110 C90,150 130,170 200,182 S300,192 340,194" fill="none" stroke="#34d399" stroke-width="2.5" style="animation-delay:.8s"/>
    <line x1="20" x2="344" y1="210" y2="210" stroke="rgba(255,255,255,.15)"/>
    <text x="24" y="34" fill="#8b919e" font-family="JetBrains Mono" font-size="11">COST PER REPORT, ₹ LAKH</text>
    <text x="340" y="232" fill="#8b919e" font-family="Outfit" font-size="11" text-anchor="end">companies covered →</text></svg></div>
</a>"""


def build_walkthrough():
    url = f"{SITE}{WT_URL}"
    title = "Research desk walkthrough: cost, hours and automation"
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
  <h1>What does institutional-grade research cost you? A 5-step walkthrough.</h1>
  <p class="dek">Pick a coverage list. We cost the in-house desk, show where analyst hours go, and what automating the mechanical work does to cost per report.</p>
  <div class="answer"><span class="eyebrow">Short answer</span><p>{esc(faq[0][1])}</p></div>
  <div class="wt-page" data-walkthrough-inline></div>
</div></header>
<div class="container narrow">
  <article class="prose">
    <h2 id="steps">What each step shows</h2>
    <div class="steps-explained">{"".join(f'<div><span class="eyebrow">Step {n}</span><b>{esc(t)}</b><p>{esc(x)}</p></div>' for n, t, x in steps)}</div>
    <p>The cost model follows <a href="/blog/research-desk-cost-india/">what a research desk really costs</a>, and the hours split follows <a href="/blog/ai-investment-research-automation-india/">AI and research automation: what works</a>. For where uncovered companies sit, see <a href="/blog/coverage-gap-indian-small-caps/">the small-cap coverage gap</a>.</p>
    <section class="faq" id="faq"><h2>Frequently asked questions</h2>{"".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq)}</section>
    {cta_box({"title": "5-step research walkthrough", "cta": {"subject": "Research plan enquiry"}}, end=True).replace(f'<a class="btn ghost" href="{WT_URL}" data-walkthrough-open>Try the 5-step walkthrough</a>', '')}
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
    print(f"built {len(arts)} articles")


if __name__ == "__main__":
    main()
