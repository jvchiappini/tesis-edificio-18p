"""
====================================================================
 MÓDULO COMÚN — PLANTA TIPO RESIDENCIAL P01-P18 (3 LAYOUTS)
 Comparte la geometría y el dibujo entre ga_planta_tipo_A/B/C.py
 Edificio 18P + 2 Subsuelos | Ciudad del Este, Paraguay
====================================================================

 Geometría (idéntica a PB/subsuelos, AGENTS.md §11.1):
   X: [2.5 → 87.5 m]  (Frente = 85.0 m)  |  Y: [3.0 → 40.0 m]  (Prof = 37.0 m)
   Núcleos gemelos: N1 X:34→41 / N2 X:49→56 · Y:17→26 (7m×9m, rotados 90°)
   Pasillo técnico central: X:41→49 / Y:17→26 (ducto RSU Ø500 + shafts)
   Bandas residenciales:
     Balcón Sur   Y: 3.0→4.5  (1.5m)  |  Banda Sur   Y: 4.5→16.5 (12.0m)
     Corredor Sur Y: 16.5→18.0 (1.5m)  |  Central    Y: 18.0→25.0
     Corredor Nor Y: 25.0→27.0 (2.0m)  |  Banda Nor   Y: 27.0→38.5 (11.5m)
     Balcón Norte Y: 38.5→40.0 (1.5m)
   Pozos de luz: A X:5→19 / B X:71→85 · Y:18→25 (14m×7m = 98 m² c/u)
   Grilla estructural: XS y YS (continua S3→Azotea)
   Balcones en casi todo el perímetro exterior (corridos sur/norte +
   esquinas con balcón lateral).

 USO (desde un script de layout):
   from _planta_tipo_common import generar_plano_layout, normalizar, RESUMEN_FINAL
   w_sur, w_nor = normalizar([...])   # anchos por banda, suman 85m
   generar_plano_layout("A", "TITULO", w_sur, w_nor, "planta_tipo_layout_A.png")
====================================================================
"""

import os
import numpy as np
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ──────────────────────────────────────────────────────────────────
# PARÁMETROS GLOBALES
# ──────────────────────────────────────────────────────────────────
X_MIN, X_MAX = 2.5, 87.5
Y_MIN, Y_MAX = 3.0, 40.0
ANCHO_TOTAL = X_MAX - X_MIN     # 85.0 m
PROF_TOTAL  = Y_MAX - Y_MIN     # 37.0 m

BAL_S_Y0, BAL_S_Y1     = 3.0, 4.5
BAND_S_Y0, BAND_S_Y1   = 4.5, 16.5
COR_S_Y0, COR_S_Y1     = 16.5, 18.0
CENTRAL_Y0, CENTRAL_Y1 = 18.0, 25.0
COR_N_Y0, COR_N_Y1     = 25.0, 27.0
BAND_N_Y0, BAND_N_Y1   = 27.0, 38.5
BAL_N_Y0, BAL_N_Y1     = 38.5, 40.0

PROF_S = BAND_S_Y1 - BAND_S_Y0     # 12.0 m
PROF_N = BAND_N_Y1 - BAND_N_Y0     # 11.5 m

NUCLEOS = [
    dict(x0=34.0, x1=41.0, y0=17.0, y1=26.0, nombre="N1"),
    dict(x0=49.0, x1=56.0, y0=17.0, y1=26.0, nombre="N2"),
]
PASILLO_TECNICO = dict(x0=41.0, x1=49.0, y0=17.0, y1=26.0)
POZO_A = dict(x0=5.0, x1=19.0, y0=18.0, y1=25.0)
POZO_B = dict(x0=71.0, x1=85.0, y0=18.0, y1=25.0)

XS = [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00, 63.88, 71.75, 79.63, 87.50]
YS = [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]


def normalizar(anchos, total=ANCHO_TOTAL):
    """Escala una lista de anchos para que sumen el total (85m)."""
    factor = total / sum(anchos)
    return [w * factor for w in anchos]


