# Tesis de Grado — Diseño Estructural, Análisis Dinámico al Viento, Coordinación BIM & Presupuesto de Edificio de 18 Pisos y 3 Subsuelos

![BIM Standard](https://img.shields.io/badge/BIM%20Standard-ISO%2019650-blue.svg)
![Revit Version](https://img.shields.io/badge/Autodesk%20Revit-2024-0696D7.svg)
![Python Version](https://img.shields.io/badge/Python-3.13-3776AB.svg)
![License](https://img.shields.io/badge/Academic-Tesis%20Ingenier%C3%ADa%20Civil-green.svg)
![Location](https://img.shields.io/badge/Ubicaci%C3%B3n-Ciudad%20del%20Este%2C%20Paraguay-red.svg)

---

## 📋 Descripción del Proyecto

Este repositorio contiene el desarrollo integral de la **Tesis de Grado en Ingeniería Civil** enfocada en el diseño de un edificio en altura de uso mixto ubicado en **Ciudad del Este, Paraguay**. 

El proyecto integra la metodología **BIM (ISO 19650)**, el cálculo estructural multinormativo comparativo de acciones de viento, la optimización algorítmica de plantas mediante algoritmos genéticos y la gestión 4D/5D del proyecto.

### 🏢 Ficha Técnica Sintética
* **Tipología:** Edificio de uso mixto (Residencial + Comercial + Cocheras + Amenities).
* **Configuración de Plantas:** 3 Subsuelos de cocheras ($S1\text{–}S3$) + Planta Baja Comercial ($PB$) + 18 Pisos Residenciales ($P01\text{–}P18$) + Azotea Técnica & Amenities (Piscina + SUM).
* **Superficie Edificable por Planta:** ⏳ *En re-definición (Etapa B — Arquitectura Completa)*
* **Superficie Construida Total:** ⏳ *En re-definición (Etapa B — Arquitectura Completa)*
* **Superficie del Terreno:** $7.618,49\text{ m}^2$ (Polígono P1-P2-P3-P4, UTM Zona 21J).
* **Parámetros Urbanísticos:** FOS = 0,70 ($A_{\text{máx huella}} = 5.332\text{ m}^2$) | FOT = 4,0 ($A_{\text{sobre rasante}} = 30.474\text{ m}^2$).

---

## 🔬 Ejes Principales de Investigación

1. **Ingeniería de Viento y Dinámica Estructural (Multinormativo Comparativo):**
   * **NP 196:1991** (Paraguay - Norma Paraguaya de Viento)
   * **NBR 6123:2023** (Brasil - Forças devidas ao vento em edificações)
   * **ASCE 7-22** (EE.UU. - Minimum Design Loads and Associated Criteria for Buildings)
   * **EN 1991-1-4 / Eurocódigo 1** (Europa - Acciones en estructuras: Acciones de viento)

2. **Diseño Estructural en Hormigón Armado ($H^\circ A^\circ$):**
   * Sistema de entrepiso de **losas nervadas / reticulares alivianadas bidireccionales** con casetones recuperables.
   * Vigas de borde spandrel, pilares continuos de alta resistencia y núcleos/pantallas rígidas para la absorción de cargas laterales.

3. **Metodología BIM e ISO 19650 (CDE & Federación):**
   * Entorno Común de Datos (**CDE**) estructurado en 4 estados ISO 19650 (*WIP, Shared, Published, Archived*).
   * Modelado multidisciplinar (LOD 300 / 350) en Autodesk Revit 2024.
   * Federación de modelos 3D y detección de interferencias (*Clash Detection*) en Autodesk Navisworks Manage 2024.

4. **Optimización Algorítmica (Python & NSGA-II):**
   * Automatización mediante Python 3.13 (`DEAP`, `PyNiteFEA`, `numpy`, `pandas`, `matplotlib`) para optimización multiobjetivo de plantas y distribución de espacios interiores.

5. **Gestión de Proyecto (BIM 4D/5D):**
   * Análisis de Precios Unitarios (APU) adaptados al mercado paraguayo (CAPACO / CYPE).
   * Planificación de obra 4D (Cronograma Gantt integrativo).

---

## 📁 Estructura del Repositorio (CDE ISO 19650)

```
00_TESIS_EDIFICIO_18P/
├── 00_GESTION_DE_PROYECTO/    # BEP, Estándares, Roadmap 300 pág, Acta de proyecto
├── 01_WIP/                    # Work in Progress (Modelos Revit .rvt y planos en desarrollo)
├── 02_SHARED/                 # Shared (Modelos federados .nwd/.ifc e informes de clash)
├── 03_PUBLISHED/              # Published (Planos aprobados PDF, memorias y entregables)
├── 04_ARCHIVED/               # Archived (Historial de versiones superadas y legado)
├── 05_RECURSOS/               # Plantillas Revit, Familias, Parámetros compartidos y Scripts Python
├── 06_ANEXOS_TESIS/           # Capítulos Word (.docx), scripts Node.js y Anexos LaTeX (.tex)
├── 07_KNOWLEDGE_BASE/         # Base de conocimiento técnica (Revit, Viento, Normativa, Cálculo)
├── etapas/                    # 57 Documentos Markdown (Etapas A–P y sub-etapas estructuradas)
├── AGENTS.md                  # Reglas y guía de trabajo para agentes IA y desarrollo
├── index.html                 # Dashboard interactivod de avance y cronograma
└── visor.html                 # Visor web navegable de documentación Markdown por etapas
```

---

## 🏷️ Convención de Nomenclatura de Archivos

Todos los entregables y modelos siguen estrictamente el estándar del proyecto:

$$\text{TESIS-[DISCIPLINA]-[NIVEL]-[TIPO]-[NUMERO]}$$

* **DISCIPLINA:** `ARQ`, `EST`, `SAN`, `ELE`, `INC`, `MEC`, `CLO`, `PLU`, `COORD`.
* **NIVEL:** `SUB3`, `SUB2`, `SUB1`, `PB`, `P01`–`P18`, `AZ`, `GEN`.
* **TIPO:** `M3` (Modelo 3D), `DR` (Plano 2D), `SC` (Tabla/Cómputo), `RP` (Memoria/Reporte), `CALC` (Cálculo), `SCRIPT` (Código).
* **Ejemplo:** `TESIS-EST-P05-M3-001.rvt`

---

## 🌐 Dashboard y Visor Web Local

El proyecto cuenta con una plataforma estática interactiva para visualizar el progreso y la documentación completa de la tesis por etapas:

1. **Dashboard Principal (`index.html`):** Cronograma interactivo, métricas de avance y checklists.
2. **Visor de Etapas (`visor.html`):** Entorno de lectura interactivo con navegación en árbol de las 16 Etapas (A–P) y 41 Sub-etapas.

### Ejecución en Servidor Local

Puedes iniciar un servidor web local sencillo utilizando Python:

```bash
# Iniciar servidor local en el puerto 8000
python -m http.server 8000
```

Luego abre tu navegador en:
* Dashboard: `http://localhost:8000/index.html`
* Visor Web: `http://localhost:8000/visor.html`

---

## 🛠️ Tecnologías y Herramientas

* **BIM / CAD:** Autodesk Revit 2024 (Inglés), Autodesk Navisworks Manage 2024, CYPECAD.
* **Cálculo & Algoritmos:** Python 3.13 (`DEAP`, `PyNiteFEA`, `numpy`, `pandas`, `matplotlib`).
* **Documentación & Tesis:** Microsoft Word (Pipeline automatizado con Node.js), LaTeX (MiKTeX).
* **Web Frontend:** HTML5, CSS3 Vanilla, JavaScript (ES6+).

---

## 📜 Licencia y Derechos

Este proyecto se realiza en el marco de la **Tesis de Grado de la Carrera de Ingeniería Civil**. Todos los derechos de propiedad intelectual pertenecen al autor del trabajo de grado.
