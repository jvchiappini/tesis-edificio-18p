# Etapa E — Ingeniería de Viento, Dinámica Estructural y Efectos de 2° Orden

> **Estado:** 🔲 Sin iniciar · **Duración estimada:** 6–8 semanas · **Prioridad:** ⭐ CRÍTICO — Núcleo de la tesis

| Campo | Valor |
|---|---|
| Normativa principal | NP 196:1991 · NBR 6123:2023 · ASCE 7-22 · EN 1991-1-4 |
| Archivos clave | `06_Estructura/calculo/calculo_viento_multinormativo.py` |
| Hito de cierre | Cortantes basales, derivas y aceleraciones calculados bajo 4 normas |
| Depende de | Etapa D (cargas gravitatorias definidas) |

> **Por qué es el núcleo:** Un edificio de 18 pisos en Ciudad del Este es totalmente sensible al viento (H≈68m, T₁>1s). La comparativa multinormativa (NP 196 + NBR 6123 + ASCE 7-22 + Eurocódigo 1) es el aporte académico diferenciador de esta tesis. No es un capítulo de relleno — es el que más páginas, más tablas y más rigor requiere.

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Tareas — E.1 Parámetros de viento

- [ ] **eE-1** · Velocidad de diseño y categoría de terreno (multinormativa)
  - V₀ = 45 m/s (velocidad básica de referencia, CDE)
  - NBR usa Vk=V₀·S₁·S₂·S₃ (1 min prom.); ASCE 7-22 usa V en ráfaga de 3 s; NP 196 usa V₁₀ en 10 min; EC1 usa Vb (10 min a 10 m)
  - Calcular el factor de conversión entre ellas
  - Normativa: `NP 196:1991 §4` · `NBR 6123:2023 §5` · `ASCE 7-22 §26.5` · `EN 1991-1-4 §4.2`

- [ ] **eE-2** · Clasificación del terreno y factor de rugosidad por dirección
  - Zona urbana CDE: Categoría III (NBR), Exposición C (ASCE), Categoría II/III (EC1)
  - Documentar el perfil vertical para las 4 direcciones (N, S, E, O)
  - Normativa: `NBR 6123:2023 §6.3` · `ASCE 7-22 §26.7` · `EN 1991-1-4 §A.1`

- [ ] **eE-3** · Coeficientes de presión exterior Cpe por fachada
  - Definir presiones sobre cada fachada (barlovento, sotavento, laterales, cubierta)
  - Tabular Cpe para viento en X e Y
  - Verificar efecto de canalización entre edificios próximos
  - Normativa: `NBR 6123:2023 Fig. 4` · `ASCE 7-22 §27.3` · `EN 1991-1-4 §7.2`

- [ ] **eE-4** · Presión dinámica del viento nivel por nivel (piso a piso)
  - Calcular w(z) = q(z) × Cp × G en cada nivel
  - Integrar para obtener la fuerza lateral Fi por piso
  - Tabular: nivel, cota z (m), V_diseño(z), q(z) (Pa), Cp, G, w(z) (kN/m²), ancho tributario, Fi (kN)
  - Normativa: `NP 196:1991 §5–§6` · `NBR 6123:2023 §8` · `ASCE 7-22 §27.3`

### Tareas — E.2 Análisis dinámico y respuesta estructural

- [ ] **eE-5** · Período fundamental de la estructura T₁
  - Fórmulas empíricas: T₁ = Ct·hn^x (ASCE 7-22 §26.11.2), T₁ ≈ 0,09·H/√B (NBR simplificado)
  - Para 18 pisos a ~3,35 m/piso: H ≈ 67 m
  - Verificar si el edificio es "sensible al viento dinámico" (T₁ > 1 s generalmente)
  - Normativa: `ASCE 7-22 §26.11` · `NBR 6123:2023 §9` · `EN 1991-1-4 §6.3`

- [ ] **eE-6** · Factor de ráfaga G y respuesta dinámica del edificio
  - Para edificios flexibles (T₁ > 1 s o f₁ < 1 Hz): calcular G_f dinámico
  - El factor de ráfaga dinámico incluye la respuesta resonante al espectro de turbulencia
  - Comparar G_estático vs. G_dinámico
  - Normativa: `ASCE 7-22 §26.11.4` · `NBR 6123:2023 §9.3`

- [ ] **eE-7** · Cortante basal total de viento (V_base) por norma
  - V = ΣFi (suma de fuerzas en todos los pisos) para cada norma
  - Tabular: V_base NP196 / V_base NBR / V_base ASCE / V_base EC1
  - ⭐ El diagrama de cortante acumulado de arriba hacia abajo es la **figura central de la tesis**

