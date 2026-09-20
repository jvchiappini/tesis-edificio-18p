"""
====================================================================
 SUBSUELO 1 (S1) — COCHERAS + SALAS TÉCNICAS (Cota -3.50 m)
 Edificio de Uso Mixto 18P + 2 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | Layout S3 adaptado con salas técnicas
====================================================================

 Bounding Box Edificio por Nivel (idéntico a S2/S3/PB):
   X: [2.5 → 87.5 m]   (Frente Urbano = 85.0 m)
   Y: [3.0 → 40.0 m]   (Profundidad Total = 37.0 m)

 Programa S1 (cocheras + salas técnicas):
   - 56 plazas: 44 autos (2.5×5.0 m) + 12 motos (1.2×2.5 m)
     (se pierden 18 plazas del layout S3 por las salas técnicas)
   - Salas técnicas agrupadas (~350 m² bruto) en BLOQUE TÉCNICO central
     (X:34→56 / Y:26→40) consolidado sobre los núcleos, + EBAR aislado:
       • Cisternas + bombas (fondo central, X:41→49 / Y:26→40, 112 m²):
         cisterna potable ~56 m³, cisterna PCI ~56 m³, salas de bombas
       • Grupo electrógeno + tableros + depósito (X:49→56 / Y:26→40, 98 m²):
         grupo ~35 m², tableros ~20 m², depósito ~20 m²
       • PTE pluvial (X:34→41 / Y:33→40, 49 m²)
       • Taller de mantenimiento (X:34→41 / Y:26→33, 49 m²)
       • EBAR cloacal aislado en esquina SE (X:81.5→87.5 / Y:3→10, 42 m²)
   - El subsuelo NO desagota por gravedad → EBAR + PTE obligatorios.

 2 NÚCLEOS H°A° GEMELOS ROTADOS 90° (continúan desde todos los niveles):
   N1 Oeste: X: 34.0→41.0 / Y: 17.0→26.0 (7m × 9m)
   N2 Este : X: 49.0→56.0 / Y: 17.0→26.0 (7m × 9m)

 Pasillo técnico central entre núcleos (X: 41.0→49.0 / Y: 17→26):
   - Ducto RSU Ø500mm + shafts de servicios (8m de ancho).

 RAMPA ÚNICA S1 (difiere de S2/S3 — NO es doble esquina-esquina):
   - Rampa única en la esquina NE (superior derecha):
     X: 81.5→87.5 / Y: 33.0→40.0 (6m, 2 carriles), mirando hacia el OESTE.

 GRILLA ESTRUCTURAL ÓPTIMA (continua S3→Azotea, alineada a núcleos):
   Ejes X: [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
            63.88, 71.75, 79.63, 87.50]
   Ejes Y: [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

 PILARES: 90×90 cm en S1/S2/S3 (ANCHO_PILAR = 0.90), continuos S3→Azotea.

 OUTPUT: outputs/planta_subsuelo_1.png
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

# Constantes del S1 (misma huella, núcleos, rampas, grilla y pilares)
X_MIN, X_MAX = ga.X_MIN, ga.X_MAX
Y_MIN, Y_MAX = ga.Y_MIN, ga.Y_MAX
NUCLEOS = ga.NUCLEOS
PASILLO_TECNICO = ga.PASILLO_TECNICO
XS, YS = ga.XS, ga.YS
STALL_W, STALL_D = ga.STALL_W, ga.STALL_D

# RAMPA ÚNICA S1 (esquina NE, superior derecha, mirando hacia el oeste)
RAMPA_S1 = dict(x0=81.5, x1=87.5, y0=33.0, y1=40.0, orientacion="oeste")


def solapa(s, sal):
    """Devuelve True si la cochera s solapa la sala técnica sal."""
    return not (s['x0'] + s['w'] <= sal['x0'] or s['x0'] >= sal['x1'] or
                s['y0'] + s['h'] <= sal['y0'] or s['y0'] >= sal['y1'])


# ------------------------------------------------------------------
# SALAS TÉCNICAS DEL S1 (BLOQUE TÉCNICO agrupado X:34→56 / Y:26→40 + EBAR SE)
# ------------------------------------------------------------------
SALAS_TECNICAS = [
    dict(x0=41.0, x1=49.0, y0=26.0, y1=40.0, nombre="CISTERNAS + BOMBAS\n(potable + PCI)"),
    dict(x0=49.0, x1=56.0, y0=26.0, y1=40.0, nombre="GRUPO ELECTRÓGENO\n+ TABLEROS + DEPÓSITO"),
    dict(x0=34.0, x1=41.0, y0=26.0, y1=33.0, nombre="TALLER\nMANTENIMIENTO"),
    dict(x0=34.0, x1=41.0, y0=33.0, y1=40.0, nombre="PTE\n(pluvial)"),
    dict(x0=81.5, x1=87.5, y0=3.0, y1=10.0, nombre="EBAR\n(cloacal)"),
]

# Colores de salas por tipo
COLOR_SALAS = '#fda4af'
EDGE_SALAS = '#9f1239'


def generar():
    fig, ax = plt.subplots(figsize=(22, 12))
    fig.patch.set_facecolor('#f8fafc')
    ax.set_facecolor('#f1f5f9')

    ax.add_patch(Rectangle((X_MIN, Y_MIN), X_MAX - X_MIN, Y_MAX - Y_MIN,
                           facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.5, zorder=2))

    # COCHERAS S1: layout S3 filtrando las que caen dentro de salas técnicas o la rampa única
    def en_rampa(s):
        r = RAMPA_S1
        return not (s['x0'] + s['w'] <= r['x0'] or s['x0'] >= r['x1'] or
                    s['y0'] + s['h'] <= r['y0'] or s['y0'] >= r['y1'])

    stalls_s1 = [s for s in ga.STALLS_MANUALES
                 if not any(solapa(s, sal) for sal in SALAS_TECNICAS) and not en_rampa(s)]
    total_autos = 0
    total_motos = 0
    for s in stalls_s1:
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

    # SALAS TÉCNICAS
    for sal in SALAS_TECNICAS:
        ax.add_patch(Rectangle((sal['x0'], sal['y0']),
                               sal['x1'] - sal['x0'], sal['y1'] - sal['y0'],
                               facecolor=COLOR_SALAS, edgecolor=EDGE_SALAS,
                               hatch='++', alpha=0.75, lw=1.5, zorder=5))
        ax.text((sal['x0'] + sal['x1']) / 2, (sal['y0'] + sal['y1']) / 2,
                sal['nombre'], fontsize=7, fontweight='bold',
                color='#7f1d1d', ha='center', va='center', zorder=6)

    # PILARES ESTRUCTURALES H°A° (90×90, continuos)
    pilares, n_pilares = ga.generar_pilares()
    for (x0, y0, w, h) in pilares:
        ax.add_patch(Rectangle((x0, y0), w, h,
                               facecolor='#f8fafc', edgecolor='#0f172a', lw=1.0, zorder=6))

    # RAMPA ÚNICA S1 (esquina NE, mirando hacia el oeste)
    rampa = RAMPA_S1
    ax.add_patch(Rectangle((rampa['x0'], rampa['y0']),
                           rampa['x1'] - rampa['x0'], rampa['y1'] - rampa['y0'],
                           facecolor='#f97316', edgecolor='#c2410c', hatch='//', alpha=0.85, zorder=5))
    ax.text((rampa['x0'] + rampa['x1']) / 2, (rampa['y0'] + rampa['y1']) / 2,
            "RAMPA ÚNICA\n(6m, 2 carriles)\n→ hacia el OESTE",
            fontsize=7.5, fontweight='bold',
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

    area_salas = sum((s['x1'] - s['x0']) * (s['y1'] - s['y0']) for s in SALAS_TECNICAS)
    resumen = (
        "SUBSUELO 1 (S1) — NIVEL -3.50 m (cocheras + salas técnicas):\n"
        "────────────────────────────────────────────────\n"
        f"• PLAZAS DE ESTACIONAMIENTO: {total_stalls} TOTAL ({total_autos} autos + {total_motos} motos)\n"
        "• Layout S3 filtrado por salas técnicas y rampa única\n"
        f"• SALAS TÉCNICAS ({area_salas:.0f} m² bruto):\n"
        "   • BLOQUE TÉCNICO CENTRAL (X:34→56 / Y:26→40):\n"
        "     cisternas + bombas | grupo electrógeno + tableros | taller | PTE\n"
        "   • EBAR cloacal aislado en esquina SE (X:81.5→87.5 / Y:3→10)\n"
        f"• PILARES H°A° en grilla (90x90 cm, continuos S3→Azotea): {n_pilares}\n"
        "• 2 Núcleos H°A° gemelos rotados: N1 X:34→41 / N2 X:49→56 (Y:17→26)\n"
        "• RAMPA ÚNICA esquina NE (X:81.5→87.5 / Y:33→40, 6m, 2 carriles) mirando al OESTE\n"
        "• Altura de entrepiso: 3.50 m | Cota -3.50 m\n"
        "• El subsuelo NO desagota por gravedad → EBAR + PTE obligatorios"
    )
    ax.text(X_MIN, Y_MIN - 5.5, resumen, fontsize=8.5, fontweight='bold', va='top',
            bbox=dict(boxstyle='round,pad=0.6', facecolor='white', edgecolor='#0284c7', lw=1.5), zorder=20)

    ax.set_xlim(X_MIN - 7, X_MAX + 4)
    ax.set_ylim(Y_MIN - 14, Y_MAX + 3)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title(f"SUBSUELO 1 (S1) — COCHERAS + SALAS TÉCNICAS — {total_stalls} PLAZAS / {n_pilares} PILARES (90x90)",
              fontsize=13, fontweight='bold')

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "planta_subsuelo_1.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Plazas de estacionamiento S1: {total_stalls} ({total_autos} autos + {total_motos} motos)")
    print(f"Generado: {out_path}")
    return total_stalls


if __name__ == "__main__":
    generar()
