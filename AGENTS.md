# AGENTS.md — Guía de Trabajo para Agentes de IA (Copilot BIM & Estructural)

> Punto de entrada **obligatorio** para cualquier agente que trabaje en este proyecto.
> Leer este archivo completo antes de responder, editar o crear archivos.
> Este proyecto NO es un repositorio de código convencional: es un **proyecto de tesis de grado de ingeniería civil con metodología BIM (ISO 19650)** de un edificio en altura de uso mixto (18P + 2 Subsuelos).

---

## 1. Contexto del Proyecto

- **Título del Trabajo:** Tesis de Grado en Ingeniería Civil — Diseño Estructural, Análisis Dinámico al Viento, Coordinación BIM y Presupuesto de un Edificio Mixto de 18 Pisos y 2 Subsuelos.
- **Alcance Físico:** Edificio de 18 plantas tipo residenciales (P01–P18) + Planta Baja comercial + 2 Subsuelos de cocheras (S1–S2) + Azotea Técnica y Amenities (Piscina + SUM). **Sin oficinas.**
- **Superficie Construida Total:** ~68.600 m² (Área por planta edificable: ~3.145 m²).
- **Ubicación del Terreno:** Ciudad del Este, Departamento de Alto Paraná, Paraguay (UTM Zona 21J).
- **Extensión Obligatoria Tesis:** Documento académico de **~200–300 PÁGINAS**. Ver `00_GESTION_DE_PROYECTO/ROADMAP_TESIS_300_PAGINAS.md`.
- **Enfoque Principal de Investigación:**
  1. **Ingeniería de Viento y Dinámica Estructural:** Análisis multinormativo comparativo (**NP 196:1991**, **NBR 6123:2023**, **ASCE 7-22**, **EN 1991-1-4 / Eurocódigo 1**).
  2. **Diseño Estructural en Hormigón Armado:** Sistema de losas nervadas/reticulares alivianadas bidireccionales + vigas de borde spandrel + pilares continuos + núcleos H°A° (pantallas).
  3. **Metodología BIM (ISO 19650):** Modelado disciplinar (LOD 300/350), CDE, federación 3D y Clash Detection en Navisworks.
  4. **Optimización Algorítmica (NSGA-II / Python):** Distribución de recintos interiores y departamentos.
  5. **Gestión de Proyecto (5D):** Presupuesto detallado (APU / CAPACO / CYPE) y cronograma de obra (Gantt 4D).
- **Idioma de Trabajo y Entregables:** Español técnico.

---

## 2. Estructura de Carpetas del CDE (ISO 19650)

| Carpeta | Rol ISO 19650 | Contenido y Reglas |
|---|---|---|
| `00_GESTION_DE_PROYECTO` | Gestión | BEP, estándares de proyecto, actas, presupuestos, ROADMAP |
| `01_WIP` | Work in Progress | Modelos y planos en trabajo (`01.01_ARQ` … `01.09_COORD`). **No publicar aquí finales.** |
| `02_SHARED` | Shared | Modelos federados NWD/IFC, informes de clash detection compartidos |
| `03_PUBLISHED` | Published | Entregables aprobados (planos PDF, memorias, presupuestos, visor web) |
| `04_ARCHIVED` | Archived | Historias de versiones superadas y documentación obsoleta |
| `05_RECURSOS` | Resources | Plantillas Revit 2024, familias, parámetros compartidos, scripts Python (`05.05_Scripts_Python`) |
| `06_ANEXOS_TESIS` | Thesis Output | Capítulos de tesis escritas en Word (`tesis/`) y anexos LaTeX (`anexo_calculo_latex/`) |
| `07_KNOWLEDGE_BASE` | Knowledge Base | Base de conocimiento acumulada: resúmenes normativos, tutoriales Revit y memorias |
| `etapas/` | Markdown Site | 57 archivos `.md` correspondientes a las Etapas A–P y sub-etapas para el visor web |

---

## 3. Nomenclatura de Archivos Obligatoria

Convención única e inviolable: `TESIS-[DISCIPLINA]-[NIVEL]-[TIPO]-[NUMERO]`

