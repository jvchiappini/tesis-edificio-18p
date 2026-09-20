"""
====================================================================
 DISEÑO DE LOSAS NERVADAS — PANEL POR PANEL (TODOS LOS NIVELES)
 Edificio de Uso Mixto 18P + 2 Subsuelos | Ciudad del Este, Paraguay
====================================================================

 Enumeracion y diseno de TODOS los paneles de losa nervada de la
 grilla (12 ejes X x 6 ejes Y = 55 celdas por nivel) para S1, S2, S3,
 PB, P01-P18 y AZ.

 Para cada panel:
   - Dimensiones (lx, ly) y condicion de cada uno de los 4 bordes:
       S = spandrel (viga perimetral 25x50)
       N = nucleo H°A° (muro)
       P = borde contra hueco/vacio (viga de borde de pozo 20x40)
       C = continuo (losa hacia panel vecino)
   - Huecos: pozos de luz A/B (P01-P18 y AZ) y VACIO CENTRAL entre
     nucleos X:41->49 / Y:17->26 (P01-P18, decision 2026-09-11).
   - Cargas por zona (residencial, cocheras, comercial, azotea).
   - Diseno: reparto bidireccional de carga (qx+qy=q), franja de un
     modulo (0.60 m) como viga continua de 2 vanos (coeficientes
     conservadores M- = wL2/8, M+ = 9wL2/128), As por nervio en cada
     direccion, corte y estribos.

 METODO (decisión 2026-09-11): los paneles con hueco interior
 (ANILLO) se disenan conservadoramente con las dimensiones de la
 celda y borde P hacia el hueco; la verificacion exacta del anillo y
 el emparrillado se documentan como paso posterior (PyNite/CYPE).

 OUTPUTS (calculo/outputs/):
   - paneles_losas.csv          -> tabla panel por panel (todos los niveles)
   - mapa_paneles_planta_tipo.png -> plano de paneles P01-P18
   - paneles_losas_resultados.json
====================================================================
"""

import csv
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelo_estructural import (XS, YS, NUCLEOS, POZOS_LUZ, LOSA_POR_NIVEL,
                                CARGAS, NIVELES)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

# ------------------------------------------------------------------
# 1. CONSTANTES
# ------------------------------------------------------------------
X_MIN, X_MAX = 2.5, 87.5
Y_MIN, Y_MAX = 3.0, 40.0

FC = 30.0
FY = 500.0
GAMMA = 25.0
PHI_FLEX = 0.90
PHI_CORT = 0.75
REC = 0.025
EST = 0.008
SEP = 0.60          # separacion de ejes de nervios
NERVIO_W = 0.10     # ancho de nervio
CAPA = 0.10

# Vacio central entre nucleos (decision 2026-09-11): P01-P18
VACIO_CENTRAL = dict(id="VC", x0=41.0, x1=49.0, y0=17.0, y1=26.0, area=72.0)

# Sobrecargas y tabiqueria por zona (NBR 6120)
ZONA_Q = {"residencial": 2.0, "cocheras": 3.0, "comercial": 3.0,
          "azotea-tecnica": 2.0}
ZONA_TABIQUERIA = {"residencial": 1.5, "comercial": 1.0, "cocheras": 0.5,
                   "azotea-tecnica": 0.5}
ACABADOS = CARGAS["acabados"]  # 1.0 kN/m2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")

NIVELES_ORDEN = ["S3", "S2", "S1", "PB"] + \
    [f"P{i:02d}" for i in range(1, 19)] + ["AZ"]


def canto_de(nid):
    return LOSA_POR_NIVEL[nid]["canto"]


def espesor_de(nid):
    return LOSA_POR_NIVEL[nid]["espesor"]


def huecos_por_nivel(nid):
    """Huecos que ocupan area (sin losa) en cada nivel: nucleos + pozos
    + vacio central (solo P01-P18)."""
    huecos = list(NUCLEOS)
    if nid in [f"P{i:02d}" for i in range(1, 19)]:
        huecos = huecos + list(POZOS_LUZ) + [VACIO_CENTRAL]
    elif nid == "AZ":
        huecos = huecos + list(POZOS_LUZ)   # claraboyas
    return huecos


