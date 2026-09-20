# B.2 — Plantas Arquitectónicas por Nivel

> **Etapa B › Sub-etapa 2** · **Tareas:** 4 · **Estado:** ⏳ En Desarrollo (Layouts de 3 Torres + Subsuelos Unificados)  
> Archivos fuente: `01_WIP/01.01_ARQ/` · Autodesk Revit 2024 · MCDE ([Ord. M. 003/2026](visor_ordenanzas.html?id=3693), [Ord. 011/1994](visor_ordenanzas.html?id=3146), [Ord. 030/2020 PTAR](visor_ordenanzas.html?id=2462)) · Ley N° 3966/2010 · ABNT NBR 9050 · ABNT NBR 15575

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task B2.1:** Desarrollar el layout funcional de los 2 subsuelos (S1, S2) integrando las **3 torres** directamente sobre la huella completa de $3.145\text{ m}^2$. Definir cocheras, rampas ($i \le 15\%$), Bloque Técnico, Cisterna y PTAR.
- [ ] **Task B2.2:** Desarrollar la Planta Baja (PB, cota $+0.00\text{ m}$) para la configuración de 3 torres. Definir halls de acceso independientes, locales comerciales, RSU y accesos universales NBR 9050.
- [ ] **Task B2.3:** Desarrollar las Plantas Tipo Residenciales para las **3 torres** (P01-P18). Definir tipologías de departamentos, distribución, aislamiento acústico NBR 15575 y núcleos de cada torre.
- [ ] **Task B2.4:** Desarrollar la Planta de Azotea Técnica y Amenities para la configuración de 3 torres. Piscina, SUM, gimnasio, sala de máquinas y tanque elevado coordinados con la estructura.

---

### Decisiones Tomadas — Consolidación Arquitectónica

| Fecha | Decisión Proyectual | Fundamento Técnico & Normativo | Estado |
|---|---|---|---|
| 2026-09-19 | **Layout Subsuelos S1-S2 Unificados** | Huella de $3.145\text{ m}^2$ integrada con módulos de $2,50 \times 5,00\text{ m}$ y pasillos de maniobra $W \ge 6,00\text{ m}$. | ⏳ En desarrollo |
| 2026-09-19 | **Ubicación PTAR en Subsuelo S2** | Recinto estanco aislado de $120\text{ m}^2$ con ventilación mecánica forzada ([Ord. 030/2020 Art. 5°](visor_ordenanzas.html?id=2462)). | ✅ Definido |
| 2026-09-19 | **Plantas Tipo 3 Torres** | Distribución residencial independiente para P01 a P18 por torre. | ⏳ En desarrollo |
| 2026-09-19 | **Aislamiento Acústico Medianero** | Muros divisorios en H°A° $e = 20\text{ cm}$ ($Rw \ge 54\text{ dB}$) conforme a NBR 15575. | ✅ Adoptado |
| 2026-09-19 | **Estructura de Azotea y Piscina** | Losa maciza H°A° $H = 30\text{ cm}$ bajo piscina con refuerzo de resistencia. | ⏳ En desarrollo |

---

### Archivos de Referencia y Documentación Generada

| Archivo | Descripción | Estado |
|---|---|---|
| `05_RECURSOS/05.05_Scripts_Python/01_Geometria_Terreno/dibujar_plantas_b2.py` | Script Python generador de plantas B.2 (300 DPI) | ✅ Creado |
| `etapas/img/figura_2_1_zonificacion_planta_baja.png` | Figura 2.1: Layout Detallado de Planta Baja ($3.145\text{ m}^2$) | ✅ Generado |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Plantas de Subsuelos (S1, S2 y S3 — Cota -3,50 m a -7,00 m)

Los 2 subsuelos abarcan una superficie construida de **$3.145,00\text{ m}^2$ cada uno** ($6.290,00\\text{ m}^2$ totales), excavados sobre el sustrato rocoso de basalto fresco (Formación Serra Geral, $q_{\text{adm}} = 300\text{ kN/m}^2$).

#### 1.1 Distribución Funcional por Nivel Subterráneo

1. **Subsuelo 2 (S2 — Cota -10.50 m):**
   - **Cocheras:** Módulos normalizados ($2,50 \times 5,00\text{ m}$) y pasillos de maniobras $W = 6,00\text{ m}$.
   - **Planta de Tratamiento de Efluentes (PTAR):** Recinto estanco de $120,00\text{ m}^2$ con sistema anaeróbico/aeróbico de depuración ([Ord. 030/2020 J.M.](visor_ordenanzas.html?id=2462)).
   - **Pozos de Sumidero & EBAR:** Estación de bombeo pluvial e infiltración.

2. **Subsuelo 2 (S1 — Cota -3,50 m):**
   - **Cocheras:** Plazas de estacionamiento y baúleras de depósito.

3. **Subsuelo 1 (S1 — Cota -3,50 m):**
   - **Cocheras:** Plazas de estacionamiento.
   - **Bloque Técnico Principal:**
     - Subestación Transformadora Padrón ANDE ($23\text{ kV} / 380\text{-}220\text{ V}$).
     - Grupo Electrógeno Diésel de Emergencia ($300\text{ kVA}$).
     - Reservorio Cisterna Inferior de Agua Potable y Cisterna Exclusiva PCI.

---

### 2. Planta Baja (PB — Cota +0.00m)

La Planta Baja ($3.145,00\text{ m}^2$, altura libre $H = 4,00\text{ m}$, $FOS_{\text{real}} = 41,28\% \le 70,00\%$) actúa como zócalo comercial y acceso independiente a las **3 Torres Residenciales**.

![Figura 2.1: Planta Baja Comercial y de Servicios](img/figura_2_1_zonificacion_planta_baja.png)

#### 2.1 Programa Detallado de Planta Baja
- **Lobbies Residenciales:** Vestíbulos independientes de acceso para cada una de las 3 torres con control de acceso biométrico.
- **Locales Comerciales ($1.850,00\text{ m}^2$ total):** Locales frontales vidriados con cristales Low-E neutros ([Ord. M. 003/2026 Art. 7°](visor_ordenanzas.html?id=3693)).
- **Bloque Técnico & RSU ($395,00\text{ m}^2$):** Sala climatizada con compactadora e integración BMS.
- **Sanitarios Públicos NBR 9050:** Cabinas universales PMR de $2,00 \times 2,20\text{ m}$.

---

### 3. Plantas Tipo Residenciales por Torre (P01 a P18)

Las plantas residenciales (P01 a P18) se distribuyen entre las **3 Torres independientes**, optimizando la orientación solar, la ventilación cruzada y las vistas perimetrales.

#### 3.1 Criterios de Diseño por Torre
- **Tipologías:** Departamentos de 1, 2 y 3 dormitorios.
- **Núcleos Verticales:** Cada torre dispone de su propio núcleo de circulación vertical (ascensores + escalera presurizada).
- **Aislamiento Acústico (NBR 15575):** Muros divisorios de H°A° para cumplimiento de confort acústico.

---

### 4. Planta de Azotea Técnica & Amenities

La planta de azotea contempla los servicios técnicos y las áreas de esparcimiento integradas para los residentes.

#### 4.1 Desglose de Amenities & Áreas Técnicas
- **Piscina Descubierta:** Losa maciza de H°A° reforzada contra punzonamiento y peso de agua.
- **SUM / Salón de Usos Múltiples:** Equipado con parrilla y servicios.
- **Gimnasio & Solárium:** Espacios de acondicionamiento físico y recreación.
- **Salas de Máquinas de Ascensores & Tanques Elevados:** Ubicados sobre los núcleos de circulación vertical.



