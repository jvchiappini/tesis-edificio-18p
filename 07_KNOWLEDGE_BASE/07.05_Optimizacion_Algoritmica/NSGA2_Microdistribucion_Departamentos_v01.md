# Especificación — NSGA-II para Micro-distribución de Departamentos

> Base para el futuro generador de planos de departamentos con distribución óptima.
> Carpeta de trabajo: `05_RECURSOS/05.05_Scripts_Python/08_Departamentos_NSGA2/`
> Última actualización: 2026-09-15. Estado: **especificación (sin código todavía)**.

---

## 1. Objetivo

Generar automáticamente la distribución interior de los departamentos (tabiques y puertas) de modo que
cumplan **todas las reglas lógicas de arquitectura** y, al mismo tiempo, optimicen varios objetivos
(recorridos peatonales, luz natural, ventilación, área útil) mediante el algoritmo **NSGA-II**.

Resultado esperado: una familia de planos válidos (frente de Pareto) de la cual se elige el mejor y se
refina a mano, para luego **exportar a Revit/Dynamo** y usarlo como plano definitivo.

---

## 2. Entradas fijas (DATOS que el algoritmo NO mueve)

El generador recibe estas condiciones y no las modifica:

| Entrada | Descripción |
|---|---|
| **Puerta de entrada del departamento** | **SIEMPRE FIJA.** Es el dato de partida: la define el corredor/núcleo. Todo el layout se organiza a partir de ella. |
| Bounding box de la unidad | Ancho y profundidad del departamento (banda Sur o Norte). |
| Muros perimetrales | Fachada, muro de corredor y medianeras entre unidades. |
| Fachadas y pozo de luz / patio de servicio | Superficies por donde se puede iluminar y ventilar. |
| Grilla estructural y pilares | Los tabiques no deben tapar ni chocar con los pilares; se alinean lo posible con la grilla. |
| Shafts y ductos (RSU, ventilación, cloacal) | Zonas intocables (además, ruido: nada de dormitorios pegados ahí). |
| Orientación | Para decidir qué ambiente va a qué fachada (vistas, ruido, asoleamiento). |

---

## 3. Zonificación por zonas

Cada ambiente pertenece a una zona; las zonas ordenan la planta desde la entrada hacia adentro:

| Zona | Ambientes |
|---|---|
| **Social** (junto a la entrada) | Hall de acceso, Estar, Comedor, Toilette de visitas, Balcón |
| **Servicio** (intermedia, ventilada) | Cocina, Lavadero/Patio de servicio |
| **Privada** (al fondo, silenciosa) | Dormitorio principal (+ baño en suite), Dormitorios secundarios, Baño común |
| **Circulación** | Pasillo que conecta las zonas (se minimiza) |

Regla general: **Social → Servicio → Privada**, desde la puerta de entrada hacia el interior.

---

## 4. Genotipo (lo que el algoritmo mueve)

Opción recomendada (simple y estable): **una rejilla de 0,10 m sobre el bounding box**, y el individuo
codifica:

```
Individuo = [
  posición X/Y de cada tabique interior,
  ubicación de cada puerta (sobre el tabique correspondiente),
  ancho de cada ambiente
]
```

Alternativa (más flexible pero más difícil): polígonos libres por ambiente. **Se comienza con la rejilla**
porque hace fácil verificar solapes, dimensiones mínimas y la circulación.

---

## 5. Reglas lógicas de arquitectura (el corazón del módulo)

### 5.1 Reglas duras (si se violan, la solución se descarta)

1. **La puerta de entrada es fija** y da al Hall; desde el Hall se accede directamente al Estar/Comedor.
2. **El baño (o toilette) no puede tener la puerta enfrentada al comedor** ni a la mesa del comedor.
3. **Ningún baño abre directamente a la cocina.**
4. **La cocina no abre directamente a los dormitorios.**
5. **Los dormitorios no pueden ser de paso**: no se llega a un ambiente atravesando otro dormitorio.
6. **Todos los ambientes habitables** (estar, comedor, dormitorios, cocina) deben tener **iluminación y ventilación natural** (fachada, pozo de luz o patio de servicio).
7. **Baños y cocina deben ventilar** (ventana o ducto mecánico).
8. **Dimensiones mínimas por ambiente** (habitabilidad): superficies y anchos mínimos de dormitorios, cocina, baños y de los pasos.
9. **No hay dormitorio con pared compartida con el ducto de residuos o shafts** (ruido).
10. **La única circulación** hacia cada dormitorio y baño no puede atravesar otro dormitorio ni un baño.

### 5.2 Reglas blandas (se penalizan, orientan la optimización)

11. Minimizar circulación: evitar pasillos largos y fondos de saco.
12. **Concentrar las áreas húmedas** (cocina + baños) para acortar cañerías y acercarlas a los shafts.
13. El **estar/comedor** hacia la mejor fachada/vista; los **dormitorios** hacia la fachada más tranquila.
14. Evitar que el baño comparta pared con la cocina (higiene), si es posible.
15. Evitar que la cocina comparta pared con un dormitorio (ruidos y olores), si es posible.
16. El **balcón** se accede desde el estar/comedor (preferentemente).
17. Privacidad: la puerta del baño no debe quedar a la vista desde el acceso.
18. Los tabiques se alinean con la grilla estructural y **no dejan pilares dentro de los ambientes**.