- **DISCIPLINA:** `ARQ`, `EST`, `SAN`, `ELE`, `INC`, `MEC`, `CLO`, `PLU`, `COORD`.
- **NIVEL:** `SUB2`, `SUB1`, `PB`, `P01`–`P18`, `AZ` (Azotea), `GEN` (General). *(SUB3 eliminado — edificio tiene 2 subsuelos)*
- **TIPO:** `M3` (Modelo 3D), `DR` (Plano 2D), `SC` (Tabla/Cómputo), `RP` (Reporte/Memoria), `CALC` (Cálculo), `SCRIPT` (Código).
- **NUMERO:** Correlativo de 3 dígitos (`001`, `002`, ...).

*Ejemplo:* `TESIS-EST-P05-M3-001.rvt` · Fuente completa: `00_GESTION_DE_PROYECTO/00.03_Estandares_del_Proyecto/NOMENCLATURA.md`.

---

## 4. Software y Entorno de Desarrollo

- **BIM Principal:** Autodesk Revit 2024 en **Inglés** (Build `24.3.60.12`).
  - Executable: `C:\Users\jvchi\CARPETAS\Autodesk\Autodesk 2024\Revit 2024\Revit.exe`.
  - Citar siempre comandos y cintas en inglés (`Create` > `Shared Parameter`).
- **Federación y Coordinación:** Autodesk Navisworks Manage 2024 / IFC4 Reference View.
- **Motor de Cálculo y Algoritmos:** Python 3.13 (Librerías: `DEAP`, `PyNiteFEA`, `matplotlib`, `numpy`, `pandas`).
- **Redacción de Tesis:** Microsoft Word (Pipeline `build_tesis.js` en Node.js) y MiKTeX LaTeX (Anexo de cálculo).
- **Servidor Web Local:** Python HTTP Server (`python -m http.server 8000`) para visualizar `index.html` y `visor.html`.

---

## 5. Regla de Oro de la Base de Conocimiento (`07_KNOWLEDGE_BASE`)

> **Ningún agente debe buscar dos veces lo mismo.**

Cuando se resuelva una duda técnica (normas, Revit, cálculo estructural):
1. **Investigar** mediante `websearch` / `webfetch` o archivos del proyecto.
2. **Redactar** un informe técnico paso a paso y guardarlo en `07_KNOWLEDGE_BASE`:
   - Revit → `07.01_Revit_HowTo/`
   - Flujos BIM → `07.02_BIM_Workflows/`
   - Cálculo estructural → `07.03_Analisis_Estructural/`
   - Normas → `07.04_Normativa_Resumen/`
   - Optimización → `07.05_Optimizacion_Algoritmica/`
3. Citar la ruta del archivo guardado en la respuesta.

---

## 6. Parámetros Maestros y Terreno (FUENTE DE VERDAD DE SITIO)

### 6.1 Datos Geográficos y Geometría del Terreno (UTM Zona 21J)

| Parámetro | Valor Definitivo |
|---|---|
| **Ubicación** | Ciudad del Este, Alto Paraná, Paraguay |
| **Superficie Bruta Terreno** | **7.618,49 m²** (Polígono P1-P2-P3-P4) |
| **Coordenadas UTM (WGS84)** | P1(737721.76, 7176185.26) · P2(737837.53, 7176203.96) · P3(737853.36, 7176246.13) · P4(737755.78, 7176281.93) |
| **Frente Principal P1→P2** | **117,27 m** (Declinación magnética CDE ≈ -14°) |
| **Vértice Agudo P1** | **61,44°** (zona no edificable / cuña frontal de jardín / acceso peatonal) |
| **Retiros Reglamentarios Adoptados** | **Frente: 3.0m · Fondo: 3.0m · Laterales: 2.0m** (hipótesis de tesis) |
| **Parámetros Urbanísticos** | **FOS = 0,70** (Área máx. huella = 5.332 m²) · **FOT = 4,0** (Área total construible sobre rasante = 30.474 m²) |
| **Rectángulo Edificable Inscripto** | **X: 2.5m → 87.5m / Y: 3.0m → 40.0m** (85.0m × 37.0m = 3.145 m² por planta) |

### 6.2 Definición de Niveles, Núcleos y Distribuciones (⏳ EN RE-DEFINICIÓN ARQUITECTÓNICA — ETAPA B)

> **ESTADO:** ⏳ *Todas las distribuciones espaciales anteriores quedan anuladas.* Se re-planificarán desde cero en la **Etapa B (Arquitectura Completa)**.

