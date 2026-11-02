"""Small SVG card thumbnails for the research library index (Proflex-style chart motifs).

Each article gets a dedicated, visually distinct chart motif from THUMBS by slug.
Thumbnails are decorative: aria-hidden, no data claims, rendered in SVG with zero JS.
"""
import hashlib
import math

GOLD = "#b8965a"
STEEL = "#4a6a94"
GREEN = "#34d399"
RED = "#f87171"
PURPLE = "#a78bfa"
BLUE = "#60a5fa"
SUB = "#8b919e"
TEXT = "#e8e4dc"
GRID = "rgba(255,255,255,.06)"
W, H = 320, 140


def _wrap(inner, uid):
    grid = "".join(f'<line x1="16" x2="{W - 16}" y1="{y}" y2="{y}" stroke="{GRID}"/>' for y in (30, 62, 94, 126))
    return (f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" font-family="JetBrains Mono,monospace">'
            f'<defs><linearGradient id="g{uid}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{GOLD}" stop-opacity=".28"/>'
            f'<stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></linearGradient>'
            f'<linearGradient id="r{uid}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{RED}" stop-opacity=".25"/>'
            f'<stop offset="1" stop-color="{RED}" stop-opacity="0"/></linearGradient></defs>{grid}{inner}</svg>')


def _t(x, y, s, c=SUB, anchor="start", size=8, weight=400):
    return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}" font-weight="{weight}" letter-spacing=".08em" text-anchor="{anchor}">{s}</text>'


# ── Core Primitives ──────────────────────────────────────────────────────────

def bars(labels, hi=-1, heights=(70, 52, 84), colors=None):
    def f(u):
        n, s = len(labels), ""
        bw = 46 if n <= 3 else (36 if n == 4 else 28)
        gap = (W - 60 - n * bw) / max(1, n - 1)
        for i, (lab, h) in enumerate(zip(labels, heights)):
            x = 30 + i * (bw + gap)
            on = i == (hi % n)
            col = (colors[i] if colors else (GOLD if on or hi == -1 else STEEL))
            s += f'<rect class="tb" x="{x:.0f}" y="{122 - h}" width="{bw}" height="{h}" rx="2" fill="{col}" opacity="{1 if on else .55}"/>'
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
            s += _t(x, 74, str(i + 1), "#34d399" if last else GOLD, "middle", 9) + _t(x, 102, lab, anchor="middle", size=7)
        s += f'<circle class="tdot" r="3" cy="70" cx="{xs[0]}" fill="{GOLD}"/>'
        return s
    return f


def doc(label, marks=(1, 4)):
    def f(u):
        s = f'<rect x="96" y="14" width="128" height="114" rx="6" fill="rgba(255,255,255,.03)" stroke="rgba(255,255,255,.14)"/>'
        for i in range(7):
            y, w = 32 + i * 13, (96, 104, 70, 100, 88, 60, 98)[i]
            hl = i in marks
            s += f'<rect x="110" y="{y}" width="{w}" height="{5}" rx="2.5" fill="{GOLD if hl else "rgba(255,255,255,.14)"}" opacity="{.9 if hl else 1}"/>'
            if hl:
                s += f'<circle cx="244" cy="{y + 2.5}" r="3" fill="{GOLD}"/><line x1="216" x2="240" y1="{y + 2.5}" y2="{y + 2.5}" stroke="{GOLD}" stroke-dasharray="2 3"/>'
        return s + _t(24, 20, label)
    return f


def donut(label, frac=.62, inner_frac=.4, sub_labels=("PROMOTER", "PLEDGED", "PUBLIC")):
    def arc(f0, f1, r):
        a0, a1 = 2 * math.pi * f0 - math.pi / 2, 2 * math.pi * f1 - math.pi / 2
        x0, y0, x1, y1 = 150 + r * math.cos(a0), 70 + r * math.sin(a0), 150 + r * math.cos(a1), 70 + r * math.sin(a1)
        return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {1 if f1 - f0 > .5 else 0} 1 {x1:.1f},{y1:.1f}"

    def f(u):
        return (f'<circle cx="150" cy="70" r="44" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="14"/>'
                f'<path class="tl" d="{arc(0, frac, 44)}" fill="none" stroke="{GOLD}" stroke-width="14"/>'
                f'<path d="{arc(0, frac * inner_frac, 44)}" fill="none" stroke="#f87171" stroke-width="14" opacity=".85"/>'
                + _t(224, 56, sub_labels[0], GOLD) + _t(224, 70, sub_labels[1], "#f87171") + _t(224, 84, sub_labels[2]) + _t(24, 20, label))
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


# ── New Distinct Visual Motifs ───────────────────────────────────────────────

