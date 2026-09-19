# Normativa Municipal — Ordenanzas Junta Municipal de Ciudad del Este

> Repositorio local de las **ordenanzas municipales de Ciudad del Este (2020–2026 + Años Varios)**
> descargadas del portal oficial https://mcde.gov.py/categoria/ordenanzas-junta-municipal-cms el **2026-09-19**.
> Método: HTTP con reintentos + verificación con navegador headless. Los 45 PDF escaneados se procesaron con **OCR nativo de Windows (`Windows.Media.Ocr`, es)**.

## Estructura

| Ruta | Contenido |
|---|---|
| `00_Indice/00_INDICE_GENERAL.md` | Índice general, resumen cuantitativo y enlaces por año |
| `00_Indice/RELEVANCIA_PROYECTO.md` | **Qué ordenanzas aplican a la tesis y por qué** (empezar aquí) |
| `01_Catalogo_Por_Anio/` | Catálogo por año (2020…2026, VARIOS) con asunto (div mt-4), PDF y texto |
| `02_Texto_Completo/` | **230 fichas de texto** (185 del PDF nativo + 45 por OCR) |
| `03_PDF_Originales/{año}/` | **228 archivos PDF originales**, ordenados por año (231 registros con PDF; 3 son duplicados) |
| `03_PDF_Originales/_MANIFEST.csv` | Manifiesto completo (id, año, título, asunto, relevancia, páginas, estado, archivo) |
| `03_PDF_Originales/_manifest.jsonl` | Manifiesto incremental |
| `03_PDF_Originales/_ocr_manifest.jsonl` | Resultado del OCR por documento |

## Visor web

- **`visor_ordenanzas.html`** (raíz del repo): visor de ordenanzas con buscador, filtros por año/relevancia, lectura del texto y apertura del PDF original.
- Se alimenta de **`ordenanzas_data.js`** (raíz del repo), generado automáticamente.
- Requiere servidor local (`python -m http.server 8000`) o GitHub Pages (por el `fetch` de los `.md`).

## Resumen

- **236 registros** catalogados · **228 archivos PDF** (~318 MB).
- **183** con capa de texto · **45** escaneados (OCR completado) · **5** sin PDF embebido · **3** duplicados.
- **230 fichas de texto** · Relevancia: 27 ALTA · 53 MEDIA · 156 BAJA.
- **2025:** slug correcto `-ordenanzas-junta-municipal-ano-2025-cms` (con guion inicial) → 6 registros.

## Categorías oficiales

| Año | Slug |
|---|---|
| 2020 | `ordenanzas-junta-municipal-2020-cms` |
| 2021 | `ordenanzas-junta-municipal-2021-cms` |
| 2022 | `ordenanzas-junta-municipal-2022-cms` |
| 2023 | `ordenanzas-junta-municipal-2023-cms` |
| 2024 | `ordenanzas-junta-municipal-ano-2024-cms` |
| 2025 | `-ordenanzas-junta-municipal-ano-2025-cms` |
| 2026 | `ordenanzas-junta-municipal-ano-2026-cms` |
| Años Varios | `ordenanzas-junta-municipal-anos-varios--cms` |

## Nota sobre Años Varios

El **Código de Edificación base** (retiros, alturas, uso de suelo) está en las ordenanzas antiguas
de `01_Catalogo_Por_Anio/VARIOS.md` (Ord. 05/76, 11/94, 10/88, 38/99, etc.), no en las de 2020–2026.
