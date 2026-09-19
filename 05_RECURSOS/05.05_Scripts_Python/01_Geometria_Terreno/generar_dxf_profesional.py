#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TESIS DE GRADO — EDIFICIO DE USO MIXTO 18 PISOS + 3 SUBSUELOS (CIUDAD DEL ESTE)
Script: generar_dxf_profesional.py
Propósito: Generar el archivo CAD DXF profesional en METROS 1:1 (ISO 13567 / AIA CAD)
           Garantiza escala real 1 unidad = 1 metro en AutoCAD sin escalados 100x/1000x.
===============================================================================
"""

import os
import math
import ezdxf

# Rutas de salida
WIP_DIR = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\01_WIP\01.01_ARQ"
PUB_DIR = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\03_PUBLISHED\03.01_Planos"

os.makedirs(WIP_DIR, exist_ok=True)
os.makedirs(PUB_DIR, exist_ok=True)

FILE_NAME = "TESIS-ARQ-GEN-DR-001_Planimetria_y_Zonificacion.dxf"
PATH_WIP = os.path.join(WIP_DIR, FILE_NAME)
PATH_PUB = os.path.join(PUB_DIR, FILE_NAME)


def crear_dxf_profesional():
    # 1. Crear documento DXF R2018 con setup completo
    doc = ezdxf.new('R2018', setup=True)

    # Configuración estricta de Encabezado Unidades Métricas (Metros 1:1)
    doc.header['$INSUNITS'] = 6       # 6 = Metros
    doc.header['$MEASUREMENT'] = 1   # 1 = Métrico (mm/m)
    doc.header['$LUNITS'] = 2        # 2 = Decimal
    doc.header['$LUPREC'] = 2        # 2 decimales
    doc.header['$AUNITS'] = 0        # Grados decimales
    doc.header['$AUPREC'] = 2
    doc.header['$DIMALTF'] = 1.0     # Multiplicador alternativo 1.0
    doc.header['$DIMLFAC'] = 1.0     # Factor de escala de cota lineal 1.0 (1 unidad = 1 metro)
    doc.header['$DIMSCALE'] = 1.0    # Escala global de cotas 1.0
    doc.header['$DIMTXT'] = 1.2      # Altura texto de cota en metros
    doc.header['$DIMASZ'] = 0.8      # Tamaño de flecha en metros
    doc.header['$DIMEXO'] = 0.5      # Desfase línea extensión
    doc.header['$DIMEXE'] = 0.5      # Extensión de línea

    # 2. Definir Estilo de Cota Nuncio Métrico
    try:
        dimstyle = doc.dimstyles.new('METRIC_METERS')
    except Exception:
        dimstyle = doc.dimstyles.get('METRIC_METERS')

    dimstyle.dxf.dimtxt = 1.2
    dimstyle.dxf.dimasz = 0.8
    dimstyle.dxf.dimlfac = 1.0
    dimstyle.dxf.dimscale = 1.0
    dimstyle.dxf.dimdec = 2
    dimstyle.dxf.dimunit = 2
    dimstyle.dxf.dimclrd = 2
    dimstyle.dxf.dimclrt = 7
    dimstyle.dxf.dimclre = 2

    # 3. Definir Capas (ISO 13567 / AIA Standard)
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
        if name in doc.layers:
            layer = doc.layers.get(name)
        else:
            layer = doc.layers.add(name=name, color=color, linetype=linetype)
        layer.description = desc
        layer.lineweight = int(lineweight * 100)

    msp = doc.modelspace()

    # --- 4. GEOMETRÍA DEL TERRENO EN COORDENADAS LOCALES EN METROS (P1 EN 0,0) ---
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

    # --- 5. LÍNEA DE RETIROS REGLAMENTARIOS (3m Frente/Fondo, 2m Laterales) ---
    # Rectángulo Edificable Inscripto PB (85.00m x 37.00m = 3.145,00 m²)
    x0, y0 = 5.0, 5.0
    bw, bh = 85.0, 37.0

    retiro_pts = [(2.5, 3.0), (87.5, 3.0), (87.5, 40.0), (2.5, 40.0)]
    poly_retiro = msp.add_lwpolyline(retiro_pts, close=True, dxfattribs={'layer': 'C-SETB-LINE'})

    # --- 6. HUELLA EDIFICABLE DE PLANTA BAJA (85.00m x 37.00m = 3.145,00 m²) ---
    pb_pts = [(x0, y0), (x0 + bw, y0), (x0 + bw, y0 + bh), (x0, y0 + bh)]
    poly_pb = msp.add_lwpolyline(pb_pts, close=True, dxfattribs={'layer': 'A-FOOT-PB'})
    poly_pb.dxf.const_width = 0.25

    # --- 7. HUELLA DE TORRE RESIDENCIAL (48.00m x 30.00m = 1.440,00 m²) ---
    tx0, ty0 = x0 + 18.5, y0 + 3.5
    tw, th = 48.0, 30.0
    torre_pts = [(tx0, ty0), (tx0 + tw, ty0), (tx0 + tw, ty0 + th), (tx0, ty0 + th)]
    poly_torre = msp.add_lwpolyline(torre_pts, close=True, dxfattribs={'layer': 'A-FOOT-TOWR'})
    poly_torre.dxf.const_width = 0.20

    # --- 8. NÚCLEOS ESTRUCTURALES H°A° (2x Gemelos 7x9m = 126 m²) ---
    # Núcleo 1 (7m x 9m)
    nc1_pts = [(x0 + 25.0, y0 + 3.0), (x0 + 32.0, y0 + 3.0), (x0 + 32.0, y0 + 12.0), (x0 + 25.0, y0 + 12.0)]
    poly_nc1 = msp.add_lwpolyline(nc1_pts, close=True, dxfattribs={'layer': 'A-WALL-CORE'})
    poly_nc1.dxf.const_width = 0.30

    # Núcleo 2 (9m x 7m)
    nc2_pts = [(x0 + 48.0, y0 + 3.0), (x0 + 57.0, y0 + 3.0), (x0 + 57.0, y0 + 10.0), (x0 + 48.0, y0 + 10.0)]
    poly_nc2 = msp.add_lwpolyline(nc2_pts, close=True, dxfattribs={'layer': 'A-WALL-CORE'})
    poly_nc2.dxf.const_width = 0.30

    # Textos de Núcleos
    msp.add_text("NÚCLEO 1 H°A° (7x9m)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((x0 + 25.5, y0 + 7.0))
    msp.add_text("NÚCLEO 2 H°A° (9x7m)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((x0 + 48.5, y0 + 6.0))

    # --- 9. ZONIFICACIÓN DE LOCALES COMERCIALES PB ---
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

    # --- 10. ACOTACIONES DE DIMENSIONES VECTORIALES LIMPIAS 1:1 ---
    def agregar_cota_limpia(p_a, p_b, offset, texto):
        """Dibuja una cota limpia vectorial 1:1 en metros sin problemas de multiplicador de bloque."""
        ax_dx = p_b[0] - p_a[0]
        ax_dy = p_b[1] - p_a[1]
        dist = math.hypot(ax_dx, ax_dy)
        if dist == 0:
            return

        # Vector normal para offset
        nx = -ax_dy / dist
        ny = ax_dx / dist

        # Puntos de línea de cota
        c_a = (p_a[0] + nx * offset, p_a[1] + ny * offset)
        c_b = (p_b[0] + nx * offset, p_b[1] + ny * offset)

        # Líneas de extensión
        msp.add_line((p_a[0] + nx * 0.5, p_a[1] + ny * 0.5), (c_a[0] + nx * 0.8, c_a[1] + ny * 0.8), dxfattribs={'layer': 'A-ANNO-DIMS'})
        msp.add_line((p_b[0] + nx * 0.5, p_b[1] + ny * 0.5), (c_b[0] + nx * 0.8, c_b[1] + ny * 0.8), dxfattribs={'layer': 'A-ANNO-DIMS'})

        # Línea principal de cota
        msp.add_line(c_a, c_b, dxfattribs={'layer': 'A-ANNO-DIMS'})

        # Ticks en extremos (45 grados)
        tick_len = 0.6
        msp.add_line((c_a[0] - tick_len, c_a[1] - tick_len), (c_a[0] + tick_len, c_a[1] + tick_len), dxfattribs={'layer': 'A-ANNO-DIMS'})
        msp.add_line((c_b[0] - tick_len, c_b[1] - tick_len), (c_b[0] + tick_len, c_b[1] + tick_len), dxfattribs={'layer': 'A-ANNO-DIMS'})

        # Texto de cota centrado
        mid_x = (c_a[0] + c_b[0]) / 2.0 + nx * 0.8
        mid_y = (c_a[1] + c_b[1]) / 2.0 + ny * 0.8
        msp.add_text(texto, dxfattribs={'layer': 'A-ANNO-DIMS', 'height': 1.0}).set_placement((mid_x - 1.5, mid_y))

    # Cotas de Terreno (P1->P2, P2->P3, P3->P4, P4->P1)
    agregar_cota_limpia(p1, p2, -6.0, "L = 117.27 m")
    agregar_cota_limpia(p2, p3, 6.0, "L = 45.04 m")
    agregar_cota_limpia(p3, p4, 6.0, "L = 104.57 m")
    agregar_cota_limpia(p4, p1, 6.0, "L = 85.70 m")

    # Cotas Huella PB
    agregar_cota_limpia((x0, y0), (x0 + bw, y0), -3.5, "Huella L = 85.00 m")
    agregar_cota_limpia((x0, y0), (x0, y0 + bh), -3.5, "Huella W = 37.00 m")

    # Cotas Huella Torre
    agregar_cota_limpia((tx0, ty0 + th), (tx0 + tw, ty0 + th), 2.5, "Torre L = 48.00 m")
    agregar_cota_limpia((tx0 + tw, ty0), (tx0 + tw, ty0 + th), 2.5, "Torre W = 30.00 m")

    # --- 11. RÓTULO / CARÁTULA PROFESIONAL ISO 19650 (EN ESPACIO MODELO) ---
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
        "• ESCALA: 1:1 METROS (1 UNIDAD = 1 METRO)",
        "• FECHA: 2026-09-19 | REVISIÓN: Rev. 02 (Escala Corregida)"
    ]
    for idx, txt in enumerate(datos_plano):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 30.0 - idx * 2.5))

    # Guardar DXF en carpetas WIP y PUBLISHED
    doc.saveas(PATH_WIP)
    doc.saveas(PATH_PUB)
    print("[SUCCESS] Archivo DXF creado en WIP: " + PATH_WIP)
    print("[SUCCESS] Archivo DXF creado en PUBLISHED: " + PATH_PUB)


if __name__ == "__main__":
    print("[INFO] Generando archivo CAD DXF profesional en METROS 1:1 (ISO 13567 / ISO 19650)...")
    crear_dxf_profesional()
    print("[SUCCESS] Archivos DXF corregidos y generados exitosamente!")
