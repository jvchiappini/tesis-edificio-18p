# Análisis de Viento y Clasificación de Exposición — CDE — eA-5

> **Base de Conocimiento** · Proyecto Tesis 18P · Sub-etapa A.2 · Tarea eA-5
> Última actualización: 2026-09-19 · Autor: José Valentino Chiappini Vergara

---

## 1. Propósito del documento

Registrar de forma permanente los resultados técnicos de la tarea **eA-5 — Análisis de vientos dominantes y exposición**, evitando que se repita la investigación en etapas posteriores. Este documento es la fuente de verdad para la clasificación de exposición del terreno en la Etapa E (cálculo multinormativo de viento).

---

## 2. Datos del sitio

| Parámetro | Valor |
|---|---|
| Ciudad | Ciudad del Este, Departamento de Alto Paraná, Paraguay |
| Coordenadas | Lat: −25,50° (25°30'S) · Lon: −54,62° (54°37'W) |
| Altitud media | ~230 m s.n.m. |
| Clima Köppen | Cfa — Subtropical húmedo (sin estación seca, verano cálido) |

---

## 3. Régimen de vientos — Patrón estacional

**Fuente:** ERA5/ECMWF reanálisis 1991–2020, verificado con WeatherSpark (2026).
**Estado:** Hipótesis de anteproyecto. Verificar con DMH/DINAC anuario estadístico oficial.

| Período | Dirección dominante | Frecuencia aprox. | Mecanismo |
|---|---|---|---|
| Dic–feb (verano) | **Norte (N)** | ~8,5 % anual | Flujos cálidos Atlántico Norte / baja térmica Chaco |
| Feb–dic (resto año) | **Este (E)** | ~20,5 % anual (pico ~39 % en agosto) | Anticiclón Atlántico Sur |
| May–ago (frentes fríos) | **Sur (S)** | ~6,5 % anual | «Pampero» — masa polar desde Patagonia/Argentina |

**Velocidad media anual:** ~10,0 km/h (~2,8 m/s) a 10 m de altura (dato de servicio, no de diseño).

---

## 4. Velocidad básica de referencia — NP 196:1991

$$V_0 = 45{,}0 \text{ m/s}$$

- **Norma:** NP 196:1991, §5 — Mapa de isopletas de viento, Región Oriental del Paraguay.
- **Definición:** Velocidad media (análoga a media de 10 min / ráfaga 3 s según definición NBR 6123 en que se basa la NP 196), medida a 10 m sobre terreno plano, Categoría II.
- **Período de retorno:** T = 50 años (p_excedencia_anual = 2%).
- **Factor S3 adoptado:** S3 = 1,10 para edificio de alta densidad de ocupación (mixto residencial-comercial).

### Limitaciones documentadas de la NP 196:1991

1. **Solo eventos sinópticos:** No contempla tormentas convectivas (turbonadas), que en Paraguay frecuentemente superan a los eventos sinópticos. (Martínez et al., CILAMCE-PANACM 2021).
2. **Sin análisis dinámico:** No tiene método para el factor de ráfaga dinámico en estructuras esbeltas. (Ibarra et al., NewTech 2024 — ICCEIA 132).

Estas limitaciones justifican el análisis multinormativo con NBR 6123:2023, ASCE 7-22 y EN 1991-1-4.

---

## 5. Clasificación de exposición del terreno — Tabla multinormativa

**Entorno del predio:** Zona urbana de densidad media-alta, sector sur CDE (Av. Itaipú Oeste / Calle Los Lapachos). Edificaciones de 1–5 pisos (4–18 m), espaciado < 5 veces altura media de obstáculos, radio 500 m a 2 km.

| Norma | Artículo / Tabla | Categoría adoptada | Parámetros clave | Vk(z=10m) [m/s] |
|---|---|---|---|---|
| **NP 196:1991** | §5, Tabla 2, Clase B | **Categoría III** | b=0,85 · p=0,175 · zmin=5 m | **38,25** |
| **NBR 6123:2023** | §6.2, Tabela 4, Classe B | **Categoria IV** | bm=0,86 · p=0,20 · Fr=1,00 · zmin=10 m | **38,70** |
| **ASCE 7-22** | §26.7.3, Table 26.10-1 | **Exposure B** | α=7,0 · zg=365,76 m · zmin=4,572 m | **33,13** |
| **EN 1991-1-4** | §4.3, Tabla 4.1 | **Categoría III** | z0=0,30 m · zmin=5 m · kr=0,215 | **34,08** |

### ⚠️ Correcciones respecto al borrador previo

| Norma | Valor anterior (INCORRECTO) | Valor correcto |
|---|---|---|
| NBR 6123:2023 | Cat. III | **Cat. IV** (zona urbana densa con obstáculos numerosos) |
| ASCE 7-22 | Exposure C | **Exposure B** (urban/suburban — §26.7.3) |

---

## 6. Fórmulas del perfil de velocidad con la altura

### 6.1 NP 196:1991 y NBR 6123:2023 — Factor S2(z)