# ──────────────────────────────────────────────────────────────────
# TIPOLOGÍAS
# ──────────────────────────────────────────────────────────────────
def tipologia(area):
    if area < 75.0:
        return ("TIPO A · 1 DORM. / STUDIO", "1 DORM.", "#ecfeff", "#0891b2", "#164e63")
    elif area < 95.0:
        return ("TIPO B · 2 DORM. STANDARD", "2 DORM. STD", "#eff6ff", "#2563eb", "#1e3a8a")
    elif area < 120.0:
        return ("TIPO C · 2 DORM. SUITE", "2 DORM. SUITE", "#ecfdf5", "#059669", "#064e3b")
    else:
        return ("TIPO D · 3 DORM. PREMIUM", "3 DORM. PREM", "#fffbeb", "#d97706", "#78350f")


# ──────────────────────────────────────────────────────────────────
# DIBUJO
# ──────────────────────────────────────────────────────────────────
def _rect(ax, x, y, w, h, fc, ec, lw=1.2, hatch=None, zorder=3):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec,
                               linewidth=lw, hatch=hatch, zorder=zorder))


def _txt(ax, x, y, txt, fs=6.5, fw='bold', color='#1e293b', zorder=5):
    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,
            ha='center', va='center', zorder=zorder)


def dibujar_nucleos(ax):
    for c in NUCLEOS:
        _rect(ax, c['x0'], c['y0'], c['x1'] - c['x0'], c['y1'] - c['y0'],
              '#334155', '#0f172a', lw=2.5, zorder=8)
        _txt(ax, (c['x0'] + c['x1']) / 2, (c['y0'] + c['y1']) / 2,
             f"NÚCLEO {c['nombre']}\n2 asc + esc. RF\n(shafts c/u)",
             fs=6.5, fw='bold', color='white', zorder=9)
    p = PASILLO_TECNICO
    _rect(ax, p['x0'], p['y0'], p['x1'] - p['x0'], p['y1'] - p['y0'],
          '#a5b4fc', '#4338ca', hatch='..', lw=1.5, zorder=7)
    _txt(ax, (p['x0'] + p['x1']) / 2, (p['y0'] + p['y1']) / 2,
         "PASILLO TÉCNICO\nDUCTO RSU Ø500\n+ shafts", fs=5.5, fw='bold',
         color='#312e81', zorder=9)


def dibujar_pozos(ax):
    for pz, tag in [(POZO_A, "POZO A"), (POZO_B, "POZO B")]:
        _rect(ax, pz['x0'], pz['y0'], pz['x1'] - pz['x0'], pz['y1'] - pz['y0'],
              '#e0f2fe', '#0284c7', hatch='////', lw=1.5, zorder=5)
        _txt(ax, (pz['x0'] + pz['x1']) / 2, (pz['y0'] + pz['y1']) / 2,
             f"{tag}\n14m × 7m\n(98 m²)\n· aire y luz ·",
             fs=6.0, fw='bold', color='#0369a1', zorder=6)


