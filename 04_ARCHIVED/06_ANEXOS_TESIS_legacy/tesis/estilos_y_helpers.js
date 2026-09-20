const docxModule = require("docx");
const {
    Paragraph, TextRun, HeadingLevel, AlignmentType,
    LevelFormat, PageBreak, SimpleField, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType,
    BorderStyle, BookmarkStart, BookmarkEnd, TabStopType,
    Math: DocxMath, MathRun, MathFraction, MathSubScript, MathSuperScript, MathSubSuperScript,
    MathRadical, MathRoundBrackets, MathSquareBrackets, MathCurlyBrackets
} = docxModule;
const fs = require("fs");
const path = require("path");

// ---------- PALETA DE COLORES ACADÉMICA / INGENIERÍA ESTRUCTURAL ----------
const BLACK = "000000";
const DARK = "1E293B";       // Títulos principales (#1E293B)
const NAVY = "0F172A";       // Encabezados primarios (#0F172A)
const BLUE = "0284C7";       // Subtítulos y acentos (#0284C7)
const GRAY = "475569";       // Texto secundario
const LIGHT_BG = "F8FAFC";   // Fondo de filas alternadas de tabla
const BORDER_COLOR = "CBD5E1";
const WHITE = "FFFFFF";

// ---------- TIPOGRAFÍA ACADÉMICA ----------
const FONT_BODY = "Cambria";   // Texto principal (Serif formal)
const FONT_HEAD = "Calibri";   // Encabezados y títulos (Sans-serif)

const AUTOR = "José Valentino Chiappini Vergara";
const UNIVERSIDAD = "Universidad Internacional Tres Fronteras (UNINTER)";
const FACULTAD = "FACULTAD DE CIENCIAS Y TECNOLOGÍA (FACITPRO) — INGENIERÍA CIVIL";
const TITULO_TESIS = "DISEÑO ESTRUCTURAL, OPTIMIZACIÓN ALGORÍTMICA (NSGA-II) Y METODOLOGÍA BIM (ISO 19650) DE UN EDIFICIO DE USO MIXTO DE 18 pisos y 2 subsuelos SOMETIDO A CARGAS DE VIENTO EN CIUDAD DEL ESTE";
const SUBTITULO_TESIS = "Aplicación al Caso de Estudio: Edificio de 18 Niveles (90.0m x 40.0m) en Ciudad del Este, Paraguay";
const TITULO_CORTO = "Tesis de Grado — Edificio Mixto 18P (Ingeniería Estructural & BIM)";

// ---------- RUTAS DE ILUSTRACIONES ----------
const BASE_DIR = path.join(__dirname, "../../..");
const PATH_IMG_PB = path.join(BASE_DIR, "05_RECURSOS/05.05_Scripts_Python/02_PB_Macro_Distribucion/outputs/masterplan_planta_baja.png");
const PATH_IMG_OFI = path.join(BASE_DIR, "05_RECURSOS/05.05_Scripts_Python/04_Planta_Tipo/outputs/esquema_intercalado_18_pisos.png");
const PATH_IMG_RES = path.join(BASE_DIR, "05_RECURSOS/05.05_Scripts_Python/04_Planta_Tipo/outputs/planta_tipo_layout_A.png");
const PATH_IMG_EST = path.join(BASE_DIR, "05_RECURSOS/05.05_Scripts_Python/06_Estructura/outputs/plano_grilla_pilares.png");

// ---------- HELPERS DE PÁRRAFOS Y TÍTULOS ----------
function h1(text) {
    return new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 420, after: 180 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: BLUE } },
        children: [new TextRun({ text, bold: true, color: DARK, size: 28, font: FONT_HEAD })],
    });
}

function h2(text) {
    return new Paragraph({
        heading: HeadingLevel.HEADING_2,
        spacing: { before: 280, after: 120 },
        children: [new TextRun({ text, bold: true, color: BLUE, size: 22, font: FONT_HEAD })],
    });
}

function h3(text) {
    return new Paragraph({
        heading: HeadingLevel.HEADING_3,
        spacing: { before: 200, after: 80 },
        children: [new TextRun({ text, bold: true, color: DARK, size: 20, font: FONT_HEAD })],
    });
}

function p(children_or_text, opts = {}) {
    const children = typeof children_or_text === "string"
        ? [new TextRun({ text: children_or_text, size: 22, font: FONT_BODY, ...opts })]
        : children_or_text;
    return new Paragraph({
        spacing: { after: 140, line: 300 }, // Interlineado 1.25
        alignment: AlignmentType.JUSTIFIED,
        children,
    });
}