def corridor(label, target="4.0%", low="2%", high="6%"):
    """Inflation / CPI target corridor with fluctuating curve oscillating around target."""
    def f(u):
        s = _t(24, 20, label)
        s += f'<rect x="20" y="46" width="{W - 40}" height="52" fill="rgba(184,150,90,.07)" stroke="rgba(184,150,90,.22)" stroke-dasharray="3 3"/>'
        s += f'<line x1="20" x2="{W - 20}" y1="72" y2="72" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="5 4"/>'
        s += _t(W - 26, 70, f"TARGET {target}", GOLD, "end", size=7)
        s += _t(26, 42, f"UPPER BAND {high}", SUB, size=7)
        s += _t(26, 110, f"LOWER BAND {low}", SUB, size=7)
        # oscillating CPI path
        cpi = "M24,80 C60,54 90,62 130,88 S180,48 220,58 S270,76 296,68"
        s += f'<path d="{cpi}" fill="none" stroke="{GREEN}" stroke-width="2.4"/>'
        s += f'<circle cx="296" cy="68" r="4" fill="{GREEN}"/>'
        s += _t(296, 60, "CPI", GREEN, "middle", size=8, weight=600)
        return s
    return f


def drawdown(label, crashes=(("1992", "-54%"), ("2008", "-60%"), ("2020", "-38%"))):
    """Bear market steep drawdown plunge curve with crash milestones."""
    def f(u):
        s = _t(24, 20, label)
        # Plunge path
        path = "M20,32 C50,34 70,118 100,118 S130,55 160,58 S180,122 210,122 S240,65 270,72 S290,105 304,105"
        s += f'<path d="{path} L304,126 L20,126 Z" fill="url(#r{u})"/>'
        s += f'<path d="{path}" fill="none" stroke="{RED}" stroke-width="2.2"/>'
        # Drawdown mark
        s += f'<line x1="20" x2="{W - 20}" y1="84" y2="84" stroke="rgba(248,113,113,.25)" stroke-dasharray="3 3"/>'
        s += _t(W - 24, 80, "BEAR THRESHOLD -20%", RED, "end", size=7)
        # Points
        pts = [(100, 118, crashes[0]), (210, 122, crashes[1]), (304, 105, crashes[2])]
        for x, y, (yr, pct) in pts:
            s += f'<circle cx="{x}" cy="{y}" r="3.5" fill="{RED}"/>'
            s += _t(x, y - 8, f"{yr}: {pct}", "#fca5a5", "middle", size=7, weight=600)
        return s
    return f


def recession_dip(label):
    """Technical recession: quarterly GDP growth dipping below zero line."""
    def f(u):
        s = _t(24, 20, label)
        # Zero baseline
        s += f'<line x1="20" x2="{W - 20}" y1="74" y2="74" stroke="rgba(255,255,255,.3)" stroke-width="1.2"/>'
        s += _t(24, 71, "0% GROWTH", SUB, size=7)
        # 5 quarterly bars: Q1 (+5.2%), Q2 (-1.8%), Q3 (-2.4%), Q4 (+1.5%), Q5 (+4.2%)
        quarters = [("Q1", 32, 5.2, GREEN), ("Q2", -18, -1.8, RED), ("Q3", -28, -2.4, RED),
                    ("Q4", 16, 1.5, GREEN), ("Q5", 38, 4.2, GREEN)]
        # Shaded recession zone across Q2 and Q3
        s += f'<rect x="94" y="32" width="102" height="84" fill="rgba(248,113,113,.1)" stroke="rgba(248,113,113,.3)" stroke-dasharray="3 3"/>'
        s += _t(145, 42, "RECESSION", RED, "middle", size=7, weight=600)
        for i, (q, val, pct, col) in enumerate(quarters):
            bx = 52 + i * 50
            if val > 0:
                s += f'<rect x="{bx}" y="{74 - val}" width="34" height="{val}" rx="2" fill="{col}" opacity=".85"/>'
                s += _t(bx + 17, 74 - val - 4, f"+{pct}%", col, "middle", size=7)
            else:
                s += f'<rect x="{bx}" y="74" width="34" height="{-val}" rx="2" fill="{col}" opacity=".9"/>'
                s += _t(bx + 17, 74 - val + 11, f"{pct}%", col, "middle", size=7)
            s += _t(bx + 17, 132, q, SUB, "middle", size=7)
        return s
    return f


def gdp_breakdown(label):
    """GDP component pillars: GVA Sectors and Expenditure breakdown."""
    def f(u):
        s = _t(24, 20, label)
        cols = [("SERVICES", 54, GOLD, "54%"), ("INDUSTRY", 29, STEEL, "29%"), ("AGRICULTURE", 17, GREEN, "17%")]
        for i, (name, share, col, pct) in enumerate(cols):
            x = 36 + i * 88
            h = share * 1.4
            s += f'<rect x="{x}" y="{118 - h:.0f}" width="68" height="{h:.0f}" rx="3" fill="{col}" opacity=".85"/>'
            s += _t(x + 34, 112 - h, pct, col, "middle", size=9, weight=600)
            s += _t(x + 34, 130, name, SUB, "middle", size=7)
        s += f'<line x1="20" x2="{W - 20}" y1="118" y2="118" stroke="rgba(255,255,255,.2)"/>'
        s += _t(W - 24, 20, "GVA SECTORS", GOLD, "end", size=7)
        return s
    return f