def dibujar_apartamento(ax, x0, w, es_sur=True, idx=1):
    if es_sur:
        y0, h = BAND_S_Y0, PROF_S
        bal_y0, bal_h = BAL_S_Y0, BAL_S_Y1 - BAL_S_Y0
        acc_y = COR_S_Y0
        flecha = "▲"
        zona_social_y = y0 + 1.0
        zona_priv_y = y0 + h - 3.5
    else:
        y0, h = BAND_N_Y0, PROF_N
        bal_y0, bal_h = BAL_N_Y0, BAL_N_Y1 - BAL_N_Y0
        acc_y = COR_N_Y1
        flecha = "▼"
        zona_social_y = y0 + h - 5.5
        zona_priv_y = y0 + 1.0

    area = w * h
    tag, tag_corto, fc, ec, tc = tipologia(area)

    _rect(ax, x0, y0, w, h, fc, ec, lw=1.5, zorder=4)

    if es_sur:
        _txt(ax, x0 + w / 2, zona_social_y, "SOCIAL", fs=4.2, color=tc, zorder=5)
        _txt(ax, x0 + w / 2, y0 + h / 2 - 0.3, "SERVICIO", fs=4.2, color=tc, zorder=5)
        _txt(ax, x0 + w / 2, zona_priv_y, "PRIVADA", fs=4.2, color=tc, zorder=5)
    else:
        _txt(ax, x0 + w / 2, zona_priv_y, "PRIVADA", fs=4.2, color=tc, zorder=5)
        _txt(ax, x0 + w / 2, y0 + h / 2 - 0.3, "SERVICIO", fs=4.2, color=tc, zorder=5)
        _txt(ax, x0 + w / 2, zona_social_y, "SOCIAL", fs=4.2, color=tc, zorder=5)

    cy = y0 + h / 2.0
    _rect(ax, x0 + 0.25, cy - 1.6, w - 0.5, 3.2, '#ffffff', ec, lw=1.0, zorder=7)
    _txt(ax, x0 + w / 2, cy + 0.9, f"APT {idx:02d}", fs=6.0, fw='bold', color='#0f172a', zorder=8)
    _txt(ax, x0 + w / 2, cy + 0.1, tag_corto, fs=5.0, fw='bold', color=tc, zorder=8)
    _txt(ax, x0 + w / 2, cy - 0.7, f"{area:.1f} m²", fs=6.0, fw='bold', color='#0f172a', zorder=8)
    _txt(ax, x0 + w / 2, cy - 1.2, f"({w:.1f}m × {h:.1f}m)", fs=4.5, fw='normal', color='#475569', zorder=8)

    _rect(ax, x0, bal_y0, w, bal_h, '#fef9c3', '#ca8a04', lw=1.0, hatch='...', zorder=6)
    if w > 6.5:
        _txt(ax, x0 + w / 2, bal_y0 + bal_h / 2, "BALCÓN", fs=4.5, fw='bold', color='#78350f', zorder=7)

    ax.plot([x0 + w / 2 - 0.4, x0 + w / 2 + 0.4], [acc_y, acc_y],
            color='#dc2626', lw=2.5, zorder=8)
    _txt(ax, x0 + w / 2, acc_y + (0.5 if es_sur else -0.5), f"{flecha} ACCESO",
         fs=4.2, color='#dc2626', fw='bold', zorder=8)

    ax.plot([x0 + w, x0 + w], [y0, y0 + h], color='#334155', lw=1.2, zorder=5)


def dibujar_banda(ax, w_banda, es_sur=True):
    x = X_MIN
    for idx, w in enumerate(w_banda, 1):
        dibujar_apartamento(ax, x, w, es_sur=es_sur, idx=idx)
        x += w


def dibujar_estructura_fija(ax):
    _rect(ax, X_MIN, Y_MIN, ANCHO_TOTAL, PROF_TOTAL, '#ffffff', '#0f172a', lw=3.0, zorder=2)

    _rect(ax, X_MIN, COR_S_Y0, ANCHO_TOTAL, COR_S_Y1 - COR_S_Y0, '#ffedd5', '#ea580c', lw=1.2, zorder=3)
    _txt(ax, 45.0, (COR_S_Y0 + COR_S_Y1) / 2, "CORREDOR SUR — 1.50 m", fs=6.0, color='#9a3412', zorder=4)
    _rect(ax, X_MIN, COR_N_Y0, ANCHO_TOTAL, COR_N_Y1 - COR_N_Y0, '#ffedd5', '#ea580c', lw=1.2, zorder=3)
    _txt(ax, 45.0, (COR_N_Y0 + COR_N_Y1) / 2, "CORREDOR NORTE — 2.00 m", fs=6.0, color='#9a3412', zorder=4)

    dibujar_pozos(ax)
    dibujar_nucleos(ax)

    for x in XS:
        ax.plot([x, x], [Y_MIN, Y_MAX], color='#94a3b8', lw=0.7, ls='--', zorder=1)
    for y in YS:
        ax.plot([X_MIN, X_MAX], [y, y], color='#94a3b8', lw=0.7, ls='--', zorder=1)

    # Pilares estructurales (grilla continua S3→Azotea)
    S_PILAR = 0.75  # sección orientativa en P01–P18 (m) — AGENTS.md §12.2
    for x in XS:
        for y in YS:
            ax.add_patch(plt.Rectangle((x - S_PILAR / 2, y - S_PILAR / 2), S_PILAR, S_PILAR,
                                       facecolor='#334155', edgecolor='#0f172a', lw=0.8, zorder=14))

    _rect(ax, X_MIN, BAL_S_Y0, ANCHO_TOTAL, BAL_S_Y1 - BAL_S_Y0, '#fef9c3', '#ca8a04', lw=1.0, zorder=3)
    _rect(ax, X_MIN, BAL_N_Y0, ANCHO_TOTAL, BAL_N_Y1 - BAL_N_Y0, '#fef9c3', '#ca8a04', lw=1.0, zorder=3)


