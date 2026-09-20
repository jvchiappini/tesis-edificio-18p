"""
====================================================================
 COMPARATIVA DE SISTEMAS ESTRUCTURALES DE ENTREPISO — COSTO
 Edificio 18P + 2 Subsuelos | CDE, Paraguay | 2026
====================================================================

 OBJETIVO
 --------
 Elegir el sistema de entrepiso MÁS ECONÓMICO ("la estructura más
 barata, no la más rápida") entre 5 alternativas, manteniendo la
 MISMA grilla de pilares (posición fija, continuidad S3→AZ — ver
 AGENTS.md §10.1) y los mismos núcleos N1/N2. La altura de cada
 sistema (espesor de losa / peralte de vigas) varía libremente.

 SISTEMAS COMPARADOS (todos H°A°):
   A) Losa plana POSTENSADA (PT no adherida) + vigas perimetrales
      (SISTEMA HÍBRIDO ACTUAL — AGENTS.md §10.0)
   B) Losa plana armada convencional (sin vigas interiores)
   C) Losa maciza + VIGAS INTERIORES (pórtico convencional)
   D) Losa NERVURADA / reticular alivianada (casetones)
   E) Vigueta pretensada + bovedilla (SOLO plantas tipo: no viable en
      PB/subsuelos/azotea por luces 7,5 m + cargas altas → en esos
      niveles se resuelve con sistema C convencional)

 PILARES Y NÚCLEOS: comunes a todos los sistemas (posición fija) →
 SE EXCLUYEN de la comparación (costo diferencial = 0). El costo
 comparado es el del SISTEMA DE ENTREPISO (losa + vigas + armadura +
 encofrado + PT/viguetas). Verificado en AGENTS.md §10.

 CANTIDADES POR SISTEMA (por m² de losa)
 ---------------------------------------
 Espesores de referencia (fuentes: PTI / TensionOne para PT; ACI
 318-19 Tabla 7.3.1.1 losas armadas L/33-36; pórticos y nervuradas
 práctica habitual; CYPE para viguetas):
   - A: PT 18 cm residencial / 25 cm PB y subsuelos (+capitel/drop)
        + vigas perimetrales 25×50 (P01-P18+AZ) → +0,02 m³/m².
   - B: losa plana armada 25 cm residencial / 30 cm PB y subsuelos
        (+capitel/drop).
   - C: losa 20 cm + vigas interiores 40×60 (TIPO/AZ) y 45×65
        (PB/sub). Vigas en grilla 7,5 m → 0,267 m de viga por m².
   - D: nervurada canto 35 cm (capa 10 + casetón 25) / 45 cm PB-sub.
   - E: vigueta T-12 + bovedilla hormigón 60×20×25, canto 30=25+5
        (idéntica al ítem CYPE EHU010).

 PRECIOS UNITARIOS (Paraguay 2025-2026 — FUENTES CITADAS, guardadas
 en 07_KNOWLEDGE_BASE/07.04_Normativa_Resumen):
   - Hormigón HA-25/B/19/IIa bombeable: 999.924 Gs/m³
     [CYPE Ingenieros — Generador de Precios Paraguay]
   - Acero AP 500 instalado (corte, doblado, armado, atar): 8.242
     Gs/kg [CYPE Paraguay; CAPACO julio-2025: varillas 10.450 Gs/kg]
   - Encofrado continuo de losa (recuperable): ~100.000 Gs/m²
     [derivado del ítem CYPE EHL020 "losa maciza y pilares" 24 cm:
     material ≈ 481.000 Gs/m², resto ≈ 151.000 Gs/m² encofrado+curado]
   - Postensado no adherido (suministro + instalación + tensado):
     12-14 USD/m² [rango típico de mercado; estudio comparativo
     Ecuador: torón 270 ksi instalado ≈ 5-6 USD/kg × ~3 kg/m²]
   - Vigueta pretensada + bovedilla + capa de compresión instalado:
     350.546 Gs/m² [CYPE EHU010 "losa unidireccional con vigas"]
   - Tipo de cambio: 6.100 Gs/USD [BCP cotización referencial
     09-06-2026 = 6.183,88; promedio 90 días ≈ 6.048]

 SALIDAS:
   - outputs/comparativa_estructuras.csv  (detalle por nivel y total)
   - outputs/comparativa_estructuras.png  (USD/m² y costo total)
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
from modelo_estructural import HUELLA, NIVELES, POZOS_LUZ

GAMMA_HORMIGON = 25.0  # kN/m³ (NBR 6120)

# ──────────────────────────────────────────────────────────────────
# 1. PRECIOS UNITARIOS (Gs) — FUENTES en docstring
# ──────────────────────────────────────────────────────────────────
P_CONCRETO = 999_924.0        # Gs/m³  HA-25/B/19/IIa bombeable  [CYPE]
P_ACERO = 8_242.0             # Gs/kg  AP 500 instalado          [CYPE]
P_ENCOFRADO = 100_000.0       # Gs/m²  encofrado continuo losa   [derivado CYPE]
PT_USD_TIPO = 12.0            # USD/m² PT plantas tipo
PT_USD_REST = 14.0            # USD/m² PT PB / subsuelos / azotea
P_VIGUETA_TIPO = 350_546.0    # Gs/m²  vigueta+bovedilla instalado [CYPE EHU010]
TC = 6_100.0                  # Gs/USD (BCP jun-2026)

# ──────────────────────────────────────────────────────────────────
# 2. ÁREAS DE LOSA POR TIPO DE NIVEL (desde modelo_estructural)
# ──────────────────────────────────────────────────────────────────
AREA_HUELLA = HUELLA["area"]                      # 3.145 m²
AREA_POZOS = sum(p["area"] for p in POZOS_LUZ)    # 196 m² (A+B)
AREA_TIPO = AREA_HUELLA - AREA_POZOS              # 2.949 m²

def area_tipo_nivel(tipo):
    return {"SUB": AREA_HUELLA, "PB": AREA_HUELLA,
            "TIPO": AREA_TIPO, "AZ": AREA_TIPO}[tipo]

def clasificar_nivel(nid):
    if nid in ("S1", "S2", "S3"):
        return "SUB"
    if nid == "PB":
        return "PB"
    if nid == "AZ":
        return "AZ"
    return "TIPO"

# ──────────────────────────────────────────────────────────────────
# 3. PARÁMETROS DE CADA SISTEMA POR TIPO DE NIVEL
#    e_losa : espesor losa (m) — informativo
#    conc   : concreto total losa+vigas (m³/m²)
#    acero  : acero de refuerzo (kg/m²)
#    encof  : encofrado (m²/m²)
#    pt_usd : costo PT (USD/m²); 0 si no aplica
#    allin  : precio llave en mano (Gs/m²) si aplica (E-TIPO); None si no
# ──────────────────────────────────────────────────────────────────
SISTEMAS = {
    "A_PT_HIBRIDO": dict(
        nombre="A) Losa plana POSTENSADA + vigas perimetrales (híbrido actual)",
        tipos=dict(
            SUB=dict(e_losa=0.25, conc=0.28, acero=8.0,  encof=1.00, pt_usd=PT_USD_REST, allin=None),
            PB =dict(e_losa=0.25, conc=0.28, acero=8.0,  encof=1.00, pt_usd=PT_USD_REST, allin=None),
            TIPO=dict(e_losa=0.18, conc=0.20, acero=7.0,  encof=1.00, pt_usd=PT_USD_TIPO, allin=None),
            AZ =dict(e_losa=0.20, conc=0.22, acero=8.0,  encof=1.00, pt_usd=PT_USD_REST, allin=None),
        ),
    ),
    "B_LOSA_PLANA_ARMADA": dict(
        nombre="B) Losa plana armada convencional (sin vigas interiores)",
        tipos=dict(
            SUB=dict(e_losa=0.30, conc=0.33, acero=28.0, encof=1.00, pt_usd=0.0, allin=None),
            PB =dict(e_losa=0.30, conc=0.33, acero=28.0, encof=1.00, pt_usd=0.0, allin=None),
            TIPO=dict(e_losa=0.25, conc=0.25, acero=24.0, encof=1.00, pt_usd=0.0, allin=None),
            AZ =dict(e_losa=0.25, conc=0.25, acero=26.0, encof=1.00, pt_usd=0.0, allin=None),
        ),
    ),
    "C_PORTAICO_VIGAS": dict(
        nombre="C) Losa maciza + vigas interiores (pórtico H°A°)",
        tipos=dict(
            SUB=dict(e_losa=0.20, conc=0.28, acero=30.0, encof=1.47, pt_usd=0.0, allin=None),
            PB =dict(e_losa=0.20, conc=0.28, acero=30.0, encof=1.47, pt_usd=0.0, allin=None),
            TIPO=dict(e_losa=0.20, conc=0.26, acero=27.0, encof=1.43, pt_usd=0.0, allin=None),
            AZ =dict(e_losa=0.20, conc=0.26, acero=27.0, encof=1.43, pt_usd=0.0, allin=None),
        ),
    ),
    "D_NERVURADA": dict(
        nombre="D) Losa nervurada / reticular alivianada",
        tipos=dict(
            SUB=dict(e_losa=0.45, conc=0.22, acero=18.0, encof=1.10, pt_usd=0.0, allin=None),
            PB =dict(e_losa=0.45, conc=0.22, acero=18.0, encof=1.10, pt_usd=0.0, allin=None),
            TIPO=dict(e_losa=0.35, conc=0.18, acero=14.0, encof=1.10, pt_usd=0.0, allin=None),
            AZ =dict(e_losa=0.35, conc=0.18, acero=16.0, encof=1.10, pt_usd=0.0, allin=None),
        ),
    ),
    "E_VIGUETA_BOVEDILLA": dict(
        nombre="E) Vigueta pretensada + bovedilla (tipo) / pórtico (resto)",
        tipos=dict(
            SUB=dict(e_losa=0.20, conc=0.28, acero=30.0, encof=1.47, pt_usd=0.0, allin=None),
            PB =dict(e_losa=0.20, conc=0.28, acero=30.0, encof=1.47, pt_usd=0.0, allin=None),
            TIPO=dict(e_losa=0.30, conc=0.143, acero=11.0, encof=1.00, pt_usd=0.0,
                      allin=P_VIGUETA_TIPO),
            AZ =dict(e_losa=0.20, conc=0.26, acero=27.0, encof=1.43, pt_usd=0.0, allin=None),
        ),
    ),
}

# ──────────────────────────────────────────────────────────────────
# 4. CÁLCULO
# ──────────────────────────────────────────────────────────────────
def costo_m2(par, mult=None):
    """Costo por m² (Gs) de un par tipo de nivel, según parámetros.

    mult: dict con multiplicadores opcionales de precio
          {'conc':1.0, 'acero':1.0, 'encof':1.0, 'pt':1.0}.
    """
    if mult is None:
        mult = dict(conc=1.0, acero=1.0, encof=1.0, pt=1.0)
    if par["allin"] is not None:
        return par["allin"] * mult["conc"]
    c = (par["conc"] * P_CONCRETO * mult["conc"]
         + par["acero"] * P_ACERO * mult["acero"]
         + par["encof"] * P_ENCOFRADO * mult["encof"]
         + par["pt_usd"] * TC * mult["pt"])
    return c

def peso_propio_m2(par):
    """Peso propio del sistema de entrepiso (kN/m²) — indicador sísmico."""
    return round(par["conc"] * GAMMA_HORMIGON, 1)

def calcular(mult=None, sistemas=None):
    """Devuelve (detalle, resumen). detalle: filas por nivel; resumen por sistema.

    mult: multiplicadores de precio {'conc','acero','encof','pt'} (1.0 = base).
    sistemas: dict de sistemas alternativo (para sensibilidad de PT).
    """
    if mult is None:
        mult = dict(conc=1.0, acero=1.0, encof=1.0, pt=1.0)
    if sistemas is None:
        sistemas = SISTEMAS
    detalle = []
    for sid, sist in sistemas.items():
        total_gs = 0.0
        total_area = 0.0
        conc_tot = 0.0
        acero_tot = 0.0
        for nivel in NIVELES:
            nid = nivel["id"]
            tipo = clasificar_nivel(nid)
            area = area_tipo_nivel(tipo)
            par = sist["tipos"][tipo]
            cm2 = costo_m2(par, mult)
            costo_nivel = cm2 * area
            conc_nivel = par["conc"] * area
            acero_nivel = par["acero"] * area
            total_gs += costo_nivel
            total_area += area
            conc_tot += conc_nivel
            acero_tot += acero_nivel
            detalle.append(dict(sistema=sid, nivel=nid, tipo=tipo, area=area,
                                costo_m2_gs=round(cm2, 0),
                                costo_gs=round(costo_nivel, 0),
                                conc_m3=round(conc_nivel, 1),
                                acero_kg=round(acero_nivel, 1),
                                pp_kNm2=peso_propio_m2(par)))
        resumen = dict(sistema=sid, nombre=sist["nombre"],
                       costo_gs=total_gs, costo_usd=total_gs / TC,
                       area=total_area, costo_m2_gs=total_gs / total_area,
                       costo_m2_usd=total_gs / total_area / TC,
                       conc_total=conc_tot, acero_total=acero_tot,
                       pp_media=conc_tot / total_area * GAMMA_HORMIGON)
        resumen["costo_m2_gs"] = round(resumen["costo_m2_gs"], 0)
        resumen["costo_m2_usd"] = round(resumen["costo_m2_usd"], 1)
        resumen["pp_media"] = round(resumen["pp_media"], 1)
        resumen["costo_usd"] = round(resumen["costo_usd"] / 1e6, 2)  # USD millones
        resumen["conc_total"] = round(resumen["conc_total"] / 1000, 1)  # miles de m³
        resumen["acero_total"] = round(resumen["acero_total"] / 1e6, 1)  # miles de t
        resumen["costo_gs"] = round(resumen["costo_gs"] / 1e9, 2)  # miles de millones
        resumen["ranking"] = None
        resumen["ahorro_vs_A"] = None
    # Ranking por costo total (más barato primero)
    return detalle, _resumenes(detalle)

def _resumenes(detalle):
    res = []
    for sid in SISTEMAS:
        filas = [d for d in detalle if d["sistema"] == sid]
        costo_gs = sum(f["costo_gs"] for f in filas)
        area = sum(f["area"] for f in filas)
        conc = sum(f["conc_m3"] for f in filas)
        acero = sum(f["acero_kg"] for f in filas)
        pp_media = sum(f["pp_kNm2"] * f["area"] for f in filas) / area
        res.append(dict(sistema=sid, nombre=SISTEMAS[sid]["nombre"],
                        costo_gs=costo_gs / 1e9,
                        costo_usd=costo_gs / TC / 1e6,
                        costo_m2_gs=costo_gs / area,
                        costo_m2_usd=costo_gs / area / TC,
                        conc_total=conc / 1000,
                        acero_total=acero / 1e6,
                        pp_media=pp_media))
    res.sort(key=lambda r: r["costo_usd"])
    min_usd = res[0]["costo_usd"]
    for i, r in enumerate(res, 1):
        r["ranking"] = i
        r["ahorro_vs_A"] = None
        ref = next((x for x in res if x["sistema"] == "A_PT_HIBRIDO"), None)
        if ref and r["sistema"] != "A_PT_HIBRIDO":
            r["ahorro_vs_A"] = round((ref["costo_usd"] - r["costo_usd"]) / ref["costo_usd"] * 100, 1)
        r["costo_m2_gs"] = round(r["costo_m2_gs"], 0)
        r["costo_m2_usd"] = round(r["costo_m2_usd"], 1)
        r["costo_usd"] = round(r["costo_usd"], 2)
        r["costo_gs"] = round(r["costo_gs"], 2)
        r["conc_total"] = round(r["conc_total"], 1)
        r["acero_total"] = round(r["acero_total"], 1)
        r["pp_media"] = round(r["pp_media"], 1)
    return res

# ──────────────────────────────────────────────────────────────────
# 5. SALIDAS
# ──────────────────────────────────────────────────────────────────
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

# ──────────────────────────────────────────────────────────────────
# 5b. SENSIBILIDAD (PT 10-16 USD/m², concreto/acero/encofrado ±15%)
# ──────────────────────────────────────────────────────────────────
import copy

def _con_pt_usd(sistemas, tipo_usd, resto_usd):
    """Devuelve copia de SISTEMAS con el costo de PT de A modificado."""
    s = copy.deepcopy(sistemas)
    s["A_PT_HIBRIDO"]["tipos"]["TIPO"]["pt_usd"] = tipo_usd
    for k in ("SUB", "PB", "AZ"):
        s["A_PT_HIBRIDO"]["tipos"][k]["pt_usd"] = resto_usd
    return s

def sensibilidad():
    """Escenarios: varía PT y precios de materiales. Devuelve lista de filas."""
    base = _resumenes(calcular()[0])
    ref_A = next(r for r in base if r["sistema"] == "A_PT_HIBRIDO")
    escenarios = [
        ("Base (PT 12/14 USD/m2)",          1.0, 1.0, 1.0, 1.0, None),
        ("PT barato (10 USD/m2)",           1.0, 1.0, 1.0, 1.0, (10.0, 10.0)),
        ("PT caro (16 USD/m2)",             1.0, 1.0, 1.0, 1.0, (16.0, 16.0)),
        ("Concreto -15%",                   0.85, 1.0, 1.0, 1.0, None),
        ("Concreto +15%",                   1.15, 1.0, 1.0, 1.0, None),
        ("Acero -15%",                      1.0, 0.85, 1.0, 1.0, None),
        ("Acero +15%",                      1.0, 1.15, 1.0, 1.0, None),
        ("Encofrado -15%",                  1.0, 1.0, 0.85, 1.0, None),
        ("Encofrado +15%",                  1.0, 1.0, 1.15, 1.0, None),
        ("Peor caso PT (acero -15%, PT 16)", 1.0, 0.85, 1.0, 1.0, (16.0, 16.0)),
        ("Mejor caso PT (materiales +15%, PT 10)", 1.15, 1.15, 1.15, 1.0, (10.0, 10.0)),
    ]
    filas = []
    for nombre, mc, ma, me, mpt, pt in escenarios:
        mult = dict(conc=mc, acero=ma, encof=me, pt=1.0 if mpt is None else 1.0)
        sist = _con_pt_usd(SISTEMAS, *pt) if pt else SISTEMAS
        res = _resumenes(calcular(mult, sist)[0])
        # costo de PT ya incorporado por pt_usd dentro de sist (no vía mult)
        g1 = next(r for r in res if r["sistema"] == "D_NERVURADA")
        g2 = next(r for r in res if r["sistema"] == "E_VIGUETA_BOVEDILLA")
        a = next(r for r in res if r["sistema"] == "A_PT_HIBRIDO")
        mejor = res[0]
        filas.append(dict(escenario=nombre,
                          A_m2=a["costo_m2_usd"], A_total=a["costo_usd"],
                          D_m2=g1["costo_m2_usd"], D_total=g1["costo_usd"],
                          E_m2=g2["costo_m2_usd"], E_total=g2["costo_usd"],
                          ganador=mejor["sistema"], A_vs_D_pct=round(
                              (a["costo_usd"] - g1["costo_usd"]) / g1["costo_usd"] * 100, 1)))
    return filas

def escribir_sensibilidad_csv(filas):
    p = os.path.join(OUT, "comparativa_sensibilidad.csv")
    with open(p, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["escenario", "A_total_MMUSD", "D_total_MMUSD", "E_total_MMUSD",
                    "A_m2_USD", "ganador", "A_vs_D_pct"])
        for r in filas:
            w.writerow([r["escenario"], r["A_total"], r["D_total"], r["E_total"],
                        r["A_m2"], r["ganador"], r["A_vs_D_pct"]])
    return p

def grafico_sensibilidad(filas):
    fig, ax = plt.subplots(figsize=(11, 5.6))
    xs = range(len(filas))
    ax.plot(xs, [r["A_total"] for r in filas], "-o", color="#1976d2",
            label="A) Losa PT + vigas perimetrales", lw=2)
    ax.plot(xs, [r["D_total"] for r in filas], "-s", color="#2e7d32",
            label="D) Losa nervurada (más barata base)", lw=2)
    ax.plot(xs, [r["E_total"] for r in filas], "-^", color="#f9a825",
            label="E) Vigueta + bovedilla", lw=2)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([r["escenario"] for r in filas], rotation=18, ha="right", fontsize=7.5)
    ax.set_ylabel("Costo total de entrepisos (MMUSD)")
    ax.set_title("Análisis de sensibilidad — costo total por sistema (68.611 m²)", fontsize=10,
                 fontweight="bold")
    ax.legend(fontsize=8.5, loc="best")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    p = os.path.join(OUT, "comparativa_sensibilidad.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p

def escribir_csv(detalle, resumen):
    p = os.path.join(OUT, "comparativa_estructuras.csv")
    with open(p, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["DETALLE POR NIVEL"])
        w.writerow(["sistema", "nivel", "tipo", "area_m2", "costo_m2_gs",
                    "costo_gs", "concreto_m3", "acero_kg", "peso_propio_kNm2"])
        for d in detalle:
            w.writerow([d["sistema"], d["nivel"], d["tipo"], d["area"],
                        d["costo_m2_gs"], d["costo_gs"], d["conc_m3"],
                        d["acero_kg"], d["pp_kNm2"]])
        w.writerow([])
        w.writerow(["RESUMEN POR SISTEMA (ordenado de más barato a más caro)"])
        w.writerow(["ranking", "sistema", "nombre", "costo_total_MMUSD",
                    "costo_m2_USD", "costo_m2_Gs", "concreto_miles_m3",
                    "acero_miles_t", "peso_propio_medio_kNm2", "ahorro_vs_A_pct"])
        for r in resumen:
            w.writerow([r["ranking"], r["sistema"], r["nombre"], r["costo_usd"],
                        r["costo_m2_usd"], r["costo_m2_gs"], r["conc_total"],
                        r["acero_total"], r["pp_media"],
                        "" if r["ahorro_vs_A"] is None else r["ahorro_vs_A"]])
    return p

def grafico(resumen):
    fig, axs = plt.subplots(1, 2, figsize=(13.5, 5.6))
    noms = [r["nombre"].split(") ")[0] for r in resumen]
    cols = ["#2e7d32", "#1976d2", "#e53935", "#f9a825", "#6a1b9a"]
    labels = [f"{r['ranking']}) {r['nombre']}" for r in resumen]
    min_usd = min(r["costo_m2_usd"] for r in resumen)

    axs[0].bar(range(len(resumen)), [r["costo_m2_usd"] for r in resumen],
               color=cols, edgecolor="black", linewidth=0.6)
    axs[0].set_xticks(range(len(resumen)))
    axs[0].set_xticklabels(labels, rotation=18, ha="right", fontsize=7.5)
    axs[0].set_ylabel("USD/m² (costo de entrepiso)")
    axs[0].set_title("Costo por m² de losa (USD/m²)", fontsize=10, fontweight="bold")
    for i, r in enumerate(resumen):
        axs[0].text(i, r["costo_m2_usd"] + 1, f"{r['costo_m2_usd']:.1f}",
                    ha="center", fontsize=9, fontweight="bold",
                    color="#2e7d32" if r["costo_m2_usd"] == min_usd else "black")

    axs[1].bar(range(len(resumen)), [r["costo_usd"] for r in resumen],
               color=cols, edgecolor="black", linewidth=0.6)
    axs[1].set_xticks(range(len(resumen)))
    axs[1].set_xticklabels(labels, rotation=18, ha="right", fontsize=7.5)
    axs[1].set_ylabel("USD millones (68.611 m² de losa)")
    axs[1].set_title("Costo total de entrepisos (USD millones)", fontsize=10, fontweight="bold")
    for i, r in enumerate(resumen):
        axs[1].text(i, r["costo_usd"] + 0.08, f"{r['costo_usd']:.2f}",
                    ha="center", fontsize=9, fontweight="bold",
                    color="#2e7d32" if r["costo_usd"] == min(r["costo_usd"] for r in resumen) else "black")

    fig.suptitle("Comparativa de sistemas estructurales de entrepiso — Edificio 18P+3SUB (CDE, PY 2026)\n"
                 "Grilla de pilares fija (continuidad S3→AZ) · precios CYPE/CAPACO 2025-26 · TC 6.100 Gs/USD",
                 fontsize=10, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    p = os.path.join(OUT, "comparativa_estructuras.png")
    fig.savefig(p, dpi=150)
    plt.close(fig)
    return p

def main():
    detalle, resumen = calcular()
    ruta_csv = escribir_csv(detalle, resumen)
    ruta_png = grafico(resumen)

    print("=" * 78)
    print(" COMPARATIVA DE SISTEMAS DE ENTREPISO — COSTO (CDE, PY 2026)")
    print(" Grilla de pilares FIJA · 68.611 m² de losa · TC 6.100 Gs/USD")
    print("=" * 78)
    print(f"{'#':<3}{'Sistema':<14}{'USD/m²':>9}{'Total MMUSD':>13}"
          f"{'Miles m³':>10}{'Miles t':>9}{'kN/m²':>8}{'Ahorro vs A':>13}")
    for r in resumen:
        ahorro = "—" if r["ahorro_vs_A"] is None else f"{r['ahorro_vs_A']:.1f}%"
        print(f"{r['ranking']:<3}{r['sistema']:<14}{r['costo_m2_usd']:>9.1f}"
              f"{r['costo_usd']:>13.2f}{r['conc_total']:>10.1f}"
              f"{r['acero_total']:>9.1f}{r['pp_media']:>8.1f}{ahorro:>13}")
    print("-" * 78)
    print("  * Peso propio = solo sistema de entrepiso (indicador de masa sísmica).")
    print("  * Columnas y núcleos: comunes (posición fija) -> excluidos.")
    print("  * Sistema E: viguetas solo en P01-P18; PB/subsuelos/azotea = pórtico (C).")
    print(f"[OK] {ruta_csv}")
    print(f"[OK] {ruta_png}")

    # ── Sensibilidad ──────────────────────────────────────────────
    filas = sensibilidad()
    ruta_scsv = escribir_sensibilidad_csv(filas)
    ruta_spng = grafico_sensibilidad(filas)
    print()
    print("=" * 78)
    print(" SENSIBILIDAD — PT 10-16 USD/m² y materiales ±15% (total MMUSD)")
    print("=" * 78)
    print(f"{'Escenario':<32}{'A':>7}{'D':>7}{'E':>7}  {'Ganador':<16}{'A vs D':>8}")
    for r in filas:
        print(f"{r['escenario']:<32}{r['A_total']:>7.2f}{r['D_total']:>7.2f}"
              f"{r['E_total']:>7.2f}  {r['ganador']:<16}{r['A_vs_D_pct']:>7.1f}%")
    print(f"[OK] {ruta_scsv}")
    print(f"[OK] {ruta_spng}")

if __name__ == "__main__":
    main()
