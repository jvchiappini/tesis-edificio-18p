#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
TESIS DE GRADO — EDIFICIO DE USO MIXTO 18 PISOS + 3 SUBSUELOS (CIUDAD DEL ESTE)
Script: dibujar_zonificacion_b1.py
Sub-etapa: B.1 — Programa y Organización Funcional

Genera las tres figuras técnicas vectoriales/gráficas en alta resolución (300 DPI):
1. Figura 2.1: Zonificación y Organización Funcional de Planta Baja (3.145 m²)
2. Figura 2.2: Perfil Volumétrico y Relación de Plantas (18P + 3 Subsuelos)
3. Figura 2.3: Zonificación Arquitectónica de Planta Tipo Residencial (1.440 m²)
===============================================================================
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración global de estilo arquitectónico ejecutivo
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 1.2

# Rutas de salida
OUTPUT_DIR = r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\etapas\img"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta de Colores Ejecutiva / Arquitectónica
BG_DARK = "#0F1419"
BG_CARD = "#19222D"
TEXT_LIGHT = "#E6EBF0"
TEXT_MUTED = "#8B98A5"
ACCENT_BLUE = "#1D9BF0"
ACCENT_GREEN = "#00BA7C"
ACCENT_GOLD = "#F7B928"
ACCENT_RED = "#F4212E"
ACCENT_PURPLE = "#7856FF"
ACCENT_ORANGE = "#FF7A00"
ACCENT_TEAL = "#00D2D3"


