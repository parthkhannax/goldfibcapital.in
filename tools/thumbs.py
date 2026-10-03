"""Small SVG card thumbnails for the research library index (Proflex-style chart motifs).

Each article gets a motif from THUMBS by slug; unknown slugs fall back to a line chart.
Thumbnails are decorative: aria-hidden, no data claims.
"""
GOLD, SUB, GRID = "#b8965a", "#8b919e", "rgba(255,255,255,.06)"
W, H = 320, 140


def _wrap(inner, uid):
    grid = "".join(f'<line x1="16" x2="{W - 16}" y1="{y}" y2="{y}" stroke="{GRID}"/>' for y in (30, 62, 94, 126))
    return (f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" font-family="JetBrains Mono,monospace">'
            f'<defs><linearGradient id="g{uid}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{GOLD}" stop-opacity=".28"/>'
            f'<stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></linearGradient></defs>{grid}{inner}</svg>')


def _t(x, y, s, c=SUB, anchor="start", size=8):
    return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}" letter-spacing=".08em" text-anchor="{anchor}">{s}</text>'


def bars(labels, hi=-1, heights=(70, 52, 84)):
    def f(u):
        n, s = len(labels), ""
        bw = 46 if n <= 3 else 34
        gap = (W - 60 - n * bw) / max(1, n - 1)
        for i, (lab, h) in enumerate(zip(labels, heights)):
            x = 30 + i * (bw + gap)
            on = i == (hi % n)
            s += f'<rect class="tb" x="{x:.0f}" y="{122 - h}" width="{bw}" height="{h}" rx="2" fill="{GOLD}" opacity="{1 if on else .45}"/>'
            s += _t(x + bw / 2, 134, lab, anchor="middle", size=7)
        return s + f'<line x1="16" x2="{W - 16}" y1="122" y2="122" stroke="rgba(255,255,255,.18)"/>'
    return f


def line(kind, labels=()):
    paths = {
        "rise": "M16,112 C80,108 120,100 170,80 S260,34 304,22",
        "decay": "M16,24 C70,60 110,92 170,104 S260,116 304,118",
        "kink": "M16,100 L150,100 L304,30",
        "wave": "M16,92 C50,60 80,110 120,78 S190,40 220,66 S280,40 304,30",
        "diverge": "M16,100 C90,80 180,58 304,26",
    }
    d = paths[kind]

    def f(u):
        s = f'<path d="{d} L304,126 L16,126 Z" fill="url(#g{u})"/>'
        if kind == "diverge":
            s += f'<path class="tl" d="M16,100 C90,92 180,80 304,64" fill="none" stroke="{SUB}" stroke-width="1.6" stroke-dasharray="4 4"/>'
        if kind == "kink":
            s += f'<path d="M16,100 L304,58" fill="none" stroke="{SUB}" stroke-width="1.2" stroke-dasharray="4 4"/><circle cx="150" cy="100" r="3.5" fill="#132338" stroke="{GOLD}" stroke-width="1.5"/>'
        s += f'<path class="tl" d="{d}" fill="none" stroke="{GOLD}" stroke-width="2.2"/>'
        for i, lab in enumerate(labels):
            s += _t(24 + i * (W - 48) / max(1, len(labels) - 1), 18, lab, GOLD if i == len(labels) - 1 else SUB,
                    anchor="start" if i == 0 else ("end" if i == len(labels) - 1 else "middle"))
        return s
    return f


def pipeline(labels):
    def f(u):
        n = len(labels)
        xs = [36 + i * (W - 72) / (n - 1) for i in range(n)]
        s = f'<line x1="{xs[0]}" x2="{xs[-1]}" y1="70" y2="70" stroke="rgba(184,150,90,.4)" stroke-width="1.5"/>'
        for i, (x, lab) in enumerate(zip(xs, labels)):
            last = i == n - 1
            s += f'<circle cx="{x:.0f}" cy="70" r="11" fill="#132338" stroke="{"#34d399" if last else GOLD}" stroke-width="1.6"/>'
            s += _t(x, 74, i + 1, "#34d399" if last else GOLD, "middle", 9) + _t(x, 102, lab, anchor="middle", size=7)
        s += f'<circle class="tdot" r="3" cy="70" cx="{xs[0]}" fill="{GOLD}"/>'
        return s
    return f


