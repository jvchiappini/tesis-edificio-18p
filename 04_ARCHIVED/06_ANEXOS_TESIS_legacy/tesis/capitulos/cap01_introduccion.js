// =====================================================================
//  Capítulo 1: Introducción.
//  Orden: Planteamiento -> Preguntas abiertas -> Objetivos ->
//  Justificación -> Hipótesis -> Alcance -> Programa -> Guía de lectura.
// =====================================================================
const { h1, h2, h3, p, bullet, dataTable, ref, pageBreak, FONT_BODY } = require("../estilos_y_helpers");
const { TextRun } = require("docx");

module.exports = function () {
    return [
        h1("Capítulo 1: Introducción"),

        // ================================================================
        h2("1.1 Planteamiento del Problema"),
        p("Ciudad del Este, capital del Departamento de Alto Paraná, es uno de los polos comerciales y de servicios más dinámicos del Paraguay. Su crecimiento demográfico y económico impulsa una densificación urbana vertical: cada vez se construyen más edificios en altura sobre terrenos que antes ocupaban casas bajas. Esta tendencia demanda edificaciones de uso mixto, es decir, que combinen locales comerciales, cocheras y viviendas, capaces de aprovechar el suelo y de dar rentabilidad al inversor. Sin embargo, construir en altura introduce desafíos técnicos que el diseño tradicional, hecho por partes y sin coordinación, no resuelve de manera integral."),
        p("El primer desafío es estructural. Un edificio alto pesa mucho y recibe fuerzas horizontales importantes del viento. Si la estructura no se piensa desde el principio junto con la arquitectura, aparecen los llamados pilares apeados: columnas que nacen sobre una losa y no continúan hasta abajo. Estos pilares obligan a usar losas de transición enormes, encarecen la obra y son una fuente de riesgos. La experiencia profesional indica que lo correcto es definir una grilla de pilares continua y regular desde el último subsuelo hasta la azotea, de modo que cada pilar transmita su carga directamente a la fundación."),
        p("El segundo desafío es la acción del viento. En un edificio de 18 niveles, el viento es la fuerza horizontal más importante y, muchas veces, la que gobierna el dimensionamiento de la estructura. Paraguay cuenta con la norma NP 196:1991, «Fuerzas del viento en las construcciones», pero se trata de una norma antigua y de alcance limitado, por lo que muchos proyectistas locales complementan el cálculo con códigos internacionales. Eso plantea una pregunta legítima: ¿cuánto cambian los resultados según la norma que se adopte? Para responderla, este trabajo adopta la norma paraguaya NP 196:1991 y la compara con tres normas internacionales de referencia: la NBR 6123 de Brasil, el ASCE 7-22 de Estados Unidos y el Eurocódigo 1 de Europa."),
        p("El tercer desafío es de gestión de la información. En la construcción tradicional, la arquitectura, la estructura y las instalaciones se desarrollan por separado, cada una en sus propios planos. Esa fragmentación genera errores: cañerías que chocan con vigas, pérdidas de tiempo y reprocesos. La metodología BIM, ordenada por la norma internacional ISO 19650, propone trabajar sobre un modelo digital único y compartido, donde todas las disciplinas se coordinan y la información queda trazada durante todo el proyecto."),
        p("En síntesis, el problema de investigación se configura en torno a tres dimensiones que se entrelazan: (i) lograr una estructura de hormigón armado eficiente y con continuidad vertical plena; (ii) evaluar con rigor la acción del viento mediante normas internacionales comparadas, ante la ausencia de un código local; y (iii) implementar un flujo de trabajo BIM conforme a ISO 19650 que integre la optimización del diseño con la coordinación de todas las disciplinas."),

        // ================================================================
        h2("1.2 Preguntas de Investigación"),
        p("De lo anterior surgen las preguntas que guían este trabajo. Se formulan de manera abierta, es decir, de modo que no puedan responderse con un simple sí o no, sino que obliguen a explicar cómo se hace, cuáles son los resultados y de qué manera se logra cada objetivo:"),
        bullet("¿Cómo lograr una distribución espacial y una grilla estructural de un edificio de uso mixto de 18 niveles que maximice la superficie útil y garantice el 100 % de continuidad vertical de los elementos resistentes, evitando los pilares apeados?"),
        bullet("¿Cuáles son las presiones, las succiones, los cortantes en la base, los momentos de vuelco y las deformaciones de piso que el viento produce sobre este edificio, y cuáles son las diferencias cuantitativas entre los resultados de la NP 196:1991, la NBR 6123, el ASCE 7-22 y el Eurocódigo 1?"),
        bullet("¿Cómo se dimensionan y se verifican los elementos de hormigón armado (losas nervadas, pilares, núcleos y fundaciones) bajo las solicitaciones combinadas del peso propio y del viento, en los estados límites últimos y de servicio, incluyendo el confort de los ocupantes en el último piso?"),
        bullet("¿De qué manera la metodología BIM bajo la norma ISO 19650, apoyada en el modelado paramétrico y en la optimización de las arquitecturas interiores, permite integrar y coordinar la información de las disciplinas de arquitectura, estructura e instalaciones, reduciendo las interferencias y los reprocesos?"),

        // ================================================================
        h2("1.3 Objetivos"),

        h3("1.3.1 Objetivo General"),
        p("Desarrollar el diseño arquitectónico y estructural, la optimización de las arquitecturas interiores por algoritmos genéticos y el modelado de la información de la construcción (BIM) bajo la norma ISO 19650 de un edificio de uso mixto de 18 niveles sometido a la acción del viento, evaluado en el contexto urbano y normativo de Ciudad del Este, Paraguay."),

        h3("1.3.2 Objetivos Específicos"),
        bullet("Definir por diseño directo, asistido por scripts paramétricos y refinado a mano, las macro distribuciones de la Planta Baja, la planta tipo y la azotea, y la grilla estructural de pilares alineada a los núcleos gemelos."),
        bullet("Formular un algoritmo genético multiobjetivo (NSGA-II) que optimice las arquitecturas interiores de los departamentos y las micro-distribuciones de la Planta Baja, minimizando pasillos y maximizando la calidad de los espacios."),
        bullet("Diseñar la distribución arquitectónica de los tres Subsuelos de cocheras (278 plazas), la Planta Baja comercial y logística (3.145,0 m²) y los dieciocho niveles residenciales (432 apartamentos en tres disposiciones intercaladas)."),
        bullet("Seleccionar el sistema estructural de entrepiso más económico mediante una comparación de costos de cinco alternativas, con análisis de sensibilidad de los precios."),
        bullet("Consolidar dos núcleos gemelos rígidos de hormigón armado que concentren los servicios verticales (ascensores, escalera de emergencia y ducto de residuos) y absorban los esfuerzos cortantes del viento."),
        bullet("Aplicar la norma paraguaya NP 196:1991 y las normas internacionales NBR 6123, ASCE 7-22 y Eurocódigo 1 para calcular las presiones, los cortantes en la base, los momentos de vuelco y las deformaciones, y comparar cuantitativamente los resultados."),
        bullet("Dimensionar y verificar los elementos de hormigón armado (losas nervadas, pilares, núcleos y fundaciones) bajo los estados límites últimos y de servicio, documentando el cálculo manual y su verificación con programas en el anexo de cálculo."),
        bullet("Implementar el flujo de trabajo BIM bajo ISO 19650 (Plan de Ejecución BIM, entorno común de datos y nomenclatura) integrando los scripts de optimización con el modelado en Revit 2024."),

        // ================================================================
        h2("1.4 Justificación"),
        p("La pertinencia de este trabajo se sustenta en tres contribuciones: técnica, normativa y metodológica."),
        p("Desde el punto de vista técnico, el diseño directo de la macro distribución y la alineación de la grilla a los núcleos permiten cuantificar cuánto hormigón y cuánto acero se ahorra al garantizar la continuidad vertical de los pilares y su ubicación sobre ejes de muros. Además, recalcular las secciones de los pilares por grupos de niveles, en lugar de usar una sección constante y arbitraria, optimiza el consumo de materiales sin resignar seguridad."),
        p("Desde el punto de vista normativo, el trabajo adopta la norma paraguaya NP 196:1991 y la compara con tres códigos internacionales de uso extendido. Como la NP 196 es una norma antigua, contrastarla con la NBR 6123, el ASCE 7-22 y el Eurocódigo 1 aporta evidencia cuantitativa sobre cuánto influye la elección de la norma en el dimensionamiento y permite identificar la más conservadora. Esta información es de alto valor para los proyectistas locales y para las discusiones regulatorias del país, y muestra además la vigencia y las limitaciones de la norma nacional."),
        p("Desde el punto de vista metodológico, integrar el diseño directo, la optimización algorítmica de las arquitecturas interiores y la gestión BIM bajo ISO 19650, con un ajuste arquitectónico manual, demuestra un enfoque híbrido, replicable en otros proyectos y alineado con las tendencias internacionales del diseño asistido por computadora y de los entornos comunes de datos."),
        p("Finalmente, el trabajo tiene valor formativo y profesional: documenta de manera completa y pedagógica cómo se calcula un edificio real, desde la definición del sistema estructural hasta el cómputo de materiales, con todas las verificaciones exigidas por las normas. De este modo, cualquier lector sin conocimiento previo puede seguir el razonamiento y comprender por qué cada decisión fue tomada."),

        // ================================================================
        h2("1.5 Hipótesis de la Investigación"),
        bullet("H1: El diseño directo de la macro distribución, refinado manualmente, y una grilla estructural alineada a los núcleos gemelos logran que el 100 % de los pilares conserven la continuidad vertical y se ubiquen sobre ejes de muros, sin interferir los ambientes."),
        bullet("H2: La adopción de un módulo estructural de 7,875 m en las alas, coordinado con los locales comerciales y con los bordes de los núcleos, maximiza la regularidad estructural y la superficie útil frente a módulos alternativos."),
        bullet("H3: Los resultados de la acción del viento presentan diferencias cuantitativas importantes entre la NP 196:1991, la NBR 6123, el ASCE 7-22 y el Eurocódigo 1, y es posible identificar el código más conservador para el dimensionamiento en Ciudad del Este."),
        bullet("H4: Los dos núcleos gemelos de hormigón armado (7 m por 9 m, rotados 90°) absorben la mayor parte de los esfuerzos cortantes del viento y mantienen las deformaciones de piso dentro de los límites admisibles."),
        bullet("H5: El flujo de trabajo BIM bajo ISO 19650, con su entorno común de datos y su nomenclatura única, reduce las interferencias entre disciplinas y asegura la trazabilidad de la información durante todo el proyecto."),

        // ================================================================
        h2("1.6 Alcance"),
        p("El alcance del Trabajo de Grado comprende las siguientes actividades: el diseño de la distribución arquitectónica de los niveles y de la grilla estructural; la optimización de las arquitecturas interiores por algoritmos genéticos; la selección del sistema de entrepiso por costo; el análisis del viento bajo la norma paraguaya NP 196:1991 y tres normas internacionales; el diseño estructural de hormigón armado; el diseño conceptual de las instalaciones; los cómputos métricos; el presupuesto; el cronograma de obra; y la redacción del documento final de tesis."),
        p("Quedan fuera del alcance la micro-distribución interior de los salones comerciales de Planta Baja (que son espacios libres que define el arrendatario), la construcción material de la obra y el estudio geotécnico de detalle del terreno, que condiciona el proyecto de fundaciones y que es tarea del propietario contratar."),

        // ================================================================
        h2("1.7 Resumen del Programa Arquitectónico"),
        p([new TextRun({ text: "El edificio se organiza en cuatro grandes bloques funcionales: los tres Subsuelos de cocheras, la Planta Baja comercial y de servicios, los dieciocho niveles residenciales y la azotea técnica y de esparcimiento. La composición por niveles se resume en la Tabla ", size: 22, font: FONT_BODY }),
            ref("tabla1_programa", "1"),
            new TextRun({ text: ".", size: 22, font: FONT_BODY })]),
        ...dataTable(
            "tabla1_programa",
            "Resumen General del Programa Arquitectónico y Estructural por Niveles.",
            [1600, 2200, 1800, 3300],
            ["Nivel / Sector", "Cota / Altura", "Superficie por Nivel", "Destino Funcional"],
            [
                ["Subsuelos S1–S3", "-6,40 m a -3,20 m (3,20 m c/u)", "3.145,0 m²", "Cocheras (278 plazas) + salas técnicas (S1)"],
                ["Planta Baja (PB)", "0,00 m (4,00 m libres)", "3.145,0 m²", "5 locales comerciales + lobby + residuos + servicios"],
                ["Pisos P01–P18", "+4,00 m a +60,95 m (3,35 m c/u)", "2.949,0 m²", "Torre residencial (432 apartamentos, disposiciones A/C/B)"],
                ["Azotea (AZ)", "+64,30 m", "2.949,0 m²", "Salas de máquinas + tanques + terraza de eventos + piscina 8×16 m"],
            ]
        ),

        // ================================================================
        h2("1.8 Guía de Lectura del Documento"),
        p("Este documento está escrito con un criterio pedagógico: cada concepto se explica desde cero antes de usarlo. El Capítulo 2 presenta los fundamentos (qué es el hormigón armado, qué es la losa nervada, cómo actúa el viento, qué son los algoritmos genéticos y qué es BIM) y está pensado para que cualquier lector pueda entender el resto sin conocimientos previos. El Capítulo 3 describe la metodología de trabajo. El Capítulo 4 describe el edificio, planta por planta. El Capítulo 5 explica el sistema estructural adoptado y cómo se eligió por costo. El Capítulo 6 desarrolla el análisis del viento bajo la norma paraguaya y las tres normas internacionales. El Capítulo 7 desarrolla el diseño de cada elemento de hormigón armado, paso a paso. Los Capítulos 8 y 9 cubren las instalaciones, los cómputos, el presupuesto y el cronograma. El Capítulo 10 reúne las conclusiones. Finalmente, las referencias y los anexos completan el trabajo, con el desarrollo matemático detallado en el anexo de cálculo."),

        pageBreak(),
    ];
};

