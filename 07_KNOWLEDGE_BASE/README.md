# 07_KNOWLEDGE_BASE — Base de Conocimiento

Memoria técnica reutilizable del proyecto. Objetivo: **ningún agente debe buscar dos veces lo mismo**.

Cuando cualquier agente resuelva una duda técnica (Revit, BIM, normativa, cálculo, etc.) debe:

1. Buscar la información con `websearch` / `webfetch`.
2. Redactar un **paso a paso detallado** (con captura conceptual, menús, atajos, notas) y guardarlo aquí.
3. Responder al usuario con un resumen breve + la ruta del archivo guardado.

## Estructura

| Carpeta | Contenido |
|---------|-----------|
| `07.01_Revit_HowTo` | Tutoriales paso a paso de Revit (modelado, familias, plantillas, tablas, vistas, parámetros compartidos, etc.). |
| `07.02_BIM_Workflows` | Flujos de trabajo BIM: ISO 19650/CDE, intercambio IFC, clash detection (Navisworks), Dynamo, federación de modelos. |
| `07.03_Analisis_Estructural` | Guías de cálculo estructural: cargas de viento, combinaciones, verificación de vigas/columnas, integración Revit-estructura. |
| `07.04_Normativa_Resumen` | Resúmenes de normas y reglamentos (ISO 19650, reglamento de Ciudad del Este/Paraguay, códigos de viento). |

## Versión de software (OBLIGATORIA)

- Todo tutorial de `07.01_Revit_HowTo` corresponde a **Autodesk Revit 2024 (build 24.3.60.12)**, interfaz en **inglés**, x64.
- **Indicar siempre la versión** en el encabezado del tutorial y usar los nombres de comandos, cintas (ribbon) y menús **en inglés** (p. ej. `Create` > `Shared Parameter`).
- Si un procedimiento varía entre versiones, anotar la diferencia como nota al pie.

## Convención de archivos en esta carpeta

`HowTo_[TEMA]_v[NN].md` — ej. `HowTo_Parametros_Compartidos_v01.md` (indicar versión de Revit al inicio del archivo)

Los archivos se escriben en Markdown, en español, y siempre incluyen:

- **Título y objetivo** (qué resuelve).
- **Prerrequisitos** (versión de software, archivos necesarios).
- **Paso a paso** numerado y detallado.
- **Notas / errores comunes**.
- **Referencias / fuentes** (links consultados).