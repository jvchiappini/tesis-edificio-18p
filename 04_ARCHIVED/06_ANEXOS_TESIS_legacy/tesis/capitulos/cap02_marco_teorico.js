// =====================================================================
//  Capítulo 2: Marco Teórico.
//  Escrito con estilo pedagógico: cada concepto se explica desde cero,
//  en castellano llano, antes de aplicarlo al edificio.
// =====================================================================
const { h1, h2, h3, p, bullet, pageBreak } = require("../estilos_y_helpers");

module.exports = function () {
    return [
        h1("Capítulo 2: Marco Teórico"),

        p("Antes de calcular cualquier cosa conviene entender qué es cada elemento, cómo trabaja y por qué se eligió. Este capítulo está escrito para que cualquier lector, aunque nunca haya estudiado estructuras, pueda seguir después cada número del cálculo. Primero se presenta el hormigón armado y sus componentes; luego la losa nervada, que es el sistema de entrepiso adoptado; después la acción del viento, que es la fuerza horizontal más importante en un edificio alto; y finalmente las dos herramientas de gestión que ordenan todo el trabajo: la optimización por algoritmos genéticos y la metodología BIM bajo la norma ISO 19650."),

        // ================================================================
        h2("2.1 El Hormigón Armado: Qué Es y Cómo Trabaja"),

        h3("2.1.1 El Problema: el Hormigón Resiste la Compresión pero no la Tracción"),
        p("El hormigón es una mezcla de cemento, arena, piedra y agua que, al endurecer, forma un material pétreo. Su virtud principal es que resiste muy bien los esfuerzos de compresión: se le puede apretar con enorme fuerza sin que se rompa. Su defecto es que resiste muy mal la tracción: si se lo estira, se fisura y se parte con poco esfuerzo. En números redondos, un hormigón de resistencia f'c = 30 MPa soporta del orden de 30 MPa a compresión, pero apenas unos 3 MPa a tracción, es decir, alrededor de un 10 %."),
        p("Para entender la diferencia, imagine que aprieta una esponja entre las manos: aguanta mucho. Ahora imagine que la estira desde los extremos: se rompe enseguida. El hormigón se comporta de manera parecida. Esto no sería un problema si los elementos estructurales solo se comprimieran, pero en la realidad las losas y vigas se flexionan, y al flexionarse una parte de la sección queda comprimida y la otra parte estirada (traccionada)."),

        h3("2.1.2 La Solución: el Acero Toma la Tracción"),
        p("La solución es combinar el hormigón con barras de acero. El acero sí resiste muy bien la tracción: una barra de acero CA-50 soporta del orden de 500 MPa, o sea unas 160 veces más que el hormigón estirado. Entonces se coloca hormigón donde hay compresión y barras de acero donde hay tracción, de modo que cada material trabaja en lo que es bueno. A ese conjunto se lo llama hormigón armado: el hormigón es el material resistente a la compresión y el acero es la armadura que absorbe la tracción."),
        p("El edificio de esta tesis usa hormigón H-30 (f'c = 30 MPa) y acero CA-50 (fy = 500 MPa). Esos dos valores aparecerán una y otra vez en los cálculos del Capítulo 7."),

        h3("2.1.3 Por Qué Ambos Materiales Trabajan Juntos"),
        p("Para que el hormigón y el acero formen un solo material compuesto deben cumplirse dos condiciones. La primera es la adherencia: el hormigón, al fraguar, se pega fuertemente a las barras corrugadas (las barras tienen resaltos justamente para mejorar ese agarre), de modo que cuando el hormigón se deforma arrastra al acero y viceversa. La segunda es que ambos materiales se dilaten de manera parecida con la temperatura: el coeficiente de dilatación térmica del hormigón y del acero son casi iguales (del orden de 10⁻⁵ por grado centígrado), por lo que al cambiar la temperatura no se separan. Gracias a estas dos condiciones, el hormigón y el acero se deforman juntos y comparten el trabajo."),

        h3("2.1.4 Los Elementos de una Estructura de Edificio"),
        p("Un edificio como el de este trabajo se puede imaginar como un esqueleto. Los elementos que lo forman son:"),
        bullet("Losas: superficies planas y horizontales que separan un piso de otro. Reciben directamente las cargas de uso (personas, muebles, tabiques, equipos) y las transmiten hacia abajo."),
        bullet("Vigas: elementos horizontales (o de borde) que recogen las cargas de las losas y las llevan hasta los pilares o muros."),
        bullet("Pilares: elementos verticales que reciben las cargas de las vigas y losas y las transmiten, piso a piso, hasta la fundación."),
        bullet("Núcleos: cajas verticales de hormigón armado que encierran los ascensores y la escalera. Además de contener esos servicios, por su gran rigidez funcionan como el principal elemento que resiste las fuerzas horizontales del viento, algo así como el tronco de un árbol que evita que la copa se doble."),
        bullet("Fundación: el elemento que recibe todas las cargas del edificio y las reparte en el terreno."),
        p("En este edificio hay losas nervadas en todos los niveles, pilares de hormigón armado con sección variable según la altura, dos núcleos gemelos y una fundación que se estudia en el Capítulo 7."),

        h3("2.1.5 Qué Fuerzas Actúan sobre el Edificio"),
        p("Las fuerzas que actúan sobre una estructura se agrupan en dos grandes familias. Las acciones verticales, que empujan hacia abajo, son el peso propio de la estructura (el peso del hormigón armado, que se toma como 25 kN por metro cúbico), las cargas permanentes (pisos, cielorrasos, tabiques) y las sobrecargas de uso (personas y muebles, que según la NBR 6120 valen 2.0 kN/m² en viviendas). Las acciones horizontales, que empujan de costado, son fundamentalmente el viento y, en menor medida, el sismo."),
        p("La unidad kN significa kilonewton y equivale aproximadamente al peso de 100 kg. Así, una sobrecarga de 2.0 kN/m² quiere decir que cada metro cuadrado de losa está previsto para soportar unos 200 kg de uso. Esta manera de leer las unidades ayuda a tener una idea física de los números que aparecerán más adelante."),

        // ================================================================
        h2("2.2 La Losa Nervada: Fundamentos Teóricos"),

        h3("2.2.1 Qué Es una Losa y Cómo Trabaja"),
        p("Una losa es un elemento estructural plano y horizontal que separa dos niveles de un edificio, soporta las cargas de uso y las transmite hacia los apoyos (pilares, vigas o muros). Cuando la losa recibe una carga vertical, se deforma hacia abajo y aparece un fenómeno llamado flexión: la cara superior de la losa se acorta (se comprime) y la cara inferior se alarga (se tracciona). Como el hormigón resiste muy bien la compresión pero casi nada la tracción, la zona inferior de la losa necesita acero, y el hormigón que ocupa esa zona traccionada no aporta resistencia: solo aporta peso."),

        h3("2.2.2 Qué Significa Flexionar: la Analogía de la Regla"),
        p("Para entender la flexión basta con tomar una regla de plástico y apoyarla entre dos libros, dejando un tramo libre en el medio. Al empujar el centro hacia abajo, la regla se curva. Si se mira con atención, la parte de arriba de la regla se estira y la de abajo se comprime, aunque en una regla tan delgada casi no se note. En una losa de hormigón ocurre lo mismo: al flexionarse, la cara de arriba se comprime y la de abajo se estira. Ahí está la clave de todo el capítulo: el hormigón de la cara inferior, que está estirada, es prácticamente inútil; por eso conviene quitarlo y reemplazarlo por acero."),

        h3("2.2.3 Por Qué la Losa Maciza Desperdicia Hormigón"),
        p("Una losa maciza es una plancha de hormigón de espesor constante. Es simple de construir, pero coloca hormigón en toda la sección, incluida la zona inferior traccionada donde ese hormigón no colabora. En una losa de gran luz, ese hormigón inerte representa una enorme cantidad de peso muerto: peso que hay que sostener con pilares y fundaciones más grandes, y que además aumenta la masa del edificio y, con ella, las fuerzas del viento y del sismo. La losa maciza es, entonces, un sistema sencillo pero poco eficiente cuando las luces son grandes."),

        h3("2.2.4 Cómo Nace la Losa Nervada"),
        p("La losa nervada nace de un razonamiento muy simple: si el hormigón de la zona traccionada no sirve, se lo quita. En lugar de una plancha maciza se deja una retícula de costillas de hormigón, llamadas nervios, que contienen el acero justo donde hace falta, y se corona el sistema con una capa delgada de hormigón llamada capa de compresión. El espacio que queda entre nervios se rellena con piezas huecas o livianas, llamadas casetones o alivianamientos, que solo sirven para dar forma y para que el piso tenga una superficie continua por arriba. El resultado es un entrepiso mucho más liviano y económico que la losa maciza, con una capacidad resistente comparable."),

        h3("2.2.5 Las Tres Partes del Sistema"),
        p("El sistema nervado/reticular alivianado está compuesto por tres partes fundamentales:"),
        bullet("Capa de compresión (o loseta superior): losa delgada de hormigón, normalmente de 10 cm, que corona el sistema. Transmite las cargas entre nervios y forma la zona comprimida de la flexión. Sobre ella se apoya el piso terminado."),
        bullet("Nervios (o nervaduras): costillas de hormigón armado, típicamente de 10 cm de ancho, que alojan las armaduras principales de tracción y llevan las cargas hacia los apoyos. Se comportan como una malla de vigas embebidas."),
        bullet("Casetones o alivianamientos: moldes huecos (de poliestireno expandido, plástico recuperable o bloques de hormigón) que ocupan el volumen entre nervios para eliminar hormigón inerte. Los casetones recuperables, además, permiten un fondo plano de la losa, apto para cielorraso."),
        p("En este edificio se adoptan casetones recuperables de plástico de 50 cm de base y 25 cm de alto, nervios de 10 cm de ancho separados 60 cm entre ejes (claro libre de 50 cm) y una capa de compresión de 10 cm. Con eso el canto total es de 35 cm en las plantas tipo y la azotea, y de 45 cm en Planta Baja y Subsuelos, porque ahí las luces son mayores."),

        h3("2.2.6 Cómo Trabajan los Nervios: las Vigas T"),
        p("El nervio, visto en corte, no trabaja solo. Como está unido a la capa de compresión, los dos forman en conjunto una sección con forma de T: el alma de la T es el nervio y el ala de la T es la capa de compresión que colabora a cada lado. Esta forma es muy eficiente porque concentra el hormigón arriba (donde hay compresión) y deja el acero abajo (donde hay tracción). Es la misma idea con la que se construyen las vigas de acero con perfil en I o las alas de un avión: mucho material lejos del centro, donde más sirve."),
        p("Además, el momento flector cambia de signo a lo largo de la losa. En el centro de un tramo la losa se flexiona con la tracción abajo, y por eso la armadura principal va abajo; pero sobre los apoyos (pilares o vigas de borde) el giro se invierte y la tracción pasa arriba, por lo que allí se coloca armadura superior. Ese detalle se ve reflejado en el plano de armado del Capítulo 7."),

        h3("2.2.7 Losas Nervadas en Una o en Dos Direcciones"),
        p("Cuando los nervios se disponen en una sola dirección, la losa se llama nervada unidireccional: la carga se reparte solo en esa dirección, como una serie de vigas paralelas. Cuando los nervios se disponen en dos direcciones perpendiculares (en este caso cada 60 cm en ambos sentidos), la losa se llama reticular o bidireccional. En el sistema bidireccional la carga se reparte entre las dos direcciones (una parte va en un sentido y el resto en el otro, de modo que la suma es la carga total), lo que reduce la flecha, aumenta la rigidez y mejora el comportamiento frente a cargas concentradas."),
        p("En este edificio los paneles de la grilla son aproximadamente cuadrados (7.875 m por 7 a 9 m). Cuando un panel es cuadrado o casi cuadrado, las dos direcciones trabajan de manera parecida y el comportamiento bidireccional resulta ventajoso. Por eso se adoptó la retícula de nervios en dos direcciones, que reparte la carga hacia las cuatro vigas de borde y mejora el comportamiento de los salones comerciales de gran luz."),

        h3("2.2.8 Ventajas y Desventajas del Sistema"),
        p("Las ventajas principales del sistema nervado son: el bajo peso propio (en este edificio 4.75 kN/m² frente a unos 9 kN/m² de una losa maciza de igual canto), el menor costo frente a las alternativas evaluadas, la gran rigidez y el buen comportamiento frente a vibraciones, el fondo plano apto para cielorraso, la posibilidad de pasar instalaciones por los espacios vacíos sin perforar la estructura, la mejor aislación térmica y acústica que dan los alivianamientos, y la versatilidad para cubrir grandes luces como las de los salones comerciales."),
        p("Sus limitaciones son: exige un canto total mayor que una losa maciza equivalente (lo que obliga a prever la altura en el proyecto arquitectónico), tiene menor resistencia al corte y a las cargas concentradas (lo que exige estribos cerca de los apoyos y nervios de reparto donde apoyan muros pesados), consume algo más de acero por metro cuadrado que la maciza (compensado por el ahorro de hormigón) y su construcción tiene más pasos por la colocación de los casetones, aunque los casetones recuperables agilizan el ciclo."),

        h3("2.2.9 Por Qué se Eligió Este Sistema en Este Edificio"),
        p("La selección de la losa nervada/reticular alivianada como sistema definitivo se apoya en cuatro criterios complementarios:"),
        bullet("Criterio técnico: el menor peso propio reduce las cargas axiales de los pilares (la carga máxima en la base llega a unos 13.8 MN, es decir unos 1.400 toneladas por pilar), las solicitaciones sobre la fundación y la masa del edificio, sin sacrificar rigidez gracias a la inercia que aporta el canto total."),
        bullet("Criterio económico: la comparación de costos de cinco sistemas de entrepiso, con precios unitarios verificados del mercado paraguayo (CYPE y CAPACO, julio de 2025) y un tipo de cambio de 6.100 guaraníes por dólar, ubicó a la losa nervada como la más económica (68.8 USD/m² sobre 68.611 m² de losa). El análisis de sensibilidad confirmó que gana en todos los escenarios evaluados."),
        bullet("Criterio constructivo: la losa nervada con casetones recuperables no exige tecnología ni mano de obra especializada, a diferencia de la losa postensada, y hay amplia disponibilidad de materiales y proveedores en la zona."),
        bullet("Criterio arquitectónico: permite cubrir grandes luces comerciales con fondo plano, da flexibilidad al arrendatario y admite el paso de instalaciones por los vacíos de los casetones sin cortar la estructura."),
        p("En síntesis, la losa nervada/reticular alivianada combina el menor costo, el menor peso y la mayor versatilidad constructiva y arquitectónica entre las alternativas evaluadas, resultando la solución óptima para este edificio de uso mixto. Su dimensionamiento detallado se desarrolla en el Capítulo 7 y en el anexo de cálculo."),

        // ================================================================
        h2("2.3 La Acción del Viento"),
        p("Cuanto más alto es un edificio, más importante es el viento. En un edificio bajo, el viento apenas se nota; en uno de 18 niveles, la fuerza horizontal del viento puede ser la solicitación más exigente sobre la estructura. Por eso el viento es uno de los temas centrales de esta tesis."),

        h3("2.3.1 Qué Es el Viento y Por Qué Empuja"),
        p("El viento es simplemente aire en movimiento. Aunque es muy liviano, cuando se mueve rápido y choca contra una superficie grande, como la fachada de un edificio, le transmite una fuerza considerable. Piense en el viento contra un cartel grande: cuanto más rápido sopla y más grande es el cartel, mayor es la fuerza. Lo mismo ocurre con la fachada del edificio."),

        h3("2.3.2 Presión y Succión"),
        p("Al chocar contra la fachada de barlovento (la cara que da al viento), el aire se frena y empuja: se produce una presión positiva. Al mismo tiempo, el aire que pasa por encima y por los costados se acelera y tiende a separarse, generando una presión negativa o succión en la fachada de sotavento (la cara opuesta) y en los laterales. El resultado es que el edificio no solo es empujado de un lado, sino también succionado del otro, y ambos efectos se suman. Si el edificio no es simétrico, además aparece un efecto de torsión, como cuando se empuja una puerta cerca de su borde libre."),

        h3("2.3.3 Qué Es la Presión Dinámica del Viento"),
        p("Para calcular cuánto empuja el viento se necesita su presión dinámica, que depende de la velocidad del viento al cuadrado. Esto significa que si la velocidad se duplica, la fuerza se cuadruplica: por eso las ráfagas fuertes son tan determinantes. La velocidad del viento, a su vez, no es igual a todas las alturas: cerca del suelo la rugosidad de la ciudad (edificios, árboles) frena el aire, y a medida que se sube en altura el viento es más veloz. Esa variación con la altura es lo que se llama perfil de velocidad o capa límite atmosférica."),

        h3("2.3.4 Coeficientes y Ráfaga"),
        p("La presión del viento no se aplica igual sobre todas las caras ni es constante en el tiempo. Para contemplar esto, las normas usan coeficientes de forma o de presión, que son números que corrigen la presión según la orientación y la geometría de cada cara. Además, el viento real llega en ráfagas, es decir, con picos de velocidad mucho mayores que el promedio; el factor de ráfaga tiene en cuenta esos picos y la forma en que la estructura responde a ellos. En edificios flexibles como el de este trabajo también influye la respuesta dinámica, porque la estructura se mueve con el viento y ese movimiento puede amplificar los efectos."),

        h3("2.3.5 Derivas y Confort"),
        p("En un edificio alto no alcanza con que la estructura no se rompa: también importa cuánto se mueve. La deriva de piso es la deformación horizontal relativa entre un piso y el siguiente; si es excesiva, las paredes se fisuran y los ocupantes sienten que el edificio se bambolea. Además, en los últimos pisos se verifica el confort frente a las aceleraciones: las personas perciben las vibraciones y, si superan cierto umbral, sienten mareo o inseguridad. Ambas verificaciones se conocen como estados límite de servicio y se explican con detalle, junto con los límites de la norma, en el Capítulo 6."),

        // ================================================================
        h2("2.4 Optimización Multiobjetivo con Algoritmos Genéticos (NSGA-II)"),

        h3("2.4.1 Qué Significa Optimizar"),
        p("Optimizar es buscar la mejor solución posible a un problema que tiene muchas alternativas. En este edificio, por ejemplo, hay muchísimas maneras de ubicar los pilares sobre la planta. Se podría probar cada combinación una por una, pero el número de posibilidades es enorme y llevaría años. Para eso existen los métodos de optimización: procedimientos que exploran de forma inteligente las alternativas en lugar de revisarlas todas."),

        h3("2.4.2 La Idea de la Evolución"),
        p("Un algoritmo genético se inspira en la evolución natural. Se parte de una población de soluciones (en este caso, distintas distribuciones del interior de un departamento o de un local), y a cada una se le mide su calidad mediante una función de aptitud. Las mejores soluciones se combinan entre sí (cruce) y se les introducen pequeños cambios aleatorios (mutación), generando una nueva generación que tiende a mejorar. Repitiendo el proceso muchas veces, la población evoluciona hacia soluciones cada vez mejores, igual que en la naturaleza sobreviven los individuos mejor adaptados."),

        h3("2.4.3 Varios Objetivos a la Vez: NSGA-II"),
        p("En la práctica casi nunca hay un solo objetivo. En este proyecto se busca, al mismo tiempo, que ningún pilar caiga en el interior de un ambiente, que la mayor cantidad posible de pilares quede alineada sobre ejes de muros y que la grilla sea lo más regular posible. Estos objetivos compiten entre sí: mejorar uno empeora otro. El algoritmo NSGA-II (de los autores Deb y colaboradores, año 2002) resuelve precisamente esto: en lugar de una única solución, entrega un conjunto de soluciones equilibradas, cada una con una compensación distinta entre los objetivos, para que el proyectista elija la más conveniente."),
        p("En este trabajo, NSGA-II se aplica a los problemas que realmente admiten muchas alternativas: las arquitecturas interiores de los departamentos y las micro-distribuciones de la Planta Baja (administración y BMS, sanitarios públicos, centro de negocios y depósito de residuos). En cambio, las macro distribuciones de los niveles y la grilla estructural no se resuelven con el algoritmo, porque la solución está fuertemente condicionada por el terreno, los núcleos y las luces comerciales: se definen por diseño directo y se refinan a mano. Esta combinación de diseño directo, script paramétrico y optimización puntual es lo que constituye la metodología híbrida del proyecto."),

        // ================================================================
        h2("2.5 Metodología BIM y la Norma ISO 19650"),

        h3("2.5.1 Qué Es BIM"),
        p("BIM son las siglas de Building Information Modelling, que en castellano se entiende como modelado de la información de la construcción. No se trata solo de dibujar el edificio en tres dimensiones: se trata de construir un modelo digital que contiene, además de la geometría, toda la información del proyecto (materiales, dimensiones, instalaciones, costos). Trabajar con un modelo así permite que arquitectura, estructura e instalaciones se coordinen sobre una misma base y evita los errores típicos de trabajar cada disciplina por separado."),

        h3("2.5.2 El Entorno Común de Datos (CDE)"),
        p("Para que un equipo trabaje ordenadamente con un modelo compartido hace falta un entorno común de datos, o CDE, que es un espacio único y organizado donde vive toda la información del proyecto. La norma distingue cuatro estados de la información: WIP (trabajo en curso, todavía sin compartir), Shared (compartido entre disciplinas), Published (publicado y aprobado para obra) y Archived (archivado, cuando ya no se usa). Esta tesis replica esa organización en su propia estructura de carpetas y en una nomenclatura única de archivos, de modo que siempre se sabe qué versión es la vigente."),

        h3("2.5.3 Qué Aporta la Norma ISO 19650"),
        p("La norma ISO 19650 (en sus partes 1 y 2) es el estándar internacional que ordena la gestión de la información de un proyecto durante todo su ciclo de vida. Define los roles y las responsabilidades, los estados por los que pasa la información y la forma de garantizar la trazabilidad de los entregables. Aplicarla en una tesis de grado permite demostrar que el proyecto se gestionó con el mismo rigor con el que una consultora profesional organizaría una obra real. En este trabajo la norma se concreta en el Plan de Ejecución BIM (BEP), el CDE, la nomenclatura de archivos y la interoperabilidad mediante archivos IFC entre Revit 2024, Navisworks y los scripts de cálculo en Python."),

        pageBreak(),
    ];
};
