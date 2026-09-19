// =====================================================================
//  Capítulo 4: Descripción del Edificio.
//  Ampliado con los criterios de diseño de cada nivel.
// =====================================================================
const { h1, h2, h3, p, bullet, dataTable, figura, ref, pageBreak, FONT_BODY } = require("../estilos_y_helpers");
const { TextRun } = require("docx");
const { IMG } = require("../imagenes");

module.exports = function () {
    return [
        h1("Capítulo 4: Descripción del Edificio"),

        p("Este capítulo describe el edificio que se calcula en los capítulos siguientes. Se presenta primero el terreno y los parámetros generales; después cada nivel, de abajo hacia arriba: los tres Subsuelos de cocheras, la Planta Baja comercial y de servicios, los dieciocho niveles residenciales y la azotea. Para cada nivel se explican las decisiones de diseño y el motivo de cada una."),

        // ================================================================
        h2("4.1 Parámetros Maestros"),
        p([new TextRun({ text: "El terreno tiene 90,0 m de frente por 40,0 m de profundidad. Sobre él, el edificio ocupa una huella de 85,0 m por 37,0 m (de X: 2,5 m a X: 87,5 m, y de Y: 3,0 m a Y: 40,0 m). Esa huella da una superficie de 3.145,0 m² por nivel. La configuración definitiva se resume en la Tabla ", size: 22, font: FONT_BODY }),
            ref("tabla2_parametros", "2"),
            new TextRun({ text: ".", size: 22, font: FONT_BODY })]),
        ...dataTable(
            "tabla2_parametros",
            "Parámetros maestros definitivos del edificio.",
            [2600, 1600, 4300],
            ["Parámetro", "Valor", "Detalle"],
            [
                ["Terreno", "90,0 × 40,0 m", "3.600,0 m²"],
                ["Huella edificable", "85,0 × 37,0 m", "3.145,0 m² por nivel"],
                ["Núcleos H°A°", "2 × (7 × 9 m)", "Gemelos rotados 90°, N1 (X:34→41) y N2 (X:49→56), Y:17→26"],
                ["Subsuelos S1–S3", "3,50 m por nivel", "Cocheras: 278 plazas en total"],
                ["Planta Baja", "4,00 m libres", "Comercial + lobby + residuos + servicios"],
                ["P01–P18 residencial", "3,00 m libres (entrepiso 3,35 m)", "432 apartamentos en 3 disposiciones"],
                ["Azotea", "+64,30 m", "Salas de máquinas, tanques, terraza de eventos, piscina 8×16 m"],
            ]
        ),
        p("Dos decisiones atraviesan todo el proyecto. La primera es la ubicación de los dos núcleos de hormigón armado: son dos cajas de 7 m por 9 m, simétricas respecto del centro del edificio, rotadas 90° de modo que sus caras largas se miran entre sí, separadas por un pasillo técnico central de 8 m. Estos núcleos contienen los ascensores y la escalera de emergencia y, por su gran rigidez, serán los encargados de resistir la mayor parte del viento. La segunda decisión es la grilla estructural única: los cuatro bordes de los núcleos (X: 34, 41, 49 y 56, e Y: 17 y 26) se adoptaron como ejes estructurales exactos, de manera que los pilares acompañen a los núcleos en toda la altura."),

        // ================================================================
        h2("4.2 Subsuelos de Cocheras (S1, S2 y S3)"),
        p("El edificio tiene tres niveles de cocheras bajo el nivel de calle, con una altura de entrepiso de 3,50 m cada uno. Los tres comparten la misma huella y los mismos dos núcleos, y se designan S1 (el más cercano a la calle, cota -3,50 m), S2 (cota -7,00 m) y S3 (el más profundo, cota -10,50 m). En total suman 278 plazas de estacionamiento."),
        h3("4.2.1 Criterios de Diseño de las Cocheras"),
        p("El diseño de una cochera se rige por dimensiones mínimas que garanticen que los vehículos entren, circulen y estacionen con comodidad. En este proyecto se adoptaron los siguientes criterios:"),
        bullet("Módulo de cochera de 2,50 m de ancho por 5,00 m de fondo, con estacionamiento perpendicular a la circulación. Es la medida habitual para automóviles."),
        bullet("Pasillo de circulación de 6,00 m entre filas de cocheras enfrentadas, ancho suficiente para maniobrar y entrar de una sola vez."),
        bullet("Rampas vehiculares de 6,00 m de ancho, con dos carriles, para el ingreso y el egreso."),
        bullet("Ubicación de los núcleos de ascensores y escalera dentro del área de cocheras, con puertas cortafuego, para que el usuario llegue a su vehículo sin cruzar zonas de riesgo."),
        p("El número de plazas no se fijó de antemano: se calculó empaquetando geométricamente las cocheras dentro de las zonas libres de pilares, núcleos y rampas, respetando el módulo y los pasillos. El resultado fue de 82 plazas en S1 (70 autos y 12 motos) y 98 plazas en cada uno de los dos subsuelos siguientes (80 autos y 18 motos), lo que da un total de 278 plazas."),
        h3("4.2.2 Circulación y Rampas"),
        p("En los Subsuelos S2 y S3 se dispuso una doble rampa de esquina a esquina: el vehículo entra por la esquina sureste y sale por la esquina noroeste, recorriendo el subsuelo en diagonal. Esta solución separa los flujos de entrada y salida y evita cruces peligrosos. En el Subsuelo S1, en cambio, se adoptó una rampa única en la esquina noreste, mirando hacia el oeste."),
        h3("4.2.3 Salas Técnicas"),
        p("El Subsuelo S1 aloja además las salas técnicas principales del edificio, agrupadas en un bloque central para que las cañerías entre ellas sean cortas: las cisternas y bombas de agua potable y de agua contra incendio, el grupo electrógeno de emergencia, el tablero general, la planta de tratamiento del agua de lluvia y el taller de mantenimiento. La planta de tratamiento cloacal (llamada EBAR) se ubica aparte, en la esquina sureste. Las plantas de los tres subsuelos se muestran en las Ilustraciones 3, 4 y 5."),
        ...figura(IMG.s3, 560, 300, "fig_s3", "Planta del Subsuelo 3 (S3) — cocheras (98 plazas)."),
        ...figura(IMG.s2, 560, 300, "fig_s2", "Planta del Subsuelo 2 (S2) — cocheras (98 plazas)."),
        ...figura(IMG.s1, 560, 300, "fig_s1", "Planta del Subsuelo 1 (S1) — cocheras (82 plazas) + bloque técnico + rampa única noreste."),

        // ================================================================
        h2("4.3 Planta Baja Comercial y de Servicios"),
        p("La Planta Baja se encuentra a la cota 0,00 m, es decir, al nivel de la calle, y tiene 4,00 m de altura libre. Es el nivel que conecta el edificio con la ciudad: aquí se ubican el acceso principal, los locales comerciales y los servicios que atienden tanto al público como a los residentes. Su superficie es de 3.145,0 m²."),
        h3("4.3.1 Locales Comerciales"),
        p("La Planta Baja incluye cinco locales comerciales flexibles: cuatro salones de 282 m² cada uno y un local mayor, llamado Megastore, de 336 m². Una decisión de diseño importante es que estos locales se entregan sin distribución interna: son espacios libres que el arrendatario organiza según su actividad. El edificio aporta el perímetro, los servicios y la estructura, no la compartimentación. Por ese motivo no se desarrolla micro-distribución en su interior."),
        h3("4.3.2 Lobby y Circulación"),
        p("En el centro de la planta, un lobby de aproximadamente 135 m² conecta los dos núcleos de ascensores y escaleras y sirve de acceso común tanto a los locales como a la torre residencial. El lobby concentra la recepción, la espera y el control de accesos."),
        h3("4.3.3 Zonas de Servicio"),
        p("Alrededor del lobby se distribuyen las zonas de servicio del edificio:"),
        bullet("Complejo de administración y BMS (380 m²): oficinas de administración del edificio y sala de monitoreo de los sistemas."),
        bullet("Sanitarios públicos con cabina para personas con movilidad reducida y lactario (228 m²)."),
        bullet("Centro de negocios y espacio de trabajo compartido (200 m²)."),
        bullet("Depósito central de residuos sólidos urbanos (228 m²), al que llega el ducto vertical de basura y donde se coloca el contenedor basculante que retira el camión recolector desde la calle, sin necesidad de entrar al subsuelo."),
        bullet("Subestación eléctrica de la ANDE (60 m²), reservorios de agua potable y contra incendio (60 m²) y pasillo técnico central de servicios (135 m²)."),
        p("La Planta Baja se muestra en la Ilustración 6 (masterplan) y sus micro-distribuciones en las Ilustraciones 7 a 10."),
        ...figura(IMG.pb, 600, 325, "fig_pb", "Masterplan de Planta Baja (3.145,0 m²) con superposición de pilares estructurales."),
        ...figura(IMG.adm, 560, 295, "fig_adm", "Micro-distribución del Complejo de Administración y BMS (380 m²)."),
        ...figura(IMG.san, 560, 295, "fig_san", "Sanitarios Públicos + PMR + Lactario (228 m²)."),
        ...figura(IMG.biz, 560, 295, "fig_biz", "Centro de Negocios + Coworking (200 m²)."),
        ...figura(IMG.rsu, 560, 295, "fig_rsu", "Depósito Central de Residuos RSU (228 m²) con contenedor basculante."),

        // ================================================================
        h2("4.4 Planta Tipo Residencial (P01–P18)"),
        p("Sobre la Planta Baja se elevan dieciocho niveles residenciales, desde P01 hasta P18. Cada nivel tiene 3,00 m de altura libre, que con el espesor de la losa de 35 cm da un entrepiso de 3,35 m. El programa total del edificio es de 432 apartamentos."),
        h3("4.4.1 Tres Disposiciones Intercaladas"),
        p("Para dar variedad y adaptarse a distintos tipos de familia, los dieciocho pisos no repiten todos la misma planta. Se definieron tres disposiciones distintas, que se intercalan en el orden A-C-B repetido:"),
        bullet("Disposición A — apartamentos pequeños (~62 m², de 1 a 2 dormitorios): 16 unidades por banda, 32 por piso. Se ubica en los pisos P01, P04, P07, P10, P13 y P16."),
        bullet("Disposición C — apartamentos combinados (~83 m², mezcla de pequeños, medianos y grandes): 12 unidades por banda, 24 por piso. Se ubica en los pisos P02, P05, P08, P11, P14 y P17."),
        bullet("Disposición B — apartamentos grandes (~125 m², 3 dormitorios): 8 unidades por banda, 16 por piso. Se ubica en los pisos P03, P06, P09, P12, P15 y P18."),
        p("Con este patrón, el último piso (P18) queda con apartamentos grandes y los 432 apartamentos se reparten en 192 pequeños, 144 combinados y 96 grandes."),
        h3("4.4.2 Organización de Cada Unidad"),
        p("El edificio se organiza en dos bandas de departamentos separadas por los núcleos y los pozos de luz. La banda sur da a la calle y la banda norte da al contrafrente. En cada banda, la unidad se ordena de afuera hacia adentro en tres zonas: la zona social (living y comedor) hacia la fachada, la zona de servicio (cocina y patio de servicio) en el medio, y la zona privada (dormitorios y baños) hacia el interior. Cada unidad cuenta con balcón exterior."),
        h3("4.4.3 Ventilación Natural"),
        p("Una preocupación central fue que todos los baños y cocinas tengan ventilación natural, sin depender de equipos. Para lograrlo se usaron tres recursos: un patio de servicio dentro de cada departamento, al que abren la cocina y el baño principal; los dos grandes pozos de luz (A y B, de 14 m por 7 m cada uno), a los que dan los baños de las unidades vecinas; y, solo para los inodoros de visita que no tienen ventana, un ducto de extracción mecánica de 200 mm de diámetro que sube hasta la azotea."),
        p("Las tres disposiciones (A, B y C) se muestran en las Ilustraciones 11, 12 y 13, y el esquema de intercalación en los 18 pisos residenciales, en la Ilustración 14."),
        ...figura(IMG.a, 600, 296, "fig_a", "Disposición A — apartamentos pequeños (~62 m²), en P01, P04, P07, P10, P13 y P16."),
        ...figura(IMG.b, 600, 296, "fig_b", "Disposición B — apartamentos grandes (~125 m²), en P03, P06, P09, P12, P15 y P18."),
        ...figura(IMG.c, 600, 296, "fig_c", "Disposición C — apartamentos combinados (~83 m²), en P02, P05, P08, P11, P14 y P17."),
        ...figura(IMG.inter, 600, 64, "fig_inter", "Esquema de intercalación de las disposiciones A, C y B en los 18 pisos residenciales."),

        // ================================================================
        h2("4.5 Azotea Técnica y de Esparcimiento"),
        p("La azotea se encuentra a la cota +64,30 m y combina dos usos: la zona técnica que da servicio a todo el edificio y las áreas de esparcimiento para los residentes. Reunir ambos usos en un solo nivel permite aprovechar una única losa de azotea, reforzada para soportar las cargas especiales de tanques y piscina."),
        h3("4.5.1 Zona Técnica"),
        p("Sobre cada núcleo se ubican las salas de máquinas de los ascensores. En el centro, sobre los dos núcleos y el corredor que los une, se apoya un bloque único de tanques elevados de agua, dividido por un muro intermedio en dos celdas: una para agua potable y otra para agua contra incendio, de aproximadamente 120 m³ cada una. También hay una sala para equipos de climatización y un cuarto de tableros."),
        h3("4.5.2 Zona de Esparcimiento"),
        p("En el sector del fondo se ubican la terraza de eventos con su quincho y parrilla cubierta, el solárium y una piscina recreativa de 8 m por 16 m con una profundidad de 1,20 m a 1,80 m. Los dos pozos de luz no se cubren: quedan como aberturas con baranda perimetral. La planta completa se muestra en la Ilustración 15."),
        ...figura(IMG.az, 600, 324, "fig_az", "Plano de Azotea Técnica y de Esparcimiento (terraza de eventos + piscina 8×16 m)."),

        // ================================================================
        h2("4.6 Envolvente y Fachada"),
        p("La fachada cumple dos funciones: proteger del clima y controlar la entrada de sol. En Ciudad del Este, de clima cálido y húmedo, el control del asoleamiento es importante para reducir el consumo de energía en refrigeración. Por eso la fachada se estudió considerando estrategias de sombreamiento, y también su respuesta frente al viento, que se analiza en el Capítulo 6. La Ilustración 16 presenta el análisis de estrategias."),
        ...figura(IMG.fach, 560, 340, "fig_fach", "Fachada sur — análisis de estrategias de sombreamiento y viento."),

        pageBreak(),
    ];
};
