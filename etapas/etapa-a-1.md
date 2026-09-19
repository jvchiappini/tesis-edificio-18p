# A.1 — Formalización del Terreno

> **Etapa A › Sub-etapa 1** · **Tareas:** 4 · **Estado:** ✅ Completado
> Normativa: Municipalidad CDE (Ordenanzas 030/2000 y 024/2014) · Ley de Mensura N° 1083/1985 · NOMENCLATURA.md

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de tareas

- [x] **eA-1** · **Planimetría del polígono real con coordenadas UTM**
  - Trazar el polígono: P1(737721.76, 7176185.26) → P2(737837.53, 7176203.96) → P3(737853.36, 7176246.13) → P4(737755.78, 7176281.93)
  - Coordenadas extraídas mediante teledetección y digitalización satelital (Google Earth Pro v7.3, UTM Zona 21J WGS84/SIRGAS2000)
  - Calcular área exacta (7.618,49 m²) por método de Gauss/Shoelace
  - Verificar cierre de poligonal ($e_L = 0,00$ m, suma de ángulos interiores = 360,00°)
  - Archivo de referencia: `05_RECURSOS/05.05_Scripts_Python/01_Geometria_Terreno/geometria_terreno.py` · `NOMENCLATURA.md`

- [x] **eA-2** · **Identificación de calles y orientación geográfica**
  - Frente principal P1→P2 (117,27 m) sobre **Calle Los Lapachos** (Azimut 80,82°, Rumbo N 80°49' E)
  - Frente secundario P2→P3 (45,04 m) sobre **Calle Los Sauces** (Azimut 20,58°, Rumbo N 20°35' E)
  - Lindero posterior P3→P4 (103,94 m) lindante con **inmueble residencial privado unifamiliar** (predio vecino de dominio particular)
  - Frente secundario / lindero lateral P4→P1 (102,48 m) sobre **Avenida Itaipú Oeste** (Azimut 199,39°, Rumbo S 19°23' W)
  - Determinar Norte verdadero vs. Norte magnético (declinación magnética en CDE = -13,8° W ≈ -14°)

- [x] **eA-3** · **Análisis del vértice agudo P1 (61,44°) y definición de la cuña**
  - Demarcar la zona no edificable en la esquina de intersección entre Av. Itaipú Oeste y Calle Los Lapachos ($\alpha_1 = 61,44°$)
  - El rectángulo edificable comienza en $u = 27,00$ m desde P1 sobre Calle Los Lapachos
  - Cuña frontal no edificable de $669,55$ m² destinada a plaza seca de acceso peatonal, control de acceso y jardín ornamental sustentable
  - Polígono edificable reducido de $85,0$ m × $37,0$ m ($3.145,00$ m² por planta) como **hipótesis formal de tesis** con retiros adoptados: 3,0 m frente, 3,0 m fondo, 2,0 m laterales
  - ⚠️ El vértice P1 de 61,44° impide estructura regular hasta esa esquina — declarado explícitamente en la memoria de tesis

- [x] **eA-4** · **Certificado de uso de suelo y normativa municipal**
  - FOS = 0,70 → área máxima de huella = 5.332,94 m² (Huella adoptada = 3.145,00 m², FOS real = 41,28% ≤ 70,00% → CUMPLE)
  - FOT = 4,0 → área total construible = 30.473,96 m²
  - Subsuelos exentos del cómputo FOT según ordenanza municipal de CDE
  - ⚠️ Con huella de 3.145,00 m² y 18 pisos residenciales + PB (19 plantas sobre rasante): área construida = 59.755,00 m² > FOT (30.473,96 m²). Requiere varianza municipal por régimen especial de desarrollo de alta densidad

### Decisiones tomadas

| Fecha | Decisión | Fundamento |
|---|---|---|
| 2026-09-19 | Origen de Coordenadas UTM | Teledetección Satelital (Google Earth Pro v7.3, UTM 21J WGS84) — Hipótesis de anteproyecto |
| 2026-09-19 | Nomenclatura Vial y Colindancias | P1-P2: Calle Los Lapachos · P2-P3: Calle Los Sauces · P3-P4: Inmueble Residencial Privado · P4-P1: Av. Itaipú Oeste |
| 2026-09-19 | Retiros adoptados: 3,0 m frente / 3,0 m fondo / 2,0 m laterales | Hipótesis de tesis congelada para desarrollo arquitectónico y estructural |
| 2026-09-19 | FOS = 0,70 / FOT = 4,0 (Huella 3.145 m² / FOS real = 41,28%) | Cumplimiento estricto de FOS municipal |
| 2026-09-19 | Solicitud de Varianza Urbanística para FOT (59.755 m²) | Justificado por exención de subsuelos y convenio de desarrollo de alta densidad |
| 2026-09-19 | Destino de cuña aguda P1 (669,55 m²) | Plaza seca de acceso peatonal, control de acceso y paisajismo ambiental |

### Archivos de referencia

| Archivo | Descripción | Estado |
|---|---|---|
| `00_GESTION_DE_PROYECTO/NOMENCLATURA.md` | Convención de nombres CDE / ISO 19650 | Existente |
| `05_RECURSOS/05.05_Scripts_Python/01_Geometria_Terreno/geometria_terreno.py` | Script Python de verificación geométrica del predio | Creado / Verificado |
| `07_KNOWLEDGE_BASE/07.04_Normativa_Resumen/Normativa_Urbanistica_CDE_Planimetria_UTM_v01.md` | Documento técnico de base de conocimiento CDE | Creado / Verificado |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO

### 1.1 Descripción del predio, planimetría y metodología de relevamiento

El terreno objeto de estudio se ubica en la ciudad de **Ciudad del Este**, departamento de Alto Paraná, República del Paraguay. Las coordenadas cartesianas de los vértices del predio fueron obtenidas mediante **técnicas de teledetección y digitalización de ortofotos satelitales (Google Earth Pro v7.3)** referenciadas al sistema de coordenadas **UTM Zona 21J, dátum WGS84 / SIRGAS2000**, resultando en la siguiente planimetría:

| Vértice | Este X (m) | Norte Y (m) | Lado | Longitud (m) | Azimut Norte (°) | Denominación de Vía Pública / Lindero Predial |
|---|---|---|---|---|---|---|
| **P1** | 737.721,76 | 7.176.185,26 | P1 → P2 | 117,271 | 80,82° | **Calle Los Lapachos** (Frente Principal N 80°49' E) |
| **P2** | 737.837,53 | 7.176.203,96 | P2 → P3 | 45,043 | 20,58° | **Calle Los Sauces** (Frente Secundario N 20°35' E) |
| **P3** | 737.853,36 | 7.176.246,13 | P3 → P4 | 103,940 | 290,15° | **Inmueble Residencial Privado** (Lindero Posterior / Predio Vecino) |
| **P4** | 737.755,78 | 7.176.281,93 | P4 → P1 | 102,481 | 199,39° | **Avenida Itaipú Oeste** (Frente Secundario S 19°23' W) |

#### Consideración metodológica sobre la precisión planimétrica

> **Nota técnica de tesis:** Las coordenadas UTM de los puntos P1 a P4 no fueron relevadas mediante una mensura geodésica directa con equipos GNSS diferencial (RTK/Estación Total) en campo, sino mediante la extracción de vectores en Google Earth Pro. Para fines del anteproyecto académico de tesis, este nivel de precisión planimétrica (con una incertidumbre posicional relativa estimada entre $\pm 1,5\text{ m}$ y $\pm 2,5\text{ m}$) resulta plenamente adecuado para la delimitación del polígono edificable. Se deja constancia de que, para la fase ejecutiva de construcción del proyecto, se requerirá un relevamiento topográfico perimetral definitivo a cargo de un perito agrimensor matriculado, en cumplimiento de la Ley N° 1083/1985 de Mensura y Procedimiento Catastral del Paraguay.

El área bruta del predio calculada mediante la regla de Gauss (algoritmo de Shoelace) resulta en **7.618,49 m²**, con un perímetro total de **368,74 m**. El frente principal se extiende a lo largo de la **Calle Los Lapachos** (tramo P1→P2) con **117,27 m** de desarrollo. El frente secundario de **45,04 m** (tramo P2→P3) linda sobre la **Calle Los Sauces**, mientras que el lindero lateral/frente secundario de **102,48 m** (tramo P4→P1) limita con la **Avenida Itaipú Oeste**. El lindero posterior de **103,94 m** (tramo P3→P4) colinda directamente con un **inmueble unifamiliar residencial de dominio privado** (predio vecino).

La declinación magnética local en Ciudad del Este se determina en **-13,8° W**, lo que implica una rotación de $13,8^\circ$ al Oeste entre el Norte magnético y el Norte verdadero.

#### Restricción geométrica — vértice agudo P1 (Intersección Av. Itaipú Oeste y Calle Los Lapachos)

El análisis de los ángulos interiores del polígono revela la siguiente configuración geométrica:
- Ángulo en $P_1$: $\alpha_1 = 61,44^\circ$ ($61,4365^\circ$) $\to$ Intersección Av. Itaipú Oeste / Calle Los Lapachos
- Ángulo en $P_2$: $\alpha_2 = 119,75^\circ$ ($119,7510^\circ$) $\to$ Intersección Calle Los Lapachos / Calle Los Sauces
- Ángulo en $P_3$: $\alpha_3 = 89,57^\circ$ ($89,5716^\circ$) $\to$ Esquina Calle Los Sauces / Lindero Privado Vecino
- Ángulo en $P_4$: $\alpha_4 = 89,24^\circ$ ($89,2409^\circ$) $\to$ Esquina Lindero Privado Vecino / Av. Itaipú Oeste
- Suma total de ángulos interiores: $360,00^\circ$ (Cierre teórico exacto).

El vértice $P_1$ presenta un **ángulo interior de 61,44°**, clasificándose como vértice agudo severo. Esta condición geométrica en la esquina de la Av. Itaipú Oeste y Calle Los Lapachos impide inscribir una estructura rectangular regular con grilla continua de pilares hasta dicha esquina. La zona triangular resultante de **669,55 m²** (cuña frontal de $27,00$ m de base sobre Calle Los Lapachos y $49,60$ m de altura perpendicular) se destina formalmente a:
- Acceso peatonal principal y plaza seca de recepción desde la vía pública
- Jardín de borde ornamental y arbolado nativo de amortiguación ambiental
- Chaflán arquitectónico de fachada y control de accesos

El rectángulo edificable neto inscripto de **85,0 m × 37,0 m** (área por planta = **3.145,00 m²**) comienza a una distancia de **27,00 m** desde el vértice $P_1$ medida sobre el eje de la Calle Los Lapachos (lado P1→P2).

```
          P4 (737755.78, 7176281.93) ─── L34 = 103.94 m (Predio Vecino Privado) ── P3 (737853.36, 7176246.13)
                      │                                                                       │
 Av. Itaipú Oeste     │  ┌─────────────────────────────────────────────────────────────────┐ │  Calle Los Sauces
 (L41 = 102.48 m)     │  │                  RECTÁNGULO EDIFICABLE                          │ │  (L23 = 45.04 m)
                      │  │                 85.00 m  ×  37.00 m                             │ │
                      │  │                (Superficie: 3.145,00 m²)                        │ │
                      │  └─────────────────────────────────────────────────────────────────┘ │
                      │ <── 27.00 m ──>                                                       │
  P1 (737721.76, 7176185.26) ──────── L12 = 117.27 m (Calle Los Lapachos - Frente Principal) ───── P2 (737837.53, 7176203.96)
        ▲  (61.44° Cuña Jardin: 669.55 m²)                                                  (N 80°49' E)
```

### 1.2 Parámetros urbanísticos y uso del suelo

De acuerdo con el Código de Edificación y Ordenamiento Urbano y Territorial de la Municipalidad de Ciudad del Este (Ordenanzas N° 030/2000 y N° 024/2014), los indicadores urbanísticos aplicables a la parcela son:

| Indicador | Valor Normativo / Adoptado | Estado de Cumplimiento | Observación / Fundamento |
|---|---|---|---|
| **Factor de Ocupación del Suelo (FOS)** | 0,70 (70,00%) | ✅ CUMPLE (41,28%) | Área máx. huella = $5.332,94\text{ m}^2$. Huella adoptada = $3.145,00\text{ m}^2$. |
| **Factor de Ocupación Total (FOT)** | 4,0 | ⚠️ Varianza solicitada | Área máx. construible = $30.473,96\text{ m}^2$. Áreas sobre rasante = $59.755,00\text{ m}^2$. |
| **Retiro frontal** | 3,0 m | ✅ Adoptado | Sobre el frente Calle Los Lapachos ($117,27\text{ m}$). |
| **Retiro de fondo** | 3,0 m | ✅ Adoptado | Sobre el lindero del inmueble privado residencial ($103,94\text{ m}$). |
| **Retiros laterales** | 2,0 m c/u | ✅ Adoptado | Sobre Calle Los Sauces ($45,04\text{ m}$) y Av. Itaipú Oeste ($102,48\text{ m}$). |
| **Altura máxima** | Sin restricción de altura | ✅ Conforme | Sujeto a plano de gálibo e iluminación según ordenanza CDE. |

> **Nota de hipótesis urbanística:** El edificio proyectado de 18 pisos residenciales + Planta Baja comercial y 3 subsuelos origina un área construida sobre rasante de **59.755,00 m²** (excluyendo los $9.435,00\text{ m}^2$ de los 3 subsuelos exentos del FOT según ordenanza). Este valor excede el límite del FOT=4,0 ($30.473,96\text{ m}^2$). El proyecto se desarrolla bajo la hipótesis formal de concesión de una **varianza urbanística por régimen de desarrollo inmobiliario de alto impacto e interés municipal**, instrumento previsto en el Código Urbanístico de Ciudad del Este mediante convenio de desarrollo urbano aprobado por la Junta Municipal.

---

### Referencias bibliográficas — A.1

- Municipalidad de Ciudad del Este — *Código de Ordenamiento Urbano y Territorial y Plan Regulador* (Ordenanzas N° 030/2000 y N° 024/2014), CDE, Paraguay.
- Dirección del Servicio Geográfico Militar (DISERGEMIL / IGM) — *Red Geodésica Nacional y Sistema de Referencia SIRGAS2000 / WGS84*, Asunción, Paraguay.
- Ley N° 1083/1985 — *Ley de Mensura y Procedimiento Catastral de la República del Paraguay*.
- Google LLC — *Google Earth Pro v7.3 Satellite Imaging & Geographic Data*, Mountain View, CA.
- INTN — Instituto Nacional de Tecnología y Normalización: Normativa Técnica Paraguaya.