# ──────────────────────────────────────────────────────────────────
# GENERACIÓN DE PLANO DE UN LAYOUT
# ──────────────────────────────────────────────────────────────────
def generar_plano_layout(codigo, titulo, w_sur, w_nor, out_name):
    fig, ax = plt.subplots(figsize=(22, 12))
    fig.patch.set_facecolor('#f1f5f9')
    ax.set_facecolor('#e2e8f0')

    dibujar_estructura_fija(ax)
    dibujar_banda(ax, w_sur, es_sur=True)
    dibujar_banda(ax, w_nor, es_sur=False)

    areas = [w * PROF_S for w in w_sur] + [w * PROF_N for w in w_nor]
    n_a = sum(1 for a in areas if a < 75.0)
    n_b = sum(1 for a in areas if 75.0 <= a < 95.0)
    n_c = sum(1 for a in areas if 95.0 <= a < 120.0)
    n_d = sum(1 for a in areas if a >= 120.0)

    leyenda = [
        mpatches.Patch(fc='#ecfeff', ec='#0891b2', label='TIPO A · 1 Dorm/Studio (< 75 m²)'),
        mpatches.Patch(fc='#eff6ff', ec='#2563eb', label='TIPO B · 2 Dorm Std (75-95 m²)'),
        mpatches.Patch(fc='#ecfdf5', ec='#059669', label='TIPO C · 2 Dorm Suite (95-120 m²)'),
        mpatches.Patch(fc='#fffbeb', ec='#d97706', label='TIPO D · 3 Dorm Premium (≥ 120 m²)'),
        mpatches.Patch(fc='#fef9c3', ec='#ca8a04', hatch='...', label='Balcones exteriores (1.5m)'),
        mpatches.Patch(fc='#ffedd5', ec='#ea580c', label='Corredores (1.5-2.0m)'),
        mpatches.Patch(fc='#e0f2fe', ec='#0284c7', hatch='////', label='Pozos de luz A/B (98 m² c/u)'),
        mpatches.Patch(fc='#334155', ec='#0f172a', label='Núcleos H°A° N1/N2 (63 m² c/u)'),
        mpatches.Patch(fc='#a5b4fc', ec='#4338ca', hatch='..', label='Pasillo técnico central (RSU Ø500)'),
    ]
    ax.legend(handles=leyenda, loc='lower center', ncol=5, fontsize=7.5,
              framealpha=0.98, edgecolor='#0f172a', bbox_to_anchor=(0.5, -0.06), borderpad=0.8)

    info = (
        f"LAYOUT {codigo} — {titulo}\n"
        f"• Unidades/piso: {len(w_sur) + len(w_nor)} ({len(w_sur)} Sur + {len(w_nor)} Norte)\n"
        f"• Área media: {np.mean(areas):.1f} m² | Mín {min(areas):.1f} | Máx {max(areas):.1f}\n"
        f"• Desglose: A={n_a} · B={n_b} · C={n_c} · D={n_d}\n"
        f"• Superficie residencial neta: {sum(areas):.0f} m² ({sum(areas)/(ANCHO_TOTAL*PROF_TOTAL):.1%})"
    )
    ax.text(X_MIN + 0.5, CENTRAL_Y0 + 0.4, info, fontsize=7.0, color='#0f172a',
            va='top', ha='left', zorder=10,
            bbox=dict(boxstyle='round,pad=0.6', fc='#ffffff', ec='#2563eb', lw=1.5))

    ax.set_xlim(-1.0, 93.0)
    ax.set_ylim(1.5, 43.0)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(True, ls=':', alpha=0.3, color='#94a3b8', zorder=0)

    ax.set_title(
        f"PLANTA TIPO RESIDENCIAL — LAYOUT {codigo} ({titulo})\n"
        f"Edificio 18P + 2 Subsuelos · CDE, Paraguay  |  {len(w_sur)+len(w_nor)} apartamentos/piso  |  "
        f"Área media {np.mean(areas):.1f} m²  |  Balcones en todo el perímetro exterior",
        fontsize=11, fontweight='bold', pad=12
    )

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, out_name)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[OK] {out_path}")
    print(f"  Unidades/piso: {len(w_sur)+len(w_nor)} | media {np.mean(areas):.1f} m² | "
          f"A={n_a} B={n_b} C={n_c} D={n_d}")
    return areas


