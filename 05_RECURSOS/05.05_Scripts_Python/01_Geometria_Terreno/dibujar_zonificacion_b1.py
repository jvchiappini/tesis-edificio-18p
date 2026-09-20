#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TESIS DE GRADO — EDIFICIO DE USO MIXTO 18 PISOS + 3 SUBSUELOS (CIUDAD DEL ESTE)
Script: dibujar_zonificacion_b1.py
Sub-etapa: B.1 — Programa y Organización Funcional

Genera la Figura 2.1 directamente extrayendo la geometría exacta del DXF:
01_WIP/01.01_ARQ/TESIS-ARQ-GEN-DR-001_Planimetria_y_Zonificacion.dxf
===============================================================================
"""

import os
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import ezdxf

# Configuración global de estilo arquitectónico ejecutivo
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.2

OUTPUT_DIR = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\etapas\img"
DXF_PATH = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\01_WIP\01.01_ARQ\TESIS-ARQ-GEN-DR-001_Planimetria_y_Zonificacion.dxf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta de Colores Ejecutiva
BG_DARK = "#0F1419"
BG_CARD = "#151F2B"
TEXT_LIGHT = "#F0F5FA"
TEXT_MUTED = "#8B98A5"
ACCENT_BLUE = "#1D9BF0"
ACCENT_GREEN = "#00BA7C"
ACCENT_GOLD = "#F7B928"
ACCENT_RED = "#F4212E"
ACCENT_PURPLE = "#7856FF"
ACCENT_ORANGE = "#FF7A00"
ACCENT_CYAN = "#00D2D3"


def clean_mtext(raw_text):
    """Limpia códigos de formato MTEXT de AutoCAD (e.g. \\P, ^J, \\PEscaleras)."""
    if not raw_text:
        return ""
    t = raw_text.replace(r'\P', '\n').replace('^J', '\n').replace(r'\p', '\n')
    t = re.sub(r'\\f[^;]+;', '', t)
    t = re.sub(r'\\[a-zA-Z0-9]+', '', t)
    t = t.replace('', '°').replace('vrtice', 'vértice').replace('Vrtice', 'Vértice').replace('Baos', 'Baños')
    return t.strip()


def generar_figura_2_1_planta_baja():
    """Genera la Figura 2.1 extrayendo la geometría y capas del DXF oficial."""
    doc = ezdxf.readfile(DXF_PATH)
    msp = doc.modelspace()

    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_CARD)

    # 1. Dibujar Límite Terreno (C-PROP-LINE)
    for e in msp.query('LWPOLYLINE[layer=="C-PROP-LINE"]'):
        pts = list(e.get_points('xy'))
        poly = patches.Polygon(pts, closed=True, edgecolor='#556B2F', facecolor='#1E2818',
                               linewidth=2.2, linestyle='--', alpha=0.8, label='Límite Terreno (7.618,49 m²)')
        ax.add_patch(poly)

    # 2. Dibujar Zonas de Parqueo PB (A-ZONE-PARK)
    park_count = 0
    for e in msp.query('LWPOLYLINE[layer=="A-ZONE-PARK"]'):
        pts = list(e.get_points('xy'))
        poly = patches.Polygon(pts, closed=True, edgecolor=ACCENT_CYAN, facecolor='#0B3036',
                               linewidth=1.2, alpha=0.85)
        ax.add_patch(poly)
        park_count += 1

    # 3. Dibujar Huella Edificable PB / Salones (A-FOOT-PB)
    for e in msp.query('LWPOLYLINE[layer=="A-FOOT-PB"]'):
        pts = list(e.get_points('xy'))
        poly = patches.Polygon(pts, closed=True, edgecolor='#20B2AA', facecolor='#10322B',
                               linewidth=1.5, alpha=0.8)
        ax.add_patch(poly)

    # 4. Dibujar Huella de Torres (A-FOOT-TOWR)
    for e in msp.query('LWPOLYLINE[layer=="A-FOOT-TOWR"]'):
        pts = list(e.get_points('xy'))
        poly = patches.Polygon(pts, closed=True, edgecolor=ACCENT_BLUE, facecolor='#142B42',
                               linewidth=2.0, alpha=0.9)
        ax.add_patch(poly)

    # 5. Dibujar Núcleos de H°A° (A-WALL-CORE)
    for e in msp.query('LWPOLYLINE[layer=="A-WALL-CORE"]'):
        pts = list(e.get_points('xy'))
        poly = patches.Polygon(pts, closed=True, edgecolor=ACCENT_RED, facecolor='#4A0E17',
                               linewidth=2.2, hatch='//', alpha=0.95)
        ax.add_patch(poly)

    # 6. Dibujar Rampa a Subsuelo 1 (Cerca de P4, orientada bajando a P3)
    # P4: (35.52, 98.17), P3: (133.10, 62.37)
    # Rampa posterior cerca de P4 (e.g. X=32 to 58, Y=82 to 90)
    rp_x, rp_y, rp_w, rp_h = 32.0, 82.0, 26.0, 7.5
    rect_rp = patches.Rectangle((rp_x, rp_y), rp_w, rp_h, edgecolor=ACCENT_GOLD, facecolor='#3A2E0B',
                                linewidth=2.0, zorder=5)
    ax.add_patch(rect_rp)
    ax.annotate('', xy=(rp_x + rp_w - 2, rp_y + rp_h/2), xytext=(rp_x + 2, rp_y + rp_h/2),
                arrowprops=dict(arrowstyle='->', color=ACCENT_GOLD, lw=2.5), zorder=6)
    ax.text(rp_x + rp_w/2, rp_y + rp_h/2, "RAMPA ACCESO SUBSUELO 1\n(Cerca de P4 ➔ Bajando a P3 | i=15%)",
            color=ACCENT_GOLD, fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=7)

    # 7. Procesar Textos y Etiquetas (A-ANNO-DIMS / C-PROP-TEXT)
    for e in msp.query('TEXT MTEXT'):
        text_str = e.dxf.text if hasattr(e.dxf, 'text') else getattr(e, 'text', '')
        cleaned = clean_mtext(text_str)
        if not cleaned:
            continue

        ins = e.dxf.insert
        x, y = ins[0], ins[1]

        layer = e.dxf.layer
        if layer == 'C-PROP-TEXT':
            if 'P1' in cleaned or 'P2' in cleaned or 'P3' in cleaned or 'P4' in cleaned:
                ax.scatter(x, y, color=ACCENT_GOLD, s=40, zorder=8)
                ax.text(x, y + 1.5, cleaned, color=ACCENT_GOLD, fontsize=8, fontweight='bold', zorder=8)
            elif 'NORTE' in cleaned:
                ax.text(x, y, "N ↑", color=ACCENT_BLUE, fontsize=12, fontweight='bold')
        elif layer == 'A-ANNO-DIMS':
            if 'Nucleo' in cleaned or 'NÚCLEO' in cleaned:
                ax.text(x, y, cleaned, color='#FFAAA6', fontsize=7.5, fontweight='bold',
                        ha='center', va='center', zorder=9,
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='#38080E', edgecolor=ACCENT_RED, alpha=0.85))
            elif 'Salon' in cleaned or 'Administracion' in cleaned or 'Ba' in cleaned:
                ax.text(x, y, cleaned, color=TEXT_LIGHT, fontsize=7.0, fontweight='bold',
                        ha='center', va='center', zorder=7,
                        bbox=dict(boxstyle='square,pad=0.15', facecolor='#111C27', edgecolor='#233649', alpha=0.8))

    # Añadir Leyenda de Parking PB
    ax.text(70.0, 15.0, f"ESTACIONAMIENTOS DE SUPERFICIE PB ({park_count} Plazas)",
            color='#80F0F0', fontsize=8.5, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#0B3036', edgecolor=ACCENT_CYAN, alpha=0.9))

    # Configuración de Ejes
    ax.set_xlim(-20, 150)
    ax.set_ylim(-10, 110)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.25, color=TEXT_MUTED)

    ax.set_title("FIGURA 2.1 — PLANTA BAJA COMERCIAL Y DE SERVICIOS (PLANIMETRÍA Y ZONIFICACIÓN EXTREMA DEL DXF)\nBasamento $3.145,00\\text{ m}^2$, 3 Torres, Rampa P4➔P3 y Estacionamiento PB (FOS = 41,28% ≤ 70,00%)",
                 color=TEXT_LIGHT, fontsize=11.5, fontweight='bold', pad=15)
    ax.set_xlabel("Coordenadas Longitudinales X (m)", color=TEXT_MUTED, fontsize=9.5)
    ax.set_ylabel("Coordenadas Transversales Y (m)", color=TEXT_MUTED, fontsize=9.5)
    ax.tick_params(colors=TEXT_MUTED)

    # Cuadro Informativo ISO 19650
    info_text = (
        "PROYECTO: Tesis Edificio 18P + 3S (CDE)\n"
        "FUENTE: TESIS-ARQ-GEN-DR-001.dxf\n"
        "DISCIPLINA: Arquitectura (ARQ)\n"
        "NIVEL: Planta Baja (PB, Cota +0.00m)\n"
        "SUPERFICIE PB: 3.145,00 m² | TERRENO: 7.618,49 m²"
    )
    ax.text(0.98, 0.96, info_text, transform=ax.transAxes, color=TEXT_LIGHT, fontsize=7.5,
            ha='right', va='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='#111822', edgecolor=ACCENT_BLUE, alpha=0.9))

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "figura_2_1_zonificacion_planta_baja.png")
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=300)
    plt.close()
    print("[SUCCESS] Generado desde DXF: " + output_path)


def generar_figura_2_2_volumetria():
    """Genera la Figura 2.2: Perfil Volumétrico y Relación de Plantas (18P + 3 Subsuelos)."""
    fig, ax = plt.subplots(figsize=(14, 11), dpi=300)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_CARD)

    # 1. Fundación en Roca Basáltica
    rect_basalto = patches.Rectangle((-10, -16), 105, 5.5, facecolor='#2C221E', edgecolor='#4A3831', hatch='..')
    ax.add_patch(rect_basalto)
    ax.text(42.5, -13.5, "ROCA BASÁLTICA DE FUNDACIÓN (q_adm = 300 kN/m² / Platea H=45cm)",
            color='#D4B2A7', fontsize=9, fontweight='bold', ha='center', va='center')

    # 2. Subsuelos (S3, S2, S1)
    subsuelos = [
        ("Subsuelo 3 (S3)", -10.50, -7.40, "#1A2533", "Estacionamiento + PTAR Estanca (120m²)"),
        ("Subsuelo 2 (S2)", -7.40, -4.30, "#1E2C3D", "Depósitos Privados & Estacionamiento Autos"),
        ("Subsuelo 1 (S1)", -4.30, -1.10, "#223347", "SALA ANDE (1.000kVA), Genset, Cisterna (60m³)")
    ]
    for nombre, y_bot, y_top, color, desc in subsuelos:
        rect = patches.Rectangle((0, y_bot), 85, (y_top - y_bot), edgecolor=ACCENT_BLUE, facecolor=color, linewidth=1.2, alpha=0.9)
        ax.add_patch(rect)
        ax.text(42.5, (y_bot + y_top)/2, f"{nombre} (Cota {y_bot:.2f}m) — Área: 3.145 m² | {desc}",
                color=TEXT_LIGHT, fontsize=8.5, fontweight='bold', ha='center', va='center')

    ax.axhline(0, color=ACCENT_GREEN, linestyle='--', linewidth=2, label='Nivel Terreno Natural (Cota ±0.00m)')
    ax.text(-8, 0, "Nivel Ground\n±0.00m", color=ACCENT_GREEN, fontsize=9, fontweight='bold', va='center')

    # 3. Planta Baja (PB, Cota 0.00m a +4.00m)
    rect_pb = patches.Rectangle((0, 0), 85, 4.0, edgecolor=ACCENT_GOLD, facecolor='#3A2E0B', linewidth=2, alpha=0.95)
    ax.add_patch(rect_pb)
    ax.text(42.5, 2.0, "PLANTA BAJA COMERCIAL (3.145 m² | FOS = 41,28% ≤ 70%)\nAcceso a 3 Torres Residenciales + Locales Comerciales",
            color=ACCENT_GOLD, fontsize=9.5, fontweight='bold', ha='center', va='center')

    # 4. 3 Torres Residenciales (P01 a P18)
    torres_x = [(5, 28, "Torre 1 (Oeste)"), (31, 54, "Torre 2 (Centro)"), (57, 80, "Torre 3 (Este)")]
    y_p01 = 4.0
    h_torre = 57.0

    for tx_start, tx_end, t_nombre in torres_x:
        tw = tx_end - tx_start
        rect_t = patches.Rectangle((tx_start, y_p01), tw, h_torre, edgecolor=ACCENT_BLUE, facecolor='#1D3246', linewidth=1.5, alpha=0.9)
        ax.add_patch(rect_t)
        ax.text(tx_start + tw/2, y_p01 + h_torre/2, f"{t_nombre}\n18 Pisos Residenciales\n(P01 a P18)",
                color=TEXT_LIGHT, fontsize=8, fontweight='bold', ha='center', va='center')

    # Configuración Ejes
    ax.set_xlim(-15, 105)
    ax.set_ylim(-18, 72)
    ax.grid(True, linestyle=':', alpha=0.25, color=TEXT_MUTED)

    ax.set_title("FIGURA 2.2 — PERFIL VOLUMÉTRICO Y RELACIÓN DE PLANTAS (3 TORRES INDEPENDIENTES + 3 SUBSUELOS)\nBasamento Comercial $3.145\\text{ m}^2$ e Integración de Núcleos de H°A°",
                 color=TEXT_LIGHT, fontsize=12.5, fontweight='bold', pad=15)
    ax.set_xlabel("Desarrollo Longitudinal (m)", color=TEXT_MUTED, fontsize=10)
    ax.set_ylabel("Cota de Nivel Z (m)", color=TEXT_MUTED, fontsize=10)
    ax.tick_params(colors=TEXT_MUTED)

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "figura_2_2_volumetria_y_perfil_edificio.png")
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=300)
    plt.close()
    print("[SUCCESS] Generado: " + output_path)

if __name__ == "__main__":
    print("[INFO] Iniciando generacion de figuras tecnicas extrayendo zonas del DXF...")
    generar_figura_2_1_planta_baja()
    generar_figura_2_2_volumetria()
    print("[SUCCESS] Generación completada exitosamente!")
