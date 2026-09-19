// =====================================================================
//  Preliminares: Resumen, Índices, Símbolos y Glosario.
// =====================================================================
const { h1, h2, p, bullet, dataTable, pageBreak } = require("../estilos_y_helpers");
const { SimpleField, TableOfContents, Paragraph } = require("docx");

module.exports = function () {
    return [
        // ================= RESUMEN =================
        h1("Resumen"),
        p("El presente Trabajo de Grado aborda de manera integral el diseño estructural, la optimización espacial multiobjetivo mediante algoritmos genéticos (NSGA-II), la selección del sistema de entrepiso más económico y el modelado de información para la construcción (BIM) bajo la norma ISO 19650, aplicados a un edificio de uso mixto de 18 niveles en Ciudad del Este, Paraguay. La edificación posee una huella edificable de 85,0 m por 37,0 m (3.145,0 m² por nivel) y comprende tres Subsuelos de cocheras (278 plazas y salas técnicas), una Planta Baja comercial y logística, dieciocho niveles residenciales con 432 apartamentos distribuidos en tres disposiciones intercaladas, y una azotea técnica con terraza de eventos y piscina recreativa."),
        p("El trabajo se desarrolla con un enfoque metodológico híbrido. Las macro distribuciones de la Planta Baja, la planta tipo y la azotea se resolvieron por diseño directo, asistido por scripts paramétricos que trazaron la zonificación, y luego se refinaron a mano con criterio arquitectónico; los tres Subsuelos de cocheras también se resolvieron manualmente. La optimización por algoritmos genéticos (NSGA-II en Python/DEAP) se reserva para los problemas que admiten muchas alternativas: las arquitecturas interiores de los departamentos y las micro-distribuciones de la Planta Baja (administración, sanitarios, centro de negocios y depósito de residuos). Sobre esa base se seleccionó el sistema estructural de entrepiso más económico mediante una comparación de costos de cinco alternativas con análisis de sensibilidad, adoptándose la losa nervada o reticular alivianada (68,8 USD/m²). El análisis de la acción del viento se realiza adoptando la norma paraguaya NP 196:1991 y comparándola con tres normas internacionales (NBR 6123, ASCE 7-22 y Eurocódigo 1), y los elementos de hormigón armado se dimensionan bajo ACI 318-19 y NBR 6118, con verificación cruzada mediante programas de cálculo (PyNite) documentados en el anexo de cálculo en LaTeX."),
        p("Palabras clave: hormigón armado, losa nervada, viento, NP 196, NBR 6123, ASCE 7-22, Eurocódigo 1, NSGA-II, BIM, ISO 19650, Ciudad del Este."),

        pageBreak(),

        // ================= ÍNDICES =================
        h1("Índice General"),
        new TableOfContents(undefined, { hyperlink: true, headingStyleRange: "1-3" }),
        pageBreak(),
        h1("Índice de Ilustraciones"),
        new Paragraph({ children: [new SimpleField('TOC \\h \\z \\c "Ilustración"')] }),
        new Paragraph({ spacing: { before: 200 } }),
        h1("Índice de Tablas"),
        new Paragraph({ children: [new SimpleField('TOC \\h \\z \\c "Tabla"')] }),
        pageBreak(),

        // ================= SÍMBOLOS Y ABREVIATURAS =================
        h1("Lista de Símbolos"),
        p("Los símbolos que se usan en los cálculos tienen el siguiente significado. Se presentan aquí para que cualquier lector pueda consultarlos sin perder el hilo del texto."),
        ...dataTable(
            "tabla_simbolos",
            "Símbolos principales empleados en los cálculos.",
            [2200, 1800, 4300],
            ["Símbolo", "Unidad", "Significado"],
            [
                ["f'c", "MPa", "Resistencia característica del hormigón a compresión (en este proyecto, 30 MPa)"],
                ["fy", "MPa", "Tensión de fluencia del acero de refuerzo (en este proyecto, 500 MPa)"],
                ["g", "kN/m²", "Carga permanente (peso propio, acabados, tabiquería)"],
                ["q", "kN/m²", "Sobrecarga de uso (variable)"],
                ["qu", "kN/m²", "Carga mayorada para el estado límite último"],
                ["qs", "kN/m²", "Carga característica para el estado límite de servicio"],
                ["w", "kN/m", "Carga lineal por metro de nervio o de viga"],
                ["L", "m", "Luz entre apoyos"],
                ["M⁻, M⁺", "kN·m", "Momento flector negativo (apoyo) y positivo (tramo)"],
                ["V", "kN", "Esfuerzo de corte"],
                ["As", "mm²", "Área de acero de refuerzo"],
                ["b", "mm o cm", "Ancho de la sección"],
                ["d", "mm o cm", "Altura útil de la sección"],
                ["h", "cm", "Canto o espesor total"],
                ["φ", "—", "Coeficiente de reducción de resistencia"],
                ["ρ", "—", "Cuantía geométrica de armadura"],
                ["Δ", "mm", "Flecha o deformación vertical"],
                ["N", "kN o MN", "Carga axial"],
            ]
        ),

        h1("Lista de Abreviaturas"),
        ...dataTable(
            "tabla_abreviaturas",
            "Abreviaturas y siglas empleadas en el documento.",
            [1800, 5400],
            ["Sigla", "Significado (explicado en castellano)"],
            [
                ["H°A°", "Hormigón armado"],
                ["ELU", "Estado límite último (seguridad estructural)"],
                ["ELS", "Estado límite de servicio (deformaciones y fisuras)"],
                ["ACI 318", "Reglamento de hormigón estructural del Instituto Americano del Hormigón"],
                ["NBR", "Norma Brasileña (Associação Brasileira de Normas Técnicas)"],
                ["NP", "Norma Paraguaya (Instituto Nacional de Tecnología, Normalización y Metrología, INTN)"],
                ["ASCE 7", "Norma de cargas mínimas de la Sociedad Americana de Ingenieros Civiles"],
                ["ISO", "Organización Internacional de Normalización"],
                ["BIM", "Modelado de la información de la construcción"],
                ["CDE", "Entorno común de datos del proyecto"],
                ["BEP", "Plan de ejecución BIM"],
                ["IFC", "Formato abierto de intercambio de modelos de construcción"],
                ["NSGA-II", "Algoritmo genético multiobjetivo no dominado, versión 2"],
                ["AG", "Algoritmo genético"],
                ["FEM", "Método de elementos finitos"],
                ["PCI", "Protección contra incendio"],
                ["BMS", "Sistema de gestión y monitoreo del edificio"],
                ["HVAC", "Climatización, ventilación y aire acondicionado"],
                ["EBAR", "Estación de bombeo de aguas residuales"],
                ["PTE", "Planta de tratamiento de efluentes (agua de lluvia)"],
                ["RSU", "Residuos sólidos urbanos"],
                ["ANDE", "Administración Nacional de Electricidad (Paraguay)"],
                ["PMR", "Persona con movilidad reducida"],
                ["USD, Gs", "Dólar estadounidense y guaraní paraguayo"],
            ]
        ),

        h1("Glosario"),
        p("Para facilitar la lectura a quien no es especialista, se define en palabras simples el significado de los términos técnicos más usados en el documento."),
        bullet("Pilar: elemento vertical de hormigón armado que transmite las cargas hacia abajo, hasta la fundación."),
        bullet("Viga: elemento horizontal que recoge las cargas de las losas y las lleva a los pilares o muros."),
        bullet("Losa: superficie plana y horizontal que separa dos pisos y recibe directamente las cargas de uso."),
        bullet("Losa nervada o alivianada: losa que en lugar de hormigón macizo tiene nervios y casetones huecos, para pesar menos."),
        bullet("Nervio: costilla de hormigón que contiene el acero de tracción en una losa nervada."),
        bullet("Casetón: molde hueco que se coloca entre nervios para alivianar la losa y darle fondo plano."),
        bullet("Capa de compresión: loseta delgada superior de la losa nervada, que trabaja a compresión."),
        bullet("Flexión: deformación de un elemento que se curva, con una cara comprimida y otra traccionada."),
        bullet("Cortante: esfuerzo que tiende a cortar un elemento, como una tijera."),
                bullet("Flecha: deformación vertical de una losa o viga bajo carga."),
        bullet("Deriva de piso: deformación horizontal relativa entre un piso y el siguiente, causada por el viento."),
        bullet("Núcleo: caja vertical de hormigón armado que contiene ascensores y escaleras y resiste el viento."),
        bullet("Pilar apeado: pilar que no llega a la fundación y nace sobre una losa; se busca evitarlo."),
        bullet("Grilla estructural: conjunto de ejes en planta donde se ubican los pilares."),
        bullet("Momento de vuelco: efecto del viento que tiende a volcar el edificio."),
        bullet("Ráfaga: golpe de viento de corta duración y velocidad superior al promedio."),
                bullet("Barlovento y sotavento: cara del edificio que enfrenta al viento y cara opuesta, respectivamente."),
        bullet("Cisterna: depósito de agua ubicado en los niveles bajos del edificio."),
        bullet("Tanque elevado: depósito de agua ubicado en la azotea, que da presión por gravedad."),
        bullet("Shaft: hueco vertical por donde suben las instalaciones entre pisos."),
    ];
};
