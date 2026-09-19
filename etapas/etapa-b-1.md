# B.1 — Programa y Organización Funcional

> **Etapa B › Sub-etapa 1** · **Tareas:** 4 · **Estado:** 🔴 En Re-planificación (diseño de subsuelos y torres ANULADO — ver nota)  
> ⚠️ **NOTA (2026-09-19):** Las distribuciones espaciales, el diseño de subsuelos, el perfil volumétrico y el layout de todas las plantas de torre han sido declaradas **obsoletas** y deben rediseñarse desde cero. **Lo único válido de esta sub-etapa** es: `§2.2 Zonificación Detallada de Planta Baja` (imagen `figura_2_1_zonificacion_planta_baja.png` — distribución funcional de PB con 3 torres diferenciadas cuyos subsuelos abarcan la huella completa de $3.145\\text{ m}^2$ directamente). **Todo lo demás — incluyendo §2.1 Perfil Volumétrico, cuadro de áreas, núcleos, cocheras y evacuación — está ANULADO.**  
> Normativa: MCDE ([Ord. M. 003/2026 J.M. Art. 3°, 4°, 5°, 6° y 7°](visor_ordenanzas.html?id=3693) — Uso Residencial Mixto, Lote Mínimo 3.000m², IOS desde Subsuelo y Fachadas No Espejadas; [Ord. 011/1994](visor_ordenanzas.html?id=3146); [Ord. 038/1999 PCI](visor_ordenanzas.html?id=3123)) · Ley N° 3966/2010 Orgánica Municipal · ABNT NBR 9050 · ABNT NBR 9077 · ISO 4190 · Neufert

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task B1.1:** ⚠️ *PENDIENTE — REDISEÑO REQUERIDO.* Definir el cuadro de áreas maestro por uso y nivel (Subsuelos S1-S3, PB comercial, 3 Torres Residenciales P01-P18, Azotea) con la nueva configuración de **3 torres independientes** cuyos subsuelos se integran directamente en la huella total de $3.145\text{ m}^2$. Incluir matriz de compatibilidad estructural avanzada.
- [ ] **Task B1.2:** ⚠️ *PENDIENTE — REDISEÑO REQUERIDO.* Dimensionar y validar los núcleos de circulación vertical de H°A° para la nueva distribución de **3 torres** (cantidad, posición y dimensiones a redefinir en Etapa B re-diseño), verificando su rol como pantallas principales de rigidez eólica ($V_0 = 45\text{ m/s}$).
- [ ] **Task B1.3:** ⚠️ *PENDIENTE — REDISEÑO REQUERIDO.* Zonificar recintos de Planta Baja para la nueva distribución con 3 torres. El layout de Lobby, Locales Comerciales, Sanitarios, BMS/Admin, RSU y rampas debe rehacerse desde cero según la nueva morfología.
- [ ] **Task B1.4:** ⚠️ *PENDIENTE — REDISEÑO REQUERIDO.* Rediseñar el esquema de evacuación y medios de escape (PCI) para la nueva configuración de 3 torres y la nueva distribución de subsuelos. Recalcular dotación de cocheras.

---

### Decisiones Tomadas — Re-planificación Arquitectónico-Estructural Avanzada

