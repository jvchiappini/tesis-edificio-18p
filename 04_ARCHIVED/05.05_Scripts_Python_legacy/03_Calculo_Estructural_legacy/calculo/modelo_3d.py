"""
====================================================================
 MODELO 3D ESTRUCTURAL — EDIFICIO 18P + 2 Subsuelos (CDE, Paraguay)
 Metodología BIM ISO 19650 | AGENTS.md §10 · modelo_estructural.py
====================================================================

 Genera el modelo geométrico 3D de TODA la estructura:
   - Pilares H°A° (grilla continua S3→AZ, secciones por grupo de niveles)
   - Losas nervuradas/reticulares alivianadas en cada nivel (S3→AZ)
   - Vigas de borde (spandrel 25×50) + bordes de pozos A/B (20×40)
     → SISTEMA NERVURADO (AGENTS.md §10.0, adoptado 2026-09-10)
   - 2 Núcleos H°A° gemelos (pantallas de rigidez lateral)
   - Masas de azotea: tanques elevados + piscina 8×16m (representación)

 ELEMENTOS (fuente única de verdad: modelo_estructural.py):
   - Grilla X: [2.50 ... 87.50] (12 ejes) · Y: [3.00 ... 40.00] (6 ejes)
   - Núcleos: N1 X:34→41 / N2 X:49→56 · Y:17→26 (7m×9m, rotados 90°)
   - Niveles: S2 -6,40 · S1 -3,20 · PB 0,00 (h=4,50)
             P01..P18 cada 3.35 m (3.00 m libres piso a cielo raso)
             AZ 64.30 (h=2.20)

 SECCIONES DE PILARES POR GRUPO DE NIVELES (PROVISIONAL para el modelo 3D;
   el dimensionamiento final recalculará cada sección — AGENTS.md §10):
   - S3→PB: 90×90 cm · P01–P05: 80×80 · P06–P11: 70×70 · P12–P18: 60×60

 SALIDAS:
   - outputs/modelo_3d_iso.png       (vista isométrica)
   - outputs/modelo_3d_planta.png     (vista en planta desde arriba)
   - outputs/modelo_3d_elevacion.png  (elevación / fachada)
   - outputs/elementos_3d.json        (inventario de elementos para otros módulos)
====================================================================
"""

import os
import sys
import json
import numpy as np
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Reutilizar la fuente única de verdad (modelo_estructural.py en 06_Estructura)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelo_estructural import (HUELLA, XS, YS, NUCLEOS, PASILLO_TECNICO,
                                NIVELES, LOSA_POR_NIVEL)

# ──────────────────────────────────────────────────────────────────
# SECCIONES PROVISIONALES DE PILARES (m) por grupo de cotas
#   -10.5 → 0.00  : 90×90 cm  (subsuelos + PB, carga axial máxima)
#    4.0 → 20.75  : 80×80 cm  (P01–P05)
#   20.75 → 40.85 : 70×70 cm  (P06–P11)
#   40.85 → AZ    : 60×60 cm  (P12–P18)
# ──────────────────────────────────────────────────────────────────
# Cota inferior de la estructura (fondo de losa S3) y superior (azotea)
Z_BASE = -10.50
Z_AZOTEA = next(n["cota"] for n in NIVELES if n["id"] == "AZ")  # 64.30

GRUPOS_SECCION = [
    dict(zmax=0.0,    ancho=0.90),
    dict(zmax=20.75,  ancho=0.80),
    dict(zmax=40.85,  ancho=0.70),
    dict(zmax=Z_AZOTEA, ancho=0.60),
]

# Canto físico de losa por nivel — LOSA_POR_NIVEL[nivel]["canto"]
# (nervurada: 45 cm PB/sub, 35 cm plantas tipo y azotea)
ESPESOR_AZOTEA = LOSA_POR_NIVEL["AZ"]["canto"]  # 0.35

def canto_losa(nid):
    """Canto físico (m) de la losa de un nivel (nervurada)."""
    return LOSA_POR_NIVEL.get(nid, {}).get("canto", 0.35)