- [ ] **eE-8** · Momento de vuelco (Mₒ) y distribución de fuerzas sísmicas
  - Mₒ = ΣFi × zi (momento de vuelco en la base) para cada norma
  - Comparar con el momento estabilizador (peso del edificio × excentricidad mínima)
  - Calcular fuerza sísmica equivalente y comparar Vs vs. Vw (¿cuál gobierna?)
  - Normativa: `ASCE 7-22 §12.8` · `NBR 15421:2023` · `EN 1998-1`

- [ ] **eE-9** · Derivas de entrepiso (drift) por nivel
  - Calcular δi y Δi = δi - δ(i-1) en cada nivel bajo carga de viento
  - Verificar Δi/hi ≤ H/500 (CIRSOC) en todos los niveles
  - Si algún nivel supera el límite → reforzar núcleos o agregar muros de corte
  - Normativa: `CIRSOC 103 §6` · `ASCE 7-22 §12.12` · `NBR 6118:2023 §15.7`

- [ ] **eE-10** · Efectos de segundo orden (P-Δ) y estabilidad global
  - Calcular θ = ΔPtot / (Vtot × hi) para cada nivel
  - Si θ > 0,10 (ACI/AISC): las cargas de viento se amplifican
  - Si θ > 0,33: el edificio es inestable con ese sistema
  - Normativa: `ASCE 7-22 §12.8.7` · `ACI 318-19 §6.6.4` · `EC2 §5.8`

- [ ] **eE-11** · Aceleraciones en planta alta y confort de los ocupantes
  - Calcular la aceleración pico en el techo bajo viento de diseño
  - Verificar a_pico ≤ 20 mG (1 año retorno, uso residencial, ISO 10137)
  - Si se supera: considerar amortiguadores de masa activos
  - Normativa: `ISO 10137:2007` · `AISC Design Guide 11`

- [ ] **eE-12** · Script Python de cálculo de viento multinormativo
  - Motor de cálculo: perfiles de velocidad, presiones, fuerzas por piso, cortante basal, momento de vuelco, derivas — bajo las 4 normativas simultáneamente
  - Output: tabla comparativa + gráficos PNG
  - Cada número del capítulo de viento de la tesis debe salir de este script
  - Archivo: `06_Estructura/calculo/calculo_viento_multinormativo.py`

---

### Decisiones tomadas

| Fecha | Decisión | Fundamento |
|---|---|---|
| — | V₀ = 45 m/s como velocidad básica de referencia | NP 196:1991 para CDE |
| — | Categoría de terreno III (NBR) / Exposición C (ASCE) | Zona urbana CDE |

---

### Archivos de referencia

| Archivo | Descripción | Estado |
|---|---|---|
| `06_Estructura/calculo/calculo_viento_multinormativo.py` | Script multinormativo | ⏳ Pendiente crear |
| `07_KNOWLEDGE_BASE/07.04_Normativa_Resumen/` | Resúmenes de normas | Revisar |

---

### Notas de trabajo

> *(Dudas técnicas, observaciones, cosas a recordar)*

- La tesis AGENTES.md indica V₀ = 45 m/s para CDE. Confirmar con INTN/SEAM.
- La grilla de pilares y las secciones de núcleos (Etapa F) dependen directamente de los resultados de esta etapa.
- El análisis de torsión en planta (excentricidad accidental ±5%) debe incluirse aunque no esté en el roadmap original.

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO

### Capítulo — Ingeniería de Viento y Dinámica Estructural

#### 1. Introducción y justificación del análisis

El edificio en estudio tiene una altura total aproximada de **68,80 m** sobre el nivel de la calle (18 pisos residenciales + Planta Baja comercial), lo que lo clasifica como una **estructura esbelta sensible al viento dinámico** (H/B > 4; período fundamental T₁ > 1,0 s). A esta altura, el viento es la acción lateral que gobierna el diseño estructural por sobre la acción sísmica, dada la baja sismicidad de la región de Ciudad del Este.

La normativa paraguaya de referencia en materia de cargas de viento es la **NP 196:1991**, elaborada por el Instituto Nacional de Tecnología y Normalización (INTN). Dado que dicha norma data de 1991 y carece de procedimiento dinámico explícito para edificios flexibles, el presente trabajo adopta una metodología multinormativa comparativa que incluye adicionalmente:

- **NBR 6123:2023** (Brasil) — actualización más reciente, con procedimiento dinámico explícito
- **ASCE 7-22** (EE.UU.) — norma de referencia internacional con procedimiento GRF (Gust Response Factor) completo
- **EN 1991-1-4** (Eurocódigo 1, Europa) — norma europea con procedimiento de respuesta espectral

Esta comparativa multinormativa constituye el **aporte académico diferenciador** de la tesis.

#### 2. Parámetros de viento

##### 2.1 Velocidad básica de referencia

La velocidad básica de referencia adoptada para Ciudad del Este es **V₀ = 45 m/s**, correspondiente a una media cuadrática de ráfaga de 10 minutos a 10 m de altura sobre terreno plano, con período de retorno de 50 años.

*(Completar con: tabla de conversión de velocidades entre normas, mapa de isogustas, justificación del valor V₀)*

##### 2.2 Perfil de velocidades con la altura

Cada norma define un perfil de velocidades con la altura z de acuerdo a la rugosidad del terreno circundante:

| Norma | Categoría de terreno | Perfil de velocidades | z₀ (m) |
|---|---|---|---|
| NP 196:1991 | Categoría III — Zona urbana | Potencial (α=0,25) | — |
| NBR 6123:2023 | Categoria III — Zona urbana | Logarítmico | 0,30 |
| ASCE 7-22 | Exposure C — Open terrain | Potencial (α=1/6,5) | — |
| EN 1991-1-4 | Terrain cat. III | Logarítmico | 0,30 |

*(Completar con: tabla de velocidades Vz por nivel z de 0 a 70 m para cada norma, gráficos de perfiles)*

#### 3. Presiones y fuerzas de viento

##### 3.1 Coeficientes de presión exterior (Cpe)

*(Completar con: tablas de Cpe para edificio de relación H/B según cada norma, diagramas de distribución de presiones)*

##### 3.2 Distribución de fuerzas laterales por nivel

| Nivel | z (m) | Fi_NP196 (kN) | Fi_NBR (kN) | Fi_ASCE (kN) | Fi_EC1 (kN) |
|---|---|---|---|---|---|
| P18 | ~63,15 | — | — | — | — |
| P17 | ~59,80 | — | — | — | — |
| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |
| PB | 0,00 | — | — | — | — |

*(Completar con los valores calculados por el script `calculo_viento_multinormativo.py`)*

#### 4. Análisis dinámico

##### 4.1 Período fundamental de vibración

*(Completar con: cálculo de T₁ según cada norma, comparación con modelo analítico)*

##### 4.2 Factor de ráfaga dinámico (Gf)

*(Completar con: cálculo del factor G dinámico vs. estático, tabla comparativa)*

#### 5. Cortante basal y momento de vuelco — Comparativa multinormativa

*(Esta es la figura y tabla central del capítulo — completar con los resultados del script Python)*

| Norma | V_base (kN) | M_base (kN·m) | Δ_max (mm) | Δ/h_max |
|---|---|---|---|---|
| NP 196:1991 | — | — | — | — |
| NBR 6123:2023 | — | — | — | — |
| ASCE 7-22 | — | — | — | — |
| EN 1991-1-4 | — | — | — | — |

#### 6. Efectos de segundo orden (P-Δ)

*(Completar con: coeficiente θ por nivel, diagrama de derivas amplificadas)*

#### 7. Confort de los ocupantes — Aceleraciones bajo viento

*(Completar con: cálculo de aceleración pico en techo, comparación con ISO 10137:2007)*

#### 8. Conclusiones del capítulo

*(Completar una vez finalizadas todas las tareas de la Sección 1)*

---

### Referencias bibliográficas — Etapa E

- NP 196:1991 — Norma Paraguaya. Ações do vento nas edificações. INTN, Asunción, 1991.
- ABNT NBR 6123:2023 — Forças devidas ao vento em edificações. ABNT, Rio de Janeiro, 2023.
- ASCE 7-22 — Minimum Design Loads and Associated Criteria for Buildings and Other Structures. ASCE, Reston, 2022.
- EN 1991-1-4:2005 — Eurocode 1: Actions on Structures — Part 1-4: General actions — Wind actions. CEN, Brussels, 2005.
- ISO 10137:2007 — Bases for design of structures — Serviceability of buildings and walkways against vibrations. ISO, Geneva, 2007.
- AISC Design Guide 11 — Vibrations of Steel-Framed Structural Systems. AISC, Chicago, 2016.