| Fecha | Decisión Proyectual | Fundamento Técnico & Normativo | Estado |
|---|---|---|---|
| 2026-09-19 | **Zonificación de Planta Baja** | Imagen `figura_2_1_zonificacion_planta_baja.png` — distribución funcional de PB con 3 torres y subsuelos integrando huella completa $3.145\text{ m}^2$. | ✅ **ÚNICO ÍTEM VÁLIDO** |
| 2026-09-19 | **Compatibilidad Estructural Flexible por Nivel** | `AGENTS.md §6.2 y §7`. | ❌ **ANULADO** — Redefinir para nueva morfología de 3 torres |
| 2026-09-19 | **Huella PB ($3.145\text{ m}^2$) y FOS/FOT** | FOS real = 41,28% ≤ 70%. FOT real = 3,97 ≤ 4,00. | ⏳ Valores numéricos válidos — reconfirmar con nuevo programa |
| 2026-09-19 | **Perfil Volumétrico (diseño viejo — §2.1)** | Imagen `figura_2_2_volumetria_y_perfil_edificio.png` — 1 única torre. | ❌ **ANULADO** — Rehacerlo para 3 torres |
| 2026-09-19 | **Distribución de Departamentos (diseño viejo — 1 torre 48×30m)** | 108 Dptos (6 dptos/piso), Planta Tipo $1.440\text{ m}^2$. | ❌ **ANULADO** — Rediseñar con 3 torres |
| 2026-09-19 | **Transición Escalonada de Pilares (diseño viejo)** | S1-PB: 90×90cm → P01-P06: 80×80cm → P07-P12: 70×70cm → P13-P18: 60×60cm. | ❌ **ANULADO** — Depende del nuevo layout |
| 2026-09-19 | **Vigas de Transferencia / Apeo en PB (diseño viejo)** | Vigas 80×120cm en cota +4,00m. | ❌ **ANULADO** — Depende del nuevo layout |
| 2026-09-19 | **Núcleos H°A° — cantidad y posición (diseño viejo)** | 2 núcleos gemelos rotados 90° (7×9m). | ❌ **ANULADO** — Redefinir en nuevo diseño |
| 2026-09-19 | **Layout Subsuelos S1-S3 (diseño viejo)** | 270 plazas totales (90/nivel, módulo 2,50×5,00m). | ❌ **ANULADO** — Rediseñar integrando 3 torres |
| 2026-09-19 | **Evacuación y Medios de Escape (diseño viejo)** | Recorrido máximo ≤ 28,40m ([Ord. 038/1999 J.M.](visor_ordenanzas.html?id=3123)). | ❌ **ANULADO** — Recalcular con nueva distribución |

---

### Archivos de Referencia y Documentación Generada

| Archivo | Descripción | Estado |
|---|---|---|
| `00_GESTION_DE_PROYECTO/ROADMAP_TESIS_300_PAGINAS.md` | Hoja de ruta académica de la tesis | Actualizado |
| `07_KNOWLEDGE_BASE/.../3693_ordenanza-m-n003-2026-jm.md` | Texto completo verificado de la Ord. M. 003/2026 J.M. | Verificado |
| `etapas/img/figura_2_1_zonificacion_planta_baja.png` | Figura 2.1: Zonificación de Planta Baja Comercial ($3.145\text{ m}^2$) | ✅ Generado (Único Válido) |
| `etapas/img/figura_2_2_volumetria_y_perfil_edificio.png` | Figura 2.2: Perfil Volumétrico y Relación de Plantas (18P + 3 Subsuelos) | ❌ Anulado |
| `etapas/img/figura_2_3_planta_tipo_residencial.png` | Figura 2.3: Planta Tipo Residencial ($1.440\text{ m}^2$) | ❌ Anulado |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

> ⚠️ **AVISO DE RE-PLANIFICACIÓN (2026-09-19):** Salvo la **Sección 2.2 (Zonificación Detallada de Planta Baja)**, los contenidos numéricos y esquemáticos de este borrador académico (§1, §2.1, §3, §4 y §5) pertenecen al **prototipo anterior de una única torre de 48×30m y 108 dptos**. Dichas secciones quedan **ANULADAS / PENDIENTES DE RE-DISEÑO** para la nueva configuración de **3 torres independientes** sobre la huella completa de $3.145\text{ m}^2$.

---

### 1. Cuadro de Áreas Maestro, Desglose por Uso y Compatibilidad Estructural por Nivel

> ❌ **[ANULADO — DISEÑO ANTERIOR DE 1 TORRE]** *Los valores numéricos, la cantidad de plantas tipo de 1.440m² y las transiciones de pilares corresponden a la torre única previa y serán recalculados para las 3 torres.*

El edificio mixto de 18 pisos y 3 subsuelos se emplaza sobre un terreno de **$7.618,49\text{ m}^2$** en Ciudad del Este (UTM Zona 21J). El anteproyecto contempla una superficie construida total acumulada de **$39.700,00\text{ m}^2$** sobre rasante y **$9.435,00\text{ m}^2$** bajo rasante en 3 subsuelos (exentos del cómputo FOT según Art. 226 de la Ley N° 3966/2010 Orgánica Municipal).

