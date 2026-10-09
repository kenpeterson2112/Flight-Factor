"""Draws the Factor Flight reward creatures as standalone SVG files into ../rewards.

Run: python3 tools/make-reward-art.py  (add a new creature as another ART[...] entry).

Shared style: 100x100 viewBox, chunky navy outline, soft gradient fill, a highlight,
big shiny eyes and blush cheeks, plus a ground shadow.
"""
import math, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rewards')
INK = '#1d2150'
SW = 3


def svg(body, defs=''):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + ('<defs>' + defs + '</defs>' if defs else '') + body + '</svg>\n')


def lin(id_, a, b, x2=0, y2=1):
    return (f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient>')


def rad(id_, a, b, cx=.35, cy=.3, r=.85):
    return (f'<radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="{r}">'
            f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>')


def shadow(cx=50, cy=91, rx=30):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="5" fill="{INK}" opacity=".22"/>'


def o(extra=''):
    return f'stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"{extra}'


def eye(x, y, r=7, look=(1, 1)):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r * 1.12:.1f}" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
            f'<circle cx="{x + look[0]}" cy="{y + look[1] * 1.5}" r="{r * .58:.1f}" fill="{INK}"/>'
            f'<circle cx="{x + look[0] + r * .25:.1f}" cy="{y + look[1] * 1.5 - r * .25:.1f}" r="{r * .22:.1f}" fill="#fff"/>')


def happy_eye(x, y, w=5):
    return f'<path d="M{x - w} {y + 1}q{w} -6 {w * 2} 0" fill="none" {o()} stroke-width="3.5"/>'


def cheeks(x1, x2, y, c='#ff7aa8'):
    return (f'<ellipse cx="{x1}" cy="{y}" rx="4.5" ry="2.6" fill="{c}" opacity=".55"/>'
            f'<ellipse cx="{x2}" cy="{y}" rx="4.5" ry="2.6" fill="{c}" opacity=".55"/>')


def smile(x, y, w=6):
    return f'<path d="M{x - w} {y}q{w} {w * .9:.1f} {w * 2} 0" fill="none" {o()} stroke-width="3"/>'


def open_mouth(x, y, w=6):
    return (f'<path d="M{x - w} {y}q{w} {w * 1.4:.1f} {w * 2} 0z" fill="{INK}" {o()} stroke-width="2"/>'
            f'<path d="M{x - w * .5:.1f} {y + w * .45:.1f}q{w * .5:.1f} {w * .5:.1f} {w} 0" fill="#ff7aa8"/>')


def shine(d, w=4, op=.75):
    return f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/>'


def star(cx, cy, ro, ri, fill, rot=-90, stroke=True):
    pts = []
    for i in range(10):
        a = math.radians(rot + i * 36)
        r = ro if i % 2 == 0 else ri
        pts.append(f'{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}')
    s = o() if stroke else ''
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" {s} stroke-width="2.2"/>'


def sparkle(cx, cy, r, fill='#fff', op=1):
    return (f'<path d="M{cx} {cy - r}Q{cx} {cy} {cx + r} {cy}Q{cx} {cy} {cx} {cy + r}Q{cx} {cy} {cx - r} {cy}Q{cx} {cy} {cx} {cy - r}z"'
            f' fill="{fill}" opacity="{op}"/>')


ART = {}

# ---------- common ----------
ART['common/green-slime'] = svg(
    shadow(rx=36) +
    f'<path d="M50 16C31 16 23 38 21 56c-2 14-7 22 1 27 6 3 9-3 13 0 4 4 9 5 15 4 6 1 11 0 15-4 4-3 7 3 13 0 8-5 3-13 1-27C77 38 69 16 50 16z" fill="url(#g)" {o()}/>'
    + shine('M33 32c4-7 10-10 16-10') + '<circle cx="29" cy="42" r="3" fill="#fff" opacity=".75"/>'
    + eye(39, 52) + eye(61, 52) + cheeks(29, 71, 63) + open_mouth(50, 64),
    lin('g', '#8cf7d6', '#22b487'))

