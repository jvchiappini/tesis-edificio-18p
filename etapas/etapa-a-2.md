# A.2 — Análisis de Sitio

> **Etapa A › Sub-etapa 2** · **Tareas:** 4 · **Estado:** 🟡 En progreso (eA-5 ✅ Completado)
> Normativa: NP 196:1991 · NBR 6123:2023 · ASCE 7-22 §26 · EN 1991-1-4 · NBR 15421

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de tareas

- [x] **eA-5** · **Análisis de vientos dominantes y exposición** ✅ 2026-09-19
  - Dirección dominante: **E (Este)** anual + **N** en verano (dic–feb) + frentes fríos del **S** (pampero, may–ago)
  - Fuente climatológica: ERA5/ECMWF 1991–2020 (hipótesis de tesis — verificar con DMH/DINAC)
  - Clasificación multinormativa:
    - **NP 196:1991 → Cat. III, Clase B** (b=0,85; p=0,175) — §5 Tabla 2
    - **NBR 6123:2023 → Categoria IV, Classe B** (bm=0,86; p=0,20) — §6.2 Tabela 4
    - **ASCE 7-22 → Exposure B** (α=7,0; zg=365,76 m) — §26.7 Table 26.10-1
    - **EN 1991-1-4 → Categoría III** (z₀=0,30 m; zmin=5 m) — §4.3 Tabla 4.1
  - Velocidad básica confirmada: **V₀ = 45 m/s** (NP 196:1991, Ciudad del Este, T=50 años)
  - Figuras generadas: `etapas/img/figura_1_4_rosa_de_vientos_cde.png` · `etapas/img/figura_1_5_perfiles_velocidad_multinormativos.png`
  - Script: `05_RECURSOS/05.05_Scripts_Python/02_Ingenieria_Viento/ea5_vientos_dominantes_exposicion.py`
  - KB: `07_KNOWLEDGE_BASE/07.04_Normativa_Resumen/Analisis_Viento_Exposicion_CDE_eA5_v01.md`

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
  - 🌧️ **LLUVIA — Incluir obligatoriamente el dato pluvial del sitio:**
    - Intensidad de diseño de la curva IDF de la **DMH/DINAC** para CDE: `i ≈ 80–120 mm/h` (T=10 años, tc=10 min)
    - Período de retorno para red pluvial del edificio: **T=10 años** (uso interno) / **T=25 años** (calle / desborde)
    - Precipitación media anual CDE: ~1.900 mm/año (dato DMH/DINAC)
    - Este dato es insumo directo de **Etapa G.1** (cálculo de bajadas pluviales) y **Etapa D.1** (carga lluvia en azotea)
  - Archivo: `00_GESTION_DE_PROYECTO/LINEAMIENTOS_Y_RECOMENDACIONES_TESIS.md`

### Decisiones tomadas

| Fecha | Decisión | Fundamento |
|---|---|---|
| 2026-09-19 | **V₀ = 45 m/s** — Velocidad básica de referencia | NP 196:1991 — Mapa de isopletas de viento para la Región Oriental del Paraguay, Ciudad del Este |
| 2026-09-19 | Dirección dominante: **E** anual / **N** (dic–feb) / **S** pampero (may–ago) | ERA5/ECMWF reanálisis 1991–2020 — WeatherSpark CDE. Verificación pendiente DMH/DINAC |
| 2026-09-19 | **NP 196:1991 → Categoría III, Clase B** (b=0,85; p=0,175) | Zona urbana con obstáculos de 5–15 m, radio 500 m–2 km. §5 Tabla 2 NP 196 |
| 2026-09-19 | **NBR 6123:2023 → Categoria IV, Classe B** (bm=0,86; p=0,20) | Zona urbanizada densa, obstáculos numerosos y poco espaciados. §6.2 Tabela 4 |
| 2026-09-19 | **ASCE 7-22 → Exposure B** (α=7,0; zg=365,76 m) | Urban/suburban terrain, closely spaced obstructions. §26.7.3, Table 26.10-1 |
| 2026-09-19 | **EN 1991-1-4 → Categoría III** (z₀=0,30 m; zmin=5 m; kr=0,215) | Regular cover vegetation/buildings, suburban terrain. §4.3, Tabla 4.1 |
| 2026-09-19 | ⚠️ **CORRECCIÓN:** ASCE 7-22 → Exp. **B** (no C como figuraba en el borrador anterior) | El entorno de CDE es urbano consolidado. Exp. C corresponde a terreno abierto/campo (§26.7.2) |
| 2026-09-19 | ⚠️ **CORRECCIÓN:** NBR 6123 → Cat. **IV** (no III como figuraba en el borrador anterior) | Entorno de CDE con edificaciones frecuentes encuadra en Cat. IV (obstáculos numerosos, §6.2) |
| 2026-09-19 | Viento **gobierna sobre sismicidad** para diseño estructural | Zona sísmica baja (PGA ~0,05–0,08g), sustrato roca basáltica. Verificar cuantitativamente en Etapa E |

