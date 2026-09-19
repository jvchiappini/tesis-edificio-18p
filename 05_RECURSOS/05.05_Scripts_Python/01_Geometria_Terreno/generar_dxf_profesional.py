#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TESIS DE GRADO — EDIFICIO DE USO MIXTO 18 PISOS + 3 SUBSUELOS (CIUDAD DEL ESTE)
Script: generar_dxf_profesional.py
Propósito: Generar la base CAD DXF limpia y profesional con ORIENTACIÓN NORTE REAL
           (Norte Geográfico = Eje +Y), coordenadas UTM Zona 21J reales y relativas,
           retiros reglamentarios, acotaciones y capas pre-configuradas según
           estándar ISO 13567 / AIA CAD.
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


def crear_dxf_profesional_norte_real():
    # 1. Crear documento DXF R2018
    doc = ezdxf.new('R2018', setup=True)

    # Configuración estricta de Encabezado Unidades Métricas (Metros 1:1)
    doc.header['$INSUNITS'] = 6       # 6 = Metros
    doc.header['$MEASUREMENT'] = 1   # 1 = Métrico
    doc.header['$LUNITS'] = 2        # 2 = Decimal
    doc.header['$LUPREC'] = 2        # 2 decimales
    doc.header['$AUNITS'] = 0        # Grados decimales
    doc.header['$DIMALTF'] = 1.0     # Multiplicador alternativo 1.0
    doc.header['$DIMLFAC'] = 1.0     # Factor de cota lineal 1.0 (1m = 1u)
    doc.header['$DIMSCALE'] = 1.0    # Escala global de cotas 1.0
    doc.header['$DIMTXT'] = 1.2
    doc.header['$DIMASZ'] = 0.8

    # 2. Definir Capas Profesionales Normalizadas (ISO 13567 / AIA CAD)
    capas = [
        ("C-PROP-LINE", 3, "Continuous", 0.50, "Límite Catastral del Terreno (7.618,49 m²)"),
        ("C-PROP-VERT", 2, "Continuous", 0.25, "Vértices P1-P4 con Marcadores y Coordenadas"),
        ("C-PROP-TEXT", 7, "Continuous", 0.25, "Textos del Predio, Rumbos y Áreas"),
        ("C-SETB-LINE", 1, "DASHED", 0.25, "Línea de Retiros Reglamentarios (3m Frente/Fondo, 2m Lat.)"),
        ("A-FOOT-PB", 4, "Continuous", 0.35, "Huella Edificable de Referencia PB (3.145,00 m²)"),
        ("A-FOOT-TOWR", 5, "Continuous", 0.35, "Huella Torre Residencial (1.440,00 m²)"),
        ("A-WALL-CORE", 251, "Continuous", 0.50, "Núcleos Estructurales H°A° (7x9m c/u)"),
        ("A-ZONE-COMM", 30, "Continuous", 0.25, "Capa para Zonificación Comercial"),
        ("A-ZONE-LOBBY", 40, "Continuous", 0.25, "Capa para Lobby Residencial"),
        ("A-ZONE-SERV", 140, "Continuous", 0.25, "Capa para Bloque Técnico, RSU & Rampas"),
        ("A-ANNO-DIMS", 2, "Continuous", 0.18, "Acotaciones del Proyecto"),
        ("A-ANNO-TEXT", 7, "Continuous", 0.25, "Textos de Espacios y Especificaciones"),
        ("G-TITLE-BLOCK", 7, "Continuous", 0.35, "Carátula / Rótulo de Plano ISO 19650")
    ]

    for name, color, linetype, lineweight, desc in capas:
        if name in doc.layers:
            layer = doc.layers.get(name)
        else:
            layer = doc.layers.add(name=name, color=color, linetype=linetype)
        layer.description = desc
        layer.lineweight = int(lineweight * 100)

    msp = doc.modelspace()

    # --- 3. COORDENADAS UTM REALES Y RELATIVAS CON NORTE REAL (NORTE = +Y) ---
    # Coordenadas UTM WGS84 Zona 21J
    utm_p1 = (737721.76, 7176185.26)
    utm_p2 = (737837.53, 7176203.96)
    utm_p3 = (737853.36, 7176246.13)
    utm_p4 = (737755.78, 7176281.93)

    # Coordenadas Relativas en Metros manteniendo la orientación exacta del Norte Real (P1 en 0,0)
    p1 = (0.00, 0.00)
    p2 = (utm_p2[0] - utm_p1[0], utm_p2[1] - utm_p1[1])  # (115.77, 18.70)
    p3 = (utm_p3[0] - utm_p1[0], utm_p3[1] - utm_p1[1])  # (131.60, 60.87)
    p4 = (utm_p4[0] - utm_p1[0], utm_p4[1] - utm_p1[1])  # (34.02, 96.67)

    pts_terreno = [p1, p2, p3, p4]

    # Polígono Catastral Terreno (Límite de Propiedad)
    poly_terreno = msp.add_lwpolyline(pts_terreno, close=True, dxfattribs={'layer': 'C-PROP-LINE'})
    poly_terreno.dxf.const_width = 0.35

    # Vértices y Marcas de Registro
    vertices_info = [
        ("P1", p1, f"E: {utm_p1[0]:.2f} | N: {utm_p1[1]:.2f}", "Vértice Agudo 61.44°"),
        ("P2", p2, f"E: {utm_p2[0]:.2f} | N: {utm_p2[1]:.2f}", "Frente Principal 117.27m"),
        ("P3", p3, f"E: {utm_p3[0]:.2f} | N: {utm_p3[1]:.2f}", "Esquina Fondo Este"),
        ("P4", p4, f"E: {utm_p4[0]:.2f} | N: {utm_p4[1]:.2f}", "Esquina Fondo Norte")
    ]

    for label, pos, utm_txt, desc in vertices_info:
        msp.add_circle(pos, radius=0.8, dxfattribs={'layer': 'C-PROP-VERT'})
        msp.add_circle(pos, radius=0.2, dxfattribs={'layer': 'C-PROP-VERT'})
        msp.add_text(f"{label} ({desc})", dxfattribs={'layer': 'C-PROP-TEXT', 'height': 1.2}).set_placement((pos[0] + 1.5, pos[1] + 1.5))
        msp.add_text(utm_txt, dxfattribs={'layer': 'C-PROP-TEXT', 'height': 0.8}).set_placement((pos[0] + 1.5, pos[1] - 1.0))

    # --- 4. FLECHA SÍMBOLO DE NORTE REAL (NORTE GEOGRÁFICO = +Y) ---
    nx, ny = -15.0, 50.0
    msp.add_line((nx, ny), (nx, ny + 15.0), dxfattribs={'layer': 'C-PROP-TEXT'})
    msp.add_line((nx, ny + 15.0), (nx - 1.5, ny + 11.0), dxfattribs={'layer': 'C-PROP-TEXT'})
    msp.add_line((nx, ny + 15.0), (nx + 1.5, ny + 11.0), dxfattribs={'layer': 'C-PROP-TEXT'})
    msp.add_text("N (NORTE REAL)", dxfattribs={'layer': 'C-PROP-TEXT', 'height': 1.5}).set_placement((nx - 4.5, ny + 17.0))

    # --- 5. LÍNEAS DE RETIROS REGLAMENTARIOS (3m Frente P1-P2, 3m Fondo P3-P4, 2m Laterales) ---
    # Calculamos offset paralelo de 3m desde P1-P2 (frente)
    ang_frente = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    nx_frente = -math.sin(ang_frente)
    ny_frente = math.cos(ang_frente)

    # Offset 3m frente
    ret_p1 = (p1[0] + nx_frente * 3.0 + math.cos(ang_frente)*2.0, p1[1] + ny_frente * 3.0 + math.sin(ang_frente)*2.0)
    ret_p2 = (p2[0] + nx_frente * 3.0 - math.cos(ang_frente)*2.0, p2[1] + ny_frente * 3.0 - math.sin(ang_frente)*2.0)

    ang_fondo = math.atan2(p4[1] - p3[1], p4[0] - p3[0])
    nx_fondo = math.sin(ang_fondo)
    ny_fondo = -math.cos(ang_fondo)
    ret_p3 = (p3[0] + nx_fondo * 3.0 - math.cos(ang_fondo)*2.0, p3[1] + ny_fondo * 3.0 - math.sin(ang_fondo)*2.0)
    ret_p4 = (p4[0] + nx_fondo * 3.0 + math.cos(ang_fondo)*2.0, p4[1] + ny_fondo * 3.0 + math.sin(ang_fondo)*2.0)

    retiro_pts = [ret_p1, ret_p2, ret_p3, ret_p4]
    poly_retiro = msp.add_lwpolyline(retiro_pts, close=True, dxfattribs={'layer': 'C-SETB-LINE'})

    # --- 6. HUELLA EDIFICABLE DE REFERENCIA EN METROS (85m x 37m = 3.145,00 m²) ---
    # Rectángulo alineado a la grilla de diseño en cota interior
    pb_x0, pb_y0 = 12.0, 15.0
    bw, bh = 85.0, 37.0

    # Construimos el rectángulo rotado alineado al frente del terreno (9.17°)
    cos_a = math.cos(ang_frente)
    sin_a = math.sin(ang_frente)

    def to_global(lx, ly):
        gx = pb_x0 + lx * cos_a - ly * sin_a
        gy = pb_y0 + lx * sin_a + ly * cos_a
        return (gx, gy)

    pb_p1 = to_global(0, 0)
    pb_p2 = to_global(bw, 0)
    pb_p3 = to_global(bw, bh)
    pb_p4 = to_global(0, bh)

    poly_pb = msp.add_lwpolyline([pb_p1, pb_p2, pb_p3, pb_p4], close=True, dxfattribs={'layer': 'A-FOOT-PB'})
    poly_pb.dxf.const_width = 0.25

    # Huella Torre Residencial de Referencia (48m x 30m)
    tw, th = 48.0, 30.0
    torre_p1 = to_global(18.5, 3.5)
    torre_p2 = to_global(18.5 + tw, 3.5)
    torre_p3 = to_global(18.5 + tw, 3.5 + th)
    torre_p4 = to_global(18.5, 3.5 + th)

    poly_torre = msp.add_lwpolyline([torre_p1, torre_p2, torre_p3, torre_p4], close=True, dxfattribs={'layer': 'A-FOOT-TOWR'})
    poly_torre.dxf.const_width = 0.20

    # Núcleos Estructurales H°A° de Referencia (7x9m c/u)
    nc1_p1 = to_global(25.0, 3.0)
    nc1_p2 = to_global(32.0, 3.0)
    nc1_p3 = to_global(32.0, 12.0)
    nc1_p4 = to_global(25.0, 12.0)
    poly_nc1 = msp.add_lwpolyline([nc1_p1, nc1_p2, nc1_p3, nc1_p4], close=True, dxfattribs={'layer': 'A-WALL-CORE'})
    poly_nc1.dxf.const_width = 0.30

    nc2_p1 = to_global(48.0, 3.0)
    nc2_p2 = to_global(57.0, 3.0)
    nc2_p3 = to_global(57.0, 10.0)
    nc2_p4 = to_global(48.0, 10.0)
    poly_nc2 = msp.add_lwpolyline([nc2_p1, nc2_p2, nc2_p3, nc2_p4], close=True, dxfattribs={'layer': 'A-WALL-CORE'})
    poly_nc2.dxf.const_width = 0.30

    # --- 7. ACOTACIONES LINEALES 1:1 EN METROS ---
    def agregar_cota_limpia(pa, pb, offset, texto):
        ax_dx = pb[0] - pa[0]
        ax_dy = pb[1] - pa[1]
        dist = math.hypot(ax_dx, ax_dy)
        if dist == 0:
            return
        nx_val = -ax_dy / dist
        ny_val = ax_dx / dist
        ca = (pa[0] + nx_val * offset, pa[1] + ny_val * offset)
        cb = (pb[0] + nx_val * offset, pb[1] + ny_val * offset)
        msp.add_line((pa[0] + nx_val * 0.5, pa[1] + ny_val * 0.5), (ca[0] + nx_val * 0.8, ca[1] + ny_val * 0.8), dxfattribs={'layer': 'A-ANNO-DIMS'})
        msp.add_line((pb[0] + nx_val * 0.5, pb[1] + ny_val * 0.5), (cb[0] + nx_val * 0.8, cb[1] + ny_val * 0.8), dxfattribs={'layer': 'A-ANNO-DIMS'})
        msp.add_line(ca, cb, dxfattribs={'layer': 'A-ANNO-DIMS'})
        tick_len = 0.6
        msp.add_line((ca[0] - tick_len, ca[1] - tick_len), (ca[0] + tick_len, ca[1] + tick_len), dxfattribs={'layer': 'A-ANNO-DIMS'})
        msp.add_line((cb[0] - tick_len, cb[1] - tick_len), (cb[0] + tick_len, cb[1] + tick_len), dxfattribs={'layer': 'A-ANNO-DIMS'})
        mid_x = (ca[0] + cb[0]) / 2.0 + nx_val * 0.8
        mid_y = (ca[1] + cb[1]) / 2.0 + ny_val * 0.8
        msp.add_text(texto, dxfattribs={'layer': 'A-ANNO-DIMS', 'height': 1.0}).set_placement((mid_x - 1.5, mid_y))

    agregar_cota_limpia(p1, p2, -6.0, "Frente L = 117.27 m")
    agregar_cota_limpia(p2, p3, 6.0, "L = 45.04 m")
    agregar_cota_limpia(p3, p4, 6.0, "Fondo L = 103.94 m")
    agregar_cota_limpia(p4, p1, 6.0, "L = 102.48 m")

    # --- 8. RÓTULO / CARÁTULA PROFESIONAL ISO 19650 (EN METROS) ---
    rx, ry = 145.0, -10.0
    rw, rh = 45.0, 110.0
    rotulo_box = [(rx, ry), (rx + rw, ry), (rx + rw, ry + rh), (rx, ry + rh)]
    msp.add_lwpolyline(rotulo_box, close=True, dxfattribs={'layer': 'G-TITLE-BLOCK'})

    y_lines = [ry + 15.0, ry + 40.0, ry + 65.0, ry + 90.0]
    for yl in y_lines:
        msp.add_line((rx, yl), (rx + rw, yl), dxfattribs={'layer': 'G-TITLE-BLOCK'})

    msp.add_text("TESIS DE GRADO — INGENIERÍA CIVIL", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.6}).set_placement((rx + 2.0, ry + 100.0))
    msp.add_text("EDIFICIO MIXTO 18 PISOS + 3 SUBSUELOS", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.3}).set_placement((rx + 2.0, ry + 95.0))
    msp.add_text("CIUDAD DEL ESTE — PARAGUAY (UTM 21J)", dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 1.0}).set_placement((rx + 2.0, ry + 91.5))

    datos_urbanisticos = [
        "DATOS DE TERRENO Y ZONIFICACIÓN:",
        "• Superficie Terreno: 7.618,49 m²",
        "• Orientación: NORTE REAL (Eje +Y)",
        "• FOS Máximo: 0,70 | Real: 41,28% (3.145m²)",
        "• FOT Máximo: 4,00 | Real: 3,97 (30.265m²)",
        "• Lote Mínimo: Ord. M. 003/2026 Art. 3° (≥3.000m²)",
        "• Retiros: 3m Frente / 3m Fondo / 2m Lat."
    ]
    for idx, txt in enumerate(datos_urbanisticos):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 85.0 - idx * 2.5))

    datos_capas = [
        "ESTÁNDAR DE CAPAS CAD (ISO 13567):",
        "• C-PROP-LINE: Terreno Real (Verde, 0.50mm)",
        "• C-PROP-VERT: Vértices UTM P1-P4 (Amarillo)",
        "• C-SETB-LINE: Retiros Reglamentarios (Rojo)",
        "• A-FOOT-PB: Huella PB (Cian, 0.35mm)",
        "• A-FOOT-TOWR: Huella Torre (Azul, 0.35mm)",
        "• A-WALL-CORE: Núcleos H°A° (Gris, 0.50mm)",
        "• A-ZONE-*: Capas para Zonificación Manual"
    ]
    for idx, txt in enumerate(datos_capas):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 60.0 - idx * 2.5))

    datos_plano = [
        "FICHA TÉCNICA DEL PLANO CAD:",
        "• CÓDIGO: TESIS-ARQ-GEN-DR-001",
        "• DISCIPLINA: Arquitectura (ARQ)",
        "• ESCALA: 1:1 METROS (Norte Real = Eje +Y)",
        "• ESTADO: Base Limpia para Distribución",
        "• FECHA: 2026-09-19 | REVISIÓN: Rev. 03 (Norte Real)"
    ]
    for idx, txt in enumerate(datos_plano):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 35.0 - idx * 2.5))

    # Guardar DXF en carpetas WIP y PUBLISHED
    doc.saveas(PATH_WIP)
    doc.saveas(PATH_PUB)
    print("[SUCCESS] Archivo DXF base creado en WIP: " + PATH_WIP)
    print("[SUCCESS] Archivo DXF base creado en PUBLISHED: " + PATH_PUB)


if __name__ == "__main__":
    print("[INFO] Generando base CAD DXF con NORTE REAL (Eje +Y) y capas normalizadas...")
    crear_dxf_profesional_norte_real()
    print("[SUCCESS] Base CAD DXF generada exitosamente para diseño manual!")