ART['common/moon-blob'] = svg(
    shadow() +
    f'<circle cx="50" cy="52" r="34" fill="url(#g)" {o()}/>'
    '<circle cx="29" cy="38" r="6" fill="#8d9ad3" opacity=".55"/><circle cx="70" cy="31" r="4" fill="#8d9ad3" opacity=".55"/>'
    '<circle cx="72" cy="66" r="7" fill="#8d9ad3" opacity=".5"/><circle cx="33" cy="73" r="3.5" fill="#8d9ad3" opacity=".5"/>'
    + shine('M30 26c5-4 11-6 17-6', 3.5, .8)
    + happy_eye(41, 52) + happy_eye(59, 52) + cheeks(32, 68, 60) + smile(50, 62, 5)
    + star(82, 18, 8, 3.5, '#ffc857'),
    rad('g', '#f5f8ff', '#9fadE4'))


def fluffy(cx, cy, r, n, fr, fill):
    pts = [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n)) for i in range(n)]
    outline = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{fr}"/>' for x, y in pts)
    fillc = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{fr}"/>' for x, y in pts)
    return (f'<g fill="{INK}" stroke="{INK}" stroke-width="{SW * 2}">{outline}<circle cx="{cx}" cy="{cy}" r="{r}"/></g>'
            f'<g fill="{fill}">{fillc}<circle cx="{cx}" cy="{cy}" r="{r}"/></g>')


ART['common/dust-bunny'] = svg(
    shadow(rx=32) +
    f'<g transform="rotate(-14 38 30)"><ellipse cx="38" cy="26" rx="8" ry="20" fill="#ffb3d1" {o()}/><ellipse cx="38" cy="28" rx="3.5" ry="13" fill="#ff7aa8"/></g>'
    f'<g transform="rotate(14 62 30)"><ellipse cx="62" cy="26" rx="8" ry="20" fill="#ffb3d1" {o()}/><ellipse cx="62" cy="28" rx="3.5" ry="13" fill="#ff7aa8"/></g>'
    + fluffy(50, 60, 24, 14, 8, 'url(#g)')
    + '<circle cx="36" cy="49" r="3" fill="#fff" opacity=".8"/>'
    + eye(41, 58, 6) + eye(59, 58, 6) + cheeks(32, 68, 68)
    + f'<path d="M47 66l3 3 3-3z" fill="#ff5c8a" {o()} stroke-width="1.5"/>'
    + f'<path d="M50 69v3m0 0q-3 3-6 1m6-1q3 3 6 1" fill="none" {o()} stroke-width="2.2"/>',
    rad('g', '#ffe0ee', '#ff9cc4', .4, .35, .8))

ART['common/pebble-pup'] = svg(
    shadow(rx=30) +
    f'<rect x="33" y="76" width="10" height="13" rx="5" fill="#9b8571" {o()}/><rect x="57" y="76" width="10" height="13" rx="5" fill="#9b8571" {o()}/>'
    f'<path d="M26 40c2-14 14-22 26-22 14 0 24 8 26 20 3 14 1 30-6 38-8 8-34 8-42 0-6-8-6-22-4-36z" fill="url(#g)" {o()}/>'
    f'<path d="M28 28c-10 2-14 14-10 26 3 6 10 4 11-2 1-8 2-16-1-24z" fill="#8a7461" {o()}/>'
    f'<path d="M72 28c10 2 14 14 10 26-3 6-10 4-11-2-1-8-2-16 1-24z" fill="#8a7461" {o()}/>'
    f'<path d="M62 26l4 6-3 5M36 74l4-4" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round" opacity=".35"/>'
    + shine('M38 26c4-3 9-4 13-4', 3.5, .6)
    + eye(40, 46, 6.5) + eye(60, 46, 6.5)
    + f'<ellipse cx="50" cy="62" rx="13" ry="9" fill="#e9dccb" {o()} stroke-width="2.5"/>'
    + f'<ellipse cx="50" cy="58" rx="5" ry="3.5" fill="{INK}"/>'
    + f'<path d="M50 61v4m-5 1q5 4 10 0" fill="none" {o()} stroke-width="2.4"/>'
    + cheeks(31, 69, 57),
    lin('g', '#d9c4ad', '#a88f78'))