#### 1.1 Matriz de Superficies y Transición Estructural por Nivel *(Anulado / A Recalcular)*

| Nivel / Planta | Cota (m) | Altura Libre (m) | Función Principal / Programa | Área Construida (m²) | Área FOT (m²) | Sección Pilares H°A° | Sistema de Entrepiso & Transición |
|---|---|---|---|---|---|---|---|
| **Subsuelo 3 (S3)** | -10.50 | 3.10 | Estacionamiento (90 autos/18 motos), Depósitos & PTAR Estanca | 3.145,00 | 0,00 *(Exento)* | Muros contención $30\text{cm}$ + Pilares $90 \times 90\text{ cm}$ | Platea cimentación en basalto $q_{\text{adm}}=300\text{ kN/m}^2$ + Losa H=45cm |
| **Subsuelo 2 (S2)** | -7.00 | 3.10 | Estacionamiento (90 autos/15 motos) & Depósitos Privados | 3.145,00 | 0,00 *(Exento)* | Pilares $90 \times 90\text{ cm}$ | Losa nervada bidireccional H=45cm con casetones recuperables |
| **Subsuelo 1 (S1)** | -3.50 | 3.20 | Estacionamiento (90 autos/15 motos), ANDE 1.000kVA, Genset, Cisterna 60m³ | 3.145,00 | 0,00 *(Exento)* | Pilares $90 \times 90\text{ cm}$ | Losa nervada H=45cm + Ábacos refuerzo punzonamiento |
| **Planta Baja (PB)** | +0.00 | 4.00 | Lobby Residencial ($250\text{m}^2$), 3 Locales Comerciales ($1.850\text{m}^2$), RSU, BMS, Rampa | 3.145,00 | 3.145,00 | Pilares $90 \times 90\text{ cm}$ (Perímetro) | **Vigas de Transferencia H°A° ($80 \times 120\text{ cm}$)** en cota +4.00m |
| **Pisos P01 a P06** | +4.00 a +20.75 | 3.00 c/u | Residencial (6 plantas tipo × 1.440 m² = 36 dptos) | 8.640,00 | 8.640,00 | **Pilares $80 \times 80\text{ cm}$** | Losa nervada bidireccional H=35cm (casetón 25cm + capa 10cm) |
| **Pisos P07 a P12** | +24.10 a +40.85 | 3.00 c/u | Residencial (6 plantas tipo × 1.440 m² = 36 dptos) | 8.640,00 | 8.640,00 | **Pilares $70 \times 70\text{ cm}$** | Losa nervada bidireccional H=35cm + Vigas de borde $25 \times 50\text{ cm}$ |
| **Pisos P13 a P18** | +44.20 a +60.95 | 3.00 c/u | Residencial (6 plantas tipo × 1.440 m² = 36 dptos) | 8.640,00 | 8.640,00 | **Pilares $60 \times 60\text{ cm}$** | Losa nervada H=35cm + Balcones en voladizo de 1,50 m |
| **Azotea Técnica** | +64.30 | 3.50 | Amenities (Piscina 8×16m, SUM 150m², Gym) + Salas Máquinas | 1.200,00 | 1.200,00 | Pilares $60 \times 60\text{ cm}$ | Losa maciza de piscina $H=30\text{ cm}$ + Losa nervada H=35cm |
| **TOTALES** | **-10.50 a +68.80** | **—** | **Edificio Mixto 18P + 3 Subsuelos (108 Dptos / 270 Cocheras)** | **39.700,00** | **30.265,00** | **Optimización Escalonada** | **Análisis Estructural Complejo Avanzado** |

---

#### 1.2 Verificación de Indicadores Urbanísticos CDE

1. **Factor de Ocupación del Suelo (FOS):**
   - **Límite Normativo Máximo ([Ord. 011/1994 Art. 3°](visor_ordenanzas.html?id=3146)):** $FOS_{\text{máx}} = 0,70 \implies A_{\text{huella, máx}} = 0,70 \times 7.618,49\text{ m}^2 = \mathbf{5.332,94\text{ m}^2}$.
   - **Huella Proyectada en Planta Baja:** Rectángulo inscripto de $85,00\text{ m} \times 37,00\text{ m} = \mathbf{3.145,00\text{ m}^2}$.
   - **Ocupación Real:**
     $$FOS_{\text{real}} = \frac{3.145,00\text{ m}^2}{7.618,49\text{ m}^2} = \mathbf{0,4128 \quad (41,28\%)} \le 70,00\% \quad \text{(CUMPLE RIGUROSAMENTE)}$$

