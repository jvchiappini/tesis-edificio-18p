"""
====================================================================
 SUBSUELO 2 (S2) — COCHERAS (Cota -7.00 m)
 Edificio de Uso Mixto 18P + 3 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | Layout reutilizado de S3
====================================================================

 Bounding Box Edificio por Nivel (idéntico a S3/PB):
   X: [2.5 → 87.5 m]   (Frente Urbano = 85.0 m)
   Y: [3.0 → 40.0 m]   (Profundidad Total = 37.0 m)

 Programa S2 (solo cocheras, MISMO layout que S3 — ✅ Validado):
   - 98 plazas: 80 autos (2.5×5.0 m) + 18 motos (1.2×2.5 m)
   - Plazas ubicadas manualmente en AutoCAD (DXF) y extraídas
     con extraer_cocheras_dxf.py → STALLS_MANUALES en ga_subsuelo_3.py
   - Módulo auto: 2.50 × 5.00 m | Moto: 1.20 × 2.50 m

 2 NÚCLEOS H°A° GEMELOS ROTADOS 90° (continúan desde todos los niveles):
   N1 Oeste: X: 34.0→41.0 / Y: 17.0→26.0 (7m × 9m)
   N2 Este : X: 49.0→56.0 / Y: 17.0→26.0 (7m × 9m)

 Pasillo técnico central entre núcleos (X: 41.0→49.0 / Y: 17→26):
   - Ducto RSU Ø500mm + shafts de servicios (8m de ancho).

 DOBLE RAMPA ESQUINA-ESQUINA (todos los niveles, entrada+salida):
   - Rampa ENTRADA (bajada): Esquina SE X: 81.5→87.5 / Y: 3.0→10.0 (6m, 2 carriles)
   - Rampa SALIDA (subida): Esquina NO X: 2.5→8.5 / Y: 33.0→40.0 (6m, 2 carriles)

 GRILLA ESTRUCTURAL ÓPTIMA (continua S3→Azotea, alineada a núcleos):
   Ejes X: [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
            63.88, 71.75, 79.63, 87.50]
   Ejes Y: [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

 PILARES: 90×90 cm en S3/S2 (ANCHO_PILAR = 0.90), continuos S3→Azotea.

 OUTPUT: outputs/planta_subsuelo_2.png
====================================================================
"""

import os
import sys

import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ga_subsuelo_3 as ga

# Constantes del S2 (misma huella, núcleos, rampas, grilla y pilares)
X_MIN, X_MAX = ga.X_MIN, ga.X_MAX
Y_MIN, Y_MAX = ga.Y_MIN, ga.Y_MAX
NUCLEOS = ga.NUCLEOS
PASILLO_TECNICO = ga.PASILLO_TECNICO
RAMPA_ENTRADA = ga.RAMPA_ENTRADA
RAMPA_SALIDA = ga.RAMPA_SALIDA
XS, YS = ga.XS, ga.YS
STALL_W, STALL_D = ga.STALL_W, ga.STALL_D


