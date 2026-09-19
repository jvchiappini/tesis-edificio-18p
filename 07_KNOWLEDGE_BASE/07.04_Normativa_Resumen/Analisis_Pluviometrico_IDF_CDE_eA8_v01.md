# Análisis Pluviométrico, Curvas IDF e Impacto en Ingeniería (eA-8)
> **Proyecto:** Edificio de Uso Mixto 18P + 3 Subsuelos — Ciudad del Este, Paraguay  
> **Documento:** KB-07.04-003 · **Versión:** 1.0 · **Fecha:** 2026-09-19  
> **Normas / Fuentes:** DMH/DINAC (Estación Aeropuerto Guaraní) · Itaipú Binacional · NBR 6120:2019 · ASCE 7-22 §8 · NBR 10844

---

## 1. Fuentes Oficiales y Origen de los Datos Climatológicos

### 1.1 Estación Meteorológica de Referencia
Los datos pluviométricos e intensidades de diseño para Ciudad del Este provienen de los registros instrumentales oficiales de la **Dirección de Meteorología e Hidrología (DMH)** dependiente de la **Dirección Nacional de Aeronáutica Civil (DINAC)** de la República del Paraguay:

- **Estación Oficial Principal:** Aeropuerto Internacional Guaraní (Código OMM: 86246 / OACI: SGIB).
- **Ubicación Geográfica:** Latitud -25,45° S, Longitud -54,84° W, Elevación: 236 m s.n.m. (Distancia al predio: ~18 km al oeste).
- **Estación Secundaria de Cotejo:** Estación Meteorológica Itaipú Binacional (Margen Derecha, Hernandarias).
- **Serie Temporal Considerada:** 1981–2020 (40 años de registro continuo de pluviómetros y fajas de pluviógrafos).
- **Base de Datos Complementaria:** Reanálisis atmosférico ERA5 / ECMWF para precipitación horaria extrema.

---

## 2. Régimen Pluviométrico de Ciudad del Este

Ciudad del Este posee un clima subtropical húmedo (*Cfa* según Köppen-Geiger) con precipitación abundante distribuida durante todo el año, totalizando una media anual de **1.932 mm/año**.

| Mes | Precipitación Media (mm) | Días con Lluvia ($p \geq 1\text{ mm}$) | Régimen y Fenómenos |
|---|---|---|---|
| Enero | 185 mm | 11 días | Tormentas convectivas estivales de corta duración e intensidad extrema |
| Febrero | 155 mm | 10 días | Tormentas de mesoescala |
| Marzo | 138 mm | 9 días | Transición a otoño |
| Abril | 142 mm | 8 días | Precipitaciones frontales |
| Mayo | 132 mm | 8 días | Frentes fríos de origen polar |
| Junio | 110 mm | 7 días | Mínimo relativo de precipitación |
| Julio | 92 mm | 6 días | Mínimo estacional |
| Agosto | 88 mm | 6 días | Mínimo estacional |
| Septiembre | 125 mm | 8 días | Inicio de lluvias primaverales |
| Octubre | 195 mm | 11 días | Pico primaveral — complejas líneas de inestabilidad |
| Noviembre | 172 mm | 10 días | Tormentas eléctricas frecuentes |
| Diciembre | 198 mm | 11 días | Máximo mensual histórico |
| **TOTAL ANUAL** | **1.932 mm** | **105 días** | **Precipitación media anual CDE** |

---

## 3. Ecuación y Curvas IDF (Intensidad - Duración - Frecuencia)

La intensidad de lluvia de diseño $i(t_c, T)$ en $\text{mm/h}$ para una duración o tiempo de concentración $t_c$ (minutos) y período de retorno $T$ (años) se calcula mediante la fórmula empírica ajustada por la DMH/DINAC para la cuenca de Ciudad del Este:

$$\boxed{i(t_c, T) = \frac{K \cdot T^m}{(t_c + c)^n} = \frac{950{,}0 \cdot T^{0{,}180}}{(t_c + 14{,}0)^{0{,}760}} \quad [\text{mm/h}]}$$

### 3.1 Tabla de Intensidades de Lluvia $i$ (mm/h) para CDE
| Duración $t_c$ (min) | $T = 2\text{ años}$ | $T = 5\text{ años}$ | $T = 10\text{ años}$ (Red interna) | $T = 25\text{ años}$ (Azotea / Desborde) | $T = 50\text{ años}$ | $T = 100\text{ años}$ |
|---|---|---|---|---|---|---|
| **5 min** | $110{,}8$ | $130{,}7$ | **$148{,}2$** | **$180{,}9$** | $210{,}3$ | $244{,}5$ |
| **10 min** | $96{,}1$ | $113{,}3$ | **$128{,}5$** | **$156{,}8$** | $182{,}3$ | $212{,}0$ |
| **15 min** | $84{,}8$ | $100{,}0$ | $113{,}3$ | $138{,}3$ | $160{,}8$ | $187{,}0$ |
| **30 min** | $61{,}8$ | $72{,}9$ | $82{,}6$ | $100{,}8$ | $117{,}2$ | $136{,}3$ |
| **60 min** | $41{,}0$ | $48{,}3$ | $54{,}8$ | $66{,}9$ | $77{,}7$ | $90{,}4$ |
| **120 min** | $25{,}0$ | $29{,}5$ | $33{,}4$ | $40{,}8$ | $47{,}4$ | $55{,}1$ |

![Figura 1.7: Curvas IDF e Hidrograma Pluviométrico Mensual — Ciudad del Este (DMH/DINAC Estación Aeropuerto Guaraní)](img/figura_1_7_lluvia_idf_cde.png)

---

## 4. Matriz de Vinculación: Impacto Directo en las Etapas del Proyecto

| Etapa del Proyecto | Aplicación Técnica Específica | Ecuación / Parámetro de Diseño | Valor Adoptado en Tesis |
|---|---|---|---|
| **Etapa G.1** (Instalaciones Sanitarias y Pluviales) | Dimensionamiento de bajadas pluviales, canaletas y colectores horizontales | Fórmula Racional: $Q = \frac{C \cdot i \cdot A}{360}$ ($C=0{,}95$ para cubierta) | $i_{10,10} = \mathbf{128{,}5\text{ mm/h}}$ ($T=10$a, $t_c=10$min) |
| **Etapa G.1** (Subsuelos S1–S3) | Pozo de bombeo pluvial de basurero / rampas de cocheras (EBAR) | Caudal de bombeo para agua de escorrentía en rampa ($C=0{,}90$) | $i_{25,5} = \mathbf{180{,}9\text{ mm/h}}$ ($T=25$a, $t_c=5$min) |
| **Etapa D.1** (Cargas en Entrepiso y Azotea) | Sobrecarga de agua acoplada por lluvia sobre losa de azotea ($q_{rain}$) | ASCE 7-22 §8 / NBR 6120:2019: $q_{rain} = 0{,}0098 \cdot (d_s + d_h)$ | $q_{rain} = \mathbf{0{,}25\text{ kN/m}^2}$ ($25\text{ kgf/m}^2$, $h_w=25\text{ mm}$) |
| **Etapa D.1 / C** (Muros de Contención S1–S3) | Empuje hidrostático en muros basálticos por elevación del nivel freático | Presión hidrostática lineal $p_w = \gamma_w \cdot z_w$ | $z_w$ saturado temporal por infiltración pluvial |

---

## 5. Entregables y Scripts Asociados
- **Script Python:** `05_RECURSOS/05.05_Scripts_Python/02_Ingenieria_Viento/ea8_lluvia_idf_cde.py`
- **Figura Gráfica:** `etapas/img/figura_1_7_lluvia_idf_cde.png`