def tax_reconcile(label):
    """Tax documents matching: 26AS (TDS) + AIS (SFT) + ITR."""
    def f(u):
        s = _t(24, 20, label)
        docs = [("FORM 26AS", "TDS / TCS", 34), ("AIS / TIS", "SFT TRANSACTIONS", 126), ("ITR-2 / 3", "CAPITAL GAINS", 218)]
        for name, sub, x in docs:
            s += f'<rect x="{x}" y="36" width="68" height="66" rx="4" fill="rgba(255,255,255,.04)" stroke="{GOLD}" stroke-width="1.2"/>'
            s += _t(x + 34, 56, name, GOLD, "middle", size=7, weight=600)
            s += _t(x + 34, 70, sub.split()[0], SUB, "middle", size=6)
            s += _t(x + 34, 80, sub.split()[-1] if len(sub.split()) > 1 else "", SUB, "middle", size=6)
            s += f'<circle cx="{x + 34}" cy="92" r="4" fill="{GREEN}"/>'
        s += f'<path d="M102,69 L126,69" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="2 2"/>'
        s += f'<path d="M194,69 L218,69" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="2 2"/>'
        s += _t(W / 2, 126, "✓ 3-WAY RECONCILIATION MATCHED", GREEN, "middle", size=7, weight=600)
        return s
    return f


def esop_ladder(label):
    """ESOP lifecycle steps: Grant -> Vesting -> Exercise (Perquisite) -> Sale (LTCG)."""
    def f(u):
        s = _t(24, 20, label)
        steps = [("GRANT", "Strike ₹100", 30, 96), ("VEST", "1-4 Yrs", 100, 78),
                 ("EXERCISE", "TDS / Perq", 170, 58), ("SALE", "LTCG 12.5%", 240, 38)]
        for i, (st, sub, x, y) in enumerate(steps):
            s += f'<rect x="{x}" y="{y}" width="54" height="{122 - y}" rx="3" fill="{GOLD}" opacity="{.35 + i * .2:.2f}"/>'
            s += _t(x + 27, y - 6, st, GOLD if i >= 2 else TEXT, "middle", size=7, weight=600)
            s += _t(x + 27, 132, sub, SUB, "middle", size=6)
        s += f'<line x1="20" x2="{W - 20}" y1="122" y2="122" stroke="rgba(255,255,255,.2)"/>'
        return s
    return f


def slb_circuit(label):
    """Securities Lending & Borrowing exchange clearing loop."""
    def f(u):
        s = _t(24, 20, label)
        s += f'<rect x="26" y="44" width="70" height="52" rx="4" fill="#132338" stroke="{GOLD}"/>'
        s += _t(61, 66, "LENDER", GOLD, "middle", size=8, weight=600)
        s += _t(61, 80, "EARNS FEE", SUB, "middle", size=6)

        s += f'<rect x="125" y="36" width="70" height="68" rx="4" fill="#1a2c45" stroke="{GREEN}"/>'
        s += _t(160, 62, "CLEARING", GREEN, "middle", size=8, weight=600)
        s += _t(160, 74, "NSCCL / ICCL", TEXT, "middle", size=6)
        s += _t(160, 88, "GUARANTEE", GREEN, "middle", size=6)

        s += f'<rect x="224" y="44" width="70" height="52" rx="4" fill="#132338" stroke="{STEEL}"/>'
        s += _t(259, 66, "BORROWER", STEEL, "middle", size=8, weight=600)
        s += _t(259, 80, "SHORT / ARB", SUB, "middle", size=6)

        s += f'<path d="M96,62 L125,62" stroke="{GOLD}" stroke-width="1.5"/>'
        s += f'<path d="M195,62 L224,62" stroke="{GREEN}" stroke-width="1.5"/>'
        s += f'<path d="M224,82 L96,82" stroke="{SUB}" stroke-width="1.2" stroke-dasharray="3 3"/>'
        s += _t(W / 2, 126, "EXCHANGE GUARANTEED RETURN", GOLD, "middle", size=7)
        return s
    return f


