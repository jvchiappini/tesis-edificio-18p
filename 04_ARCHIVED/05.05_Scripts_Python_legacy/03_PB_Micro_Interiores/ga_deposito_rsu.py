"""
====================================================================
 ALGORITMO GENÉTICO DE MICRO-DISTRIBUCIÓN DE PAREDES INTERIORES
 Depósito RSU & Compactación Central (228 m²)
 Edificio de Uso Mixto 18P | CDE, Paraguay
====================================================================

Bounding Box del Sector:
 - X: [2.5 m, 21.5 m]  (Ancho = 19.0 m)
 - Y: [28.0 m, 40.0 m] (Profundidad = 12.0 m)

Contexto del Sistema RSU (Opción C — Pleno Técnico Horizontal):
 El ducto vertical RSU baja desde Pisos 1–16 hasta PB en el Núcleo H°A°
 (pos. 41.5, 24.8). Desde allí, un ducto horizontal Ø500mm recorre:
   T1: 9m vertical (Y:25→34) por el Pasillo Técnico de Servicios.
   T2: ~29m horizontal (X:41.5→12.0) bajo cielorraso suspendido (pleno ≥ 0.80m).
 El punto de descarga es (12.0, 34.0) — Tolva Inox al interior de este depósito.

Programa Arquitectónico Interno:
 1. Zona de Recepción de RSU por Tolva (área de caída + zona de seguridad)    ~30 m²
 2. Compactador Hidráulico Estacionario (mach. + área de maniobra)            ~45 m²
 3. Cámaras Contenedoras Diferenciadas: Reciclables / Orgánicos / Generales   ~80 m²
 4. Cuarto de Lavado y Desinfección de Contenedores (piso dren + duchas)      ~25 m²
 5. Vestuario & Sanitario Personal Operativo (2 personas mínimo)              ~18 m²
 6. Acceso Vehicular — Portón de Carga Lateral (vereda lateral X=2.5m)        ~30 m²

Criterios de Optimización Multiobjetivo (NSGA-II):
 - Minimizar distancia entre punto de descarga de Tolva y Zona Compactador.
 - Maximizar separación entre vestuario/sanitario y zona de contenedores
   (higiene y seguridad operativa).
 - Minimizar cruces de circulación entre flujo de RSU y personal operativo.

Accesos:
 - Portón vehicular en VEREDA LATERAL IZQUIERDA (X=1.5m, Y=31→37): camiones recolectores.
 - Acceso peatonal de personal desde corredor de administración (Y=28m).
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from deap import base, creator, tools, algorithms

# ------------------------------------------------------------------
# Dimensiones del Sector RSU
# ------------------------------------------------------------------
X0, X1 = 2.5, 21.5
Y0, Y1 = 28.0, 40.0
ANCHO, ALTO = X1 - X0, Y1 - Y0  # 19m × 12m

# Punto de descarga de la tolva (fijo, definido por el sistema RSU)
X_TOLVA, Y_TOLVA = 12.0, 34.0

# ------------------------------------------------------------------
# Configuración DEAP — NSGA-II
# ------------------------------------------------------------------
creator.create("FitnessRSU", base.Fitness, weights=(-1.0, -1.0, 1.0))
creator.create("IndRSU", list, fitness=creator.FitnessRSU)

toolbox = base.Toolbox()

def gen_ind():
    """Genotipo: posición X del muro divisorio principal (compactador | contenedores)."""
    x_div_compactador = random.uniform(X0 + 5.0, X0 + 7.0)   # M1: separa tolva/compactador (~6m desde X0)
    x_div_lavado = random.uniform(X0 + 12.0, X0 + 15.0)       # M2: separa contenedores de lavado/vestuarios
    y_div_vestuario = random.uniform(Y0 + 4.0, Y0 + 7.0)      # MH: muro horizontal zona norte/sur
    return creator.IndRSU([x_div_compactador, x_div_lavado, y_div_vestuario])

toolbox.register("individual", gen_ind)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluar(ind):
    x_comp, x_lav, y_vest = ind

    # Penalizar si los muros se solapan o están muy juntos
    penalizacion = 0.0
    if x_lav - x_comp < 6.0:
        penalizacion += 100.0
    if x_comp < X0 + 4.0 or x_lav > X1 - 1.5:
        penalizacion += 100.0

    # Obj 1: Minimizar distancia de la tolva al compactador (centroide de zona compactador)
    x_centro_comp = (X0 + x_comp) / 2.0
    dist_tolva_comp = abs(X_TOLVA - x_centro_comp) + abs(Y_TOLVA - (Y0 + ALTO / 2))

    # Obj 2: Minimizar cruces (la zona de lavado debe estar lejos del acceso vehicular)
    dist_cruce = abs(x_lav - X1)  # queremos lavado cerca del fondo (X1)

    # Obj 3: Maximizar higiene — separación entre vestuario y contenedores
    sep_higiene = abs(y_vest - Y0) * abs(x_lav - x_comp)

    return dist_tolva_comp + penalizacion, dist_cruce + penalizacion, sep_higiene

toolbox.register("evaluate", evaluar)
toolbox.register("mate", tools.cxBlend, alpha=0.4)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.5, indpb=0.3)
toolbox.register("select", tools.selNSGA2)

# ------------------------------------------------------------------
# Función Principal de Optimización y Generación de Plano 2D
# ------------------------------------------------------------------
def optimizar_rsu():
    random.seed(404)
    pop = toolbox.population(n=80)
    algorithms.eaMuPlusLambda(
        pop, toolbox, mu=80, lambda_=80,
        cxpb=0.7, mutpb=0.25, ngen=40, verbose=False
    )

    # Seleccionar mejor individuo del frente Pareto
    pareto_front = tools.sortNondominated(pop, len(pop), first_front_only=True)[0]
    mejor = min(pareto_front, key=lambda ind: ind.fitness.values[0] + ind.fitness.values[1])
    x_comp, x_lav, y_vest = mejor[0], mejor[1], mejor[2]

    print(f"[RSU GA] Muro 1 (Tolva/Compactador|Contenedores): X = {x_comp:.2f}m")
    print(f"[RSU GA] Muro 2 (Contenedores|Lavado+Vestuarios): X = {x_lav:.2f}m")
    print(f"[RSU GA] Muro horizontal (Zona Norte/Sur):         Y = {y_vest:.2f}m")

    # ------------------------------------------------------------------
    # Generación del Plano 2D
    # ------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 8))

    # Contorno exterior del sector
    ax.add_patch(plt.Rectangle((X0, Y0), ANCHO, ALTO,
                                facecolor='#dcfce7', edgecolor='#14532d', lw=2.5))

    # --- ZONA 1: Recepción Tolva + Compactador (X: 2.5 → x_comp) ---
    ax.add_patch(plt.Rectangle((X0, Y0), x_comp - X0, ALTO,
                                facecolor='#4ade80', edgecolor='#15803d', alpha=0.85))
    ax.text((X0 + x_comp) / 2, Y0 + ALTO / 2,
            f"ZONA TOLVA RSU\n& COMPACTADOR\nHIDRÁULICO\n({(x_comp - X0) * ALTO:.0f} m²)",
            color='#052e16', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # Punto de descarga de la tolva (viene desde el pleno técnico horizontal)
    ax.scatter(X_TOLVA, Y_TOLVA, color='#facc15', s=300, zorder=8,
               edgecolor='#14532d', lw=2.0, marker='v')
    ax.annotate("DESCARGA TOLVA\nInox RSU (Pleno T2)",
                (X_TOLVA, Y_TOLVA), xytext=(X_TOLVA + 1.5, Y_TOLVA + 1.5),
                arrowprops=dict(arrowstyle='->', color='#14532d', lw=1.2),
                fontsize=6.5, fontweight='bold', color='#14532d',
                bbox=dict(boxstyle='round,pad=0.2', fc='#fef9c3', ec='#ca8a04', lw=0.8),
                zorder=9)

    # --- ZONA 2: Cámaras de Contenedores Diferenciados (x_comp → x_lav) ---
    ancho_cont = x_lav - x_comp
    # Sub-zona norte: Reciclables (Y: y_vest → 40)
    ax.add_patch(plt.Rectangle((x_comp, y_vest), ancho_cont, Y1 - y_vest,
                                facecolor='#86efac', edgecolor='#15803d', alpha=0.85))
    ax.text((x_comp + x_lav) / 2, (y_vest + Y1) / 2,
            f"RECICLABLES\n({ancho_cont * (Y1 - y_vest):.0f} m²)",
            color='#052e16', fontsize=7, fontweight='bold', ha='center', va='center')

    # Sub-zona sur: Organicos + Generales (Y: 28 → y_vest)
    ax.add_patch(plt.Rectangle((x_comp, Y0), ancho_cont, y_vest - Y0,
                                facecolor='#bbf7d0', edgecolor='#15803d', alpha=0.85))
    ax.text((x_comp + x_lav) / 2, (Y0 + y_vest) / 2,
            f"ORGÁNICOS\n+ GENERALES\n({ancho_cont * (y_vest - Y0):.0f} m²)",
            color='#052e16', fontsize=7, fontweight='bold', ha='center', va='center')

    # --- ZONA 3: Lavado + Vestuario/Sanitario (x_lav → 21.5) ---
    ancho_serv = X1 - x_lav
    # Cuarto de Lavado (Y: y_vest → 40)
    ax.add_patch(plt.Rectangle((x_lav, y_vest), ancho_serv, Y1 - y_vest,
                                facecolor='#38bdf8', edgecolor='#0284c7', alpha=0.85))
    ax.text((x_lav + X1) / 2, (y_vest + Y1) / 2,
            f"LAVADO &\nDESINFECCIÓN\n({ancho_serv * (Y1 - y_vest):.0f} m²)",
            color='white', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # Vestuario + Sanitario Personal (Y: 28 → y_vest)
    ax.add_patch(plt.Rectangle((x_lav, Y0), ancho_serv, y_vest - Y0,
                                facecolor='#fbbf24', edgecolor='#b45309', alpha=0.85))
    ax.text((x_lav + X1) / 2, (Y0 + y_vest) / 2,
            f"VESTUARIO &\nSANIT. PERSONAL\n({ancho_serv * (y_vest - Y0):.0f} m²)",
            color='#451a03', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # --- Muros divisorios (líneas verticales y horizontal del GA) ---
    ax.plot([x_comp, x_comp], [Y0, Y1], color='#052e16', lw=2.0, ls='-', zorder=5)
    ax.plot([x_lav, x_lav],   [Y0, Y1], color='#052e16', lw=2.0, ls='-', zorder=5)
    ax.plot([x_comp, X1],     [y_vest, y_vest], color='#052e16', lw=1.5, ls='--', zorder=5)

    # Anotaciones de muros
    ax.text(x_comp, Y0 - 0.4, f"M1\nX={x_comp:.1f}m", color='#052e16',
            fontsize=6, ha='center', fontweight='bold')
    ax.text(x_lav,  Y0 - 0.4, f"M2\nX={x_lav:.1f}m",  color='#052e16',
            fontsize=6, ha='center', fontweight='bold')
    ax.text(X0 - 0.6, y_vest, f"MH\nY={y_vest:.1f}m", color='#052e16',
            fontsize=6, va='center', fontweight='bold')

    # --- Portón vehicular lateral izquierdo ---
    ax.add_patch(plt.Rectangle((1.5, 31.0), 1.0, 6.0,
                                facecolor='#f59e0b', edgecolor='#b45309', zorder=8, lw=1.5))
    ax.text(0.5, 34.0, "PORTÓN\nCARGA\nRSU", color='black', fontsize=6,
            fontweight='bold', ha='center', va='center', rotation=90)

    # --- Acceso peatonal personal (Y=28 desde Admin) ---
    ax.annotate("", xy=(X0 + 2.0, Y0), xytext=(X0 + 2.0, Y0 - 0.8),
                arrowprops=dict(arrowstyle='->', color='#1d4ed8', lw=1.5))
    ax.text(X0 + 2.0, Y0 - 1.2, "Acceso personal\n(desde Admin)",
            color='#1d4ed8', fontsize=5.5, ha='center')

    # --- Etiqueta de área total ---
    ax.text(X0 + ANCHO / 2, Y1 + 0.5,
            f"ÁREA TOTAL DEL SECTOR: {ANCHO * ALTO:.0f} m²  |  Bounding Box: X[{X0}→{X1}] / Y[{Y0}→{Y1}]",
            color='#052e16', fontsize=7, fontweight='bold', ha='center')

    # Formato del plano
    ax.set_xlim(0.0, 24.0)
    ax.set_ylim(26.0, 41.5)
    ax.set_aspect('equal')
    ax.set_xlabel("Coordenada X [m]", fontsize=8)
    ax.set_ylabel("Coordenada Y [m]", fontsize=8)
    ax.grid(True, linestyle=':', alpha=0.4, color='#6b7280')
    ax.set_title(
        "Micro-Distribución de Paredes Interiores | Depósito RSU & Compactación Central (228 m²)\n"
        "Optimización Genética NSGA-II | Sistema de Pleno Técnico Horizontal (Opción C) | CDE, Paraguay",
        fontsize=9.5, fontweight='bold'
    )
    plt.tight_layout()
    plt.savefig(
        "05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_deposito_rsu.png",
        dpi=300
    )
    plt.close()
    print("Plano 2D de Depósito RSU generado en: "
          "05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_deposito_rsu.png")


if __name__ == "__main__":
    optimizar_rsu()
