"""
====================================================================
 GENERADOR DE DXF BASE — PLANTA BAJA (PB) PARA TRAZADO EN AutoCAD
 Edificio de Uso Mixto 18P + 3 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | Refinamiento manual profesional (§10.7)
====================================================================

 Genera un archivo DXF (R2000, unidades METROS) con la BASE del plano
 de Planta Baja para dibujar la distribución arquitectónica de forma
 PROFESIONAL en AutoCAD 2024 (los plots PNG de matplotlib NO son
 entregables de planos — decisión 2026-09-10).

 La base incluye SOLO lo verificado y definitivo:
   TESIS-HUELLA    → perímetro (X:2.5→87.5 / Y:3.0→40.0)
   TESIS-GRILLA    → grilla estructural óptima (12 ejes X, 6 ejes Y)
   TESIS-EJES      → etiquetas 1–12 y A–F
   TESIS-NUCLEOS   → 2 núcleos H°A° gemelos N1/N2 (7m×9m, rotados 90°)
   TESIS-PASILLO   → pasillo técnico central de servicios (§9.2)
   TESIS-PILARES   → 72 pilares 90×90 cm (sección PB, grilla completa)
   TESIS-PROGRAMA  → perímetros de zonas definitivas fijas (§9.3) en
                     línea punteada de REFERENCIA: Administración & BMS,
                     Sanitarios + PMR, Business Center, Depósito RSU,
                     rampa y pasaje vehicular.
   TESIS-COMERCIAL → frente comercial FLEXIBLE (Y:3→17) para distribuir
                     salones/lobby/gimnasio/cafetería/dársena en AutoCAD.
   TESIS-ARQ-USUARIO → CAPA DEL USUARIO (verde): dibujar aquí la
                     distribución arquitectónica definitiva.
   TESIS-INSTRUCCIONES → notas de ayuda.

 NOTAS:
   - Subestación ANDE y Reservorio PCI+POTABLE: las coordenadas de
     AGENTS §9.2 (X:49.5→59.5) SOLAPAN el núcleo N2 (X:49→56). Se
     omiten de la base para que las ubiques correctamente al dibujar.
   - Los salones comerciales 1–5, lobby, gimnasio/SUM, cafetería y
     dársena se distribuyen libremente en el frente (TESIS-COMERCIAL).

 FLUJO:
   1) python generar_dxf_planta_baja.py → outputs/planta_baja_base.dxf
   2) Abrir en AutoCAD 2024 y dibujar la distribución en la capa
      TESIS-ARQ-USUARIO (verde). Guardar DXF R2000/ASCII.
   3) Importar en Revit 2024 como underlay (Insert > Link CAD).

 REQUIERE: ezdxf (pip install ezdxf)
 OUTPUT: outputs/planta_baja_base.dxf
====================================================================
"""

import os

import ezdxf

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
DXF_PATH = os.path.join(OUT_DIR, "planta_baja_base.dxf")

# Huella y grilla (AGENTS §10.0)
X_MIN, X_MAX = 2.5, 87.5
Y_MIN, Y_MAX = 3.0, 40.0
XS = [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
      63.88, 71.75, 79.63, 87.50]