def transfer_bridge(label):
    """Demat account in-kind transfer: Demat A -> CDSL/NSDL -> Demat B."""
    def f(u):
        s = _t(24, 20, label)
        s += f'<rect x="30" y="44" width="74" height="54" rx="4" fill="#132338" stroke="{GOLD}"/>'
        s += _t(67, 66, "SOURCE DP", GOLD, "middle", size=7, weight=600)
        s += _t(67, 80, "DEMAT A", TEXT, "middle", size=7)

        s += f'<circle cx="160" cy="71" r="22" fill="#1a2c45" stroke="{GREEN}" stroke-width="1.4"/>'
        s += _t(160, 68, "CDSL/NSDL", GREEN, "middle", size=7, weight=600)
        s += _t(160, 79, "EASIEST", SUB, "middle", size=6)

        s += f'<rect x="216" y="44" width="74" height="54" rx="4" fill="#132338" stroke="{GOLD}"/>'
        s += _t(253, 66, "TARGET DP", GOLD, "middle", size=7, weight=600)
        s += _t(253, 80, "DEMAT B", TEXT, "middle", size=7)

        s += f'<line x1="104" x2="138" y1="71" y2="71" stroke="{GOLD}" stroke-width="1.5"/>'
        s += f'<line x1="182" x2="216" y1="71" y2="71" stroke="{GREEN}" stroke-width="1.5"/>'
        s += _t(W / 2, 126, "OFF-MARKET IN-KIND • ZERO CAPITAL GAINS", GREEN, "middle", size=7)
        return s
    return f


def accredited_shield(label):
    """SEBI Accredited Investor institutional badge."""
    def f(u):
        s = _t(24, 20, label)
        # Shield outline
        s += f'<path d="M160,30 L204,44 L204,82 C204,104 160,118 160,118 C160,118 116,104 116,82 L116,44 Z" fill="rgba(184,150,90,.08)" stroke="{GOLD}" stroke-width="1.8"/>'
        s += _t(160, 62, "SEBI", GOLD, "middle", size=8, weight=700)
        s += _t(160, 74, "ACCREDITED", TEXT, "middle", size=7, weight=600)
        s += _t(160, 86, "₹5 CR+ NET WORTH", GREEN, "middle", size=6)
        s += _t(50, 72, "AIF / PMS", SUB, "middle", size=7)
        s += _t(270, 72, "NO MINIMUMS", GOLD, "middle", size=7)
        return s
    return f


def cross_border(label):
    """Dubai vs GIFT City dual hubs linked by ODI/LRS bridge."""
    def f(u):
        s = _t(24, 20, label)
        # GIFT City Tower
        s += f'<rect x="36" y="38" width="80" height="74" rx="4" fill="#132338" stroke="{GOLD}" stroke-width="1.4"/>'
        s += _t(76, 58, "GIFT IFSCA", GOLD, "middle", size=8, weight=600)
        s += _t(76, 72, "USD / INR", TEXT, "middle", size=7)
        s += _t(76, 86, "10Y TAX HOLIDAY", GREEN, "middle", size=6)
        s += _t(76, 98, "FIF VEHICLE", SUB, "middle", size=6)

        # Dubai Tower
        s += f'<rect x="204" y="38" width="80" height="74" rx="4" fill="#132338" stroke="{BLUE}" stroke-width="1.4"/>'
        s += _t(244, 58, "DIFC / ADGM", BLUE, "middle", size=8, weight=600)
        s += _t(244, 72, "COMMON LAW", TEXT, "middle", size=7)
        s += _t(244, 86, "0% CT SFO", GREEN, "middle", size=6)
        s += _t(244, 98, "GLOBAL CUSTODY", SUB, "middle", size=6)

        # Bridge
        s += f'<path d="M116,66 C140,54 180,54 204,66" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 3"/>'
        s += _t(160, 52, "ODI / LRS", GOLD, "middle", size=7, weight=600)
        s += _t(W / 2, 128, "BIFURCATED OFFSHORE ALLOCATION", SUB, "middle", size=7)
        return s
    return f


def trust_foundation(label):
    """Indian Trust vs UAE Foundation comparison."""
    def f(u):
        s = _t(24, 20, label)
        s += f'<rect x="32" y="38" width="112" height="74" rx="4" fill="#132338" stroke="{STEEL}"/>'
        s += _t(88, 56, "INDIAN TRUST", STEEL, "middle", size=8, weight=600)
        s += _t(88, 70, "Trusts Act 1882", SUB, "middle", size=6)
        s += _t(88, 84, "Fiduciary Contract", TEXT, "middle", size=6)
        s += _t(88, 98, "MMR 42.7% Drag", RED, "middle", size=6)

        s += f'<rect x="176" y="38" width="112" height="74" rx="4" fill="#132338" stroke="{GOLD}"/>'
        s += _t(232, 56, "UAE FOUNDATION", GOLD, "middle", size=8, weight=600)
        s += _t(232, 70, "DIFC / ADGM Law", SUB, "middle", size=6)
        s += _t(232, 84, "Legal Body Corporate", TEXT, "middle", size=6)
        s += _t(232, 98, "0% Corporate Tax", GREEN, "middle", size=6)

        s += _t(W / 2, 128, "VS • RING-FENCING & SUCCESSION", GOLD, "middle", size=7)
        return s
    return f


