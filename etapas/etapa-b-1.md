# B.1 — Programa y Organización Funcional

> **Etapa B › Sub-etapa 1** · **Tareas:** 4 · **Estado:** ⏳ En Desarrollo (Programa de 3 Torres + Subsuelos Unificados)  
> Normativa: MCDE ([Ord. M. 003/2026 J.M. Art. 3°, 4°, 5°, 6° y 7°](visor_ordenanzas.html?id=3693) — Uso Residencial Mixto, Lote Mínimo 3.000m², IOS desde Subsuelo y Fachadas No Espejadas; [Ord. 011/1994](visor_ordenanzas.html?id=3146); [Ord. 038/1999 PCI](visor_ordenanzas.html?id=3123)) · Ley N° 3966/2010 Orgánica Municipal · ABNT NBR 9050 · ABNT NBR 9077 · ISO 4190 · Neufert

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task B1.1:** Definir el cuadro de áreas maestro por uso y nivel (Subsuelos S1-S3, PB comercial, 3 Torres Residenciales P01-P18, Azotea) con la configuración de **3 torres independientes** cuyos subsuelos se integran directamente en la huella total de $3.145\text{ m}^2$. Incluir matriz de compatibilidad estructural avanzada.
- [ ] **Task B1.2:** Dimensionar y validar los núcleos de circulación vertical de H°A° para las **3 torres** (cantidad, posición y dimensiones por torre), verificando su rol como pantallas principales de rigidez eólica ($V_0 = 45\text{ m/s}$).
- [ ] **Task B1.3:** Zonificar recintos de Planta Baja para la distribución con 3 torres. Layout de Lobby, Locales Comerciales, Sanitarios, BMS/Admin, RSU y rampas.
- [ ] **Task B1.4:** Diseñar el esquema de evacuación y medios de escape (PCI) para la configuración de 3 torres y la distribución de subsuelos. Recalcular dotación de cocheras.

---

### Decisiones Tomadas — Organización Arquitectónico-Estructural

| Fecha | Decisión Proyectual | Fundamento Técnico & Normativo | Estado |
|---|---|---|---|
| 2026-09-19 | **Zonificación de Planta Baja** | Imagen `figura_2_1_zonificacion_planta_baja.png` — distribución funcional de PB con 3 torres y subsuelos integrando huella completa $3.145\text{ m}^2$. | ✅ Adoptado |
| 2026-09-19 | **Compatibilidad Estructural por Torre** | `AGENTS.md §6.2 y §7` — Grilla e inserción de núcleos H°A° coordinados para cada una de las 3 torres. | ⏳ En desarrollo |
| 2026-09-19 | **Huella PB ($3.145\text{ m}^2$) y FOS/FOT** | FOS real = 41,28% ≤ 70%. FOT real = 3,97 ≤ 4,00. | ✅ Verificado |

---

### Archivos de Referencia y Documentación Generada

| Archivo | Descripción | Estado |
|---|---|---|
| `00_GESTION_DE_PROYECTO/ROADMAP_TESIS_300_PAGINAS.md` | Hoja de ruta académica de la tesis | Actualizado |
| `07_KNOWLEDGE_BASE/.../3693_ordenanza-m-n003-2026-jm.md` | Texto completo verificado de la Ord. M. 003/2026 J.M. | Verificado |
| `05_RECURSOS/05.05_Scripts_Python/01_Geometria_Terreno/dibujar_zonificacion_b1.py` | Script Python generador de figuras vectoriales (300 DPI) | ✅ Creado |
| `etapas/img/figura_2_1_zonificacion_planta_baja.png` | Figura 2.1: Zonificación de Planta Baja Comercial ($3.145\text{ m}^2$) | ✅ Generado |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Cuadro de Áreas Maestro, Desglose por Uso e Indicadores Urbanísticos

El edificio mixto de 18 pisos y 3 subsuelos se emplaza sobre un terreno de **$7.618,49\text{ m}^2$** en Ciudad del Este (UTM Zona 21J). El anteproyecto contempla una superficie construida distribuida en 3 subsuelos bajo rasante (exentos del cómputo FOT según Art. 226 de la Ley N° 3966/2010 Orgánica Municipal), Planta Baja comercial unificada de $3.145,00\text{ m}^2$ y 3 Torres Residenciales independientes (P01 a P18).

#### 1.1 Verificación de Indicadores Urbanísticos CDE

