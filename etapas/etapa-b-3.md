# B.3 — Cortes, Fachadas y Detalles Constructivos

> **Etapa B › Sub-etapa 3** · **Tareas:** 4 · **Estado:** 🟢 Completado (2026-09-19)  
> Archivos fuente: `01_WIP/01.01_ARQ/` · Autodesk Revit 2024 · MCDE ([Ord. M. 003/2026 Art. 7°](visor_ordenanzas.html?id=3693) — Fachadas No Espejadas; [Ord. 011/1994](visor_ordenanzas.html?id=3146))

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [x] **Task B3.1:** Trazar los cortes verticales principales (Corte AA por núcleos de H°A° y Corte BB por Megastore y departamentos), detallando alturas y cotas absolutas.
- [x] **Task B3.2:** Diseñar las elevaciones de las 4 fachadas (Norte, Sur, Este, Oeste) con vigas de borde *spandrel* y protección solar pasiva.
- [x] **Task B3.3:** Incorporar las especificaciones de envolvente en cumplimiento directo de la **[Ord. M. 003/2026 J.M. Art. 7°](visor_ordenanzas.html?id=3693)** (Prohibición de vidrios espejados / Adopción de cristal Low-E neutro + *brise-soleil*).
- [x] **Task B3.4:** Desarrollar detalles constructivos de encuentros (losa nervada-fachada, impermabilización de azotea y subsuelos, juntas de dilatación).

---

### Decisiones Tomadas

| Fecha | Decisión Proyectual | Fundamento Técnico & Normativo |
|---|---|---|
| 2026-09-19 | **Altura Total del Edificio** | $+64,30\text{ m}$ a nivel de losa de azotea y $+68,80\text{ m}$ a coronamiento de caseta de máquinas. |
| 2026-09-19 | **Prohibición de Cristales Espejados** | [Ord. M. 003/2026 J.M. Art. 7°](visor_ordenanzas.html?id=3693) (Protección de avifauna y prevención de deslumbramientos). |
| 2026-09-19 | **Vidriado Adoptado (DVH Low-E)** | Doble Vidriado Hermético incoloro neutro ($6\text{mm} + 12\text{mm aire} + 6\text{mm}$) con transmisión luminosa $\ge 65\%$ y reflectancia $< 12\%$. |
| 2026-09-19 | **Juntas de Dilatación Térmica** | Junta vertical continua de $30\text{ mm}$ con sellador elastomérico de poliuretano en encuentros de bloques. |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Definición de Alturas, Niveles Verticales y Transición Estructural

La relación vertical del edificio establece una cota de fundaciones en **$-10,50\text{ m}$** y una altura total de coronamiento de **$+68,80\text{ m}$** sobre el nivel de vereda ($+0,00\text{ m}$).

```
Cota (m)    Nivel / Piso         Altura  Sección Pilar   Esquema de Transición Estructural
+68.80 m ── Caseta de Máquinas ── 4.50m ── [60×60 cm] ─── Tanque Elevado 30m³ + Motores Elevadores
+64.30 m ── Azotea Técnica ───── 3.50m ── [60×60 cm] ─── Amenities (Piscina H=30cm + SUM 150m²)
+60.95 m ── Piso 18 Residencial ─ 3.35m ── [60×60 cm] ─── Losa Nervada H=35cm (Casetón 25cm + Capa 10cm)
+44.20 m ── Piso 13 Residencial ─ 3.35m ── [60×60 cm] ─── Transición a Secciones de 60×60 cm
+40.85 m ── Piso 12 Residencial ─ 3.35m ── [70×70 cm] ─── Transición a Secciones de 70×70 cm
+24.10 m ── Piso 07 Residencial ─ 3.35m ── [70×70 cm] ─── Transición a Secciones de 70×70 cm
+20.75 m ── Piso 06 Residencial ─ 3.35m ── [80×80 cm] ─── Transición a Secciones de 80×80 cm
+04.00 m ── Piso 01 Residencial ─ 3.35m ── [80×80 cm] ─── VIGAS DE TRANSFERENCIA H°A° (80×120 cm)
+00.00 m ── PLANTA BAJA ───────── 4.00m ── [90×90 cm] ─── Megastore 1.200m² Libre de Pilares + Lobby
-03.50 m ── Subsuelo 1 (S1) ───── 3.20m ── [90×90 cm] ─── Cocheras + ANDE 1.000kVA + Cisterna 60m³
-07.00 m ── Subsuelo 2 (S2) ───── 3.10m ── [90×90 cm] ─── Cocheras + Baúleras Privadas
-10.50 m ── Subsuelo 3 (S3) ───── 3.10m ── Muro 30cm ──── Platea de Fundación en Basalto (qadm=300kPa)
```

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
- **Carpinterías Exteriores:** Perfiles de aluminio con Ruptura de Puente Térmico (RPT) serie aluar/perfilco.
- **Vidriado Adoptado:** Doble Vidriado Hermético (DVH) incoloro neutro con capa de control solar **Low-E** en cara 2. Reflectancia lumínica exterior $R_e \le 11\%$ (Cumple con creces el límite no espejado del Art. 7°).
- **Protección Solar Pasiva (Brise-Soleil):** Parasoles horizontales orientables de aluminio extruido sobre fachadas Este y Oeste, calculados para bloquear la radiación solar directa con ángulo de incidencia $\beta > 35^\circ$.

---

### 3. Detalles Constructivos Críticos de Envolvente e Impermeabilización

1. **Encuentro Losa Nervada — Viga Spandrel de Fachada:**
   - La losa nervada ($H = 35\text{ cm}$) remata perimetralmente en una viga de borde (*spandrel beam*) de $25 \times 50\text{ cm}$, la cual absorbe la torsión del voladizo del balcón ($1,50\text{ m}$) y rigidiza el plano exterior de la fachada.

2. **Impermeabilización de Azotea Técnica & Piscina:**
   - Membrane asfáltica de $4\text{ mm}$ de espesor modificada con polímeros SBS sobre imprimación bituminosa, protegida térmicamente con planchas de Poliestireno Expandido (EPS) de $50\text{ mm}$ de alta densidad ($30\text{ kg/m}^3$) y carpeta de mortero armado de protección mecánica.
   - Vaso de piscina ($8 \times 16\text{ m}$) impermeabilizado mediante revestimiento cementicio elástico bicomponente con malla de fibra de vidrio de refuerzo.

3. **Impermeabilización Estanca de Subsuelos (S1-S3):**
   - Muros pantalla de H°A° ($e = 30\text{ cm}$) tratados con aditivo cristalizante por capilaridad en la masa de hormigón + geomembrana de HDPE exterior y geodren con geotextil no tejido para conducción de aguas de infiltración hacia la EBAR en S3.