ART['common/bubble-bug'] = svg(
    '<circle cx="50" cy="52" r="42" fill="#bfe9ff" opacity=".14" stroke="#bfe9ff" stroke-width="2.5" stroke-opacity=".6"/>'
    + shine('M20 40c3-12 12-21 24-24', 4, .7) + '<circle cx="78" cy="76" r="3" fill="#fff" opacity=".6"/>'
    + f'<path d="M42 28c-4-8-8-12-13-12M58 28c4-8 8-12 13-12" fill="none" {o()} stroke-width="2.5"/>'
    '<circle cx="29" cy="16" r="3.5" fill="#ffc857" stroke="#1d2150" stroke-width="2"/><circle cx="71" cy="16" r="3.5" fill="#ffc857" stroke="#1d2150" stroke-width="2"/>'
    f'<path d="M30 52a20 20 0 0 1 40 0v6a20 20 0 0 1-40 0z" fill="url(#g)" {o()}/>'
    f'<path d="M50 40v35" stroke="{INK}" stroke-width="2.5"/>'
    '<circle cx="39" cy="62" r="4" fill="#9fd0ff"/><circle cx="61" cy="62" r="4" fill="#9fd0ff"/><circle cx="42" cy="72" r="2.5" fill="#9fd0ff"/><circle cx="58" cy="72" r="2.5" fill="#9fd0ff"/>'
    f'<path d="M34 44a16 14 0 0 1 32 0z" fill="#2e57a8" {o()}/>'
    + eye(43, 37, 5.5) + eye(57, 37, 5.5) + cheeks(36, 64, 46),
    lin('g', '#7cc0ff', '#3a7fe0'))

# ---------- rare ----------
ART['rare/comet-cat'] = svg(
    '<path d="M44 40 6 8l20 32-14 4 24 10z" fill="url(#t)"/>'
    + sparkle(14, 22, 4, '#fff', .9) + sparkle(28, 12, 3, '#fff', .7) + sparkle(8, 40, 2.5, '#fff', .7)
    + shadow(58, 92, 26)
    + f'<path d="M38 40 34 18l16 12zM78 40l4-22-16 12z" fill="url(#g)" {o()}/>'
    '<path d="M38 34 37 24l7 6zM78 34l1-10-7 6z" fill="#ff9cc4"/>'
    f'<ellipse cx="58" cy="58" rx="28" ry="26" fill="url(#g)" {o()}/>'
    + shine('M40 44c4-5 9-8 15-8', 3.5, .7)
    + eye(48, 56, 6.5, (1.5, 1)) + eye(68, 56, 6.5, (1.5, 1)) + cheeks(40, 77, 66)
    + f'<path d="M56 64l2 2.5 2-2.5z" fill="#ff5c8a" {o()} stroke-width="1.6"/>'
    + f'<path d="M58 67q-3 4-6 2m6-2q3 4 6 2" fill="none" {o()} stroke-width="2.2"/>'
    + f'<path d="M30 62h9M31 68l8-2M86 62h-9M85 68l-8-2" stroke="{INK}" stroke-width="1.8" stroke-linecap="round" opacity=".6"/>',
    lin('g', '#c8f6ff', '#4fc6ef') + '<linearGradient id="t" x1="1" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#e8fbff"/><stop offset="1" stop-color="#7fe3ff" stop-opacity="0"/></linearGradient>')


def tentacle(x, sway):
    return (f'<path d="M{x} 60c{sway} 8 {-sway} 16 {sway * 1.4:.1f} 26" fill="none" stroke="{INK}" stroke-width="{11 + SW}" stroke-linecap="round"/>',
            f'<path d="M{x} 60c{sway} 8 {-sway} 16 {sway * 1.4:.1f} 26" fill="none" stroke="#ff8db6" stroke-width="11" stroke-linecap="round"/>')


