"""
====================================================================
 DISENO DE LOSA NERVADA / RETICULAR ALIVIANADA
 Edificio de Uso Mixto 18P + 3 Subsuelos | Ciudad del Este, Paraguay
====================================================================

 Metodologia:
  1) CALCULO MANUAL paso a paso bajo norma:
     - ACI 318-19 secc. 8.8 (two-way joist / reticular) y 9.8 (one-way)
     - ABNT NBR 6118:2014 secc. 13.2.4.1 (lajes nervuradas) y 14.7.7
  2) VERIFICACION CRUZADA con PyNite (FEM de barras) sobre la franja
     equivalente de un modulo (nervio + capa).

 La tesis documenta el procedimiento manual en LaTeX (anexo de
 calculo) y compara los resultados con el programa.

 OUTPUTS (calculo/outputs/):
  - losas_nervadas_resultados.json  -> valores para el anexo LaTeX
  - losas_nervadas_compare.csv      -> tabla de comparacion manual vs PyNite
====================================================================
"""

import csv
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modelo_estructural import LOSA_POR_NIVEL, CARGAS

from Pynite import FEModel3D

# ------------------------------------------------------------------
# 1. GEOMETRIA Y MATERIALES (desde modelo_estructural.py)
# ------------------------------------------------------------------
CANTO_TIPO = LOSA_POR_NIVEL["P01"]["canto"]          # 0.35 m
ESPESOR_EQ_TIPO = LOSA_POR_NIVEL["P01"]["espesor"]   # 0.19 m (m3/m2)
CAPA = 0.10                                          # capa de compresion (m)
NERVIO_W = 0.10                                      # ancho de nervio (m)
SEP = 0.60                                           # separacion de ejes (m)
CLARO_RIB = SEP - NERVIO_W                           # claro libre entre nervios

GAMMA = 25.0                                         # kN/m3 (NBR 6120)
FC = 30.0                                            # f'c = 30 MPa (H-30)
FY = 500.0                                           # fy = 500 MPa (CA-50)
EC = 4700.0 * math.sqrt(FC) / 1000.0                 # Ec = 4700 sqrt(f'c) [GPa]

LUZ = 7.875                                          # vano critico ala (m)
ANCHO_APOYO = 0.5                                    # ancho de apoyo (m)
LN = LUZ - ANCHO_APOYO                               # luz libre (m)

REC = 0.025                                          # recubrimiento losa (m)
PHI_FLEX = 0.90
PHI_CORT = 0.75

# Cargas caracteristicas (kN/m2) desde modelo_estructural
Q_RES = CARGAS["residencial"]        # 2.0
TABIQUERIA = CARGAS["tabiqueria"]    # 1.5
ACABADOS = CARGAS["acabados"]        # 1.0

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")


# ------------------------------------------------------------------
# 2. VERIFICACION DIMENSIONAL (normas)
# ------------------------------------------------------------------
def verificar_dimensiones():
    """Comprueba que la geometria cumple ACI 318-19 y NBR 6118."""
    checks = {}
    # ACI 318-19 9.8.1.2 / 8.8.1.2: ancho nervio >= 4 in = 101.6 mm
    checks["ACI_ancho_nervio_4in"] = (NERVIO_W * 1000 >= 100.0)
    # ACI 8.8.1.3 / 9.8.1.3: peralte nervio <= 3.5 x ancho
    peralte_nervio = CANTO_TIPO - CAPA
    checks["ACI_peralte_3.5b"] = (peralte_nervio <= 3.5 * NERVIO_W)
    # ACI 8.8.1.4 / 9.8.1.4: claro libre entre nervios <= 30 in = 762 mm
    checks["ACI_claro_30in"] = (CLARO_RIB * 1000 <= 762.0)
    # ACI 8.8.3.1: capa >= max(1/12 claro, 2 in = 50.8 mm)
    capa_min_aci = max(CLARO_RIB / 12.0, 0.0508)
    checks["ACI_capa_max"] = (CAPA >= capa_min_aci)
    # NBR 6118 13.2.4.1: nervio >= 5 cm ; capa >= max(1/15 claro, 4 cm)
    checks["NBR_nervio_5cm"] = (NERVIO_W * 100 >= 5.0)
    capa_min_nbr = max(CLARO_RIB / 15.0, 0.04)
    checks["NBR_capa_max"] = (CAPA >= capa_min_nbr)
    checks["NBR_esp_ejes_65cm"] = (SEP <= 0.65)  # dispensa verificacion de mesa
    checks["ACI_capa_min_m"] = round(capa_min_aci, 4)
    checks["NBR_capa_min_m"] = round(capa_min_nbr, 4)
    return checks


