"""
====================================================================
 CARGAS GRAVITATORIAS — PESO PROPIO + SOBRECARGAS + AXIAL POR PILAR
 Edificio 18P + 2 Subsuelos | CDE, Paraguay
 Normas: NBR 6120:2019 (base) · ASCE 7-22 (comparativa)
====================================================================

 Calcula TODAS las acciones verticales del edificio:
   1. Carga permanente g por nivel (peso propio losa + acabados +
      tabiquería + impermeabilizaciones).
   2. Sobrecarga de uso q por nivel (NBR 6120 Tabela 10 y ASCE 7-22
      Tabla 4.3-1) — comparativa por norma.
   3. Cargas especiales de azotea: piscina (agua + uso), tanques
      elevados (agua + estructura), salas de máquinas.
   4. Carga axial acumulada N por pilar (método de áreas tributarias)
      en cada nivel — insumo para dimensionamiento y fundaciones.

 Método de áreas tributarias:
   Para cada pilar (xi, yi), el área tributaria por nivel es el
   producto de las semi-distancias a los pilares adyacentes en X y en
   Y (hasta el borde del edificio en los bordes).

 Valores (verificado y guardado en 07.04_Normativa_Resumen):
   - Concreto armado: γ = 25 kN/m³
   - Residencial q=1,5 kN/m² (NBR) / 1,92 kN/m² (ASCE, 40 psf)
   - Comercial  q=3,0 kN/m² (NBR) / 4,79 kN/m² (ASCE, 100 psf)
   - Cocheras   q=3,0 kN/m² (NBR) / 1,92 kN/m² (ASCE, 40 psf)
   - Azotea     q=1,0 kN/m² (NBR) / 0,96 kN/m² (ASCE, 20 psf)
   - Piscina: agua 10 kN/m³ × prof. media 1,5 m ≈ 15 kN/m²
   - Tanques: 45 m³ agua / 49 m² ≈ 9,2 kN/m² + estructura ≈ 10 kN/m²

 SALIDAS:
   - outputs/tabla_cargas_nivel.csv    (g, q, g+q, peso por nivel)
   - outputs/axial_pilares.csv         (N por pilar en cada nivel)
   - outputs/carga_axial_vs_altura.png (diagrama N vs altura)
====================================================================
"""

import os
import sys
import csv
import numpy as np
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelo_estructural import HUELLA, XS, YS, NUCLEOS, NIVELES, LOSA_POR_NIVEL

GAMMA_HORMIGON = 25.0        # kN/m³  (NBR 6120)
GAMMA_AGUA = 10.0            # kN/m³

# ──────────────────────────────────────────────────────────────────
# CARGAS POR NIVEL (kN/m²)
# ──────────────────────────────────────────────────────────────────
def cargas_por_nivel():
    """Devuelve dict nivel -> dict(g, q_nbr, q_asce, nota)."""
    res = {}
    for n in NIVELES:
        nid = n["id"]
        # espesor EQUIVALENTE (m³/m²) del sistema nervurado → peso propio
        t = LOSA_POR_NIVEL.get(nid, {}).get("espesor", 0.19)
        if nid == "AZ":
            t = LOSA_POR_NIVEL["AZ"]["espesor"]
        pp_losa = t * GAMMA_HORMIGON

        if nid in ("S1", "S2", "S3"):
            g = pp_losa + 0.5                     # acabados cochera
            q_nbr, q_asce = 3.0, 1.92             # cocheras
            nota = "cocheras"
        elif nid == "PB":
            g = pp_losa + 1.5                     # acabados comercial
            q_nbr, q_asce = 3.0, 4.79             # comercial / retail 100psf
            nota = "comercial"
        elif nid == "AZ":
            g = pp_losa + 2.0                     # impermeabilización+acabado
            q_nbr, q_asce = 1.0, 0.96             # azotea mantenimiento
            nota = "azotea"
        else:
            g = pp_losa + 1.0 + 1.5               # acabados + tabiquería
            q_nbr, q_asce = 1.5, 1.92             # residencial
            nota = "residencial"

        res[nid] = dict(g=round(g, 2), q_nbr=round(q_nbr, 2),
                        q_asce=round(q_asce, 2), espesor=t, nota=nota)
    return res


