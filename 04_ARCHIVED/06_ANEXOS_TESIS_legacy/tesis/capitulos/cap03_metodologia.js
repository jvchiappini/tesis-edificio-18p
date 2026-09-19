// =====================================================================
//  Capítulo 3: Metodología.
//  Ampliado: tipo de investigación, etapas, flujo de datos y control
//  de calidad del proyecto.
// =====================================================================
const { h1, h2, h3, p, bullet, pageBreak } = require("../estilos_y_helpers");

module.exports = function () {
    return [
        h1("Capítulo 3: Metodología"),

        // ================================================================
        h2("3.1 Tipo de Investigación y Enfoque"),
        p("Este trabajo es una investigación aplicada: no busca descubrir una ley nueva de la física, sino resolver un problema real de ingeniería, el diseño de un edificio de 18 niveles, aplicando y combinando los conocimientos y las normas existentes. El enfoque metodológico es híbrido, y esa palabra es importante: significa que el diseño no se resolvió ni solo a mano ni solo por computadora, sino combinando dos etapas que se complementan."),
        p("La primera etapa es de diseño directo, asistido por scripts paramétricos. La macro distribución de cada nivel y la grilla estructural están fuertemente condicionadas por el terreno, por los dos núcleos gemelos y por las luces de los locales comerciales, de modo que la solución válida es prácticamente única: no tiene sentido buscarla con un optimizador porque no hay muchas alternativas entre las que elegir. Se programaron entonces scripts en Python que trazan de manera ordenada la zonificación y la grilla, y esos esquemas se refinaron a mano con criterio arquitectónico. La segunda etapa es de optimización propiamente dicha, y se aplica a los problemas que sí admiten muchas variantes: las arquitecturas interiores de los departamentos y las micro-distribuciones de la Planta Baja, que se resuelven con el algoritmo genético NSGA-II."),
        p("Este enfoque híbrido tiene una virtud práctica: usa la computadora para lo que la computadora hace mejor (trazar la zonificación de forma ordenada y explorar, con el algoritmo genético, las muchas variantes de una arquitectura interior) y deja al ingeniero a cargo de las decisiones que requieren juicio, como las circulaciones, las vistas y la comodidad de cada ambiente. Es la forma de trabajo que hoy usan las consultoras de ingeniería más avanzadas."),

        // ================================================================
        h2("3.2 Regla de Oro del Trabajo: Ningún Dato se Inventa"),
        p("Todo el proyecto se apoya en una regla estricta: ningún dato técnico se inventa. Cada valor de carga, cada coeficiente de norma, cada precio y cada dimensión proviene de una de estas tres fuentes: una norma reconocida (NBR, ASCE, ACI, Eurocódigo, ISO), un documento del propio proyecto (planos, cómputos, informes) o una fuente verificable (cotizaciones, publicaciones técnicas). Cuando un dato no está disponible, en lugar de suponerlo se lo declara explícitamente como pendiente y se indica quién debe aportarlo. Esta disciplina es la que hace que el trabajo sea defendible: cualquier número puede rastrearse hasta su origen."),

        // ================================================================
        h2("3.3 Etapas del Desarrollo"),
        p("La investigación se desarrolló en etapas encadenadas, donde cada una aprovecha los resultados de la anterior. Se describen a continuación en su orden real de trabajo."),
        h3("3.3.1 Etapa de Fundamentos"),
        p("Se consolidó el marco teórico: qué es el hormigón armado, cómo trabaja una losa nervada, cómo actúa el viento sobre un edificio alto, qué son los algoritmos genéticos y en qué consiste la metodología BIM bajo ISO 19650. También se recopilaron las normas que se aplicarían y se definió el problema, las preguntas de investigación y los objetivos."),
        h3("3.3.2 Etapa de Macro Distribución y Grilla"),
        p("Se programaron los scripts en Python que trazan, de manera ordenada y determinista, la macro distribución de la Planta Baja, las tres disposiciones de planta tipo residencial, la azotea y la grilla estructural de pilares alineada a los núcleos gemelos. Como la solución está fuertemente condicionada por el terreno, los núcleos y las luces comerciales, estos scripts generan un único esquema válido, que luego se refina a mano. Los tres Subsuelos de cocheras se resolvieron directamente a mano."),
        h3("3.3.3 Etapa de Optimización Algorítmica"),
        p("Se aplicó el algoritmo genético NSGA-II, mediante la biblioteca DEAP de Python, a los problemas que admiten muchas alternativas: las arquitecturas interiores de los departamentos y las micro-distribuciones de la Planta Baja (administración y BMS, sanitarios públicos, centro de negocios y depósito de residuos). En cada caso el algoritmo parte de una población de soluciones, la evalúa según dos o tres objetivos y evoluciona durante decenas de generaciones hasta obtener un conjunto de soluciones equilibradas, entre las que se elige la definitiva."),
        h3("3.3.4 Etapa de Refinamiento Arquitectónico Manual"),
        p("Sobre los esquemas trazados por los scripts y las soluciones propuestas por el algoritmo, el proyectista ajustó circulaciones, accesos, ventilación y vistas. Este paso es el que convierte una solución técnicamente correcta en una solución arquitectónicamente buena."),
        h3("3.3.5 Etapa de Selección del Sistema Estructural"),
        p("Con la grilla de pilares ya fija, se compararon cinco sistemas de entrepiso distintos, calculando el costo de cada uno con los mismos pilares y los mismos precios. Se hizo además un análisis de sensibilidad, que consiste en mover los precios y volver a comparar, para comprobar si el sistema ganador sigue ganando aunque los precios cambien. El sistema adoptado fue la losa nervada."),
        h3("3.3.6 Etapa de Cálculo Estructural"),
        p("Se dimensionaron y verificaron todos los elementos de hormigón armado bajo las normas ACI 318-19 y NBR 6118: la losa nervada, los pilares, los núcleos y las fundaciones. Cada elemento se calculó primero a mano, siguiendo paso a paso la norma, y luego se verificó con un programa de elementos finitos (PyNite). Esta doble verificación, manual y por programa, es la que da confianza en los resultados."),
        h3("3.3.7 Etapa de Análisis del Viento"),
        p("Se desarrolló el cálculo del viento adoptando la norma paraguaya NP 196:1991 y comparándola con las normas internacionales NBR 6123, ASCE 7-22 y Eurocódigo 1, con planillas por nivel, y se compararon sus resultados para identificar la norma más conservadora."),
        h3("3.3.8 Etapa de Instalaciones, Cómputos y Coordinación"),
        p("Se diseñaron de manera conceptual las instalaciones del edificio (sanitarias, cloacales, pluviales, eléctricas, contra incendio y mecánicas), se calcularon los cómputos métricos de materiales, se armó el presupuesto y se definió el cronograma de obra. La coordinación entre disciplinas se planificó sobre modelos federados, con detección de interferencias."),
        h3("3.3.9 Etapa de Redacción del Documento"),
        p("Finalmente se redactó este documento, con sus figuras, tablas y el anexo de cálculo donde se desarrolla matemáticamente cada verificación."),

        // ================================================================
        h2("3.4 Flujo de Datos entre los Programas"),
        p("Una de las decisiones que más ordena el trabajo es que los programas no dupliquen información: cada dato vive en un solo lugar y los demás programas lo consultan. En la práctica, el modelo estructural de geometría es la fuente única de verdad de coordenadas y niveles; los scripts de optimización le pasan las grillas y las distribuciones; los módulos de cálculo toman esa geometría y le aplican las cargas y las normas. Así, si cambia una dimensión, el cambio se propaga sola y no hay planos contradictorios."),
        p("Ese flujo se apoya en la idea de interoperabilidad, que es una de las bases de BIM: los datos viajan de un programa a otro mediante formatos estándar (como IFC, entre Revit y Navisworks; o CSV y JSON, entre los scripts de Python y las planillas). De este modo, el modelo arquitectónico, el estructural y el de instalaciones pueden compararse entre sí y detectar interferencias antes de la obra."),

        // ================================================================
        h2("3.5 Herramientas y Normativas de Referencia"),
        bullet("Programas de modelado y coordinación: Autodesk Revit 2024 (versión 24.3.60.12, interfaz en inglés), formato IFC para intercambio, Navisworks para detección de interferencias y Dynamo para automatización."),
        bullet("Programas de cálculo y optimización: Python, con la biblioteca DEAP para los algoritmos genéticos NSGA-II; PyNite para el análisis de elementos finitos; CYPE para verificación comercial; y LaTeX (MiKTeX) para el anexo de cálculo."),
        bullet("Planillas y documentos: Microsoft Excel para cómputos y presupuesto, y Microsoft Word para el documento de tesis."),
        bullet("Normas de viento: NP 196:1991 (Paraguay), NBR 6123:2023 (Brasil), ASCE/SEI 7-22 (Estados Unidos) y Eurocódigo 1, parte 1-4 (EN 1991-1-4, Europa)."),
        bullet("Normas de hormigón y cargas: NBR 6118:2014, NBR 6120:2019, NBR 8681, ACI 318-19."),
        bullet("Normas de gestión de la información: ISO 19650, partes 1 y 2, y norma de confort por vibración ISO 6897."),

        // ================================================================
        h2("3.6 Control de Calidad del Trabajo"),
        p("El proyecto incorpora tres mecanismos de control de calidad que son, en sí mismos, un aporte metodológico. El primero es la doble verificación estructural: cada elemento se calcula a mano y se contrasta con un programa, y solo se acepta cuando ambos coinciden. El segundo es la verificación contra norma: cada dimensión y cada armadura se compara con los límites mínimos y máximos que exigen los reglamentos, de modo que ninguna solución sea insuficiente ni exagerada. El tercero es la trazabilidad de la información: cada archivo tiene un nombre único según la nomenclatura del proyecto, y cada dato puede rastrearse hasta su fuente. Estos tres controles son los que permiten afirmar que el trabajo se desarrolló con el mismo rigor con que una consultora profesional encararía una obra real."),

        pageBreak(),
    ];
};