def doc(label, marks=(1, 4)):
    def f(u):
        s = f'<rect x="96" y="14" width="128" height="114" rx="6" fill="rgba(255,255,255,.03)" stroke="rgba(255,255,255,.14)"/>'
        for i in range(7):
            y, w = 32 + i * 13, (96, 104, 70, 100, 88, 60, 98)[i]
            hl = i in marks
            s += f'<rect x="110" y="{y}" width="{w}" height="5" rx="2.5" fill="{GOLD if hl else "rgba(255,255,255,.14)"}" opacity="{.9 if hl else 1}"/>'
            if hl:
                s += f'<circle cx="244" cy="{y + 2.5}" r="3" fill="{GOLD}"/><line x1="216" x2="240" y1="{y + 2.5}" y2="{y + 2.5}" stroke="{GOLD}" stroke-dasharray="2 3"/>'
        return s + _t(24, 20, label)
    return f


def donut(label, frac=.62, inner_frac=.4):
    import math

    def arc(f0, f1, r):
        a0, a1 = 2 * math.pi * f0 - math.pi / 2, 2 * math.pi * f1 - math.pi / 2
        x0, y0, x1, y1 = 160 + r * math.cos(a0), 70 + r * math.sin(a0), 160 + r * math.cos(a1), 70 + r * math.sin(a1)
        return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {1 if f1 - f0 > .5 else 0} 1 {x1:.1f},{y1:.1f}"

    def f(u):
        return (f'<circle cx="160" cy="70" r="44" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="14"/>'
                f'<path class="tl" d="{arc(0, frac, 44)}" fill="none" stroke="{GOLD}" stroke-width="14"/>'
                f'<path d="{arc(0, frac * inner_frac, 44)}" fill="none" stroke="#f87171" stroke-width="14" opacity=".85"/>'
                + _t(232, 56, "PROMOTER", GOLD) + _t(232, 70, "PLEDGED", "#f87171") + _t(232, 84, "PUBLIC") + _t(24, 20, label))
    return f


def funnel(labels):
    def f(u):
        s = ""
        for i, lab in enumerate(labels):
            w = 230 - i * 52
            x = (W - w) / 2
            s += f'<rect x="{x:.0f}" y="{18 + i * 28}" width="{w}" height="20" rx="3" fill="{GOLD}" opacity="{.3 + i * .22:.2f}"/>'
            s += _t(W / 2, 31 + i * 28, lab, "#0c1220" if i >= 2 else "#e8e4dc", "middle", 8)
        return s
    return f


def nodes(center, leaves):
    import math

    def f(u):
        s, n = "", len(leaves)
        for i, lab in enumerate(leaves):
            a = -math.pi / 2 + i * 2 * math.pi / n
            x, y = 160 + 104 * math.cos(a), 70 + 48 * math.sin(a)
            s += f'<line x1="160" y1="70" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(184,150,90,.35)"/>'
            s += f'<rect x="{x - 34:.0f}" y="{y - 9:.0f}" width="68" height="18" rx="9" fill="#132338" stroke="rgba(255,255,255,.18)"/>' + _t(x, y + 3, lab, anchor="middle", size=7)
        return s + f'<circle cx="160" cy="70" r="20" fill="{GOLD}"/>' + _t(160, 73, center, "#0c1220", "middle", 8)
    return f


def timeline(labels, band=(1, 2)):
    def f(u):
        n = len(labels)
        xs = [30 + i * (W - 60) / (n - 1) for i in range(n)]
        s = f'<rect x="{xs[band[0]]:.0f}" y="52" width="{xs[band[1]] - xs[band[0]]:.0f}" height="36" fill="rgba(248,113,113,.12)" stroke="rgba(248,113,113,.4)" stroke-dasharray="3 3"/>'
        s += _t((xs[band[0]] + xs[band[1]]) / 2, 46, "LOCK-IN", "#f87171", "middle")
        s += f'<line x1="{xs[0]}" x2="{xs[-1]}" y1="70" y2="70" stroke="{GOLD}" stroke-width="2"/>'
        for x, lab in zip(xs, labels):
            s += f'<circle cx="{x:.0f}" cy="70" r="4" fill="{GOLD}"/>' + _t(x, 106, lab, anchor="middle", size=7)
        return s
    return f