def intersecta(r1, r2):
    """True si dos rectangulos [x0,y0,x1,y1] se intersectan."""
    return not (r1["x1"] <= r2["x0"] or r2["x1"] <= r1["x0"] or
                r1["y1"] <= r2["y0"] or r2["y1"] <= r1["y0"])


def dentro_de(celda, r):
    """True si la celda esta totalmente dentro del rectangulo r."""
    return (celda["x0"] >= r["x0"] - 1e-9 and celda["x1"] <= r["x1"] + 1e-9 and
            celda["y0"] >= r["y0"] - 1e-9 and celda["y1"] <= r["y1"] + 1e-9)


def punto_en_borde(px, py, r):
    """True si el punto (px,py) esta sobre el borde del rectangulo r."""
    on_x = (abs(px - r["x0"]) < 1e-6 or abs(px - r["x1"]) < 1e-6) and \
           (r["y0"] - 1e-6 <= py <= r["y1"] + 1e-6)
    on_y = (abs(py - r["y0"]) < 1e-6 or abs(py - r["y1"]) < 1e-6) and \
           (r["x0"] - 1e-6 <= px <= r["x1"] + 1e-6)
    return on_x or on_y


def clasificar_borde(px, py, huecos):
    """Clasifica un borde por su punto medio: S spandrel, N nucleo,
    P hueco (pozo/vacio), C continuo."""
    if abs(px - X_MIN) < 1e-6 or abs(px - X_MAX) < 1e-6 or \
       abs(py - Y_MIN) < 1e-6 or abs(py - Y_MAX) < 1e-6:
        return "S"
    for h in huecos:
        if h["id"].startswith("N"):     # nucleo
            if punto_en_borde(px, py, h):
                return "N"
        else:                            # pozo o vacio central
            if punto_en_borde(px, py, h):
                return "P"
    return "C"


# ------------------------------------------------------------------
# 2. DISENO DEL PANEL (misma metodologia que losas_nervadas.py)
# ------------------------------------------------------------------
def as_flexion(Mu, b, d):
    Rn = Mu / (PHI_FLEX * b * d ** 2)
    rho = (0.85 * FC / FY) * (1 - math.sqrt(1 - 2 * Rn / (0.85 * FC * 1000.0)))
    return max(rho * b * d * 1e6, 0.0)      # mm2 por nervio/franja


def disenar_panel(lx, ly, qu, canto):
    d = canto - REC - EST
    Lx4, Ly4 = lx ** 4, ly ** 4
    den = Lx4 + Ly4
    qx = qu * Ly4 / den      # carga que lleva la direccion X (vanos lx)
    qy = qu * Lx4 / den      # carga que lleva la direccion Y (vanos ly)
    wx = qx * SEP
    wy = qy * SEP
    # coeficientes conservadores de viga continua (2 vanos)
    Mx_neg, Mx_pos = wx * lx ** 2 / 8.0, 9.0 * wx * lx ** 2 / 128.0
    My_neg, My_pos = wy * ly ** 2 / 8.0, 9.0 * wy * ly ** 2 / 128.0
    Asx_neg = as_flexion(Mx_neg, NERVIO_W, d)
    Asx_pos = as_flexion(Mx_pos, SEP, d)
    Asy_neg = as_flexion(My_neg, NERVIO_W, d)
    Asy_pos = as_flexion(My_pos, SEP, d)
    as_min = max(0.25 * math.sqrt(FC) / FY, 1.4 / FY) * (NERVIO_W * d) * 1e6
    # corte (2 vanos: Vmax = 5wL/8)
    Vx = 5.0 * wx * lx / 8.0
    Vy = 5.0 * wy * ly / 8.0
    vc = 1.1 * 0.17 * math.sqrt(FC) * (NERVIO_W * d) * 1000.0
    phiVc = PHI_CORT * vc
    return dict(d=d, qx=qx, qy=qy, wx=wx, wy=wy,
                Mx_neg=Mx_neg, Mx_pos=Mx_pos, My_neg=My_neg, My_pos=My_pos,
                Asx_neg=Asx_neg, Asx_pos=Asx_pos,
                Asy_neg=Asy_neg, Asy_pos=Asy_pos,
                as_min=as_min, Vx=Vx, Vy=Vy, Vc=vc, phiVc=phiVc,
                estribos_x=(Vx > phiVc), estribos_y=(Vy > phiVc))