tents = [tentacle(x, s) for x, s in [(30, -6), (40, 4), (50, -4), (60, 5), (70, 7)]]
ART['rare/star-squid'] = svg(
    shadow(rx=32) + ''.join(t[0] for t in tents) + ''.join(t[1] for t in tents)
    + '<circle cx="28" cy="80" r="1.8" fill="#ffd1e2"/><circle cx="44" cy="82" r="1.8" fill="#ffd1e2"/><circle cx="56" cy="80" r="1.8" fill="#ffd1e2"/><circle cx="72" cy="84" r="1.8" fill="#ffd1e2"/>'
    + f'<path d="M50 8C66 18 78 36 78 54c0 10-12 12-28 12S22 64 22 54c0-18 12-36 28-46z" fill="url(#g)" {o()}/>'
    + f'<path d="M24 42 12 34l4 14zM76 42l12-8-4 14z" fill="#ff8db6" {o()}/>'
    + star(50, 30, 9, 4, '#ffc857')
    + shine('M33 34c2-6 6-11 10-14', 3.5, .7)
    + eye(41, 50, 6.5) + eye(59, 50, 6.5) + cheeks(31, 69, 59) + smile(50, 58, 4.5),
    lin('g', '#ffc2d8', '#ff5c93'))

ART['rare/rocket-otter'] = svg(
    f'<path d="M36 80q-4 10 0 16 4-6 4-16zM64 80q4 10 0 16-4-6-4-16z" fill="#ffc857" {o()} stroke-width="2"/>'
    + f'<path d="M37 82q-2 6 0 9 2-3 2-9zM63 82q2 6 0 9-2-3-2-9z" fill="#ff6b3d"/>'
    + f'<rect x="30" y="62" width="12" height="20" rx="5" fill="#c9d3f2" {o()}/><rect x="58" y="62" width="12" height="20" rx="5" fill="#c9d3f2" {o()}/>'
    + f'<ellipse cx="50" cy="72" rx="16" ry="15" fill="url(#g)" {o()}/><ellipse cx="50" cy="75" rx="9" ry="9" fill="#f3d9bd"/>'
    + f'<circle cx="31" cy="26" r="7" fill="#9a6440" {o()}/><circle cx="69" cy="26" r="7" fill="#9a6440" {o()}/>'
    + f'<ellipse cx="50" cy="42" rx="25" ry="22" fill="url(#g)" {o()}/>'
    + f'<path d="M25 34q25-8 50 0" fill="none" stroke="{INK}" stroke-width="5"/>'
    + f'<circle cx="40" cy="31" r="7.5" fill="#7fe3ff" {o()} stroke-width="2.5"/><circle cx="60" cy="31" r="7.5" fill="#7fe3ff" {o()} stroke-width="2.5"/>'
    + '<circle cx="38" cy="29" r="2.2" fill="#fff"/><circle cx="58" cy="29" r="2.2" fill="#fff"/>'
    + f'<ellipse cx="50" cy="52" rx="13" ry="9" fill="#f3d9bd" {o()} stroke-width="2.5"/>'
    + eye(40, 43, 4.5) + eye(60, 43, 4.5)
    + f'<ellipse cx="50" cy="49" rx="4" ry="3" fill="{INK}"/><path d="M50 52v2m-4 1q4 3 8 0" fill="none" {o()} stroke-width="2.2"/>'
    + f'<path d="M36 52h-9M36 56l-8 2M64 52h9M64 56l8 2" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" opacity=".6"/>',
    lin('g', '#c9906a', '#9a6440'))

ART['rare/nebula-newt'] = svg(
    shadow(rx=30)
    + ''.join(f'<path d="M{24 if s < 0 else 76} {y}l{s * 14} {dy}" stroke="{INK}" stroke-width="{7 + SW}" stroke-linecap="round"/>'
              f'<path d="M{24 if s < 0 else 76} {y}l{s * 14} {dy}" stroke="#ff8db6" stroke-width="7" stroke-linecap="round"/>'
              for s in (-1, 1) for y, dy in ((36, -10), (44, -1), (52, 8)))
    + f'<path d="M34 70c-2 10 4 18 16 18s18-8 16-18z" fill="url(#g)" {o()}/>'
    + f'<ellipse cx="50" cy="50" rx="28" ry="22" fill="url(#g)" {o()}/>'
    + sparkle(34, 36, 3.5) + sparkle(64, 34, 2.5) + sparkle(58, 64, 2) + '<circle cx="42" cy="34" r="1.3" fill="#fff"/><circle cx="70" cy="46" r="1.3" fill="#fff"/><circle cx="30" cy="56" r="1.3" fill="#fff"/>'
    + eye(38, 49, 5.5) + eye(62, 49, 5.5) + cheeks(30, 70, 58)
    + f'<path d="M38 59q12 9 24 0" fill="none" {o()} stroke-width="3"/>',
    lin('g', '#b49cff', '#6a3fd8', .4, 1))