### 5.3 Matriz de compatibilidad (resumen)

Leyenda: **P** = puerta obligatoria · **A** = adyacencia permitida · **—** = sin relación especial ·
**X** = acceso directo prohibido · **XX** = puerta enfrentada prohibida.

| | Acceso | Estar | Comedor | Cocina | Lavadero | Dorm. Princ. | Dorm. Sec. | Baño común | Toilette | Balcón | Pasillo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Acceso** | — | P | A | X | X | X | X | A | A | — | P |
| **Estar** | P | — | P | A | X | X | X | X | A | P | A |
| **Comedor** | A | P | — | A | X | X | X | **XX** | **XX** | A | A |
| **Cocina** | X | A | A | — | P | X | X | X | X | A | A |
| **Lavadero** | X | X | X | P | — | X | X | X | X | A | A |
| **Dorm. Princ.** | X | X | X | X | X | — | A | A | X | A | P |
| **Dorm. Sec.** | X | X | X | X | X | A | — | A | X | A | P |
| **Baño común** | A | X | **XX** | X | X | A | A | — | A | X | P |
| **Toilette** | A | A | **XX** | X | X | X | X | A | — | X | P |
| **Balcón** | — | P | A | A | A | A | A | X | X | — | X |
| **Pasillo** | P | A | A | A | A | P | P | P | P | X | — |

> Esta matriz es el punto de partida: debe revisarse y **validarse con el tutor/arquitecto** antes de
> programarla, y afinarse con la normativa de habitabilidad aplicable.

---

## 6. Objetivos del NSGA-II (fitness)

Se optimizan simultáneamente (todos minimizados o maximizados, según corresponda):

1. **Minimizar el recorrido peatonal total** (suma ponderada de los caminos desde la entrada hasta cada ambiente).
2. **Minimizar el área de circulación** (pasillo), ganando superficie útil.
3. **Maximizar la luz natural** (área con acceso directo a fachada/pozo).
4. **Maximizar la ventilación cruzada** (pares de vanos en caras opuestas).
5. **Minimizar las penalizaciones** por violar reglas blandas (5.2).

Restricciones duras (5.1) se aplican como **reparación o rechazo** del individuo.

---

## 7. Simulación de recorridos peatonales

1. Rasterizar la planta en una **grilla**; las celdas libres forman un **grafo** (`networkx`).
2. El **recorrido** de una persona = **camino más corto** desde la puerta de entrada hasta el centro de cada ambiente, esquivando muebles fijos (cama, mesada, mesa).
3. Métrica de circulación = suma ponderada de recorridos (el baño y la cocina pesan distinto que un dormitorio de uso esporádico).
4. **Nivel avanzado (opcional):** simulación **basada en agentes** (modelo de fuerzas sociales, biblioteca `mesa`) para obtener tiempos y detección de cuellos de botella.

---

## 8. Salidas

| Salida | Formato |
|---|---|
| Plano de la mejor distribución y de 3–5 soluciones del frente de Pareto | PNG |
| Tabla de ambientes (nombre, área, lados, ventilación/luz) | CSV |
| Métricas por solución (recorrido, área de circulación, luz, ventilación, penalizaciones) | JSON/CSV |
| Genotipo de la solución elegida (para exportar a Revit/Dynamo) | JSON |

---

## 9. Herramientas

`deap` (NSGA-II) · `shapely` (geometría) · `networkx` (recorridos) · `mesa` (agentes, opcional) ·
`matplotlib` (figuras). Exportación a Revit/Dynamo por JSON/CSV.

---

## 10. Validación

- Comparar el mejor layout contra el dibujado a mano.
- Analizar con **space syntax** (integración/conectividad) como control externo.
- Refinamiento manual final (metodología híbrida de la tesis).

---

## 11. Fases de desarrollo

| Fase | Contenido |
|---|---|
| 0 | Definir entradas de **una sola tipología** (p. ej. 1 dormitorio) y fijar la puerta de entrada. |
| 1 | Geometría base: bounding box, fachada, pozo/patio, pilares y shafts. |
| 2 | Genotipo + validación de restricciones duras. |
| 3 | Objetivos + simulación de recorridos. |
| 4 | NSGA-II y frente de Pareto. |
| 5 | Validación (space syntax + revisión manual). |
| 6 | Export a Revit/Dynamo y réplica a las tipologías B y C. |

---

## 12. Glosario de ambientes

**Acceso/Hall** · **Estar** · **Comedor** · **Cocina** · **Lavadero / Patio de servicio** ·
**Dormitorio principal** (+ baño en suite) · **Dormitorios secundarios** · **Baño común** ·
**Toilette de visitas** · **Balcón** · **Pasillo/Circulación**.