# ------------------------------------------------------------------
# 3. ENUMERACION DE PANELES
# ------------------------------------------------------------------
def enumerar_paneles(nid):
    huecos = huecos_por_nivel(nid)
    canto = canto_de(nid)
    espesor = espesor_de(nid)
    pp = espesor * GAMMA
    funcion = next(n["funcion"] for n in NIVELES if n["id"] == nid)
    q_uso = ZONA_Q.get(funcion, 2.0)
    tabiq = ZONA_TABIQUERIA.get(funcion, 1.0)
    g = pp + ACABADOS + tabiq
    qu = 1.4 * (g + q_uso)

    paneles = []
    n_panel = 0
    for i in range(len(XS) - 1):
        for j in range(len(YS) - 1):
            celda = dict(id=f"{nid}-{i+1}-{j+1}",
                         x0=XS[i], x1=XS[i + 1], y0=YS[j], y1=YS[j + 1],
                         lx=XS[i + 1] - XS[i], ly=YS[j + 1] - YS[j])
            n_panel += 1

            # tipo: NUCLEO (dentro de un nucleo) / VACIO / NORMAL / ANILLO
            tipo = "NORMAL"
            dentro_core = False
            con_hueco = False
            for h in huecos:
                if h["id"].startswith("N") and dentro_de(celda, h):
                    dentro_core = True
                elif not h["id"].startswith("N"):
                    if dentro_de(celda, h):
                        tipo = "VACIO"
                    elif intersecta(celda, h):
                        con_hueco = True
            if dentro_core:
                tipo = "NUCLEO"
            elif tipo == "NORMAL" and con_hueco:
                tipo = "ANILLO"

            # bordes (punto medio de cada lado)
            mxw, myw = celda["x0"], (celda["y0"] + celda["y1"]) / 2.0
            mxe, mye = celda["x1"], (celda["y0"] + celda["y1"]) / 2.0
            mxs, mys = (celda["x0"] + celda["x1"]) / 2.0, celda["y0"]
            mxn, myn = (celda["x0"] + celda["x1"]) / 2.0, celda["y1"]
            bordes = (clasificar_borde(mxw, myw, huecos) +
                      clasificar_borde(mxe, mye, huecos) +
                      clasificar_borde(mxs, mys, huecos) +
                      clasificar_borde(mxn, myn, huecos))

            fila = dict(id=celda["id"], nivel=nid,
                        x0=celda["x0"], x1=celda["x1"],
                        y0=celda["y0"], y1=celda["y1"],
                        lx=round(celda["lx"], 3), ly=round(celda["ly"], 3),
                        tipo=tipo, bordes=bordes,
                        g=round(g, 2), q=round(q_uso, 2), qu=round(qu, 2))
            if tipo in ("NORMAL", "ANILLO"):
                d = disenar_panel(celda["lx"], celda["ly"], qu, canto)
                fila.update({k: round(v, 2) if isinstance(v, float) else v
                             for k, v in d.items()})
            paneles.append(fila)
    return paneles, canto


