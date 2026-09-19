# ROADMAP_TESIS_300_PAGINAS.md — Hoja de Ruta Maestra para Tesis Monumental (300 Páginas)

> **REGLA DE ORO OBLIGATORIA PARA TODOS LOS AGENTES DE IA (COPILOT):**
> Este proyecto de tesis de Ingeniería Civil NO es un documento resumido. La meta explícita y obligatoria es alcanzar una extensión de **300 PÁGINAS HASTA EL FINAL DE LA TESIS**, combinando un marco teórico exhaustivo, desarrollo de ingeniería detallado, análisis eólico tri-normativo profundo, diseño integral de todas las instalaciones (MEP/EST/ARQ), cómputos métricos completos, memorias de cálculo paso a paso y anexos de código/planos.

---

## 🎯 Visión General del Proyecto

* **Título:** Diseño Estructural, Análisis Aerodinámico ante Cargas de Viento y Modelado BIM (ISO 19650) de un Edificio de Uso Mixto de 18 Plantas en Ciudad del Este, Paraguay.
* **Autor:** José Valentino Chiappini Vergara.
* **Extensión Objetivo:** **~300 Páginas** (Formato Word / PDF de Alta Fidelidad Académica).
* **Núcleo Técnico:** Énfasis principal en **Ingeniería de Viento y Dinámica de Estructuras** comparando la **Norma Paraguaya NP 196:1991** con estándares internacionales (**NBR 6123:2023, ASCE 7-22, Eurocódigo 1 EN 1991-1-4**), complementado con diseño estructural completo en H°A° (losa nervada/reticular H=35cm, pilares continuos, núcleos H°A°), diseño integral de instalaciones MEP, optimización algorítmica (NSGA-II) y gestión BIM ISO 19650.

---

## 📐 Estrategia de Distribución de Páginas (~300 Páginas)

| Sección / Capítulo | Descripción y Contenido Requerido | Extensión Objetivo |
|---|---|---|
| **Secciones Preliminares** | Carátula, Dedicatoria, Agradecimientos, Resumen/Abstract, Índice General, Índice de Figuras, Índice de Tablas, Lista de Símbolos y Abreviaturas. | ~15 págs. |
| **Capítulo 1** | **Introducción y Planteamiento del Problema:** Justificación técnica, hipótesis, objetivos generales y específicos, alcance del proyecto, caracterización de Ciudad del Este (clima, suelo, desarrollo urbano y contexto normativo nacional). | ~20 págs. |
| **Capítulo 2** | **Marco Teórico Expositivo I — Ingeniería de Viento y Aerodinámica:** Capa límite atmosférica, perfil de velocidad, turbulencia, desprendimiento de vórtices, galope, flutter, dinámica de fluidos computacional (CFD), túnel de viento, mitigación de forma. | ~45 págs. |
| **Capítulo 3** | **Marco Teórico Expositivo II — Comparativa Multi-Normativa de Viento:** Desglose artículo por artículo de la **NP 196:1991 (Paraguay)**, **NBR 6123:2023 (Brasil)**, **ASCE 7-22 (EE.UU.)** y **EN 1991-1-4 (Eurocódigo 1)**. Fórmulas, tablas de coeficientes de forma/presión, factores topográficos, ráfagas, resonancia y velocidades de referencia local. | ~40 págs. |
| **Capítulo 4** | **Metodología BIM bajo ISO 19650 y Optimización Algorítmica Híbrida:** BEP (BIM Execution Plan), CDE (Common Data Environment), LOIN/LOD, Algoritmos Genéticos Multiobjetivo (NSGA-II) en Python combinados con refinamiento y ajuste manual arquitectónico de circulaciones, automatización con Dynamo y Revit 2024. | ~35 págs. |
| **Capítulo 5** | **Análisis Eólico y Estructural del Caso de Estudio (Edificio 18P):** Cálculo numérico de presiones, succión, cortante basal, momento flector, deriva de piso (drift), confort humano ante aceleraciones top floor. Comparativa exhaustiva: NP 196 vs NBR 6123 vs ASCE 7-22 vs EC1. | ~45 págs. |
| **Capítulo 6** | **Diseño Estructural de Hormigón Armado (Memoria de Cálculo):** Estructura formal canónica de cálculo de pórticos, losas nervadas/reticulares alivianadas (H=35cm y H=45cm), vigas spandrel, recálculo dinámico de pilares por grupos de niveles (flexocompresión biaxial N + Mx + My) y núcleos de H°A°. Fundaciones y muros de contención. Estados Límites Últimos (ELU) y de Servicio (ELS). | ~40 págs. |
| **Capítulo 7** | **Diseño Integral de Instalaciones (MEP) y Coordinación:** Redes Sanitarias, Cloacales, Pluviales (PTE+EBAR), Eléctricas (Subestación ANDE 60m²), Contra Incendio (PCI), Climatización/Ventilación y Sistema RSU (Pleno T1-T2). Detección de interferencias. | ~30 págs. |
| **Capítulo 8** | **Presupuesto, Cómputo Métrico y Cronograma 4D/5D:** Cómputo detallado ítem por ítem, precios unitarios (CYPE/CAPACO), cronograma de obra de 18 pisos, análisis de factibilidad económica y sustentabilidad. | ~15 págs. |
| **Capítulo 9** | **Conclusiones, Recomendaciones y Futuras Líneas de Investigación.** | ~15 págs. |
| **Anexos A** | **Memorias de Cálculo Detalladas:** Planillas tabuladas nivel por nivel de presiones de viento (NP 196/NBR/ASCE/EC1), momentos, cortantes, armaduras de pilares, vigas, losas y anclajes. | ~25 págs. |
| **Anexos B** | **Código Fuente Python Completo:** Scripts documentados línea por línea de NSGA-II y cálculo estructural (`ga_master_planta_baja.py`, `ga_grilla_pilares.py`, `losas_nervadas.py`, `cargas_gravitatorias.py`, etc.). | ~20 págs. |
| **Anexos C** | **Pliego de Especificaciones Técnicas y Planos de Referencia.** | ~15 págs. |
| **TOTAL** | | **~360 págs.** (Supera ampliamente las 300 págs.) |