def generar():
    fig, ax = plt.subplots(figsize=(22, 12))
    fig.patch.set_facecolor('#f8fafc')
    ax.set_facecolor('#f1f5f9')

    ax.add_patch(Rectangle((X_MIN, Y_MIN), X_MAX - X_MIN, Y_MAX - Y_MIN,
                           facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.5, zorder=2))

    # COCHERAS (mismo layout que S3 — 80 autos + 18 motos)
    total_autos = 0
    total_motos = 0
    for s in ga.STALLS_MANUALES:
        es_moto = s['h'] < 3.0 or s['w'] < 1.8
        if es_moto:
            total_motos += 1
            col, edge = '#fde68a', '#b45309'
        else:
            total_autos += 1
            col, edge = '#bae6fd', '#0369a1'
        ax.add_patch(Rectangle((s['x0'] + 0.05, s['y0'] + 0.05),
                               s['w'] - 0.1, s['h'] - 0.1,
                               facecolor=col, edgecolor=edge, lw=0.6, zorder=4))
    total_stalls = total_autos + total_motos

    # PILARES ESTRUCTURALES H°A° (90×90, continuos)
    pilares, n_pilares = ga.generar_pilares()
    for (x0, y0, w, h) in pilares:
        ax.add_patch(Rectangle((x0, y0), w, h,
                               facecolor='#f8fafc', edgecolor='#0f172a', lw=1.0, zorder=6))

    # DOBLE RAMPA ESQUINA-ESQUINA
    for rampa, etiqueta in [
        (RAMPA_ENTRADA, "RAMPA ENTRADA\n(bajada, giro 90°)"),
        (RAMPA_SALIDA,  "RAMPA SALIDA\n(subida, giro 90°)"),
    ]:
        ax.add_patch(Rectangle((rampa['x0'], rampa['y0']),
                               rampa['x1'] - rampa['x0'], rampa['y1'] - rampa['y0'],
                               facecolor='#f97316', edgecolor='#c2410c', hatch='//', alpha=0.85, zorder=5))
        ax.text((rampa['x0'] + rampa['x1']) / 2, (rampa['y0'] + rampa['y1']) / 2,
                etiqueta, fontsize=7.5, fontweight='bold',
                color='white', ha='center', va='center', zorder=6)

    # Pasillo técnico central
    p = PASILLO_TECNICO
    ax.add_patch(Rectangle((p['x0'], p['y0']), p['x1'] - p['x0'], p['y1'] - p['y0'],
                           facecolor='#a5b4fc', edgecolor='#4338ca', hatch='..', alpha=0.7, zorder=5))
    ax.text((p['x0'] + p['x1']) / 2, (p['y0'] + p['y1']) / 2,
            "PASILLO TÉCNICO\n(ducto RSU Ø500\n+ servicios)",
            fontsize=6.5, fontweight='bold', color='#312e81', ha='center', va='center', zorder=6)

    # Núcleos
    for c in NUCLEOS:
        ax.add_patch(Rectangle((c['x0'], c['y0']), c['x1'] - c['x0'], c['y1'] - c['y0'],
                               facecolor='#334155', edgecolor='#0f172a', lw=2.5, zorder=7))
        ax.text((c['x0'] + c['x1']) / 2, (c['y0'] + c['y1']) / 2,
                f"NÚCLEO {c['nombre']}\n(continúa desde PB)\n2 asc + escalera RF",
                color='white', fontsize=7, fontweight='bold', ha='center', va='center', zorder=8)

    # Grilla
    for x in XS:
        ax.plot([x, x], [Y_MIN - 1.5, Y_MAX + 1.5], color='#64748b', lw=1.0, ls='--', zorder=1)
    for y in YS:
        ax.plot([X_MIN - 1.5, X_MAX + 1.5], [y, y], color='#64748b', lw=1.0, ls='--', zorder=1)

    # Etiquetas de ejes
    for i, x in enumerate(XS):
        ax.text(x, Y_MIN - 1.9, f"{i+1}", fontsize=8, fontweight='bold', color='#0f172a',
                ha='center', va='top', zorder=12)
    for i, y in enumerate(YS):
        ax.text(X_MIN - 1.9, y, chr(65 + i), fontsize=8, fontweight='bold', color='#0f172a',
                ha='right', va='center', zorder=12)

    resumen = (
        "SUBSUELO 2 (S2) — NIVEL -7.00 m (solo cocheras):\n"
        "────────────────────────────────────────────────\n"
        f"• PLAZAS DE ESTACIONAMIENTO: {total_stalls} TOTAL ({total_autos} autos + {total_motos} motos)\n"
        "• MISMO layout que S3 (autos 2.5×5.0 / motos 1.2×2.5)\n"
        f"• PILARES H°A° en grilla (90x90 cm, continuos S3→Azotea): {n_pilares}\n"
        "• 2 Núcleos H°A° gemelos rotados: N1 X:34→41 / N2 X:49→56 (Y:17→26)\n"
        "• Pasillo técnico central (X:41→49, 8m): ducto RSU Ø500mm + servicios\n"
        "• DOBLE RAMPA ESQUINA-ESQUINA: Entrada SE + Salida NO (6m, 2 carriles)\n"
        "• Altura de entrepiso: 3.50 m | Cota -7.00 m\n"
        "• S2: sin salas técnicas (quedan en S1)"
    )
    ax.text(X_MIN, Y_MIN - 5.5, resumen, fontsize=8.5, fontweight='bold', va='top',
            bbox=dict(boxstyle='round,pad=0.6', facecolor='white', edgecolor='#0284c7', lw=1.5), zorder=20)

    ax.set_xlim(X_MIN - 7, X_MAX + 4)
    ax.set_ylim(Y_MIN - 12, Y_MAX + 3)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title(f"SUBSUELO 2 (S2) — COCHERAS + PILARES Y GRILLA — {total_stalls} PLAZAS / {n_pilares} PILARES (90x90)",
              fontsize=13, fontweight='bold')

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "planta_subsuelo_2.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Plazas de estacionamiento S2: {total_stalls} ({total_autos} autos + {total_motos} motos)")
    print(f"Generado: {out_path}")
    return total_stalls


if __name__ == "__main__":
    generar()