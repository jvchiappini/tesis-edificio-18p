// =====================================================================
//  capitulos/index.js — Ensambla el cuerpo completo de la tesis.
//  Cada capítulo es un módulo independiente que exporta una función
//  que devuelve un arreglo de párrafos. Para agregar o reordenar
//  capítulos, basta con editar esta lista.
// =====================================================================
const preliminares = require("./preliminares");
const cap01 = require("./cap01_introduccion");
const cap02 = require("./cap02_marco_teorico");
const cap03 = require("./cap03_metodologia");
const cap04 = require("./cap04_descripcion_edificio");
const cap05 = require("./cap05_estructura_optimizacion");
const cap06 = require("./cap06_viento");
const cap07 = require("./cap07_diseno_hormigon");
const cap08 = require("./cap08_instalaciones");
const cap09 = require("./cap09_computos");
const cap10 = require("./cap10_conclusiones");
const referenciasAnexos = require("./referencias_anexos");

module.exports = function cuerpo() {
    return [
        ...preliminares(),
        ...cap01(),
        ...cap02(),
        ...cap03(),
        ...cap04(),
        ...cap05(),
        ...cap06(),
        ...cap07(),
        ...cap08(),
        ...cap09(),
        ...cap10(),
        ...referenciasAnexos(),
    ];
};
