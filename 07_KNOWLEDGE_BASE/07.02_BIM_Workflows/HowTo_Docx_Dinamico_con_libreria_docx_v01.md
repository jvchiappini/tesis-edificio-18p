# Generación de documentos Word dinámicos y profesionales con la librería `docx` (Node.js) — v04

> Área: flujos de trabajo BIM — generación de documentos de tesis.
> Fecha: 2026-08-19. Herramientas: Node.js v22, librería `docx` v9.7.1, Python 3.13 + matplotlib para figuras, Microsoft 365 Word (16.0.20228.20190, x64, interfaz en inglés), PowerShell 5.1 (.NET ZipArchive) para post-proceso.
> Uso: generar capítulos/tareas de la tesis en `.docx` con campos dinámicos de Word, escalable en grises.

## Objetivo
Crear un `.docx` profesional que sea **verdaderamente dinámico al editarlo en Word**: índices que se actualizan, numeración automática de figuras/tablas, encabezado con el título del capítulo actual y propiedades de documento editables.

## Herramientas
- `npm install docx` (Node.js). Script: `build.js` con `const { Document, Packer, ... } = require("docx")`.
- Figuras en Python/matplotlib con `matplotlib.use("Agg")`, guardadas como PNG (usar escala de grises, ver abajo).

## Elementos dinámicos implementados (con la librería docx v9)

| Elemento dinámico | Código | Efecto en Word |
|-------------------|--------|----------------|
| Actualizar campos al abrir | `features: { updateFields: true }` en `new Document(...)` | Word pide actualizar campos al abrir |
| Propiedades del documento | `title`, `subject`, `creator`, `keywords`, `description`, `lastModifiedBy` en `new Document(...)` | Visibles en Archivo → Información |
| Índice general | `new TableOfContents(undefined, { hyperlink: true, headingStyleRange: "1-2" })` | TOC editable/actualizable |
| Índice de figuras | `new SimpleField('TOC \\h \\z \\c "Ilustración"')` | Recoge los campos `SEQ Ilustración` |
| Numeración de figuras | `new SimpleField("SEQ Ilustración \\* ARABIC")` dentro del pie | Auto-numera al insertar nuevas |
| Numeración de tablas | `new SimpleField("SEQ Tabla \\* ARABIC")` en el título de tabla | Auto-numera al insertar nuevas |
| Página X de Y | `PageNumber.CURRENT` y `PageNumber.TOTAL_PAGES` en el footer | Números de página dinámicos |
| Capítulo actual en el encabezado | `new SimpleField("STYLEREF 1 \\* MERGEFORMAT")` en el header | Muestra el título de la sección actual |
| Fecha dinámica | `new SimpleField('DATE \\@ "dd/MM/yyyy"')` | Fecha que se actualiza |
| Enlaces a figuras en el texto | `new InternalHyperlink({ anchor: "fig2", children: [...] })` + `BookmarkStart/End` en el pie | Navegación clic a la figura |
| Estilos editables | `styles.default.heading1/heading2/document/hyperlink` | Se modifican desde el panel de estilos de Word |

## Reglas clave de la API (docx v9)
- `SimpleField` renderiza `<w:fldSimple>` y va como **hijo de párrafo** (no dentro de `TextRun`), aunque el resultado se formatea según los valores por defecto del párrafo.
- `TextRun({ children: [...] })` acepta `SimpleField` y `PageNumber.CURRENT`.
- `TableOfContents(alias, options)`: pasar `undefined` como alias evita duplicar el título del índice (se usa un `h1` propio).
- `InternalHyperlink` requiere `anchor` + `children`; el destino es un `BookmarkStart/BookmarkEnd` (puede ir dentro del párrafo del pie de figura).
- Sombreado por filas: `TableCell({ shading: { fill, type: ShadingType.CLEAR } })`; no hay sombreado directo en `TableRow`.
- Celdas de encabezado de tabla repetibles entre páginas: `TableRow({ tableHeader: true })`.

## Escala de grises (design)
- Paleta usada: `#262626` (títulos), `#595959` (texto secundario), `#808080` (reglas), `#D9D9D9` (sombreado claro), `#F2F2F2` (filas alternadas), `#000000` (cuerpo).
- Tipografía académica: cuerpo en **Cambria** (serif), títulos en **Calibri** (sans-serif).
- Figuras matplotlib: cambiar las constantes de color a grises para que las figuras sean también monocromáticas.

## Estructura del documento
1. **Sección 1 (carátula):** sin encabezado/pie, título y autor estáticos estilizados, reglas dobles, ciudad y año.
2. **Sección 2 (contenido):** numeración de página reiniciada (`pageNumbers: { start: 1 }`), header con `STYLEREF` + título corto, footer con autor + página X de Y, índice general, índice de ilustraciones y el cuerpo.

## Citas bibliográficas embebidas en Word (References → Manage Sources) — v03/v04
Las fuentes y las citas se pueden precargar en el `.docx` para que el usuario **no tenga que tipearlas** en Word.

