"""
====================================================================
 GENERADOR DE DXF BASE — SUBSUELO 3 (COCHERAS)
 Edificio de Uso Mixto 18P + 2 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | Flujo manual en AutoCAD
====================================================================

 Genera un archivo DXF (formato R2000, unidades METROS) con el
 "esqueleto" del Subsuelo 3 para editarlo en AutoCAD 2024:

   TESIS-HUELLA        → perímetro del edificio (X:2.5→87.5 / Y:3→40)
   TESIS-GRILLA        → grilla estructural óptima (12 ejes X, 6 ejes Y)
   TESIS-EJES          → etiquetas de ejes (1–12 y A–F)
   TESIS-NUCLEOS       → 2 núcleos H°A° gemelos (N1 / N2)
   TESIS-PASILLO       → pasillo técnico central (ducto RSU + servicios)
   TESIS-RAMPAS        → doble rampa esquina-esquina (SE entrada / NO salida)
   TESIS-PILARES       → pilares 90x90 cm en intersecciones de grilla
   TESIS-ZONAS         → zonas de estacionamiento de referencia (punteado)
   TESIS-COCHERAS      → CAPA DEL USUARIO: dibujar aquí los rectángulos de
                         cada cochera con el comando RECTANG (módulo 2.5x5.0 m)
   TESIS-INSTRUCCIONES → texto de ayuda dentro del dibujo

 FLUJO DE TRABAJO:
   1) python generar_dxf_subsuelo.py      → outputs/subsuelo_3_base.dxf
   2) Abrir en AutoCAD, dibujar las cocheras en la capa TESIS-COCHERAS
      (comando RECTANG) y GUARDAR como DXF (formato R2000 / ASCII).
   3) python extraer_cocheras_dxf.py      → lee el DXF y exporta los
      bounding boxes como STALLS_MANUALES (JSON + .py para ga_subsuelo_3).

 REQUIERE: ezdxf (pip install ezdxf)

 OUTPUT: outputs/subsuelo_3_base.dxf
====================================================================
"""

import os
import sys

import ezdxf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ga_subsuelo_3 as ga

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
DXF_PATH = os.path.join(OUT_DIR, "subsuelo_3_base.dxf")


def generar_dxf():
    os.makedirs(OUT_DIR, exist_ok=True)

    doc = ezdxf.new("R2000", setup=True)
    doc.units = 6  # 6 = metros (INSUNITS)

    # ---------------- Capas ----------------
    capas = [
        ("TESIS-HUELLA", 7),            # blanco/negro
        ("TESIS-GRILLA", 8),            # gris
        ("TESIS-EJES", 7),
        ("TESIS-NUCLEOS", 5),           # azul
        ("TESIS-PASILLO", 4),           # cian
        ("TESIS-RAMPAS", 1),            # rojo
        ("TESIS-PILARES", 2),           # amarillo
        ("TESIS-ZONAS", 6, "DASHED"),   # magenta punteado
        ("TESIS-COCHERAS", 3),          # VERDE = capa del usuario
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

    # ---------------- Huella ----------------
    rect("TESIS-HUELLA", ga.X_MIN, ga.Y_MIN, ga.X_MAX, ga.Y_MAX)

    # ---------------- Grilla estructural ----------------
    for x in ga.XS:
        msp.add_line((x, ga.Y_MIN - 1.5), (x, ga.Y_MAX + 1.5),
                     dxfattribs={"layer": "TESIS-GRILLA"})
    for y in ga.YS:
        msp.add_line((ga.X_MIN - 1.5, y), (ga.X_MAX + 1.5, y),
                     dxfattribs={"layer": "TESIS-GRILLA"})

    # Etiquetas de ejes
    for i, x in enumerate(ga.XS):
        texto("TESIS-EJES", x, ga.Y_MIN - 2.0, 0.7, str(i + 1))
    for i, y in enumerate(ga.YS):
        texto("TESIS-EJES", ga.X_MIN - 2.0, y - 0.35, 0.7, chr(65 + i))

    # ---------------- Zonas de estacionamiento de referencia ----------------
    for z in ga.ZONAS_PARKING:
        rect("TESIS-ZONAS", z['x0'], z['y0'], z['x1'], z['y1'])

    # ---------------- Pilares estructurales (90x90 cm) ----------------
    pilares, _ = ga.generar_pilares()
    for (px0, py0, w, h) in pilares:
        rect("TESIS-PILARES", px0, py0, px0 + w, py0 + h)

    # ---------------- Rampas esquina-esquina ----------------
    for rampa, nombre in [
        (ga.RAMPA_ENTRADA, "RAMPA ENTRADA SE"),
        (ga.RAMPA_SALIDA, "RAMPA SALIDA NO"),
    ]:
        rect("TESIS-RAMPAS", rampa['x0'], rampa['y0'], rampa['x1'], rampa['y1'])
        texto("TESIS-RAMPAS", (rampa['x0'] + rampa['x1']) / 2,
              (rampa['y0'] + rampa['y1']) / 2, 0.6, nombre)

    # ---------------- Pasillo técnico central ----------------
    p = ga.PASILLO_TECNICO
    rect("TESIS-PASILLO", p['x0'], p['y0'], p['x1'], p['y1'])
    texto("TESIS-PASILLO", (p['x0'] + p['x1']) / 2, (p['y0'] + p['y1']) / 2,
          0.6, "PASILLO TECNICO (ducto RSU)")

    # ---------------- Núcleos ----------------
    for c in ga.NUCLEOS:
        rect("TESIS-NUCLEOS", c['x0'], c['y0'], c['x1'], c['y1'])
        texto("TESIS-NUCLEOS", (c['x0'] + c['x1']) / 2, (c['y0'] + c['y1']) / 2,
              0.8, f"NUCLEO {c['nombre']}")

    # ---------------- Instrucciones (sobre el plano, fuera de la huella) ----------------
    instr = [
        "INSTRUCCIONES:",
        "1) Dibuje CADA cochera como un rectangulo (comando RECTANG)",
        "   en la capa TESIS-COCHERAS (verde). Modulo 2.5 x 5.0 m.",
        "2) Deje 6.0 m de pasillo entre filas enfrentadas.",
        "3) Guarde el archivo como DXF (formato R2000 / ASCII).",
        "4) Ejecute: python extraer_cocheras_dxf.py  [ruta_al_dxf]",
        "   Esto extraera todos los rectangulos de TESIS-COCHERAS",
        "   y los exportara como STALLS_MANUALES.",
        "Coordenadas en METROS. Huella X:2.5-87.5 / Y:3.0-40.0.",
    ]
    ytxt = ga.Y_MAX + 3.5
    for i, line in enumerate(instr):
        texto("TESIS-INSTRUCCIONES", ga.X_MIN, ytxt - i * 0.9, 0.6, line)

    # ---------------- Guardar ----------------
    doc.saveas(DXF_PATH)
    print(f"[OK] DXF generado (ezdxf): {DXF_PATH}")
    print(f"     Pilares: {len(pilares)} | Zonas: {len(ga.ZONAS_PARKING)} | "
          f"Capas: {', '.join(c[0] for c in capas)}")
    return DXF_PATH


if __name__ == "__main__":
    generar_dxf()
