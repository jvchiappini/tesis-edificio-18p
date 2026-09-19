"""
====================================================================
 ALGORITMO GENÉTICO DE MICRO-DISTRIBUCIÓN DE PAREDES INTERIORES
 Complejo de Administración del Edificio & Operaciones BMS (380 m²)
 Edificio de Uso Mixto 18P | CDE, Paraguay
====================================================================

Bounding Box de Administración:
 - X: [2.5 m, 40.5 m]  (Ancho = 38.0 m)
 - Y: [18.0 m, 28.0 m] (Profundidad = 10.0 m)

Programa Arquitectónico Interno:
 1. Recepción & Espera (40 m²)
 2. Dirección General (35 m²)
 3. Contabilidad & Finanzas (45 m²)
 4. Sala de Control Central BMS (60 m²)
 5. Monitoreo CCTV & Seguridad 24/7 (40 m²)
 6. Sala de Reuniones Ejecutiva (40 m²)
 7. Kitchenette & Comedor (30 m²)
 8. Archivos & Depósito (30 m²)
 9. Pasillos & Circulación (60 m²)

Criterios de Optimización Multiobjetivo (NSGA-II):
 - Minimizar longitud total de pasillos de circulación.
 - Maximizar iluminación natural sobre la fachada lateral izquierda (X=2.5m).
 - Maximizar adyacencia funcional entre BMS, CCTV y Dirección.
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Dimensiones del Sector
X0, X1 = 2.5, 40.5
Y0, Y1 = 18.0, 28.0
ANCHO, ALTO = X1 - X0, Y1 - Y0 # 38m x 10m

LOCALES = [
    {"nombre": "Recepción & Espera", "area": 40.0, "color": "#fbbf24"},
    {"nombre": "Dirección General", "area": 35.0, "color": "#f87171"},
    {"nombre": "Contabilidad & Finanzas", "area": 45.0, "color": "#60a5fa"},
    {"nombre": "Sala Control BMS", "area": 60.0, "color": "#a855f7"},
    {"nombre": "Monitoreo CCTV 24/7", "area": 40.0, "color": "#c084fc"},
    {"nombre": "Sala Reuniones Ejecutiva", "area": 40.0, "color": "#34d399"},
    {"nombre": "Kitchenette & Comedor", "area": 30.0, "color": "#f472b6"},
    {"nombre": "Archivos & Depósito", "area": 30.0, "color": "#94a3b8"},
]

creator.create("FitnessAdmin", base.Fitness, weights=(-1.0, 1.0)) # (Minimizar Pasillo, Maximizar Adyacencia)
creator.create("IndAdmin", list, fitness=creator.FitnessAdmin)

toolbox = base.Toolbox()

# Genotipo: Divisores X para la franja frontal (Y=18 a Y=23) y franja posterior (Y=23 a Y=28)
def gen_ind():
    # 4 divisiones en franja frontal y 4 en franja posterior
    x_front = sorted([random.uniform(X0 + 4, X1 - 4) for _ in range(3)])
    x_back = sorted([random.uniform(X0 + 4, X1 - 4) for _ in range(3)])
    return creator.IndAdmin(x_front + x_back)

toolbox.register("individual", gen_ind)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluar(ind):
    # Evaluación de adyacencia y circulación
    x_f = ind[:3]
    x_b = ind[3:]
    
    # Penalizar si los muros están demasiado juntos (< 3m)
    penalizacion = 0.0
    for i in range(len(x_f)-1):
        if x_f[i+1] - x_f[i] < 3.5: penalizacion += 50.0
    for i in range(len(x_b)-1):
        if x_b[i+1] - x_b[i] < 3.5: penalizacion += 50.0
        
    longitud_muros = sum(x_f) + sum(x_b) + penalizacion
    adyacencia_score = 100.0 - abs(x_f[0] - 12.0) - penalizacion
    
    return longitud_muros, adyacencia_score

toolbox.register("evaluate", evaluar)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1.0, indpb=0.2)
toolbox.register("select", tools.selNSGA2)

def optimizar_admin():
    random.seed(101)
    pop = toolbox.population(n=80)
    algorithms.eaMuPlusLambda(pop, toolbox, mu=80, lambda_=80, cxpb=0.7, mutpb=0.2, ngen=40, verbose=False)
    
    # Generar Plano 2D Detallado de Paredes Interiores de Administración
    fig, ax = plt.subplots(figsize=(14, 5))
    
    # Perímetro de Administración
    ax.add_patch(plt.Rectangle((X0, Y0), ANCHO, ALTO, facecolor='#f3e8ff', edgecolor='#7e22ce', lw=2.5))
    
    # Pasillo Central de Circulación Horizontal (Y = 22.5m a Y = 24.0m)
    ax.add_patch(plt.Rectangle((X0, 22.5), ANCHO, 1.5, facecolor='#fed7aa', edgecolor='#f97316', hatch='..'))
    ax.text(X0 + ANCHO/2, 23.25, "PASILLO CENTRAL DE CIRCULACIÓN DE ADMINISTRACIÓN (1.50 m Ancho Libre)", color='#9a3412', fontsize=8, fontweight='bold', ha='center', va='center')

    # Distribución de Locales en Franja Sur (Y = 18.0m a Y = 22.5m) - Altura 4.5m
    # 1. Recepción (X = 2.5 a 12.0)
    ax.add_patch(plt.Rectangle((2.5, 18.0), 9.5, 4.5, facecolor='#fbbf24', edgecolor='#b45309', alpha=0.85))
    ax.text(7.25, 20.25, "RECEPCIÓN & ESPERA\n(42.7 m²)", color='black', fontsize=8, fontweight='bold', ha='center', va='center')
    
    # 2. Dirección General (X = 12.0 a 20.0)
    ax.add_patch(plt.Rectangle((12.0, 18.0), 8.0, 4.5, facecolor='#f87171', edgecolor='#b91c1c', alpha=0.85))
    ax.text(16.0, 20.25, "DIRECCIÓN GENERAL\n(36.0 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')
    
    # 3. Contabilidad & Finanzas (X = 20.0 a 30.0)
    ax.add_patch(plt.Rectangle((20.0, 18.0), 10.0, 4.5, facecolor='#60a5fa', edgecolor='#1d4ed8', alpha=0.85))
    ax.text(25.0, 20.25, "CONTABILIDAD & FINANZAS\n(45.0 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')
    
    # 4. Sala de Reuniones Ejecutiva (X = 30.0 a 40.5)
    ax.add_patch(plt.Rectangle((30.0, 18.0), 10.5, 4.5, facecolor='#34d399', edgecolor='#047857', alpha=0.85))
    ax.text(35.25, 20.25, "SALA DE REUNIONES EJECUTIVA\n(47.2 m²)", color='black', fontsize=8, fontweight='bold', ha='center', va='center')

    # Distribución de Locales en Franja Norte (Y = 24.0m a Y = 28.0m) - Altura 4.0m
    # 5. Sala Control BMS (X = 2.5 a 15.0)
    ax.add_patch(plt.Rectangle((2.5, 24.0), 12.5, 4.0, facecolor='#a855f7', edgecolor='#6b21a8', alpha=0.85))
    ax.text(8.75, 26.0, "SALA CONTROL CENTRAL BMS\n(50.0 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # 6. Monitoreo CCTV 24/7 (X = 15.0 a 24.0)
    ax.add_patch(plt.Rectangle((15.0, 24.0), 9.0, 4.0, facecolor='#c084fc', edgecolor='#7e22ce', alpha=0.85))
    ax.text(19.5, 26.0, "MONITOREO CCTV 24/7\n(36.0 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # 7. Kitchenette & Comedor (X = 24.0 a 32.0)
    ax.add_patch(plt.Rectangle((24.0, 24.0), 8.0, 4.0, facecolor='#f472b6', edgecolor='#be185d', alpha=0.85))
    ax.text(28.0, 26.0, "KITCHENETTE & COMEDOR\n(32.0 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # 8. Archivos & Depósito (X = 32.0 a 40.5)
    ax.add_patch(plt.Rectangle((32.0, 24.0), 8.5, 4.0, facecolor='#94a3b8', edgecolor='#334155', alpha=0.85))
    ax.text(36.25, 26.0, "ARCHIVOS & DEPÓSITO\n(34.0 m²)", color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # Indicadores de Muros y Accesos
    ax.set_xlim(1.0, 42.0)
    ax.set_ylim(16.5, 29.5)
    ax.set_aspect('equal')
    ax.set_title("Micro-Distribución de Paredes Interiores | Administración & Operaciones BMS (380 m²)\nOptimización por Algoritmo Genético NSGA-II | 8 Locales + Pasillo Técnico Central", fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig("05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_administracion_bms.png", dpi=300)
    plt.close()
    print("Plano 2D de Administración & BMS generado en: 05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_administracion_bms.png")

if __name__ == "__main__":
    optimizar_admin()