def ladder(labels):
    def f(u):
        s = ""
        for i, lab in enumerate(labels):
            x, y, w = 30 + i * 70, 108 - i * 24, 66
            s += f'<rect x="{x}" y="{y}" width="{w}" height="{126 - y}" rx="3" fill="{GOLD}" opacity="{.3 + i * .18:.2f}"/>' + _t(x + w / 2, y - 6, lab, GOLD if i == len(labels) - 1 else SUB, "middle", 7)
        return s
    return f


def checks(label, items):
    def f(u):
        s = _t(24, 20, label)
        for i, it in enumerate(items):
            y = 40 + i * 22
            s += (f'<rect x="60" y="{y - 9}" width="12" height="12" rx="3" fill="none" stroke="{GOLD}"/>'
                  f'<path d="M62.5,{y - 3} l3,3 l5,-6" fill="none" stroke="{GOLD}" stroke-width="1.6"/>'
                  + _t(84, y, it, "#d3d0c9", size=8)
                  + f'<rect x="210" y="{y - 6}" width="{40 + (i * 23) % 50}" height="5" rx="2.5" fill="rgba(255,255,255,.12)"/>')
        return s
    return f


THUMBS = {
    "institutional-grade-equity-research-india": checks("INSTITUTIONAL STANDARD", ["SOURCED", "MODELLED", "REVIEWED", "DISCLOSED"]),
    "reading-indian-annual-report-checklist": doc("ANNUAL REPORT", (1, 3, 5)),
    "dcf-valuation-indian-companies": line("kink", ("EXPLICIT", "FADE", "TERMINAL")),
    "earnings-call-transcript-analysis-india": line("wave", ("Q1", "Q2", "Q3", "TONE")),
    "promoter-pledging-shareholding-signals": donut("SHAREHOLDING"),
    "coverage-gap-indian-small-caps": bars(("LARGE", "MID", "SMALL", "MICRO"), 0, (96, 58, 22, 8)),
    "ai-investment-research-automation-india": bars(("MANUAL", "ASSISTED", "AUTOMATED"), 2, (40, 64, 92)),
    "nse-bse-filings-research-data-pipeline": pipeline(("FILINGS", "PARSE", "STORE", "MODEL", "ALERT")),
    "research-desk-cost-india": bars(("IN-HOUSE", "OUTSOURCED", "AUTOMATED"), 2, (96, 66, 34)),
    "student-led-equity-research-model": nodes("PM", ["ANALYST", "ANALYST", "REVIEW", "DATA", "MODEL"]),
    "family-office-research-function-india": nodes("CIO", ["MEMO", "DEALS", "MANAGERS", "MONITOR"]),
    "investment-memo-template-family-office": doc("ONE-PAGE MEMO", (0, 2, 6)),
    "pms-vs-aif-vs-direct-equity-india": line("diverge", ("DIRECT", "AFTER FEES")),
    "pre-ipo-unlisted-shares-due-diligence-india": timeline(("ENTRY", "IPO", "+6M", "EXIT")),
    "stock-screening-india-factor-models": funnel(("UNIVERSE 2,000+", "LIQUIDITY", "QUALITY", "SHORTLIST")),
    "equity-research-skills-students-india": ladder(("READ", "MODEL", "VALUE", "WRITE")),
}


def thumb(slug, uid):
    return _wrap(THUMBS.get(slug, line("rise"))(uid), uid)


def walkthrough(uid="wt"):
    """Thumbnail for the 5-step walkthrough card: cost per report, manual vs automated."""
    s = ""
    for i, h in enumerate((84, 58, 42, 32, 26)):
        s += f'<rect class="tb" x="{34 + i * 52}" y="{122 - h}" width="30" height="{h}" rx="2" fill="{GOLD}" opacity=".45"/>'
    s += f'<path class="tl" d="M30,30 C90,62 140,86 200,96 S280,104 300,106" fill="none" stroke="#e8e4dc" stroke-width="2"/>'
    s += f'<path class="tl" d="M30,62 C90,92 140,104 200,110 S280,114 300,115" fill="none" stroke="#34d399" stroke-width="2"/>'
    s += _t(24, 18, "COST PER REPORT") + _t(296, 18, "★ 5 STEPS", GOLD, "end")
    return _wrap(s, uid)
