# Catálogo de Aplicaciones Algorítmicas de la Tesis

> Memoria de decisiones. Aquí se registran las ideas de uso de algoritmos evaluadas para la tesis,
> para no volver a analizarlas desde cero. Última actualización: 2026-09-15.
>
> Regla: la tesis mantiene el foco en **viento + estructura + BIM + optimización espacial**. No se
> agregan algoritmos que diluyan ese foco.

## 1. Estado actual (lo ya definido)

| Uso | Herramienta | Estado |
|---|---|---|
| Macro distribuciones (PB, planta tipo, azotea) | Scripts paramétricos (dibujo determinista) | ✅ hecho |
| Subsuelos (cocheras) | Manual | ✅ hecho |
| Grilla de pilares | Diseño directo alineado a los núcleos (sin AG) | ✅ hecho |
| Micro-distribuciones de PB (admin/BMS, sanitarios, centro de negocios, RSU) | NSGA-II (DEAP) | ✅ hecho |
| **Micro-distribución de departamentos** | **NSGA-II + simulación de circulación** | ⏳ a desarrollar |

## 2. Ideas evaluadas (ordenadas por encaje con la tesis)

### 2.1 Muy alineadas — recomendadas

1. **Optimización de la forma del edificio frente al viento (aerodinámica).**
   - Genotipo: parámetros de forma (achaflanados de esquina, escalonamientos/setbacks, reducción en altura, orientación).
   - Objetivos: minimizar cortante basal, momento de vuelco, deriva y aceleraciones de confort, sin perder superficie útil.
   - Herramienta: NSGA-II (DEAP) + módulo de viento (NP 196 / NBR 6123 / ASCE 7-22 / EC1).
   - Aporte: es el capítulo de ingeniería de viento más original. **Recomendado.**
   - Encaje: Cap. 6 (Viento).

2. **Micro-distribución de departamentos con simulación de circulación.**
   - Ver especificación dedicada: `NSGA2_Microdistribucion_Departamentos_v01.md`.
   - Encaje: Cap. 4 (Descripción) + Cap. 5 (Optimización). **Recomendado.**

3. **Optimización de secciones de pilares y canto de losa.**
   - Genotipo: sección por grupo de niveles + canto de losa nervada.
   - Objetivos: minimizar costo / hormigón / CO₂, sujeto a derivas (NBR 6118) y flechas (ELS).
   - Encaje: Cap. 5 y Cap. 7.

### 2.2 Válidas — secundarias

4. **Distribución de cocheras (empaquetado).** Maximizar plazas respetando rampas, pilares y pasillos de 6 m. GA o empaquetado geométrico. (Hoy manual; podría automatizarse como anexo.)
5. **Optimización de la fachada.** Sombreamiento + apertura de vanos para confort térmico y luz natural (clima cálido y húmedo de CDE).
6. **Multiobjetivo costo vs. huella de carbono** de la estructura.
7. **Nivelación de recursos del cronograma (4D)** por algoritmo genético.

### 2.3 Complementarias (simulación, no optimización)

8. **Simulación de evacuación** de las escaleras de emergencia (modelo basado en agentes) → tiempos de salida. Coherente con PCI en edificio alto.
9. **Análisis de circulaciones "space syntax"** (integración y conectividad) para validar las plantas.

## 3. Decisión de alcance

Para no diluir la tesis, se priorizan **dos** usos nuevos:
- **(2.1.1) Forma del edificio frente al viento.**
- **(2.1.2) Micro-distribución de departamentos con circulación.**

El resto queda como **trabajos futuros** (Cap. 10).

## 4. Herramientas libres disponibles

| Necesidad | Biblioteca |
|---|---|
| NSGA-II | `deap` (Python) |
| Geometría | `shapely` |
| Caminos/grafos | `networkx` |
| Agentes (evacuación/circulación) | `mesa` |
| Figuras | `matplotlib` |
| Export a Revit/Dynamo | JSON/CSV |