# ---------- epic ----------
ART['epic/galaxy-ghost'] = svg(
    '<path d="M18 50a32 32 0 0 1 64 0v38l-8-6-8 6-8-6-8 6-8-6-8 6-8-6-8 6z" fill="none" stroke="#b49cff" stroke-width="10" stroke-linejoin="round" opacity=".35"/>'
    + f'<path d="M18 50a32 32 0 0 1 64 0v38l-8-6-8 6-8-6-8 6-8-6-8 6-8-6-8 6z" fill="url(#g)" {o()}/>'
    + '<ellipse cx="62" cy="70" rx="14" ry="6" fill="#ff7aa8" opacity=".25" transform="rotate(-20 62 70)"/>'
    + sparkle(30, 66, 4) + sparkle(70, 34, 3) + sparkle(64, 78, 2.5, '#ffc857') + sparkle(34, 30, 2.5, '#7fe3ff')
    + '<circle cx="26" cy="46" r="1.3" fill="#fff"/><circle cx="74" cy="56" r="1.5" fill="#fff"/><circle cx="46" cy="78" r="1.3" fill="#fff"/><circle cx="54" cy="24" r="1.2" fill="#fff"/>'
    + '<ellipse cx="40" cy="48" rx="7" ry="9" fill="#e8fbff"/><ellipse cx="60" cy="48" rx="7" ry="9" fill="#e8fbff"/>'
    + f'<ellipse cx="41" cy="50" rx="3.5" ry="5" fill="{INK}"/><ellipse cx="61" cy="50" rx="3.5" ry="5" fill="{INK}"/>'
    + '<circle cx="42.5" cy="47.5" r="1.4" fill="#fff"/><circle cx="62.5" cy="47.5" r="1.4" fill="#fff"/>'
    + f'<ellipse cx="50" cy="63" rx="4" ry="5" fill="{INK}"/>',
    rad('g', '#7d5cff', '#1a1550', .4, .3, .9))

ART['epic/plasma-owl'] = svg(
    shadow(rx=28)
    + f'<path d="M14 30l8 6-6 3 9 5M86 30l-8 6 6 3-9 5" fill="none" stroke="#ffc857" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
    + f'<path d="M30 30 26 12l14 10zM70 30l4-18-14 10z" fill="#e8476e" {o()}/>'
    + f'<path d="M50 18c18 0 28 14 28 34 0 22-12 36-28 36S22 74 22 52c0-20 10-34 28-34z" fill="url(#g)" {o()}/>'
    + f'<path d="M24 50c-6 10-4 24 6 30 2-12 0-22-6-30zM76 50c6 10 4 24-6 30-2-12 0-22 6-30z" fill="#e8476e" {o()}/>'
    + f'<ellipse cx="50" cy="66" rx="13" ry="16" fill="#ffd0dc"/>'
    + f'<path d="M51 56l-6 10h5l-3 9 9-12h-5l3-7z" fill="#ffc857" {o()} stroke-width="1.8"/>'
    + f'<circle cx="38" cy="40" r="11" fill="#fff4cc" stroke="#ffc857" stroke-width="3"/><circle cx="62" cy="40" r="11" fill="#fff4cc" stroke="#ffc857" stroke-width="3"/>'
    + f'<circle cx="38" cy="41" r="6" fill="{INK}"/><circle cx="62" cy="41" r="6" fill="{INK}"/><circle cx="40" cy="38.5" r="2.2" fill="#fff"/><circle cx="64" cy="38.5" r="2.2" fill="#fff"/>'
    + f'<path d="M46 48l4 7 4-7z" fill="#ff9a5a" {o()} stroke-width="2"/>'
    + shine('M32 24c4-3 9-4 13-4', 3.5, .6),
    lin('g', '#ff9cb5', '#ff4f7b'))

