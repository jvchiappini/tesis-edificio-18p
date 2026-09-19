// =====================================================================
//  Capítulo 5: Sistema Estructural y Optimización Algorítmica.
//  Ampliado: formulación de la optimización, grilla, pilares, costos
//  y modelo 3D.
// =====================================================================
const { h1, h2, h3, p, bullet, dataTable, figura, ref, pageBreak, FONT_BODY } = require("../estilos_y_helpers");
const { TextRun } = require("docx");
const { IMG } = require("../imagenes");

module.exports = function () {
    return [
        h1("Capítulo 5: Sistema Estructural y Optimización Algorítmica"),

        // ================================================================
        h2("5.1 El Problema de la Grilla de Pilares"),
        p("La grilla de pilares es el conjunto de posiciones en planta donde se ubican las columnas del edificio. Es una decisión fundamental porque condiciona todo lo demás: dónde van las losas, cómo se reparten las cargas, dónde conviene apoyar las vigas y, sobre todo, si los espacios interiores quedan libres o cortados por una columna. Una grilla mal elegida obliga a apear pilares, es decir, a hacer nacer una columna sobre una losa en vez de continuarla hasta la fundación, lo que encarece la obra y complica la estructura."),
        p("Lo deseable es exactamente lo contrario: una grilla única y regular que se mantenga igual desde el último subsuelo hasta la azotea, de modo que cada pilar transmita su carga en línea recta hasta el suelo. En este proyecto, la posición de los pilares no se buscó con un optimizador automático, porque la solución válida está fuertemente condicionada: los cuatro bordes de los dos núcleos deben ser ejes estructurales, las luces de los locales comerciales deben respetarse y la huella la fija el terreno. Se trata, entonces, de un problema de diseño directo, que se resolvió con un script paramétrico en Python y se ordenó según los criterios que siguen."),

        // ================================================================
        h2("5.2 Criterios de Definición de la Grilla"),
        p("La grilla se definió aplicando cuatro criterios, en este orden de prioridad:"),
        bullet("Alineación a los núcleos: los cuatro bordes de cada núcleo gemelo (X: 34, 41, 49 y 56, e Y: 17 y 26) se adoptaron como ejes estructurales exactos, de modo que los pilares acompañen a los núcleos en toda la altura y la grilla quede simétrica respecto del centro del edificio."),
        bullet("Coordinación con los locales comerciales: en las dos alas se adoptó un módulo de 7,875 m, que coincide con el ancho natural de los salones comerciales, de manera que los pilares caigan sobre las divisiones y no dentro de los locales."),
        bullet("Continuidad vertical: todos los pilares conservan la misma posición en planta desde el Subsuelo S3 hasta la azotea, sin pilares apeados."),
        bullet("Regularidad: se buscó que los vanos fueran iguales entre sí, porque un vano distinto obliga a reforzar la losa y encarece la estructura."),
        p("Con esos criterios se obtuvo una grilla de doce ejes en la dirección X y seis en la dirección Y. El algoritmo genético NSGA-II no se emplea en esta etapa, porque no hay muchas alternativas entre las que elegir: se reserva para las arquitecturas interiores de los departamentos, donde el número de distribuciones posibles es enorme y el algoritmo sí aporta valor."),

        // ================================================================
        h2("5.3 La Grilla Estructural Adoptada"),
        p([new TextRun({ text: "La grilla definitiva es única y continua desde el Subsuelo S3 hasta la Azotea. Queda definida por doce ejes en la dirección X y seis ejes en la dirección Y, garantizando el 100 % de continuidad vertical de los pilares, es decir, sin pilares apeados. Los ejes se alinearon a los dos núcleos gemelos, de modo que los cuatro bordes de los núcleos (X: 34, 41, 49 y 56, e Y: 17 y 26) son ejes estructurales exactos. La Ilustración ", size: 22, font: FONT_BODY }),
            ref("fig_grilla", "17"),
            new TextRun({ text: " presenta la grilla adoptada y la Tabla ", size: 22, font: FONT_BODY }),
            ref("tabla3_grilla", "3"),
            new TextRun({ text: " resume las coordenadas de los ejes.", size: 22, font: FONT_BODY })]),
        ...dataTable(
            "tabla3_grilla",
            "Ejes de la grilla estructural adoptada.",
            [2600, 2200, 3200],
            ["Ejes", "Coordenadas (m)", "Vanos"],
            [
                ["X", "2,50 · 10,38 · 18,25 · 26,13 · 34,00 · 41,00 · 49,00 · 56,00 · 63,88 · 71,75 · 79,63 · 87,50", "Alas 7,875 m · Núcleos 7 m · Pasillo 8 m"],
                ["Y", "3,00 · 10,00 · 17,00 · 26,00 · 33,00 · 40,00", "Frente y fondo 7 m · Núcleos 9 m"],
            ]
        ),
        p("La lógica de la grilla es la siguiente: en las dos alas (de X: 2,50 a 34,00 y de X: 56,00 a 87,50) se repiten cuatro vanos iguales de 7,875 m, que es el módulo de referencia. Entre los núcleos, en X, quedan los vanos de 7 m de cada núcleo y el vano de 8 m del pasillo técnico central. En la dirección Y, hay dos vanos de 7 m al frente, la zona de los núcleos de 9 m y dos vanos de 7 m al fondo. Esta regularidad es la que permite que todos los paneles de losa sean casi cuadrados, condición ideal para que la losa reticular trabaje en dos direcciones."),
        ...figura(IMG.grilla, 620, 298, "fig_grilla", "Grilla estructural optimizada de pilares (continuidad S3–AZ)."),

        // ================================================================
        h2("5.4 Secciones de Pilares por Grupos de Niveles"),
        p("Con la posición de los pilares ya fijada, falta definir su tamaño. Aquí se aplica un criterio de economía: la sección del pilar no es la misma en toda la altura, sino que se reduce a medida que se sube, porque la carga que soporta también se reduce. El pilar de la planta baja debe sostener el peso de los 21 niveles que tiene encima; el pilar del último piso apenas sostiene su techo. Mantener una sección constante y grande en toda la altura desperdiciaría hormigón y acero."),
        p("El dimensionamiento se hace en función de las solicitaciones combinadas, es decir, la carga axial más el momento flector que produce el viento. Se definieron cuatro grupos de niveles con secciones decrecientes:"),
        bullet("Subsuelos y Planta Baja: sección de 90 × 90 cm, donde la carga axial máxima llega a unos 13,8 MN (unas 1.400 toneladas por pilar)."),
        bullet("Niveles inferiores de la torre: sección de 80 × 80 cm."),
        bullet("Niveles medios: sección de 70 × 70 cm."),
        bullet("Niveles superiores: sección de 60 × 60 cm."),
        p("Lo importante es que, aunque la sección cambia, la posición en planta no cambia: todos los pilares conservan el mismo eje de abajo hacia arriba. Así se logra, al mismo tiempo, continuidad estructural y ahorro de material. El cálculo de cada sección bajo flexocompresión biaxial se desarrolla en el Capítulo 7 y en el anexo de cálculo."),

        // ================================================================
        h2("5.5 Selección del Sistema de Entrepiso por Costo"),
        p("Con la grilla de pilares en posición fija, se planteó una comparación equitativa entre cinco sistemas de entrepiso distintos: losa nervada o reticular alivianada, vigueta pretensada con bovedilla, losa plana postensada, losa plana armada convencional y losa maciza con vigas interiores (pórtico). Como todos se calcularon sobre la misma grilla y con los mismos pilares, la comparación refleja la diferencia real de cada sistema, sin ventajas artificiales."),
        p([new TextRun({ text: "Los precios unitarios se tomaron de fuentes verificadas del mercado paraguayo: el generador de precios de CYPE (2025) y el listado de insumos de CAPACO (julio de 2025), con un tipo de cambio de 6.100 guaraníes por dólar. La comparación se hizo sobre 68.611 m² de losa. La Tabla ", size: 22, font: FONT_BODY }),
            ref("tabla4_comparativa", "4"),
            new TextRun({ text: " resume el orden de costos y la Ilustración ", size: 22, font: FONT_BODY }),
            ref("fig_comp", "18"),
            new TextRun({ text: " lo presenta gráficamente.", size: 22, font: FONT_BODY })]),
        ...dataTable(
            "tabla4_comparativa",
            "Comparación de sistemas de entrepiso por costo (68.611 m² de losa).",
            [500, 2800, 1000, 1300, 1300],
            ["Orden", "Sistema", "USD/m²", "Total (MMUSD)", "Peso propio (kN/m²)"],
            [
                ["1", "Losa nervada / reticular alivianada", "68,8", "4,72", "4,7"],
                ["2", "Vigueta pretensada + bovedilla", "69,1", "4,74", "4,3"],
                ["3", "Losa plana postensada + vigas perimetrales", "73,9", "5,07", "5,4"],
                ["4", "Losa plana armada convencional", "93,3", "6,40", "6,6"],
                ["5", "Losa maciza + vigas interiores (pórtico)", "104,0", "7,14", "6,6"],
            ]
        ),
        ...figura(IMG.comp, 620, 257, "fig_comp", "Comparación de costos de sistemas de entrepiso (USD/m² y costo total)."),
        ...figura(IMG.sens, 620, 257, "fig_sens", "Análisis de sensibilidad: la losa nervada (D) es la más económica en todos los escenarios."),
        p("El sistema más económico resultó la losa nervada o reticular alivianada, con 68,8 USD/m² y un costo total de 4,72 millones de dólares sobre los 68.611 m² de losa. La segunda opción, vigueta pretensada con bovedilla, quedó muy cerca, a 69,1 USD/m². El pórtico convencional de losa maciza resultó el más caro, un 51 % más que la losa nervada."),
        p("Para asegurar que esta conclusión no dependiera de un precio puntual, se hizo un análisis de sensibilidad: se movieron los precios del postensado entre 10 y 16 dólares por metro cuadrado, y se variaron los precios de los materiales en más y menos 15 %. El resultado fue contundente: la losa nervada ganó en todos los escenarios, incluso en el más favorable a la losa postensada, donde la diferencia se redujo a un mínimo del 2 %. Esta robustez es lo que permite afirmar que la elección no es casual sino sólida."),
        p("En consecuencia, se adoptó la losa nervada o reticular alivianada como sistema definitivo, con un canto de 35 cm en las plantas tipo y la azotea (capa de 10 cm más casetón de 25 cm) y de 45 cm en la Planta Baja y los Subsuelos, con nervios de 10 cm cada 60 cm. Se complementa con vigas de borde perimetrales, que ayudan a controlar la deformación por viento y sirven de apoyo a los balcones."),

        // ================================================================
        h2("5.6 Modelo Estructural Tridimensional"),
        p([new TextRun({ text: "Una vez definidos la grilla, los pilares y el sistema de entrepiso, se construyó un modelo tridimensional del edificio que reúne todos los elementos: 72 pilares continuos, 23 losas nervadas, los dos núcleos gemelos y las masas de la azotea (los tanques de agua y la piscina). Este modelo permite ver el edificio completo en tres dimensiones y obtener la carga axial de cada pilar según su altura. La carga máxima se produce en la base, en el Subsuelo S3, y alcanza aproximadamente 13,8 MN por pilar, valor que gobierna el dimensionamiento de los pilares y de la fundación. Las Ilustraciones ", size: 22, font: FONT_BODY }),
            ref("fig_m3d", "19"),
            new TextRun({ text: " y ", size: 22, font: FONT_BODY }),
            ref("fig_axial", "20"),
            new TextRun({ text: " presentan el modelo en elevación y el diagrama de carga axial por altura.", size: 22, font: FONT_BODY })]),
        ...figura(IMG.m3d, 430, 447, "fig_m3d", "Modelo estructural 3D en elevación (pilares, losas, núcleos y masas de azotea)."),
        ...figura(IMG.axial, 350, 486, "fig_axial", "Diagrama de carga axial acumulada por pilar según la altura (N máx ≈ 13,8 MN en S3)."),

        pageBreak(),
    ];
};
