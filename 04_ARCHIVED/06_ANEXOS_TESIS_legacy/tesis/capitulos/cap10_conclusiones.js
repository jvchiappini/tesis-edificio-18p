// =====================================================================
//  Capítulo 10: Conclusiones y Recomendaciones.
// =====================================================================
const { h1, h2, h3, p, bullet, pageBreak } = require("../estilos_y_helpers");

module.exports = function () {
    return [
        h1("Capítulo 10: Conclusiones y Recomendaciones"),

        // ================================================================
        h2("10.1 Conclusiones"),
        p("El trabajo permitió desarrollar, de principio a fin, el diseño de un edificio de uso mixto de 18 niveles, desde la definición del sistema estructural hasta el cómputo de materiales, aplicando normas reconocidas y verificando cada resultado por dos caminos independientes. Las conclusiones se ordenan según cada objetivo planteado."),
        h3("10.1.1 Sobre la Macro Distribución y la Grilla Estructural"),
        p("La macro distribución de los niveles y la grilla estructural se resolvieron por diseño directo, asistido por scripts paramétricos en Python y refinado a mano. Este enfoque es el correcto para este tipo de problema: como la solución válida está fuertemente condicionada por el terreno, por los dos núcleos gemelos y por las luces de los locales comerciales, no hay muchas alternativas entre las que elegir, y un optimizador no aportaría valor. El resultado es una grilla única y continua, alineada a los núcleos, con un módulo de 7,875 m en las alas, que cumple el objetivo central: el 100 % de los pilares conserva la continuidad vertical, no hay pilares apeados y los pilares se ubican sobre las divisiones de los locales o sobre los ejes de los muros."),
        h3("10.1.2 Sobre la Selección del Sistema de Entrepiso"),
        p("La comparación de cinco sistemas de entrepiso, realizada sobre la misma grilla y con precios verificados del mercado paraguayo, ubicó a la losa nervada o reticular alivianada como la opción más económica, con 68,8 USD/m² y un costo total de 4,72 millones de dólares sobre los 68.611 m² de losa. El análisis de sensibilidad confirmó que esta conclusión es robusta: la losa nervada gana en todos los escenarios evaluados, incluso en el más favorable a su competidora más cercana, la losa postensada. El pórtico convencional de losa maciza resultó un 51 % más caro."),
        h3("10.1.3 Sobre el Diseño de Hormigón Armado"),
        p("El cálculo manual de la losa nervada bajo las normas ACI 318-19 y NBR 6118 fue verificado con el modelo de elementos finitos de PyNite, y ambos resultados coincidieron exactamente (momento negativo de 60,23 kN·m, momento positivo de 33,88 kN·m, corte de 38,24 kN y flecha de 6,2 mm frente a un límite de 16,4 mm). Esta coincidencia valida la metodología de doble verificación del proyecto y confirma que la geometría adoptada, con canto de 35 cm, cumple todas las verificaciones de flexión, corte, adherencia y deformación. Las secciones de los pilares, variables por grupos de niveles, permiten optimizar el material sin perder seguridad ni continuidad."),
        h3("10.1.4 Sobre la Configuración Arquitectónica"),
        p("La configuración definitiva —tres Subsuelos de cocheras con 278 plazas, una Planta Baja comercial y de servicios, dieciocho niveles residenciales con 432 apartamentos en tres disposiciones intercaladas y una azotea técnica con terraza y piscina— cumple el programa funcional de un edificio de uso mixto y responde a los criterios de diseño planteados: ventilación natural de baños y cocinas, balcones en todas las unidades, circulación vehicular segregada y recolección de residuos sin ingreso al subsuelo."),
        h3("10.1.5 Sobre la Metodología BIM"),
        p("La implementación del flujo de trabajo BIM bajo ISO 19650, con un entorno común de datos, una nomenclatura única y la interoperabilidad mediante archivos IFC, garantiza la trazabilidad de la información y permite coordinar todas las disciplinas sobre un modelo compartido. La detección de interferencias sobre el modelo federado, antes de la obra, es el mecanismo que evita los sobrecostos y atrasos que suelen aparecer cuando los conflictos se resuelven en el terreno."),
        h3("10.1.6 Conclusión General"),
        p("En conjunto, el trabajo demuestra que es posible diseñar un edificio de gran altura combinando, en una misma metodología, el diseño directo asistido por scripts, la optimización algorítmica aplicada donde realmente aporta, el cálculo estructural bajo norma, el análisis del viento y la gestión BIM. El criterio rector es usar cada herramienta para lo que sirve: los scripts paramétricos para trazar y ordenar la macro distribución, el algoritmo genético para las arquitecturas interiores que admiten muchas variantes, el cálculo manual y el programa para verificar. Este uso equilibrado de las herramientas, y no la aplicación indiscriminada de un optimizador, constituye el principal aporte metodológico de esta tesis."),

        // ================================================================
        h2("10.2 Recomendaciones y Trabajos Futuros"),
        p("El trabajo deja planteadas varias líneas que conviene completar para llevar el proyecto al nivel de una obra ejecutiva."),
        bullet("Completar el análisis del viento adoptando la norma paraguaya NP 196:1991 y comparándola con la NBR 6123, el ASCE 7-22 y el Eurocódigo 1, para identificar la norma más conservadora e integrar esos resultados al dimensionamiento de los núcleos y los pilares."),
        bullet("Desarrollar en detalle el dimensionamiento de los pilares a flexocompresión biaxial, los núcleos, el muro de contención y la fundación en el anexo de cálculo."),
        bullet("Aportar el estudio geotécnico y topográfico del terreno, que es un dato del sitio indispensable para definir la fundación, el muro de contención y el sistema de agotamiento."),
        bullet("Reproducir el diseño de la losa nervada en un programa comercial de emparrillado, como CYPE, para validar el comportamiento bidireccional de la retícula."),
        bullet("Modelar el edificio completo en Revit 2024, incluidas las instalaciones, y ejecutar la detección de interferencias entre todas las disciplinas."),
        bullet("Completar los cómputos métricos, el presupuesto definitivo con cotizaciones reales de proveedores y el cronograma de obra detallado."),
        bullet("Verificar la respuesta dinámica del edificio frente al viento y el confort de los ocupantes en los pisos superiores, según la norma ISO 6897."),

        pageBreak(),
    ];
};
