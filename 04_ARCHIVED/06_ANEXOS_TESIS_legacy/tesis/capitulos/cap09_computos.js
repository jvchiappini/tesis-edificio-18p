// =====================================================================
//  Capítulo 9: Cómputos, Presupuesto, Método Constructivo y Cronograma.
// =====================================================================
const { h1, h2, h3, p, bullet, pageBreak } = require("../estilos_y_helpers");

module.exports = function () {
    return [
        h1("Capítulo 9: Cómputos, Presupuesto, Método Constructivo y Cronograma"),

        p("Calcular una estructura es necesario, pero no suficiente para construirla: también hay que saber cuánto material lleva, cuánto cuesta, cómo se construye y en qué orden. Este capítulo desarrolla esas cuatro cuestiones, que en un proyecto real son las que permiten tomar decisiones y contratar la obra."),

        // ================================================================
        h2("9.1 Cómputos Métricos"),
        p("Un cómputo métrico es la medición detallada de la cantidad de cada material o de cada tarea que exige la obra. Se calcula a partir del modelo: se mide el volumen de hormigón de cada elemento, el peso del acero de refuerzo, la superficie de encofrado y las unidades de cada instalación. El cómputo es la base del presupuesto, porque multiplicando cada cantidad por su precio unitario se obtiene el costo."),
        p("En este proyecto los cómputos se separan por sistema y por elemento. Para la estructura, se computan por un lado los pilares, por otro las losas nervadas, por otro los núcleos y por otro los muros de contención. Para cada uno se obtiene el volumen de hormigón en metros cúbicos, la masa de acero en kilogramos, según los planos de armado, y la superficie de encofrado en metros cuadrados. Para las instalaciones se computan las unidades de cañería, los artefactos, las bombas, los tableros y los equipos. Todos estos cómputos se vuelcan en planillas que acompañan al documento."),

        // ================================================================
        h2("9.2 Presupuesto de Estructura"),
        p("El presupuesto se arma multiplicando cada cantidad computada por su precio unitario. Los precios unitarios no se estiman a ojo: se toman de fuentes verificadas del mercado paraguayo, el generador de precios de CYPE (2025) y el listado de insumos de CAPACO (julio de 2025), con un tipo de cambio de 6.100 guaraníes por dólar. Como el sistema de entrepiso es el rubro que más pesa en el costo de la estructura, su análisis se hizo con especial detalle en el Capítulo 5."),
        p("El resultado principal de esa comparación es que la losa nervada, con 68,8 dólares por metro cuadrado, representa unos 4,72 millones de dólares sobre los 68.611 m² de losa del edificio. Ese número es el corazón del presupuesto de estructura y, a la vez, la justificación económica de haber elegido ese sistema: si se hubiera adoptado un pórtico convencional de losa maciza, el mismo entrepiso habría costado un 51 % más."),
        p("El presupuesto se completa con los rubros de fundaciones, muros de contención, núcleos, instalaciones y terminaciones. La comparación de los cinco sistemas de entrepiso se presentó en la Tabla 4, y el detalle de precios unitarios se documenta en las planillas del proyecto."),

        // ================================================================
        h2("9.3 Método Constructivo y Secuencia de Obra"),
        p("Pensar cómo se construye es parte del diseño: una solución muy elegante en el papel puede ser imposible de ejecutar. En este edificio, el método constructivo sigue una secuencia lógica que empieza desde el fondo y sube."),
        h3("9.3.1 Excavación y Contención"),
        p("La obra comienza con la excavación para los tres Subsuelos, que alcanzan los 10,50 m de profundidad. A medida que se excava, las paredes del terreno deben contenerse para que no se derrumben: para eso se usan pantallas o tablestacas. Si aparece agua freática, se la controla con agotamiento, es decir, bombeando el agua para mantener el fondo seco mientras se trabaja. Estas tareas son críticas y su costo depende directamente del estudio geotécnico del terreno."),
        h3("9.3.2 Estructura de Subsuelos y Torre"),
        p("Una vez contenida la excavación, se construyen los muros perimetrales y la platea de fundación, y luego la estructura de los subsuelos hacia arriba. A partir de la Planta Baja, el edificio se levanta piso por piso con un ciclo repetitivo: se encofran y hormigonan los pilares y los núcleos, se colocan los casetones de la losa nervada, se arma el acero y se hormigona la losa. El ciclo se repite idéntico en cada nivel, lo que permite que la cuadrilla gane velocidad con la práctica. La losa nervada con casetones recuperables es especialmente adecuada para este ritmo, porque los casetones se retiran, se limpian y se vuelven a usar en el piso siguiente."),
        h3("9.3.3 Verificaciones de Constructibilidad"),
        p("Un diseño es constructible cuando se puede ejecutar sin improvisar. Para asegurarlo se verifican varios aspectos: que la armadura quepa físicamente dentro de cada elemento (por ejemplo, que dos barras de 18 mm más los estribos entren en un nervio de 10 cm con sus recubrimientos), que los recubrimientos y las tolerancias sean los de la norma, que los casetones se puedan desmoldar y reutilizar, y que exista espacio para las instalaciones en los plenos y shafts. También se verifica el acceso de los equipos de obra, como la grúa y la bomba de hormigón. Estas verificaciones son las que distinguen un cálculo académico de un proyecto listo para construir."),

        // ================================================================
        h2("9.4 Cronograma 4D y 5D"),
        p("El cronograma de obra es el plan de tiempos que indica cuándo se ejecuta cada tarea. En un proyecto BIM, el cronograma se enlaza con el modelo tridimensional: cuando el tiempo se suma a las tres dimensiones del modelo se habla de cuarta dimensión, o 4D, y cuando además se le suma el costo se habla de quinta dimensión, o 5D. Este enlace permite ver, por ejemplo, cómo crece el edificio mes a mes, y saber cuánto dinero se ejecuta en cada etapa."),
        p("El cronograma de este edificio sigue la secuencia constructiva descrita: excavación y contención, estructura de subsuelos, estructura de la torre con su ciclo repetitivo de losa nervada, azotea y tanques, y finalmente instalaciones y terminaciones. La ventaja de vincular el cronograma al modelo y al presupuesto es que cualquier atraso o cambio se refleja de inmediato en el tiempo y en el costo, y el proyectista puede anticipar el impacto antes de que ocurra en la obra."),

        pageBreak(),
    ];
};
