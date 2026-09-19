#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TESIS DE GRADO — EDIFICIO DE USO MIXTO 18 PISOS + 3 SUBSUELOS (CIUDAD DEL ESTE)
Script: generar_dxf_profesional.py
Propósito: Generar el archivo CAD DXF profesional en metros (ISO 13567 / AIA CAD)
           con el terreno real en UTM 21J, coordenadas locales, zonificación PB,
           huella de torre, retiros, cotas y rótulo/carátula de plano ISO 19650.
===============================================================================
"""

import os
import ezdxf
from ezdxf.units import PaperSpaceUnits

# Rutas de salida
WIP_DIR = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\01_WIP\01.01_ARQ"
PUB_DIR = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\03_PUBLISHED\03.01_Planos"

os.makedirs(WIP_DIR, exist_ok=True)
os.makedirs(PUB_DIR, exist_ok=True)

FILE_NAME = "TESIS-ARQ-GEN-DR-001_Planimetria_y_Zonificacion.dxf"
PATH_WIP = os.path.join(WIP_DIR, FILE_NAME)
PATH_PUB = os.path.join(PUB_DIR, FILE_NAME)


def crear_dxf_profesional():
    # 1. Crear documento DXF R2018
    doc = ezdxf.new('R2018', setup=True)
    doc.header['$INSUNITS'] = 6  # 6 = Metros

    # 2. Definir Capas (ISO 13567 / AIA Standard)
    capas = [
        ("C-PROP-LINE", 3, "Continuous", 0.50, "Límite Catastral Terreno (7.618,49 m²)"),
        ("C-PROP-VERT", 2, "Continuous", 0.25, "Vértices UTM P1-P4"),
        ("C-PROP-TEXT", 7, "Continuous", 0.25, "Textos y Cotas del Terreno"),
        ("C-SETB-LINE", 1, "DASHED", 0.25, "Línea de Retiros Reglamentarios (3m/2m)"),
        ("A-FOOT-PB", 4, "Continuous", 0.35, "Huella Edificable PB (3.145,00 m²)"),
        ("A-FOOT-TOWR", 5, "Continuous", 0.35, "Huella Torre Residencial (1.440,00 m²)"),
        ("A-WALL-CORE", 251, "Continuous", 0.50, "Núcleos Estructurales H°A° (7x9m c/u)"),
        ("A-ZONE-COMM", 30, "Continuous", 0.25, "Locales Comerciales PB (1.850 m²)"),
        ("A-ZONE-LOBBY", 40, "Continuous", 0.25, "Lobby Principal Residencial (250 m²)"),
        ("A-ZONE-SERV", 140, "Continuous", 0.25, "Bloque Técnico, RSU & Rampa Subsuelos"),
        ("A-ANNO-DIMS", 2, "Continuous", 0.18, "Acotaciones del Proyecto"),
        ("A-ANNO-TEXT", 7, "Continuous", 0.25, "Textos de Espacios y Especificaciones"),
        ("G-TITLE-BLOCK", 7, "Continuous", 0.35, "Carátula Rótulo ISO 19650 (Formato A1)")
    ]

    for name, color, linetype, lineweight, desc in capas:
        layer = doc.layers.add(name=name, color=color, linetype=linetype)
        layer.description = desc
        layer.lineweight = int(lineweight * 100)

    msp = doc.modelspace()

    # --- 3. GEOMETRÍA DEL TERRENO EN COORDENADAS LOCALES (P1 EN 0,0) ---
    # P1 (0,0), P2 (117.27, 0), P3 (133.10, 42.17), P4 (35.52, 77.97)
    p1 = (0.0, 0.0)
    p2 = (117.27, 0.0)
    p3 = (133.10, 42.17)
    p4 = (35.52, 77.97)
    pts_terreno = [p1, p2, p3, p4]

    # Polígono Terreno
    poly_terreno = msp.add_lwpolyline(pts_terreno, close=True, dxfattribs={'layer': 'C-PROP-LINE'})
    poly_terreno.dxf.const_width = 0.35

    # Vértices y Coordenadas UTM WGS84
    vertices_data = [
        ("P1", p1, "E: 737721.76 | N: 7176185.26", "Vértice Agudo 61,44°"),
        ("P2", p2, "E: 737837.53 | N: 7176203.96", "Frente Principal 117,27m"),
        ("P3", p3, "E: 737853.36 | N: 7176246.13", "Esquina Fondo Este"),
        ("P4", p4, "E: 737755.78 | N: 7176281.93", "Esquina Fondo Norte")
    ]

    for label, pos, utm_txt, desc in vertices_data:
        msp.add_circle(pos, radius=0.8, dxfattribs={'layer': 'C-PROP-VERT'})
        msp.add_circle(pos, radius=0.2, dxfattribs={'layer': 'C-PROP-VERT'})
        msp.add_text(f"{label} ({desc})", dxfattribs={'layer': 'C-PROP-TEXT', 'height': 1.2}).set_placement((pos[0] + 1.5, pos[1] + 1.5))
        msp.add_text(utm_txt, dxfattribs={'layer': 'C-PROP-TEXT', 'height': 0.8}).set_placement((pos[0] + 1.5, pos[1] - 1.0))

    # --- 4. HUELLA EDIFICABLE DE PLANTA BAJA (85.00m x 37.00m = 3.145,00 m²) ---
    x0, y0 = 5.0, 5.0
    bw, bh = 85.0, 37.0
    pb_pts = [(x0, y0), (x0 + bw, y0), (x0 + bw, y0 + bh), (x0, y0 + bh)]

    poly_pb = msp.add_lwpolyline(pb_pts, close=True, dxfattribs={'layer': 'A-FOOT-PB'})
    poly_pb.dxf.const_width = 0.25

    # --- 5. HUELLA DE TORRE RESIDENCIAL (48.00m x 30.00m = 1.440,00 m²) ---
    tx0, ty0 = x0 + 18.5, y0 + 3.5
    tw, th = 48.0, 30.0
    torre_pts = [(tx0, ty0), (tx0 + tw, ty0), (tx0 + tw, ty0 + th), (tx0, ty0 + th)]

    poly_torre = msp.add_lwpolyline(torre_pts, close=True, dxfattribs={'layer': 'A-FOOT-TOWR'})
    poly_torre.dxf.const_width = 0.20

    # --- 6. NÚCLEOS ESTRUCTURALES H°A° (2x Gemelos 7x9m = 126 m²) ---
    # Núcleo A (7m x 9m)
    nc1_pts = [(x0 + 25.0, y0 + 3.0), (x0 + 32.0, y0 + 3.0), (x0 + 32.0, y0 + 12.0), (x0 + 25.0, y0 + 12.0)]
    poly_nc1 = msp.add_lwpolyline(nc1_pts, close=True, dxfattribs={'layer': 'A-WALL-CORE'})
    poly_nc1.dxf.const_width = 0.30

    # Núcleo B (9m x 7m)
    nc2_pts = [(x0 + 48.0, y0 + 3.0), (x0 + 57.0, y0 + 3.0), (x0 + 57.0, y0 + 10.0), (x0 + 48.0, y0 + 10.0)]
    poly_nc2 = msp.add_lwpolyline(nc2_pts, close=True, dxfattribs={'layer': 'A-WALL-CORE'})
    poly_nc2.dxf.const_width = 0.30

    # Textos de Núcleos
    msp.add_text("NÚCLEO 1 H°A° (7x9m)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((x0 + 25.5, y0 + 7.0))
    msp.add_text("NÚCLEO 2 H°A° (9x7m)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((x0 + 48.5, y0 + 6.0))

    # --- 7. ZONIFICACIÓN DE LOCALES COMERCIALES PB ---
    # Megastore Comercial (1.050 m²)
    ms_pts = [(x0 + 40.0, y0 + 14.0), (x0 + 85.0, y0 + 14.0), (x0 + 85.0, y0 + 37.0), (x0 + 40.0, y0 + 37.0)]
    msp.add_lwpolyline(ms_pts, close=True, dxfattribs={'layer': 'A-ZONE-COMM'})
    msp.add_text("MEGASTORE COMERCIAL (1.050,00 m²)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.2}).set_placement((x0 + 45.0, y0 + 25.0))

    # Local Comercial 2 (450 m²)
    l2_pts = [(x0 + 20.0, y0 + 14.0), (x0 + 40.0, y0 + 14.0), (x0 + 40.0, y0 + 37.0), (x0 + 20.0, y0 + 37.0)]
    msp.add_lwpolyline(l2_pts, close=True, dxfattribs={'layer': 'A-ZONE-COMM'})
    msp.add_text("LOCAL 2 (450,00 m²)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.0}).set_placement((x0 + 22.0, y0 + 25.0))

    # Local Comercial 1 (350 m²)
    l1_pts = [(x0, y0 + 20.0), (x0 + 20.0, y0 + 20.0), (x0 + 20.0, y0 + 37.0), (x0, y0 + 37.0)]
    msp.add_lwpolyline(l1_pts, close=True, dxfattribs={'layer': 'A-ZONE-COMM'})
    msp.add_text("LOCAL 1 (350,00 m²)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.0}).set_placement((x0 + 3.0, y0 + 28.0))

    # Lobby Residencial (250 m²)
    lb_pts = [(x0, y0), (x0 + 20.0, y0), (x0 + 20.0, y0 + 20.0), (x0, y0 + 20.0)]
    msp.add_lwpolyline(lb_pts, close=True, dxfattribs={'layer': 'A-ZONE-LOBBY'})
    msp.add_text("LOBBY RESIDENCIAL (250,00 m²)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.0}).set_placement((x0 + 2.0, y0 + 10.0))

    # Bloque Técnico & RSU (395 m²)
    bt_pts = [(x0 + 60.0, y0), (x0 + 85.0, y0), (x0 + 85.0, y0 + 14.0), (x0 + 60.0, y0 + 14.0)]
    msp.add_lwpolyline(bt_pts, close=True, dxfattribs={'layer': 'A-ZONE-SERV'})
    msp.add_text("BLOQUE TÉCNICO & RSU (395 m²)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((x0 + 62.0, y0 + 7.0))

    # Rampa de Subsuelos (400 m²)
    rp_pts = [(x0 + 33.0, y0), (x0 + 47.0, y0), (x0 + 47.0, y0 + 12.0), (x0 + 33.0, y0 + 12.0)]
    msp.add_lwpolyline(rp_pts, close=True, dxfattribs={'layer': 'A-ZONE-SERV'})
    msp.add_text("RAMPA SUBSUELOS (400 m²)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.8}).set_placement((x0 + 34.0, y0 + 5.0))

    # --- 8. ACOTACIONES LINEALES Y COTAS DE PROYECTO ---
    # Cotas Terreno Frente y Fondo
    msp.add_aligned_dim(p1=p1, p2=p2, distance=5.0, dxfattribs={'layer': 'A-ANNO-DIMS'})
    msp.add_aligned_dim(p1=p2, p2=p3, distance=5.0, dxfattribs={'layer': 'A-ANNO-DIMS'})
    msp.add_aligned_dim(p1=p3, p2=p4, distance=5.0, dxfattribs={'layer': 'A-ANNO-DIMS'})
    msp.add_aligned_dim(p1=p4, p2=p1, distance=5.0, dxfattribs={'layer': 'A-ANNO-DIMS'})

    # Cotas Huella PB
    msp.add_aligned_dim(p1=(x0, y0), p2=(x0 + bw, y0), distance=-3.0, dxfattribs={'layer': 'A-ANNO-DIMS'})
    msp.add_aligned_dim(p1=(x0, y0), p2=(x0, y0 + bh), distance=-3.0, dxfattribs={'layer': 'A-ANNO-DIMS'})

    # --- 9. RÓTULO / CARÁTULA PROFESIONAL ISO 19650 (EN ESPACIO MODELO) ---
    rx, ry = 95.0, -10.0
    rw, rh = 45.0, 95.0
    rotulo_box = [(rx, ry), (rx + rw, ry), (rx + rw, ry + rh), (rx, ry + rh)]
    msp.add_lwpolyline(rotulo_box, close=True, dxfattribs={'layer': 'G-TITLE-BLOCK'})

    # Líneas de División de Carátula
    y_lines = [ry + 15.0, ry + 35.0, ry + 55.0, ry + 75.0]
    for yl in y_lines:
        msp.add_line((rx, yl), (rx + rw, yl), dxfattribs={'layer': 'G-TITLE-BLOCK'})

    # Textos de la Carátula / Rótulo
    msp.add_text("TESIS DE GRADO — INGENIERÍA CIVIL", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.6}).set_placement((rx + 2.0, ry + 85.0))
    msp.add_text("EDIFICIO MIXTO 18 PISOS + 3 SUBSUELOS", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.3}).set_placement((rx + 2.0, ry + 80.0))
    msp.add_text("CIUDAD DEL ESTE — ALTO PARANÁ — PARAGUAY", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.0}).set_placement((rx + 2.0, ry + 76.5))

    datos_urbanisticos = [
        "PARÁMETROS URBANÍSTICOS (CDE):",
        "• Superficie Terreno: 7.618,49 m²",
        "• FOS Máximo: 0,70 | Real: 41,28% (3.145m²)",
        "• FOT Máximo: 4,00 | Real: 3,97 (30.265m²)",
        "• Lote Mínimo: Ord. M. 003/2026 Art. 3° (≥3.000m²)",
        "• Retiros: 3m Frente / 3m Fondo / 2m Lat."
    ]
    for idx, txt in enumerate(datos_urbanisticos):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 70.0 - idx * 2.5))

    datos_programa = [
        "PROGRAMA ARQUITECTÓNICO & COCHERAS:",
        "• Planta Baja Comercial: 3.145,00 m² (1.850m² Locales)",
        "• Torre Residencial (P01-P18): 1.440,00 m²/piso",
        "• Total Departamentos: 108 Dptos (6 dptos/piso)",
        "• Cocheras Requeridas: 187 Autos (1.5/dpto + Com)",
        "• Cocheras Proyectadas: 270 Plazas (3 Subsuelos)"
    ]
    for idx, txt in enumerate(datos_programa):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 50.0 - idx * 2.5))

    datos_plano = [
        "INFORMACIÓN DEL PLANO CAD:",
        "• CODIGO: TESIS-ARQ-GEN-DR-001",
        "• DISCIPLINA: Arquitectura (ARQ)",
        "• CONTENIDO: Planimetría, Retiros & Zonificación PB",
        "• METODOLOGÍA: BIM ISO 19650 / CAD Standard",
        "• ESCALA: 1:200 | UNIDADES: Metros (m)",
        "• FECHA: 2026-09-19 | REVISIÓN: Rev. 01"
    ]
    for idx, txt in enumerate(datos_plano):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 30.0 - idx * 2.5))

    # Guardar DXF en carpetas WIP y PUBLISHED
    doc.saveas(PATH_WIP)
    doc.saveas(PATH_PUB)
    print("[SUCCESS] Archivo DXF creado en WIP: " + PATH_WIP)
    print("[SUCCESS] Archivo DXF creado en PUBLISHED: " + PATH_PUB)


if __name__ == "__main__":
    print("[INFO] Generando archivo CAD DXF profesional en metros (ISO 13567 / ISO 19650)...")
    crear_dxf_profesional()
    print("[SUCCESS] Archivos DXF generados exitosamente!")