# ──────────────────────────────────────────────────────────────────
# CARGAS ESPECIALES DE AZOTEA (kN/m² sobre huella de la zona)
# ──────────────────────────────────────────────────────────────────
PISCINA = dict(x0=10.25, x1=26.25, y0=29.0, y1=37.0,
               carga_agua=round(1.5 * GAMMA_AGUA, 2))   # 15,0 kN/m²
# Tanques elevados UNIDOS EN BLOQUE ÚNICO sobre núcleos N1/N2 + corredor
# (X:34→56 × Y:17→26), muro intermedio en X=45
TANQUES = [
    dict(id="POTABLE", x0=34.0, x1=45.0, y0=17.0, y1=26.0),
    dict(id="PCI",     x0=45.0, x1=56.0, y0=17.0, y1=26.0),
]
CARGA_TANQUE = 10.0   # agua 9,2 + estructura ≈ 10 kN/m²


# ──────────────────────────────────────────────────────────────────
# ÁREAS TRIBUTARIAS POR PILAR
# ──────────────────────────────────────────────────────────────────
def pilares_efectivos():
    """Mismos criterios que ga_grilla_pilares: quita pilares dentro de núcleos."""
    out = []
    for x in XS:
        for y in YS:
            dentro = any((c["x0"] + 0.90) < x < (c["x1"] - 0.90) and
                         (c["y0"] + 0.90) < y < (c["y1"] - 0.90)
                         for c in NUCLEOS)
            if not dentro:
                out.append((x, y))
    return out


def area_tributaria(x, y):
    """Producto de semi-vanos (hasta borde del edificio en bordes)."""
    ix = [i for i, v in enumerate(XS) if abs(v - x) < 1e-9][0]
    iy = [i for i, v in enumerate(YS) if abs(v - y) < 1e-9][0]
    x_izq = XS[ix - 1] if ix > 0 else HUELLA["x0"]
    x_der = XS[ix + 1] if ix < len(XS) - 1 else HUELLA["x1"]
    y_inf = YS[iy - 1] if iy > 0 else HUELLA["y0"]
    y_sup = YS[iy + 1] if iy < len(YS) - 1 else HUELLA["y1"]
    dx = (x - x_izq) / 2 + (x_der - x) / 2
    dy = (y - y_inf) / 2 + (y_sup - y) / 2
    return dx * dy


# ──────────────────────────────────────────────────────────────────
# CARGA AXIAL ACUMULADA POR PILAR
# ──────────────────────────────────────────────────────────────────
def axial_por_pilar(cargas, norma="nbr"):
    """N acumulada (kN) por pilar en cada nivel, sumando desde AZ→S3.
    Incluye peso propio de losa, cargas, y peso propio del pilar."""
    niveles = [n["id"] for n in NIVELES]          # S3..AZ (orden abajo→arriba)
    cotas = {n["id"]: n["cota"] for n in NIVELES}
    alturas = {n["id"]: n["altura"] for n in NIVELES}
    pilares = pilares_efectivos()
    areas = {p: area_tributaria(*p) for p in pilares}

    # carga por nivel sobre área tributaria
    qkey = "q_nbr" if norma == "nbr" else "q_asce"
    w_nivel = {nid: cargas[nid]["g"] + cargas[nid][qkey] for nid in niveles}

    # acumular de arriba hacia abajo
    resultados = {}
    N_acum = {p: 0.0 for p in pilares}
    for nid in reversed(niveles):
        for p in pilares:
            # peso de la losa de este nivel sobre área tributaria
            N_acum[p] += w_nivel[nid] * areas[p]
            # peso propio del pilar en el tramo de este nivel (sección provisional,
            # grupos por cota alineados con modelo_3d.py)
            ancho = 0.90 if nid in ("S1", "S2", "S3", "PB") else \
                    0.80 if cotas[nid] <= 20.75 else \
                    0.70 if cotas[nid] <= 40.85 else 0.60
            altura = alturas[nid]
            N_acum[p] += (ancho ** 2) * altura * GAMMA_HORMIGON
        resultados[nid] = {p: round(N_acum[p], 1) for p in pilares}
    return resultados, pilares, areas


