// =====================================================================
//  Capítulo 6: Análisis de la Acción del Viento.
//  Teoría de las normas explicada con Ecuaciones Nativas de Word (OMML)
//  y desglose pedagógico de variables ("Donde:").
// =====================================================================
const {
    h1, h2, h3, p, bullet, pageBreak, FONT_BODY,
    eqBlock, eqDonde, mathInline, mRun, mSub, mSup, mFrac, mRad, mBrackets
} = require("../estilos_y_helpers");
const { TextRun } = require("docx");

module.exports = function () {
    return [
        h1("Capítulo 6: Análisis de la Acción del Viento"),

        p("El edificio de este trabajo tiene unos 68 m de altura hasta la azotea y una planta alargada de 85 m por 37 m. Con esas dimensiones, el viento deja de ser un detalle y pasa a ser, muy probablemente, la solicitación horizontal que gobierna el diseño. Este capítulo explica, primero, los conceptos que comparten las normas; después, cómo calcula el viento cada una de ellas, empezando por la norma paraguaya NP 196:1991 y siguiendo con la NBR 6123 de Brasil, el ASCE 7-22 de Estados Unidos y el Eurocódigo 1 de Europa; y finalmente, cómo se aplican al edificio para obtener las presiones, el cortante en la base, el momento de vuelco, las deformaciones de piso y el confort de los ocupantes."),

        // ================================================================
        h2("6.1 Por Qué Dos Códigos No Dan el Mismo Resultado"),
        p("Antes de ver las fórmulas conviene entender una idea clave: no existe una única manera de calcular el viento. Cada norma nació en un país con un clima distinto y con una historia distinta de accidentes y de investigación. La NBR 6123 (Brasil) fue pensada para un país sin huracanes pero con vientos fuertes de tormenta; el ASCE 7-22 (Estados Unidos) incorpora procedimientos especiales para huracanes y tornados; el Eurocódigo 1 (Europa) pone mucho énfasis en la respuesta dinámica y en la turbulencia. Por eso, ante el mismo edificio y la misma velocidad de viento, las tres normas arrojan presiones diferentes. Cuantificar esa diferencia es uno de los objetivos de esta tesis."),
        p("Paraguay cuenta con la NP 196:1991, pero se trata de una norma clásica de alcance estático, que no cubre el efecto dinámico del viento en edificios esbeltos. Por ese motivo este trabajo la adopta como norma nacional y, además, compara sus resultados con los de tres códigos internacionales: para saber cuál es más conservador y cuál conviene usar como complemento en Ciudad del Este."),

        // ================================================================
        h2("6.2 Conceptos Comunes a las Normas"),

        h3("6.2.1 La Velocidad Básica del Viento"),
        p([
            new TextRun({ text: "Todo cálculo de viento parte de la velocidad básica de ráfaga (", size: 22, font: FONT_BODY }),
            mathInline([mSub("V", "0")]),
            new TextRun({ text: " o ", size: 22, font: FONT_BODY }),
            mathInline([mRun("V")]),
            new TextRun({ text: "), que representa la ráfaga de 3 segundos superada una vez cada 50 años a 10 m de altura en terreno abierto plano.", size: 22, font: FONT_BODY })
        ]),

        h3("6.2.2 La Presión Dinámica Fundamental"),
        p("La energía cinética del flujo de aire se transforma en presión estática sobre la superficie mediante la ecuación fundamental de Bernoulli:"),
        
        eqBlock([
            mRun("q = "),
            mFrac("1", "2"),
            mRun(" · ρ · "),
            mSup("V", "2")
        ], "6.1"),

        ...eqDonde([
            [mRun("q"), "presión dinámica del viento ejercida sobre una superficie perpendicular (N/m² o Pa)."],
            [mRun("ρ"), "densidad de masa del aire atmosférico (adoptada como 1,225 kg/m³ en condiciones estándar)."],
            [mRun("V"), "velocidad del viento incidente a la altura considerada (m/s)."]
        ]),

        p("Sustituyendo la densidad estándar del aire, la presión dinámica básica se simplifica a la forma universal empleada en las normativas regionales:"),

        eqBlock([
            mRun("q = 0,613 · "),
            mSup("V", "2")
        ], "6.2"),

        ...eqDonde([
            [mRun("q"), "presión dinámica calculada en newtons por metro cuadrado (N/m²)."],
            [mRun("0,613"), "factor de conversión dimensional correspondiente a ½ × 1,225 kg/m³."],
            [mRun("V"), "velocidad efectiva del viento expresada en metros por segundo (m/s)."]
        ]),

        h3("6.2.3 El Perfil de Velocidad y la Rugosidad del Terreno"),
        p("Cerca del suelo, el flujo es frenado por la fricción con el terreno y los obstáculos urbanos. A mayor altura el viento incrementa su velocidad siguiendo perfiles potenciales o logarítmicos caracterizados por la rugosidad del entorno."),

        h3("6.2.4 Los Coeficientes de Presión"),
        p("La presión neta sobre un cerramiento se determina multiplicando la presión dinámica por la diferencia entre los coeficientes de presión externa e interna:"),

        eqBlock([
            mRun("Δp = q · "),
            mBrackets([mSub("C", "pe"), mRun(" - "), mSub("C", "pi")])
        ], "6.3"),

        ...eqDonde([
            [mRun("Δp"), "presión estática neta efectiva actuante sobre el cerramiento o paramento (N/m²)."],
            [mRun("q"), "presión dinámica del viento a la cota del nivel analizado (N/m²)."],
            [mSub("C", "pe"), "coeficiente de presión externa (positivo para barlovento, negativo para sotavento y laterales)."],
            [mSub("C", "pi"), "coeficiente de presión interna (dependiente de la permeabilidad y aberturas del edificio)."]
        ]),

        // ================================================================
        h2("6.3 La Norma Paraguaya NP 196:1991"),
        p("La norma paraguaya NP 196:1991 («Acción del viento en las construcciones», INTN) evalúa la velocidad característica mediante factores de corrección topográfica y de rugosidad:"),

        eqBlock([
            mSub("V", "k"),
            mRun(" = "),
            mSub("V", "0"),
            mRun(" · "),
            mSub("S", "1"),
            mRun(" · "),
            mSub("S", "2")
        ], "6.4"),

        ...eqDonde([
            [mSub("V", "k"), "velocidad característica de cálculo del viento (m/s)."],
            [mSub("V", "0"), "velocidad básica de viento regional obtenida de la zonificación paraguaya (m/s)."],
            [mSub("S", "1"), "factor topográfico que contempla pendientes, valles o cimas del terreno (S₁ = 1,0 en terreno llano)."],
            [mSub("S", "2"), "factor combinado de rugosidad del terreno y altura sobre la cota del suelo."]
        ]),

        // ================================================================
        h2("6.4 La NBR 6123:2023 (Brasil)"),
        p("La norma brasileña NBR 6123 desglosa la velocidad característica incorporando además el factor estadístico de riesgo S3:"),

        eqBlock([
            mSub("V", "k"),
            mRun(" = "),
            mSub("V", "0"),
            mRun(" · "),
            mSub("S", "1"),
            mRun(" · "),
            mSub("S", "2"),
            mRun(" · "),
            mSub("S", "3")
        ], "6.5"),

        ...eqDonde([
            [mSub("V", "k"), "velocidad característica de ráfaga para el dimensionamiento (m/s)."],
            [mSub("V", "0"), "velocidad básica de isopletas para la región fronteriza (V₀ = 45 m/s para Ciudad del Este)."],
            [mSub("S", "1"), "factor topográfico (admitido S₁ = 1,00 para topografía plana a suave)."],
            [mSub("S", "2"), "factor de rugosidad, dimensiones de la edificación y variación con la altura z."],
            [mSub("S", "3"), "factor estadístico de seguridad según la vida útil y destino del edificio (S₃ = 1,00 para residencial/comercial)."]
        ]),

        p("A partir de la cual se calcula la presión dinámica característica de diseño:"),

        eqBlock([
            mRun("q = 0,613 · "),
            mSup(mSub("V", "k"), "2")
        ], "6.6"),

        // ================================================================
        h2("6.5 El ASCE/SEI 7-22 (Estados Unidos)"),
        p("El estándar estadounidense ASCE 7-22 define la presión por velocidad qz en cada cota z mediante la formulación:"),

        eqBlock([
            mSub("q", "z"),
            mRun(" = 0,613 · "),
            mSub("K", "z"),
            mRun(" · "),
            mSub("K", "zt"),
            mRun(" · "),
            mSub("K", "d"),
            mRun(" · "),
            mSub("K", "e"),
            mRun(" · "),
            mSup("V", "2")
        ], "6.7"),

        ...eqDonde([
            [mSub("q", "z"), "presión por velocidad evaluada a la altura z (N/m²)."],
            [mSub("K", "z"), "coeficiente de exposición a la presión por velocidad según la categoría de terreno."],
            [mSub("K", "zt"), "factor topográfico de elevación."],
            [mSub("K", "d"), "factor de direccionalidad del viento (Kd = 0,85 para edificios principales)."],
            [mSub("K", "e"), "factor de elevación sobre el nivel del mar."],
            [mRun("V"), "velocidad básica de viento para categoría de riesgo II (m/s)."]
        ]),

        // ================================================================
        h2("6.6 El Eurocódigo 1 — Parte 1-4 (EN 1991-1-4)"),
        p("El Eurocódigo 1 define la presión de velocidad de pico qp(z) integrando la velocidad media con la intensidad de turbulencia local Iv(z):"),

        eqBlock([
            mSub("q", "p"),
            mBrackets("z"),
            mRun(" = "),
            mBrackets([mRun("1 + 7 · "), mSub("I", "v"), mBrackets("z")]),
            mRun(" · "),
            mFrac("1", "2"),
            mRun(" · ρ · "),
            mSup(mSub("v", "m"), "2"),
            mBrackets("z")
        ], "6.8"),

        ...eqDonde([
            [mathInline([mSub("q", "p"), mBrackets("z")]), "presión de velocidad de pico a la cota z (N/m²)."],
            [mathInline([mSub("I", "v"), mBrackets("z")]), "intensidad de turbulencia a la altura z."],
            [mathInline([mSub("v", "m"), mBrackets("z")]), "velocidad media del viento a la cota z (m/s)."],
            [mRun("ρ"), "densidad del aire (1,25 kg/m³ según Eurocódigo)."]
        ]),

        // ================================================================
        h2("6.7 Determinación de Esfuerzos Globales en el Edificio"),
        p("Con las presiones obtenidas en cada piso se calculan las fuerzas horizontales totales, el cortante basal y el momento de vuelco en la base:"),

        eqBlock([
            mSub("V", "basal"),
            mRun(" = "),
            mRun("∑ "),
            mSub("F", "i")
        ], "6.9"),

        ...eqDonde([
            [mSub("V", "basal"), "fuerza cortante total en la base del edificio (kN o MN)."],
            [mSub("F", "i"), "fuerza horizontal estática equivalente concentrada en el nivel i (kN)."]
        ]),

        eqBlock([
            mSub("M", "vuelco"),
            mRun(" = "),
            mRun("∑ "),
            mBrackets([mSub("F", "i"), mRun(" · "), mSub("z", "i")])
        ], "6.10"),

        ...eqDonde([
            [mSub("M", "vuelco"), "momento de vuelco global en la cota de fundación (kN·m o MN·m)."],
            [mSub("z", "i"), "altura del nivel i respecto a la cota de empotramiento de la fundación (m)."]
        ]),

        p("Estos esfuerzos son absorbidos por los dos núcleos gemelos de hormigón armado de 7 m × 9 m y el pórtico perimetral de columnas, garantizando la estabilidad y el confort de la estructura."),

        pageBreak(),
    ];
};