# ------------------------------------------------------------------
# 4. SALIDAS
# ------------------------------------------------------------------
def guardar():
    os.makedirs(OUT, exist_ok=True)
    todas = []
    for nid in NIVELES_ORDEN:
        paneles, _ = enumerar_paneles(nid)
        todas.extend(paneles)

    cols = ["id", "nivel", "tipo", "bordes", "lx", "ly",
            "g", "q", "qu", "qx", "qy", "Mx_neg", "Mx_pos", "My_neg",
            "My_pos", "Asx_neg", "Asx_pos", "Asy_neg", "Asy_pos",
            "as_min", "Vx", "Vy", "Vc", "phiVc", "estribos_x", "estribos_y"]
    with open(os.path.join(OUT, "paneles_losas.csv"), "w", newline="",
              encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter=";",
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(todas)

    resumen = {}
    for t in ("NORMAL", "ANILLO", "VACIO", "NUCLEO"):
        resumen[t] = sum(1 for p in todas if p["tipo"] == t)
    with open(os.path.join(OUT, "paneles_losas_resultados.json"), "w",
              encoding="utf-8") as f:
        json.dump({"resumen": resumen, "total_paneles": len(todas),
                   "niveles": NIVELES_ORDEN}, f, ensure_ascii=False, indent=2)

    # ---- Mapa de paneles de planta tipo (P01-P18) ----
    fig, ax = plt.subplots(figsize=(12, 6.4))
    paneles, canto = enumerar_paneles("P18")
    huecos = huecos_por_nivel("P18")

    def box(r, **kw):
        return Rectangle((r["x0"], r["y0"]), r["x1"] - r["x0"],
                         r["y1"] - r["y0"], **kw)

    for p in paneles:
        if p["tipo"] == "NUCLEO":
            ax.add_patch(box(p, facecolor="#1f2937", edgecolor="#111827",
                             zorder=2))
        elif p["tipo"] == "VACIO":
            ax.add_patch(box(p, facecolor="#d1d5db", edgecolor="#9ca3af",
                             hatch="///", zorder=2))
        elif p["tipo"] == "ANILLO":
            ax.add_patch(box(p, facecolor="#fde68a", edgecolor="#f59e0b",
                             zorder=1))
        else:
            ax.add_patch(box(p, facecolor="#e0e7ff", edgecolor="#a5b4fc",
                             zorder=1))
        etiq = f"{p['bordes']}\n{p['lx']:.1f}x{p['ly']:.1f}"
        ax.text((p["x0"] + p["x1"]) / 2, (p["y0"] + p["y1"]) / 2, etiq,
                ha="center", va="center", fontsize=7, zorder=3,
                color="#111827")

    for x in XS:
        ax.axvline(x, color="#374151", lw=0.5, zorder=0)
    for y in YS:
        ax.axhline(y, color="#374151", lw=0.5, zorder=0)
    ax.set_xlim(0, 90)
    ax.set_ylim(1.5, 41.5)
    ax.set_aspect("equal")
    ax.set_title("Planta Tipo P01-P18 — Mapa de paneles de losa nervada\n"
                 "Bordes: S=spandrel · N=núcleo · P=hueco · C=continuo · "
                 "Amarillo=anillo con hueco · Gris=vacío · Gris oscuro=núcleo",
                 fontsize=10)
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.grid(False)
    fig.tight_layout()
    out_png = os.path.join(OUT, "mapa_paneles_planta_tipo.png")
    fig.savefig(out_png, dpi=150)
    plt.close(fig)

    print(f"Total paneles: {len(todas)} | {resumen}")
    print("NORMAL:", resumen["NORMAL"], "| ANILLO:", resumen["ANILLO"],
          "| VACIO:", resumen["VACIO"], "| NUCLEO:", resumen["NUCLEO"])
    print("Ejemplo planta tipo (P18):")
    for p in [p for p in todas if p["nivel"] == "P18"][:8]:
        print(" ", p["id"], p["tipo"], p["bordes"], "Asx-", p.get("Asx_neg"))
    print("CSV:", os.path.join(OUT, "paneles_losas.csv"))
    print("PNG:", out_png)


if __name__ == "__main__":
    guardar()