function bullet(text) {
    return new Paragraph({
        numbering: { reference: "main-bullets", level: 0 },
        spacing: { after: 90, line: 280 },
        alignment: AlignmentType.JUSTIFIED,
        children: [new TextRun({ text, size: 22, font: FONT_BODY })],
    });
}

// Salto de página explícito (para cerrar cada capítulo).
function pageBreak() {
    return new Paragraph({ children: [new PageBreak()] });
}

// Referencia cruzada IEEE a Tabla/Ilustración mediante campo REF de Word.
// `cached` es el resultado mostrado hasta que Word actualiza los campos
// (features.updateFields = true recalcula al abrir).
function ref(captionId, cached) {
    return new TextRun({
        children: [new SimpleField(`REF ${captionId} \\h`, String(cached || ""))],
        bold: true,
        color: BLUE,
        font: FONT_BODY,
    });
}

function figura(imgPath, widthPx, heightPx, id, captionText) {
    if (!fs.existsSync(imgPath)) {
        console.warn(`[ADVERTENCIA] Imagen no encontrada: ${imgPath}`);
        return [];
    }
    const img = new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 80 },
        children: [
            new ImageRun({
                type: "png",
                data: fs.readFileSync(imgPath),
                transformation: { width: widthPx, height: heightPx },
            }),
        ],
    });
    const cap = new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 40, after: 240 },
        children: [
            new BookmarkStart(id, id),
            new TextRun({ text: "Ilustración ", bold: true, size: 18, color: BLUE, font: FONT_HEAD }),
            new SimpleField("SEQ Ilustración \\* ARABIC"),
            new TextRun({ text: `: ${captionText}`, size: 18, color: GRAY, italics: true, font: FONT_BODY }),
            new BookmarkEnd(id),
        ],
    });
    return [img, cap];
}

function cell(text, opts = {}) {
    return new TableCell({
        width: { size: opts.width || 2000, type: WidthType.DXA },
        shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR } : undefined,
        margins: { top: 120, bottom: 120, left: 140, right: 140 },
        verticalAlign: "center",
        children: [
            new Paragraph({
                alignment: opts.header ? AlignmentType.CENTER : (opts.align || AlignmentType.LEFT),
                children: [
                    new TextRun({
                        text,
                        bold: !!opts.header,
                        color: opts.header ? WHITE : BLACK,
                        size: opts.fontSize || 19,
                        font: FONT_BODY,
                    }),
                ],
            }),
        ],
    });
}

function dataTable(captionId, captionText, columnWidths, headers, rows) {
    const cap = new Paragraph({
        spacing: { before: 240, after: 100 },
        alignment: AlignmentType.CENTER,
        children: [
            new BookmarkStart(captionId, captionId),
            new TextRun({ text: "Tabla ", bold: true, size: 19, color: BLUE, font: FONT_HEAD }),
            new SimpleField("SEQ Tabla \\* ARABIC"),
            new TextRun({ text: `: ${captionText}`, bold: true, size: 19, color: DARK, font: FONT_HEAD }),
            new BookmarkEnd(captionId),
        ],
    });

    // Escala las columnas para ocupar el ancho útil de la hoja (A4, márgenes 1417 twips)
    // → 11906 - 2×1417 = 9072 twips. La tabla queda centrada y a ancho completo.
    const PAGE_USABLE_DXA = 9072;
    const total = columnWidths.reduce((a, b) => a + b, 0);
    const scale = PAGE_USABLE_DXA / total;
    const widths = columnWidths.map((w) => Math.round(w * scale));
    const totalWidth = widths.reduce((a, b) => a + b, 0);

    const t = new Table({
        alignment: AlignmentType.CENTER,
        width: { size: totalWidth, type: WidthType.DXA },
        columnWidths: widths,
        borders: {
            top: { style: BorderStyle.SINGLE, size: 8, color: DARK },
            bottom: { style: BorderStyle.SINGLE, size: 8, color: DARK },
            left: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
            right: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
            insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
            insideVertical: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
        },
        rows: [
            new TableRow({
                tableHeader: true,
                children: headers.map((h, i) => cell(h, { header: true, width: widths[i], fill: DARK })),
            }),
            ...rows.map((r, idx) =>
                new TableRow({
                    children: r.map((c, i) => cell(c, { width: widths[i], fill: idx % 2 === 1 ? LIGHT_BG : WHITE })),
                })
            ),
        ],
    });
    return [cap, t];
}

// ---------- HELPERS DE ECUACIONES NATIVAS DE WORD (OMML) ----------