def generar_figura_2_1_planta_baja():
    """Genera la Figura 2.1: Zonificación de Planta Baja (3.145 m²)."""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_CARD)

    # Coordenadas Terreno (Aproximado UTM local, P1 en origen (0,0))
    # Terreno 7.618,49 m²
    p1 = np.array([0, 0])
    p2 = np.array([117.27, 0])
    p3 = np.array([133.10, 42.17])
    p4 = np.array([35.52, 77.97])

    polygon_terreno = patches.Polygon([p1, p2, p3, p4], closed=True,
                                      edgecolor='#556B2F', facecolor='#1E2818',
                                      linewidth=2, linestyle='--', alpha=0.7, label='Límite Terreno (7.618,49 m²)')
    ax.add_patch(polygon_terreno)

    # Retiros y Huella Rectangular Inscripta (85m x 37m)
    x0, y0 = 5.0, 5.0
    bw, bh = 85.0, 37.0

    # Fondo PB
    rect_pb = patches.Rectangle((x0, y0), bw, bh, edgecolor=ACCENT_BLUE, facecolor='#162536',
                                linewidth=2.5, alpha=0.9, label='Huella Edificable PB (3.145 m²)')
    ax.add_patch(rect_pb)

    # --- ZONAS INTERIORES DE PLANTA BAJA ---
    # 1. Megastore Comercial (1.050 m²)
    ms_x, ms_y, ms_w, ms_h = x0 + 40.0, y0 + 14.0, 45.0, 23.0
    rect_ms = patches.Rectangle((ms_x, ms_y), ms_w, ms_h, edgecolor='#00A86B', facecolor='#0D3B29',
                                linewidth=1.5, alpha=0.85)
    ax.add_patch(rect_ms)
    ax.text(ms_x + ms_w/2, ms_y + ms_h/2, "MEGASTORE COMERCIAL\n1.050 m²\n(Salón Libre sin Pilares Intermedios)",
            color=TEXT_LIGHT, fontsize=10, fontweight='bold', ha='center', va='center')

    # 2. Local Comercial 2 (450 m²)
    l2_x, l2_y, l2_w, l2_h = x0 + 20.0, y0 + 14.0, 20.0, 23.0
    rect_l2 = patches.Rectangle((l2_x, l2_y), l2_w, l2_h, edgecolor='#20B2AA', facecolor='#0C3636',
                                linewidth=1.5, alpha=0.85)
    ax.add_patch(rect_l2)
    ax.text(l2_x + l2_w/2, l2_y + l2_h/2, "LOCAL 2\n450 m²\n(Retail / Tienda)",
            color=TEXT_LIGHT, fontsize=9, fontweight='bold', ha='center', va='center')

    # 3. Local Comercial 1 (350 m²)
    l1_x, l1_y, l1_w, l1_h = x0, y0 + 20.0, 20.0, 17.0
    rect_l1 = patches.Rectangle((l1_x, l1_y), l1_w, l1_h, edgecolor='#3CB371', facecolor='#123A25',
                                linewidth=1.5, alpha=0.85)
    ax.add_patch(rect_l1)
    ax.text(l1_x + l1_w/2, l1_y + l1_h/2, "LOCAL 1\n350 m²\n(Galería)",
            color=TEXT_LIGHT, fontsize=9, fontweight='bold', ha='center', va='center')

    # 4. Lobby Principal Residencial (250 m²)
    lb_x, lb_y, lb_w, lb_h = x0, y0, 20.0, 20.0
    rect_lb = patches.Rectangle((lb_x, lb_y), lb_w, lb_h, edgecolor=ACCENT_GOLD, facecolor='#3A2E0B',
                                linewidth=1.8, alpha=0.9)
    ax.add_patch(rect_lb)
    ax.text(lb_x + lb_w/2, lb_y + lb_h/2, "LOBBY RESIDENCIAL\n250 m²\n(Concierge + Control BMS)",
            color=ACCENT_GOLD, fontsize=9, fontweight='bold', ha='center', va='center')

    # 5. Núcleos H°A° (2x Gemelos 7x9m = 126 m²)
    # Núcleo A
    nc1_x, nc1_y, nc1_w, nc1_h = x0 + 25.0, y0 + 3.0, 7.0, 9.0
    rect_nc1 = patches.Rectangle((nc1_x, nc1_y), nc1_w, nc1_h, edgecolor=ACCENT_RED, facecolor='#4A0E17',
                                 linewidth=2, hatch='//')
    ax.add_patch(rect_nc1)
    ax.text(nc1_x + nc1_w/2, nc1_y + nc1_h/2, "NÚCLEO 1 H°A°\n7×9m (63m²)\n2 Asc. + Esc.",
            color='#FFAAA6', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # Núcleo B
    nc2_x, nc2_y, nc2_w, nc2_h = x0 + 48.0, y0 + 3.0, 9.0, 7.0
    rect_nc2 = patches.Rectangle((nc2_x, nc2_y), nc2_w, nc2_h, edgecolor=ACCENT_RED, facecolor='#4A0E17',
                                 linewidth=2, hatch='\\\\')
    ax.add_patch(rect_nc2)
    ax.text(nc2_x + nc2_w/2, nc2_y + nc2_h/2, "NÚCLEO 2 H°A°\n9×7m (63m²)\n2 Asc. + Esc.",
            color='#FFAAA6', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # 6. Bloque Técnico & RSU (395 m²)
    bt_x, bt_y, bt_w, bt_h = x0 + 60.0, y0, 25.0, 14.0
    rect_bt = patches.Rectangle((bt_x, bt_y), bt_w, bt_h, edgecolor=ACCENT_ORANGE, facecolor='#3A1C0B',
                                linewidth=1.5, alpha=0.85)
    ax.add_patch(rect_bt)
    ax.text(bt_x + bt_w/2, bt_y + bt_h/2, "BLOQUE TÉCNICO & RSU\n395 m²\n(RSU Estanco, BMS, Baños NBR 9050)",
            color='#FFC09F', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # 7. Rampa de Subsuelos (400 m²)
    rp_x, rp_y, rp_w, rp_h = x0 + 33.0, y0, 14.0, 12.0
    rect_rp = patches.Rectangle((rp_x, rp_y), rp_w, rp_h, edgecolor=TEXT_MUTED, facecolor='#252E38',
                                linewidth=1.5, linestyle=':')
    ax.add_patch(rect_rp)
    ax.text(rp_x + rp_w/2, rp_y + rp_h/2, "RAMPA SUBSUELOS\n400 m² (W=6m, i=15%)\n⬇ Ramal S1-S3",
            color=TEXT_LIGHT, fontsize=8, fontweight='bold', ha='center', va='center')

    # Cotas de Dimensionamiento
    ax.annotate('', xy=(x0, y0 - 2.5), xytext=(x0 + bw, y0 - 2.5),
                arrowprops=dict(arrowstyle='<->', color=ACCENT_BLUE, lw=1.5))
    ax.text(x0 + bw/2, y0 - 4.5, "Largo Huella PB = 85.00 m", color=ACCENT_BLUE, fontsize=10, fontweight='bold', ha='center')

    ax.annotate('', xy=(x0 - 2.5, y0), xytext=(x0 - 2.5, y0 + bh),
                arrowprops=dict(arrowstyle='<->', color=ACCENT_BLUE, lw=1.5))
    ax.text(x0 - 5.5, y0 + bh/2, "Ancho Huella\n37.00 m", color=ACCENT_BLUE, fontsize=10, fontweight='bold', va='center', ha='center', rotation=90)

    # Detalle Cuña Aguda Vértice P1 (61.44°)
    ax.plot([p1[0], p1[0]+25], [p1[1], p1[1]+14], color='#888888', linestyle=':', lw=1.2)
    ax.text(p1[0] + 8, p1[1] + 3, "Cuña Jardín P1\n61,44°", color=ACCENT_GOLD, fontsize=8, fontweight='bold')

    # Configuración de Ejes y Títulos
    ax.set_xlim(-15, 145)
    ax.set_ylim(-10, 85)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.3, color=TEXT_MUTED)

    ax.set_title("FIGURA 2.1 — PLANTA BAJA COMERCIAL Y DE SERVICIOS (3.145,00 m²)\nZonificación Funcional, Accesos y Vigas de Transferencia (FOS Real = 41,28% ≤ 70,00%)",
                 color=TEXT_LIGHT, fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel("Coordenadas Longitudinales X (m)", color=TEXT_MUTED, fontsize=10)
    ax.set_ylabel("Coordenadas Transversales Y (m)", color=TEXT_MUTED, fontsize=10)
    ax.tick_params(colors=TEXT_MUTED)

    # Bloque de Información ISO 19650
    info_text = (
        "PROYECTO: Tesis Edificio 18P + 3S (CDE)\n"
        "DISCIPLINA: Arquitectura (ARQ)\n"
        "NIVEL: Planta Baja (PB, Cota +0.00m)\n"
        "NORMATIVA: MCDE Ord. M. 003/2026 Art. 3°, 5° & 7°\n"
        "SUPERFICIE PB: 3.145,00 m² | TERRENO: 7.618,49 m²"
    )
    ax.text(0.98, 0.96, info_text, transform=ax.transAxes, color=TEXT_LIGHT, fontsize=8,
            ha='right', va='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='#111822', edgecolor=ACCENT_BLUE, alpha=0.9))

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "figura_2_1_zonificacion_planta_baja.png")
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=300)
    plt.close()
    print("[SUCCESS] Generado: " + output_path)


def generar_figura_2_2_volumetria():
    """Genera la Figura 2.2: Perfil Volumétrico y Relación de Plantas (18P + 3 Subsuelos)."""
    fig, ax = plt.subplots(figsize=(14, 11), dpi=300)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_CARD)

    # Eje X: Ancho del edificio (0m a 85m PB / 18.5m a 66.5m Torre)
    # Eje Y: Cotas de Nivel (-10.50m a +68.80m)

    # 1. Fundación en Roca Basáltica
    rect_basalto = patches.Rectangle((-10, -16), 105, 5.5, facecolor='#2C221E', edgecolor='#4A3831', hatch='..')
    ax.add_patch(rect_basalto)
    ax.text(42.5, -13.5, "ROCA BASÁLTICA DE FUNDACIÓN (q_adm = 300 kN/m² / Platea H=45cm)",
            color='#D4B2A7', fontsize=9, fontweight='bold', ha='center', va='center')

    # 2. Subsuelos (S3, S2, S1) - Huella 85m x 3.145m² c/u
    subsuelos = [
        ("Subsuelo 3 (S3)", -10.50, -7.40, "#1A2533", "270 Cocheras (Total 3S) + PTAR Estanca (120m²)"),
        ("Subsuelo 2 (S2)", -7.40, -4.30, "#1E2C3D", "Depósitos Privados & Estacionamiento Autos"),
        ("Subsuelo 1 (S1)", -4.30, -1.10, "#223347", "SALA ANDE (1.000kVA), Genset, Cisterna (60m³)")
    ]
    for nombre, y_bot, y_top, color, desc in subsuelos:
        rect = patches.Rectangle((0, y_bot), 85, (y_top - y_bot), edgecolor=ACCENT_BLUE, facecolor=color, linewidth=1.2, alpha=0.9)
        ax.add_patch(rect)
        ax.text(42.5, (y_bot + y_top)/2, f"{nombre} (Cota {y_bot:.2f}m) — Area: 3.145 m² | {desc}",
                color=TEXT_LIGHT, fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Línea del Terreno (Cota ±0.00m)
    ax.axhline(0, color=ACCENT_GREEN, linestyle='--', linewidth=2, label='Nivel Terreno Natural (Cota ±0.00m)')
    ax.text(-8, 0, "Nivel Ground\n±0.00m", color=ACCENT_GREEN, fontsize=9, fontweight='bold', va='center')

    # 3. Planta Baja Comercial (PB, Cota 0.00m a +4.00m) - Huella 85m x 37m = 3.145 m²
    rect_pb = patches.Rectangle((0, 0), 85, 4.0, edgecolor=ACCENT_GOLD, facecolor='#3A2E0B', linewidth=2, alpha=0.95)
    ax.add_patch(rect_pb)
    ax.text(42.5, 2.0, "PLANTA BAJA COMERCIAL & LOBBY RESIDENCIAL (3.145 m² | FOS = 41,28% ≤ 70%)\n3 Locales Comerciales (1.850 m²) + Lobby + BMS + RSU",
            color=ACCENT_GOLD, fontsize=9.5, fontweight='bold', ha='center', va='center')

    # 4. Vigas de Transferencia / Apeo H°A° (Cota +4.00m)
    viga_apeo = patches.Rectangle((0, 4.0), 85, 1.2, edgecolor=ACCENT_ORANGE, facecolor='#5E2B0C', linewidth=1.5, hatch='//')
    ax.add_patch(viga_apeo)
    ax.text(42.5, 4.6, "VIGAS DE TRANSFERENCIA H°A° (80 × 120 cm) EN COTA +4.00m (APEO DE TORRE)",
            color='#FFC09F', fontsize=8, fontweight='bold', ha='center', va='center')

    # 5. Torre Residencial (P01 a P18) — Huella Reducida 48m x 30m = 1.440 m²/piso (X: 18.5m a 66.5m)
    x_torre_0 = 18.5
    w_torre = 48.0
    y_p01 = 5.2
    h_piso = 3.1
    num_pisos = 18

    # Bloques por grupos de pilares
    grupos = [
        ("P01 a P06 (Cota +4.00m a +23.80m)", 0, 6, "#182A3A", "Pilares 80×80 cm | 36 Dptos"),
        ("P07 a P12 (Cota +23.80m a +42.40m)", 6, 12, "#1D3246", "Pilares 70×70 cm | 36 Dptos"),
        ("P13 a P18 (Cota +42.40m a +61.00m)", 12, 18, "#223B52", "Pilares 60×60 cm | 36 Dptos")
    ]

    for nombre_grp, i_start, i_end, color_grp, desc_grp in grupos:
        y_b = y_p01 + i_start * h_piso
        y_t = y_p01 + i_end * h_piso
        rect_grp = patches.Rectangle((x_torre_0, y_b), w_torre, (y_t - y_b),
                                     edgecolor=ACCENT_BLUE, facecolor=color_grp, linewidth=1.5, alpha=0.9)
        ax.add_patch(rect_grp)
        ax.text(x_torre_0 + w_torre/2, (y_b + y_t)/2, f"{nombre_grp}\nHuella: 48,00 m × 30,00 m = 1.440,00 m²/piso\n{desc_grp}",
                color=TEXT_LIGHT, fontsize=8.5, fontweight='bold', ha='center', va='center')

        # Balcones voladizo 1.50m a ambos lados
        balc_l = patches.Rectangle((x_torre_0 - 1.5, y_b), 1.5, (y_t - y_b), facecolor='#115588', alpha=0.5, edgecolor=ACCENT_BLUE)
        balc_r = patches.Rectangle((x_torre_0 + w_torre, y_b), 1.5, (y_t - y_b), facecolor='#115588', alpha=0.5, edgecolor=ACCENT_BLUE)
        ax.add_patch(balc_l)
        ax.add_patch(balc_r)

    # Dibujar líneas de entrepiso individuales
    for i in range(num_pisos + 1):
        y_losa = y_p01 + i * h_piso
        ax.plot([x_torre_0 - 1.5, x_torre_0 + w_torre + 1.5], [y_losa, y_losa], color='#4A6A8A', lw=0.8, alpha=0.7)

    # 6. Núcleos Estructurales de H°A° (Continuos desde S3 a Azotea)
    # Núcleo A: X=25m a 32m
    rect_nc_a = patches.Rectangle((25, -10.5), 7, 75.3, edgecolor=ACCENT_RED, facecolor='#4A0E17', alpha=0.4, hatch='//')
    ax.add_patch(rect_nc_a)
    ax.text(28.5, 30, "NÚCLEO 1 H°A°\n( Rigidez 78% Cortante V0=45m/s )", color='#FFAAA6', fontsize=7.5, fontweight='bold', rotation=90, ha='center', va='center')

    # Núcleo B: X=48m a 57m
    rect_nc_b = patches.Rectangle((48, -10.5), 9, 75.3, edgecolor=ACCENT_RED, facecolor='#4A0E17', alpha=0.4, hatch='\\\\')
    ax.add_patch(rect_nc_b)
    ax.text(52.5, 30, "NÚCLEO 2 H°A°\n( Rigidez 78% Cortante V0=45m/s )", color='#FFAAA6', fontsize=7.5, fontweight='bold', rotation=90, ha='center', va='center')

    # 7. Azotea Técnica & Amenities (Cota +61.00m a +64.80m)
    y_az = y_p01 + 18 * h_piso
    rect_az = patches.Rectangle((x_torre_0, y_az), w_torre, 3.8, edgecolor=ACCENT_PURPLE, facecolor='#2E1A47', linewidth=2, alpha=0.95)
    ax.add_patch(rect_az)
    ax.text(x_torre_0 + w_torre/2, y_az + 1.9, "AZOTEA TÉCNICA & AMENITIES (1.200 m² · Cota +64.30m)\nPiscina 8×16m + SUM 150m² + Gym + Salas de Máquinas",
            color='#DDBBFF', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Cotas de Altura Lateral (Eje Y)
    ax.annotate('', xy=(-5, -10.5), xytext=(-5, 64.8), arrowprops=dict(arrowstyle='<->', color=ACCENT_BLUE, lw=1.8))
    ax.text(-8, 27, "Altura Total\n75.30 m\n(18P+3S)", color=ACCENT_BLUE, fontsize=10, fontweight='bold', ha='center', va='center', rotation=90)

    # Indicador de Área Torre vs PB
    ax.annotate("Reducción de Huella:\nPB (3.145 m²) ➔ Torre (1.440 m²)\nÁrea Torre = 45,79% de PB",
                xy=(x_torre_0 + w_torre + 2, 20), xytext=(x_torre_0 + w_torre + 12, 20),
                arrowprops=dict(facecolor=ACCENT_GOLD, edgecolor=ACCENT_GOLD, arrowstyle='->', lw=1.5),
                color=ACCENT_GOLD, fontsize=9, fontweight='bold', bbox=dict(boxstyle='round,pad=0.4', facecolor='#251E0A', edgecolor=ACCENT_GOLD))

    # Configuración Ejes
    ax.set_xlim(-15, 105)
    ax.set_ylim(-18, 72)
    ax.grid(True, linestyle=':', alpha=0.25, color=TEXT_MUTED)

    ax.set_title("FIGURA 2.2 — PERFIL VOLUMÉTRICO Y RELACIÓN DE PLANTAS (EDIFICIO 18P + 3 SUBSUELOS)\nTransición Estructural, Vigas de Transferencia (+4.00m) y Núcleos Continuos de H°A°",
                 color=TEXT_LIGHT, fontsize=12.5, fontweight='bold', pad=15)
    ax.set_xlabel("Desarrollo Longitudinal (m)", color=TEXT_MUTED, fontsize=10)
    ax.set_ylabel("Cota de Nivel Z (m)", color=TEXT_MUTED, fontsize=10)
    ax.tick_params(colors=TEXT_MUTED)

    # Cuadro Resumen Técnico
    resumen_txt = (
        "CUADRO DE INDICADORES MAESTROS:\n"
        "------------------------------------\n"
        "• Superficie Terreno: 7.618,49 m²\n"
        "• FOS Real: 41,28% ≤ 70,00% (PB: 3.145 m²)\n"
        "• FOT Real: 3,97 ≤ 4,00 (30.265 m² Sobre Rasante)\n"
        "• Total Departamentos: 108 Dptos (6 dptos/piso)\n"
        "• Dotación Cocheras: 270 Plazas en 3 Subsuelos\n"
        "  (Requerimiento: 162 Res + 25 Com = 187 Autos)"
    )
    ax.text(0.98, 0.45, resumen_txt, transform=ax.transAxes, color=TEXT_LIGHT, fontsize=8,
            ha='right', va='center', bbox=dict(boxstyle='round,pad=0.5', facecolor='#111822', edgecolor=ACCENT_GREEN, alpha=0.9))

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "figura_2_2_volumetria_y_perfil_edificio.png")
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=300)
    plt.close()
    print("[SUCCESS] Generado: " + output_path)


def generar_figura_2_3_planta_tipo():
    """Genera la Figura 2.3: Zonificación de Planta Tipo Residencial (1.440 m²)."""
    fig, ax = plt.subplots(figsize=(15, 8.5), dpi=300)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_facecolor(BG_CARD)

    # Dimensiones de Planta Tipo: 48.0m x 30.0m = 1.440 m²
    x0, y0 = 0.0, 0.0
    w, h = 48.0, 30.0

    # Rectángulo Losa Planta Tipo
    rect_planta = patches.Rectangle((x0, y0), w, h, edgecolor=ACCENT_BLUE, facecolor='#162333', linewidth=2.5)
    ax.add_patch(rect_planta)

    # Balcones Perimetrales Voladizo (1.50m)
    balc_top = patches.Rectangle((x0 - 1.5, y0 + h), w + 3.0, 1.5, edgecolor=ACCENT_TEAL, facecolor='#0D3838', alpha=0.75, hatch='//')
    balc_bot = patches.Rectangle((x0 - 1.5, y0 - 1.5), w + 3.0, 1.5, edgecolor=ACCENT_TEAL, facecolor='#0D3838', alpha=0.75, hatch='//')
    ax.add_patch(balc_top)
    ax.add_patch(balc_bot)
    ax.text(w/2, y0 + h + 0.75, "BALCÓN PERIMETRAL VOLADIZO (1,50 m)", color=ACCENT_TEAL, fontsize=8, fontweight='bold', ha='center', va='center')

    # Pasillo Central de Circulación (Width = 1.80m, Y: 14.1m a 15.9m)
    pasillo = patches.Rectangle((x0, 14.1), w, 1.8, edgecolor='#666666', facecolor='#2A3440', alpha=0.9)
    ax.add_patch(pasillo)
    ax.text(6.0, 15.0, "PASILLO COMÚN DE CIRCULACIÓN (W = 1,80 m)", color=TEXT_LIGHT, fontsize=8, fontweight='bold', va='center')

    # Núcleos de H°A° (2x Gemelos)
    nc1 = patches.Rectangle((14.0, 10.5), 7.0, 9.0, edgecolor=ACCENT_RED, facecolor='#4A0E17', linewidth=1.8, hatch='//')
    nc2 = patches.Rectangle((27.0, 10.5), 9.0, 7.0, edgecolor=ACCENT_RED, facecolor='#4A0E17', linewidth=1.8, hatch='\\\\')
    ax.add_patch(nc1)
    ax.add_patch(nc2)
    ax.text(17.5, 15.0, "NÚCLEO 1\n7×9m", color='#FFAAA6', fontsize=7.5, fontweight='bold', ha='center', va='center')
    ax.text(31.5, 14.0, "NÚCLEO 2\n9×7m", color='#FFAAA6', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # --- 6 DEPARTAMENTOS POR PISO ---
    # Dpto 3D-A (140 m²) - Top Left
    d3a = patches.Rectangle((0, 15.9), 14.0, 14.1, edgecolor=ACCENT_GOLD, facecolor='#362A0B', alpha=0.85)
    ax.add_patch(d3a)
    ax.text(7.0, 23.0, "DPTO 3D-A\n140 m² útiles\n(Suite + 2 Dorm + Parrilla)", color=ACCENT_GOLD, fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Dpto 3D-B (140 m²) - Top Right
    d3b = patches.Rectangle((34.0, 15.9), 14.0, 14.1, edgecolor=ACCENT_GOLD, facecolor='#362A0B', alpha=0.85)
    ax.add_patch(d3b)
    ax.text(41.0, 23.0, "DPTO 3D-B\n140 m² útiles\n(Suite + 2 Dorm + Parrilla)", color=ACCENT_GOLD, fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Dpto 2D-A (100 m²) - Top Center
    d2a = patches.Rectangle((21.0, 15.9), 13.0, 14.1, edgecolor=ACCENT_GREEN, facecolor='#0D3622', alpha=0.85)
    ax.add_patch(d2a)
    ax.text(27.5, 23.0, "DPTO 2D-A\n100 m² útiles\n(Suite + 1 Dorm)", color='#7CE8B3', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Dpto 2D-B (100 m²) - Bottom Center
    d2b = patches.Rectangle((21.0, 0), 13.0, 14.1, edgecolor=ACCENT_GREEN, facecolor='#0D3622', alpha=0.85)
    ax.add_patch(d2b)
    ax.text(27.5, 7.0, "DPTO 2D-B\n100 m² útiles\n(Suite + 1 Dorm)", color='#7CE8B3', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Dpto 1D-A (70 m²) - Bottom Left
    d1a = patches.Rectangle((0, 0), 14.0, 14.1, edgecolor=ACCENT_PURPLE, facecolor='#2B1A42', alpha=0.85)
    ax.add_patch(d1a)
    ax.text(7.0, 7.0, "DPTO 1D-A\n70 m² útiles\n(Executive Suite)", color='#D1B3FF', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Dpto 1D-B (70 m²) - Bottom Right
    d1b = patches.Rectangle((36.0, 0), 12.0, 14.1, edgecolor=ACCENT_PURPLE, facecolor='#2B1A42', alpha=0.85)
    ax.add_patch(d1b)
    ax.text(42.0, 7.0, "DPTO 1D-B\n70 m² útiles\n(Executive Suite)", color='#D1B3FF', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Dimensionamiento Cotas
    ax.annotate('', xy=(x0, y0 - 3.5), xytext=(x0 + w, y0 - 3.5), arrowprops=dict(arrowstyle='<->', color=ACCENT_BLUE, lw=1.5))
    ax.text(w/2, y0 - 5.2, "Largo Losa Torre = 48.00 m", color=ACCENT_BLUE, fontsize=9.5, fontweight='bold', ha='center')

    ax.annotate('', xy=(x0 - 3.5, y0), xytext=(x0 - 3.5, y0 + h), arrowprops=dict(arrowstyle='<->', color=ACCENT_BLUE, lw=1.5))
    ax.text(x0 - 6.0, h/2, "Ancho Losa\n30.00 m", color=ACCENT_BLUE, fontsize=9.5, fontweight='bold', va='center', ha='center', rotation=90)

    # Configuración de Ejes
    ax.set_xlim(-10, 58)
    ax.set_ylim(-8, 38)
    ax.set_aspect('equal')
    ax.grid(True, linestyle=':', alpha=0.25, color=TEXT_MUTED)

    ax.set_title("FIGURA 2.3 — PLANTA TIPO RESIDENCIAL (P01 A P18) — HUELLA 1.440,00 m²\nOrganización Funcional de 6 Departamentos/Piso (108 Dptos Totales / 1.5 Autos por Dpto)",
                 color=TEXT_LIGHT, fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel("Desarrollo Longitudinal (m)", color=TEXT_MUTED, fontsize=9.5)
    ax.set_ylabel("Desarrollo Transversal (m)", color=TEXT_MUTED, fontsize=9.5)
    ax.tick_params(colors=TEXT_MUTED)

    # Cuadro Informativo
    info_dptos = (
        "TIPOLOGÍAS POR PLANTA (6 Dptos/Piso):\n"
        "• 2× Dpto 3 Dormitorios (140 m² útil c/u)\n"
        "• 2× Dpto 2 Dormitorios (100 m² útil c/u)\n"
        "• 2× Dpto 1 Dormitorio (70 m² útil c/u)\n"
        "---------------------------------------\n"
        "• TOTAL EDIFICIO (18P): 108 Dptos\n"
        "• DEMANDA GARAJE: 162 Cocheras Res."
    )
    ax.text(0.98, 0.95, info_dptos, transform=ax.transAxes, color=TEXT_LIGHT, fontsize=8,
            ha='right', va='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='#111822', edgecolor=ACCENT_GOLD, alpha=0.9))

    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "figura_2_3_planta_tipo_residencial.png")
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', dpi=300)
    plt.close()
    print("[SUCCESS] Generado: " + output_path)

if __name__ == "__main__":
    print("[INFO] Iniciando generacion de figuras tecnicas de alta resolucion para Sub-etapa B.1...")
    generar_figura_2_1_planta_baja()
    generar_figura_2_2_volumetria()
    generar_figura_2_3_planta_tipo()
    print("[SUCCESS] Generacion completada exitosamente!")