### Archivos de referencia y figuras generadas

| Archivo | Descripción | Estado |
|---|---|---|
| `05_RECURSOS/05.05_Scripts_Python/02_Ingenieria_Viento/ea5_vientos_dominantes_exposicion.py` | Script Python eA-5: Rosa de vientos + Perfiles multinormativos | ✅ Creado |
| `etapas/img/figura_1_4_rosa_de_vientos_cde.png` | Figura 1.4: Rosa de vientos anual CDE — ERA5/ECMWF 1991–2020 | ✅ Generado |
| `etapas/img/figura_1_5_perfiles_velocidad_multinormativos.png` | Figura 1.5: Perfiles Vk(z) comparativos — 4 normas | ✅ Generado |
| `07_KNOWLEDGE_BASE/07.04_Normativa_Resumen/Analisis_Viento_Exposicion_CDE_eA5_v01.md` | KB: Análisis multinormativo de exposición eA-5 | ✅ Creado |
| `00_GESTION_DE_PROYECTO/LINEAMIENTOS_Y_RECOMENDACIONES_TESIS.md` | Ficha técnica del sitio (actualizar con parámetros eA-5) | Pendiente eA-8 |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO

### 1.3 Vientos dominantes y clasificación de la exposición

#### 1.3.1 Régimen de vientos en Ciudad del Este — Análisis climatológico

La ciudad de Ciudad del Este, departamento de Alto Paraná, República del Paraguay, se ubica en la confluencia de los ríos Paraná y Monday (lat: 25°30'S, lon: 54°37'W, altitud media: ~230 m s.n.m.). El clima es subtropical húmedo de tipo **Cfa** (Köppen-Geiger), con precipitaciones distribuidas a lo largo del año. El régimen de vientos está condicionado por el desplazamiento estacional de los sistemas de presión atmosférica sobre el Cono Sur americano.

A partir del reanálisis climático ERA5/ECMWF 1991–2020 (hipótesis de anteproyecto; fuente primaria oficial: DMH/DINAC), se identifican los siguientes patrones estacionales:

| Período | Dirección dominante | Mecanismo físico |
|---|---|---|
| Dic–feb (verano) | **Norte (N)** — ~8,5 % frecuencia anual | Flujos cálidos y húmedos del Atlántico Norte; baja térmica sobre el Chaco |
| Feb–dic (resto del año) | **Este (E)** — ~20,5 % frecuencia anual | Anticiclón del Atlántico Sur; pico ~39 % en agosto |
| May–ago (frentes fríos) | **Sur (S)** — ~6,5 % frecuencia anual | «Pampero»: masa de aire frío polar desde la Patagonia/Argentina |

> **Hipótesis de anteproyecto:** Datos estadísticos obtenidos de reanálisis ERA5/ECMWF 1991–2020 para lat=−25,50°, lon=−54,62°. La fuente oficial primaria es la **DMH/DINAC** (Anuario Estadístico, Cuadro 1.3.9). Para la etapa ejecutiva se requerirá el anuario estadístico oficial (disponible en datos.gov.py).

La velocidad media anual del viento a 10 m de altura es de aproximadamente **10,0 km/h** (~2,8 m/s), valor de servicio habitual muy inferior a la velocidad de diseño estructural.

![Figura 1.4: Rosa de vientos anual — Ciudad del Este, Paraguay (ERA5/ECMWF 1991–2020)](img/figura_1_4_rosa_de_vientos_cde.png)

#### 1.3.2 Velocidad básica de referencia — NP 196:1991

