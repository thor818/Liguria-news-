"""Genera i poster Live Riviera (SVG, formato 50x70).

Ogni poster è un'illustrazione vettoriale in stile vintage: cielo, mare, città
disegnate con forme piatte, titolo grande in basso. Uso: python3 genera.py
"""
import random
from pathlib import Path

W, H = 500, 700
OUT = Path(__file__).parent / "svg"

# Palette comune della collezione
CREAM = "#f6ecd9"
NAVY = "#14324a"
INK = "#1e2a33"
SHUTTER = "#3f6b4a"
HOUSES = ["#e8a55a", "#d9663f", "#f2c45a", "#e88a6a", "#c94f3b", "#f0d9a8", "#e3b07a", "#b84a3a", "#f4b88a"]


def rect(x, y, w, h, fill, extra=""):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" {extra}/>'


def poly(points, fill, extra=""):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polygon points="{pts}" fill="{fill}" {extra}/>'


def path(d, fill, extra=""):
    return f'<path d="{d}" fill="{fill}" {extra}/>'


def circle(x, y, r, fill, extra=""):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" {extra}/>'


def house(x, base, w, h, color, rnd, roof=True, shutters=True):
    """Casa ligure: facciata colorata, finestre con persiane verdi, tetto."""
    out = [rect(x, base - h, w, h, color)]
    if roof:
        out.append(poly([(x - 1.5, base - h), (x + w + 1.5, base - h), (x + w - 2, base - h - 5), (x + 2, base - h - 5)], "#9c4a33"))
    cols = max(1, int(w // 11))
    rows = max(1, int((h - 8) // 15))
    gw = w / cols
    for r in range(rows):
        for c in range(cols):
            wx = x + c * gw + gw / 2 - 2.2
            wy = base - h + 7 + r * 15
            if wy + 8 > base - 2:
                continue
            out.append(rect(wx, wy, 4.4, 8, SHUTTER if shutters and rnd.random() > 0.15 else INK))
    return "".join(out)


def town(x0, x1, base, hmin, hmax, rnd, colors=HOUSES, step=(16, 28)):
    out, x = [], x0
    while x < x1:
        w = rnd.uniform(*step)
        h = rnd.uniform(hmin, hmax)
        out.append(house(x, base, w, h, rnd.choice(colors), rnd))
        x += w - 0.5
    return "".join(out)


def hill_town(cx, base, width, height, rnd, colors=HOUSES):
    """Borgo arroccato su una collina: case piccole a gradoni."""
    out = []
    layers = 7
    for i in range(layers):
        y = base - i * height / layers
        half = width / 2 * (1 - i / (layers + 1.5))
        x = cx - half
        while x < cx + half:
            w = rnd.uniform(8, 14)
            h = rnd.uniform(10, 18)
            out.append(rect(x, y - h, w, h, rnd.choice(colors)))
            out.append(rect(x + w / 2 - 1.5, y - h + 4, 3, 4, SHUTTER))
            x += w
    return "".join(out)


def palm(x, y, h, color="#2f5a3c", trunk="#7a5236", lean=6):
    out = [path(f"M{x-3},{y} Q{x+lean/2},{y-h/2} {x+lean},{y-h} L{x+lean+4},{y-h} Q{x+lean/2+4},{y-h/2} {x+3},{y} Z", trunk)]
    tx, ty = x + lean + 2, y - h
    for ang, ln in [(-160, 34), (-120, 30), (-60, 32), (-20, 36), (200, 26), (-90, 22), (20, 28)]:
        import math
        a = math.radians(ang)
        ex, ey = tx + math.cos(a) * ln, ty + math.sin(a) * ln * 0.75 + 8
        cx, cy = tx + math.cos(a) * ln * 0.5, ty + math.sin(a) * ln * 0.5 - 10
        out.append(path(f"M{tx},{ty} Q{cx},{cy} {ex},{ey} Q{cx},{cy+8} {tx},{ty+3} Z", color))
    return "".join(out)


def boat(x, y, color, sail=False, s=1.0):
    out = [path(f"M{x},{y} L{x+30*s},{y} L{x+25*s},{y+7*s} L{x+5*s},{y+7*s} Z", color),
           rect(x + 2 * s, y - 1.5 * s, 26 * s, 1.5 * s, CREAM)]
    if sail:
        out.append(poly([(x + 15 * s, y - 2), (x + 15 * s, y - 34 * s), (x + 29 * s, y - 4)], CREAM))
        out.append(rect(x + 14.3 * s, y - 36 * s, 1.4 * s, 34 * s, INK))
    return "".join(out)


def yacht(x, y, s=1.0):
    return (path(f"M{x},{y} L{x+60*s},{y} L{x+52*s},{y+9*s} L{x+6*s},{y+9*s} Z", "#fbfaf6")
            + rect(x + 14 * s, y - 8 * s, 30 * s, 8 * s, "#fbfaf6") + rect(x + 18 * s, y - 6 * s, 22 * s, 3 * s, NAVY)
            + rect(x + 22 * s, y - 13 * s, 14 * s, 5 * s, "#fbfaf6"))


def umbrella(x, y, c1, c2="#fbfaf6", r=18):
    out = [rect(x - 0.8, y - 2, 1.6, 26, INK)]
    for i in range(6):
        a0, a1 = 180 + i * 30, 180 + (i + 1) * 30
        import math
        p0 = (x + r * math.cos(math.radians(a0)), y + r * 0.55 * math.sin(math.radians(a0)))
        p1 = (x + r * math.cos(math.radians(a1)), y + r * 0.55 * math.sin(math.radians(a1)))
        out.append(poly([(x, y - r * 0.55), p0, p1], c1 if i % 2 == 0 else c2))
    return "".join(out)


def waves(y0, y1, color, rnd, n=26):
    out = []
    for _ in range(n):
        x = rnd.uniform(0, W)
        y = rnd.uniform(y0, y1)
        w = rnd.uniform(10, 34)
        out.append(rect(x, y, w, 1.6, color, 'rx="0.8" opacity="0.55"'))
    return "".join(out)


def sky(c_top, c_bot):
    return (f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c_top}"/>'
            f'<stop offset="1" stop-color="{c_bot}"/></linearGradient>')


def frame(title, sub, body, band, title_color=CREAM, sub_color=None, defs="", size=96):
    """Cornice comune: illustrazione + banda con titolo, sottotitolo e marchio."""
    sub_color = sub_color or title_color
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*2}" height="{H*2}">
<defs>{defs}
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4"/>
<feColorMatrix values="0 0 0 0 0.2  0 0 0 0 0.15  0 0 0 0 0.1  0 0 0 0.09 0"/></filter>
<clipPath id="art"><rect x="22" y="22" width="{W-44}" height="530"/></clipPath>
</defs>
<rect width="{W}" height="{H}" fill="{CREAM}"/>
<g clip-path="url(#art)">{body}</g>
<rect x="22" y="552" width="{W-44}" height="126" fill="{band}"/>
<text x="{W/2}" y="638" text-anchor="middle" font-family="'Bebas Neue', 'Oswald', Impact, sans-serif" font-size="{size}" letter-spacing="6" fill="{title_color}">{title}</text>
<text x="{W/2}" y="664" text-anchor="middle" font-family="'Josefin Sans', 'Futura', sans-serif" font-size="12.5" font-weight="600" letter-spacing="5" fill="{sub_color}">{sub}</text>
<text x="{W-30}" y="{H-8}" text-anchor="end" font-family="'Josefin Sans', sans-serif" font-size="7.5" font-weight="700" letter-spacing="2.5" fill="{INK}" opacity="0.75">LIVE RIVIERA</text>
<rect width="{W}" height="{H}" filter="url(#grain)"/>
</svg>'''


# ---------------------------------------------------------------- LIGURIA

def genova():
    rnd = random.Random(1)
    b = [rect(0, 0, W, 560, "url(#sky)"), circle(370, 150, 58, "#ffd45c"), circle(370, 150, 74, "#ffd45c", 'opacity="0.25"')]
    # colline con la città che sale
    b.append(path("M0,250 Q90,170 190,215 T380,190 T500,170 L500,420 L0,420 Z", "#8fa06a"))
    b.append(path("M0,300 Q120,240 240,280 T500,250 L500,420 L0,420 Z", "#a7b07a"))
    for i in range(6):
        y = 400 - i * 24
        b.append(town(-10 + i * 18, 520 - i * 14, y, 18, 40 - i * 3, rnd, step=(12, 22)))
    # porto
    b.append(rect(0, 400, W, 160, NAVY))
    b.append(rect(0, 400, W, 6, "#2c5875"))
    b.append(waves(410, 540, "#4f7f9f", rnd, 40))
    # traghetto
    b.append(path("M40,440 L210,440 L196,462 L58,462 Z", "#fbfaf6") + rect(70, 420, 110, 20, "#fbfaf6")
             + rect(80, 426, 90, 5, NAVY) + rect(150, 404, 14, 16, "#d9663f") + rect(150, 404, 14, 4, INK))
    # Lanterna sullo scoglio
    b.append(path("M320,560 L338,428 Q380,400 450,404 L520,420 L520,560 Z", "#5d5348"))
    b.append(path("M350,560 L362,446 Q400,428 470,432 L520,444 L520,560 Z", "#4a4239"))
    b.append(rect(370, 316, 56, 102, "#f4ecda") + rect(370, 316, 18, 102, "#e2d6bd"))
    b.append(rect(380, 238, 36, 78, "#f4ecda") + rect(380, 238, 12, 78, "#e2d6bd"))
    b.append(rect(366, 312, 64, 7, "#c94f3b") + rect(376, 234, 44, 6, "#c94f3b") + rect(366, 414, 64, 8, "#c94f3b"))
    b.append(rect(388, 212, 20, 22, "#ffd45c") + rect(386, 208, 24, 4, INK) + poly([(384, 208), (412, 208), (398, 192)], INK))
    b.append(poly([(398, 220), (520, 168), (520, 262)], "#ffd45c", 'opacity="0.3"'))
    for k in range(4):
        b.append(rect(394, 250 + k * 15, 8, 8, INK))
    for k in range(5):
        b.append(rect(392, 330 + k * 16, 12, 8, INK))
    b.append(boat(240, 500, "#c94f3b", sail=True, s=1.1))
    return frame("GENOVA", "LIGURIA · ITALIA", "".join(b), NAVY, defs=sky("#f39a6a", "#ffd9a0"))


def portofino():
    rnd = random.Random(2)
    b = [rect(0, 0, W, 560, "url(#sky)")]
    # promontorio verde con chiesa di San Giorgio e Castello Brown
    b.append(path("M260,560 L260,250 Q320,150 420,175 Q480,190 520,240 L520,560 Z", "#3f6b4a"))
    b.append(path("M300,560 L300,280 Q360,210 440,230 Q490,245 520,280 L520,560 Z", "#4f7d55"))
    for k in range(18):
        x, y = rnd.uniform(300, 500), rnd.uniform(230, 330)
        b.append(circle(x, y, rnd.uniform(8, 15), "#2f5a3c"))
    b.append(rect(392, 162, 40, 22, "#f2c45a") + poly([(388, 162), (436, 162), (412, 146)], "#9c4a33"))
    b.append(rect(420, 128, 10, 34, "#f2c45a") + poly([(418, 128), (432, 128), (425, 114)], "#9c4a33"))
    # colline dietro a sinistra
    b.append(path("M-20,560 L-20,230 Q60,170 150,215 Q210,240 270,250 L270,560 Z", "#5f8a5d"))
    # case colorate intorno al porto
    b.append(town(-10, 320, 395, 60, 105, rnd, step=(20, 30)))
    b.append(rect(0, 393, 320, 8, "#cdbb98"))
    # mare
    b.append(rect(0, 400, W, 160, "#2f7fa8"))
    b.append(rect(0, 400, W, 4, "#1f5f80"))
    b.append(waves(410, 540, "#cfe7f0", rnd, 30))
    for x, y, c, s in [(40, 450, "#fbfaf6", 1.1), (120, 470, "#c94f3b", 1.0), (210, 445, "#f2c45a", 0.9), (70, 505, "#14324a", 1.2)]:
        b.append(boat(x, y, c, s=s))
    b.append(yacht(270, 480, 1.4))
    b.append(boat(400, 455, "#fbfaf6", sail=True, s=1.2))
    return frame("PORTOFINO", "LIGURIA · ITALIA", "".join(b), "#2f7fa8", defs=sky("#8fc8e8", "#e6f3f6"))


def camogli():
    rnd = random.Random(3)
    b = [rect(0, 0, W, 560, "url(#sky)"), circle(110, 110, 40, "#fff2c4")]
    b.append(path("M-10,330 Q120,200 260,240 Q380,270 520,210 L520,400 L-10,400 Z", "#6f8f5f"))
    # case altissime di Camogli
    x = -5
    while x < 520:
        w = rnd.uniform(26, 38)
        h = rnd.uniform(150, 200)
        b.append(house(x, 410, w, h, rnd.choice(HOUSES), rnd))
        x += w - 0.5
    # Basilica con cupola e castello della Dragonara
    b.append(path("M330,560 L340,380 L470,380 L500,560 Z", "#6a5d4f"))
    b.append(rect(360, 300, 70, 82, "#f0d9a8") + path("M360,300 A35,30 0 0 1 430,300 Z", "#9c4a33"))
    b.append(rect(436, 250, 22, 132, "#f0d9a8") + poly([(434, 250), (460, 250), (447, 228)], "#9c4a33"))
    b.append(rect(442, 262, 10, 14, INK))
    b.append(rect(320, 340, 30, 42, "#d8c49a") + "".join(rect(320 + k * 8, 334, 5, 6, "#d8c49a") for k in range(4)))
    # spiaggia con ombrelloni
    b.append(rect(0, 410, 340, 40, "#e7d7b4"))
    for k in range(80):
        b.append(circle(rnd.uniform(0, 340), rnd.uniform(414, 448), rnd.uniform(1, 2.2), "#c9b691"))
    for x, c in [(30, "#c94f3b"), (90, "#14324a"), (150, "#f2c45a"), (210, "#2f7fa8"), (270, "#c94f3b")]:
        b.append(umbrella(x, 410, c))
    # mare
    b.append(rect(0, 450, W, 110, "#2f7fa8"))
    b.append(waves(456, 548, "#cfe7f0", rnd, 26))
    b.append(boat(60, 490, "#f2c45a") + boat(160, 510, "#c94f3b", s=1.2) + boat(260, 485, "#fbfaf6", sail=True))
    return frame("CAMOGLI", "LIGURIA · ITALIA", "".join(b), "#c94f3b", defs=sky("#9fd0ea", "#fbe6c4"))


def sanremo():
    rnd = random.Random(4)
    b = [rect(0, 0, W, 560, "url(#sky)"), circle(250, 140, 50, "#ffe08a")]
    # colline e la Pigna
    b.append(path("M-10,300 Q100,190 220,220 Q340,250 520,180 L520,360 L-10,360 Z", "#7c9a6a"))
    b.append(hill_town(140, 330, 200, 110, rnd))
    # mare
    b.append(rect(0, 330, W, 40, "#3f8fb8"))
    b.append(waves(334, 366, "#d8eef6", rnd, 12))
    # Casinò bianco
    b.append(rect(270, 270, 170, 90, "#fbf6ea"))
    b.append(rect(330, 250, 50, 20, "#fbf6ea") + path("M330,250 A25,22 0 0 1 380,250 Z", "#fbf6ea"))
    b.append(path("M270,270 A14,14 0 0 1 298,270 Z", "#fbf6ea") + path("M412,270 A14,14 0 0 1 440,270 Z", "#fbf6ea"))
    for k in range(8):
        b.append(rect(280 + k * 20, 290, 9, 26, "#7fa9c4"))
        b.append(rect(280 + k * 20, 330, 9, 22, "#7fa9c4"))
    b.append(rect(266, 356, 178, 6, "#e8dcc4"))
    # campi di fiori a righe
    colors = ["#e0457b", "#f2c45a", "#f07a3a", "#c9356a", "#fbf6ea", "#e8628f"]
    for i in range(9):
        y0 = 370 + i * 21
        b.append(path(f"M-10,{y0} L520,{y0 - 6} L520,{y0 + 15} L-10,{y0 + 21} Z", "#4f7d4a" if i % 2 else "#3f6b3c"))
        for k in range(26):
            x = k * 20 + rnd.uniform(-4, 4)
            b.append(circle(x, y0 + 8 - x * 0.011, rnd.uniform(3, 5.5), colors[i % len(colors)]))
    b.append(palm(70, 470, 200, lean=10) + palm(450, 480, 180, lean=-12))
    return frame("SANREMO", "RIVIERA DEI FIORI · ITALIA", "".join(b), "#c9356a", defs=sky("#7fc0e4", "#fde3c8"))


# ------------------------------------------------------------ CÔTE D'AZUR

def nice():
    rnd = random.Random(5)
    b = [rect(0, 0, W, 560, "url(#sky)")]
    # monti e colline del castello
    b.append(path("M-10,220 Q80,150 170,190 Q260,230 360,160 Q440,110 520,170 L520,300 L-10,300 Z", "#a9b9c9"))
    b.append(path("M330,300 Q380,190 470,200 Q500,205 520,215 L520,320 L330,320 Z", "#4f7d55"))
    # facciate della Promenade lungo la baia curva
    x = -10
    while x < 360:
        w = rnd.uniform(24, 40)
        h = rnd.uniform(40, 75) - x * 0.06
        b.append(house(x, 300 - x * 0.03, w, h, rnd.choice(["#f4e3c2", "#f2c9a0", "#fbf1df", "#e9b98a", "#f6d6b0"]), rnd, roof=False))
        x += w
    # mare turchese e spiaggia di ciottoli in curva
    b.append(path("M-10,300 L520,290 L520,560 L-10,560 Z", "#1f8fb5"))
    b.append(path("M-10,302 Q200,310 360,300 L360,312 Q200,330 -10,326 Z", "#e4dccd"))
    b.append(waves(330, 440, "#d6f0f6", rnd, 30))
    b.append(boat(380, 360, "#fbfaf6", sail=True, s=1.1))
    # Promenade con le sedie blu
    b.append(rect(0, 440, W, 120, "#e9d7bb"))
    b.append(rect(0, 438, W, 6, "#fbfaf6"))
    for k in range(26):
        b.append(rect(k * 20, 444, 3, 10, "#fbfaf6"))
    for x in [70, 190, 310]:
        cx, cy = x, 500
        b.append(path(f"M{cx},{cy} L{cx+40},{cy} L{cx+46},{cy+34} L{cx+40},{cy+34} L{cx+36},{cy+8} L{cx+4},{cy+8} L{cx},{cy+34} L{cx-6},{cy+34} Z", "#2a6fb8"))
        b.append(path(f"M{cx+4},{cy} L{cx+10},{cy-42} L{cx+40},{cy-42} L{cx+38},{cy} Z", "#2a6fb8"))
        for j in range(4):
            b.append(rect(cx + 12, cy - 38 + j * 9, 26, 3, "#4f8fd0"))
    b.append(palm(455, 530, 230, lean=-14))
    return frame("NICE", "CÔTE D'AZUR · FRANCE", "".join(b), "#2a6fb8", defs=sky("#7cc4ec", "#eaf6fb"))


def menton():
    rnd = random.Random(6)
    b = [rect(0, 0, W, 560, "url(#sky)")]
    b.append(path("M-10,250 Q90,140 220,190 Q340,240 520,130 L520,340 L-10,340 Z", "#7d9a76"))
    # città vecchia color pastello a gradoni
    pastel = ["#f6c9a0", "#f4dfa8", "#e9a98a", "#f7e6c4", "#efb7a0", "#f2cf8a", "#e8c2b0"]
    for i in range(6):
        b.append(town(60 + i * 22, 470 - i * 20, 380 - i * 26, 22, 40, rnd, colors=pastel, step=(14, 24)))
    # campanile della Basilica Saint-Michel
    b.append(rect(250, 150, 26, 110, "#f4dfa8") + rect(246, 140, 34, 14, "#e9a98a"))
    b.append(path("M250,140 Q263,100 276,140 Z", "#3f6b4a") + rect(258, 162, 10, 16, INK))
    b.append(rect(240, 260, 46, 60, "#f2cf8a"))
    # mare e spiaggia
    b.append(rect(0, 380, W, 180, "#2f8fbf"))
    b.append(rect(0, 378, W, 6, "#e4dccd"))
    b.append(waves(392, 548, "#d6f0f6", rnd, 30))
    b.append(boat(150, 440, "#fbfaf6", sail=True, s=1.2) + boat(300, 470, "#f2c45a"))
    # ramo di limoni in primo piano
    b.append(path("M520,10 Q420,40 360,110 Q330,150 300,160", "none", f'stroke="#5a4030" stroke-width="7" stroke-linecap="round"'))
    leaves = [(470, 30, -30), (430, 50, 20), (400, 80, -40), (370, 110, 30), (340, 135, -20), (450, 60, 60), (320, 160, 40)]
    for lx, ly, a in leaves:
        b.append(f'<ellipse cx="{lx}" cy="{ly}" rx="26" ry="10" fill="#2f6b3a" transform="rotate({a} {lx} {ly})"/>')
    for lx, ly in [(445, 85), (395, 120), (350, 175), (480, 75)]:
        b.append(f'<ellipse cx="{lx}" cy="{ly}" rx="20" ry="16" fill="#ffd23f"/><ellipse cx="{lx-6}" cy="{ly-5}" rx="6" ry="4" fill="#fff0a0" opacity="0.7"/>')
    return frame("MENTON", "CÔTE D'AZUR · FRANCE", "".join(b), "#e8a020", title_color=INK, defs=sky("#9fd3ef", "#fff1d0"))


def monaco():
    rnd = random.Random(7)
    b = [rect(0, 0, W, 560, "url(#sky)"), circle(400, 120, 40, "#ffd9a0")]
    # Tête de Chien e monti
    b.append(path("M-10,260 L60,150 L140,170 L230,110 L320,180 L420,150 L520,200 L520,330 L-10,330 Z", "#9a8a9a"))
    b.append(path("M-10,300 L80,230 L200,250 L320,220 L520,250 L520,340 L-10,340 Z", "#7d7290"))
    # grattacieli di Monte-Carlo
    x = 250
    while x < 520:
        w = rnd.uniform(18, 30)
        h = rnd.uniform(50, 130)
        b.append(house(x, 340, w, h, rnd.choice(["#fbf1df", "#f4e3c2", "#e9d0b0", "#f6f0e6"]), rnd, roof=False, shutters=False))
        x += w + 2
    # il Rocher con il Palazzo del Principe
    b.append(path("M-10,560 L-10,320 Q40,280 150,290 Q210,296 240,340 L250,560 Z", "#8a6a50"))
    b.append(rect(20, 250, 170, 50, "#f2e2c0") + "".join(rect(20 + k * 14, 244, 8, 8, "#f2e2c0") for k in range(13)))
    b.append(rect(80, 220, 30, 30, "#f2e2c0") + "".join(rect(84 + k * 8, 214, 5, 7, "#f2e2c0") for k in range(3)))
    for k in range(10):
        b.append(rect(30 + k * 16, 262, 7, 12, "#9c4a33"))
    b.append(rect(94, 196, 2, 24, INK) + poly([(96, 196), (118, 200), (96, 205)], "#d62828") + poly([(96, 205), (118, 210), (96, 214)], "#fbfaf6"))
    b.append(path("M0,300 Q60,290 120,300 Q150,320 190,300", "none", 'stroke="#3f6b4a" stroke-width="10"'))
    # porto con yacht
    b.append(rect(240, 340, 280, 220, "#1f6fa8"))
    b.append(rect(240, 340, 280, 5, "#e4dccd"))
    b.append(waves(350, 548, "#cfe7f0", rnd, 26))
    for x, y, s in [(270, 380, 1.2), (360, 410, 1.5), (280, 460, 1.8), (420, 470, 1.3), (330, 520, 1.6)]:
        b.append(yacht(x, y, s))
    return frame("MONACO", "MONTE-CARLO · CÔTE D'AZUR", "".join(b), "#b5233a", defs=sky("#f7b28a", "#fde9cf"))


POSTERS = {
    "liguria-genova": genova, "liguria-portofino": portofino, "liguria-camogli": camogli, "liguria-sanremo": sanremo,
    "cotedazur-nice": nice, "cotedazur-menton": menton, "cotedazur-monaco": monaco,
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, fn in POSTERS.items():
        (OUT / f"{name}.svg").write_text(fn())
        print(name)