ART['epic/crystal-golem'] = svg(
    shadow(rx=34)
    + f'<path d="M30 78h14v12H28zM56 78h14l2 12H56z" fill="#2c9c86" {o()}/>'
    + f'<path d="M16 46l10-6 6 22-8 10-10-6z" fill="#3fd1b0" {o()}/><path d="M84 46l-10-6-6 22 8 10 10-6z" fill="#3fd1b0" {o()}/>'
    + f'<path d="M28 42h44l6 18-8 22H30l-8-22z" fill="url(#g)" {o()}/>'
    + f'<path d="M28 42l22 10 22-10M22 60l28-8 28 8M50 52v30" fill="none" stroke="#1d2150" stroke-width="1.6" opacity=".3"/>'
    + f'<path d="M36 18h28l6 14-6 12H36l-6-12z" fill="url(#g)" {o()}/>'
    + f'<path d="M40 18 34 4l12 10zM50 16l2-14 6 14zM60 18l8-12 0 14z" fill="#b49cff" {o()} stroke-width="2.4"/>'
    + '<path d="M44 52l6-6 6 6-6 8z" fill="#ffc857" stroke="#1d2150" stroke-width="2"/>'
    + '<rect x="39" y="27" width="7" height="5" rx="1.5" fill="#ffc857"/><rect x="54" y="27" width="7" height="5" rx="1.5" fill="#ffc857"/>'
    + '<rect x="40" y="27" width="3" height="2" fill="#fff"/><rect x="55" y="27" width="3" height="2" fill="#fff"/>'
    + f'<path d="M44 37h12" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>'
    + shine('M38 22l8-1', 3, .8) + shine('M32 48l7-3', 3, .7),
    lin('g', '#9ff5e0', '#2fb898', .6, 1))

# ---------- legendary ----------
def mirror(d):
    """Mirror an absolute-coordinate path (M/C/L/Z with x,y pairs) across x = 50."""
    import re
    nums = re.split(r'([MCLZ])', d)
    out, tok = [], None
    for part in nums:
        if part in 'MCLZ' and part:
            out.append(part); continue
        vals = [float(v) for v in re.findall(r'-?\d+\.?\d*', part)]
        out.append(' '.join(f'{100 - vals[i]:g} {vals[i + 1]:g}' for i in range(0, len(vals), 2)))
    return ''.join(out)


WING = 'M44 50C32 34 18 24 2 24C8 30 10 36 8 40C14 40 18 42 16 48C22 48 26 50 24 56C30 56 34 58 32 64C38 64 42 64 46 62Z'
FEATHERS = 'M40 52C30 44 22 40 12 36M38 56C30 52 24 50 18 48M38 60C32 58 28 56 24 56'
TAIL = 'M44 76C40 84 34 88 30 96C38 94 44 90 46 84C46 90 46 94 50 99C54 94 54 90 54 84C56 90 62 94 70 96C66 88 60 84 56 76Z'
ART['legendary/cosmic-phoenix'] = svg(
    f'<path d="{TAIL}" fill="url(#w)" {o()} stroke-width="2.6"/>'
    + f'<path d="{WING}" fill="url(#w)" {o()}/><path d="{mirror(WING)}" fill="url(#w2)" {o()}/>'
    + f'<path d="{FEATHERS}" fill="none" stroke="#fff3b0" stroke-width="2.2" stroke-linecap="round" opacity=".8"/>'
    + f'<path d="{mirror(FEATHERS)}" fill="none" stroke="#fff3b0" stroke-width="2.2" stroke-linecap="round" opacity=".8"/>'
    + f'<path d="M50 36C62 36 66 50 66 60C66 74 58 82 50 82C42 82 34 74 34 60C34 50 38 36 50 36Z" fill="url(#g)" {o()}/>'
    + '<path d="M50 52C55 52 57 58 57 64C57 72 54 76 50 76C46 76 43 72 43 64C43 58 45 52 50 52Z" fill="#ffe9a0"/>'
    + f'<path d="M42 22C40 14 42 8 46 4C46 10 48 12 50 12C50 6 54 2 58 0C58 6 60 12 58 20Z" fill="#ffc857" {o()} stroke-width="2.4"/>'
    + f'<circle cx="50" cy="30" r="14" fill="url(#g)" {o()}/>'
    + eye(44, 29, 4.5) + eye(56, 29, 4.5) + cheeks(39, 61, 36)
    + f'<path d="M47 35l3 6 3-6z" fill="#ffc857" {o()} stroke-width="2"/>'
    + sparkle(10, 60, 3.5, '#ffe9a0') + sparkle(90, 60, 3.5, '#ffe9a0') + sparkle(84, 8, 2.8, '#fff') + sparkle(16, 8, 2.8, '#fff'),
    lin('g', '#ffb36b', '#ff5c5c') + lin('w', '#ffe066', '#ff4f6d', 1, 1)
    + '<linearGradient id="w2" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe066"/><stop offset="1" stop-color="#ff4f6d"/></linearGradient>')