Conforme a la **NP 196:1991** (*Acción del viento en las construcciones*, INTN, Asunción, 1991), la velocidad básica de referencia adoptada para Ciudad del Este, departamento de Alto Paraná, es:

$$\boxed{V_0 = 45{,}0 \text{ m/s}}$$

Esta velocidad corresponde a la velocidad media (ráfaga de 3 s / media de 10 min, según la definición análoga a la NBR 6123 en que se basa la NP 196), medida a **10 m de altura** sobre terreno plano abierto (Categoría II), con **período de retorno T = 50 años** (probabilidad de excedencia anual $p = 2\%$). El factor de riesgo social $S_3 = 1{,}10$ se adopta para edificios de alta densidad de ocupación.

> **Nota de rigor normativo:** La NP 196:1991 contempla únicamente eventos **sinópticos** y carece de método de análisis dinámico para estructuras esbeltas (Martínez et al., CILAMCE-PANACM 2021; Ibarra et al., ICCEIA 132, 2024). Esta limitación justifica el análisis complementario con NBR 6123:2023, ASCE 7-22 y EN 1991-1-4, que sí incorporan el factor de ráfaga dinámico ($\xi$, $G_f$, $c_s c_d$).

#### 1.3.3 Clasificación del terreno y categoría de exposición — Análisis multinormativo

El entorno inmediato del predio (radio 500 m a 2 km) en el sector sur de Ciudad del Este corresponde a una **zona urbana de densidad media-alta**: edificaciones de 1–5 pisos (4–18 m), lotes de 10–25 m de frente, espaciado entre edificios inferior a 5 veces la altura media de obstáculos. Bajo estas condiciones, la clasificación de rugosidad por norma es:

| Norma | Art. / Tabla | **Categoría adoptada** | Parámetros | Descripción del entorno tipo | $V_k(z{=}10\text{ m})$ (m/s) |
|---|---|---|---|---|---|
| **NP 196:1991** | §5 — Tabla 2, Clase B | **Categoría III** | $b=0{,}85$; $p=0{,}175$ | Zona con obstáculos frecuentes de pequeñas dimensiones (h=5–15 m), periferia urbana | **38,25** |
| **NBR 6123:2023** | §6.2 — Tabela 4, Classe B | **Categoria IV** | $b_m=0{,}86$; $p=0{,}20$; $F_r=1{,}00$ | Terrenos cobertos por obstáculos numerosos e pouco espaçados (parques, cidades pequenas) | **38,70** |
| **ASCE 7-22** | §26.7.3 — Table 26.10-1 | **Exposure B** | $\alpha=7{,}0$; $z_g=365{,}76\text{ m}$ | Urban and suburban areas; closely spaced obstructions ≥ single-family dwellings | **33,13** |
| **EN 1991-1-4** | §4.3 — Tabla 4.1 | **Categoría III** | $z_0=0{,}30\text{ m}$; $z_{min}=5\text{ m}$ | Area with regular cover of vegetation or buildings; suburban terrain | **34,08** |

Las fórmulas del perfil de velocidad con la altura empleadas por norma son:

**NP 196:1991 y NBR 6123:2023** — Factor $S_2(z)$:

$$V_k(z) = V_0 \cdot S_1 \cdot S_2(z) \cdot S_3 \qquad \text{con} \quad S_2(z) = b \cdot \left(\frac{z}{10}\right)^p \quad \text{para } z \geq z_{min}$$

**EN 1991-1-4:2010** — Factor de rugosidad $c_r(z)$ (§4.3.2):

$$v_m(z) = c_r(z) \cdot c_o(z) \cdot v_b \qquad \text{con} \quad c_r(z) = k_r \cdot \ln\!\left(\frac{z}{z_0}\right), \quad k_r = 0{,}19 \cdot \left(\frac{z_0}{0{,}05}\right)^{0{,}07}$$

**ASCE 7-22** — Coeficiente de exposición $K_z$ (§26.10.1, Table 26.10-1):

$$K_z = 2{,}01 \cdot \left(\frac{z}{z_g}\right)^{2/\alpha} \qquad \Rightarrow \quad q_z = 0{,}613 \cdot K_z \cdot K_{zt} \cdot K_e \cdot V^2 \quad \text{(Pa)}$$