# ------------------------------------------------------------------
# 3. CARGAS Y COMBINACIONES (ELU / ELS)
# ------------------------------------------------------------------
def cargas():
    pp = ESPESOR_EQ_TIPO * GAMMA                      # peso propio losa
    g = pp + ACABADOS + TABIQUERIA                    # permanente total
    q = Q_RES                                         # sobrecarga de uso
    qu = 1.4 * g + 1.4 * q                            # ELU (NBR 8681)
    qs = g + q                                        # ELS caracteristica
    return dict(pp=pp, g=g, q=q, qu=qu, qs=qs)


# ------------------------------------------------------------------
# 4. DISENO A FLEXION (franja = 1 modulo de 0.60 m, viga continua)
# ------------------------------------------------------------------
def diseno_flexion(wu, L):
    d = CANTO_TIPO - REC - 0.008                      # altura util (estribo+barra)
    Mneg = wu * L ** 2 / 8.0                          # apoyo interior (2 vanos)
    Mpos = 9.0 * wu * L ** 2 / 128.0                  # tramo

    def as_flexion(Mu, b):
        Rn = Mu / (PHI_FLEX * b * d ** 2)             # kN/m2
        rho = (0.85 * FC / FY) * (1 - math.sqrt(1 - 2 * Rn / (0.85 * FC * 1000.0)))
        return rho * b * d * 1e6                      # mm2

    as_neg = as_flexion(Mneg, NERVIO_W)
    as_pos = as_flexion(Mpos, SEP)                    # seccion T, b = ancho modulo
    # cuantia minima (ACI 9.6.1.2) por nervio
    as_min = max(0.25 * math.sqrt(FC) / FY, 1.4 / FY) * (NERVIO_W * d) * 1e6
    return dict(d=d, Mneg=Mneg, Mpos=Mpos, as_neg=as_neg, as_pos=as_pos,
                as_min=as_min)


# ------------------------------------------------------------------
# 5. DISENO A CORTE (joist: +10% ACI 8.8.1.5 / 9.8.1.5)
# ------------------------------------------------------------------
def diseno_corte(wu, L, d):
    # Viga continua de 2 vanos iguales (coeficientes ACI / análisis):
    # apoyo exterior: 3wL/8 · apoyo interior: 5wL/8 (el maximo)
    Vmax = 5.0 * wu * L / 8.0                          # max en cara de apoyo interior
    Vu = Vmax - wu * d                                 # a distancia "d" de la cara
    vc = 1.1 * 0.17 * math.sqrt(FC) * (NERVIO_W * d) * 1000.0  # kN (+10% joist)
    phiVc = PHI_CORT * vc
    estribos = (Vu > phiVc)
    # estribos minimos cerca del apoyo (smax = d/2 = 0.16 m; se adopta 0.15)
    s = 0.15
    if estribos:
        av = 2 * (math.pi * 6.0 ** 2 / 4.0) * 1e-6          # 2 ramas O6 [m2]
        phiVs = PHI_CORT * av * FY * 1000.0 * d / s
    else:
        phiVs = None
    return dict(Vu=Vu, Vmax=Vmax, Vc=vc, phiVc=phiVc, estribos=estribos,
                s_estribo=s, phiVs=phiVs)


