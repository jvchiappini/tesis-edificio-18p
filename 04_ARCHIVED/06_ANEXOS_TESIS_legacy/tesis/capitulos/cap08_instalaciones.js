// =====================================================================
//  Capítulo 8: Instalaciones y Coordinación BIM.
//  Ampliado: cada instalación explicada desde cero y con sus criterios.
// =====================================================================
const { h1, h2, h3, p, bullet, pageBreak } = require("../estilos_y_helpers");

module.exports = function () {
    return [
        h1("Capítulo 8: Instalaciones y Coordinación BIM"),

        p("Un edificio no es solo estructura: para que funcione tiene que llevar agua, retirar residuos, distribuir electricidad, proteger contra incendios y ventilar sus ambientes. A todo eso se lo llama instalaciones, y su diseño no puede hacerse después de la estructura ni por separado, porque una instalación mal coordinada termina cortando vigas o atravesando losas donde no se debe. Este capítulo describe las instalaciones del edificio y la forma en que se coordinaron mediante la metodología BIM."),

        // ================================================================
        h2("8.1 Instalación Sanitaria de Agua Potable"),
        p("La instalación sanitaria es la que lleva el agua potable desde la calle hasta cada artefacto del edificio. Como el edificio es alto y la presión de la red pública no alcanza para los pisos superiores, el agua no se impulsa de una sola vez: se almacena abajo y se rebombea por etapas. El sistema se organiza así: el agua llega de la red al Subsuelo S1, donde se ubica un bloque de cisternas de agua potable con sus bombas; desde allí se bombea a los tanques elevados de la azotea, que actúan como reserva y cabecera del sistema; y desde los tanques, por gravedad, el agua baja a todos los pisos. Este esquema de cisterna, bombeo y tanque elevado es el más confiable y el que mejor responde ante un corte de energía, porque el tanque de la azotea mantiene reserva."),
        p("El dimensionamiento del almacenamiento se hace según el consumo previsto de los 432 apartamentos más los locales comerciales, siguiendo la norma de instalaciones sanitarias. El bombeo se organiza con bombas alternadas y una de reserva, de modo que el sistema no se detenga si una bomba falla. En la Planta Baja se reservan 60 m² para el conjunto de reservorios y bombas."),

        // ================================================================
        h2("8.2 Instalación Cloacal"),
        p("La instalación cloacal es la que recoge las aguas servidas de baños, cocinas y lavaderos y las conduce al sistema público. Como los tres Subsuelos están por debajo del nivel de la calle, sus desagües no pueden salir por gravedad: necesitan ser bombeados. Para eso se dispone una estación de bombeo de aguas residuales, llamada EBAR, ubicada en la esquina sureste del Subsuelo S1, con bombas que impulsan el líquido hacia arriba, hasta la cota de la red pública. Las cañerías cloacales se dividen en dos redes, una para los artefactos y otra para la ventilación, de modo que los olores no entren a los ambientes y las presiones se equilibren."),

        // ================================================================
        h2("8.3 Instalación Pluvial"),
        p("La instalación pluvial es la que recoge el agua de lluvia de la azotea y de las terrazas y la conduce fuera del edificio. Se compone de desagües de azotea, bajantes verticales y una planta de tratamiento de agua de lluvia, conocida por sus siglas PTE, ubicada en el Subsuelo S1. La PTE recibe el agua de lluvia, la decanta y la filtra, y el agua tratada se puede reutilizar para riego y para el lavado de pisos y cocheras. Esta reutilización reduce el consumo de agua potable y es una medida de sostenibilidad que se documenta en el cómputo de instalaciones. En la Planta Baja se prevé una dársena de carga y descarga, que también debe tener su desagüe."),

        // ================================================================
        h2("8.4 Instalación Eléctrica"),
        p("La instalación eléctrica incluye desde la acometida de la calle hasta el último tomacorriente del edificio. El punto de partida es la subestación eléctrica de la ANDE, ubicada en la Planta Baja en un local de 60 m², donde se transforma la tensión de la red pública. Desde allí la energía se distribuye a través de tableros generales y seccionales, uno por cada zona del edificio."),
        p("Como el edificio no puede quedar a oscuras ante un corte de energía, se dispone un grupo electrógeno de emergencia en el Subsuelo S1, de aproximadamente 35 m², que alimenta los servicios esenciales: ascensores, bombas de agua, iluminación de emergencia y escaleras, sistema contra incendio y sala de monitoreo. Además de la energía de emergencia, el edificio prevé una red de muy baja tensión para las comunicaciones y el sistema de gestión del edificio, llamado BMS, que monitorea y controla las instalaciones desde un puesto central."),

        // ================================================================
        h2("8.5 Instalación Contra Incendio"),
        p("La instalación contra incendio, abreviada PCI, tiene por objeto detectar un incendio y permitir apagarlo o controlarlo, además de evacuar a los ocupantes. Se compone de cuatro partes. La primera es la reserva de agua contra incendio, independiente de la de agua potable, almacenada en el bloque de tanques de la azotea (aproximadamente 120 m³) y en el reservorio de la Planta Baja, con sus bombas de presión. La segunda es la red de hidrantes, que recorre los niveles y permite a los bomberos conectar mangueras. La tercera es el sistema de rociadores automáticos, que detecta el calor y descarga agua sobre el foco. La cuarta es el sistema de detección y alarma, con detectores de humo y pulsadores manuales."),
        p("Un aspecto crítico en un edificio alto es la evacuación. Los dos núcleos gemelos contienen sendas cajas de escalera de emergencia, diseñadas para ser protegidas y para que las personas salgan sin cruzarse con el humo. Los ascensores se ubican en un vestíbulo protegido, para que puedan usarse en la evacuación asistida. Estas decisiones se relacionan directamente con la forma de los núcleos que se describió en el Capítulo 4."),

        // ================================================================
        h2("8.6 Instalación Mecánica y Ventilación"),
        p("La instalación mecánica se ocupa del aire: climatizar los ambientes, ventilar los que no tienen ventana y extraer el aire viciado de los locales técnicos. En este edificio, la climatización de los apartamentos se resuelve con equipos individuales, porque cada unidad se controla por separado; los locales comerciales de la Planta Baja, por su parte, reciben la instalación básica para que el arrendatario instale su propio sistema. La ventilación mecánica se concentra en tres puntos: los baños sin ventana, que se extraen mediante un ducto de 200 mm de diámetro, la cochera de los Subsuelos, que necesita renovar el aire por la presencia de vehículos, y las salas técnicas, donde el grupo electrógeno y los tableros requieren ventilación propia. En la azotea se prevé una sala para los equipos de climatización."),

        // ================================================================
        h2("8.7 Gestión de Residuos Sólidos Urbanos"),
        p("Para retirar la basura de 432 apartamentos sin obligar a nadie a bajar 18 pisos con bolsas, el edificio incorpora un sistema de ducto vertical de residuos. Es un conducto de acero inoxidable de 500 mm de diámetro que recorre el edificio desde la azotea hasta la Planta Baja, y en cada piso tiene una boca de carga en la sala de basura. La basura cae por gravedad hasta el depósito central de residuos de la Planta Baja, donde descarga directamente en un contenedor basculante de aproximadamente 10 m³."),
        p("El depósito central, de unos 228 m², está al nivel de la calle y tiene el piso inclinado, una rejilla de lavado y ventilación forzada para mantener la higiene. Su mayor ventaja es la facilidad de la recolección: el camión recolector entra marcha atrás por un pasaje lateral de al menos 3,5 m de ancho, levanta el contenedor con su sistema hidráulico y lo vacía, sin necesidad de que el personal entre al subsuelo ni de manipular bolsas. Este sistema, además de cómodo, reduce el riesgo sanitario y el ruido."),

        // ================================================================
        h2("8.8 Coordinación de las Instalaciones y Detección de Interferencias"),
        p("Todas las instalaciones anteriores deben convivir en el mismo espacio físico, y ahí es donde la metodología BIM demuestra su valor. Cada disciplina se modela por separado y luego los modelos se superponen en un modelo federado, que es un modelo que reúne todos los demás. Sobre él se ejecuta la detección de interferencias, que consiste en buscar automáticamente los choques entre elementos: una cañería que atraviesa una viga, un ducto que no deja pasar una escalera, un cable que ocupa el espacio de un pilar."),
        p("En este proyecto la coordinación se realiza en Navisworks sobre los modelos federados del estado compartido del entorno común de datos, y los puntos críticos son los shafts y el pasillo técnico central, donde conviven el ducto de residuos, los montantes de instalaciones y la ventilación. La losa nervada, por su parte, admite el paso de instalaciones por los vacíos entre casetones, lo que da flexibilidad sin necesidad de perforar la estructura. Detectar y resolver estas interferencias en el modelo, antes de la obra, es lo que evita los sobrecostos y los atrasos que genera resolverlos en el terreno."),

        pageBreak(),
    ];
};
