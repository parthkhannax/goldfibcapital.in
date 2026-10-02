"""Inline-SVG chart renderers for Goldfib articles.

Every renderer takes a spec dict (parsed from a ```viz block) and returns an
HTML string. Charts are plain SVG so crawlers and answer engines can read the
labels, and they need no JavaScript.
"""
import html
import json
import math

GOLD = "#b8965a"
STEEL = "#4a6a94"
PALETTE = ["#b8965a", "#60a5fa", "#34d399", "#f472b6", "#a78bfa", "#8b919e", "#fb923c"]
TEXT = "#e8e4dc"
SUB = "#8b919e"
MUTED = "#5f6878"
GRID = "rgba(255,255,255,.07)"
FONT = "Outfit, system-ui, sans-serif"
MONO = "JetBrains Mono, ui-monospace, monospace"


def esc(s):
    return html.escape(str(s), quote=True)


def wrap(text, width):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines or [""]


def fmt(v, spec):
    pre, unit, dp = spec.get("prefix", ""), spec.get("unit", ""), spec.get("decimals")
    if dp is None:
        dp = 0 if float(v).is_integer() else 1
    return f"{pre}{v:,.{dp}f}{unit}"


def nice_ticks(lo, hi, n=5):
    if hi == lo:
        hi = lo + 1
    raw = (hi - lo) / n
    mag = 10 ** math.floor(math.log10(raw))
    step = min((s * mag for s in (1, 2, 2.5, 5, 10) if s * mag >= raw), default=raw)
    start = math.floor(lo / step) * step
    ticks, t = [], start
    while t <= hi + step * 0.001:
        ticks.append(round(t, 10))
        t += step
    if ticks[-1] < hi:
        ticks.append(ticks[-1] + step)
    return ticks


