# B.3 — Cortes, Fachadas y Detalles Constructivos

> **Etapa B › Sub-etapa 3** · **Tareas:** 4 · **Estado:** ⏳ En Desarrollo (Cortes, Elevaciones y Envolventes de 3 Torres)  
> Archivos fuente: `01_WIP/01.01_ARQ/` · Autodesk Revit 2024 · MCDE ([Ord. M. 003/2026 Art. 7°](visor_ordenanzas.html?id=3693) — Fachadas No Espejadas; [Ord. 011/1994](visor_ordenanzas.html?id=3146))

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task B3.1:** Trazar los cortes verticales principales para las **3 torres**, detallando cotas absolutas, alturas de entrepiso y soluciones de transición estructural.
- [ ] **Task B3.2:** Diseñar las elevaciones de las fachadas (Norte, Sur, Este, Oeste) para las 3 torres con vigas de borde *spandrel* y protección solar pasiva, aplicando la [Ord. M. 003/2026 Art. 7°](visor_ordenanzas.html?id=3693).
- [ ] **Task B3.3:** Incorporar especificaciones de envolvente (DVH Low-E neutro, *brise-soleil*) para las 3 torres, cumpliendo la [Ord. M. 003/2026 J.M. Art. 7°](visor_ordenanzas.html?id=3693) (prohibición de vidrios espejados).
- [ ] **Task B3.4:** Desarrollar detalles constructivos de encuentros: losa nervada-fachada, impermeabilización de azotea y subsuelos unificados, y juntas de dilatación entre torres.

---

### Decisiones Tomadas

| Fecha | Decisión Proyectual | Fundamento Técnico & Normativo | Estado |
|---|---|---|---|
| 2026-09-19 | **Definición de Alturas y Relación Vertical** | Cota $-10.50\text{ m}$ en S3 a nivel de coronamiento en azotea técnica. | ⏳ En desarrollo |
| 2026-09-19 | **Prohibición de Cristales Espejados** | [Ord. M. 003/2026 J.M. Art. 7°](visor_ordenanzas.html?id=3693) (Protección de avifauna y prevención de deslumbramientos). | ✅ Adoptado |
| 2026-09-19 | **Vidriado Adoptado (DVH Low-E)** | Doble Vidriado Hermético incoloro neutro ($6\text{mm} + 12\text{mm aire} + 6\text{mm}$), transmisión luminosa $\ge 65\%$, reflectancia $< 12\%$. | ✅ Adoptado |
| 2026-09-19 | **Juntas de Dilatación Térmica** | Junta vertical continua con sellador elastomérico de poliuretano entre cuerpos de edificación. | ⏳ En desarrollo |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Definición de Alturas y Relación Vertical

La relación vertical del conjunto contempla la cota de fundación de los 3 subsuelos en **$-10,50\text{ m}$** sobre el basamento rocoso, el nivel de vereda en **$+0,00\text{ m}$** (Planta Baja comercial) y las alturas libres de las **3 Torres Residenciales** (P01 a P18) hasta la Azotea Técnica.

---

### 2. Envolvente Térmica y Criterios Facádicos (Cumplimiento Ord. M. 003/2026 J.M.)

En cumplimiento estricto del **[Art. 7° de la Ordenanza Municipal M. N° 003/2026 J.M.](visor_ordenanzas.html?id=3693)**, **queda expresamente prohibido el uso de fachadas con efecto espejo o altamente reflectantes** en edificaciones en altura, con el objetivo de proteger la avifauna del ecosistema urbano y evitar deslumbramientos.

```
                  ┌──────────────────────────────────────────────────────────┐
                  │ PARED EXTERIOR / VIGA SPANDREL DE H°A° (25 × 50 cm)     │
                  └────────────────────────────┬─────────────────────────────┘
                                               │
               ┌───────────────────────────────┴──────────────────────────────┐
               │ ABERTURA DVH NEUTRA LOW-E (NO ESPEJADA)                      │
               │ Glass 6mm Incoloro + Cámara Aire 12mm + Glass 6mm Low-E      │
               │ Transmisión Luminosa TL = 68% · Factor Solar g = 0,38        │
               └───────────────────────────────┬──────────────────────────────┘
                                               │
               ┌───────────────────────────────┴──────────────────────────────┐
               │ PROTECCIÓN SOLAR PASIVA (BRISE-SOLEIL)                       │
               │ Parasoles horizontales de aluminio extruido anodizado natural│
               │ Balcones corridos con voladizo de 1,50 m                      │
               └──────────────────────────────────────────────────────────────┘
```

#### 2.1 Especificaciones de Vidrio y Parasoles Pasivos
- **Carpinterías Exteriores:** Perfiles de aluminio con Ruptura de Puente Térmico (RPT).
- **Vidriado Adoptado:** Doble Vidriado Hermético (DVH) incoloro neutro con capa de control solar **Low-E** en cara 2. Reflectancia lumínica exterior $R_e \le 11\%$ (Cumple el límite no espejado del Art. 7°).
- **Protección Solar Pasiva (Brise-Soleil):** Parasoles horizontales orientables de aluminio extruido sobre fachadas expuestas, calculados para bloquear la radiación solar directa.

---

### 3. Detalles Constructivos Críticos de Envolvente e Impermeabilización

1. **Encuentro Losa Nervada — Viga Spandrel de Fachada:**
   - La losa nervada ($H = 35\text{ cm}$) remata perimetralmente en una viga de borde (*spandrel beam*) de $25 \times 50\text{ cm}$, la cual absorbe la torsión del voladizo del balcón ($1,50\text{ m}$) y rigidiza el plano exterior de la fachada.

2. **Impermeabilización de Azotea Técnica & Piscina:**
   - Membrana asfáltica de $4\text{ mm}$ modificada con polímeros SBS sobre imprimación bituminosa, protegida térmicamente con planchas de Poliestireno Expandido (EPS) de $50\text{ mm}$ de alta densidad ($30\text{ kg/m}^3$) y carpeta de mortero armado de protección mecánica.
   - Vaso de piscina impermeabilizado mediante revestimiento cementicio elástico bicomponente con malla de fibra de vidrio de refuerzo.

3. **Impermeabilización Estanca de Subsuelos (S1-S3):**
   - Muros pantalla de H°A° ($e = 30\text{ cm}$) tratados con aditivo cristalizante por capilaridad en la masa de hormigón + geomembrana de HDPE exterior y geodren con geotextil no tejido para conducción de aguas de infiltración hacia la EBAR en S3.
