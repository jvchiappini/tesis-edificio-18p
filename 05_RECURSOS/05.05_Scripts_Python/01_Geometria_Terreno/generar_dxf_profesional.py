#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TESIS DE GRADO — EDIFICIO DE USO MIXTO 18 PISOS + 3 SUBSUELOS (CIUDAD DEL ESTE)
Script: generar_dxf_profesional.py
Propósito: Generar la plantilla CAD DXF base limpia y profesional con ORIENTACIÓN NORTE REAL
           (Norte Geográfico = Eje +Y), coordenadas UTM Zona 21J reales y relativas,
           acotaciones 1:1 en metros, capas ISO 13567 pre-configuradas y rótulo ISO 19650.
           Sin elementos flotantes ni retiros mal calculados para diseño manual libre.
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


def crear_dxf_base_limpio():
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
        ("C-SETB-LINE", 1, "DASHED", 0.25, "Línea de Retiros Reglamentarios (A definir por arquitecto)"),
        ("A-FOOT-PB", 4, "Continuous", 0.35, "Huella Edificable Planta Baja"),
        ("A-FOOT-TOWR", 5, "Continuous", 0.35, "Huella Torre Residencial"),
        ("A-WALL-CORE", 251, "Continuous", 0.50, "Núcleos Estructurales H°A°"),
        ("A-ZONE-COMM", 30, "Continuous", 0.25, "Zonificación Locales Comerciales"),
        ("A-ZONE-LOBBY", 40, "Continuous", 0.25, "Zonificación Lobby Residencial"),
        ("A-ZONE-SERV", 140, "Continuous", 0.25, "Bloque Técnico, RSU & Rampas"),
        ("A-ZONE-PARK", 61, "Continuous", 0.25, "Zonificación Estacionamiento Exterior/Frente"),
        ("A-PARK-LINE", 140, "Continuous", 0.25, "Demarcación de Cocheras y Módulos de Parqueo (2.50x5.00m)"),
        ("A-PARK-CARS", 8, "Continuous", 0.18, "Vehículos y Bloques de Estacionamiento"),
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

    # --- 3. COORDENADAS UTM REALES Y RELATIVAS EN METROS (NORTE REAL = EJE +Y) ---
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

    # Polígono Catastral Terreno (Límite de Propiedad - Capa Verde C-PROP-LINE)
    poly_terreno = msp.add_lwpolyline(pts_terreno, close=True, dxfattribs={'layer': 'C-PROP-LINE'})
    poly_terreno.dxf.const_width = 0.35

    # Vértices y Marcas de Registro
    vertices_info = [
        ("P1", p1, f"E: {utm_p1[0]:.2f} | N: {utm_p1[1]:.2f}", "Vértice Agudo 61,44°"),
        ("P2", p2, f"E: {utm_p2[0]:.2f} | N: {utm_p2[1]:.2f}", "Frente Principal 117,27m"),
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

    # --- 5. ACOTACIONES DE LINDEROS (1:1 EN METROS) ---
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

    # --- 6. RÓTULO / CARÁTULA PROFESIONAL ISO 19650 (EN METROS) ---
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
        "DATOS DEL TERRENO (PARÁMETROS CDE):",
        "• Superficie Terreno: 7.618,49 m²",
        "• Orientación: NORTE REAL (Eje +Y)",
        "• FOS Máximo: 0,70 (Huella máx. 5.332,94 m²)",
        "• FOT Máximo: 4,00 (Sup. máx. 30.473,96 m²)",
        "• Lote Mínimo: Ord. M. 003/2026 Art. 3° (≥3.000m²)",
        "• Retiros: Según Ord. M. 003/2026 y Ord. 011/1994"
    ]
    for idx, txt in enumerate(datos_urbanisticos):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 85.0 - idx * 2.5))

    datos_capas = [
        "ESTÁNDAR DE CAPAS CAD PRE-CONFIGURADAS:",
        "• C-PROP-LINE: Terreno Real (Verde, 0.50mm)",
        "• C-PROP-VERT: Vértices UTM P1-P4 (Amarillo)",
        "• C-SETB-LINE: Retiros Reglamentarios (Rojo)",
        "• A-FOOT-PB: Capa para Huella PB (Cian)",
        "• A-FOOT-TOWR: Capa para Huella Torre (Azul)",
        "• A-WALL-CORE: Capa para Núcleos H°A° (Gris)",
        "• A-ZONE-*: Capas para Zonificación Libre"
    ]
    for idx, txt in enumerate(datos_capas):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 60.0 - idx * 2.5))

    datos_plano = [
        "FICHA TÉCNICA DEL PLANO CAD:",
        "• CÓDIGO: TESIS-ARQ-GEN-DR-001",
        "• DISCIPLINA: Arquitectura (ARQ)",
        "• ESCALA: 1:1 METROS (1 unidad = 1 metro)",
        "• ESTADO: Plantilla Limpia para Diseño Manual",
        "• FECHA: 2026-09-19 | REVISIÓN: Rev. 04 (Lienzo Limpio)"
    ]
    for idx, txt in enumerate(datos_plano):
        msp.add_text(txt, dxfattribs={'layer': 'A-ANNO-TEXT', 'height': 0.9}).set_placement((rx + 2.0, ry + 35.0 - idx * 2.5))

    # Guardar DXF en carpetas WIP y PUBLISHED
    doc.saveas(PATH_WIP)
    doc.saveas(PATH_PUB)
    print("[SUCCESS] Archivo DXF plantilla limpia creado en WIP: " + PATH_WIP)
    print("[SUCCESS] Archivo DXF plantilla limpia creado en PUBLISHED: " + PATH_PUB)


if __name__ == "__main__":
    print("[INFO] Generando plantilla CAD DXF limpia (1:1 Metros / Norte Real) para diseño manual...")
    crear_dxf_base_limpio()
    print("[SUCCESS] Plantilla CAD DXF creada exitosamente!")
