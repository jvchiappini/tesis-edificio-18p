# Ordenanzas Municipales de Ciudad del Este aplicables a la tesis — Análisis de relevancia

> **Proyecto:** Edificio mixto 18P + PB + 3 subsuelos · Terreno 7.618,49 m² · Av. Itaipú Oeste / Calle Los Lapachos, CDE.
> **Fuente:** Repositorio oficial MCDE (mcde.gov.py) · **Extracción:** 2026-09-19 (con navegador headless y HTTP con reintentos).
> **Universo analizado:** **236 ordenanzas** (2020–2026 + Años Varios). Ver `00_INDICE_GENERAL.md`.
> **Criterio:** ALTA = gobierna directamente el diseño · MEDIA = incide en sitio, permisos, obra o presupuesto · BAJA = administrativa.

---

## 1. Advertencia de método (leer antes de usar)

1. El análisis parte del **título + asunto publicado** y, cuando el PDF tenía capa de texto, del **texto extraído** (`02_Texto_Completo/`). Todo artículo citado con número fue **leído del texto extraído**; si no, se indica *"por verificar"*.
2. **45 PDFs eran escaneados** (imagen). Fueron procesados con **OCR nativo de Windows (`Windows.Media.Ocr`, es)** con dpi adaptativo y detección de rotación; su texto está en `02_Texto_Completo/`. Entre ellos ya son legibles las ordenanzas **más críticas de uso de suelo 2026** (003, 006, 007) y la de **altura 010/1988**. *El texto OCR puede contener errores: verificar contra el PDF.*
3. **La categoría 2025 existe**, pero con slug con guion inicial (`-ordenanzas-junta-municipal-ano-2025-cms`); contiene 6 registros (mayormente tributaria/tránsito).
4. Las ordenanzas **base del Código de Edificación** (alturas, retiros, uso de suelo) están en la categoría "Años Varios".

---

## 2. Ordenanzas de relevancia ALTA (gobiernan el diseño)

| ID | Ordenanza | Tema | Artículos / contenido verificado | Ficha |
|---:|---|---|---|---|
| 3146 | **Ord. 011/1994** | Uso del suelo CDE (zonificación A1–A4) | Art.4: retiro mín. **5 m a calles / 6 m a avenidas**. Art.3: A1 máx. **3 plantas**; A2/A3 remiten a Ord. 10/88; A4 = **4 plantas + 1 subsuelo**. Art.5: vereda mín. 2 m. Art.6: pozos ciegos solo sin red cloacal. Art.7: prohíbe industrias nocivas y moteles. | [3146](../02_Texto_Completo/3146_ordenanza-011-1994-.md) |
| 3693 | **Ord. M. 003/2026** | **Modifica 011/1994 y 027/2014** — uso de suelo, planificación urbana, ordenamiento territorial y protección ambiental | **VERIFICADO COMPLETO** — Art.3°: Uso Residencial Mixto. Art.4°: IOS desde subsuelo + Geotecnia/Agua subterránea. Art.5°: Lote mín. 3.000 m², Frente mín. 30 m (4–12P). Art.6°: Retiro frontal 8m calles / 10m avenidas (8m terreno 2 frentes). Art.7°: **Prohibición de fachadas espejo**. | [3693](../02_Texto_Completo/3693_ordenanza-m-n003-2026-jm.md) |
| 3691 | Ord. 006/2026 | Regula uso del suelo y zona residencial Barrio Boquerón II | **ESCANEADO** — verificar si el terreno cae en su ámbito | [3691](../02_Texto_Completo/3691_ordenanza-n-006-2026-jm-.md) |
| 3692 | Ord. 007/2026 | Regula uso del suelo y zona residencial **Área 1** | **ESCANEADO** — verificar ámbito | [3692](../02_Texto_Completo/3692_ordenanza-n-007-2026-jm.md) |
| 3143 | **Ord. 010/1988** | **Altura y características de los edificios** en zona céntrica | **ESCANEADO** — crítica para 18 pisos | — |
| 3144 | Ord. 010/1990 | Modifica art. 28 (inc. c y d) de Ord. 12/88 — locales comerciales | ESCANEADO | — |
| 3118 / 3601 | Ord. 005/1976 (05/76) | **Reglamenta las edificaciones** (código base) | Texto extenso extraído | [3118](../02_Texto_Completo/3118_oedenanza-005-1976-.md) |
| 3122 / 3159 | Ord. 022/1998 | Modifica parcialmente Ord. 05/76 | Texto extraído | [3122](../02_Texto_Completo/3122_ordenanaza-022-1998-.md) |
| 3165 | Ord. 031/1998 | Modifica parcialmente Ord. 05/76 | Texto extraído | — |
| 3170 | Ord. 049/1998 | Modifica parcialmente Ord. 05/76 | ESCANEADO | — |
| 2725 | **Ord. 027/2022** | Reglamenta Art. **227 y 229 Ley 3966/2010**: dimensiones mínimas de lotes/calles | **Superficie mínima de lote urbano = 360 m²**; excepciones y fraccionamientos. | [2725](../02_Texto_Completo/2725_ord027022-por-la-cual-se-reglamenta-las-disposiciones-de-los-art-227-y-229-de-la-ley-3966-sobre-dimensiones-minimas-de-lotes-y-calles-y-avenidas.md) |
| 2462 / 2649 / 3164 | **Ord. 030/2020** | Instalaciones sanitarias y desagües (amplía Ord. 50/97) | **Art.5: obras con cobertura ≥ 2.000 m² deben instalar sistema de tratamiento de efluentes**; Art.9: exige **DIA + PGA (MADES)**. | [2462](../02_Texto_Completo/2462_ordenanza030020-que-modifica-y-amplia-la-ord-5097-jm-que-establece-normas-de-instalaciones-sanitarias-y-desagues.md) |
| 2849 | **Ord. 033/2023** | Amplía y modifica Ord. 030/2020 (efluentes cloacales/industriales/agua servida) | Texto extraído | [2849](../02_Texto_Completo/2849_ord0332023-jm-que-amplia-y-modifica-la-ordenanza-302020-que-establece-las-normas-de-cumplimiento-obligatoria-en-instalaciones-sanitarias-y-desagues.md) |
| 3127 | Ord. 067/1999 | Cámaras **desbarradoras y desengrasadoras** | ESCANEADO | — |
| 3123 / 3250 / 3168 / 3117 | Ord. 038/1999, 026/1990, 024/2005, 001/2006 | **Prevención y protección contra incendios** en edificaciones | Textos extraídos (038/1999 y 026/1990) | [3123](../02_Texto_Completo/3123_ordenanza-038-1999.md) |
| 3161 | Ord. 026/1990 | Normas de seguridad y prevención contra incendio | Texto extraído | — |
| 3160 | Ord. 024/2005 | Amplía Ord. 038/99 (incendios) | ESCANEADO | — |
| 3666 / 2615 | **Ord. 019/2023** | Autorización para **captación de aguas subterráneas** (pozos artesianos/sondeos) | ESCANEADO — relevante para subsuelos/fundaciones | — |
| 3667 | **Ord. 032/2023** | **Delimita la zona industrial** del distrito | ESCANEADO — verificar superposición con el terreno | — |