YS = [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

# Núcleos y pasillo técnico (§9.2)
NUCLEOS = [
    dict(id="N1", x0=34.0, x1=41.0, y0=17.0, y1=26.0),
    dict(id="N2", x0=49.0, x1=56.0, y0=17.0, y1=26.0),
]
PASILLO_TECNICO = dict(x0=40.5, x1=49.5, y0=25.0, y1=40.0)

# Zonas definitivas FIJAS de referencia (§9.3 / §9.2)
ZONAS_PROGRAMA = [
    dict(nombre="ADMINISTRACION & BMS (380 m2)", x0=2.5, x1=40.5, y0=18.0, y1=28.0),
    dict(nombre="SANITARIOS PUB + PMR + LACTARIO (228)", x0=21.5, x1=40.5, y0=28.0, y1=40.0),
    dict(nombre="BUSINESS CENTER + COWORKING (200)", x0=49.5, x1=69.5, y0=30.0, y1=40.0),
    dict(nombre="DEPOSITO RSU (228)", x0=2.5, x1=21.5, y0=28.0, y1=40.0),
    dict(nombre="RAMPA → S1 (6m, 2 carriles)", x0=81.5, x1=87.5, y0=33.0, y1=40.0),
    dict(nombre="PASAJE VEHICULAR (ingreso ESTE)", x0=81.5, x1=87.5, y0=26.0, y1=33.0),
]

# Frente comercial FLEXIBLE (a distribuir en AutoCAD)
COMERCIAL = dict(x0=X_MIN, x1=X_MAX, y0=3.0, y1=17.0)

S_PILAR = 0.9  # sección pilar en PB (m) — AGENTS §12.2


def generar_dxf():
    os.makedirs(OUT_DIR, exist_ok=True)

    doc = ezdxf.new("R2000", setup=True)
    doc.units = 6  # metros

    capas = [
        ("TESIS-HUELLA", 7),
        ("TESIS-GRILLA", 8),
        ("TESIS-EJES", 7),
        ("TESIS-NUCLEOS", 5),            # azul
        ("TESIS-PASILLO", 4),            # cian
        ("TESIS-PILARES", 2),            # amarillo
        ("TESIS-PROGRAMA", 6, "DASHED"), # magenta punteado (referencia)
        ("TESIS-COMERCIAL", 1, "DASHDOT"),  # rojo (frente flexible)
        ("TESIS-ARQ-USUARIO", 3),        # VERDE = capa del usuario
        ("TESIS-INSTRUCCIONES", 1),
    ]
    for c in capas:
        if len(c) == 3:
            doc.layers.add(c[0], color=c[1], linetype=c[2])
        else:
            doc.layers.add(c[0], color=c[1])

    msp = doc.modelspace()

    def rect(layer, x0, y0, x1, y1):
        msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)],
                           close=True, dxfattribs={"layer": layer})

    def texto(layer, x, y, h, txt):
        msp.add_text(txt, height=h, dxfattribs={"layer": layer}).set_placement((x, y))

    # Huella
    rect("TESIS-HUELLA", X_MIN, Y_MIN, X_MAX, Y_MAX)

    # Grilla
    for x in XS:
        msp.add_line((x, Y_MIN - 1.5), (x, Y_MAX + 1.5),
                     dxfattribs={"layer": "TESIS-GRILLA"})
    for y in YS:
        msp.add_line((X_MIN - 1.5, y), (X_MAX + 1.5, y),
                     dxfattribs={"layer": "TESIS-GRILLA"})
    for i, x in enumerate(XS):
        texto("TESIS-EJES", x, Y_MIN - 2.0, 0.7, str(i + 1))
    for i, y in enumerate(YS):
        texto("TESIS-EJES", X_MIN - 2.0, y - 0.35, 0.7, chr(65 + i))

    # Núcleos
    for c in NUCLEOS:
        rect("TESIS-NUCLEOS", c["x0"], c["y0"], c["x1"], c["y1"])
        texto("TESIS-NUCLEOS", (c["x0"] + c["x1"]) / 2, (c["y0"] + c["y1"]) / 2,
              0.8, "NUCLEO %s" % c["id"])

    # Pasillo técnico
    p = PASILLO_TECNICO
    rect("TESIS-PASILLO", p["x0"], p["y0"], p["x1"], p["y1"])
    texto("TESIS-PASILLO", (p["x0"] + p["x1"]) / 2, (p["y0"] + p["y1"]) / 2,
          0.6, "PASILLO TECNICO")

    # Pilares (72 = grilla completa XS×YS, sección PB 90×90)
    n_pil = 0
    for x in XS:
        for y in YS:
            rect("TESIS-PILARES", x - S_PILAR / 2, y - S_PILAR / 2,
                 x + S_PILAR / 2, y + S_PILAR / 2)
            n_pil += 1

    # Zonas de programa fijas (referencia punteada)
    for z in ZONAS_PROGRAMA:
        rect("TESIS-PROGRAMA", z["x0"], z["y0"], z["x1"], z["y1"])
        texto("TESIS-PROGRAMA", (z["x0"] + z["x1"]) / 2, (z["y0"] + z["y1"]) / 2,
              0.55, z["nombre"])

    # Frente comercial flexible
    c = COMERCIAL
    rect("TESIS-COMERCIAL", c["x0"], c["y0"], c["x1"], c["y1"])
    texto("TESIS-COMERCIAL", (c["x0"] + c["x1"]) / 2, c["y0"] + 0.8, 0.8,
          "FRENTE COMERCIAL FLEXIBLE — DISTRIBUIR (salones, lobby, gym, cafeteria, darsena)")

    # Instrucciones
    instr = [
        "PLANTA BAJA — BASE PARA TRAZADO PROFESIONAL EN AutoCAD 2024",
        "1) Dibuje la distribucion arquitectonica en la capa TESIS-ARQ-USUARIO (verde).",
        "2) Zonas punteadas (magenta) = periodos definitivos fijos de referencia.",
        "3) El frente Y:3->17 (rojo) es FLEXIBLE: distribuya salones 1-5, lobby,",
        "   gimnasio/SUM (~120), cafeteria (~40) y darsena (~40).",
        "4) SUBESTACION ANDE y RESERVORIO PCI+POTABLE: NO incluidos porque las",
        "   coords de AGENTS 9.2 (X:49.5->59.5) solapan el nucleo N2. Ubicarlos",
        "   en el fondo central (X:56->66 / Y:18->30 aprox) o donde definas.",
        "5) Pilares 90x90 cm = seccion de PB (disminuye en altura: 80/70/60).",
        "6) Coordenadas en METROS. Guardar DXF R2000 / ASCII.",
        "7) Importar en Revit 2024 como underlay (Insert > Link CAD).",
    ]
    ytxt = Y_MAX + 3.5
    for i, line in enumerate(instr):
        texto("TESIS-INSTRUCCIONES", X_MIN, ytxt - i * 0.9, 0.6, line)

    doc.saveas(DXF_PATH)
    print(f"[OK] DXF generado (ezdxf): {DXF_PATH}")
    print(f"     Pilares: {n_pil} | Zonas fijas: {len(ZONAS_PROGRAMA)} | "
          f"Capas: {', '.join(c[0] for c in capas)}")
    return DXF_PATH


if __name__ == "__main__":
    generar_dxf()