2. **Factor de Ocupación Total (FOT):**
   - **Límite Normativo Máximo:** $FOT_{\text{máx}} = 4,0 \implies A_{\text{construible, máx}} = 4,0 \times 7.618,49\text{ m}^2 = \mathbf{30.473,96\text{ m}^2}$.
   - **Exención Legal de Subsuelos:** Los 3 subsuelos ($9.435,00\text{ m}^2$) se destinan exclusivamente a estacionamientos y locales técnicos sin permanencia humana, quedando exentos del cómputo FOT conforme al Art. 226 de la Ley N° 3966/2010 Orgánica Municipal y ordenanzas de CDE.
   - **Superficie Computable sobre Rasante *(A Recalcular)*:** $\text{PB} (3.145,00\text{ m}^2) + \text{P01-P18} (18 \times 1.440,00\text{ m}^2 = 25.920,00\text{ m}^2) + \text{Azotea} (1.200,00\text{ m}^2) = \mathbf{30.265,00\text{ m}^2}$.
   - **Conclusión FOT:**
     $$FOT_{\text{real}} = \frac{30.265,00\text{ m}^2}{7.618,49\text{ m}^2} = \mathbf{3,97} \le 4,00 \quad \text{(CUMPLE CON HOLGURA DE } 208,96\text{ m}^2\text{)}$$

---

### 2. Organización Funcional y Esquemas Gráficos

#### 2.1 Perfil Volumétrico y Relación de Plantas *(Anulado — Prototipo 1 Torre)*

> ❌ **[ANULADO]** *La Figura 2.2 corresponde al perfil volumétrico de una sola torre continua de 48×30m. Debe reemplazarse por el nuevo esquema tridimensional de 3 torres independientes.*

![Figura 2.2: Perfil Volumétrico y Relación de Plantas — Edificio 18P + 3 Subsuelos](img/figura_2_2_volumetria_y_perfil_edificio.png)

#### 2.2 Zonificación Detallada de Planta Baja ($3.145,00\text{ m}^2$) — ✅ ÚNICO ÍTEM VÁLIDO

> ✅ **[VÁLIDO Y ADOPTADO]** *Esta zonificación contempla la Planta Baja comercial de $3.145\text{ m}^2$ articulando los accesos a las **3 torres diferenciadas**, con los 3 subsuelos abarcando la huella completa.*

![Figura 2.1: Planta Baja Comercial y de Servicios (3.145,00 m²)](img/figura_2_1_zonificacion_planta_baja.png)

---

### 3. Programa de Departamentos y Cuantificación de Estacionamientos *(Anulado — Prototipo 1 Torre)*

> ❌ **[ANULADO — DISEÑO ANTERIOR DE 1 TORRE DE 108 DPTOS]** *El programa de departamentos de planta única de 1.440m² y el cálculo de cocheras asociado corresponden al prototipo viejo de 1 sola torre y quedan anulados para ser re-desarrollados según las 3 torres.*

#### 3.1 Programa de la Torre Residencial *(Diseño Viejo: 108 Departamentos en 1 Torre)*

![Figura 2.3: Planta Tipo Residencial (P01 a P18) — Huella 1.440,00 m² (ANULADO)](img/figura_2_3_planta_tipo_residencial.png)

En la Torre Residencial ($P01$ a $P18$ prototipo 1 torre), cada planta tipo de **$1.440,00\text{ m}^2$** se distribuía en:
- **Áreas Comunes y Núcleos ($180,00\text{ m}^2\text{/piso}$):** Antecámaras presurizadas, hall de ascensores, 2 núcleos H°A° ($126\text{ m}^2$) y ductos técnicos.
- **Área Útil Vendible de Departamentos ($1.260,00\text{ m}^2\text{/piso}$):**
  - **2 Departamentos de 3 Dormitorios ($140,00\text{ m}^2$ útiles c/u):** Suite principal + 2 dormitorios secundarias, living-comedor, cocina, área de servicio y balcón con parrilla.
  - **2 Departamentos de 2 Dormitorios ($100,00\text{ m}^2$ útiles c/u):** Suite + 1 dormitorio, living-comedor y balcón.
  - **2 Departamentos de 1 Dormitorio / Executive Suite ($70,00\text{ m}^2$ útiles c/u):** Suite, kitchenette y balcón.
