"""Render the hero laptop as one inline SVG and inject it into index.html.

The laptop is modelled in 3D (base slab, keyboard, trackpad, lid at an open
angle) and drawn with an orthographic camera, so every face is an exact
parallelogram. The dashboard in tools/laptop_screen.svg (640x416) is mapped
onto the screen with an affine matrix. Edit the camera or dimensions below and
re-run: python3 tools/laptop.py
"""
import math, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCREEN = (ROOT / 'tools/laptop_screen.svg').read_text()

# model units: x right, y up, z toward the viewer; hinge on the x axis
W, D, T = 400, 268, 9          # base width, depth, thickness
H, OPEN = 262, 14              # lid height, degrees tilted back past vertical
LT = 5                         # lid thickness
LIFT = 70                      # float height above the ground plane
YAW, PITCH, ROLL = -22, 20, -11  # camera, degrees

def cam(p):
    x, y, z = p
    a = math.radians(YAW); x, z = x*math.cos(a) + z*math.sin(a), -x*math.sin(a) + z*math.cos(a)
    b = math.radians(PITCH); y, z = y*math.cos(b) - z*math.sin(b), y*math.sin(b) + z*math.cos(b)
    c = math.radians(ROLL); x, y = x*math.cos(c) - y*math.sin(c), x*math.sin(c) + y*math.cos(c)
    return (x, -y)

def P(x, y, z): return cam((x, y + LIFT, z))
def lid(x, v, off=0.0):
    """Point on the lid: v is height up the lid, off pushes along its back normal."""
    t = math.radians(OPEN)
    return P(x, T + v*math.cos(t) - off*math.sin(t), -v*math.sin(t) - off*math.cos(t))

def poly(pts, **attr):
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    a = ''.join(f' {k.replace("_", "-")}="{v}"' for k, v in attr.items())
    return f'<polygon points="{d}"{a}/>'

def quad(x0, x1, z0, z1, y):
    return [P(x0, y, z0), P(x1, y, z0), P(x1, y, z1), P(x0, y, z1)]

out = []
w = W/2

# ground: soft shadow and a faded mirror of the base footprint
g = [cam((x, 0, z)) for x, z in [(-w, 0), (w, 0), (w, D), (-w, D)]]
gx = sum(p[0] for p in g)/4; gy = sum(p[1] for p in g)/4
out.append(f'<ellipse cx="{gx:.1f}" cy="{gy+6:.1f}" rx="{W*.62:.0f}" ry="{D*.30:.0f}" fill="#000" opacity=".55" filter="url(#lp-blur)"/>')
out.append(f'<ellipse cx="{gx:.1f}" cy="{gy+10:.1f}" rx="{W*.5:.0f}" ry="{D*.2:.0f}" fill="#c8a76a" opacity=".22" filter="url(#lp-blur)"/>')
mir = lambda x, y, z: cam((x, -(y + LIFT) + 2*0, z))
refl = [mir(-w, T, 0), mir(w, T, 0), mir(w, T, D), mir(-w, T, D)]
out.append(poly(refl, fill='url(#lp-refl)', opacity='.22'))

# base slab: front edge, right edge, top
out.append(poly([P(-w, T, D), P(w, T, D), P(w, 0, D), P(-w, 0, D)], fill='url(#lp-edge)'))
out.append(poly([P(w, T, D), P(w, T, 0), P(w, 0, 0), P(w, 0, D)], fill='#2a2f37'))
out.append(poly(quad(-w, w, 0, D, T), fill='url(#lp-top)', stroke='rgba(255,255,255,.22)', stroke_width='.8', stroke_linejoin='round'))
# front lip highlight
out.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in [P(-w, T, D), P(w, T, D), P(w, T, 0)])}" fill="none" stroke="rgba(255,255,255,.45)" stroke-width="1"/>')

# keyboard well and keys
kx0, kx1, kz0, kz1 = -w + 34, w - 34, 22, 138
out.append(poly(quad(kx0, kx1, kz0, kz1, T), fill='#0a0c10'))
rows = [(0, 14), (1, 14), (2, 14), (3, 13), (4, 12), (5, 11)]
pad = 3.2; rh = (kz1 - kz0 - pad) / 6
for r, n in rows:
    z0 = kz0 + pad + r*rh; z1 = z0 + rh - pad
    if r == 0: z1 = z0 + rh*.62 - pad          # short function row
    widths = [1]*n
    if r == 3: widths[0] = widths[-1] = 1.55
    if r == 4: widths[0] = widths[-1] = 2.05
    if r == 5: widths = [1, 1, 1, 1.25, 5.2, 1.25, 1, 1, 1]
    tot = sum(widths); span = kx1 - kx0 - pad
    x = kx0 + pad
    for k in widths:
        x1 = x + span*k/tot - pad
        out.append(poly(quad(x, x1, z0, z1, T + .6), fill='#1a1e25', stroke='#2b313a', stroke_width='.5'))
        x = x1 + pad
