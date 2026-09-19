# 06.01 — Capítulos del Documento Escrito de Tesis

> **Estado:** ⏳ *En preparación para la nueva redacción tras el desarrollo de las Etapas B a P.*

---

## 🏗️ Principio Rector: Arquitectura 100% Modular

La redacción del documento escrito de tesis y sus anexos de cálculo debe estructurarse de forma **estrictamente modular, desacoplada y mantenible**:

1. **Estructura Modular de Capítulos:**
   - Cada capítulo vive en su propio archivo independiente dentro de `capitulos/` (`cap01_introduccion.js`, `cap02_marco_teorico.js`, ..., `cap10_conclusiones.js`).
   - El ensamblador principal (`build_tesis.js`) importa de forma modular la lista de capítulos desde `capitulos/index.js`.
   - Permite agregar, reordenar o modificar cualquier capítulo sin afectar al resto del sistema.

2. **Anexos de Cálculo en LaTeX Modulares:**
   - El anexo de cálculo en LaTeX posee un documento maestro (`main.tex`) que incluye mediante `\input{capitulos/0N_*.tex}` cada capítulo de cálculo independiente.
   - Las variables y resultados numéricos provienen directamente de archivos `.json` / `.csv` generados por los módulos de cálculo en Python.

3. **Independencia de Contenidos:**
   - Ningún capítulo debe tener código duro ni dependencias cruzadas opacas.
   - Toda tabla de datos, gráfico o referencia debe conectarse a través del módulo maestro de imágenes `imagenes.js` y las planillas de datos de origen.

---

- **Entregable Principal:** Documento Word (`.docx`) compilado mediante pipeline Node.js / JavaScript y anexos de cálculo en LaTeX (`.tex` / `.pdf`).
- **Extensión Objetivo:** ~200–300 Páginas de contenido técnico riguroso en español.
- **Histórico:** Los borradores de capítulos y anexos anteriores se encuentran archivados en `04_ARCHIVED/06_ANEXOS_TESIS_legacy/`.
