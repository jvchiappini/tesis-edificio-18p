// =====================================================================
//  TESIS DE GRADO — DOCUMENTO FINAL (build_tesis.js)
//  Genera TESIS_CHIAPPINI_v01.docx — documento de la tesis completa.
//  Pipeline: Word (docx) para el documento; cálculos en anexo LaTeX.
//  Compilar: node build_tesis.js   (override: $env:TESIS_OUT="nombre.docx")
//
//  El contenido está modularizado en ./capitulos/*.js y las rutas de
//  las ilustraciones en ./imagenes.js. Este archivo solo ensambla el
//  documento (portada, estilos, encabezado/pie y orden de capítulos).
// =====================================================================
const {
    Document, Packer, Paragraph, TextRun, AlignmentType,
    LevelFormat, PageBreak, Footer, Header, SimpleField,
    PageNumber, BorderStyle, TabStopType,
} = require("docx");
const fs = require("fs");
const path = require("path");

const {
    DARK, NAVY, BLUE, GRAY, BORDER_COLOR, FONT_BODY, FONT_HEAD,
    UNIVERSIDAD, FACULTAD, TITULO_TESIS, SUBTITULO_TESIS, TITULO_CORTO, AUTOR,
} = require("./estilos_y_helpers");

const cuerpo = require("./capitulos");

console.log("Compilando TESIS DE GRADO (documento final)...");

const doc = new Document({
    creator: AUTOR,
    title: TITULO_TESIS,
    subject: "Tesis de Grado — Ingeniería Civil · BIM ISO 19650 · Estructuras",
    keywords: "Tesis; BIM; ISO 19650; NSGA-II; Viento; Losa nervada; Ciudad del Este",
    description: "Documento final de Trabajo de Grado: diseño estructural, optimización algorítmica (NSGA-II) y metodología BIM ISO 19650 de un edificio de uso mixto de 18 pisos y 2 subsuelos en Ciudad del Este.",
    lastModifiedBy: AUTOR,
    features: { updateFields: true },
    numbering: {
        config: [
            {
                reference: "main-bullets",
                levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
                           style: { paragraph: { indent: { left: 420, hanging: 260 } } } }],
            },
            {
                reference: "main-list",
                levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
                           style: { paragraph: { indent: { left: 420, hanging: 260 } } } }],
            },
        ],
    },
    styles: {
        default: {
            document: { run: { font: FONT_BODY, size: 22, color: "000000" }, paragraph: { spacing: { line: 300 } } },
        },
    },
    sections: [
        // ================= PORTADA DE LA TESIS =================
        {
            properties: {
                page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417 } },
            },
            children: [
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300, after: 80 },
                    children: [new TextRun({ text: UNIVERSIDAD, bold: true, size: 22, color: DARK, font: FONT_HEAD })] }),
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 },
                    children: [new TextRun({ text: FACULTAD, bold: true, size: 18, color: GRAY, font: FONT_HEAD })] }),
                new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: BLUE } }, spacing: { after: 800 }, children: [] }),
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
                    children: [new TextRun({ text: "TESIS DE GRADO", bold: true, size: 22, color: BLUE, font: FONT_HEAD })] }),
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 400 },
                    children: [new TextRun({ text: TITULO_TESIS, bold: true, size: 26, color: NAVY, font: FONT_HEAD })] }),
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 900 },
                    children: [new TextRun({ text: SUBTITULO_TESIS, italics: true, size: 20, color: GRAY, font: FONT_BODY })] }),
                new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: BLUE } }, spacing: { after: 1000 }, children: [] }),
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
                    children: [new TextRun({ text: "Postulante:", size: 20, color: GRAY, font: FONT_BODY })] }),
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 800 },
                    children: [new TextRun({ text: AUTOR, bold: true, size: 24, color: DARK, font: FONT_HEAD })] }),
                new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 1000, after: 60 },
                    children: [new TextRun({ text: "Ciudad del Este — Paraguay", size: 20, color: GRAY, font: FONT_BODY })] }),
                new Paragraph({ alignment: AlignmentType.CENTER,
                    children: [new TextRun({ text: "2026", bold: true, size: 20, color: DARK, font: FONT_BODY })] }),
            ],
        },

        // ================= CUERPO DE LA TESIS =================
        {
            properties: {
                page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417 }, pageNumbers: { start: 1 } },
            },
            headers: {
                default: new Header({
                    children: [
                        new Paragraph({
                            border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BORDER_COLOR } },
                            tabStops: [{ type: TabStopType.RIGHT, position: 9070 }],
                            children: [
                                new TextRun({ text: TITULO_CORTO, size: 15, color: GRAY, italics: true, font: FONT_BODY }),
                                new TextRun({ text: "\t", size: 15 }),
                                new TextRun({ children: [new SimpleField("STYLEREF 1 \\* MERGEFORMAT")], size: 15, color: BLUE, font: FONT_BODY }),
                            ],
                        }),
                    ],
                }),
            },
            footers: {
                default: new Footer({
                    children: [
                        new Paragraph({
                            border: { top: { style: BorderStyle.SINGLE, size: 6, color: BORDER_COLOR } },
                            tabStops: [{ type: TabStopType.RIGHT, position: 9070 }],
                            children: [
                                new TextRun({ text: AUTOR, size: 16, color: GRAY, font: FONT_BODY }),
                                new TextRun({ text: "\t", size: 16 }),
                                new TextRun({ text: "Página ", size: 16, color: GRAY, font: FONT_BODY }),
                                new TextRun({ children: [PageNumber.CURRENT], size: 16, color: DARK, font: FONT_BODY }),
                                new TextRun({ text: " de ", size: 16, color: GRAY, font: FONT_BODY }),
                                new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: DARK, font: FONT_BODY }),
                            ],
                        }),
                    ],
                }),
            },
            children: cuerpo(),
        },
    ],
});

Packer.toBuffer(doc).then((buf) => {
    const fileName = process.env.TESIS_OUT || "TESIS_CHIAPPINI_v01.docx";
    const outPath = path.join(__dirname, fileName);
    fs.writeFileSync(outPath, buf);
    console.log(`\n============================================================`);
    console.log(`✔ TESIS DE GRADO COMPILADA EXITOSAMENTE EN:`);
    console.log(`   ${outPath}`);
    console.log(`============================================================\n`);
}).catch((err) => {
    console.error("❌ ERROR DURANTE LA COMPILACIÓN DE LA TESIS:", err);
});