# ------------------------------------------------------------------
# 6. ELS — CONTROL DE ESPESOR Y FLECHA INSTANTANEA
# ------------------------------------------------------------------
def esl(wu, ws, L, d):
    # ACI Tabla 8.3.1.2 (dos direcciones, panel interior): h = ln/33, fy=420
    coef = 0.4 + FY / 700.0                            # ajuste por fy
    h_min = LN / 33.0 * coef
    ok_espesor = (CANTO_TIPO >= h_min)
    # Flecha instantanea: franja como viga continua (2 vanos), Ig seccion T
    e = EC * 1e6                                       # kPa
    area_capa = SEP * CAPA
    area_nervio = NERVIO_W * (CANTO_TIPO - CAPA)
    a_tot = area_capa + area_nervio
    yb = (area_capa * (CANTO_TIPO - CAPA / 2.0) +
          area_nervio * (CANTO_TIPO - CAPA) / 2.0) / a_tot
    ig = (SEP * CAPA ** 3 / 12.0 + area_capa * (CANTO_TIPO - CAPA / 2.0 - yb) ** 2 +
          NERVIO_W * (CANTO_TIPO - CAPA) ** 3 / 12.0 +
          area_nervio * (yb - (CANTO_TIPO - CAPA) / 2.0) ** 2)
    w_serv = ws * SEP                                  # kN/m a servicio
    delta = 0.0054 * w_serv * L ** 4 / (e * ig)        # m
    limite = L / 480.0
    return dict(h_min=h_min, ok_espesor=ok_espesor, yb=yb, ig=ig,
                delta=delta, limite=limite, ok_flecha=(delta <= limite))


# ------------------------------------------------------------------
# 7. DETALLES DE ARMADO — anclajes, corte de barras y malla (ACI §25.4)
# ------------------------------------------------------------------
def detalles():
    # Longitud de desarrollo (ACI 318-19 25.4.2.3a / NBR 6118 9.4.2)
    # ld = (fy·psi_t·psi_e·psi_s / (2.1·lambda·sqrt(f'c)))·db
    num = FY * 1.0 * 1.0
    ld_pos = (num * 0.8 / (2.1 * math.sqrt(FC))) * 14.0 / 1000.0   # 2Ø14 tramo
    ld_neg = (num * 1.3 * 0.8 / (2.1 * math.sqrt(FC))) * 18.0 / 1000.0  # 2Ø18 sup.
    # Corte de armadura negativa: 0.25·Ln desde la cara del apoyo
    corte_neg = 0.25 * LN
    # Malla retracción/temperatura en la capa (ACI 24.4.3.2): As = 0.0018·b·h
    as_temp = 0.0018 * 1.0 * CAPA * 1e6                 # mm2/m
    return dict(ld_pos=ld_pos, ld_neg=ld_neg, corte_neg=corte_neg,
                as_temp=as_temp)


# ------------------------------------------------------------------
# 8. VERIFICACION CRUZADA CON PyNite (2 vanos, franja equivalente)
# ------------------------------------------------------------------
def pynite_compare(wu, ws, L, d, ig):
    e = EC * 1e6                                       # kPa
    gmod = e / (2.0 * (1 + 0.2))
    model = FEModel3D()
    for i, x in enumerate([0.0, L, 2 * L]):
        model.add_node(f"N{i}", x, 0.0, 0.0)
    model.add_material("CONC", e, gmod, 0.2, 24.0)
    model.add_section("RIB", NERVIO_W * CANTO_TIPO, 1e-6, ig, 0.0)
    for i in range(2):
        model.add_member(f"M{i}", f"N{i}", f"N{i+1}", "CONC", "RIB")
        model.add_member_dist_load(f"M{i}", "FY", wu, wu, case="ELU")
        model.add_member_dist_load(f"M{i}", "FY", ws * SEP, ws * SEP, case="ELS")
    for n in ("N0", "N1", "N2"):
        model.def_support(n, True, True, True, True, True, False)
    model.add_load_combo("C-ELU", {"ELU": 1.0})
    model.add_load_combo("C-ELS", {"ELS": 1.0})
    model.analyze()
    mneg = min(model.members["M0"].min_moment("Mz", "C-ELU"),
               model.members["M1"].min_moment("Mz", "C-ELU"))
    mpos = max(model.members["M0"].max_moment("Mz", "C-ELU"),
               model.members["M1"].max_moment("Mz", "C-ELU"))
    vmax = max(model.members["M0"].max_shear("Fy", "C-ELU"),
               model.members["M1"].max_shear("Fy", "C-ELU"))
    dmax = model.members["M1"].max_deflection("dy", "C-ELS")
    if isinstance(dmax, tuple):
        dmax = dmax[1]
    return dict(mneg=mneg, mpos=mpos, vmax=vmax, dmax=dmax)