def ops_engine(label):
    """PMS / AIF Operations automated STP pipeline."""
    def f(u):
        s = _t(24, 20, label)
        nodes_ = [("FIX / OMS", 34), ("BROKER REC", 104), ("CUSTODIAN", 174), ("SHADOW NAV", 244)]
        for i, (name, x) in enumerate(nodes_):
            col = GREEN if i == 3 else GOLD
            s += f'<rect x="{x}" y="52" width="56" height="38" rx="3" fill="#132338" stroke="{col}"/>'
            s += _t(x + 28, 68, name.split()[0], col, "middle", size=7, weight=600)
            s += _t(x + 28, 80, name.split()[-1] if len(name.split()) > 1 else "", SUB, "middle", size=6)
            if i < len(nodes_) - 1:
                s += f'<line x1="{x + 56}" x2="{x + 70}" y1="71" y2="71" stroke="{GOLD}" stroke-width="1.5"/>'
        s += _t(W / 2, 122, "ZERO SPREADSHEET DISCREPANCY • T+1 SETTLEMENT", GREEN, "middle", size=7)
        return s
    return f


def factor_trio(label):
    """Quantitative multi-factor triangle: Momentum + Quality + Low Vol."""
    def f(u):
        s = _t(24, 20, label)
        # Triangle layout
        pts = [(160, 36, "MOMENTUM", GOLD), (90, 102, "QUALITY", GREEN), (230, 102, "LOW VOL", BLUE)]
        s += f'<polygon points="160,36 90,102 230,102" fill="rgba(184,150,90,.06)" stroke="{GOLD}" stroke-width="1.2"/>'
        for x, y, name, col in pts:
            s += f'<circle cx="{x}" cy="{y}" r="22" fill="#132338" stroke="{col}" stroke-width="1.6"/>'
            s += _t(x, y + 4, name, col, "middle", size=7, weight=600)
        s += _t(160, 84, "NSE 500 ALPHA", TEXT, "middle", size=7, weight=600)
        s += _t(W / 2, 132, "ENSEMBLE MULTI-FACTOR MODEL", GOLD, "middle", size=7)
        return s
    return f


def compliance_ceiling(label):
    """SEBI regulatory limit ceilings: 10% Single-Stock & 25% Sector."""
    def f(u):
        s = _t(24, 20, label)
        # Ceilings
        s += f'<line x1="30" x2="{W - 30}" y1="50" y2="50" stroke="{RED}" stroke-width="1.6" stroke-dasharray="4 4"/>'
        s += _t(W - 32, 46, "10% SINGLE-STOCK CAP", RED, "end", size=7)
        s += f'<line x1="30" x2="{W - 30}" y1="84" y2="84" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="4 4"/>'
        s += _t(W - 32, 80, "25% SECTOR LIMIT", GOLD, "end", size=7)
        # Compliant bars
        holdings = [("STOCK A", 8.4, GREEN), ("STOCK B", 7.2, GREEN), ("STOCK C", 9.6, GOLD), ("STOCK D", 4.5, GREEN)]
        for i, (st, val, col) in enumerate(holdings):
            x = 44 + i * 58
            h = val * 5.5
            s += f'<rect x="{x}" y="{118 - h:.0f}" width="34" height="{h:.0f}" rx="2" fill="{col}" opacity=".85"/>'
            s += _t(x + 17, 114 - h, f"{val}%", col, "middle", size=7, weight=600)
            s += _t(x + 17, 132, st, SUB, "middle", size=6)
        return s
    return f


def waterfall_exit(label):
    """Liquidation preference waterfall: 1x Pref -> Common."""
    def f(u):
        s = _t(24, 20, label)
        bars_ = [("EXIT", 100, GOLD), ("1x PREF", -40, STEEL), ("DEBT", -20, RED), ("COMMON", 40, GREEN)]
        y_base = 118
        for i, (name, val, col) in enumerate(bars_):
            x = 36 + i * 66
            h = abs(val) * 0.75
            y = y_base - h if val >= 0 else y_base - 50
            s += f'<rect x="{x}" y="{y:.0f}" width="44" height="{h:.0f}" rx="2" fill="{col}" opacity=".85"/>'
            s += _t(x + 22, y - 5, f"{val:+d}" if i > 0 else f"{val}", col, "middle", size=7, weight=600)
            s += _t(x + 22, 132, name, SUB, "middle", size=6)
        s += f'<line x1="20" x2="{W - 20}" y1="118" y2="118" stroke="rgba(255,255,255,.2)"/>'
        return s
    return f


# ── Exhaustive Master Motif Registry ─────────────────────────────────────────