def generar_esquema_intercalado():
    """Esquema de los 18 pisos con el patrón de intercalado (A,C,B repetido)."""
    patron = [("A", "C", "B")[(p - 1) % 3] for p in range(1, 19)]

    fig, ax = plt.subplots(figsize=(18, 6))
    fig.patch.set_facecolor('#f8fafc')
    cols = {'A': '#ecfeff', 'C': '#ecfdf5', 'B': '#fffbeb'}
    edges = {'A': '#0891b2', 'C': '#059669', 'B': '#d97706'}
    desc = {
        'A': 'Pequeños (16/banda)\n≈62-64 m² · 32 aptos',
        'C': 'Combinados (12/banda)\n≈55-120 m² · 24 aptos',
        'B': 'Grandes (8/banda)\n≈120-127 m² · 16 aptos',
    }

    for p, t in enumerate(patron, 1):
        ax.add_patch(plt.Rectangle((p - 1, 0), 1, 1, fc=cols[t], ec=edges[t], lw=2))
        ax.text(p - 0.5, 0.5, f"P{p:02d}\n{t}", ha='center', va='center',
                fontsize=7, fontweight='bold', color='#0f172a')

    ax.set_xlim(0, 18)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    ax.set_title("INTERCALADO DE LAYOUTS — P01 a P18 (P18 = apartamentos grandes ✓)\n"
                 "Patrón A,C,B repetido · A=pequeños · C=combinados · B=grandes",
                 fontsize=11, fontweight='bold')

    n_a = patron.count('A')
    n_b = patron.count('B')
    n_c = patron.count('C')
    ax.text(9.0, -0.28,
            f"A: P01,04,07,10,13,16 = {n_a} × 32 = {n_a*32} aptos   |   "
            f"C: P02,05,08,11,14,17 = {n_c} × 24 = {n_c*24} aptos   |   "
            f"B: P03,06,09,12,15,18 = {n_b} × 16 = {n_b*16} aptos   |   "
            f"TOTAL = {n_a*32 + n_b*16 + n_c*24} apartamentos",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#334155')

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "esquema_intercalado_18_pisos.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"[OK] {out_path}")


# ──────────────────────────────────────────────────────────────────
# RESULTADOS ESPERADOS (para resumen final)
# ──────────────────────────────────────────────────────────────────
RESUMEN_FINAL = (
    "RESUMEN EDIFICIO P01-P18 (18 pisos residenciales):\n"
    "  Layout A (pequeños):  6 pisos × 32 = 192 aptos\n"
    "  Layout C (combinados): 6 pisos × 24 = 144 aptos\n"
    "  Layout B (grandes):    6 pisos × 16 =  96 aptos  (P18 incluido)\n"
    "  TOTAL: 432 apartamentos"
)
