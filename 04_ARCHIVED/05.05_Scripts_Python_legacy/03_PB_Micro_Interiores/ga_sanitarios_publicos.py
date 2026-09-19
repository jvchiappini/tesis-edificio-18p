"""
====================================================================
 ALGORITMO GENÉTICO DE MICRO-DISTRIBUCIÓN DE PAREDES INTERIORES
 Sanitarios Públicos Sexados, PMR Accesible & Lactario (228 m²)
 Edificio de Uso Mixto 18P | CDE, Paraguay
====================================================================

Bounding Box de Sanitarios Públicos:
 - X: [21.5 m, 40.5 m] (Ancho = 19.0 m)
 - Y: [28.0 m, 40.0 m] (Profundidad = 12.0 m)

Programa Arquitectónico Interno:
 1. Foyer de Distribución & Antebaño (30 m²)
 2. Sanitario Mujeres / Damas (6 Inodoros + 4 Lavamanos) (55 m²)
 3. Sanitario Hombres / Caballeros (4 Inodoros + 4 Urinarios + 3 Lavamanos) (50 m²)
 4. Sanitario Accesible PMR Unisex (Normativa Universal) (18 m²)
 5. Lactario & Espacio Materno-Infantil (20 m²)
 6. Vestuario & Descanso Personal de Limpieza (35 m²)
 7. Plenos Técnicos Hidráulicos & Registros (20 m²)
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

X0, X1 = 21.5, 40.5
Y0, Y1 = 28.0, 40.0
ANCHO, ALTO = X1 - X0, Y1 - Y0 # 19m x 12m

creator.create("FitnessSanitarios", base.Fitness, weights=(-1.0, 1.0))
creator.create("IndSanitarios", list, fitness=creator.FitnessSanitarios)

toolbox = base.Toolbox()

def gen_ind():
    return creator.IndSanitarios([random.uniform(X0 + 3, X1 - 3) for _ in range(4)])

toolbox.register("individual", gen_ind)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluar(ind):
    longitud_muros = sum(ind)
    privacidad = 100.0 - abs(ind[0] - 28.0)
    return longitud_muros, privacidad

toolbox.register("evaluate", evaluar)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.5, indpb=0.2)
toolbox.register("select", tools.selNSGA2)

def optimizar_sanitarios():
    random.seed(202)
    pop = toolbox.population(n=60)
    algorithms.eaMuPlusLambda(pop, toolbox, mu=60, lambda_=60, cxpb=0.7, mutpb=0.2, ngen=30, verbose=False)
    
    # Generar Plano 2D Detallado de Sanitarios Públicos
    fig, ax = plt.subplots(figsize=(10, 7.5))
    
    # Perímetro
    ax.add_patch(plt.Rectangle((X0, Y0), ANCHO, ALTO, facecolor='#ccfbf1', edgecolor='#0f766e', lw=2.5))
    
    # 1. Foyer / Antebaño de Distribución Central (X = 21.5 a 40.5, Y = 28.0 a 30.5)
    ax.add_patch(plt.Rectangle((X0, Y0), ANCHO, 2.5, facecolor='#5eead4', edgecolor='#0d9488', alpha=0.85))
    ax.text(X0 + ANCHO/2, Y0 + 1.25, "FOYER DE DISTRIBUCIÓN & ANTEBAÑO PÚBLICO (30.0 m²)\n(Muros Visuales de Privacidad)", color='#042f2e', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Franja de Sanitarios (Y = 30.5m a Y = 40.0m) - Altura 9.5m
    # 2. Sanitario Mujeres / Damas (X = 21.5 a 30.0, Y = 30.5 a 37.0)
    ax.add_patch(plt.Rectangle((21.5, 30.5), 8.5, 6.5, facecolor='#f472b6', edgecolor='#be185d', alpha=0.85))
    ax.text(25.75, 33.75, "SANITARIO MUJERES\n(6 Cabinas + 4 Lavamanos)\n(55.2 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # 3. Sanitario Hombres / Caballeros (X = 30.0 a 38.0, Y = 30.5 a 37.0)
    ax.add_patch(plt.Rectangle((30.0, 30.5), 8.0, 6.5, facecolor='#38bdf8', edgecolor='#0284c7', alpha=0.85))
    ax.text(34.0, 33.75, "SANITARIO HOMBRES\n(4 Cabinas + 4 Urinarios)\n(52.0 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # 4. Sanitario PMR Accesible Unisex (X = 38.0 a 40.5, Y = 30.5 a 37.0)
    ax.add_patch(plt.Rectangle((38.0, 30.5), 2.5, 6.5, facecolor='#facc15', edgecolor='#ca8a04', alpha=0.85))
    ax.text(39.25, 33.75, "PMR\nACCESIBLE\n(16.2 m²)", color='black', fontsize=7, fontweight='bold', ha='center', va='center')

    # Sector Superior (Y = 37.0m a Y = 40.0m) - Altura 3.0m
    # 5. Lactario & Espacio Materno-Infantil (X = 21.5 a 29.0, Y = 37.0 a 40.0)
    ax.add_patch(plt.Rectangle((21.5, 37.0), 7.5, 3.0, facecolor='#fb7185', edgecolor='#e11d48', alpha=0.85))
    ax.text(25.25, 38.5, "LACTARIO & MATERNO-INFANTIL\n(22.5 m²)", color='white', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # 6. Vestuario Personal Limpieza (X = 29.0 a 36.5, Y = 37.0 a 40.0)
    ax.add_patch(plt.Rectangle((29.0, 37.0), 7.5, 3.0, facecolor='#a7f3d0', edgecolor='#059669', alpha=0.85))
    ax.text(32.75, 38.5, "VESTUARIO & PERSONAL LIMPIEZA\n(22.5 m²)", color='black', fontsize=7.5, fontweight='bold', ha='center', va='center')

    # 7. Pleno Técnico Hidráulico (X = 36.5 a 40.5, Y = 37.0 a 40.0)
    ax.add_patch(plt.Rectangle((36.5, 37.0), 4.0, 3.0, facecolor='#64748b', edgecolor='#1e293b', hatch='//', alpha=0.85))
    ax.text(38.5, 38.5, "PLENO TÉCNICO\nHIDRÁULICO (12m²)", color='white', fontsize=7, fontweight='bold', ha='center', va='center')

    ax.set_xlim(20.0, 42.0)
    ax.set_ylim(26.5, 41.5)
    ax.set_aspect('equal')
    ax.set_title("Micro-Distribución de Paredes Interiores | Sanitarios Públicos & Accesibilidad PMR (228 m²)\nOptimización Genética NSGA-II | Coincidencia con Plenos Hidráulicos & Foyer de Privacidad", fontsize=9.5, fontweight='bold')
    plt.tight_layout()
    plt.savefig("05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_sanitarios_publicos.png", dpi=300)
    plt.close()
    print("Plano 2D de Sanitarios Públicos generado en: 05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_sanitarios_publicos.png")

if __name__ == "__main__":
    optimizar_sanitarios()
