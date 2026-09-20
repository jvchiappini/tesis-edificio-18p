# Lineamientos Estratégicos y Recomendaciones Clave para la Tesis

> **Documento de Referencia Permanente (Copilot / LLMs & Investigador)**  
> **Proyecto:** Diseño estructural, análisis dinámico de viento y modelado BIM (ISO 19650) de un edificio de uso mixto en altura (18P + 3 Subsuelos).  
> **Ubicación:** Ciudad del Este, Alto Paraná, Paraguay.  
> **Autor:** José Valentino Chiappini Vergara.

---

## 1. Visión General y Justificación del Proyecto

Este trabajo de grado aborda la integración entre la **Ingeniería Estructural**, el **Análisis Dinámico Multinormativo al Viento**, la **Metodología BIM bajo ISO 19650**, la **Optimización Algorítmica con Python (NSGA-II)** y el **Presupuesto/Cronograma Ejecutivo (5D/4D)**.

### Parámetros Maestros Definitivos del Sitio (Ficha Técnica eA-8 Consolidada):

* **Edificio de Uso Mixto:** 18 Pisos Residenciales (P01–P18, ~64,30 m de altura total sobre rasante) + Planta Baja Comercial + 3 Subsuelos de Cocheras (S1–S2) + Azotea Técnica (Piscina + SUM). **Sin oficinas.**
* **Polígono del Terreno (UTM Zona 21J, WGS84):** **7.618,49 m²** (Vértices P1, P2, P3, P4).
  * **Frente Principal P1→P2:** 117,27 m sobre Calle Los Lapachos (declinación magnética en CDE ≈ -14° W).
  * **Vértice Agudo P1 (61,44°):** Zona no edificable / cuña frontal de 669,55 m² para plaza seca de acceso y jardín.
  * **Retiros Reglamentarios Adoptados:** Frente 3,0 m, Fondo 3,0 m, Laterales 2,0 m.
  * **Parámetros Urbanísticos:** FOS = 0,70 (Área máx. huella = 5.332,94 m²) · FOT = 4,0 (Área total construible sobre rasante = 30.473,96 m²).
* **Rectángulo Edificable Inscripto Base:** **X: 2.5m → 87.5m / Y: 3.0m → 40.0m** (85,0 m × 37,0 m = 3.145 m² por planta).
* **Ingeniería de Viento ($V_0 = 45{,}0\text{ m/s}$):**
  * **NP 196:1991:** Categoría III — Clase B ($b=0{,}85; p=0{,}175$).
  * **NBR 6123:2023:** Categoria IV — Classe B ($b_m=0{,}86; p=0{,}20$).
  * **ASCE 7-22:** Exposure B ($\alpha=7{,}0; z_g=365{,}76\text{ m}$).
  * **EN 1991-1-4:** Categoría III ($z_0=0{,}30\text{ m}; z_{min}=5\text{ m}$).
  * **Direcciones dominantes:** Este (E) anual (~20,5 %), Norte (N) en verano, Sur (S) pampero en invierno.
* **Caracterización Sísmica (Baja Sismicidad):**
  * Aceleración pico $a_g = 0{,}05\text{ g}$ a $0{,}08\text{ g}$ ($T_R = 475\text{ años}$).
  * Sustrato rocoso Formación Serra Geral ($V_{s30} > 760\text{ m/s}$): **Site Class B** (ASCE 7-22) / **Classe A** (NBR 15421:2023) ($F_a=1{,}00, F_v=1{,}00$).
  * Cortante basal por viento ($3.500$–$4.800\text{ kN}$) supera por 3–4× al sismo elástico ($1.150\text{ kN}$). Viento gobierna sobre sismo.
* **Servicios e Infraestructura Urbana:**
  * Agua Potable ESSAP ($DN 50\text{ mm}$, $P \approx 1{,}5$–$2{,}0\text{ bar}$): Cisterna inferior 60 m³ en S1 + Tanque elevado 30 m³ en azotea.
  * Energía Eléctrica ANDE MT $23\text{ kV}$: Subestación Transformadora $1.000\text{ kVA}$ en S1 + Grupo Electrógeno $300\text{ kVA}$.
  * Alcantarillado: Colector municipal / Planta PTE compacta en Subsuelo S2.
* **🌧️ Caracterización Pluviométrica de Sitio (DMH/DINAC CDE):**
  * Precipitación media anual CDE: **1.932 mm/año** (clima *Cfa*).
  * Ecuación IDF oficial: $i(t_c, T) = \frac{950{,}0 \cdot T^{0{,}180}}{(t_c + 14{,}0)^{0{,}760}}\text{ mm/h}$.
  * Intensidad pluvial red interna: $i_{10,10} = \mathbf{128{,}5\text{ mm/h}}$ ($T=10\text{a}, t_c=10\text{min}$) → Insumo para **Etapa G.1**.
  * Intensidad pluvial azotea/desborde: $i_{25,5} = \mathbf{180{,}9\text{ mm/h}}$ ($T=25\text{a}, t_c=5\text{min}$) → Insumo para **Etapa G.1**.
  * Sobrecarga de agua en azotea: $q_{rain} = \mathbf{0{,}25\text{ kN/m}^2}$ ($25\text{ kgf/m}^2$) → Insumo para **Etapa D.1**.

---

## 2. Recomendaciones Estratégicas de Ingeniería

### A. Ingeniería de Viento (Capítulo Central y Diferenciador)
* **Comparativa Multinormativa:** Evaluar las acciones eólicas comparando la norma nacional **NP 196:1991** con estándares internacionales de vanguardia: **NBR 6123:2023**, **ASCE 7-22** y **EN 1991-1-4 (Eurocódigo 1)** para $V_0 = 45.0 \text{ m/s}$.
* **Verificaciones Dinámicas:** Cortante basal acumulado, momento de vuelco en la base, derivas interpiso ($\Delta/h \le 1/500$), efectos de 2° orden ($\gamma_z / P-\Delta$) y aceleraciones en el último piso habitado bajo criterios de confort humano (**ISO 10137**).

### B. Sistema Estructural de Entrepiso
* **Losas Nervadas/Reticulares Alivianadas Bidireccionales:** Canto 35 cm en plantas tipo y azotea (casetón 25 cm + capa 10 cm); canto 45 cm en PB y subsuelos.
* **Justificación Económica:** Demostrar el ahorro material y menor consumo de hormigón/acero frente a sistemas de losa armada o postensada.

---

## 3. Hoja de Ruta y Metodología (ISO 19650)

- [x] **Fase 1: Georreferenciación y Definición de Terreno (Etapa A)**
  - Polígono UTM real P1–P4 (7.618,49 m²), parámetros urbanísticos y caracterización eólica del sitio.
- [ ] **Fase 2: Planificación Arquitectónica Completa (Etapa B)**
  - Diseño de Plantas de Subsuelos (S1–S2), PB comercial, Plantas Tipo Residenciales P01–P18 y Azotea.
- [ ] **Fase 3: Geotecnia y Fundaciones (Etapa C)**
- [ ] **Fase 4: Ingeniería Estructural Gravitatoria y de Viento (Etapas D, E, F)**
- [ ] **Fase 5: Instalaciones MEP, Coordinación BIM e Imprimibles (Etapas G, H, I, J, K, L, M, N, O, P)**

---
*Este documento debe ser consultado por cualquier agente o LLM antes de redactar capítulos o realizar análisis computacionales del proyecto.*