---

## 🏛️ Estructura Canónica Obligatoria de la Memoria de Cálculo (6 Pilares)

> **REGLA DE ORO DE INGENIERÍA ESTRUCTURAL:** Todo documento, capítulo o anexo que funcione como memoria de cálculo debe estructurarse obligatoriamente bajo los siguientes **6 apartados canónicos**:

1. **Memoria Descriptiva y Objetivos:**
   - Descripción física, funcional y tipológica de la estructura (18 pisos + PB libre 4m + 3 subsuelos a -10.50m + azotea técnica).
   - Justificación del sistema estructural adoptado: grilla continua sin apeos, losas nervadas alivianadas (menor masa sísmica/inercial), vigas de borde perimetrales spandrel y núcleos rígidos de H°A°.
   - Objetivos de desempeño estructural y niveles de seguridad.

2. **Normativa Aplicable y Códigos de Diseño:**
   - **Norma Paraguaya:** NP 196:1991 (*Cálculo de la acción del viento sobre las construcciones*).
   - **Normas Regionales e Internacionales de Viento:** NBR 6123:2023, ASCE 7-22, EN 1991-1-4 (Eurocódigo 1).
   - **Diseño en Hormigón Armado:** NBR 6118:2023 / ACI 318-19 (Capítulos 8 y 9 para losas nervadas y joists).
   - **Acciones Gravitatorias y Combinaciones:** NBR 6120 (Cargas mínimas) y NBR 8681 / ASCE 7 (Estados límites y combinaciones).

3. **Hipótesis de Carga y Acciones de Diseño:**
   - **Acciones Permanentes ($g$):** Peso propio estructural ($25\text{ kN/m}^3$), peso equivalente losa nervada ($4.75\text{ kN/m}^2$, $e_{eq}=19\text{ cm}$), acabados ($1.00\text{ kN/m}^2$), tabiquería equivalente ($1.50\text{ kN/m}^2$) $\to g_{total} = 7.25\text{ kN/m}^2$.
   - **Acciones Variables ($q$):** Sobrecargas de uso residencial ($2.00\text{ kN/m}^2$), comercial ($3.00-5.00\text{ kN/m}^2$), cocheras ($2.50\text{ kN/m}^2$) y azotea.
   - **Acciones Climáticas de Viento ($W$):** Velocidad básica local ($V_0 = 45\text{ m/s}$ en Ciudad del Este), factores de corrección ($S_1, S_2, S_3$ o equivalentes), perfiles de presión dinámica por nivel.
   - **Combinaciones de Diseño:** Estados Límites Últimos (ELU: $1.4g + 1.4q$; $1.2D + 1.6W + 1.0L$) y de Servicio (ELS: $g + q$).