# ──────────────────────────────────────────────────────────────────
# SALIDAS
# ──────────────────────────────────────────────────────────────────
def exportar_tabla_nivel(cargas, ruta):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nivel", "espesor_m", "g_kNm2", "q_nbr_kNm2",
                    "q_asce_kNm2", "gq_nbr", "gq_asce", "uso"])
        for nid, c in cargas.items():
            w.writerow([nid, c["espesor"], c["g"], c["q_nbr"], c["q_asce"],
                        round(c["g"] + c["q_nbr"], 2),
                        round(c["g"] + c["q_asce"], 2), c["nota"]])
    print(f"[OK] {ruta}")


def exportar_axial(resultados, pilares, ruta):
    niveles = list(resultados.keys())
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pilar", "x", "y"] + niveles)
        for p in pilares:
            w.writerow([f"P{p[0]:.0f}_{p[1]:.0f}", p[0], p[1]] +
                       [resultados[n][p] for n in niveles])
    print(f"[OK] {ruta}")


def graficar_axial(resultados, pilares, ruta):
    cotas = {n["id"]: n["cota"] for n in NIVELES}
    niveles = list(resultados.keys())
    N_max = {n: max(resultados[n].values()) for n in niveles}
    z = [cotas[n] for n in niveles]
    N = [N_max[n] for n in niveles]

    fig, ax = plt.subplots(figsize=(8, 11))
    ax.plot(N, z, "-o", color="#1e40af", lw=2.2, ms=5)
    ax.fill_betweenx(z, 0, N, color="#1e40af", alpha=0.15)
    ax.set_xlabel("Carga axial máxima en pilar N [kN]")
    ax.set_ylabel("Cota [m]")
    ax.set_title("CARGA AXIAL MÁXIMA POR NIVEL (áreas tributarias, NBR 6120)\n"
                 "Pilares con sección provisional (90→60 cm) · incluye peso propio",
                 fontsize=10, fontweight="bold")
    ax.grid(True, ls=":", alpha=0.5)
    for i, (niv, cota) in enumerate(zip(niveles, z)):
        ax.annotate(f"{niv}·{N[i]/1000:.0f} MN", (N[i], cota),
                    textcoords="offset points", xytext=(6, 0), fontsize=7)
    plt.tight_layout()
    plt.savefig(ruta, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {ruta}")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out, exist_ok=True)

    cargas = cargas_por_nivel()
    exportar_tabla_nivel(cargas, os.path.join(out, "tabla_cargas_nivel.csv"))

    resultados_nbr, pilares, areas = axial_por_pilar(cargas, norma="nbr")
    exportar_axial(resultados_nbr, pilares, os.path.join(out, "axial_pilares.csv"))
    graficar_axial(resultados_nbr, pilares, os.path.join(out, "carga_axial_vs_altura.png"))

    # Resumen
    N_max_base = max(resultados_nbr["S3"].values())
    N_max_az = max(resultados_nbr["AZ"].values())
    print(f"     Pilares: {len(pilares)} | N máx en S3 (base): {N_max_base/1000:.1f} MN")
    print(f"     N en azotea: {N_max_az/1000:.1f} MN | N por pilar en PB: "
          f"{max(resultados_nbr['PB'].values())/1000:.1f} MN")