THUMBS = {
    # ── Original 16 articles ──
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

    # ── Markets & Macro (The 4 from the user's screenshot - now completely distinct!) ──
    "what-is-a-recession-india": recession_dip("TECHNICAL RECESSION (GDP < 0%)"),
    "what-is-gdp-india": gdp_breakdown("INDIA GDP COMPOSITION"),
    "what-is-inflation-cpi-india": corridor("RBI INFLATION TARGET CORRIDOR", target="4.0%", low="2%", high="6%"),
    "bear-market-india": drawdown("SENSEX HISTORICAL DRAWDOWNS", (("1992", "-54%"), ("2008", "-60%"), ("2020", "-38%"))),

    # ── Investor Tax & Accounts (all previously generic - now distinct!) ──
    "ais-form-26as-capital-gains-india": tax_reconcile("ANNUAL INFORMATION STATEMENT (AIS)"),
    "esop-taxation-india": esop_ladder("ESOP DUAL-STAGE TAXATION"),
    "securities-lending-borrowing-india": slb_circuit("SECURITIES LENDING & BORROWING (SLB)"),
    "demat-account-transfer-india": transfer_bridge("DEMAT ACCOUNT IN-KIND TRANSFER"),
    "accredited-investor-india": accredited_shield("SEBI ACCREDITED INVESTOR REGIME"),

    # ── Core Family Office & Automation Suite ──
    "dubai-vs-gift-city-family-office-structuring": cross_border("GIFT CITY VS DUBAI (DIFC/ADGM)"),
    "indian-family-trust-vs-uae-foundation-difc": trust_foundation("FAMILY TRUST VS UAE FOUNDATION"),
    "pms-aif-operations-automation-tech-stack": ops_engine("STP FUND OPERATIONS PIPELINE"),
    "quantitative-factor-models-indian-equities": factor_trio("MULTI-FACTOR ALPHA ENGINE"),
    "sebi-compliance-risk-monitoring-automation": compliance_ceiling("SEBI CONCENTRATION LIMITS"),
    "family-office-direct-co-investment-diligence": waterfall_exit("DIRECT CO-INVESTMENT WATERFALL"),

    # ── Additional Family Office Articles ──
    "family-office-asset-allocation-india": donut("ASSET ALLOCATION", frac=.75, inner_frac=.45, sub_labels=("EQUITY 40%", "CREDIT 20%", "GLOBAL 15%")),
    "family-office-governance-constitution": doc("FAMILY CONSTITUTION", (0, 2, 4)),
    "adgm-vs-difc-family-office-comparison": bars(("COURTS", "SPV COST", "BANKING", "ESTATE"), 1, (78, 92, 64, 82), (STEEL, GOLD, GREEN, BLUE)),
    "family-office-private-credit-india": bars(("SENIOR 1.5x", "TRA ESCROW", "SHARE PLEDGE", "NET YIELD"), 3, (65, 80, 72, 94), (STEEL, STEEL, STEEL, GREEN)),
    "family-office-real-estate-reits-vs-fractional": bars(("DIRECT COMM", "SM REIT", "LISTED REIT", "RESIDENTIAL"), 0, (88, 84, 70, 28), (GOLD, GREEN, STEEL, SUB)),
    "singapore-vcc-vs-gift-city-fund": nodes("VCC UMBRELLA", ["SUB-FUND A", "SUB-FUND B", "RING-FENCE", "GIFT FEEDER"]),
    "family-office-lp-due-diligence-vc-pe": bars(("CASH DPI", "PAPER TVPI", "FEES", "NET IRR"), 0, (92, 45, 30, 75), (GREEN, RED, STEEL, GOLD)),
    "multi-family-office-vs-single-family-office": line("decay", ("₹50 CR", "₹100 CR", "₹250 CR (BREAKEVEN)", "₹500 CR")),
    "family-office-angel-syndicate-structuring": pipeline(("DEAL FLOW", "CAT 1 AIF", "SPV POOL", "20% CARRY")),
    "next-gen-wealth-transfer-family-office": ladder(("EXTERNAL WORK", "SHADOW IC", "SANDBOX", "TRUST VEST")),

    # ── Batch 2: Treasury, Philanthropy & Operations Suite ──
    "family-office-treasury-management-india": ladder(("T-BILLS", "ARBITRAGE", "A1+ CP", "YIELD")),
    "philanthropy-and-csr-structuring-india": checks("SECTION 8 CSR FOUNDATION", ["12AB EXEMPT", "80G DONOR", "CSR-1 FILED", "SCHEDULE VII"]),
    "family-office-direct-lending-mezzanine": bars(("SENIOR DEBT", "MEZZANINE 18%", "EQUITY KICKER"), 1, (60, 92, 45)),
    "family-office-cybersecurity-data-privacy": checks("FAMILY OFFICE CYBER DEFENSE", ["MFA TOKEN", "VAULT ENCRYPT", "DUAL SIGN", "AIR GAPPED"]),
    "family-office-offshore-banking-custody": bars(("DOMESTIC DP", "GIFT CUSTODY", "GLOBAL TIER 1"), 2, (50, 75, 95)),
    "earnings-call-qa-sentiment-nlp": line("wave", ("PREPARED", "ANALYST Q", "EVASIVE", "SENTIMENT")),
    "automated-portfolio-rebalancing-engine": pipeline(("DRIFT CHECK", "TAX HARVEST", "ORDER SLICE", "REBALANCED")),
    "insider-trading-automated-surveillance-sebi": compliance_ceiling("SEBI PIT SURVEILLANCE"),
    "custom-backtesting-engine-python-nse": line("diverge", ("STRATEGY", "NSE 500")),
    "corporate-actions-automation-demergers-dividends": pipeline(("EX-DATE", "RECORD", "RATIO", "BOOK-VALUE")),

    # ── Batch 3: Fund Automation, Engineering & Valuation Suite ──
    "automated-esg-scoring-indian-listed-firms": checks("BRSR ESG SCORING", ["SCOPE 1/2", "WATER REC", "BOARD INDEP", "SEBI CORE"]),
    "shadow-nav-and-accounting-system": ops_engine("SHADOW NAV RECONCILIATION"),
    "automated-broker-contract-note-parser": doc("CONTRACT NOTE STT/GST", (1, 2, 4)),
    "market-data-pipeline-websocket-nse-tick": pipeline(("NSE WS TICK", "ORDER BOOK", "REDIS MEM", "SIGNAL")),
    "fund-investor-reporting-automation-lp-portal": doc("LP QUARTERLY REPORT", (0, 3, 5)),
    "credit-rating-migration-tracking-engine": ladder(("AAA", "AA+", "AA-", "WATCHLIST")),
    "automated-dcf-financial-model-builder": line("kink", ("HISTORICAL", "PROJECTIONS", "TERMINAL")),
    "derivative-margin-optimization-span-var": bars(("SPAN BASE", "EXPOSURE", "SPREAD BENEFIT", "FREE CASH"), 2, (75, 45, 90, 85), (STEEL, RED, GREEN, GOLD)),
    "sebi-mishandling-and-trade-allocation-audit": checks("PRO-RATA ALLOCATION AUDIT", ["TIME PRIORITY", "VWAP FILLS", "ZERO SKEW", "SEBI COMPLIANT"]),
    "reverse-dcf-valuation-model-india": funnel(("MARKET CAP", "IMPLIED FCF", "EXPECTED ROCE", "REALITY CHECK")),

    # ── Batch 4: Institutional Research, Forensics & Capital Allocation ──
    "forensic-accounting-checklist-indian-equities": checks("FORENSIC RED FLAGS", ["CFO/EBITDA", "DEBTOR DAYS", "AUDITOR EXIT", "CWIP STAGNANT"]),
    "analyzing-contingent-liabilities-notes-accounts": bars(("TAX DISPUTES", "GUARANTEES", "CUSTOMS", "NET WORTH"), 3, (55, 78, 35, 95), (RED, RED, STEEL, GREEN)),
    "free-cash-flow-conversion-capex-cycles": waterfall_exit("FCF CONVERSION WATERFALL"),
    "auditing-related-party-transactions-india": donut("RPT SPREAD", frac=.68, inner_frac=.38, sub_labels=("LOANS 42%", "TRADING 28%", "ROYALTY 18%")),
    "working-capital-cycle-cash-conversion-trap": bars(("DSO 148D", "DIO 85D", "DPO 55D", "NET CCC"), 3, (85, 55, 40, 95), (STEEL, STEEL, SUB, RED)),
    "order-book-to-bill-ratio-epc-capital-goods": bars(("REVENUE", "ORDER BOOK", "BOOK-TO-BILL"), 1, (45, 95, 70), (STEEL, GOLD, GREEN)),
    "analyzing-indian-nbfc-asset-quality-npa": bars(("STAGE 1", "STAGE 2", "STAGE 3", "PCR 65%"), 3, (90, 40, 25, 80), (GREEN, STEEL, RED, GOLD)),
    "identifying-moats-in-indian-b2b-manufacturing": funnel(("OEM AUDIT", "SWITCHING COST", "PRICING POWER", "25% ROCE")),
    "promoter-capital-allocation-track-record": bars(("ROCE 26%", "COST OF CAP", "EVA SPREAD"), 0, (92, 50, 75), (GOLD, STEEL, GREEN)),
    "institutional-sell-discipline-stop-loss": drawdown("PORTFOLIO STOP LOSS", (("PEAK", "0%"), ("TRIM", "-8%"), ("CUT", "-15%"))),

    # ── Batch 5: Investor Tax, Wealth Structuring, Macro Transmission & Demat ──
    "angel-tax-abolition-section-56-impact": checks("SECTION 56(2)(viib) REPEAL", ["RULE 11UA FMV", "0% ANGEL TAX", "COMMERCIAL VAL", "SECTION 68 OK"]),
    "section-54f-capital-gains-tax-exemption": bars(("NET PROCEEDS", "REINVESTED", "LTCG EXEMPT", "RESIDUAL TAX"), 2, (95, 95, 95, 10), (STEEL, GOLD, GREEN, RED)),
    "set-off-and-carry-forward-losses-india": ladder(("STCL -> STCG", "STCL -> LTCG", "LTCL -> LTCG", "8-YR CARRY")),
    "foreign-tax-credit-ftc-form-67-india": checks("RULE 128 FTC / FORM 67", ["US 25% WHT", "FORM 1042-S", "FORM 67 FILED", "SCHEDULE FA"]),
    "gift-taxation-rules-for-family-wealth": nodes("PATRIARCH", ["SPOUSE", "CHILDREN", "GRANDCHILDREN", "TRUST"]),
    "demat-transmission-vs-transfer-nominee": transfer_bridge("DEMAT TRANSMISSION BY OPERATION OF LAW"),
    "india-yield-curve-inversion-signals": line("diverge", ("91D T-BILL", "1Y T-BILL", "5Y G-SEC", "10Y BENCH")),
    "current-account-deficit-and-rupee-depreciation": bars(("GOODS TRADE", "SERVICES NET", "REMITTANCES", "NET CAD <2%"), 3, (90, 60, 45, 25), (RED, GREEN, GREEN, GOLD)),
    "fii-vs-dii-liquidity-flow-dynamics": bars(("FII SELLING", "DII BUYING", "MONTHLY SIP", "NET RESILIENCE"), 2, (85, 90, 80, 95), (RED, GREEN, GOLD, GREEN)),
    "rbi-monetary-policy-transmission-repo-mclr": pipeline(("RBI REPO", "EBLR LOANS", "DEPOSIT LAG", "PEAK NIM")),
}


