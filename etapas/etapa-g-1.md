# G.1 — Instalaciones Sanitarias (SAN / CLO / PLU)

> **Etapa G › Sub-etapa 1** · **Tareas:** 4 · **Estado:** 🔲 Sin iniciar  
> Normativa: Reglamento ESSAP / SENASA · NBR 5626 (Agua) · NBR 8160 (Esgoto)

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task G1.1:** Dimensionar el volumen del reservorio inferior de agua potable (60 m² en PB/S1) y tanque elevado en azotea (Consumo: 250 L/hab/día).
- [ ] **Task G1.2:** Calcular la red de distribución de agua fría y caliente sanitaria con sistema de presurización de frecuencia variable.
- [ ] **Task G1.3:** 🌧️ **LLUVIA — Red pluvial del edificio (cálculo hidráulico obligatorio)**
  - **Insumo principal:** Intensidad pluvial de diseño de la Curva IDF DMH/DINAC para CDE: **i ≈ 80–120 mm/h** (T=10 años, tc=10 min). Dato a confirmar en **eA-8**.
  - **Caudal de diseño** por bajada (Fórmula Racional — NBR 10844:1989 §5.3):
    $$Q = \frac{C \cdot i \cdot A}{60} \quad (\text{L/min}) \qquad C_{cubierta} = 1{,}00 \quad C_{balcones} = 0{,}90$$
  - Trazar las **bajadas pluviales** (PVC DWV Ø150mm, $J_{min}=2\%$) con colectores horizontales en pleno técnico de PB.
  - **Impermeabilización** de azotea y terrazas: sistema multicapa (membranas de PVC o bituminosas) + pendientes $\geq 1{,}5\%$ hacia canaletas. Verificar ponding (conectado con Task D1.4 en Etapa D).
  - **EBAR subsuelos** (Estación de Bombeo de Aguas Residuales Pluviales): para subsuelos S1–S2, diseñar pozo de bombeo con 2 electrobombas sumergibles redundantes para evacuar infiltraciones y lluvia extrema por rampas.
  - Normativa: `NBR 10844:1989` · `ABNT NBR 7229:1993` · `NBR 5626:2020`
- [ ] **Task G1.4:** Resolver el ducto de RSU (Trash Chute Ø500mm acero inox) con descarga horizontal a contenedor basculante de 10 m³ en el Depósito RSU de PB.

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Dimensionamiento del Reservorio de Agua Potable

Para una población estimada de 650 habitantes residenciales más el uso comercial:
- Consumo diario total ($Q_d$): $650 \text{ hab} \times 250 \text{ L/hab/día} + 15.000 \text{ L (comercio)} = 177.500 \text{ L/día} = 177.5 \text{ m}^3$.
- **Cisterna Inferior (80%):** $142 \text{ m}^3$ dividida en dos compartimentos independientes de H°A°.
- **Tanque Elevado en Azotea (20%):** $40 \text{ m}^3$ en H°A° revestido.

### 2. Sistema RSU Basculante Directo

El sistema de recolección de residuos sólidos urbanos adopta un ducto vertical insonorizado de acero inoxidable Ø500mm con compuertas estancas en cada nivel. El ducto descarga por gravedad en el contenedor basculante de 10 m³ ubicado en la PB (+0.00m) accesible por camión recolector sin requerir ingreso a subsuelos.