- **Total por Edificio:** 18 pisos $\times 6\text{ dptos/piso} = \mathbf{108\text{ Departamentos}}$.

#### 3.2 Cálculo de Requerimiento de Cocheras *(Prototipo Viejo)*
- **Demanda Residencial:**
  $$N_{\text{autos, res}} = 108 \text{ dptos} \times 1,5 \frac{\text{autos}}{\text{dpto}} = \mathbf{162\text{ cocheras}}$$
- **Demanda Comercial (Planta Baja):**
  Normativa: Ord. 011/1994 CDE (1 módulo de cochera por cada $75,00\text{ m}^2$ de superficie comercial neta de $1.850,00\text{ m}^2$).
  $$N_{\text{autos, com}} = \frac{1.850,00\text{ m}^2}{75,00\text{ m}^2\text{/auto}} = \mathbf{24,67 \approx 25\text{ cocheras}}$$
- **Demanda Total Requerida:**
  $$N_{\text{total, req}} = 162 + 25 = \mathbf{187\text{ cocheras}}$$

#### 3.3 Verificación de Capacidad en Subsuelos ($S1, S2, S3$) *(Prototipo Viejo)*
- **Área Bruta de Subsuelos:** 3 niveles $\times 3.145,00\text{ m}^2 = 9.435,00\text{ m}^2$.
- **Área Neta de Maniobras y Parqueo por Nivel:** $\sim 2.475,00\text{ m}^2$ (tras descontar muros periféricos de $30\text{ cm}$, núcleos $126\text{ m}^2$, rampas $15\%$ y PTAR $120\text{ m}^2$ en S3).
- **Rendimiento por Subsuelo:** Módulo normalizado de $2,50\text{ m} \times 5,00\text{ m}$ con pasillos de $6,00\text{ m} \implies 90\text{ plazas por subsuelo}$.
- **Capacidad Total Proyectada:**
  $$N_{\text{disponible}} = 3 \text{ subsuelos} \times 90 \text{ plazas} = \mathbf{270\text{ cocheras}}$$
- **Evaluación de Suficiencia:**
  $$N_{\text{disponible}} (270) \ge N_{\text{requerida}} (187) \quad \mathbf{(\text{CUMPLE HOLGADAMENTE CON } +83 \text{ PLAZAS EXTRA FORMA ADICIONAL})}$$

---

### 4. Rigidez Lateral de Núcleos Estructurales de H°A° *(Anulado — Prototipo 2 Núcleos)*

> ❌ **[ANULADO]** *La disposición de 2 núcleos gemelos rotados correspondía a la planta tipo de 1 sola torre. En el nuevo modelo se definirán los núcleos adecuados para cada una de las 3 torres.*

#### 4.1 Rigidez Lateral Eólica y Desacoplamiento de Pilares
- **Absorción de Cortante Basal:** Los núcleos actuarán como voladizos verticales empotrados en la platea de fundación en basalto. Absorberán la mayor parte del cortante eólico total ($V_0 = 45\text{ m/s}$), limitando las derivas laterales ($\Delta/H \le 1/500$).
- **Tráfico Vertical de Ascensores (ABNT NBR 5665 / ISO 4190):** A redefinir por torre.

---

### 5. Esquema de Evacuación y Medios de Escape (PCI — Ord. 038/1999 J.M.) *(A Recalcular)*

> ❌ **[ANULADO]** *El esquema de evacuación se calculaba para 1 solo pasillo central. Se rediseñará para los recorridos de las 3 torres en el nuevo proyecto.*

- **Distancia Máxima de Recorrido:** A recalcular según layout final de las 3 torres ($\le 30,00\text{ m}$ conforme a [Ord. 038/1999 J.M.](visor_ordenanzas.html?id=3123)).
- **Tiempo Estimado de Evacuación Total:** A recalcular para la ocupación y núcleos de las 3 torres.