ART['legendary/golden-dragon'] = svg(
    shadow(rx=34)
    + f'<path d="M70 78c12 2 20-4 20-12 0-6-6-8-8-4 2 2 2 6-2 8-4 2-8 0-12 0z" fill="url(#g)" {o()}/>'
    + f'<path d="M30 50 8 34c4 10 2 16 6 20-4 0-6 4-4 8 6-2 12 0 18 2zM70 50l22-16c-4 10-2 16-6 20 4 0 6 4 4 8-6-2-12 0-18 2z" fill="#e0a23a" {o()}/>'
    + f'<path d="M50 44c16 0 24 14 24 28 0 12-10 18-24 18S26 84 26 72c0-14 8-28 24-28z" fill="url(#g)" {o()}/>'
    + f'<path d="M50 54c8 0 12 8 12 16s-5 14-12 14-12-6-12-14 4-16 12-16z" fill="#fff1c2"/>'
    + f'<path d="M41 64h18M40 71h20M42 78h16" stroke="#e0a23a" stroke-width="2" stroke-linecap="round"/>'
    + f'<path d="M36 22 32 6l10 10zM64 22l4-16-10 10z" fill="#fff1c2" {o()} stroke-width="2.4"/>'
    + f'<ellipse cx="50" cy="32" rx="22" ry="18" fill="url(#g)" {o()}/>'
    + f'<path d="M30 30l-6-3 4 7zM70 30l6-3-4 7z" fill="#e0a23a" {o()} stroke-width="2"/>'
    + f'<ellipse cx="50" cy="41" rx="10" ry="6.5" fill="#ffe9a0" {o()} stroke-width="2.4"/>'
    + '<circle cx="46.5" cy="40" r="1.5" fill="#1d2150"/><circle cx="53.5" cy="40" r="1.5" fill="#1d2150"/>'
    + eye(41, 27, 5) + eye(59, 27, 5) + cheeks(33, 67, 35)
    + f'<path d="M46 44.5q4 2.5 8 0" fill="none" {o()} stroke-width="2.2"/>'
    + f'<path d="M62 42c6 0 8-4 12-2-2 2 0 4-4 6 4 0 4 2 2 4-4-2-8 0-12-2z" fill="#ff7a4d" {o()} stroke-width="2"/>'
    + shine('M36 20c4-3 8-4 12-4', 3, .7) + sparkle(84, 18, 3.5, '#fff') + sparkle(14, 74, 3, '#fff'),
    lin('g', '#ffe27a', '#f0a92c'))

import re
import xml.dom.minidom


def dedupe(data):
    """Keep the last value of any attribute set twice on one tag (later ones are overrides)."""
    def fix(m):
        name, attrs, end = m.group(1), m.group(2), m.group(3)
        seen = {}
        for k, v in re.findall(r'([\w:-]+)="([^"]*)"', attrs):
            seen.pop(k, None)
            seen[k] = v
        return '<' + name + ''.join(f' {k}="{v}"' for k, v in seen.items()) + end
    return re.sub(r'<([\w:]+)((?:\s+[\w:-]+="[^"]*")*)\s*(/?>)', fix, data)


for path, data in ART.items():
    data = dedupe(data)
    xml.dom.minidom.parseString(data)  # fails loudly on invalid XML
    full = os.path.join(OUT, path + '.svg')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(data)
print(len(ART), 'files')