4. **Propiedades de los Materiales y Durabilidad:**
   - **Hormigón Estructural:** $H\text{-}30$ / $C30$ ($f'_c = 30\text{ MPa}$, $f_{cd} = 21.43\text{ MPa}$, $E_c = 25.74\text{ GPa}$, $\gamma_c = 25\text{ kN/m}^3$, $\nu = 0.20$).
   - **Acero de Refuerzo:** $CA\text{-}50$ / Grado 60 ($f_y = 500\text{ MPa}$, $f_{yd} = 434.78\text{ MPa}$, $E_s = 200\text{ GPa}$).
   - **Recubrimientos y Durabilidad:** Clase de agresividad ambiental II, $c_{nom} = 25\text{ mm}$ en losas, $30-40\text{ mm}$ en vigas/pilares.

5. **Modelado Matemático y Criterios de Análisis:**
   - Modelación de entrepisos: franja tributaria viga continua analítica con coeficientes de Cross exactos y verificación FEM en Python (`PyNite` / `losas_nervadas.py`).
   - Modelación global 3D: pórticos espaciales y bajada de cargas axiales por áreas tributarias (`cargas_gravitatorias.py` y `modelo_3d.py`).
   - Modelo de rigidez lateral: núcleo doble de pantallas H°A° trabajando en voladizo, evaluación de derivas ($\Delta/h \le 1/500$), efectos P-Delta ($\gamma_z$) y confort dinámico.

6. **Dimensionamiento y Verificación de Elementos:**
   - **Losas Nervadas:** Flexión en apoyo ($M^-$) y tramo ($M^+$ sección T), corte ($V_u$ vs $\phi V_c$ + estribos $2\varnothing 6\text{ c/}15$), flechas ELS ($f = 6.2\text{ mm} \le L/480 = 16.4\text{ mm}$), anclajes ($l_d$) y armadura de capa de compresión.
   - **Pilares:** Escalonamiento por grupos ($90\times 90$, $80\times 80$, $70\times 70$, $60\times 60\text{ cm}$) y flexocompresión biaxial ($N_u + M_x + M_y$).
   - **Pantallas y Núcleos:** Resistencia al vuelco, corte por fricción y cortante basal.
   - **Vigas Spandrel y Muros de Contención:** Flexión, corte, torsión perimetral y empujes de suelo/freático en subsuelos.

---

## 🚀 Checklist de Hitos y Plan de Acción Ejecutivo

### FASE 1: Consolidación del Anteproyecto e Investigación Teórica
- [x] Tarea 1 Word (Entregable corto inicial) con 4 figuras técnicas y referencias IEEE.
- [ ] Redacción extendida del **Capítulo 2 (Marco Teórico de Viento)** y **Capítulo 3 (Comparativa Multi-Normativa: NP 196 / NBR / ASCE / EC1)** en Word/Markdown.

### FASE 2: Modelado BIM Completo en Revit 2024 & Scripts Python
- [x] Script `ga_master_planta_baja.py` (Layout PB y RSU).
- [x] Scripts `ga_planta_tipo_A/B/C.py` (3 layouts residenciales P01–P18, 432 aptos).
- [x] Script `ga_grilla_pilares.py` (Pilares continuos y Ejes).
- [x] Script `ga_subsuelo_1/2/3.py` (Subsuelos y Rampas).
- [ ] Exportación de Coordenadas a CSV y Carga Paramétrica en Revit 2024.

### FASE 3: Cálculo Eólico Profundo y Simulación Estructural (6 Pilares)
- [ ] Script `calculo_viento_multinormativo.py` (Planillas piso por piso comparando **NP 196:1991**, NBR 6123, ASCE 7-22 y EC1).
- [ ] Verificación de Rigidez Lateral y Núcleo de H°A° (Momentos de Vuelco y Derivas).
- [ ] Verificación de Confort Humano por Aceleraciones Eólicas en Piso 18.
- [x] Script `losas_nervadas.py` (Cálculo manual vs FEM PyNite de losa nervada alivianada).
- [ ] Script `pilares_dimensionamiento.py` (Flexocompresión biaxial por grupos de niveles).

### FASE 4: Redacción del Documento Maestro de 300 Páginas
- [ ] Ensamblaje automatizado del documento completo de Tesis con scripts Node.js / `docx` (`build_tesis.js`).
- [ ] Inclusión de Gráficos de alta resolución, Tablas de Cómputo y Planillas de Armado.
- [ ] Generación y compilación de Memorias de Cálculo en Anexo A (LaTeX / PDF / Word).
- [ ] Revisión final de referencias IEEE y formato académico UNINTER.

---

## 📌 Nota para el Agente (Copilot)
Cualquier agente que retome esta conversación debe leer este archivo `00_GESTION_DE_PROYECTO/ROADMAP_TESIS_300_PAGINAS.md` y `AGENTS.md`. **Bajo ninguna circunstancia se debe sugerir acortar o simplificar los capítulos**. Toda memoria de cálculo debe respetar estrictamente la estructura canónica de los 6 pilares de ingeniería civil e incluir la norma paraguaya NP 196:1991 en la comparativa eólica.