> ⚠️ **Advertencia inter-normativa:** $V_0 = 45\text{ m/s}$ (NP 196 / NBR / EC1) corresponde a la velocidad **media de 10 minutos**. El ASCE 7-22 usa **ráfaga de 3 s**: conversión $V_{3s} \approx 1{,}25 \cdot V_{10min} \approx 56{,}25\text{ m/s}$. La comparación cuantitativa inter-normativa de presiones se realiza en la **Etapa E**. En esta sub-etapa se compara exclusivamente la **forma adimensional del perfil** vertical.

![Figura 1.5: Perfiles comparativos de velocidad de viento con la altura — NP 196:1991 / NBR 6123:2023 / ASCE 7-22 / EN 1991-1-4](img/figura_1_5_perfiles_velocidad_multinormativos.png)

#### 1.3.4 Implicancias sobre el diseño estructural

1. **Direcciones críticas (Etapa E):** La dirección **E–O** (azimut ~90°, mayor frecuencia anual) y la dirección **N–S** (azimut ~0°/180°, episodios de mayor intensidad por frentes fríos) deben analizarse de forma independiente sobre los dos ejes ortogonales del edificio.
2. **Reducción por rugosidad:** La adopción de Cat. III (NP 196) / Cat. IV (NBR) implica una reducción de ~12–18 % en $V_k(z=10\text{ m})$ respecto a terreno abierto, que decrece a <5 % en el piso 18 (~64 m), donde las diferencias entre categorías son mínimas.
3. **Análisis dinámico:** Para $H \approx 64\text{ m}$ y esbeltez $H/B \approx 1{,}73$ (hipótesis), la NBR 6123:2023 y el ASCE 7-22 exigen calcular el **factor de ráfaga dinámico** ($\xi$ en NBR / $G_f$ en ASCE). La NP 196:1991 carece de este método; se complementará con los procedimientos internacionales en la Etapa E.

### 1.4 Clasificación sísmica del sitio

De acuerdo con la **ABNT NBR 15421:2023** y el mapa de peligrosidad sísmica de Paraguay, Ciudad del Este se clasifica en la **Zona de Baja Sismicidad**, con aceleración pico del suelo:

$$a_g \approx 0{,}05\text{ g} \text{ a } 0{,}08\text{ g} \quad (T_R = 475 \text{ años})$$

El sustrato de la **Formación Serra Geral** (basalto toleítico, Triásico-Jurásico, afloramiento en todo el Dpto. Alto Paraná) clasifica el perfil como:

| Norma | Tipo de suelo | $V_{s30}$ | Descripción |
|---|---|---|---|
| **ASCE 7-22** §11.4 | **Site Class B** | $> 760\text{ m/s}$ | Rock — roca sana o levemente meteorizada |
| **NBR 15421:2023** | **Classe A** | $> 800\text{ m/s}$ | Rocha sã ou muito rígida |

La **acción de viento gobierna** sobre la acción sísmica para este edificio en zona de baja sismicidad con sustrato rocoso. Esta jerarquía se verificará cuantitativamente en la Etapa E.

### 1.5 Infraestructura urbana disponible

*(Tarea pendiente eA-7 — Completar con: redes ESSAP, ANDE 23 kV MT, alcantarillado y telecomunicaciones)*

### 1.6 Ficha técnica del sitio — Resumen consolidado (eA-8)