1. **Factor de Ocupación del Suelo (FOS):**
   - **Límite Normativo Máximo ([Ord. 011/1994 Art. 3°](visor_ordenanzas.html?id=3146)):** $FOS_{\text{máx}} = 0,70 \implies A_{\text{huella, máx}} = 0,70 \times 7.618,49\text{ m}^2 = \mathbf{5.332,94\text{ m}^2}$.
   - **Huella Proyectada en Planta Baja:** Rectángulo inscripto de $85,00\text{ m} \times 37,00\text{ m} = \mathbf{3.145,00\text{ m}^2}$.
   - **Ocupación Real:**
     $$FOS_{\text{real}} = \frac{3.145,00\text{ m}^2}{7.618,49\text{ m}^2} = \mathbf{0,4128 \quad (41,28\%)} \le 70,00\% \quad \text{(CUMPLE RIGUROSAMENTE)}$$

2. **Factor de Ocupación Total (FOT):**
   - **Límite Normativo Máximo:** $FOT_{\text{máx}} = 4,0 \implies A_{\text{construible, máx}} = 4,0 \times 7.618,49\text{ m}^2 = \mathbf{30.473,96\text{ m}^2}$.
   - **Exención Legal de Subsuelos:** Los 3 subsuelos ($9.435,00\text{ m}^2$) se destinan exclusivamente a estacionamientos y locales técnicos sin permanencia humana, quedando exentos del cómputo FOT conforme al Art. 226 de la Ley N° 3966/2010 Orgánica Municipal y ordenanzas de CDE.
   - **Superficie Computable sobre Rasante:** A determinar en la cuantificación definitiva de las 3 torres ($\le 30.473,96\text{ m}^2$).

---

### 2. Organización Funcional y Esquemas Gráficos

#### 2.1 Zonificación Detallada de Planta Baja ($3.145,00\text{ m}^2$)

![Figura 2.1: Planta Baja Comercial y de Servicios (3.145,00 m²)](img/figura_2_1_zonificacion_planta_baja.png)

La Planta Baja ($3.145,00\text{ m}^2$) actúa como basamento comercial y de articulación peatonal y vehicular. Permite el acceso independiente a los vestíbulos de las **3 Torres Residenciales**, integrando locales comerciales frontales, áreas administrativas/BMS, servicios técnicos y rampas de acceso a los subsuelos unificados.

---

### 3. Programa de Torres Residenciales y Estacionamientos

#### 3.1 Esquema de Torres Residenciales
- **Configuración:** 3 Torres independientes proyectadas sobre el basamento de Planta Baja.
- **Distribución:** Niveles P01 a P18 dedicados a uso residencial con circulaciones verticales propias por torre.
- **Amenities & Azotea:** Espacios de esparcimiento en azotea técnica coordinados con los núcleos de cada torre.

#### 3.2 Cálculo de Cocheras en Subsuelos ($S1, S2, S3$)
- **Superficie por Subsuelo:** $3.145,00\text{ m}^2$ por nivel ($9.435,00\text{ m}^2$ totales en 3 subsuelos).
- **Criterio de Diseño:** Módulos normalizados de $2,50\text{ m} \times 5,00\text{ m}$ con pasillos de maniobra $W \ge 6,00\text{ m}$.
- **Locales Técnicos Subterráneos:** Subestación ANDE, Grupo Electrógeno, Cisterna PCI/Potable y PTAR estanca en S3 ([Ord. 030/2020 J.M.](visor_ordenanzas.html?id=2462)).

---

### 4. Rigidez Lateral y Núcleos Estructurales de H°A°

Para absorber los esfuerzos cortantes eólicos ($V_0 = 45\text{ m/s}$) y albergar las circulaciones verticales, cada una de las 3 torres contará con sus respectivos **núcleos estructurales de H°A° (pantallas de rigidización)**.

- **Absorción de Cortante Basal:** Los núcleos actuarán como voladizos verticales empotrados en la platea de fundación en basalto fresco ($q_{\text{adm}} = 300\text{ kN/m}^2$).
- **Tráfico Vertical (ABNT NBR 5665 / ISO 4190):** Ascensores dimensionados independientemente para el flujo de población de cada torre.

---

### 5. Esquema de Evacuación y Medios de Escape (PCI — Ord. 038/1999 J.M.)

- **Distancia Máxima de Recorrido:** Las rutas de evacuación en cada torre y en el basamento respetarán $d_{\text{máx}} \le 30,00\text{ m}$ conforme a la [Ord. 038/1999 J.M.](visor_ordenanzas.html?id=3123).
- **Compartimentación y Resistencia al Fuego:** Las cajas de ascensores y escaleras constituidas por muros de H°A° garantizan protección RF-180.