# ──────────────────────────────────────────────────────────────────
# VIGAS DE BORDE (SISTEMA NERVURADO — AGENTS.md §10.0, adoptado 2026-09-10)
#   Spandrel perimetral 25×50 en las 4 fachadas + vigas de borde
#   20×40 en pozos de luz A/B (P01-P18 + AZ). Sin vigas interiores.
# ──────────────────────────────────────────────────────────────────
SPANDREL_W = 0.25        # ancho viga perimetral (m)
SPANDREL_H = 0.50        # peralte viga perimetral (m)
POZO_BEAM_W = 0.20       # ancho viga de borde de pozo (m)
POZO_BEAM_H = 0.40       # peralte viga de borde de pozo (m)
POZOS_MODELO = [dict(id="A", x0=5.0,  x1=19.0, y0=18.0, y1=25.0),
                dict(id="B", x0=71.0, x1=85.0, y0=18.0, y1=25.0)]
NIVELES_CON_POZOS = {f"P{i:02d}" for i in range(1, 19)} | {"AZ"}


def seccion_pilar_en(z_centro):
    """Devuelve el ancho de pilar (m) según la cota del centro del tramo."""
    for g in GRUPOS_SECCION:
        if z_centro <= g["zmax"]:
            return g["ancho"]
    return GRUPOS_SECCION[-1]["ancho"]


def pilares_de_grilla():
    """Genera la lista de pilares (mismos criterios que ga_grilla_pilares.py):
       - 1 pilar en cada intersección de ejes
       - se retiran los que caen DENTRO del área maciza de un núcleo"""
    pilares = []
    for x in XS:
        for y in YS:
            dentro = any((c["x0"] + 0.90) < x < (c["x1"] - 0.90) and
                         (c["y0"] + 0.90) < y < (c["y1"] - 0.90)
                         for c in NUCLEOS)
            if dentro:
                continue
            pilares.append(dict(id=f"P{len(pilares)+1:03d}", x=x, y=y))
    return pilares


def segmentos_de_pilar(x, y, z0, z1):
    """Divide un pilar en tramos según los límites de cambio de sección
    (1 tramo por grupo de sección → máx. 4 tramos por pilar)."""
    limites = sorted({g["zmax"] for g in GRUPOS_SECCION})
    puntos = [z0] + [L for L in limites if z0 < L < z1] + [z1]
    seg = []
    for i in range(len(puntos) - 1):
        za, zb = puntos[i], puntos[i + 1]
        ancho = seccion_pilar_en((za + zb) / 2)
        seg.append(dict(z0=za, z1=zb, ancho=ancho))
    return seg


def generar_vigas():
    """Vigas de borde del sistema nervurado:
       - Spandrel perimetral en las 4 fachadas (entre pilares de borde),
         en CADA nivel, peralte SPANDREL_H bajo la losa.
       - Vigas de borde alrededor de los pozos de luz A/B (P01-P18 + AZ).
       Sin vigas interiores (losa nervurada/reticular)."""
    vigas = []
    cotas = {n["id"]: n["cota"] for n in NIVELES}
    for nid, cota in cotas.items():
        z0, z1 = cota - SPANDREL_H, cota
        # Spandrel Sur (Y=3.0) y Norte (Y=40.0) — tramos entre columnas X
        for y_f in (HUELLA["y0"], HUELLA["y1"]):
            for i in range(len(XS) - 1):
                vigas.append(dict(id=f"VB_{nid}_{y_f:.0f}_{i:02d}",
                                  x0=XS[i], x1=XS[i + 1],
                                  y0=y_f - SPANDREL_W / 2, y1=y_f + SPANDREL_W / 2,
                                  z0=z0, z1=z1, tipo="spandrel"))
        # Spandrel Oeste (X=2.5) y Este (X=87.5) — tramos entre columnas Y
        for x_f in (HUELLA["x0"], HUELLA["x1"]):
            for j in range(len(YS) - 1):
                vigas.append(dict(id=f"VB_{nid}_{x_f:.0f}_{j:02d}",
                                  x0=x_f - SPANDREL_W / 2, x1=x_f + SPANDREL_W / 2,
                                  y0=YS[j], y1=YS[j + 1],
                                  z0=z0, z1=z1, tipo="spandrel"))
        # Bordes de pozos de luz (P01-P18 + AZ)
        if nid in NIVELES_CON_POZOS:
            for pz in POZOS_MODELO:
                for b in (dict(y=pz["y0"]), dict(y=pz["y1"])):
                    vigas.append(dict(id=f"VP_{nid}_{pz['id']}_{b['y']:.0f}",
                                      x0=pz["x0"], x1=pz["x1"],
                                      y0=b["y"] - POZO_BEAM_W / 2,
                                      y1=b["y"] + POZO_BEAM_W / 2,
                                      z0=z0, z1=z1, tipo="pozo"))
                for b in (dict(x=pz["x0"]), dict(x=pz["x1"])):
                    vigas.append(dict(id=f"VP_{nid}_{pz['id']}_{b['x']:.0f}",
                                      x0=b["x"] - POZO_BEAM_W / 2,
                                      x1=b["x"] + POZO_BEAM_W / 2,
                                      y0=pz["y0"], y1=pz["y1"],
                                      z0=z0, z1=z1, tipo="pozo"))
    return vigas


