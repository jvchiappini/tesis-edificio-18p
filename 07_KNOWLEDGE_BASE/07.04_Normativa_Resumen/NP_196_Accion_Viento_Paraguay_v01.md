# NP 196:1991 — Acción del Viento en las Construcciones (Paraguay)

> Ficha de normativa del proyecto. Fuente única para citar la norma paraguaya de viento.
> Última actualización: 2026-09-15.

## 1. Identificación

| Dato | Valor |
|---|---|
| Denominación | **NP 196: Acción del viento en las construcciones** (también citada como «Fuerzas del viento en las construcciones») |
| Organismo | Instituto Nacional de Tecnología, Normalización y Metrología (**INTN**), Paraguay |
| Edición | 1.ª edición, Asunción, **1991** |
| Tipo | Norma Paraguaya (NP) |
| Uso en el proyecto | Norma local del cálculo de viento, comparada con NBR 6123:2023, ASCE 7-22 y Eurocódigo 1 (EN 1991-1-4) |

## 2. Método de cálculo (según fuentes públicas)

La NP 196 estima la acción del viento sobre las construcciones a partir de factores de corrección de la velocidad básica, con una estructura semejante a la de la NBR 6123 de Brasil:

- **S1** — factor topográfico (variaciones del relieve del terreno).
- **S2** — factor combinado de rugosidad del terreno y variación de la velocidad con la altura.
- La velocidad básica se obtiene de mapas de isopletas del territorio paraguayo.

> Dlubal Software publica un servicio en línea de «Velocidad básica del viento para Paraguay según NP 196:1991»: <https://www.dlubal.com/es/zonas-de-cargas-para-nieve-viento-y-sismos/viento-np-196.html>

## 3. Limitaciones verificadas (fuente: estudios FI-UNA)

De dos trabajos de acceso abierto de la Facultad de Ingeniería de la Universidad Nacional de Asunción (UNA) se desprenden las siguientes limitaciones, **citables** en la tesis:

1. **Solo eventos sinópticos.** La NP 196 considera únicamente vientos sinópticos y **no contempla los efectos de las tormentas convectivas (turbonadas / reventones)**, que en la región suelen alcanzar velocidades mayores que los eventos sinópticos. *(CILAMCE-PANACM 2021.)*
2. **Sin análisis dinámico.** La NP 196 reconoce los efectos del viento sobre **estructuras rígidas**, pero **carece de un método de diseño para el efecto dinámico** del viento en edificios esbeltos y flexibles, que son los más sensibles. *(ICCEIA 2024.)*

Estas dos limitaciones justifican complementar la norma local con las normas internacionales, que sí incorporan el efecto dinámico (factor de ráfaga, `cs·cd`, etc.).

## 4. Disponibilidad

- La norma **no es de descarga libre**: la comercializa el INTN (<https://intn.gov.py>).
- Existen copias subidas por usuarios en Scribd y Studocu, **con derechos de autor**; no se incorporan al proyecto.
- **Pendiente:** incorporar el PDF oficial (obtenerlo por el INTN o aportarlo por el estudiante) en esta carpeta como `NP_196_1991.pdf`.

## 5. Estudios de apoyo archivados (acceso abierto)

Ubicación: `00_GESTION_DE_PROYECTO/00.02_Normativa_y_Referencias/`

| Archivo | Contenido |
|---|---|
| `NP196_Estudio_Vientos_Maximos_Paraguay_CILAMCE2021.pdf` | Martínez, Marín, Aquino y Arévalos, «Study of the maximum wind speeds and meteorological characteristics in Paraguay… for a future update of the NP-196», CILAMCE-PANACM 2021. Clasifica eventos sinópticos y no sinópticos; concluye el predominio de eventos no sinópticos (tormentas) no contemplados por la NP 196. |
| `NP196_Analisis_Dinamico_Edificio_Esbelto_ICCEIA2024.pdf` | Ibarra, Arévalos, Silva, Quintana y Martínez-Pavetti, «Dynamic Analysis of a Slender Building Using Two Parallel Spectral Analysis Methods», NewTech 2024 (ICCEIA 132). Analiza el factor de respuesta a la ráfaga (Davenport y Galindez) ante la ausencia de método dinámico en la NP 196. |

## 6. Cómo citar (IEEE)

- [ ] Instituto Nacional de Tecnología, Normalización y Metrología, *Acción del viento en las construcciones*, Norma Paraguaya NP 196:1991, 1.ª ed., Asunción, Paraguay, 1991.

## 7. Implicancia para la tesis

La tesis **adopta la NP 196:1991 como norma local** del cálculo de viento y la compara con la NBR 6123:2023, el ASCE 7-22 y el Eurocódigo 1. La comparación permite: (i) mostrar la vigencia y las limitaciones de la norma nacional; (ii) identificar la norma más conservadora; y (iii) evaluar la necesidad de considerar el efecto dinámico que la NP 196 no cubre.