```
Vk(z) = V0 · S1 · S2(z) · S3

S2(z) = b · (z/10)^p   para z >= zmin
S2(z) = b · (zmin/10)^p  para z < zmin
```

| Cat. | Clase | b | p | zmin [m] | z0 equiv. [m] |
|---|---|---|---|---|---|
| III | B | 0,85 | 0,175 | 5 | ~0,30 |
| IV | B | 0,86 | 0,20 | 10 | ~1,00 |

### 6.2 EN 1991-1-4:2010 — Factor de rugosidad cr(z) — §4.3.2

```
vm(z) = cr(z) · co(z) · vb
cr(z) = kr · ln(z / z0)    para zmin <= z <= 200 m
kr = 0,19 · (z0 / 0,05)^0,07
co = 1,0  (terreno plano CDE, sin efecto orográfico)
```

| Cat. | z0 [m] | zmin [m] | kr |
|---|---|---|---|
| III | 0,30 | 5 | 0,215 |
| IV | 1,00 | 10 | 0,234 |

### 6.3 ASCE 7-22 — Coeficiente Kz — §26.10.1, Table 26.10-1

```
Kz = 2,01 · (z / zg)^(2/α)   para zmin <= z <= zg
Kz = Kz(zmin)                 para z < zmin

Exposure B: α=7,0 · zg=365,76 m · zmin=4,572 m (15 ft)
```

Presión de viento: qz = 0,613 · Kz · Kzt · Ke · V² [Pa, V en m/s]

---

## 7. Advertencia inter-normativa: definición de velocidad básica

| Norma | Tipo de velocidad | Equivalencia |
|---|---|---|
| NP 196:1991 | Media de 10 min a 10 m, Cat. II | V = 45 m/s |
| NBR 6123:2023 | Media de 10 min a 10 m, Cat. II | V = 45 m/s |
| ASCE 7-22 | Ráfaga de 3 s a 10 m, Cat. II | V3s ≈ 1,25 × V10min ≈ 56,25 m/s |
| EN 1991-1-4 | Media de 10 min a 10 m, Cat. II | vb = 45 m/s |

**Conclusión:** Para comparación cualitativa de perfiles (eA-5), se usa V0=45 m/s como base en todas las normas. Para comparación cuantitativa de presiones y fuerzas (Etapa E), se aplicarán los factores de conversión correspondientes.

---

## 8. Implicancias para la Etapa E — Cálculo multinormativo de viento

1. **Direcciones de análisis:** Eje E–O (azimut ~90°, mayor frecuencia) y Eje N–S (azimut ~0°/180°, mayor intensidad por frentes fríos). Ambas direcciones ortogonales al eje del edificio.
2. **Factor S2 / cr / Kz por nivel:** Calcular piso a piso para z = 0 m (PB) hasta z ≈ 64 m (P18) + azotea z ≈ 80 m.
3. **Factor de ráfaga dinámico:** Requerido por NBR 6123:2023 (coeficiente ξ) y ASCE 7-22 (Gust Factor Gf ≥ 0,85 para estructuras rígidas; Gf dinámico para esbeltas). La NP 196 no lo contempla — usar método Ibarra et al. (2024) como referencia académica complementaria.
4. **Coeficientes de forma Cf:** Obtener según NBR 6123:2023 Anexo B (planta rectangular H/B=1,73) y ASCE 7-22 §27 (MWFRS). La NP 196 los provee en tabla de su §6.

---

## 9. Figuras generadas

| Figura | Archivo | Descripción |
|---|---|---|
| **Fig. 1.4** | `etapas/img/figura_1_4_rosa_de_vientos_cde.png` | Rosa de vientos anual CDE — ERA5/ECMWF 1991–2020 |
| **Fig. 1.5** | `etapas/img/figura_1_5_perfiles_velocidad_multinormativos.png` | Perfiles Vk(z) — NP 196 / NBR 6123 / ASCE 7-22 / EN 1991-1-4 |

Script generador: `05_RECURSOS/05.05_Scripts_Python/02_Ingenieria_Viento/ea5_vientos_dominantes_exposicion.py`

---

## 10. Referencias bibliográficas

- INTN, *NP 196:1991 — Acción del viento en las construcciones*, Asunción, PY, 1991.
- ABNT, *NBR 6123:2023 — Forças devidas ao vento*, Rio de Janeiro, BR, 2023. §6.2, Tabela 4.
- ASCE/SEI 7-22, *Minimum Design Loads*, Reston, VA, USA, 2022. §26.7, Table 26.10-1.
- CEN, *EN 1991-1-4:2010 — Wind actions*, Brussels, BE, 2010. §4.3, Tabla 4.1.
- A. Martínez et al., «Study of maximum wind speeds in Paraguay… NP-196», *CILAMCE-PANACM 2021*.
- W. Ibarra et al., «Dynamic Analysis of a Slender Building», *NewTech 2024 — ICCEIA 132*.
- DMH/DINAC, *Anuarios Estadísticos Climatológicos*, Asunción, PY. https://datos.gov.py
- WeatherSpark.com, *Climate CDE*, Cedar Lake Ventures, 2026. https://weatherspark.com/y/28524/
