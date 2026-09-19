// =====================================================================
//  Referencias (IEEE) y Anexos.
// =====================================================================
const { h1, h2, p, bullet } = require("../estilos_y_helpers");

module.exports = function () {
    return [
        h1("Referencias (IEEE)"),
        p("[1] Organization and digitization of information about buildings and civil engineering works — Building information modelling (BIM) — Part 1: Concepts and principles, ISO 19650-1:2018, ISO, Geneva, Switzerland, 2018."),
        p("[2] Organization and digitization of information about buildings and civil engineering works — Building information modelling (BIM) — Part 2: Delivery phase of the assets, ISO 19650-2:2018, ISO, Geneva, Switzerland, 2018."),
        p("[3] Forças devidas ao vento em edificações, ABNT NBR 6123:2023, Associação Brasileira de Normas Técnicas, Rio de Janeiro, Brazil, 2023."),
        p("[4] Projeto de estruturas de concreto — Procedimento, ABNT NBR 6118:2014, Associação Brasileira de Normas Técnicas, Rio de Janeiro, Brazil, 2014."),
        p("[5] Ações para o cálculo de estruturas de edificações, ABNT NBR 6120:2019, Associação Brasileira de Normas Técnicas, Rio de Janeiro, Brazil, 2019."),
        p("[6] Minimum Design Loads and Associated Criteria for Buildings and Other Structures, ASCE/SEI 7-22, American Society of Civil Engineers, Reston, VA, USA, 2022."),
        p("[7] Building Code Requirements for Structural Concrete and Commentary, ACI 318-19, American Concrete Institute, Farmington Hills, MI, USA, 2019."),
        p("[8] Eurocode 1: Actions on structures — Part 1-4: General actions — Wind actions, EN 1991-1-4, European Committee for Standardization, Brussels, Belgium, 2005."),
        p("[9] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, \"A fast and elitist multiobjective genetic algorithm: NSGA-II,\" IEEE Transactions on Evolutionary Computation, vol. 6, no. 2, pp. 182–197, 2002."),
        p("[10] A. K. Chopra, Dynamics of Structures: Theory and Applications to Earthquake Engineering, 5th ed., Pearson, 2017."),
        p("[11] E. W. East, Construction Operations Building Information Exchange (COBie), US Army Corps of Engineers, 2007."),
        p("[12] Listado de Precios de Insumos, Cámara Paraguaya de la Industria de la Construcción (CAPACO), Asunción, Paraguay, Jul. 2025."),
        p("[13] Generador de Precios de la Construcción — Paraguay, CYPE Ingenieros, 2025. [En línea]. Disponible: https://paraguay.generadordeprecios.info/"),
        p("[14] Cotización Referencial de Monedas — Dólar estadounidense vs. Guaraní, Banco Central del Paraguay (BCP), Asunción, Paraguay, Jun. 2026."),
        p("[15] PyNiteFEA, Biblioteca de elementos finitos de barras en Python, J. W. Brinck, 2024. [En línea]. Disponible: https://github.com/JWock82/Pynite"),
        p("[16] Acción del viento en las construcciones, Norma Paraguaya NP 196:1991, 1.ª ed., Instituto Nacional de Tecnología, Normalización y Metrología (INTN), Asunción, Paraguay, 1991."),
        p("[17] Á. J. Martínez, F. D. Marín, F. A. Aquino y M. A. Arévalos, \"Study of the maximum wind speeds and meteorological characteristics in Paraguay in order to differentiate synoptic and non-synoptic events, for a future update of the NP-196,\" en Proc. CILAMCE-PANACM 2021, Río de Janeiro, Brasil, 2021."),
        p("[18] N. Ibarra, A. Arévalos, R. Silva, I. Quintana y B. Martínez-Pavetti, \"Dynamic Analysis of a Slender Building Using Two Parallel Spectral Analysis Methods,\" en Proc. 10th World Congress on New Technologies (NewTech'24), Barcelona, España, 2024, Paper ICCEIA 132."),

        h1("Anexos"),
        h2("Anexo A: Anexo de Cálculo Estructural (LaTeX)"),
        p("Los cálculos estructurales se documentan en un anexo en LaTeX con estilo pedagógico (cada elemento se explica desde cero, se calcula manualmente bajo norma y se verifica con programas). El anexo compila a PDF con MiKTeX y actualmente desarrolla el módulo de la losa nervada:"),
        bullet("A.1 — Diseño de la losa nervada/reticular alivianada (ACI 318-19 §8.8/§9.8 · NBR 6118 §13.2.4.1): qué es, componentes, verificación dimensional, cargas, flexión, corte, estado límite de servicio, detalles de armado y comparación con PyNite."),
        bullet("A.2 en adelante — Viento (NP 196:1991 y comparación con NBR 6123, ASCE 7-22 y Eurocódigo 1), pilares, núcleos, muro de contención y fundaciones (en desarrollo)."),
        p("Ruta: 06_ANEXOS_TESIS/06.01_Capitulos_Documento_Escrito/anexo_calculo_latex/main.pdf"),
    ];
};
