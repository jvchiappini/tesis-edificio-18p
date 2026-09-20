"""
====================================================================
 GRILLA Y PILARES ESTRUCTURALES — GRILLA DEFINITIVA (idéntica a S1)
 Edificio de Uso Mixto 18P + 2 Subsuelos | CDE, Paraguay
 Metodología BIM ISO 19650 | Fuente: modelo_estructural.py
====================================================================

 La grilla estructural es DEFINITIVA y ÚNICA para todo el edificio
 (S3 → Azotea), idéntica a la usada en Subsuelos (AGENTS.md §10.0/§12.3).
 NO se optimiza con GA: los ejes son fijos y alineados a los núcleos.

 GRILLA (desde modelo_estructural.py):
   Ejes X: [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
            63.88, 71.75, 79.63, 87.50]   (12 ejes)
     - Alas: 4 vanos de 7.875m (2.5→34 y 56→87.5)
     - N1: 7m (34→41) · Pasillo técnico: 8m (41→49) · N2: 7m (49→56)
   Ejes Y: [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]   (6 ejes)
     - Frente: 7m + 7m (3→17) · Núcleos: 9m (17→26) · Fondo: 7m + 7m

 CRITERIO DE PILARES (idéntico a ga_subsuelo_3.py):
   - Se crea un pilar en CADA intersección (xi, yi) de los ejes.
   - Se RETIRAN los que caen DENTRO del área maciza de un Núcleo
     (el núcleo es pantalla H°A° y absorbe esos puntos).
   - Se MANTIENEN los pilares en los BORDES de los núcleos (perímetro)
     y en los bordes del pasillo técnico.
   - Sección inicial de referencia: 60×60 cm (la optimización de
     sección por carga axial/momento se hará en ga_pilares_dim.py).

 SALIDA:
   - Plano: outputs/plano_grilla_pilares.png
   - Datos: outputs/pilares_grilla.csv (id, x, y, nivel, sección)
====================================================================
"""

import os
import csv
import sys
import numpy as np
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modelo_estructural import XS, YS, NUCLEOS, PASILLO_TECNICO, HUELLA

# Sección inicial de pilares (m) — se optimizará en ga_pilares_dim.py
ANCHO_PILAR = 0.60


def generar_pilares(ancho=ANCHO_PILAR):
    """Genera pilares en intersecciones de la grilla, retirando los que
    caen dentro del área maciza de un núcleo (criterio de S1)."""
    pilares = []
    for x in XS:
        for y in YS:
            x0, y0 = x - ancho / 2, y - ancho / 2
            dentro_de_nucleo = False
            for c in NUCLEOS:
                if (c['x0'] + ancho) < x < (c['x1'] - ancho) and \
                   (c['y0'] + ancho) < y < (c['y1'] - ancho):
                    dentro_de_nucleo = True
                    break
            if dentro_de_nucleo:
                continue
            pilares.append(dict(id=f"P{len(pilares)+1:03d}", x=x, y=y,
                                x0=x0, y0=y0, w=ancho, h=ancho))
    return pilares


def exportar_csv(pilares, ruta):
    """Exporta pilares a CSV con id, coordenadas y sección."""
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "x_centro", "y_centro", "x0", "y0", "ancho", "alto", "seccion_m2"])
        for p in pilares:
            w.writerow([p["id"], round(p["x"], 2), round(p["y"], 2),
                        round(p["x0"], 3), round(p["y0"], 3),
                        round(p["w"], 3), round(p["h"], 3), round(p["w"] * p["h"], 3)])
    return ruta


