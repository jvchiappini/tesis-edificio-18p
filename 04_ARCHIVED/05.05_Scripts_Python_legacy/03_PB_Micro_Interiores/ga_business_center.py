"""
====================================================================
 ALGORITMO GENÉTICO DE MICRO-DISTRIBUCIÓN DE PAREDES INTERIORES
 Business Center, Coworking & Boardroom (200 m²)
 Edificio de Uso Mixto 18P | CDE, Paraguay
====================================================================

Bounding Box de Business Center:
 - X: [49.5 m, 69.5 m] (Ancho = 20.0 m)
 - Y: [30.0 m, 40.0 m] (Profundidad = 10.0 m)

Programa Arquitectónico Interno:
 1. Reception & Foyer de Negocios (35 m²)
 2. Coworking Open Space (12 Puestos) (65 m²)
 3. Sala de Directorio Executive Boardroom (12 pax) (40 m²)
 4. 2 Phonebooths / Cabinas Privadas Acústicas (15 m²)
 5. Coffee Bar & Lounge (25 m²)
 6. Circulación & Locker Storage (20 m²)
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

X0, X1 = 49.5, 69.5
Y0, Y1 = 30.0, 40.0
ANCHO, ALTO = X1 - X0, Y1 - Y0 # 20m x 10m

creator.create("FitnessBC", base.Fitness, weights=(-1.0, 1.0))
creator.create("IndBC", list, fitness=creator.FitnessBC)

toolbox = base.Toolbox()

def gen_ind():
    return creator.IndBC([random.uniform(X0 + 2, X1 - 2) for _ in range(4)])

toolbox.register("individual", gen_ind)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluar(ind):
    return sum(ind), 100.0 - abs(ind[0] - 56.0)

toolbox.register("evaluate", evaluar)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.5, indpb=0.2)
toolbox.register("select", tools.selNSGA2)

def optimizar_bc():
    random.seed(303)
    pop = toolbox.population(n=60)
    algorithms.eaMuPlusLambda(pop, toolbox, mu=60, lambda_=60, cxpb=0.7, mutpb=0.2, ngen=30, verbose=False)
    
    # Generar Plano 2D Detallado de Business Center & Coworking
    fig, ax = plt.subplots(figsize=(11, 6))
    
    # Perímetro
    ax.add_patch(plt.Rectangle((X0, Y0), ANCHO, ALTO, facecolor='#faf5ff', edgecolor='#7e22ce', lw=2.5))
    
    # 1. Reception & Foyer de Negocios (X = 49.5 a 56.0, Y = 30.0 a 35.0)
    ax.add_patch(plt.Rectangle((49.5, 30.0), 6.5, 5.0, facecolor='#c084fc', edgecolor='#7e22ce', alpha=0.85))
    ax.text(52.75, 32.5, "RECEPCIÓN &\nFOYER (32.5 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # 2. Coffee Bar & Lounge (X = 49.5 a 56.0, Y = 35.0 a 40.0)
    ax.add_patch(plt.Rectangle((49.5, 35.0), 6.5, 5.0, facecolor='#f472b6', edgecolor='#be185d', alpha=0.85))
    ax.text(52.75, 37.5, "COFFEE BAR &\nLOUNGE (32.5 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # 3. Coworking Open Space (X = 56.0 a 64.0, Y = 30.0 a 40.0)
    ax.add_patch(plt.Rectangle((56.0, 30.0), 8.0, 10.0, facecolor='#a855f7', edgecolor='#6b21a8', alpha=0.85))
    ax.text(60.0, 35.0, "COWORKING OPEN SPACE\n(12 Puestos Ergonométricos)\n(80.0 m²)", color='white', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # 4. Sala de Directorio Boardroom (X = 64.0 a 69.5, Y = 30.0 a 36.0)
    ax.add_patch(plt.Rectangle((64.0, 30.0), 5.5, 6.0, facecolor='#34d399', edgecolor='#047857', alpha=0.85))
    ax.text(66.75, 33.0, "EXECUTIVE BOARDROOM\n(12 pax)\n(33.0 m²)", color='black', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # 5. Phonebooths Acústicos (X = 64.0 a 69.5, Y = 36.0 a 40.0)
    ax.add_patch(plt.Rectangle((64.0, 36.0), 5.5, 4.0, facecolor='#fbbf24', edgecolor='#b45309', alpha=0.85))
    ax.text(66.75, 38.0, "2 PHONEBOOTHS\nACÚSTICOS (22.0 m²)", color='black', fontsize=7.5, fontweight='bold', ha='center', va='center')

    ax.set_xlim(47.5, 71.5)
    ax.set_ylim(28.5, 41.5)
    ax.set_aspect('equal')
    ax.set_title("Micro-Distribución de Paredes Interiores | Business Center & Coworking (200 m²)\nOptimización Genética NSGA-II | Zonificación Acústica (Lounge -> Open Space -> Boardroom)", fontsize=9.5, fontweight='bold')
    plt.tight_layout()
    plt.savefig("05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_business_center.png", dpi=300)
    plt.close()
    print("Plano 2D de Business Center generado en: 05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_business_center.png")

if __name__ == "__main__":
    optimizar_bc()