// Párrafo de Ecuación Nativa en Bloque (centrada, opcionalmente numerada a la derecha)
function eqBlock(mathObj, eqLabel) {
    if (!eqLabel) {
        return new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { before: 180, after: 180 },
            children: [mathObj instanceof DocxMath ? mathObj : new DocxMath({ children: Array.isArray(mathObj) ? mathObj : [mathObj] })],
        });
    }
    const mathChild = mathObj instanceof DocxMath ? mathObj : new DocxMath({ children: Array.isArray(mathObj) ? mathObj : [mathObj] });
    return new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 180, after: 180 },
        tabStops: [{ type: TabStopType.RIGHT, position: 9072 }],
        children: [
            mathChild,
            new TextRun({ text: `\t(${eqLabel})`, size: 20, font: FONT_BODY, color: GRAY, bold: true })
        ],
    });
}

function mathInline(children) {
    const list = Array.isArray(children) ? children : [children];
    return new DocxMath({ children: list });
}

function mRun(text) {
    return new MathRun(text);
}

function mSub(base, sub) {
    return new MathSubScript({
        children: typeof base === "string" ? [new MathRun(base)] : (Array.isArray(base) ? base : [base]),
        subScript: typeof sub === "string" ? [new MathRun(sub)] : (Array.isArray(sub) ? sub : [sub])
    });
}

function mSup(base, sup) {
    return new MathSuperScript({
        children: typeof base === "string" ? [new MathRun(base)] : (Array.isArray(base) ? base : [base]),
        superScript: typeof sup === "string" ? [new MathRun(sup)] : (Array.isArray(sup) ? sup : [sup])
    });
}

function mSubSup(base, sub, sup) {
    return new MathSubSuperScript({
        children: typeof base === "string" ? [new MathRun(base)] : (Array.isArray(base) ? base : [base]),
        subScript: typeof sub === "string" ? [new MathRun(sub)] : (Array.isArray(sub) ? sub : [sub]),
        superScript: typeof sup === "string" ? [new MathRun(sup)] : (Array.isArray(sup) ? sup : [sup])
    });
}

function mFrac(num, den) {
    return new MathFraction({
        numerator: typeof num === "string" ? [new MathRun(num)] : (Array.isArray(num) ? num : [num]),
        denominator: typeof den === "string" ? [new MathRun(den)] : (Array.isArray(den) ? den : [den])
    });
}

function mRad(radicand, degree) {
    return new MathRadical({
        children: typeof radicand === "string" ? [new MathRun(radicand)] : (Array.isArray(radicand) ? radicand : [radicand]),
        degree: degree ? (typeof degree === "string" ? [new MathRun(degree)] : degree) : undefined
    });
}

function mBrackets(expr) {
    return new MathRoundBrackets({
        children: typeof expr === "string" ? [new MathRun(expr)] : (Array.isArray(expr) ? expr : [expr])
    });
}

function mSquareBrackets(expr) {
    return new MathSquareBrackets({
        children: typeof expr === "string" ? [new MathRun(expr)] : (Array.isArray(expr) ? expr : [expr])
    });
}

// Helper para listar la definición y unidades de las variables de una ecuación ("Donde:")
function eqDonde(variablesList) {
    return [
        new Paragraph({
            spacing: { before: 80, after: 60, line: 280 },
            children: [
                new TextRun({ text: "Donde:", italics: true, bold: true, size: 21, font: FONT_BODY, color: DARK })
            ]
        }),
        ...variablesList.map(([v, desc]) => {
            const mathChild = v instanceof DocxMath ? v : new DocxMath({ children: Array.isArray(v) ? v : [v] });
            return new Paragraph({
                indent: { left: 420 },
                spacing: { after: 50, line: 260 },
                children: [
                    new TextRun({ text: "• ", bold: true, color: BLUE }),
                    mathChild,
                    new TextRun({ text: `: ${desc}`, size: 21, font: FONT_BODY, color: BLACK })
                ]
            });
        })
    ];
}

module.exports = {
    BLACK, DARK, NAVY, BLUE, GRAY, LIGHT_BG, BORDER_COLOR, WHITE,
    FONT_BODY, FONT_HEAD, AUTOR, UNIVERSIDAD, FACULTAD, TITULO_TESIS, SUBTITULO_TESIS, TITULO_CORTO,
    PATH_IMG_PB, PATH_IMG_OFI, PATH_IMG_RES, PATH_IMG_EST,
    h1, h2, h3, p, bullet, figura, dataTable, ref, pageBreak,
    DocxMath, MathRun, MathFraction, MathSubScript, MathSuperScript, MathSubSuperScript,
    MathRadical, MathRoundBrackets, MathSquareBrackets, MathCurlyBrackets,
    eqBlock, eqDonde, mathInline, mRun, mSub, mSup, mSubSup, mFrac, mRad, mBrackets, mSquareBrackets
};