def generar_plano():
    fig, ax = plt.subplots(figsize=(25, 12))
    fig.patch.set_facecolor('#f8fafc')
    ax.set_facecolor('#f1f5f9')

    # Huella
    h = HUELLA
    ax.add_patch(patches.Rectangle((h['x0'], h['y0']), h['ancho'], h['profundidad'],
                                   facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.5, zorder=2))

    # Núcleos gemelos
    for c in NUCLEOS:
        ax.add_patch(patches.Rectangle((c['x0'], c['y0']), c['x1'] - c['x0'], c['y1'] - c['y0'],
                                       facecolor='#334155', edgecolor='#0f172a', lw=2.5, zorder=5))
        ax.text((c['x0'] + c['x1']) / 2, (c['y0'] + c['y1']) / 2,
                f"NÚCLEO {c['id']}\n(2 asc + esc. RF + shaft)",
                fontsize=8, color='white', ha='center', va='center', fontweight='bold', zorder=6)

    # Pasillo técnico central
    p = PASILLO_TECNICO
    ax.add_patch(patches.Rectangle((p['x0'], p['y0']), p['x1'] - p['x0'], p['y1'] - p['y0'],
                                   facecolor='#a5b4fc', edgecolor='#4338ca', hatch='..',
                                   alpha=0.7, lw=1.5, zorder=4))
    ax.text((p['x0'] + p['x1']) / 2, (p['y0'] + p['y1']) / 2,
            "PASILLO TÉCNICO\nDUCTO RSU + shafts",
            fontsize=7, color='#312e81', ha='center', va='center', fontweight='bold', zorder=6)

    # Grilla: ejes con burbujas y cotas
    for i, x in enumerate(XS):
        ax.plot([x, x], [h['y0'] - 1.5, h['y1'] + 1.5], color='#94a3b8', lw=1.0, ls='--', zorder=3)
        ax.add_patch(patches.Circle((x, h['y1'] + 1.5), 0.8, fc='#ffffff', ec='#0284c7', lw=1.5, zorder=10))
        ax.text(x, h['y1'] + 1.5, chr(65 + i), fontsize=8, color='#0369a1',
                ha='center', va='center', fontweight='bold', zorder=11)
        if i > 0:
            ax.text((XS[i - 1] + x) / 2, h['y1'] + 3.2, f"{x - XS[i-1]:.2f}m",
                    fontsize=6.5, color='#475569', ha='center', fontweight='bold')
    for j, y in enumerate(YS):
        ax.plot([h['x0'] - 1.5, h['x1'] + 1.5], [y, y], color='#94a3b8', lw=1.0, ls='--', zorder=3)
        ax.add_patch(patches.Circle((h['x0'] - 1.5, y), 0.8, fc='#ffffff', ec='#0284c7', lw=1.5, zorder=10))
        ax.text(h['x0'] - 1.5, y, str(j + 1), fontsize=8, color='#0369a1',
                ha='center', va='center', fontweight='bold', zorder=11)
        if j > 0:
            ax.text(h['x0'] - 3.4, (YS[j - 1] + y) / 2, f"{y - YS[j-1]:.2f}m",
                    fontsize=6.5, color='#475569', ha='center', fontweight='bold', rotation=90)

    # Pilares
    pilares = generar_pilares()
    n_perimetral = 0
    n_interior = 0
    n_borde_nucleo = 0
    for p_ in pilares:
        x, y = p_['x'], p_['y']
        es_perimetral = (abs(x - h['x0']) < 0.1 or abs(x - h['x1']) < 0.1 or
                         abs(y - h['y0']) < 0.1 or abs(y - h['y1']) < 0.1)
        en_borde_nucleo = any(
            abs(x - c['x0']) < 0.6 or abs(x - c['x1']) < 0.6 or
            abs(y - c['y0']) < 0.6 or abs(y - c['y1']) < 0.6 for c in NUCLEOS)

        if es_perimetral:
            fc, ec = '#16a34a', '#14532d'
            n_perimetral += 1
        elif en_borde_nucleo:
            fc, ec = '#dc2626', '#991b1b'
            n_borde_nucleo += 1
        else:
            fc, ec = '#2563eb', '#1e3a8a'
            n_interior += 1

        ax.add_patch(patches.Rectangle((p_['x0'], p_['y0']), p_['w'], p_['h'],
                                       facecolor=fc, edgecolor=ec, lw=1.2, zorder=8))
        ax.text(x, y + 0.45, p_['id'], fontsize=5.0, color='#0f172a',
                ha='center', va='bottom', fontweight='bold', zorder=9)

    # Leyenda
    ax.legend(handles=[
        patches.Patch(color='#16a34a', label=f'Pilares perimetrales ({n_perimetral})'),
        patches.Patch(color='#2563eb', label=f'Pilares interiores ({n_interior})'),
        patches.Patch(color='#dc2626', label=f'Pilares borde de núcleo ({n_borde_nucleo})'),
        patches.Patch(color='#334155', label='Núcleos H°A° (pantallas)'),
    ], loc='lower right', fontsize=8, framealpha=0.98)

    info = (
        "GRILLA ESTRUCTURAL DEFINITIVA (idéntica a S1):\n"
        "────────────────────────────────────────────────\n"
        f"• Ejes X: {len(XS)} | Ejes Y: {len(YS)}\n"
        f"• Total pilares: {len(pilares)} (sección inicial 60×60 cm)\n"
        f"  - Perimetrales: {n_perimetral} | Interiores: {n_interior} | Borde núcleo: {n_borde_nucleo}\n"
        "• Vanos alas: 7.875m × 4 | Núcleos: 7m | Pasillo: 8m\n"
        "• Vanos Y: 7m + 7m frente | Núcleos: 9m | 7m + 7m fondo\n"
        "• Se retiran pilares dentro del área maciza de núcleos\n"
        "• Sección a optimizar por carga axial/momento (NBR 6118)"
    )
    ax.text(h['x0'] + 0.5, h['y0'] + 0.5, info, fontsize=7.5, fontweight='bold',
            va='bottom', ha='left', color='#0f172a',
            bbox=dict(boxstyle='round,pad=0.4', fc='#ffffff', ec='#1e3a8a', lw=1.5), zorder=12)

    ax.set_xlim(h['x0'] - 6, h['x1'] + 4)
    ax.set_ylim(h['y0'] - 8, h['y1'] + 7)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("GRILLA DE EJES Y PILARES ESTRUCTURALES H°A° — GRILLA DEFINITIVA (idéntica a Subsuelos)\n"
                 f"Edificio 18P + 2 Subsuelos · {len(XS)} ejes X × {len(YS)} ejes Y · {len(pilares)} pilares · "
                 "Continuidad vertical 100% (S3→Azotea)",
                 fontsize=11, fontweight='bold')

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_png = os.path.join(out_dir, "plano_grilla_pilares.png")
    out_csv = os.path.join(out_dir, "pilares_grilla.csv")
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)
    plt.close()
    exportar_csv(pilares, out_csv)
    print(f"[OK] {out_png}")
    print(f"[OK] {out_csv}")
    print(f"     Pilares: {len(pilares)} | Perimetrales {n_perimetral} | "
          f"Interiores {n_interior} | Borde núcleo {n_borde_nucleo}")
    return pilares


if __name__ == "__main__":
    generar_plano()