# trackpad
out.append(poly(quad(-62, 62, 152, 244, T), fill='url(#lp-pad)', stroke='rgba(0,0,0,.25)', stroke_width='.7'))

# lid: thickness strip on the right and top, then the black bezel face
out.append(poly([lid(w, 0), lid(w, H), lid(w, H, LT), lid(w, 0, LT)], fill='#3a4049'))
out.append(poly([lid(-w, H), lid(w, H), lid(w, H, LT), lid(-w, H, LT)], fill='#4a515b'))
out.append(poly([lid(-w, 0), lid(w, 0), lid(w, H), lid(-w, H)], fill='#07090c', stroke='#5a616b', stroke_width='1', stroke_linejoin='round'))
# hinge shadow line
out.append(f'<line x1="{lid(-w+40,0)[0]:.1f}" y1="{lid(-w+40,0)[1]:.1f}" x2="{lid(w-40,0)[0]:.1f}" y2="{lid(w-40,0)[1]:.1f}" stroke="#000" stroke-width="3" opacity=".5"/>')

# screen: map the 640x416 dashboard onto the bezel's inner rectangle
bz, chin = 9, 16
sw, sh = W - 2*bz, H - bz - chin
o = lid(-w + bz, H - bz); ox = lid(w - bz, H - bz); oy = lid(-w + bz, chin)
a, b = (ox[0]-o[0])/640, (ox[1]-o[1])/640
c, d = (oy[0]-o[0])/416, (oy[1]-o[1])/416
mat = f'matrix({a:.5f} {b:.5f} {c:.5f} {d:.5f} {o[0]:.2f} {o[1]:.2f})'
scr = [lid(-w+bz, H-bz), lid(w-bz, H-bz), lid(w-bz, chin), lid(-w+bz, chin)]
out.append(f'<clipPath id="lp-scr"><polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in scr)}"/></clipPath>')
out.append(f'<g clip-path="url(#lp-scr)"><g transform="{mat}">{SCREEN}</g></g>')
out.append(poly(scr, fill='url(#lp-glare)'))
cx, cy = lid(0, H - bz/2)
out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="1.6" fill="#1d2430"/>')

# fit viewBox to everything drawn
nums = [float(v) for v in re.findall(r'-?\d+\.\d+', ' '.join(out[3:]).split('matrix')[0])]
pts = list(zip(nums[0::2], nums[1::2]))
xs = [p[0] for p in pts] + [p[0] for p in refl]; ys = [p[1] for p in pts] + [p[1] for p in refl]
m = 24
vb = f'{min(xs)-m:.0f} {min(ys)-m:.0f} {max(xs)-min(xs)+2*m:.0f} {max(ys)-min(ys)+2*m:.0f}'

defs = '''<defs>
<filter id="lp-blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
<linearGradient id="lp-top" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7c828c"/><stop offset=".55" stop-color="#4b515a"/><stop offset="1" stop-color="#2c3138"/></linearGradient>
<linearGradient id="lp-edge" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#6f757e"/><stop offset=".6" stop-color="#a3a9b2"/><stop offset="1" stop-color="#5a6069"/></linearGradient>
<linearGradient id="lp-pad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5d636c"/><stop offset="1" stop-color="#3b4048"/></linearGradient>
<linearGradient id="lp-glare" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".13"/><stop offset=".38" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="lp-refl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a4049" stop-opacity=".9"/><stop offset=".7" stop-color="#3a4049" stop-opacity="0"/></linearGradient>
</defs>'''

svg = (f'<svg class="laptop" viewBox="{vb}" font-family="Inter,Arial,sans-serif" role="img" '
       'aria-label="The Goldfib desk on a laptop: one portfolio view synced across all sources, a performance chart, and diligence memos ready before the investment committee.">'
       + defs + ''.join(out) + '</svg>')

html = (ROOT / 'index.html').read_text()
block = f'  <!-- laptop:start -->\n  <div class="device">{svg}</div>\n  <!-- laptop:end -->'
html = re.sub(r'  <!-- laptop:start -->.*?<!-- laptop:end -->', lambda _: block, html, flags=re.S)
(ROOT / 'index.html').write_text(html)
print('laptop injected, viewBox', vb)