def text(x, y, s, size=13, fill=TEXT, anchor="start", weight=400, font=FONT, extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" font-family="{font}"{extra}>{esc(s)}</text>')


def mtext(x, y, lines, size=13, lh=1.3, **kw):
    return "".join(text(x, y + i * size * lh, ln, size=size, **kw) for i, ln in enumerate(lines))


def figure(spec, svg, w, h, min_w=520):
    title = spec.get("title", "")
    cap = spec.get("caption", "")
    src = spec.get("source", "")
    head = f'<div class="viz-title">{esc(title)}</div>' if title else ""
    body = (f'<div class="viz-scroll"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{esc(title or cap)}" '
            f'style="min-width:{min_w}px">{f"<title>{esc(title)}</title>" if title else ""}{svg}</svg></div>')
    foot = ""
    if cap or src:
        foot = '<figcaption>' + esc(cap) + (f' <span class="viz-src">Source: {esc(src)}</span>' if src else "") + '</figcaption>'
    return f'<figure class="viz">{head}{body}{foot}</figure>'


# ── horizontal bars ──────────────────────────────────────────────────────────
def bars(spec):
    data = spec["data"]
    hl = set(spec.get("highlight", []))
    lw = spec.get("label_width", 210)
    W, row = 720, 40
    vmax = spec.get("max") or max(abs(d[1]) for d in data)
    plot = W - lw - 90
    out, y = [], 14
    for d in data:
        label, v = d[0], d[1]
        note = d[2] if len(d) > 2 else ""
        lines = wrap(label, int(lw / 7.4))
        bw = max(2, plot * abs(v) / vmax)
        col = GOLD if (label in hl or not hl) else STEEL
        out.append(mtext(lw - 12, y + 19 - (len(lines) - 1) * 7, lines, size=13, fill=TEXT if label in hl else SUB, anchor="end"))
        out.append(f'<rect x="{lw}" y="{y + 6}" width="{bw:.1f}" height="{row - 14}" rx="4" fill="{col}" opacity="{1 if col == GOLD else .85}"/>')
        out.append(text(lw + bw + 8, y + 24, fmt(v, spec), size=13, fill=TEXT, weight=600, font=MONO))
        if note:
            out.append(text(lw + bw + 8 + 9 * len(fmt(v, spec)), y + 24, note, size=11, fill=MUTED))
        y += row
    return figure(spec, "".join(out), W, y + 10)


# ── vertical columns ─────────────────────────────────────────────────────────
def columns(spec):
    data = spec["data"]
    hl = set(spec.get("highlight", []))
    W, H, L, B, T = 720, 340, 56, 54, 24
    vals = [d[1] for d in data]
    ticks = nice_ticks(min(0, min(vals)), max(vals))
    lo, hi = ticks[0], ticks[-1]
    ph = H - B - T
    y_of = lambda v: T + ph * (1 - (v - lo) / (hi - lo))
    out = []
    for t in ticks:
        out.append(f'<line x1="{L}" x2="{W - 10}" y1="{y_of(t):.1f}" y2="{y_of(t):.1f}" stroke="{GRID}"/>')
        out.append(text(L - 8, y_of(t) + 4, fmt(t, {**spec, "decimals": spec.get("tick_decimals", 0)}), size=11, fill=MUTED, anchor="end", font=MONO))
    slot = (W - L - 10) / len(data)
    bw = min(56, slot * 0.62)
    for i, d in enumerate(data):
        cx = L + slot * (i + .5)
        col = GOLD if (d[0] in hl or not hl) else STEEL
        y0, y1 = y_of(max(0, d[1])), y_of(min(0, d[1]))
        out.append(f'<rect x="{cx - bw / 2:.1f}" y="{y0:.1f}" width="{bw:.1f}" height="{max(1, y1 - y0):.1f}" rx="3" fill="{col}"/>')
        out.append(text(cx, y0 - 7, fmt(d[1], spec), size=12, anchor="middle", weight=600, font=MONO))
        out.append(mtext(cx, H - B + 20, wrap(d[0], max(6, int(slot / 7.5))), size=11.5, fill=SUB, anchor="middle"))
    return figure(spec, "".join(out), W, H)


# ── stacked horizontal bars ──────────────────────────────────────────────────
def stacked(spec):
    series, rows = spec["series"], spec["rows"]
    lw, W, row = spec.get("label_width", 190), 720, 46
    totals = [sum(r["values"]) for r in rows]
    vmax = max(totals)
    plot = W - lw - 100
    out, x = [], lw
    for i, s in enumerate(series):  # legend
        out.append(f'<rect x="{x}" y="6" width="11" height="11" rx="2" fill="{PALETTE[i % len(PALETTE)]}"/>')
        out.append(text(x + 16, 16, s, size=12, fill=SUB))
        x += 30 + len(s) * 6.8
    y = 34
    for r, tot in zip(rows, totals):
        lines = wrap(r["label"], int(lw / 7.4))
        out.append(mtext(lw - 12, y + 22 - (len(lines) - 1) * 7, lines, size=13, fill=TEXT, anchor="end"))
        x = lw
        for i, v in enumerate(r["values"]):
            w = plot * v / vmax
            out.append(f'<rect x="{x:.1f}" y="{y + 6}" width="{max(0, w - 1.5):.1f}" height="{row - 16}" fill="{PALETTE[i % len(PALETTE)]}"/>')
            if w > 44 and spec.get("segment_labels", True):
                out.append(text(x + w / 2, y + 26, fmt(v, spec), size=11, fill="#0c1220", anchor="middle", weight=600, font=MONO))
            x += w
        out.append(text(x + 8, y + 26, fmt(tot, spec), size=13, weight=700, font=MONO))
        y += row
    return figure(spec, "".join(out), W, y + 8)


# ── multi-series line ────────────────────────────────────────────────────────
def line(spec):
    xs, series = spec["x"], spec["series"]
    W, H, L, B, T, R = 720, 340, 60, 40, 40, 120
    allv = [v for s in series for v in s["values"] if v is not None]
    ticks = nice_ticks(min(spec.get("ymin", min(allv)), min(allv)), max(allv))
    lo, hi = ticks[0], ticks[-1]
    pw, ph = W - L - R, H - B - T
    x_of = lambda i: L + pw * i / (len(xs) - 1)
    y_of = lambda v: T + ph * (1 - (v - lo) / (hi - lo))
    out = []
    for t in ticks:
        out.append(f'<line x1="{L}" x2="{L + pw}" y1="{y_of(t):.1f}" y2="{y_of(t):.1f}" stroke="{GRID}"/>')
        out.append(text(L - 8, y_of(t) + 4, fmt(t, {**spec, "decimals": spec.get("tick_decimals", 0)}), size=11, fill=MUTED, anchor="end", font=MONO))
    step = max(1, len(xs) // 8)
    for i, xl in enumerate(xs):
        if i % step == 0 or i == len(xs) - 1:
            out.append(text(x_of(i), H - B + 20, xl, size=11, fill=SUB, anchor="middle", font=MONO))
    for si, s in enumerate(series):
        col = s.get("color") or PALETTE[si % len(PALETTE)]
        pts = [(x_of(i), y_of(v)) for i, v in enumerate(s["values"]) if v is not None]
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        dash = ' stroke-dasharray="6 5"' if s.get("dashed") else ""
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{3 if si == 0 else 2.2}"{dash} stroke-linejoin="round"/>')
        lx, ly = pts[-1]
        out.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="4" fill="{col}"/>')
        out.append(text(lx + 9, ly + 4, f'{s["name"]} {fmt(s["values"][-1], spec)}', size=12, fill=col, weight=600))
    return figure(spec, "".join(out), W, H)


# ── heatmap (supports a computed DCF sensitivity) ────────────────────────────
def _lerp(c1, c2, t):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


def heatmap(spec):
    if spec.get("compute") == "gordon":
        p = spec["params"]
        spec["rows"] = [f"{w}%" for w in p["wacc"]]
        spec["cols"] = [f"{g}%" for g in p["growth"]]
        spec["values"] = [[p["fcf"] * (1 + g / 100) / (w / 100 - g / 100) for g in p["growth"]] for w in p["wacc"]]
    rows, cols, vals = spec["rows"], spec["cols"], spec["values"]
    flat = [v for r in vals for v in r if v is not None]
    lo, hi = min(flat), max(flat)
    L, T, cw, ch = 120, 64, min(110, 560 / len(cols)), 44
    W = L + cw * len(cols) + 20
    H = T + ch * len(rows) + 16
    cold, hot = spec.get("low_color", "#203450"), spec.get("high_color", GOLD)
    out = [text(L + cw * len(cols) / 2, 18, spec.get("col_title", ""), size=12, fill=SUB, anchor="middle", weight=600),
           text(14, T + ch * len(rows) / 2, spec.get("row_title", ""), size=12, fill=SUB, weight=600,
                extra=f' transform="rotate(-90 14 {T + ch * len(rows) / 2:.0f})" dominant-baseline="hanging"')]
    for j, c in enumerate(cols):
        out.append(text(L + cw * (j + .5), T - 12, c, size=12, fill=TEXT, anchor="middle", font=MONO))
    base = spec.get("base")
    for i, r in enumerate(rows):
        out.append(text(L - 12, T + ch * (i + .5) + 4, r, size=12, fill=TEXT, anchor="end", font=MONO))
        for j, v in enumerate(vals[i]):
            x, y = L + cw * j, T + ch * i
            if v is None:
                out.append(f'<rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" fill="#1a2c45"/>')
                continue
            t = (v - lo) / (hi - lo) if hi > lo else .5
            fill = _lerp(cold, hot, t)
            stroke = f' stroke="{TEXT}" stroke-width="2"' if base and base == [i, j] else ""
            out.append(f'<rect x="{x + 1}" y="{y + 1}" width="{cw - 2}" height="{ch - 2}" rx="3" fill="{fill}"{stroke}/>')
            out.append(text(x + cw / 2, y + ch / 2 + 4, fmt(v, spec), size=12, fill="#0c1220" if t > .55 else TEXT,
                            anchor="middle", weight=600, font=MONO))
    return figure(spec, "".join(out), W, H, min_w=min(520, W))


# ── left-to-right tree ───────────────────────────────────────────────────────
def tree(spec):
    root = spec["root"]
    nw, gap, lh = spec.get("node_width", 170), spec.get("col_gap", 44), 15

    def depth(n):
        return 1 + max((depth(c) for c in n.get("children", [])), default=0)

    def lines_of(n, d):
        return wrap(n["label"], int(nw / (7.6 if d else 8.4)))

    def height(n, d):
        own = 16 + len(lines_of(n, d)) * lh
        kids = n.get("children", [])
        return max(own + 10, sum(height(c, d + 1) for c in kids)) if kids else own + 10

    D = depth(root)
    W = D * nw + (D - 1) * gap + 20
    H = height(root, 0) + 10
    edges, nodes = [], []

    def place(n, d, top):
        h = height(n, d)
        ls = lines_of(n, d)
        bh = 12 + len(ls) * lh
        x, cy = 10 + d * (nw + gap), top + h / 2
        kids, y = n.get("children", []), top
        for c in kids:
            ch_ = height(c, d + 1)
            cx2, cy2 = 10 + (d + 1) * (nw + gap), y + ch_ / 2
            mid = x + nw + gap / 2
            edges.append(f'<path d="M{x + nw},{cy:.1f} C{mid},{cy:.1f} {mid},{cy2:.1f} {cx2},{cy2:.1f}" fill="none" stroke="{GOLD if d == 0 else STEEL}" stroke-opacity=".6" stroke-width="1.5"/>')
            place(c, d + 1, y)
            y += ch_
        fill = GOLD if d == 0 else ("#253c5b" if kids else "#1a2c45")
        tc = "#0c1220" if d == 0 else TEXT
        box = (f'<rect x="{x}" y="{cy - bh / 2:.1f}" width="{nw}" height="{bh}" rx="7" fill="{fill}" '
               f'stroke="{GOLD if n.get("hl") else "rgba(255,255,255,.12)"}"/>'
               + mtext(x + 10, cy - bh / 2 + 6 + lh * .8, ls, size=12.5 if d else 13.5, lh=lh / 12.5, fill=tc, weight=700 if d < 2 else 400))
        if n.get("href"):
            box = f'<a href="{esc(n["href"])}">{box}</a>'
        nodes.append(box)

    place(root, 0, 5)
    return figure(spec, "".join(edges + nodes), W, H, min_w=min(W, 640))


# ── process flow (vertical, numbered) ────────────────────────────────────────
def flow(spec):
    steps, W = spec["steps"], 720
    out, y = [], 6
    for i, s in enumerate(steps):
        sub = wrap(s.get("sub", ""), 88) if s.get("sub") else []
        h = 46 + len(sub) * 17
        out.append(f'<rect x="60" y="{y}" width="{W - 70}" height="{h}" rx="9" fill="#1a2c45" stroke="rgba(255,255,255,.08)"/>')
        out.append(f'<circle cx="28" cy="{y + h / 2:.1f}" r="17" fill="{GOLD}"/>')
        out.append(text(28, y + h / 2 + 5, f"{i + 1:02d}", size=12, fill="#0c1220", anchor="middle", weight=700, font=MONO))
        out.append(text(78, y + 27, s["title"], size=15, weight=600))
        if s.get("tag"):
            out.append(text(W - 24, y + 27, s["tag"], size=11, fill=GOLD, anchor="end", font=MONO))
        out.append(mtext(78, y + 48, sub, size=12.5, lh=1.36, fill=SUB))
        if i < len(steps) - 1:
            out.append(f'<path d="M28,{y + h / 2 + 18:.1f} L28,{y + h + 14:.1f}" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 4"/>')
        y += h + 14
    return figure(spec, "".join(out), W, y)


# ── funnel ───────────────────────────────────────────────────────────────────
def funnel(spec):
    stages, W, sh = spec["stages"], 720, 52
    vmax = stages[0][1]
    out, y = [], 4
    for i, (label, v, *note) in enumerate(stages):
        nxt = stages[i + 1][1] if i + 1 < len(stages) else v * .7
        w1 = 120 + 300 * math.sqrt(v / vmax)
        w2 = 120 + 300 * math.sqrt(nxt / vmax)
        cx = 230
        col = _lerp(STEEL, GOLD, i / max(1, len(stages) - 1))
        out.append(f'<path d="M{cx - w1 / 2:.1f},{y} L{cx + w1 / 2:.1f},{y} L{cx + w2 / 2:.1f},{y + sh - 4} L{cx - w2 / 2:.1f},{y + sh - 4} Z" fill="{col}"/>')
        out.append(text(cx, y + sh / 2 + 4, fmt(v, spec), size=15, fill="#0c1220" if i > len(stages) / 2 else TEXT, anchor="middle", weight=700, font=MONO))
        out.append(text(410, y + 22, label, size=14, weight=600))
        if note:
            out.append(text(410, y + 40, note[0], size=12, fill=SUB))
        y += sh
    return figure(spec, "".join(out), W, y + 4)


# ── 2x2 quadrant ─────────────────────────────────────────────────────────────
def quadrant(spec):
    W, H, L, B, T, R = 720, 470, 56, 46, 14, 20
    pw, ph = W - L - R, H - T - B
    q = spec.get("quadrants", ["", "", "", ""])  # TL, TR, BL, BR
    out = [f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" fill="#1a2c45" rx="8"/>',
           f'<rect x="{L + pw / 2}" y="{T}" width="{pw / 2}" height="{ph / 2}" fill="{GOLD}" fill-opacity=".09"/>',
           f'<line x1="{L + pw / 2}" x2="{L + pw / 2}" y1="{T}" y2="{T + ph}" stroke="rgba(255,255,255,.15)" stroke-dasharray="4 4"/>',
           f'<line x1="{L}" x2="{L + pw}" y1="{T + ph / 2}" y2="{T + ph / 2}" stroke="rgba(255,255,255,.15)" stroke-dasharray="4 4"/>']
    for k, (qx, qy, anc) in enumerate([(L + 12, T + 22, "start"), (L + pw - 12, T + 22, "end"),
                                       (L + 12, T + ph - 12, "start"), (L + pw - 12, T + ph - 12, "end")]):
        out.append(text(qx, qy, q[k], size=11.5, fill=GOLD if k == 1 else MUTED, anchor=anc, weight=600, font=MONO))
    out.append(text(L + pw / 2, H - 12, spec.get("x_label", "") + "  →", size=12.5, fill=SUB, anchor="middle", weight=600))
    out.append(text(18, T + ph / 2, spec.get("y_label", "") + "  →", size=12.5, fill=SUB, anchor="middle", weight=600,
                    extra=f' transform="rotate(-90 18 {T + ph / 2})"'))
    for p in spec["points"]:
        x, y = L + pw * p["x"], T + ph * (1 - p["y"])
        col = GOLD if p.get("hl") else "#60a5fa"
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{9 if p.get("hl") else 7}" fill="{col}" fill-opacity=".9" stroke="#132338" stroke-width="2"/>')
        anc = "end" if p["x"] > .72 else "start"
        dx = -14 if anc == "end" else 14
        out.append(mtext(x + dx, y + 4, wrap(p["label"], 24), size=12, anchor=anc, weight=600 if p.get("hl") else 400))
    return figure(spec, "".join(out), W, H)


# ── vertical timeline ────────────────────────────────────────────────────────
def timeline(spec):
    ev, W = spec["events"], 720
    out, y = [], 8
    for i, e in enumerate(ev):
        sub = wrap(e.get("sub", ""), 70)
        h = 34 + len(sub) * 17
        out.append(text(110, y + 18, e["when"], size=12, fill=GOLD, anchor="end", weight=600, font=MONO))
        out.append(f'<circle cx="134" cy="{y + 13}" r="7" fill="{GOLD if e.get("hl") else STEEL}" stroke="#132338" stroke-width="3"/>')
        if i < len(ev) - 1:
            out.append(f'<line x1="134" x2="134" y1="{y + 22}" y2="{y + h + 6}" stroke="rgba(255,255,255,.14)" stroke-width="2"/>')
        out.append(text(156, y + 18, e["title"], size=14.5, weight=600))
        out.append(mtext(156, y + 38, sub, size=12.5, lh=1.36, fill=SUB))
        y += h + 10
    return figure(spec, "".join(out), W, y)


# ── donut ────────────────────────────────────────────────────────────────────
def donut(spec):
    data, W, H = spec["data"], 720, 300
    tot = sum(d[1] for d in data)
    cx, cy, r, rw = 150, 150, 118, 34
    out, a0 = [], -math.pi / 2
    for i, d in enumerate(data):
        a1 = a0 + 2 * math.pi * d[1] / tot
        large = 1 if a1 - a0 > math.pi else 0
        p = lambda a, rr: (cx + rr * math.cos(a), cy + rr * math.sin(a))
        (x0, y0), (x1, y1) = p(a0, r), p(a1 - .012, r)
        (x2, y2), (x3, y3) = p(a1 - .012, r - rw), p(a0, r - rw)
        out.append(f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} '
                   f'A{r - rw},{r - rw} 0 {large} 0 {x3:.1f},{y3:.1f} Z" fill="{PALETTE[i % len(PALETTE)]}"/>')
        a0 = a1
    out.append(text(cx, cy - 2, spec.get("center", ""), size=26, anchor="middle", weight=700, font="Space Grotesk, sans-serif"))
    out.append(text(cx, cy + 20, spec.get("center_sub", ""), size=11.5, fill=SUB, anchor="middle"))
    y = 150 - len(data) * 17
    for i, d in enumerate(data):
        out.append(f'<rect x="320" y="{y - 10}" width="12" height="12" rx="2" fill="{PALETTE[i % len(PALETTE)]}"/>')
        out.append(text(342, y, d[0], size=13.5))
        out.append(text(700, y, f"{fmt(d[1], spec)}  ·  {100 * d[1] / tot:.0f}%", size=12.5, fill=SUB, anchor="end", font=MONO))
        y += 34
    return figure(spec, "".join(out), W, H)


# ── radar ────────────────────────────────────────────────────────────────────
def radar(spec):
    axes, series = spec["axes"], spec["series"]
    W, H, cx, cy, R = 720, 420, 250, 210, 160
    n, vmax = len(axes), spec.get("max", 10)
    ang = lambda i: -math.pi / 2 + 2 * math.pi * i / n
    out = []
    for k in range(1, 6):
        rr = R * k / 5
        pts = " ".join(f"{cx + rr * math.cos(ang(i)):.1f},{cy + rr * math.sin(ang(i)):.1f}" for i in range(n))
        out.append(f'<polygon points="{pts}" fill="none" stroke="{GRID}"/>')
    for i, a in enumerate(axes):
        x, y = cx + R * math.cos(ang(i)), cy + R * math.sin(ang(i))
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{GRID}"/>')
        lx, ly = cx + (R + 20) * math.cos(ang(i)), cy + (R + 20) * math.sin(ang(i))
        anc = "middle" if abs(lx - cx) < 10 else ("start" if lx > cx else "end")
        out.append(mtext(lx, ly + 4, wrap(a, 18), size=12, fill=SUB, anchor=anc))
    for si, s in enumerate(series):
        col = s.get("color") or PALETTE[si % len(PALETTE)]
        pts = " ".join(f"{cx + R * v / vmax * math.cos(ang(i)):.1f},{cy + R * v / vmax * math.sin(ang(i)):.1f}" for i, v in enumerate(s["values"]))
        out.append(f'<polygon points="{pts}" fill="{col}" fill-opacity=".16" stroke="{col}" stroke-width="2.2"/>')
        out.append(f'<rect x="520" y="{150 + si * 30}" width="14" height="14" rx="3" fill="{col}"/>')
        out.append(text(544, 162 + si * 30, s["name"], size=13.5))
    return figure(spec, "".join(out), W, H)


# ── waterfall ────────────────────────────────────────────────────────────────
def waterfall(spec):
    steps = spec["steps"]  # [label, delta] ; label starting with '=' is a total bar
    W, H, L, B, T = 720, 340, 56, 58, 26
    run, bars_, lo, hi = 0, [], 0, 0
    for label, v in steps:
        if label.startswith("="):
            bars_.append((label[1:], 0, run, True))
        else:
            bars_.append((label, run, run + v, False))
            run += v
        lo, hi = min(lo, run), max(hi, run)
    ticks = nice_ticks(lo, hi)
    lo, hi = ticks[0], ticks[-1]
    ph = H - B - T
    y_of = lambda v: T + ph * (1 - (v - lo) / (hi - lo))
    slot = (W - L - 10) / len(bars_)
    bw = slot * .6
    out = []
    for t in ticks:
        out.append(f'<line x1="{L}" x2="{W - 10}" y1="{y_of(t):.1f}" y2="{y_of(t):.1f}" stroke="{GRID}"/>')
        out.append(text(L - 8, y_of(t) + 4, fmt(t, {**spec, "decimals": 0}), size=11, fill=MUTED, anchor="end", font=MONO))
    for i, (label, a, b, total) in enumerate(bars_):
        cx = L + slot * (i + .5)
        col = GOLD if total else ("#34d399" if b >= a else "#f87171")
        top, bot = y_of(max(a, b)), y_of(min(a, b))
        out.append(f'<rect x="{cx - bw / 2:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{max(1.5, bot - top):.1f}" rx="3" fill="{col}"/>')
        val = b if total else b - a
        out.append(text(cx, top - 7, ("" if total or val < 0 else "+") + fmt(val, spec), size=11.5, anchor="middle", weight=600, font=MONO))
        out.append(mtext(cx, H - B + 18, wrap(label, max(7, int(slot / 7))), size=11, fill=SUB, anchor="middle"))
    return figure(spec, "".join(out), W, H)


# ── HTML blocks (not SVG) ────────────────────────────────────────────────────
def stats(spec):
    items = "".join(f'<div class="stat"><b>{esc(i["value"])}</b><span>{esc(i["label"])}</span></div>' for i in spec["items"])
    return f'<div class="stats">{items}</div>'


def widget(spec):
    cfg = esc(json.dumps(spec.get("config", {})))
    return (f'<figure class="viz widget" data-widget="{esc(spec["name"])}" data-config="{cfg}">'
            f'<div class="viz-title">{esc(spec.get("title", ""))}</div><div class="widget-body"></div>'
            f'<figcaption>{esc(spec.get("caption", ""))}</figcaption></figure>')


RENDERERS = {f.__name__: f for f in (bars, columns, stacked, line, heatmap, tree, flow, funnel, quadrant,
                                     timeline, donut, radar, waterfall, stats, widget)}


def render(spec):
    return RENDERERS[spec["type"]](spec)