### Dónde guarda Word las fuentes (IMPORTANTE)
- La **lista actual del documento** (Current List) se guarda en la parte **`customXml/item1.xml`**, NO en `settings.xml`. (Un intento previo de ponerlas en `word/settings.xml` con `<w:bibliography>` hizo que Word mostrara "contenido que no se puede abrir" y todas las citas dijeran "Invalid source specified": el esquema de `CT_Settings` no admite ese elemento en esa posición.)
- Plomería necesaria (idéntica a la que genera Word, verificada con COM):
  - `customXml/item1.xml`: `<b:Sources xmlns:b="http://schemas.openxmlformats.org/officeDocument/2006/bibliography" xmlns="..." SelectedStyle="\IEEE2006OfficeOnline.xsl" StyleName="IEEE" Version="2006">` con `<b:Source>…</b:Source>` por fuente.
  - Cada `<b:Source>` (sin atributo de estilo) lleva: `<b:Tag>` (p. ej. `Els17` = 3 letras apellido + año), `<b:SourceType>` (`JournalArticle`, `ConferenceProceedings`), `<b:Author><b:Author><b:NameList><b:Person><b:Last/><b:First/>…` (el wrapper `Author` se repite DOS veces), `<b:Title>`, `<b:Year>`, `<b:JournalName>`, `<b:Volume>`, `<b:Issue>`, `<b:Pages>`, `<b:StandardNumber>` (DOI), `<b:ConferenceName>`, `<b:Publisher>`.
  - `customXml/itemProps1.xml`: `<ds:datastoreItem ds:itemID="{GUID}" xmlns:ds="http://schemas.openxmlformats.org/officeDocument/2006/customXml"><ds:schemaRefs><ds:schemaRef ds:uri="http://schemas.openxmlformats.org/officeDocument/2006/bibliography"/></ds:schemaRefs></ds:datastoreItem>`.
  - `customXml/_rels/item1.xml.rels`: relación `customXmlProps` → `itemProps1.xml`.
  - `[Content_Types].xml`: `<Override PartName="/customXml/itemProps1.xml" ContentType="application/vnd.openxmlformats-officedocument.customXmlProperties+xml"/>` (item1.xml lo cubre el Default `application/xml`).
  - `word/_rels/document.xml.rels`: `<Relationship Id="rIdN" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml" Target="../customXml/item1.xml"/>` con `rIdN` no usado.
- Script listo: `tarea1_word/add_citations_zip.ps1` (inyección zip pura, sin Word).

### Citas en el texto
- Campo `CITATION <Tag> \l 1033` (IEEE numérico). Con `docx` se genera con `new SimpleField("CITATION Els17 \\l 1033", "[1]")` — el 2º argumento debe ser un **string** (SimpleField lo envuelve en `TextRun`); si se pasa un array de TextRun, la librería produce un run vacío (`<w:r/>`).
- El resultado cacheado sale sin `rPr`; opcionalmente se le aplica formato con el regex `(<w:fldSimple w:instr="CITATION [^"]*"><w:r>)(<w:t[^>]*>[^<]*</w:t>)?(</w:r></w:fldSimple>)` → `$1 + rPr + $2 + $3`. No es imprescindible: Word re-formatea el resultado al actualizar.
- Al abrir el documento (con `features: { updateFields: true }`) Word pide actualizar campos y las citas se resuelven desde `customXml` ([1]…[8] verificados). Alternativa: `Ctrl+A` → `F9`.
- **No** reemplazar marcadores tipo `[CITA n]` con un regex que busque su `<w:r>`: el `.*?` del grupo `rPr` puede consumir contenido entre runs y corromper el XML. Generar el campo directo con `SimpleField` es seguro.

### Alternativa COM (descartada por cuelgues)
`Word` COM (`doc.Bibliography.Sources.Add("<b:Source xmlns:b='http://schemas.microsoft.com/office/word/2004/10/bibliography'>…")`) funciona para añadir fuentes, pero `doc.Fields.Update()` se colgó en este documento (probablemente por la paginación + campos TOC/PAGE). Se optó por la inyección zip pura.

## Interacción con Word (interfaz en inglés) — citas, figuras e índices (v02)
Verificado en Microsoft 365 Word 16.0.20228.20190 x64 (interfaz en inglés). El usuario debe operar con la terminología inglesa de los menús:

| Acción | Menú en inglés (Word 365) |
|--------|---------------------------|
| Actualizar índice general | Clic derecho sobre el TOC → `Update Field` → `Update entire table`, o pestaña **References** → **Table of Contents** → **Update Table** |
| Actualizar índice de figuras/tablas | Clic en la tabla → **References** → **Captions** → **Update Table** (o clic derecho → `Update Field` → `Update entire table`) |
| Pie/leyenda de figura nueva | **References** → **Captions** → **Insert Caption** → `New Label` → "Ilustración" → Position: Below selected item |
| Referencia a figura en el texto | **References** → **Captions** → **Cross-reference** → Reference type: Figure → Insert reference to: Only label and number → activar `Insert as hyperlink` |
| Cargar fuente de cita | **References** → **Citations & Bibliography** → `Style` → IEEE → **Insert Citation** → **Add New Source** → completar en `Create Source` |
| Reusar cita existente | **References** → **Insert Citation** → seleccionar la fuente |
| Generar bibliografía | **References** → **Bibliography** → **Insert Bibliography** (añadir título "References") |
| Actualizar bibliografía | Seleccionarla → **References** → **Update Citations and Bibliography** (o Ctrl+A y F9) |

Reglas operativas:
- La numeración de figuras usa el campo `SEQ` con etiqueta "Ilustración"; el índice de figuras es `TOC \h \z \c "Ilustración"`. Ambos deben coincidir en la etiqueta para que el `Insert Caption`/`Insert Table of Figures` de Word los reconozca.
- Word **no** actualiza la bibliografía automáticamente (a diferencia del TOC con `updateFields`): hay que pulsar `Update Citations and Bibliography` o F9.
- Los títulos de las fuentes se mantienen en el idioma original de publicación; es práctica académica estándar (no es texto redactado por el autor).

## Referencia de archivo
Script completo de ejemplo: `06_ANEXOS_TESIS/06.01_Capitulos_Documento_Escrito/tarea1_word/build.js`.
Citas/fuentes: `tarea1_word/add_citations_zip.ps1` (se ejecuta tras `node build.js`).
Figuras: `tarea1_word/make_charts.py` (guarda PNG en `tarea1_word/images/`).