---

## 3. Hallazgos críticos que impactan los parámetros maestros de la tesis

> ⚠️ **Estos puntos contradicen o condicionan las "hipótesis" fijadas en AGENTS.md. Deben resolverse antes de la Etapa B.**

### 3.1 Retiros — la hipótesis 3 m/3 m/2 m no encuentra respaldo
- La **Ord. 011/1994 (Art. 4)** establece **retiro mínimo de 5 m sobre calles y 6 m sobre avenidas**; admite hacer el retiro sobre una sola calle en esquina (mín. 5 m).
- El terreno tiene **dos frentes** (Calle Los Lapachos y Av. Itaipú Oeste), por lo que el régimen de retiros y el **rectángulo edificable** (hoy X: 2,5→87,5 / Y: 3,0→40,0) podrían cambiar.
- **Acción:** determinar la **zona de uso de suelo** del terreno (ver 3.4) y leer **Ord. 003/2026** (que modifica 011/1994) para confirmar los retiros vigentes.

### 3.2 FOS = 0,70 y FOT = 4,0 — origen sin verificar
- La base de conocimiento cita *"Ordenanza 030/2000 y 024/2014 (Plan Regulador / Código de Edificación)"*, pero **dichas ordenanzas no aparecen en el repositorio oficial 2020–2026 ni en Años Varios**. El ID 030/2020 es de instalaciones sanitarias, no urbanística.
- **Acción:** solicitar a la Municipalidad (Dirección de Planificación / Catastro) la ordenanza vigente del Plan Regulador / Código de Edificación que fija FOS/FOT y la asignación de zona del inmueble.

### 3.3 Altura — depende de la zona
- **Ord. 011/1994** permite en **A1 solo 3 plantas**; en **A2/A3** remite a la **Ord. 010/1988**; en **A4** hasta **4 plantas + 1 subsuelo**.
- Un edificio de **18 pisos** solo es admisible si el terreno está en una zona de alta densidad definida por **Ord. 010/1988** o por la reforma de **Ord. 003/2026**.
- **Acción:** leer 010/1988 (OCR) y 003/2026 (OCR) y confirmar el **régimen de altura** aplicable.

### 3.4 Zona de uso de suelo del terreno — verificación imprescindible
- La **Ord. 011/1994** delimita zonas A1, A1(1), A1(2), A2(1–3), A3 y A4. La zona **A2(2)** menciona explícitamente la *"Avda. Los Lapachos"*, y la **A4** linda al Oeste con *"Los Lapachos y Cayguá"*.
- **Ord. 007/2026** establece zona residencial del **"Área 1"**; **Ord. 006/2026** del **Barrio Boquerón II**.
- **Acción:** con el polígono UTM (P1–P4) y las calles linderas, consultar el **plano de zonificación municipal**. Esto fija retiros, altura, FOS/FOT y usos permitidos (mixto residencial + comercial + amenities).

