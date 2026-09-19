"""
====================================================================
 MODELO DE DATOS ESTRUCTURAL (SDF) — FUENTE ÚNICA DE VERDAD
 Edificio de Uso Mixto 18P + 3 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | Versión: v1 (2026-09-09)
====================================================================

 Este módulo centraliza TODA la geometría del edificio en un único
 lugar. Todos los scripts de cálculo (grilla de pilares, cómputo de
 cargas, dimensionamiento, armaduras, viento) DEBEN importar desde
 aquí para garantizar consistencia absoluta entre disciplinas.

 CONTENIDO:
  1. Geometría general (huella, grilla definitiva, núcleos, pasillo)
  2. Niveles (cotas, alturas, función)
  3. Losas (sistema postensado, espesores por nivel)
  4. Materiales (H°A°, acero, cargas)
  5. Recintos por nivel (para el GA de pilares)
  6. Exportación a JSON estandarizado (para Revit / otros scripts)

 GRILLA ESTRUCTURAL DEFINITIVA (AGENTS.md §10.0 y §12.3):
   Ejes X: [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
            63.88, 71.75, 79.63, 87.50]
     - Alas: 4 vanos de 7.875m (2.5→34 y 56→87.5)
     - N1: 7m (34→41) · Pasillo técnico: 8m (41→49) · N2: 7m (49→56)
   Ejes Y: [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]
     - Frente: 2 vanos de 7m (3→17) · Núcleos: 9m (17→26)
     - Fondo: 2 vanos de 7m (26→40)
   Los 4 bordes de núcleos (X:34, 41, 49, 56 / Y:17, 26) son ejes exactos.

 USO:
   from modelo_estructural import ESTRUCTURA
   xs, ys = ESTRUCTURA['grilla']['XS'], ESTRUCTURA['grilla']['YS']
   niveles = ESTRUCTURA['niveles']
====================================================================
"""

import json
import os

# ──────────────────────────────────────────────────────────────────
# 1. GEOMETRÍA GENERAL
# ──────────────────────────────────────────────────────────────────
TERRENO = dict(frente=90.0, profundidad=40.0)
HUELLA = dict(x0=2.5, x1=87.5, y0=3.0, y1=40.0,
              ancho=85.0, profundidad=37.0, area=3145.0)

# Grilla estructural definitiva (definida en AGENTS.md §10.0)
XS = [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
      63.88, 71.75, 79.63, 87.50]
