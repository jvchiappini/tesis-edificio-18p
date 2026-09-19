// =====================================================================
//  imagenes.js — Fuente única de rutas de ilustraciones de la tesis.
//  Todas las figuras provienen de los scripts de Python del proyecto.
// =====================================================================
const path = require("path");

const BASE_DIR = path.join(__dirname, "../../..");
const R = (rel) => path.join(BASE_DIR, rel);

const IMG = {
    s1: R("05_RECURSOS/05.05_Scripts_Python/01_Subsuelos/outputs/planta_subsuelo_1.png"),
    s2: R("05_RECURSOS/05.05_Scripts_Python/01_Subsuelos/outputs/planta_subsuelo_2.png"),
    s3: R("05_RECURSOS/05.05_Scripts_Python/01_Subsuelos/outputs/planta_subsuelo_3.png"),
    pb: R("05_RECURSOS/05.05_Scripts_Python/02_PB_Macro_Distribucion/outputs/masterplan_planta_baja.png"),
    adm: R("05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_administracion_bms.png"),
    san: R("05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_sanitarios_publicos.png"),
    biz: R("05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_business_center.png"),
    rsu: R("05_RECURSOS/05.05_Scripts_Python/03_PB_Micro_Interiores/outputs/plan_deposito_rsu.png"),
    a: R("05_RECURSOS/05.05_Scripts_Python/04_Planta_Tipo/outputs/planta_tipo_layout_A.png"),
    b: R("05_RECURSOS/05.05_Scripts_Python/04_Planta_Tipo/outputs/planta_tipo_layout_B.png"),
    c: R("05_RECURSOS/05.05_Scripts_Python/04_Planta_Tipo/outputs/planta_tipo_layout_C.png"),
    inter: R("05_RECURSOS/05.05_Scripts_Python/04_Planta_Tipo/outputs/esquema_intercalado_18_pisos.png"),
    az: R("05_RECURSOS/05.05_Scripts_Python/05_Azotea/outputs/plano_azotea_tecnica.png"),
    grilla: R("05_RECURSOS/05.05_Scripts_Python/06_Estructura/outputs/plano_grilla_pilares.png"),
    m3d: R("05_RECURSOS/05.05_Scripts_Python/06_Estructura/calculo/outputs/modelo_3d_elevacion.png"),
    axial: R("05_RECURSOS/05.05_Scripts_Python/06_Estructura/calculo/outputs/carga_axial_vs_altura.png"),
    comp: R("05_RECURSOS/05.05_Scripts_Python/06_Estructura/calculo/outputs/comparativa_estructuras.png"),
    sens: R("05_RECURSOS/05.05_Scripts_Python/06_Estructura/calculo/outputs/comparativa_sensibilidad.png"),
    fach: R("05_RECURSOS/05.05_Scripts_Python/07_Fachada/outputs/fachada_sur_estrategias.png"),
};

module.exports = { IMG, BASE_DIR, R };