| Parámetro | Valor adoptado | Fuente / Estado |
|---|---|---|
| Coordenadas UTM | Zona 21J, WGS84 / SIRGAS2000 | Google Earth Pro v7.3 — Hipótesis tesis |
| Área del terreno | 7.618,49 m² | Cálculo Gauss/Shoelace ✅ |
| Frente principal P1→P2 | 117,27 m (Calle Los Lapachos, azimut 80,82°) | Planimetría UTM ✅ |
| Vértice agudo P1 | 61,44° (cuña 669,55 m²) | Cálculo trigonométrico ✅ |
| FOS / FOT | 0,70 / 4,0 | Ordenanzas CDE 030/2000 y 024/2014 ✅ |
| **V₀** | **45,0 m/s** | **NP 196:1991 — isopletas PY ✅** |
| **Cat. terreno NP 196** | **Cat. III — Clase B** | Análisis entorno urbano ✅ |
| **Cat. terreno NBR 6123** | **Cat. IV — Classe B** | Análisis entorno urbano ✅ |
| **Exposición ASCE 7-22** | **Exposure B** | §26.7.3 ASCE 7-22 ✅ |
| **Cat. terreno EC1** | **Cat. III (z₀=0,30 m)** | §4.3 EN 1991-1-4 ✅ |
| Dirección dominante anual | **Este (E)** — ~20,5 % freq. | ERA5/ECMWF — Hipótesis ⚠️ |
| Dirección dominante (verano) | **Norte (N)** — dic a feb | ERA5/ECMWF — Hipótesis ⚠️ |
| Frentes fríos (invierno) | **Sur (S)** — may a ago (pampero) | ERA5/ECMWF — Hipótesis ⚠️ |
| Velocidad media anual | ~10,0 km/h (~2,8 m/s) | ERA5/ECMWF — Hipótesis ⚠️ |
| Sismicidad | Zona baja — $a_g \approx 0{,}05$–$0{,}08\text{ g}$ | NBR 15421:2023 / ASCE 7-22 ✅ |
| Perfil sísmico | **Site Class B / Classe A** | Formación Serra Geral (basalto) ✅ |
| $V_{s30}$ | $> 760\text{ m/s}$ | Hipótesis — sustrato basáltico ⚠️ |
| Capacidad portante $q_{adm}$ | 300 kN/m² | Hipótesis de tesis ⚠️ |
| Nivel freático | $> 12\text{ m}$ de profundidad | Hipótesis de tesis ⚠️ |
| 🌧️ **Precipitación media anual** | **~1.900 mm/año** | DMH/DINAC — Hipótesis ⚠️ (confirmar en eA-8) |
| 🌧️ **Intensidad pluvial diseño** | **i ≈ 80–120 mm/h** (T=10 años, tc=10 min) | Curva IDF DMH/DINAC CDE — Hipótesis ⚠️ → Usar en **G.1** y **D.1** |

> ✅ = Determinado técnicamente · ⚠️ = Hipótesis de anteproyecto pendiente de verificación instrumental

> **Declaración formal:** Los valores marcados ⚠️ no han sido obtenidos mediante instrumentación in situ. No reemplazan: (i) estación meteorológica en el predio; (ii) estudio geotécnico con sondeo SPT; (iii) relevamiento geodésico GNSS diferencial. Para la etapa ejecutiva se requerirán estudios homologados conforme a la legislación de la República del Paraguay.

---

### Referencias bibliográficas — A.2

- Instituto Nacional de Tecnología, Normalización y Metrología (INTN), *Acción del viento en las construcciones*, Norma Paraguaya NP 196:1991, 1.ª ed., Asunción, Paraguay, 1991.
- Associação Brasileira de Normas Técnicas, *Forças devidas ao vento em edificações*, ABNT NBR 6123:2023, Rio de Janeiro, Brasil, 2023. §6.2, Tabela 4.
- American Society of Civil Engineers, *Minimum Design Loads and Associated Criteria for Buildings and Other Structures*, ASCE/SEI 7-22, Reston, VA, EE.UU., 2022. §26.7, Table 26.10-1.
- European Committee for Standardization (CEN), *EN 1991-1-4:2010 — Eurocode 1: Actions on structures — Part 1-4: Wind actions*, Brussels, Belgium, 2010. §4.3, Tabla 4.1.
- Associação Brasileira de Normas Técnicas, *Projeto de estruturas resistentes a sismos*, ABNT NBR 15421:2023, Rio de Janeiro, Brasil, 2023.
- A. Martínez, A. Marín, E. Aquino y D. Arévalos, «Study of the maximum wind speeds and meteorological characteristics in Paraguay using the NP-196 standard for a future update», *Proc. CILAMCE-PANACM 2021*, San Pablo, Brasil, 2021.
- W. Ibarra, D. Arévalos, V. Silva, L. Quintana y O. Martínez-Pavetti, «Dynamic Analysis of a Slender Building Using Two Parallel Spectral Analysis Methods», *NewTech 2024 — ICCEIA 132*, Asunción, Paraguay, 2024.
- Dirección de Meteorología e Hidrología (DMH/DINAC), *Anuarios Estadísticos Climatológicos*, Asunción, Paraguay. Disponible en: https://datos.gov.py
- WeatherSpark.com, *Promedio del Tiempo en Ciudad del Este, Paraguay*, Cedar Lake Ventures, Inc., 2026. Disponible en: https://weatherspark.com/y/28524/

