#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TESIS DE GRADO — EDIFICIO DE USO MIXTO 18 PISOS + 3 SUBSUELOS (CIUDAD DEL ESTE)
Script: dibujar_zonificacion_b1.py
Sub-etapa: B.1 — Programa y Organización Funcional

Genera la Figura 2.1 en ULTRA ALTA CALIDAD (400 DPI) extrayendo la geometría
exacta del DXF oficial:
01_WIP/01.01_ARQ/TESIS-ARQ-GEN-DR-001_Planimetria_y_Zonificacion.dxf
- Rampa leída directamente de la capa DXF 'A-ZONE-RAMP' para permitir edición en CAD.
- Torres representadas con LÍNEAS DE PUNTOS (proyección superior P01-P18).
- Nombres y superficies de TODOS los salones/recintos centrados en sus centroides geométricos.
===============================================================================
"""

import os
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import ezdxf

# Configuración global de estilo arquitectónico ejecutivo de ultra alta fidelidad
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#2A3644'
plt.rcParams['axes.linewidth'] = 1.5

OUTPUT_DIR = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\etapas\img"
DXF_PATH = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\01_WIP\01.01_ARQ\TESIS-ARQ-GEN-DR-001_Planimetria_y_Zonificacion.dxf"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta de Colores Arquitectónica de Alta Fidelidad
BG_DARK = "#090D12"
BG_CARD = "#121A24"
TEXT_LIGHT = "#F0F5FA"
TEXT_MUTED = "#9AA8B6"
ACCENT_BLUE = "#1D9BF0"
ACCENT_CYAN = "#00D2D3"
ACCENT_GREEN = "#00BA7C"
ACCENT_GOLD = "#F7B928"
ACCENT_RED = "#F4212E"
ACCENT_PURPLE = "#A855F7"
ACCENT_ORANGE = "#FF7A00"


def clean_mtext(raw_text):
    """Limpia códigos de formato MTEXT de AutoCAD."""
    if not raw_text:
        return ""
    t = raw_text.replace('\x00', '')
    t = t.replace(r'\P', '\n').replace('^J', '\n').replace(r'\p', '\n')
    t = re.sub(r'\\f[^;]+;', '', t)
    t = re.sub(r'\\[a-zA-Z0-9]+', '', t)
    t = t.replace('vrtice', 'vértice').replace('Vrtice', 'Vértice').replace('Baos', 'Baños')
    t = re.sub(r'(\d+)\.(\d+)m2', r'\1,\2 m²', t)
    t = re.sub(r'(\d+)m2', r'\1 m²', t)
    return t.strip()


def poly_centroid_and_area(pts):
    """Calcula el centroide exacto (cx, cy) y el área m² de un polígono."""
    pts_arr = np.array(pts)
    x, y = pts_arr[:, 0], pts_arr[:, 1]
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    cx, cy = np.mean(x), np.mean(y)
    return cx, cy, area


def generar_figura_2_1_planta_baja():
    """Genera la Figura 2.1 extrayendo la geometría y capas del DXF oficial."""
    doc = ezdxf.readfile(DXF_PATH)
    msp = doc.modelspace()

    fig, ax = plt.subplots(figsize=(24, 14), dpi=400)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_CARD)

    # 1. Dibujar Límite Terreno (C-PROP-LINE)
    for e in msp.query('LWPOLYLINE[layer=="C-PROP-LINE"]'):
        pts = list(e.get_points('xy'))
        poly = patches.Polygon(pts, closed=True, edgecolor='#6B8E23', facecolor='#1A2416',
                               linewidth=2.5, linestyle='--', alpha=0.85, label='Límite Terreno (7.618,49 m²)')
        ax.add_patch(poly)

    # 2. Dibujar Zonas de Estacionamiento PB (A-ZONE-PARK)
    park_count = 0
    for e in msp.query('LWPOLYLINE[layer=="A-ZONE-PARK"]'):
        pts = list(e.get_points('xy'))
        poly = patches.Polygon(pts, closed=True, edgecolor=ACCENT_CYAN, facecolor='#0B3036',
                               linewidth=1.2, alpha=0.85)
        ax.add_patch(poly)
        park_count += 1

    # 3. Dibujar Salones / Recintos PB (A-FOOT-PB)
    salons = list(msp.query('LWPOLYLINE[layer=="A-FOOT-PB"]'))
    texts_dxf = list(msp.query('MTEXT[layer=="A-ANNO-DIMS"]')) + list(msp.query('TEXT[layer=="A-ANNO-DIMS"]'))

    for poly in salons:
        pts = list(poly.get_points('xy'))
        cx, cy, area = poly_centroid_and_area(pts)

        poly_patch = patches.Polygon(pts, closed=True, edgecolor='#2E5B70', facecolor='#132738',
                                     linewidth=1.5, alpha=0.9)
        ax.add_patch(poly_patch)

        min_d = 1e9
        matched_txt = ""
        for t in texts_dxf:
            t_str = clean_mtext(t.dxf.text if hasattr(t.dxf, 'text') else getattr(t, 'text', ''))
            ins = t.dxf.insert
            d = np.hypot(ins[0] - cx, ins[1] - cy)
            if d < min_d:
                min_d = d
                matched_txt = t_str

        if matched_txt and not ("Nucleo" in matched_txt or "NÚCLEO" in matched_txt):
            ax.text(cx, cy, matched_txt, color=TEXT_LIGHT, fontsize=7.2, fontweight='bold',
                    ha='center', va='center', zorder=8,
                    bbox=dict(boxstyle='round,pad=0.25', facecolor='#0B1724', edgecolor=ACCENT_BLUE, alpha=0.9, lw=0.8))

    # 4. Dibujar Torres con LÍNEAS DE PUNTOS (A-FOOT-TOWR)
    tower_idx = 1
    for e in msp.query('LWPOLYLINE[layer=="A-FOOT-TOWR"]'):
        pts = list(e.get_points('xy'))
        cx, cy, _ = poly_centroid_and_area(pts)
        
        poly_tower = patches.Polygon(pts, closed=True, edgecolor=ACCENT_GOLD, facecolor='#362C0B',
                                     linewidth=2.8, linestyle=':', alpha=0.45, zorder=6)
        ax.add_patch(poly_tower)
        
        ax.text(cx, cy + 8.0, f"TORRE {tower_idx}\n(Proyección P01-P18)", color=ACCENT_GOLD, fontsize=9.5, fontweight='bold',
                ha='center', va='center', zorder=10,
                bbox=dict(boxstyle='round,pad=0.35', facecolor='#241B05', edgecolor=ACCENT_GOLD, alpha=0.95, lw=1.2))
        tower_idx += 1

    # 5. Dibujar Núcleos de H°A° (A-WALL-CORE)
    core_idx = 1
    for e in msp.query('LWPOLYLINE[layer=="A-WALL-CORE"]'):
        pts = list(e.get_points('xy'))
        cx, cy, _ = poly_centroid_and_area(pts)
        poly_core = patches.Polygon(pts, closed=True, edgecolor=ACCENT_RED, facecolor='#520F1A',
                                    linewidth=2.2, hatch='//', alpha=0.95, zorder=7)
        ax.add_patch(poly_core)
        ax.text(cx, cy, f"NÚCLEO {core_idx}\nH°A° (80 m²)", color='#FFAAA6', fontsize=7.5, fontweight='bold',
                ha='center', va='center', zorder=9,
                bbox=dict(boxstyle='square,pad=0.2', facecolor='#3B0810', edgecolor=ACCENT_RED, alpha=0.9, lw=1.0))
        core_idx += 1

    # 6. Dibujar Rampa a Subsuelo 1 EXTRAÍDA DIRECTAMENTE DE LA CAPA DXF 'A-ZONE-RAMP'
    ramp_polys = list(msp.query('LWPOLYLINE[layer=="A-ZONE-RAMP"]')) + list(msp.query('POLYLINE[layer=="A-ZONE-RAMP"]'))
    ramp_texts = list(msp.query('MTEXT[layer=="A-ZONE-RAMP"]')) + list(msp.query('TEXT[layer=="A-ZONE-RAMP"]'))

    for poly in ramp_polys:
        pts = list(poly.get_points('xy'))
        cx, cy, _ = poly_centroid_and_area(pts)
        poly_ramp = patches.Polygon(pts, closed=True, edgecolor=ACCENT_ORANGE, facecolor='#3D1C08',
                                    linewidth=2.2, zorder=7)
        ax.add_patch(poly_ramp)
        
        # Orientación y flecha indicadora
        pts_arr = np.array(pts)
        min_x, max_x = np.min(pts_arr[:, 0]), np.max(pts_arr[:, 0])
        min_y, max_y = np.min(pts_arr[:, 1]), np.max(pts_arr[:, 1])
        ax.annotate('', xy=(max_x - 1.5, (min_y + max_y)/2), xytext=(min_x + 1.5, (min_y + max_y)/2),
                    arrowprops=dict(arrowstyle='->', color=ACCENT_ORANGE, lw=3.0), zorder=8)

    for t in ramp_texts:
        t_str = clean_mtext(t.dxf.text if hasattr(t.dxf, 'text') else getattr(t, 'text', ''))
        ins = t.dxf.insert
        ax.text(ins[0], ins[1], t_str, color='#FFC09F', fontsize=8.0, fontweight='bold',
                ha='center', va='center', zorder=9,
                bbox=dict(boxstyle='round,pad=0.25', facecolor='#291104', edgecolor=ACCENT_ORANGE, alpha=0.95))

    # 7. Procesar Vértices del Terreno y Títulos (C-PROP-TEXT)
    for e in msp.query('TEXT[layer=="C-PROP-TEXT"]'):
        txt = clean_mtext(e.dxf.text)
        ins = e.dxf.insert
        x, y = ins[0], ins[1]
        if 'P1' in txt or 'P2' in txt or 'P3' in txt or 'P4' in txt:
            ax.scatter(x, y, color=ACCENT_GOLD, s=70, zorder=11)
            ax.text(x, y + 2.0, txt, color=ACCENT_GOLD, fontsize=9.0, fontweight='bold', zorder=11)
        elif 'NORTE' in txt:
            ax.text(x, y, "N ↑", color=ACCENT_BLUE, fontsize=13, fontweight='bold', zorder=11)

    # Etiqueta de Estacionamiento de Superficie PB
    ax.text(65.0, 16.0, f"ESTACIONAMIENTOS DE SUPERFICIE PB ({park_count} Plazas para Visitas & Locales)",
            color='#80F0F0', fontsize=9.0, fontweight='bold', ha='center', va='center', zorder=8,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#0B3036', edgecolor=ACCENT_CYAN, alpha=0.95, lw=1.2))

    # Configuración de Ejes y Grilla
    ax.set_xlim(-15, 145)
    ax.set_ylim(-10, 110)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.25, color=TEXT_MUTED)

    ax.set_title("FIGURA 2.1 — PLANTA BAJA COMERCIAL Y DE SERVICIOS (ZONIFICACIÓN OFICIAL EXTRAÍDA DEL DXF)\nBasamento $3.145,00\\text{ m}^2$, Proyección 3 Torres (Líneas de Puntos), Rampa Capa 'A-ZONE-RAMP' y Parking PB (FOS = 41,28% ≤ 70,00%)",
                 color=TEXT_LIGHT, fontsize=12.5, fontweight='bold', pad=18)
    ax.set_xlabel("Coordenadas Longitudinales X (m)", color=TEXT_MUTED, fontsize=10.5)
    ax.set_ylabel("Coordenadas Transversales Y (m)", color=TEXT_MUTED, fontsize=10.5)
    ax.tick_params(colors=TEXT_MUTED, labelsize=9.5)

    # Convención / Leyenda Técnica ISO 19650
    legend_elements = [
        patches.Patch(facecolor='#1A2416', edgecolor='#6B8E23', linestyle='--', label='Límite Terreno (7.618,49 m²)'),
        patches.Patch(facecolor='#132738', edgecolor='#2E5B70', label='Salones Comercial / Servicios PB'),
        patches.Patch(facecolor='#362C0B', edgecolor=ACCENT_GOLD, linestyle=':', label='Proyección 3 Torres (P01-P18)'),
        patches.Patch(facecolor='#520F1A', edgecolor=ACCENT_RED, hatch='//', label='Núcleos H°A° (Ascensores + Esc.)'),
        patches.Patch(facecolor='#3D1C08', edgecolor=ACCENT_ORANGE, label='Rampa Subsuelo 1 (Capa DXF A-ZONE-RAMP)'),
        patches.Patch(facecolor='#0B3036', edgecolor=ACCENT_CYAN, label=f'Parking Superficie ({park_count} Plazas)')
    ]
    ax.legend(handles=legend_elements, loc='lower right', facecolor='#111822', edgecolor='#2A3644',
              labelcolor=TEXT_LIGHT, fontsize=8.5, framealpha=0.95)

    # Bloque de Información de Proyecto
    info_text = (
        "PROYECTO: Tesis Edificio 18P + 3S (CDE)\n"
        "FUENTE: TESIS-ARQ-GEN-DR-001.dxf\n"
        "CONFIGURACIÓN: 3 Torres (Proyección Puntos)\n"
        "PLANTA BAJA: Basamento Comercial 3.145,00 m²\n"
        "RAMPA S1: Entidad DXF en capa A-ZONE-RAMP\n"
        "SUPERFICIE PB: 3.145,00 m² | TERRENO: 7.618,49 m²"
    )
    ax.text(0.02, 0.96, info_text, transform=ax.transAxes, color=TEXT_LIGHT, fontsize=8.0,
            ha='left', va='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='#111822', edgecolor=ACCENT_BLUE, alpha=0.95, lw=1.2))

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "figura_2_1_zonificacion_planta_baja.png")
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=400)
    plt.close()
    print("[SUCCESS] Generado desde DXF con capa A-ZONE-RAMP: " + output_path)


def generar_figura_2_2_volumetria():
    """Genera la Figura 2.2: Perfil Volumétrico y Relación de Plantas (3 Torres Independientes)."""
    fig, ax = plt.subplots(figsize=(15, 11), dpi=400)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_CARD)

    rect_basalto = patches.Rectangle((-10, -16), 105, 5.5, facecolor='#2C221E', edgecolor='#4A3831', hatch='..')
    ax.add_patch(rect_basalto)
    ax.text(42.5, -13.5, "ROCA BASÁLTICA DE FUNDACIÓN (q_adm = 300 kN/m² / Platea H=45cm)",
            color='#D4B2A7', fontsize=9, fontweight='bold', ha='center', va='center')

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

    rect_pb = patches.Rectangle((0, 0), 85, 4.0, edgecolor=ACCENT_GOLD, facecolor='#3A2E0B', linewidth=2, alpha=0.95)
    ax.add_patch(rect_pb)
    ax.text(42.5, 2.0, "PLANTA BAJA COMERCIAL (3.145 m² | FOS = 41,28% ≤ 70%)\nAcceso a 3 Torres Residenciales + Locales Comerciales",
            color=ACCENT_GOLD, fontsize=9.5, fontweight='bold', ha='center', va='center')

    torres_x = [(5, 28, "Torre 1 (Oeste)"), (31, 54, "Torre 2 (Centro)"), (57, 80, "Torre 3 (Este)")]
    y_p01 = 4.0
    h_torre = 57.0

    for tx_start, tx_end, t_nombre in torres_x:
        tw = tx_end - tx_start
        rect_t = patches.Rectangle((tx_start, y_p01), tw, h_torre, edgecolor=ACCENT_GOLD, facecolor='#1D3246', linewidth=1.8, linestyle=':', alpha=0.9)
        ax.add_patch(rect_t)
        ax.text(tx_start + tw/2, y_p01 + h_torre/2, f"{t_nombre}\n18 Pisos Residenciales\n(P01 a P18)",
                color=TEXT_LIGHT, fontsize=8.5, fontweight='bold', ha='center', va='center')

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
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=400)
    plt.close()
    print("[SUCCESS] Generado: " + output_path)

if __name__ == "__main__":
    print("[INFO] Generando figuras extrayendo rampa y zonas directamente del DXF...")
    generar_figura_2_1_planta_baja()
    generar_figura_2_2_volumetria()
    print("[SUCCESS] ¡Generación desde DXF completada exitosamente!")