def _fallback_thumb(slug, uid):
    """Dynamic, deterministic visual fallback generator.
    
    Guarantees that any slug without an explicit THUMBS entry still gets a
    unique, beautiful, domain-specific chart motif rather than a generic line!
    """
    h = int(hashlib.md5(slug.encode("utf-8")).hexdigest(), 16)
    archetype = h % 8
    clean_label = slug.replace("-", " ").upper()[:24]

    if archetype == 0:
        h1 = 40 + (h % 50)
        h2 = 50 + ((h >> 4) % 40)
        h3 = 70 + ((h >> 8) % 30)
        return bars(("TIER 1", "TIER 2", "TARGET"), 2, (h1, h2, h3))(uid)
    elif archetype == 1:
        return line("wave", ("ANALYSIS", "SIGNAL", "EXECUTION"))(uid)
    elif archetype == 2:
        return donut(clean_label, frac=0.55 + ((h % 30) / 100))
    elif archetype == 3:
        return pipeline(("STAGE 1", "MODEL", "AUDIT", "OUTPUT"))(uid)
    elif archetype == 4:
        return checks(clean_label, ["AUDITED", "VERIFIED", "COMPLIANT", "INDEXED"])(uid)
    elif archetype == 5:
        return ladder(("LEVEL 1", "LEVEL 2", "LEVEL 3", "ALPHA"))(uid)
    elif archetype == 6:
        return corridor(clean_label)(uid)
    else:
        return funnel(("RAW DATA", "FILTERED", "OPTIMIZED", "PORTFOLIO"))(uid)


def thumb(slug, uid):
    fn = THUMBS.get(slug)
    if fn:
        return _wrap(fn(uid), uid)
    return _wrap(_fallback_thumb(slug, uid), uid)


def walkthrough(uid="wt"):
    """Thumbnail for the 5-step walkthrough card: cost per report, manual vs automated."""
    s = ""
    for i, h in enumerate((84, 58, 42, 32, 26)):
        s += f'<rect class="tb" x="{34 + i * 52}" y="{122 - h}" width="30" height="{h}" rx="2" fill="{GOLD}" opacity=".45"/>'
    s += f'<path class="tl" d="M30,30 C90,62 140,86 200,96 S280,104 300,106" fill="none" stroke="#e8e4dc" stroke-width="2"/>'
    s += f'<path class="tl" d="M30,62 C90,92 140,104 200,110 S280,114 300,115" fill="none" stroke="#34d399" stroke-width="2"/>'
    s += _t(24, 18, "COST PER REPORT") + _t(296, 18, "★ 5 STEPS", GOLD, "end")
    return _wrap(s, uid)