### 3.5 Tratamiento de efluentes — obligatorio para el proyecto
- La **Ord. 030/2020 (Art. 5)** obliga a **sistema de tratamiento de efluentes** a toda obra con cobertura ≥ **2.000 m²**; el proyecto (~3.145 m²/planta) **supera ampliamente** ese umbral.
- Exige además **DIA + PGA aprobados por el MADES** (Art. 9) y remite a Ley 5.428/15, Ley 294/93, Ley 1.614/00, Ley 716/96.
- **Acción:** incorporar **PTAR** y plan de gestión ambiental al alcance de tesis (incide en losa de subsuelo, sótanos y presupuesto).

---

## 4. Ordenanzas de relevancia MEDIA (sitio, permisos, obra y presupuesto)

| Tema | Ordenanzas (ID) |
|---|---|
| Ruidos y polución sonora (obra) | 028/2020 (2464), 050/2021 (2697), 019/2014 (3172), 28/20 (2642, 3173) |
| Contaminación ambiental y residuos | 029/2020 (2463), 037/2020 (2455) |
| Bosque urbano y arbolado (retiros/jardín) | 019/2022 (2717) |
| Calidad del aire | 004/2021 (2537) |
| Patios baldíos y limpieza | 007/2020 (2646), 009/2022 (2707) |
| Escombros y contenedores de obra | 009/1998 (3140), 027/2020 (2465) |
| Veredas y murallas | 002/1976 (3131), 002/1997 (3132) |
| Regularización / profesionales de la construcción | 015/1997 (3151), 016/1988 (3152), 006/2000 (3136) |
| Prohibición/restricción de construcciones | 015/1991 (3150) |
| Publicidad y carteles en fachada | 010/2011 (3120), 020/2017 (3121), 066/1999 (3126), 009/1989 (3142), 036/2000 (3166/3128) |
| Torres de antenas | 008/2000 (3665), 019/2015 (3664) |
| Numeración domiciliaria | 018/2022 (2716) |
| Tasa de prevención de incendios | 021/2018 (3158), 028/1990 (3163) |
| Estacionamiento vehicular | 042/2020 (2450), 005/2021 (2536), 013/2025 (3533) |
| Tributaria / tasas de construcción (5D presupuesto) | Tributarias 2020–2026 (p. ej. 021/2020-2471, 043/2021-2500, 017/2024-3035, 040/2024-3303, 004/2026-3743) |

---

## 5. Ordenanzas descartadas (relevancia BAJA) — resumen

Tránsito y transporte, nomenclatura de calles/plazas, presupuestos y ampliaciones de caja, juegos de azar, patentes comerciales, tenencia de animales, playas/mercados, plataformas (Uber/MUV), atención preferencial, etc. Catalogadas íntegramente en `01_Catalogo_Por_Anio/`.

---

## 6. Lista de uso prioritario para la tesis (ordenada por impacto)

| Prioridad | Ordenanza (ID) | Para qué se usa |
|---|---|---|
| 1 | **011/1994 (3146)** + **003/2026 (3693)** + **007/2026 (3692)** / **006/2026 (3691)** | Uso de suelo, zona, retiros, usos permitidos |
| 1 | **010/1988 (3143)** + **010/1990 (3144)** | Altura y volumetría (18 pisos) |
| 1 | **005/1976 (3118/3601)** + modificatorias (3122, 3165, 3170) | Código base de edificaciones |
| 1 | **027/2022 (2725)** | Dimensiones mínimas de lotes (Ley 3966/2010) |
| 1 | **030/2020 (2462)** + **033/2023 (2849)** | Instalaciones sanitarias, PTAR, DIA/PGA |
| 1 | **038/1999 (3123)** + **026/1990 (3161)** + **024/2005 (3160)** + **001/2006 (3117)** | Seguridad contra incendios |
| 2 | **019/2023 (3666)** | Captación de aguas subterráneas / pozos |
| 2 | **032/2023 (3667)** | Zona industrial (verificar superposición) |
| 2 | **067/1999 (3127)** | Cámaras desbarradoras/desengrasadoras |
| 3 | Ruido (028/2020, 050/2021), ambiente (029/2020), bosque urbano (019/2022), escombros (009/1998) | Plan de gestión de obra |
| 3 | Tributaria vigente (040/2024 + modif. 2025–2026) | Tasas y presupuesto 5D |

---

## 7. Pendientes inmediatos

- [x] **OCR** de las 45 escaneadas (003/2026, 006/2026, 007/2026, 010/1988, 010/1990, 019/2023, 032/2023, 067/1999, 024/2005, 001/2006, etc.) → hecho con OCR Windows (es). Revisar calidad de casos con bajo rendimiento (p. ej. 015/1997).
- [ ] **Determinar la zona de uso de suelo** del terreno (plano de zonificación municipal) → fija retiros, altura y FOS/FOT.
- [ ] **Verificar el origen legal de FOS=0,70 / FOT=4,0** (no respaldado por ordenanza publicada).
- [ ] Actualizar `07.04_Normativa_Resumen/Normativa_Urbanistica_CDE_Planimetria_UTM_v01.md`, que cita "Ord. 030/2000 y 024/2014" sin respaldo en el repositorio oficial.