- **Niveles Base:** 2 Subsuelos (S1–S2) + PB Comercial + 18 Pisos Residenciales (P01–P18, sin oficinas) + Azotea.
- **Superficie de Subsuelos (Parámetro Maestro Congelado):** **4.922,66 m² bruta por nivel** ($S1$ y $S2$, total $9.845,32\text{ m}^2$ sin descontar PTAR, subestación ANDE ni áreas técnicas, exentos de FOT).
- **Alturas de Entrepiso (Parámetro Maestro Congelado):** Subsuelos S1–S2 = **3,50 m** total (libre: 3,05 m + losa 45 cm) · Pisos P01–P18 = **3,35 m** total (libre: 3,00 m + losa 35 cm) · PB = **4,50 m** (libre: 4,05 m + losa 45 cm).
- **Cotas de Nivel Definitivas:** SUB2 = **-7,00 m** · SUB1 = **-3,50 m** · PB = ±0,00 m · P01 = +4,50 m · P18 = +64,80 m · Azotea = +68,15 m (estimado).
- **Núcleos H°A° y Grilla:** La cantidad, posición, forma de los núcleos y la grilla de pilares se definirán en la Etapa B.
- **Distribución de Cocheras, PB, Planta Tipo y Amenities:** Se diseñarán desde cero en la Etapa B.

---

## 7. Sistema Estructural (⏳ EN RE-PLANIFICACIÓN — ETAPAS B y D)

- **Sistema de Entrepiso Propuesto:** Losas nervadas/reticulares alivianadas bidireccionales con casetones recuperables (propuesto por menor masa y costo material).
- **Grilla y Resistencia Lateral:** Se definirá la grilla continua y la posición de pantallas H°A° / pórticos para absorber las acciones de viento multinormativo (NP 196, NBR 6123, ASCE 7-22, EC1).

---

## 8. Sistema de Documentación Web (GitHub Pages & `visor.html`)

El proyecto dispone de una plataforma estática completa navegable desde la web o localmente:

- **Dashboard Principal (`index.html`):** Cronograma dinámico interactivo y checklists de tareas.
- **Visor Markdown (`visor.html`):** Visor con menú lateral desplegable en árbol (Etapas A–P y Sub-etapas A.1–P.2).
- **Carpeta `etapas/` (57 archivos `.md`):**
  - `etapa-a.md` … `etapa-p.md` (16 Índices de Etapa).
  - `etapa-a-1.md` … `etapa-p-2.md` (41 Sub-etapas estructuradas en **Gestión de Tareas** y **Borrador Académico de Tesis**).

---

## 9. Reglas Metodológicas para Agentes IA

1. **Rigor Técnico Imprescindible:** Todos los valores de resistencia ($f'_c = 30\text{ MPa}$, $f_y = 500\text{ MPa}$), cargas ($g_{total} = 7.25\text{ kN/m}^2$, $V_0 = 45\text{ m/s}$) y dimensiones deben mantenerse coherentes en todos los documentos (Word, LaTeX, Python y HTML).
2. **Estructura Canónica de Memorias de Cálculo (6 Apartados Obligatorios):**
   1. Memoria Descriptiva y Objetivos.
   2. Normativa Aplicable (NP 196, NBR 6123, ASCE 7-22, EC1, NBR 6118, ACI 318-19).
   3. Hipótesis de Carga y Acciones de Diseño.
   4. Propiedades de los Materiales.
   5. Modelado Matemático y Criterios de Análisis.
   6. Dimensionamiento y Verificación ELU/ELS.
3. **No alterar parámetros maestros ni decisiones de diseño congeladas.**
4. **Actualización del Dashboard Web (`index.html`):** Al completar tareas o sub-etapas, es **obligatorio** actualizar `index.html` cambiando la etiqueta del elemento HTML a `<label class="task done">` y agregando el atributo `checked` en el `<input type="checkbox" data-id="..." checked>` correspondiente para mantener la sincronización visual del proyecto.
5. **Principio de Doble Capa Comunicativa (Rigor Técnico + Claridad Divulgativa):** Todo documento, memoria de cálculo, informe o explicación redactada debe combinar el **máximo rigor técnico-normativo** (fórmulas avanzadas, normas internacionales, tablas y unidades del SI) con **explicaciones conceptuales intuitivas en lenguaje sencillo** (mediante recuadros *«💡 En palabras sencillas / ¿Qué significa esto en la práctica?»*, analogías claras y esquemas visuales), de modo que el trabajo sea 100% riguroso para un tribunal de tesis y 100% comprensible para cualquier persona sin conocimientos de ingeniería o construcción.