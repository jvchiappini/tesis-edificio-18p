# A.2 — Análisis de Sitio

> **Etapa A › Sub-etapa 2** · **Tareas:** 4 · **Estado:** 🔲 Sin iniciar
> Normativa: NP 196:1991 · NBR 6123:2023 · ASCE 7-22 §26 · NBR 15421

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de tareas

- [ ] **eA-5** · **Análisis de vientos dominantes y exposición**
  - Determinar dirección predominante de viento en CDE (generalmente NE-SO en la región)
  - Clasificar rugosidad del terreno: Categoría de exposición según NP 196:1991, NBR 6123:2023 y ASCE 7-22
  - Esto condiciona directamente la **Etapa E** (cálculo de viento)
  - Normativa: `NP 196:1991 §5` · `NBR 6123:2023 §6` · `ASCE 7-22 §26`

- [ ] **eA-6** · **Clasificación sísmica del sitio**
  - Verificar zonificación sísmica de Paraguay (CDE: zona baja a moderada)
  - Clasificar el perfil de suelo (Tipo A–D según ASCE 7-22 o NBR 6118)
  - Documentar el período del suelo Ts para el espectro de diseño
  - Normativa: `NBR 15421` · `ASCE 7-22 §11`

- [ ] **eA-7** · **Estudio de infraestructura urbana disponible**
  - Agua potable: red ESSAP (presión disponible en la red municipal)
  - Alcantarillado sanitario: red pública o sistema propio (cámara séptica + pozo absorbente)
  - Electricidad: tensión ANDE disponible (23 kV en media tensión para subestación propia)
  - Gas natural: disponibilidad en la zona (si no hay, prever GLP en tanques)
  - Telecomunicaciones: operadoras disponibles (Claro, Tigo, Personal)

- [ ] **eA-8** · **Ficha técnica del sitio y declaración de hipótesis**
  - Redactar documento resumen con todos los parámetros del sitio
  - Cada valor asumido lleva la nota **"hipótesis de tesis"**
  - Este documento es la referencia única para todas las etapas siguientes
  - Archivo: `00_GESTION_DE_PROYECTO/LINEAMIENTOS_Y_RECOMENDACIONES_TESIS.md`

### Decisiones tomadas

| Fecha | Decisión | Fundamento |
|---|---|---|
| — | V₀ = 45 m/s como velocidad básica de referencia | NP 196:1991 para zona CDE |
| — | Categoría de terreno urbano (Cat. III NBR / Exp. C ASCE) | Entorno urbano consolidado de CDE |
| — | Suelo Tipo B (roca basáltica, Vs30 > 760 m/s) | Formación Serra Geral en CDE |

### Archivos de referencia

| Archivo | Descripción | Estado |
|---|---|---|
| `00_GESTION_DE_PROYECTO/LINEAMIENTOS_Y_RECOMENDACIONES_TESIS.md` | Ficha técnica del sitio | Actualizar |
| `07_KNOWLEDGE_BASE/07.04_Normativa_Resumen/` | Resúmenes normativos | Revisar |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO

### 1.3 Vientos dominantes y clasificación de la exposición

La ciudad de Ciudad del Este se encuentra en la **región oriental del Paraguay**, caracterizada por un clima subtropical húmedo (clasificación Köppen: Cfa). Los vientos predominantes en la región provienen del sector **Norte-Noreste (NNE)** durante la primavera y el verano, y del sector **Sur-Suroeste (SSO)** durante el otoño y el invierno.

Para los efectos del diseño estructural, la velocidad básica de referencia adoptada es **V₀ = 45 m/s**, correspondiente a una media cuadrática de ráfaga de 10 minutos medida a 10 m de altura sobre terreno plano y homogéneo, con período de retorno de 50 años, de acuerdo con la `NP 196:1991`.

La clasificación del terreno circundante al predio, considerando la densidad urbana del entorno, resulta en:

| Norma | Categoría | Descripción |
|---|---|---|
| NP 196:1991 | Categoría III | Zona urbana con obstáculos frecuentes |
| NBR 6123:2023 | Categoria III | Superfície plana com obstáculos numerosos |
| ASCE 7-22 | Exposure C | Open terrain with scattered obstructions |
| EN 1991-1-4 | Terrain cat. III | Area with regular cover of vegetation |

*(Insertar: rosa de vientos, perfiles de velocidad verticales por categoría de terreno)*

### 1.4 Clasificación sísmica del sitio

De acuerdo con el mapa de peligrosidad sísmica de la República del Paraguay, la zona de Ciudad del Este se clasifica dentro de la **Zona de Baja Sismicidad**, con una aceleración pico del suelo (PGA) para un período de retorno de 475 años estimada en **a_g ≈ 0,05 g** a 0,08 g.

El perfil de suelo en la zona, correspondiente al sustrato basáltico de la **Formación Serra Geral** (basalto toleítico del Triásico-Jurásico), se clasifica como:

| Norma | Tipo de suelo | Vs30 | Descripción |
|---|---|---|---|
| ASCE 7-22 | Site Class B | > 760 m/s | Rock |
| NBR 6118:2023 | Rocha ou solo muito rígido | > 800 m/s | — |

Para las combinaciones de carga de diseño, se verificará que la **acción de viento** gobierna sobre la acción sísmica, lo cual es esperado para un edificio de esta altura en zona de baja sismicidad.

### 1.5 Infraestructura urbana disponible

*(Completar con: descripción de redes existentes, tensión y potencia ANDE disponible, presión de la red ESSAP, sistema de aguas residuales municipal)*

### 1.6 Ficha técnica del sitio — Resumen

| Parámetro | Valor | Fuente / Hipótesis |
|---|---|---|
| Coordenadas UTM | Zona 21J, WGS84 | Relevamiento GPS |
| Área del terreno | 7.618,49 m² | Cálculo por coordenadas |
| Frente principal | 117,27 m | Medición |
| Ángulo vértice P1 | 61,44° | Cálculo trigonométrico |
| FOS / FOT | 0,70 / 4,0 | Hipótesis de tesis |
| Velocidad básica V₀ | 45 m/s | NP 196:1991 |
| Categoría de terreno | III (NBR) / C (ASCE) | Análisis del entorno |
| Perfil sísmico | Tipo B (roca) | Formación Serra Geral |
| Capacidad portante | 300 kN/m² | Hipótesis de tesis |
| Nivel freático | > 12 m prof. | Hipótesis de tesis |

> **Declaración:** Todos los valores sin fuente de campo se adoptan como **hipótesis de tesis** y no reemplazan estudios específicos de campo (estudio geotécnico, estudio de suelos, estudio de viento instrumental).

---

### Referencias bibliográficas — A.2

- NP 196:1991 — Norma Paraguaya de Cargas de Viento. INTN, Asunción.
- ABNT NBR 6123:2023 — Forças devidas ao vento em edificações. ABNT, Rio de Janeiro.
- ASCE 7-22 — Minimum Design Loads and Associated Criteria. ASCE, Reston, 2022.
- ABNT NBR 15421:2023 — Projeto de estruturas resistentes a sismos. ABNT.
- ESSAP S.A. — Empresa de Servicios Sanitarios del Paraguay.
- ANDE — Administración Nacional de Electricidad del Paraguay.