def main():
    os.makedirs(OUT, exist_ok=True)
    r = {}
    r["geometria"] = dict(canto=CANTO_TIPO, capa=CAPA, nervio=NERVIO_W,
                          separacion=SEP, claro_libre=CLARO_RIB,
                          espesor_equiv=ESPESOR_EQ_TIPO, luz=LUZ)
    r["materiales"] = dict(fc=FC, fy=FY, ec=round(EC, 2))
    r["dimensiones"] = verificar_dimensiones()
    c = cargas()
    r["cargas"] = {k: round(v, 3) for k, v in c.items()}
    wu = c["qu"] * SEP
    d = CANTO_TIPO - REC - 0.008
    f = diseno_flexion(wu, LUZ)
    r["flexion"] = {k: round(v, 4) if isinstance(v, float) else v
                    for k, v in f.items()}
    v = diseno_corte(wu, LUZ, f["d"])
    r["corte"] = {k: round(vv, 3) if isinstance(vv, float) else vv
                  for k, vv in v.items()}
    e = esl(wu, c["qs"], LUZ, f["d"])
    r["esl"] = {k: round(vv, 5) if isinstance(vv, float) else vv
                for k, vv in e.items()}
    dt = detalles()
    r["detalles"] = {k: round(vv, 4) if isinstance(vv, float) else vv
                     for k, vv in dt.items()}
    py = pynite_compare(wu, c["qs"], LUZ, f["d"], e["ig"])
    r["pynite"] = {k: round(vv, 4) if isinstance(vv, float) else vv
                   for k, vv in py.items()}

    # Tabla de comparacion
    filas = [
        ["M(-) apoyo int. (kN.m)", f["Mneg"], py["mneg"]],
        ["M(+) tramo (kN.m)", f["Mpos"], py["mpos"]],
        ["V max (kN)", v["Vmax"], py["vmax"]],
        ["Flecha ELS (mm)", e["delta"] * 1000, py["dmax"] * 1000],
    ]
    with open(os.path.join(OUT, "losas_nervadas_compare.csv"), "w",
              newline="", encoding="utf-8") as fcsv:
        wcsv = csv.writer(fcsv, delimiter=";")
        wcsv.writerow(["Magnitud", "Manual (ACI/NBR)", "PyNite (FEM)"])
        wcsv.writerows(filas)
    with open(os.path.join(OUT, "losas_nervadas_resultados.json"), "w",
              encoding="utf-8") as fjson:
        json.dump(r, fjson, ensure_ascii=False, indent=2)

    print("=== LOSA NERVADA - RESULTADOS ===")
    print("Geometria:", r["geometria"])
    print("Verif. dimensional:", {k: v for k, v in r["dimensiones"].items()
                                  if isinstance(v, bool)})
    print("Cargas kN/m2:", r["cargas"])
    print("Flexion:", r["flexion"])
    print("Corte:", r["corte"])
    print("ELS:", r["esl"])
    print("Detalles:", r["detalles"])
    print("PyNite:", r["pynite"])
    print("COMPARACION:")
    for fila in filas:
        print(f"  {fila[0]:<28} manual={fila[1]:>8.3f}  pynite={fila[2]:>8.3f}")
    print("JSON:", os.path.join(OUT, "losas_nervadas_resultados.json"))


if __name__ == "__main__":
    main()