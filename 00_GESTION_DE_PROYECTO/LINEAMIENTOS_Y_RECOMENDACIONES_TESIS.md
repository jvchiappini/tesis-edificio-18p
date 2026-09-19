# Lineamientos Estratégicos y Recomendaciones Clave para la Tesis

> **Documento de Referencia Permanente (Copilot / LLMs & Investigador)**  
> **Proyecto:** Diseño estructural, análisis dinámico de viento y modelado BIM (ISO 19650) de un edificio de uso mixto en altura (18P + 3 Subsuelos).  
> **Ubicación:** Ciudad del Este, Alto Paraná, Paraguay.  
> **Autor:** José Valentino Chiappini Vergara.

---

## 1. Visión General y Justificación del Proyecto

Este trabajo de grado aborda la integración entre la **Ingeniería Estructural**, el **Análisis Dinámico Multinormativo al Viento**, la **Metodología BIM bajo ISO 19650**, la **Optimización Algorítmica con Python (NSGA-II)** y el **Presupuesto/Cronograma Ejecutivo (5D/4D)**.

### Parámetros Maestros Definitivos del Proyecto:
* **Edificio de Uso Mixto:** 18 Pisos Residenciales (P01–P18, ~64.30m de altura total sobre rasante) + Planta Baja Comercial + 3 Subsuelos de Cocheras (S1–S3) + Azotea Técnica (Piscina + SUM). **Sin oficinas.**
* **Polígono del Terreno (UTM Zona 21J):** **7.618,49 m²** (Vértices P1, P2, P3, P4).
  * **Frente Principal P1→P2:** 117,27 m sobre vía pública (declinación magnética en CDE ≈ -14°).
  * **Vértice Agudo P1 (61,44°):** Zona no edificable / cuña frontal de acceso peatonal y jardín.
  * **Retiros Reglamentarios Adoptados:** Frente 3.0 m, Fondo 3.0 m, Laterales 2.0 m.
  * **Parámetros Urbanísticos:** FOS = 0,70 (Área máx. huella = 5.332 m²) · FOT = 4,0 (Área total construible sobre rasante = 30.474 m²).
* **Rectángulo Edificable Inscripto Base:** **X: 2.5m → 87.5m / Y: 3.0m → 40.0m** (85.0 m × 37.0 m = 3.145 m² por planta).

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
  - Diseño de Plantas de Subsuelos (S1–S3), PB comercial, Plantas Tipo Residenciales P01–P18 y Azotea.
- [ ] **Fase 3: Geotecnia y Fundaciones (Etapa C)**
- [ ] **Fase 4: Ingeniería Estructural Gravitatoria y de Viento (Etapas D, E, F)**
- [ ] **Fase 5: Instalaciones MEP, Coordinación BIM e Imprimibles (Etapas G, H, I, J, K, L, M, N, O, P)**

---
*Este documento debe ser consultado por cualquier agente o LLM antes de redactar capítulos o realizar análisis computacionales del proyecto.*
