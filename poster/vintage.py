"""Poster Live Riviera — collezione vintage (N° 2).

Ogni poster ha uno stile diverso, come nelle vecchie affiches della Riviera:
- art déco anni '30 (Genova)
- illustrazione rétro anni '50-'60 con personaggi (Portofino, Sanremo, Monaco)
- acquerello minimal (Camogli, Nice)
- linoleografia a tre colori (Menton)
Le texture (carta, acquerello, inchiostro) sono filtri SVG, così il disegno resta modificabile.
Uso: python3 vintage.py  ->  svg in vintage/svg/
"""
import math
import random
from pathlib import Path

W, H = 500, 700
OUT = Path(__file__).parent / "vintage" / "svg"

FONTS = ("https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,800;1,6..96,500"
         "&family=Jost:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,500;1,500"
         "&family=Alfa+Slab+One&family=Racing+Sans+One&display=block")


def P(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


# ------------------------------------------------------------------ texture

def filters(seed=3):
    return f'''
<filter id="rough" x="-5%" y="-5%" width="110%" height="110%">
  <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="3" seed="{seed}" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3" xChannelSelector="R" yChannelSelector="G"/>
</filter>
<filter id="wc" x="-10%" y="-10%" width="120%" height="120%">
  <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="4" seed="{seed}" result="t1"/>
  <feDisplacementMap in="SourceGraphic" in2="t1" scale="13" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="3" seed="{seed + 7}" result="t2"/>
  <feColorMatrix in="t2" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.9 1.25" result="m"/>
  <feComposite in="d" in2="m" operator="in" result="tex"/>
  <feMorphology in="tex" operator="erode" radius="1.4" result="inner"/>
  <feComposite in="tex" in2="inner" operator="out" result="edge"/>
  <feColorMatrix in="edge" type="matrix" values="0.7 0 0 0 0  0 0.7 0 0 0  0 0 0.7 0 0  0 0 0 0.5 0" result="edgeDark"/>
  <feMerge><feMergeNode in="tex"/><feMergeNode in="edgeDark"/></feMerge>
</filter>
<filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
  <feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="{seed}" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="1" seed="{seed + 3}" result="s"/>
  <feColorMatrix in="s" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -9 7.6" result="sm"/>
  <feComposite in="d" in2="sm" operator="in"/>
</filter>
<filter id="paper" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="{seed}"/>
  <feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.28  0 0 0 0 0.2  0 0 0 0.16 0"/>
</filter>
<filter id="fibre" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="0.012 0.2" numOctaves="2" seed="{seed + 1}"/>
  <feColorMatrix values="0 0 0 0 0.4  0 0 0 0 0.32  0 0 0 0 0.22  0 0 0 0.07 0"/>
</filter>
<radialGradient id="vignette" cx="0.5" cy="0.45" r="0.75">
  <stop offset="0.6" stop-color="#3a2a1a" stop-opacity="0"/><stop offset="1" stop-color="#3a2a1a" stop-opacity="0.28"/>
</radialGradient>'''


def grad(gid, stops, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def page(body, defs="", seed=3, border="#f4ead6"):
    """Foglio: illustrazione a tutta pagina, bordo carta, grana e vignettatura."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*2}" height="{H*2}">
<defs><style>@import url("{FONTS}");</style>{filters(seed)}{defs}
<clipPath id="sheet"><rect x="14" y="14" width="{W-28}" height="{H-28}"/></clipPath></defs>
<rect width="{W}" height="{H}" fill="{border}"/>
<g clip-path="url(#sheet)">{body}
<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="url(#vignette)"/></g>
<rect width="{W}" height="{H}" filter="url(#fibre)"/>
<rect width="{W}" height="{H}" filter="url(#paper)"/>
</svg>'''


def text(x, y, s, font, size, fill, spacing=0, weight=400, anchor="middle", style="", extra=""):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" letter-spacing="{spacing}" fill="{fill}" {style} {extra}>{s}</text>')


def palm(x, y, h, lean, frond="#1f4a35", trunk="#6b4a32", s=1.0):
    out = [f'<path d="M{x-3*s},{y} Q{x+lean*0.4},{y-h*0.55} {x+lean},{y-h} L{x+lean+5*s},{y-h} Q{x+lean*0.4+5*s},{y-h*0.55} {x+3*s},{y} Z" fill="{trunk}"/>']
    for k in range(int(h / 9)):
        yy = y - k * 9
        xx = x + lean * ((k * 9) / h) ** 1.4 * 0.95
        out.append(f'<path d="M{xx-3*s},{yy} l{6*s},-2" stroke="#4a3220" stroke-width="1" opacity="0.6"/>')
    tx, ty = x + lean + 2.5 * s, y - h
    for ang, ln in [(-170, 46), (-140, 40), (-110, 34), (-70, 34), (-40, 42), (-10, 48), (160, 36), (20, 38), (195, 30)]:
        a = math.radians(ang)
        ex, ey = tx + math.cos(a) * ln * s, ty + (math.sin(a) * 0.55 + 0.55) * ln * s
        cx, cy = tx + math.cos(a) * ln * 0.5 * s, ty + math.sin(a) * ln * 0.45 * s - 6 * s
        out.append(f'<path d="M{tx},{ty} Q{cx},{cy} {ex},{ey} Q{cx},{cy + 7*s} {tx},{ty + 3*s} Z" fill="{frond}"/>')
    return "".join(out)


# ----------------------------------------------------------- 1. GENOVA déco

def genova():
    rnd = random.Random(11)
    navy, cream, gold, terra, sea2 = "#16283b", "#f1e3c2", "#d9a441", "#b8482e", "#24496a"
    b = [f'<rect width="{W}" height="{H}" fill="url(#gsky)"/>']
    # raggiera déco dietro la Lanterna
    cx, cy = 330, 250
    for i in range(36):
        a0, a1 = math.radians(i * 10), math.radians(i * 10 + 5)
        b.append(f'<polygon points="{P([(cx, cy), (cx + 700*math.cos(a0), cy + 700*math.sin(a0)), (cx + 700*math.cos(a1), cy + 700*math.sin(a1))])}" fill="{gold}" opacity="0.18"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="62" fill="{gold}"/><circle cx="{cx}" cy="{cy}" r="78" fill="none" stroke="{gold}" stroke-width="2" opacity="0.6"/>')
    # colline a gradoni con la città geometrica
    for i, (yb, col) in enumerate([(370, "#c7a77c"), (410, "#b48f66"), (450, "#9c7656")]):
        b.append(f'<path d="M0,{yb-60+i*8} Q120,{yb-110} 250,{yb-70} T500,{yb-90} L500,{yb+40} L0,{yb+40} Z" fill="{col}"/>')
        x = -5
        while x < 505:
            w, h = rnd.uniform(14, 26), rnd.uniform(18, 46)
            yy = yb - 30 + rnd.uniform(-10, 10) + i * 4
            c = rnd.choice([cream, "#e9cfa0", "#d98c5f", terra, "#efdcb4"])
            b.append(f'<rect x="{x:.1f}" y="{yy-h:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{c}"/>')
            b.append(f'<rect x="{x:.1f}" y="{yy-h:.1f}" width="{w*0.35:.1f}" height="{h:.1f}" fill="#000" opacity="0.12"/>')
            for r in range(int(h // 10)):
                b.append(f'<rect x="{x+w*0.55:.1f}" y="{yy-h+4+r*10:.1f}" width="3" height="5" fill="{navy}" opacity="0.7"/>')
            x += w
    # mare a bande
    b.append(f'<rect x="0" y="470" width="{W}" height="230" fill="{navy}"/>')
    for i in range(14):
        y = 478 + i * 9
        b.append(f'<rect x="0" y="{y}" width="{W}" height="2" fill="{sea2}" opacity="{0.9 - i*0.05:.2f}"/>')
    # transatlantico déco a sinistra
    b.append(f'<path d="M-20,505 L210,505 L185,560 L-20,560 Z" fill="{cream}"/>')
    b.append(f'<path d="M-20,532 L198,532 L190,548 L-20,548 Z" fill="{terra}"/>')
    b.append(f'<rect x="10" y="470" width="150" height="35" fill="{cream}"/><rect x="10" y="470" width="150" height="35" fill="#000" opacity="0.06"/>')
    for k in range(12):
        b.append(f'<circle cx="{20 + k*12}" cy="490" r="2.6" fill="{navy}"/>')
    for x in (40, 85, 130):
        b.append(f'<path d="M{x},470 L{x+4},420 L{x+30},420 L{x+28},470 Z" fill="{terra}"/><rect x="{x+4}" y="420" width="26" height="9" fill="{navy}"/>')
    b.append(f'<path d="M-20,560 L185,560 L180,566 L-20,566 Z" fill="#0c1826"/>')
    # Lanterna: due torri quadrate sullo scoglio
    b.append(f'<path d="M265,700 L285,520 Q330,500 390,506 L420,700 Z" fill="#3b3128"/>')
    b.append(f'<path d="M285,520 Q330,500 390,506 L395,540 Q330,530 282,548 Z" fill="#584a3c"/>')
    b.append(f'<rect x="300" y="350" width="62" height="160" fill="{cream}"/><rect x="300" y="350" width="22" height="160" fill="#cdb48c"/>')
    b.append(f'<rect x="309" y="230" width="44" height="120" fill="{cream}"/><rect x="309" y="230" width="16" height="120" fill="#cdb48c"/>')
    for y, w, x in ((346, 70, 296), (226, 52, 305), (505, 70, 296)):
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="7" fill="{terra}"/>')
    for k in range(3):
        b.append(f'<rect x="327" y="{380 + k*38}" width="10" height="18" fill="{navy}"/>')
        b.append(f'<rect x="328" y="{252 + k*30}" width="7" height="13" fill="{navy}"/>')
    b.append(f'<rect x="318" y="196" width="26" height="30" fill="{gold}"/><rect x="315" y="192" width="32" height="5" fill="{navy}"/>')
    b.append(f'<path d="M313,192 L349,192 L331,170 Z" fill="{navy}"/><rect x="330" y="160" width="2" height="12" fill="{navy}"/>')
    b.append(f'<polygon points="{P([(331, 210), (520, 120), (520, 300)])}" fill="{gold}" opacity="0.22"/>')
    b.append(f'<polygon points="{P([(331, 210), (-20, 150), (-20, 230)])}" fill="{gold}" opacity="0.12"/>')
    # gabbiani
    for gx, gy in ((120, 150), (150, 128), (430, 340)):
        b.append(f'<path d="M{gx-10},{gy} q5,-6 10,0 q5,-6 10,0" fill="none" stroke="{navy}" stroke-width="1.8"/>')
    art = f'<g filter="url(#rough)">{"".join(b)}</g>'
    # titolo déco
    t = (f'<rect x="14" y="14" width="{W-28}" height="118" fill="{navy}" opacity="0.92"/>'
         + text(250, 98, "GENOVA", "'Bodoni Moda', serif", 82, cream, 10, 800)
         + text(250, 122, "LA SUPERBA", "Jost, sans-serif", 12, gold, 9, 500)
         + f'<rect x="30" y="30" width="440" height="86" fill="none" stroke="{gold}" stroke-width="1"/>'
         + text(250, 672, "RIVIERA LIGURE · ITALIA", "Jost, sans-serif", 12, cream, 6, 500)
         + text(476, 690, "LIVE RIVIERA", "Jost, sans-serif", 7, gold, 3, 600, anchor="end"))
    defs = grad("gsky", [(0, "#e7b46a"), (0.55, "#f3d9a4"), (1, "#f1e3c2")])
    return page(art + t, defs, seed=11)


# ------------------------------------------------- 2. PORTOFINO rétro anni '60

def portofino():
    rnd = random.Random(12)
    b = [f'<rect width="{W}" height="{H}" fill="url(#psky)"/>']
    # promontorio con castello e chiesa
    b.append('<path d="M250,372 Q300,215 420,205 Q500,205 530,250 L530,372 Z" fill="#46744a"/>')
    b.append('<path d="M300,372 Q350,268 450,262 Q510,266 530,300 L530,372 Z" fill="#5b8a52"/>')
    for k in range(26):
        x = rnd.uniform(330, 510); y = rnd.uniform(250, 350)
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rnd.uniform(6, 13):.1f}" fill="#2f5638" opacity="0.8"/>')
    b.append('<rect x="392" y="186" width="44" height="24" fill="#f0c66a"/><polygon points="388,186 440,186 414,172" fill="#a5452c"/>'
             '<rect x="428" y="158" width="11" height="30" fill="#f0c66a"/><polygon points="426,158 441,158 433.5,144" fill="#a5452c"/>')
    # piazzetta: facciate alte con persiane e finestre dipinte
    cols = ["#e7a34f", "#d4613d", "#f1c35d", "#e98a63", "#bf4a35", "#f2dcac", "#e5b07c", "#f5c79a"]
    x = -10
    while x < 330:
        w, h = rnd.uniform(34, 50), rnd.uniform(130, 190)
        base = 360
        c = rnd.choice(cols)
        b.append(f'<rect x="{x:.1f}" y="{base-h:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{c}"/>')
        b.append(f'<rect x="{x+w-7:.1f}" y="{base-h:.1f}" width="7" height="{h:.1f}" fill="#000" opacity="0.1"/>')
        b.append(f'<path d="M{x-2:.1f},{base-h:.1f} L{x+w+2:.1f},{base-h:.1f} L{x+w-3:.1f},{base-h-8:.1f} L{x+3:.1f},{base-h-8:.1f} Z" fill="#8f3f2a"/>')
        for r in range(int((h - 30) // 24)):
            for cc in range(int(w // 16)):
                wx, wy = x + 7 + cc * 16, base - h + 14 + r * 24
                b.append(f'<rect x="{wx:.1f}" y="{wy:.1f}" width="9" height="13" fill="#2d5a3d"/><rect x="{wx+4:.1f}" y="{wy:.1f}" width="1" height="13" fill="#1d3a28"/>')
                b.append(f'<rect x="{wx-1:.1f}" y="{wy-2:.1f}" width="11" height="2" fill="#fff" opacity="0.45"/>')
        x += w
    b.append('<rect x="-10" y="356" width="340" height="12" fill="#c9b48e"/>')
    for k in range(6):
        b.append(f'<path d="M{20+k*52},356 l12,-16 l12,16 Z" fill="{["#c94f3b", "#f4ecdc"][k % 2]}"/><rect x="{31+k*52}" y="340" width="2" height="16" fill="#555"/>')
    # acqua
    b.append('<rect x="0" y="366" width="500" height="334" fill="url(#psea)"/>')
    for k in range(40):
        y = rnd.uniform(375, 690)
        b.append(f'<path d="M{rnd.uniform(-20, 480):.1f},{y:.1f} q10,-3 20,0 t20,0" fill="none" stroke="#e8f6f7" stroke-width="1.4" opacity="{rnd.uniform(0.3, 0.7):.2f}"/>')
    # riflessi delle case
    for k in range(14):
        b.append(f'<rect x="{rnd.uniform(0, 320):.1f}" y="372" width="{rnd.uniform(6, 16):.1f}" height="{rnd.uniform(25, 70):.1f}" fill="{rnd.choice(cols)}" opacity="0.25"/>')
    # gozzi ormeggiati
    for gx, gy, c in ((40, 395, "#f4ecdc"), (120, 405, "#2d6e9a"), (220, 392, "#c94f3b")):
        b.append(f'<path d="M{gx},{gy} L{gx+44},{gy} L{gx+37},{gy+9} L{gx+6},{gy+9} Z" fill="{c}"/><rect x="{gx+2}" y="{gy-2}" width="40" height="2" fill="#8a5a3a"/>')
    # motoscafo in mogano con la signora alla guida
    b.append('<path d="M-30,612 Q120,590 300,540 Q380,520 430,522 L440,526 Q400,560 300,592 Q140,640 -30,660 Z" fill="#fbf7ee" opacity="0.85"/>')  # scia
    hull = "M-40,560 L380,498 Q430,494 452,508 Q430,530 380,548 L-40,640 Z"
    b.append(f'<path d="{hull}" fill="url(#mahog)"/>')
    for k in range(5):
        y0 = 572 + k * 13
        b.append(f'<path d="M-40,{y0} L{400 - k*12},{512 + k*7}" stroke="#d68a52" stroke-width="0.9" opacity="0.6"/>')
    b.append('<path d="M-40,560 L380,498 Q430,494 452,508 L446,512 Q420,503 380,506 L-40,570 Z" fill="#f6efe2"/>')
    # ponte in mogano con le giunture chiare
    b.append('<path d="M-40,548 L380,490 Q425,488 450,504 L380,498 L-40,560 Z" fill="#7a2f17"/>')
    for k in range(4):
        b.append(f'<path d="M-40,{550 + k*2.6} L{380 + k*14},{491 + k*3}" stroke="#f3e2c4" stroke-width="0.6"/>')
    # parabrezza
    b.append('<path d="M222,516 L238,486 L292,476 L300,505 Z" fill="#bfe3ef" opacity="0.75"/><path d="M222,516 L238,486 L292,476 L300,505" fill="none" stroke="#e9e9e9" stroke-width="2.4"/>')
    # signora: foulard rosso al vento, occhiali da sole, abito bianco
    skin = "#ecc9a4"
    b.append('<path d="M206,482 Q236,488 252,500" stroke="%s" stroke-width="5.5" fill="none" stroke-linecap="round"/>' % skin)   # braccio
    b.append('<ellipse cx="258" cy="500" rx="9" ry="5" fill="none" stroke="#2a2a2a" stroke-width="2"/>')                           # volante
    b.append('<path d="M174,530 Q172,488 190,474 Q202,468 214,472 Q228,484 228,530 Z" fill="#fbf8f1"/>')                         # abito
    b.append('<path d="M190,474 Q202,486 214,472" fill="none" stroke="#e3d6c0" stroke-width="1.5"/>')
    b.append('<rect x="198" y="452" width="11" height="20" fill="%s"/>' % skin)                                                     # collo
    b.append('<path d="M190,454 Q180,432 196,424 Q214,418 222,434 L219,448 Q206,440 197,456 Z" fill="#3b2618"/>')                  # capelli
    b.append('<path d="M205,428 Q222,426 224,442 L227,446 L223,448 Q222,456 214,458 Q204,458 202,448 Z" fill="%s"/>' % skin)       # viso di profilo
    b.append('<path d="M188,440 Q188,418 208,416 Q224,418 224,432 Q206,424 194,444 Z" fill="#c62f2f"/>')                         # foulard
    b.append('<path d="M190,442 Q160,440 126,424 Q150,450 188,452 Z" fill="#c62f2f"/><path d="M188,446 Q166,456 146,452" stroke="#c62f2f" stroke-width="3.5" fill="none"/>')
    b.append('<path d="M210,437 L226,437 L225,443 L211,443 Z" fill="#1d1d1d"/>')                                                  # occhiali
    b.append('<path d="M219,452 q3,1 5,-1" stroke="#b5413b" stroke-width="1.8" fill="none"/><circle cx="204" cy="450" r="1.6" fill="#f4d36a"/>')
    # bandierina a poppa
    b.append('<rect x="30" y="520" width="2" height="34" fill="#888"/><path d="M32,520 l18,4 l-18,5 Z" fill="#2e7d4f"/><path d="M32,529 l18,0 l-18,0" fill="#fff"/>')
    art = f'<g filter="url(#rough)">{"".join(b)}</g>'
    t = (text(250, 92, "PORTOFINO", "Jost, sans-serif", 70, "#fbf4e6", 6, 600,
              extra='stroke="#1f4f6e" stroke-width="1.2" paint-order="stroke"')
         + text(250, 118, "RIVIERA LIGURE · ITALIA", "Jost, sans-serif", 12, "#1f4f6e", 6, 600)
         + text(476, 684, "LIVE RIVIERA", "Jost, sans-serif", 7, "#fbf4e6", 3, 600, anchor="end"))
    defs = (grad("psky", [(0, "#86c6e3"), (1, "#f4ecd7")])
            + grad("psea", [(0, "#2f88ad"), (1, "#16557a")])
            + grad("mahog", [(0, "#a8481f"), (1, "#5e2210")]))
    return page(art + t, defs, seed=12)


# --------------------------------------------------- 3. CAMOGLI acquerello

def camogli():
    rnd = random.Random(13)
    wc = 'filter="url(#wc)" style="mix-blend-mode:multiply"'
    b = ['<rect width="500" height="700" fill="#f5eedf"/>']
    b.append(f'<rect x="-20" y="-20" width="540" height="300" fill="#b9d7e6" {wc} opacity="0.75"/>')
    b.append(f'<rect x="-20" y="150" width="540" height="140" fill="#f2d3b0" {wc} opacity="0.45"/>')
    b.append(f'<path d="M-20,260 Q120,180 260,220 Q380,250 520,190 L520,330 L-20,330 Z" fill="#9db58a" {wc} opacity="0.8"/>')
    # case alte di Camogli in acquerello
    cols = ["#e9a868", "#de7a57", "#f0c870", "#e89a7e", "#cf6a4f", "#f3dcb4", "#e7b98c"]
    x = -10
    while x < 520:
        w, h = rnd.uniform(30, 44), rnd.uniform(140, 200)
        b.append(f'<rect x="{x:.1f}" y="{400-h:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{rnd.choice(cols)}" filter="url(#wc)" opacity="0.97"/>')
        for r in range(int((h - 20) // 22)):
            for cc in range(int(w // 14)):
                b.append(f'<rect x="{x+6+cc*14:.1f}" y="{400-h+12+r*22:.1f}" width="5" height="10" fill="#4e7a5a" opacity="0.55" filter="url(#rough)"/>')
        x += w - 2
    # basilica con cupola
    b.append(f'<path d="M370,400 L370,300 Q405,262 440,300 L440,400 Z" fill="#f0dab0" {wc}/>')
    b.append(f'<rect x="446" y="250" width="22" height="150" fill="#f0dab0" {wc}/><path d="M444,250 L470,250 L457,228 Z" fill="#b8644a" {wc}/>')
    # mare a pennellate
    b.append(f'<rect x="-20" y="398" width="540" height="140" fill="#5d9cc0" {wc} opacity="0.85"/>')
    b.append(f'<rect x="-20" y="440" width="540" height="100" fill="#3f7ea6" {wc} opacity="0.55"/>')
    for k in range(18):
        y = rnd.uniform(410, 520)
        b.append(f'<path d="M{rnd.uniform(0, 470):.0f},{y:.0f} l{rnd.uniform(14, 40):.0f},0" stroke="#fff" stroke-width="1.6" opacity="0.6" filter="url(#rough)"/>')
    # spiaggia
    b.append(f'<path d="M-20,520 Q250,500 520,525 L520,720 L-20,720 Z" fill="#ecd6ab" {wc}/>')
    for k in range(200):
        b.append(f'<circle cx="{rnd.uniform(0, 500):.0f}" cy="{rnd.uniform(530, 690):.0f}" r="{rnd.uniform(0.6, 1.6):.1f}" fill="#b89b70" opacity="0.5"/>')
    # ombrelloni a righe blu
    def umb(x, y, r, c):
        out = [f'<rect x="{x-1}" y="{y - r*0.5:.0f}" width="2.2" height="{r*2.3:.0f}" fill="#6b5a48"/>']
        ax, ay, n = x, y - r * 0.62, 8
        for i in range(n):
            x0, x1 = x - r + i * 2 * r / n, x - r + (i + 1) * 2 * r / n
            y0 = y + 0.06 * r * (1 - ((x0 - x) / r) ** 2)
            y1 = y + 0.06 * r * (1 - ((x1 - x) / r) ** 2)
            mx = (x0 + x1) / 2
            bulge = -0.18 * r * (1 if mx < x else -1)
            out.append(f'<path d="M{ax:.1f},{ay:.1f} Q{(ax+x0)/2 + bulge:.1f},{(ay+y0)/2 - r*0.12:.1f} {x0:.1f},{y0:.1f} '
                       f'Q{mx:.1f},{(y0+y1)/2 + r*0.1:.1f} {x1:.1f},{y1:.1f} Q{(ax+x1)/2 + bulge:.1f},{(ay+y1)/2 - r*0.12:.1f} {ax:.1f},{ay:.1f} Z" '
                       f'fill="{c if i % 2 == 0 else "#fbf7ee"}" filter="url(#rough)"/>')
        return "".join(out)
    b.append(umb(110, 540, 52, "#2f5fa0") + umb(400, 560, 44, "#2f5fa0") + umb(270, 520, 30, "#c9583e"))
    # signora sul telo, di spalle, con cappello di paglia
    b.append(f'<path d="M150,640 L330,622 L340,664 L150,684 Z" fill="#d9573f" {wc}/>')
    b.append('<path d="M220,642 Q222,600 240,592 Q262,596 266,640 Z" fill="#fbf7ee"/>')
    b.append('<path d="M236,592 Q244,588 250,594" fill="#e2bd98"/>')
    b.append('<ellipse cx="244" cy="582" rx="30" ry="9" fill="#e8cf8f"/><ellipse cx="244" cy="576" rx="14" ry="11" fill="#e8cf8f"/><rect x="230" y="577" width="28" height="3" fill="#2a2a2a"/>')
    b.append('<path d="M220,630 Q205,640 200,652" stroke="#e2bd98" stroke-width="5" fill="none"/><rect x="190" y="646" width="20" height="13" fill="#f6f1e6" transform="rotate(-12 200 652)"/>')
    art = "".join(b)
    t = (text(250, 96, "C A M O G L I", "'Cormorant Garamond', serif", 50, "#2b4a63", 6, 500)
         + text(250, 124, "Riviera di Levante · Italia", "'Cormorant Garamond', serif", 15, "#7a5a44", 2, 500, style='font-style="italic"')
         + text(476, 686, "LIVE RIVIERA", "Jost, sans-serif", 7, "#2b4a63", 3, 600, anchor="end"))
    return page(art + t, "", seed=13, border="#f5eedf")


# ------------------------------------------------ 4. SANREMO rétro in bici

def sanremo():
    rnd = random.Random(14)
    b = ['<rect width="500" height="700" fill="url(#ssky)"/>']
    b.append('<path d="M-10,280 Q90,200 200,230 Q320,260 520,190 L520,330 L-10,330 Z" fill="#87a273"/>')
    # la Pigna sulla collina
    for i in range(7):
        y, half = 320 - i * 14, 110 - i * 14
        x = 140 - half
        while x < 140 + half:
            w = rnd.uniform(8, 13)
            b.append(f'<rect x="{x:.1f}" y="{y-12:.1f}" width="{w:.1f}" height="13" fill="{rnd.choice(["#f2c993", "#e9a678", "#f4dfb0", "#d98b66"])}"/>')
            x += w
    b.append('<rect x="134" y="200" width="12" height="28" fill="#f4dfb0"/><path d="M134,200 Q140,186 146,200 Z" fill="#3c6b4a"/>')
    # Casinò
    b.append('<rect x="300" y="250" width="160" height="80" fill="#fbf4e3"/><path d="M350,250 Q380,212 410,250 Z" fill="#fbf4e3"/>'
             '<path d="M300,250 Q314,234 328,250 Z M432,250 Q446,234 460,250 Z" fill="#fbf4e3"/>')
    for k in range(7):
        b.append(f'<rect x="{310+k*21}" y="268" width="9" height="22" fill="#8bb2cc"/><rect x="{310+k*21}" y="300" width="9" height="22" fill="#8bb2cc"/>')
    # mare
    b.append('<rect x="-10" y="322" width="520" height="70" fill="#2e8ab4"/>')
    for k in range(20):
        b.append(f'<path d="M{rnd.uniform(0, 480):.0f},{rnd.uniform(330, 385):.0f} l{rnd.uniform(10, 26):.0f},0" stroke="#e7f5f8" stroke-width="1.2" opacity="0.7"/>')
    b.append('<path d="M400,352 l0,-30 l16,28 Z" fill="#fbf4e3"/><path d="M386,354 l38,0 l-6,6 l-28,0 Z" fill="#c94f3b"/>')
    # lungomare in prospettiva
    b.append('<path d="M-10,392 L520,392 L520,700 L-10,700 Z" fill="#e7cfa6"/>')
    b.append('<path d="M-10,392 L520,392 L520,400 L-10,400 Z" fill="#f6ecd8"/>')
    for k in range(13):
        b.append(f'<rect x="{k*40-10}" y="400" width="4" height="16" fill="#f6ecd8"/>')
    b.append('<path d="M-10,416 L520,416 L520,422 L-10,422 Z" fill="#f6ecd8"/>')
    b.append('<path d="M-10,600 L520,560 L520,700 L-10,700 Z" fill="#d6b98c"/>')
    # aiuole di fiori
    for k in range(70):
        x, y = rnd.uniform(-10, 510), rnd.uniform(600, 690) - 0.08 * rnd.uniform(0, 500)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(3, 6):.1f}" fill="{rnd.choice(["#e0457b", "#f2c45a", "#f07a3a", "#c9356a", "#fbf6ea"])}"/>')
    b.append(palm(40, 470, 230, 14, s=1.1) + palm(470, 440, 200, -10, s=1.0))
    # ciclista con cesto di fiori
    wheel = lambda cx, cy: (f'<circle cx="{cx}" cy="{cy}" r="34" fill="none" stroke="#2a2a2a" stroke-width="3.5"/>'
                            + "".join(f'<line x1="{cx}" y1="{cy}" x2="{cx+34*math.cos(math.radians(a)):.1f}" y2="{cy+34*math.sin(math.radians(a)):.1f}" stroke="#555" stroke-width="0.7"/>' for a in range(0, 360, 30)))
    b.append(wheel(170, 560) + wheel(310, 560))
    b.append('<path d="M170,560 L225,560 L282,500 L210,500 Z M225,560 L205,488 M282,500 L310,560 M282,500 L286,478" fill="none" stroke="#2d6e9a" stroke-width="5" stroke-linejoin="round"/>')
    b.append('<path d="M196,486 l22,0" stroke="#3a2a1a" stroke-width="5" stroke-linecap="round"/><path d="M276,478 l20,-4" stroke="#2a2a2a" stroke-width="3.5" stroke-linecap="round"/>')
    b.append('<path d="M290,470 L332,470 L326,500 L296,500 Z" fill="#c99a5a"/>')
    for k in range(12):
        b.append(f'<circle cx="{294 + rnd.uniform(0, 36):.0f}" cy="{470 - rnd.uniform(0, 14):.0f}" r="{rnd.uniform(4, 6.5):.1f}" fill="{rnd.choice(["#e0457b", "#f2c45a", "#c9356a", "#f07a3a", "#fbf6ea"])}"/>')
    b.append('<path d="M190,486 Q196,420 226,404 Q252,400 262,430 L270,470 L206,490 Z" fill="#f2c45a"/>')        # abito
    b.append('<path d="M210,486 Q236,500 230,530 L222,560" stroke="#e8c6a2" stroke-width="7" fill="none" stroke-linecap="round"/>')  # gamba
    b.append('<path d="M230,530 Q240,520 226,560" fill="#f2c45a"/>')
    b.append('<path d="M242,420 Q266,440 288,474" stroke="#e8c6a2" stroke-width="6" fill="none" stroke-linecap="round"/>')  # braccio
    b.append('<circle cx="236" cy="386" r="16" fill="#eccaa4"/><path d="M222,380 Q236,360 252,378 Z" fill="#5a3a24"/>')
    b.append('<ellipse cx="234" cy="372" rx="34" ry="8" fill="#e8cf8f"/><ellipse cx="234" cy="366" rx="16" ry="10" fill="#e8cf8f"/><rect x="218" y="366" width="32" height="3" fill="#c94f3b"/>')
    b.append('<path d="M206,374 Q186,382 176,398" stroke="#c94f3b" stroke-width="3" fill="none"/>')
    b.append('<rect x="240" y="384" width="13" height="5" rx="2.5" fill="#1d1d1d"/>')
    art = f'<g filter="url(#rough)">{"".join(b)}</g>'
    t = (text(250, 110, "SANREMO", "Jost, sans-serif", 76, "#c62f5d", 6, 600, extra='stroke="#fff6e8" stroke-width="2" paint-order="stroke"')
         + text(250, 140, "RIVIERA DEI FIORI · ITALIA", "Jost, sans-serif", 12, "#2b4a63", 6, 600)
         + text(476, 684, "LIVE RIVIERA", "Jost, sans-serif", 7, "#2b4a63", 3, 600, anchor="end"))
    defs = grad("ssky", [(0, "#f7c9a5"), (0.6, "#fbe6cc"), (1, "#fdf0dc")])
    return page(art + t, defs, seed=14)


# ---------------------------------------------- 5. NICE acquerello, sedia blu

def nice():
    rnd = random.Random(15)
    wc = 'filter="url(#wc)" style="mix-blend-mode:multiply"'
    b = ['<rect width="500" height="700" fill="#f6efe2"/>']
    b.append(f'<rect x="-20" y="-20" width="540" height="330" fill="#f2b9a0" {wc} opacity="0.6"/>')
    b.append(f'<rect x="-20" y="-20" width="540" height="170" fill="#c9d9ea" {wc} opacity="0.8"/>')
    b.append(f'<circle cx="360" cy="250" r="44" fill="#f6c86a" {wc}/>')
    # Baie des Anges e colline
    b.append(f'<path d="M-20,300 Q60,240 140,262 Q200,276 250,270 L250,320 L-20,320 Z" fill="#8a9fb8" {wc} opacity="0.7"/>')
    b.append(f'<path d="M-20,316 Q120,300 250,312 L250,330 L-20,330 Z" fill="#e8c9a8" {wc}/>')
    x = -10
    while x < 230:
        w = rnd.uniform(14, 22)
        b.append(f'<rect x="{x:.0f}" y="{300 - rnd.uniform(6, 20) + x*0.03:.0f}" width="{w:.0f}" height="20" fill="{rnd.choice(["#f5e1c4", "#f2c9a8", "#fbefe0"])}" {wc}/>')
        x += w
    b.append(f'<rect x="-20" y="318" width="540" height="240" fill="#3f8fb8" {wc} opacity="0.85"/>')
    b.append(f'<rect x="-20" y="318" width="540" height="40" fill="#f2b9a0" {wc} opacity="0.35"/>')
    b.append(f'<path d="M330,330 L390,330 L420,520 L300,520 Z" fill="#fbe7b0" filter="url(#wc)" opacity="0.35"/>')
    for k in range(20):
        b.append(f'<path d="M{rnd.uniform(0, 470):.0f},{rnd.uniform(340, 540):.0f} l{rnd.uniform(14, 40):.0f},0" stroke="#fff" stroke-width="1.6" opacity="0.6" filter="url(#rough)"/>')
    # Promenade e ringhiera
    b.append(f'<rect x="-20" y="540" width="540" height="180" fill="#e7d4b4" {wc}/>')
    b.append('<rect x="-20" y="536" width="540" height="5" fill="#fbf7ef"/>')
    for k in range(26):
        b.append(f'<rect x="{k*20}" y="541" width="3" height="16" fill="#fbf7ef"/>')
    # sedia blu con signore di spalle e cappello
    blue = "#2c63b0"
    b.append(f'<path d="M160,640 L170,520 L330,520 L340,640" fill="none" stroke="{blue}" stroke-width="9" stroke-linejoin="round" {wc}/>')
    b.append(f'<path d="M150,600 L350,600 L346,640 L154,640 Z" fill="{blue}" {wc}/>')
    b.append(f'<path d="M160,640 L150,700 M340,640 L350,700" stroke="{blue}" stroke-width="9" {wc}/>')
    for k in range(5):
        b.append(f'<rect x="{176}" y="{528 + k*14}" width="148" height="9" fill="{blue}" {wc}/>')
    b.append('<path d="M200,596 Q198,520 250,506 Q302,520 300,596 Z" fill="#f4f0e8"/>')
    b.append('<rect x="238" y="486" width="24" height="24" fill="#e0b48e"/>')
    b.append('<circle cx="250" cy="474" r="22" fill="#4a3324"/>')
    b.append('<ellipse cx="250" cy="462" rx="54" ry="13" fill="#ead39a"/><ellipse cx="250" cy="452" rx="25" ry="17" fill="#ead39a"/><rect x="226" y="456" width="48" height="4" fill="#2c3e50"/>')
    art = "".join(b)
    t = (text(250, 90, "N I C E", "'Cormorant Garamond', serif", 58, "#2c4a6e", 8, 500)
         + text(250, 120, "La Baie des Anges · Côte d'Azur", "'Cormorant Garamond', serif", 15, "#8a5a44", 2, 500, style='font-style="italic"')
         + text(476, 686, "LIVE RIVIERA", "Jost, sans-serif", 7, "#2c4a6e", 3, 600, anchor="end"))
    return page(art + t, "", seed=15, border="#f6efe2")


# ------------------------------------------ 6. MENTON linoleografia 3 colori

def menton():
    rnd = random.Random(16)
    yel, green, terra, navy, cream = "#f2b81f", "#1f5a3d", "#c8553a", "#1d3b5a", "#f3e7cc"
    ink = 'filter="url(#ink)"'
    b = [f'<rect width="500" height="700" fill="{cream}"/>']
    # sole a righe
    b.append(f'<circle cx="250" cy="250" r="120" fill="{yel}" {ink}/>')
    for k in range(9):
        b.append(f'<rect x="120" y="{180 + k*16}" width="260" height="5" fill="{cream}"/>')
    # città vecchia a gradoni (terracotta su crema)
    for i in range(7):
        y, half = 420 - i * 22, 230 - i * 26
        x = 250 - half
        while x < 250 + half:
            w = rnd.uniform(16, 26)
            h = rnd.uniform(20, 30)
            b.append(f'<rect x="{x:.0f}" y="{y-h:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{terra if rnd.random() > 0.35 else cream}" stroke="{navy}" stroke-width="1.6" {ink}/>')
            b.append(f'<rect x="{x+w/2-2:.0f}" y="{y-h+6:.0f}" width="4" height="7" fill="{navy}"/>')
            x += w
    # campanile della Basilica
    b.append(f'<rect x="236" y="200" width="28" height="100" fill="{cream}" stroke="{navy}" stroke-width="2" {ink}/>'
             f'<path d="M232,200 Q250,160 268,200 Z" fill="{green}" {ink}/><rect x="245" y="216" width="10" height="16" fill="{navy}"/>')
    # mare a righe blu
    b.append(f'<rect x="0" y="420" width="500" height="280" fill="{navy}" {ink}/>')
    for k in range(10):
        b.append(f'<path d="M0,{436 + k*14} q25,-6 50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0 t50,0" fill="none" stroke="{cream}" stroke-width="1.5" opacity="0.8"/>')
    b.append(f'<path d="M300,470 l0,-46 l26,42 Z" fill="{cream}" {ink}/><path d="M282,472 l54,0 l-8,10 l-38,0 Z" fill="{terra}" {ink}/>')
    # ramo di limoni in primo piano (cornice)
    b.append(f'<path d="M-10,560 Q120,520 230,600 Q300,650 520,610" fill="none" stroke="#4a3020" stroke-width="9" {ink}/>')
    for lx, ly, a in [(40, 548, -20), (95, 520, 25), (150, 555, -35), (210, 585, 15), (270, 640, -10), (330, 610, 30), (400, 640, -25), (460, 600, 20), (120, 590, 50), (380, 590, -50)]:
        b.append(f'<ellipse cx="{lx}" cy="{ly}" rx="34" ry="12" fill="{green}" transform="rotate({a} {lx} {ly})" {ink}/>')
    for lx, ly in [(70, 590), (180, 620), (300, 670), (430, 655), (240, 560)]:
        b.append(f'<ellipse cx="{lx}" cy="{ly}" rx="27" ry="22" fill="{yel}" stroke="{navy}" stroke-width="2" {ink}/>'
                 f'<path d="M{lx-12},{ly-8} q6,-6 14,-4" stroke="{cream}" stroke-width="3" fill="none"/>')
    art = "".join(b)
    t = (text(250, 92, "MENTON", "'Alfa Slab One', serif", 74, navy, 4)
         + text(250, 120, "LA PERLE DE LA FRANCE · CÔTE D'AZUR", "Jost, sans-serif", 11, terra, 4, 600)
         + text(476, 686, "LIVE RIVIERA", "Jost, sans-serif", 7, navy, 3, 600, anchor="end"))
    return page(art + t, "", seed=16, border=cream)


# ---------------------------------------- 7. MONACO Grand Prix anni '50

def monaco():
    rnd = random.Random(17)
    b = ['<rect width="500" height="700" fill="url(#msky)"/>']
    b.append('<path d="M-10,250 L70,150 L150,180 L240,90 L330,170 L420,130 L520,190 L520,330 L-10,330 Z" fill="#8f7f99"/>')
    b.append('<path d="M-10,290 L90,220 L210,250 L330,210 L520,250 L520,340 L-10,340 Z" fill="#74688c"/>')
    # Monte-Carlo
    x = 260
    while x < 520:
        w, h = rnd.uniform(20, 32), rnd.uniform(50, 120)
        b.append(f'<rect x="{x:.0f}" y="{340-h:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{rnd.choice(["#fbf1df", "#f4e1c3", "#ead1b2"])}"/>')
        for r in range(int(h // 12)):
            b.append(f'<rect x="{x+3:.0f}" y="{340-h+5+r*12:.0f}" width="{w-6:.0f}" height="3" fill="#6d8fb0" opacity="0.6"/>')
        x += w + 2
    # Rocher e Palazzo
    b.append('<path d="M-10,400 L-10,300 Q40,262 150,272 Q210,280 240,320 L250,400 Z" fill="#8e6a4c"/>')
    b.append('<rect x="15" y="236" width="170" height="44" fill="#f3e3c2"/>')
    for k in range(13):
        b.append(f'<rect x="{15+k*14}" y="230" width="8" height="8" fill="#f3e3c2"/>')
    for k in range(10):
        b.append(f'<rect x="{25+k*16}" y="248" width="7" height="12" fill="#a8452c"/>')
    b.append('<rect x="92" y="196" width="2" height="34" fill="#333"/><path d="M94,196 l24,4 l-24,5 Z" fill="#d22630"/><path d="M94,205 l24,4 l-24,5 Z" fill="#fbfaf6"/>')
    # porto con yacht
    b.append('<rect x="-10" y="340" width="520" height="110" fill="#1e74ad"/>')
    for k in range(24):
        b.append(f'<path d="M{rnd.uniform(240, 500):.0f},{rnd.uniform(345, 440):.0f} l{rnd.uniform(10, 24):.0f},0" stroke="#d8eef7" stroke-width="1.2" opacity="0.7"/>')
    for yx, yy, s in ((270, 360, 1.0), (360, 380, 1.3), (300, 410, 1.6), (430, 400, 1.2)):
        b.append(f'<path d="M{yx},{yy} l{60*s:.0f},0 l{-8*s:.0f},{9*s:.0f} l{-46*s:.0f},0 Z" fill="#fbfaf6"/><rect x="{yx+14*s:.0f}" y="{yy-8*s:.0f}" width="{30*s:.0f}" height="{8*s:.0f}" fill="#fbfaf6"/><rect x="{yx+18*s:.0f}" y="{yy-6*s:.0f}" width="{22*s:.0f}" height="{3*s:.0f}" fill="#1e3a5a"/>')
    # strada del circuito in curva con cordoli
    b.append('<path d="M-10,470 Q250,430 520,470 L520,700 L-10,700 Z" fill="#54565a"/>')
    b.append('<path d="M-10,450 Q250,412 520,450 L520,470 Q250,430 -10,470 Z" fill="#fbf7ef"/>')
    for k in range(13):
        b.append(f'<rect x="{k*42-10}" y="{452 + abs(k*42-250)*0.06:.0f}" width="21" height="8" fill="#d22630"/>')
    for k in range(10):
        b.append(f'<path d="M{rnd.uniform(-10, 160):.0f},{rnd.uniform(540, 640):.0f} l{rnd.uniform(60, 140):.0f},{rnd.uniform(-6, 6):.0f}" stroke="#d9d9d9" stroke-width="2" opacity="0.6"/>')
    # monoposto rossa anni '50
    car = ('<path d="M150,600 Q170,560 260,552 L400,552 Q450,556 470,580 Q474,600 450,606 L170,612 Q150,612 150,600 Z" fill="url(#car)"/>'
           '<path d="M300,552 Q316,532 344,534 L356,552 Z" fill="#bfe1ee" opacity="0.85"/>'
           '<circle cx="330" cy="538" r="12" fill="#f0e6d2"/><rect x="320" y="530" width="20" height="7" rx="3" fill="#2b2b2b"/>'
           '<path d="M318,530 Q330,516 342,530 Z" fill="#fbfaf6"/>'
           '<circle cx="240" cy="580" r="18" fill="#fbfaf6"/><text x="240" y="587" text-anchor="middle" font-family="Jost, sans-serif" font-weight="600" font-size="19" fill="#1d1d1d">7</text>'
           '<path d="M450,570 L478,566 L478,596 L456,596 Z" fill="#9c1b20"/>'
           '<circle cx="210" cy="614" r="27" fill="#1a1a1a"/><circle cx="210" cy="614" r="11" fill="#bdbdbd"/>'
           '<circle cx="420" cy="614" r="27" fill="#1a1a1a"/><circle cx="420" cy="614" r="11" fill="#bdbdbd"/>')
    b.append(car)
    for k in range(6):
        b.append(f'<rect x="{40 + rnd.uniform(-20, 20):.0f}" y="{562 + k*10}" width="{rnd.uniform(60, 110):.0f}" height="2.4" fill="#fbf7ef" opacity="0.8"/>')
    art = f'<g filter="url(#rough)">{"".join(b)}</g>'
    t = (text(250, 106, "MONACO", "'Racing Sans One', sans-serif", 92, "#d22630", 4, extra='stroke="#fbf4e6" stroke-width="2" paint-order="stroke"')
         + text(250, 134, "MONTE-CARLO · CÔTE D'AZUR", "Jost, sans-serif", 12, "#1e3a5a", 6, 600)
         + text(476, 686, "LIVE RIVIERA", "Jost, sans-serif", 7, "#fbf4e6", 3, 600, anchor="end"))
    defs = (grad("msky", [(0, "#f6a98a"), (0.5, "#fbd3a8"), (1, "#fde8cc")])
            + grad("car", [(0, "#e5333a"), (1, "#8f151b")]))
    return page(art + t, defs, seed=17)


POSTERS = {
    "01-genova": genova, "02-portofino": portofino, "03-camogli": camogli, "04-sanremo": sanremo,
    "05-nice": nice, "06-menton": menton, "07-monaco": monaco,
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in POSTERS.items():
        (OUT / f"{name}.svg").write_text(fn())
        print(name)