def construir_elementos():
    """Construye el inventario de elementos 3D."""
    niveles = [n["id"] for n in NIVELES]  # S3..P18, AZ
    cotas = {n["id"]: n["cota"] for n in NIVELES}

    # Losas (una placa por nivel, canto físico del sistema nervurado)
    losas = []
    for n in NIVELES:
        t = canto_losa(n["id"])
        losas.append(dict(id=f"LOSA_{n['id']}", nivel=n["id"],
                          z_top=n["cota"], espesor=t,
                          x0=HUELLA["x0"], x1=HUELLA["x1"],
                          y0=HUELLA["y0"], y1=HUELLA["y1"]))

    # Pilares (segmentos por grupo de sección)
    pilares = []
    for p in pilares_de_grilla():
        for seg in segmentos_de_pilar(p["x"], p["y"], Z_BASE, Z_AZOTEA):
            pilares.append(dict(id=p["id"], x=p["x"], y=p["y"],
                                z0=seg["z0"], z1=seg["z1"], ancho=seg["ancho"]))

    # Núcleos (pantallas continuas S3→AZ)
    nucleos = []
    for c in NUCLEOS:
        nucleos.append(dict(id=c["id"], x0=c["x0"], x1=c["x1"],
                            y0=c["y0"], y1=c["y1"], z0=Z_BASE, z1=Z_AZOTEA))

    # Masas de azotea (representación para render y cargas)
    # Tanques elevados UNIDOS EN BLOQUE ÚNICO (X:34→56 × Y:17→26) con muro
    # intermedio en X=45 → apoyo sobre núcleos N1/N2 + losa corredor; los
    # ductos (RSU Ø500 y shafts de ventilación) suben en chase en el muro
    # partición X=45 (criterio AGENTS.md §13.2 "0 pilares apeados").
    masas = [
        dict(id="TANQUE_POTABLE", tipo="tanque", x0=34.0, x1=45.0,
             y0=17.0, y1=26.0, z0=Z_AZOTEA, z1=Z_AZOTEA + 3.0),
        dict(id="TANQUE_PCI", tipo="tanque", x0=45.0, x1=56.0,
             y0=17.0, y1=26.0, z0=Z_AZOTEA, z1=Z_AZOTEA + 3.0),
        dict(id="PISCINA", tipo="piscina", x0=10.25, x1=26.25,
             y0=29.0, y1=37.0, z0=Z_AZOTEA, z1=Z_AZOTEA + 1.6),
    ]

    # Vigas de borde (sistema nervurado: spandrel perimetral + bordes de pozos)
    vigas = generar_vigas()

    return dict(pilares=pilares, losas=losas, nucleos=nucleos,
                masas=masas, vigas=vigas, niveles=niveles, cotas=cotas)


# ──────────────────────────────────────────────────────────────────
# RENDER 3D
# ──────────────────────────────────────────────────────────────────
def _caja(ax, x0, x1, y0, y1, z0, z1, fc, ec="#0f172a", alpha=1.0, lw=0.6):
    """Dibuja una caja (paralelepípedo) en el eje 3D."""
    verts = [
        [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)],
        [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)],
        [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)],
        [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)],
        [(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)],
        [(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)],
    ]
    ax.add_collection3d(Poly3DCollection(verts, facecolors=fc, edgecolors=ec,
                                         alpha=alpha, linewidths=lw))