YS = [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

# Núcleos gemelos H°A° rotados 90° (2 asc + escalera RF + shaft c/u)
NUCLEOS = [
    dict(id="N1", x0=34.0, x1=41.0, y0=17.0, y1=26.0, ancho=7.0, alto=9.0, area=63.0),
    dict(id="N2", x0=49.0, x1=56.0, y0=17.0, y1=26.0, ancho=7.0, alto=9.0, area=63.0),
]

# Pasillo técnico central (ducto RSU Ø500 + shafts)
PASILLO_TECNICO = dict(x0=41.0, x1=49.0, y0=17.0, y1=26.0, ancho=8.0, alto=9.0, area=72.0)

# Pozos de luz (planta tipo)
POZOS_LUZ = [
    dict(id="A", x0=5.0, x1=19.0, y0=18.0, y1=25.0, area=98.0),
    dict(id="B", x0=71.0, x1=85.0, y0=18.0, y1=25.0, area=98.0),
]

# ──────────────────────────────────────────────────────────────────
# 2. NIVELES (cota, altura de entrepiso, función)
#    ALTURA_RESIDENCIAL = 3.35 m = 3.00 m libres (piso a cielo raso,
#    decisión 2026-09-10) + canto losa nervurada 0.35 m (AGENTS.md §10.0)
# ──────────────────────────────────────────────────────────────────
NIVELES = [
    dict(id="S3", cota=-10.50, altura=3.50, funcion="cocheras", plazas=98),
    dict(id="S2", cota=-7.00,  altura=3.50, funcion="cocheras", plazas=98),
    dict(id="S1", cota=-3.50,  altura=3.50, funcion="cocheras+tecnicas", plazas=82),
    dict(id="PB", cota=0.00,   altura=4.00, funcion="comercial+servicios", plazas=None),
]
ALTURA_RESIDENCIAL = 3.35  # 3.00 m libres (piso a cielo raso) + canto 0.35
for p in range(1, 19):
    NIVELES.append(dict(id=f"P{p:02d}", cota=4.00 + (p - 1) * ALTURA_RESIDENCIAL,
                        altura=ALTURA_RESIDENCIAL, funcion="residencial", plazas=None))
NIVELES.append(dict(id="AZ", cota=4.00 + 18 * ALTURA_RESIDENCIAL,
                    altura=2.20, funcion="azotea-tecnica", plazas=None))

# Índices por id para acceso rápido
NIVEL_POR_ID = {n["id"]: n for n in NIVELES}

# ──────────────────────────────────────────────────────────────────
# 3. LOSAS — SISTEMA NERVURADO / RETICULAR ALIVIANADO (AGENTS.md §10.0,
#    ADOPTADO 2026-09-10 por ser el más económico de la comparativa)
#    canto   = altura física total (capa + casetón) → geometría 3D/IFC
#    espesor = espesor EQUIVALENTE de hormigón (m³/m²) → peso propio
# ──────────────────────────────────────────────────────────────────
LOSAS = [
    dict(ids=["S1", "S2", "S3"], sistema="nervurada_reticular",
         canto=0.45, espesor=0.22, nota="canto 45 cm (capa 10 + casetón 35)"),
    dict(ids=["PB"], sistema="nervurada_reticular",
         canto=0.45, espesor=0.22, nota="canto 45 cm (gran luz)"),
    dict(ids=["P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09",
              "P10", "P11", "P12", "P13", "P14", "P15", "P16", "P17", "P18"],
         sistema="nervurada_reticular",
         canto=0.35, espesor=0.19, nota="canto 35 cm (capa 10 + casetón 25)"),
    dict(ids=["AZ"], sistema="nervurada_reticular",
         canto=0.35, espesor=0.19, nota="canto 35 cm (azotea)"),
]

LOSA_POR_NIVEL = {}
for l in LOSAS:
    for nid in l["ids"]:
        LOSA_POR_NIVEL[nid] = l

# ──────────────────────────────────────────────────────────────────
# 4. MATERIALES Y CARGAS DE REFERENCIA (se ajustarán con NBR/ASCE)
# ──────────────────────────────────────────────────────────────────
MATERIALES = dict(
    hormigon=dict(nombre="H-30", fc=30.0, fcd=21.4, gamma=25.0),   # MPa, kN/m³
    acero=dict(nombre="CA-50", fy=500.0, fyd=434.8),               # MPa (NBR 6118)
    recubrimiento_pilares=0.04,                                    # m
)

# Cargas características por uso (kN/m²) — verificar con NBR 6120/ASCE 7
CARGAS = dict(
    residencial=2.0,       # sobrecarga
    comercial=3.0,         # sobrecarga
    cocheras=3.0,          # sobrecarga
    tabiqueria=1.5,        # carga repartida equivalente
    acabados=1.0,          # piso + cielorraso
    peso_propio_ajuste=0.0,
)

# ──────────────────────────────────────────────────────────────────
# 5. RECINTOS POR NIVEL (para el GA de pilares)
#    Se completan importando los exports de los scripts de layout.
# ──────────────────────────────────────────────────────────────────
RECINTOS = {
    "PB": [],       # se completará desde ga_master_planta_baja.py
    "PT": [],       # recintos típicos (de los 3 layouts A/B/C)
    "S": [],        # subsuelos (libres de cocheras = zonas de plazas)
}


# ──────────────────────────────────────────────────────────────────
# 6. EXPORTACIÓN A JSON (para Revit y scripts de cálculo)
# ──────────────────────────────────────────────────────────────────
def exportar_json(ruta=None):
    """Serializa el modelo a JSON estandarizado."""
    data = dict(
        proyecto="Edificio de Uso Mixto 18P + 3 Subsuelos - CDE, Paraguay",
        norma="NBR 6123 / NBR 6118 / ASCE 7-22 / Eurocodigo 1",
        terreno=TERRENO,
        huella=HUELLA,
        grilla=dict(XS=XS, YS=YS,
                    vanos_X=[round(xs - XS[i], 3) for i, xs in enumerate(XS[1:])],
                    vanos_Y=[round(ys - YS[i], 3) for i, ys in enumerate(YS[1:])]),
        nucleos=NUCLEOS,
        pasillo_tecnico=PASILLO_TECNICO,
        pozos_luz=POZOS_LUZ,
        niveles=NIVELES,
        losas=LOSAS,
        materiales=MATERIALES,
        cargas=CARGAS,
        recintos=RECINTOS,
    )
    if ruta is None:
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "modelo_estructural.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return ruta


# Estructura consolidada para import conveniente
ESTRUCTURA = dict(
    terreno=TERRENO,
    huella=HUELLA,
    grilla=dict(XS=XS, YS=YS),
    nucleos=NUCLEOS,
    pasillo_tecnico=PASILLO_TECNICO,
    pozos_luz=POZOS_LUZ,
    niveles=NIVELES,
    nivel_por_id=NIVEL_POR_ID,
    losas=LOSAS,
    losa_por_nivel=LOSA_POR_NIVEL,
    materiales=MATERIALES,
    cargas=CARGAS,
    recintos=RECINTOS,
)


if __name__ == "__main__":
    ruta = exportar_json()
    print(f"[OK] Modelo estructural exportado: {ruta}")
    print(f"     Grilla X: {len(XS)} ejes | Grilla Y: {len(YS)} ejes")
    print(f"     Niveles: {len(NIVELES)} | Núcleos: {len(NUCLEOS)}")