def generar_render(elementos, vista="iso", nombre="modelo_3d_iso.png"):
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#f8fafc")

    # Losas (transparentes)
    for L in elementos["losas"]:
        _caja(ax, L["x0"], L["x1"], L["y0"], L["y1"],
              L["z_top"] - L["espesor"], L["z_top"],
              "#bae6fd", ec="#0284c7", alpha=0.32)

    # Pozos de luz: voids recortados en las losas (P01-P18 + AZ)
    cotas_set = {n["id"]: n["cota"] for n in NIVELES}
    for nid in NIVELES_CON_POZOS:
        cota = cotas_set[nid]
        t = canto_losa(nid)
        for pz in POZOS_MODELO:
            _caja(ax, pz["x0"], pz["x1"], pz["y0"], pz["y1"],
                  cota - t, cota, "#f1f5f9", ec="#0f172a", alpha=0.95, lw=0.5)

    # Vigas de borde: BANDA CONTINUA por fachada y nivel (representación limpia;
    #   evita las 888 cajas segmentadas que saturaban el render). El inventario
    #   completo por tramo sigue en elementos_3d.json para IFC/cálculo.
    for nid, cota in cotas_set.items():
        z0, z1 = cota - SPANDREL_H, cota
        for y_f in (HUELLA["y0"], HUELLA["y1"]):
            _caja(ax, HUELLA["x0"], HUELLA["x1"],
                  y_f - SPANDREL_W / 2, y_f + SPANDREL_W / 2,
                  z0, z1, "#f59e0b", ec="#92400e", alpha=0.55, lw=0.3)
        for x_f in (HUELLA["x0"], HUELLA["x1"]):
            _caja(ax, x_f - SPANDREL_W / 2, x_f + SPANDREL_W / 2,
                  HUELLA["y0"], HUELLA["y1"],
                  z0, z1, "#f59e0b", ec="#92400e", alpha=0.55, lw=0.3)

    # Pilares
    for P in elementos["pilares"]:
        a = P["ancho"]
        _caja(ax, P["x"] - a / 2, P["x"] + a / 2,
              P["y"] - a / 2, P["y"] + a / 2, P["z0"], P["z1"],
              "#94a3b8", ec="#334155", alpha=0.9, lw=0.4)

    # Núcleos
    for C in elementos["nucleos"]:
        _caja(ax, C["x0"], C["x1"], C["y0"], C["y1"], C["z0"], C["z1"],
              "#1e293b", ec="#0f172a", alpha=0.95, lw=1.0)

    # Masas de azotea
    for M in elementos["masas"]:
        if M["tipo"] == "piscina":
            _caja(ax, M["x0"], M["x1"], M["y0"], M["y1"], M["z0"], M["z1"],
                  "#38bdf8", ec="#0369a1", alpha=0.35, lw=0.8)
        else:
            _caja(ax, M["x0"], M["x1"], M["y0"], M["y1"], M["z0"], M["z1"],
                  "#fbbf24", ec="#b45309", alpha=0.8, lw=0.8)

    # Limites y vista
    ax.set_xlim(HUELLA["x0"] - 2, HUELLA["x1"] + 2)
    ax.set_ylim(HUELLA["y0"] - 2, HUELLA["y1"] + 2)
    ax.set_zlim(-13, 68)
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    if vista == "iso":
        ax.view_init(elev=24, azim=-55)
    elif vista == "planta":
        ax.view_init(elev=90, azim=-90)
    elif vista == "elevacion":
        ax.view_init(elev=0, azim=-90)  # fachada SUR (frente, 85 m) — no el costado

    ax.set_title("MODELO 3D ESTRUCTURAL — Edificio 18P + 2 Subsuelos\n"
                 "Grilla continua S3→AZ · Losas nervuradas/reticulares · 2 Núcleos H°A° · "
                 f"{len(elementos['pilares'])} tramos de pilar",
                 fontsize=11, fontweight="bold")

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    ruta = os.path.join(out_dir, nombre)
    plt.tight_layout()
    plt.savefig(ruta, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {ruta}")


# ──────────────────────────────────────────────────────────────────
# EXPORTAR INVENTARIO JSON (para cálculo / IFC / Revit)
# ──────────────────────────────────────────────────────────────────
def exportar_json(elementos, ruta=None):
    if ruta is None:
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "outputs", "elementos_3d.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(elementos, f, ensure_ascii=False, indent=2)
    print(f"[OK] {ruta}")
    return ruta


if __name__ == "__main__":
    elementos = construir_elementos()
    generar_render(elementos, "iso", "modelo_3d_iso.png")
    generar_render(elementos, "planta", "modelo_3d_planta.png")
    generar_render(elementos, "elevacion", "modelo_3d_elevacion.png")
    exportar_json(elementos)
    n_pil = len({p["id"] for p in elementos["pilares"]})
    print(f"     Pilares: {n_pil} | Losas: {len(elementos['losas'])} | "
          f"Núcleos: {len(elementos['nucleos'])} | Masas azotea: {len(elementos['masas'])}")
