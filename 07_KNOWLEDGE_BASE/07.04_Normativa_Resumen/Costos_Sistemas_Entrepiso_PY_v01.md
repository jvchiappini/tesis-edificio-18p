# Comparativa de Costos de Sistemas de Entrepiso — Paraguay 2025/2026

> Versión v01 · 2026-09-10 · Base de conocimiento `07.04_Normativa_Resumen`
> Origen: análisis de mercado (CYPE, CAPACO, BCP, ABC Color) para el Capítulo de Estructuras de la tesis.

## 1. Contexto

Se comparan 5 sistemas estructurales de entrepiso para el edificio 18P+3SUB
(grilla 7,5 m, pilares en posición FIJA, núcleos N1/N2 comunes). Objetivo:
**elegir la estructura más barata** (no la más rápida). Implementado en
`06_Estructura/calculo/comparativa_estructuras.py`.

## 2. Precios unitarios verificados (fuentes citadas)

| Ítem | Valor | Unidad | Fuente |
|---|---|---|---|
| Hormigón HA-25/B/19/IIa bombeable en planta | 999.924 | Gs/m³ | CYPE Generador de Precios Paraguay (CHH030) |
| Hormigón HM-30 bombeable | 1.579.951 | Gs/m³ | CYPE Paraguay |
| Acero AP 500 **instalado** (corte, doblado, armado) | 8.242–8.554 | Gs/kg | CYPE Paraguay (CHA010/ENA010) |
| Acero varillas conformadas (solo material) | 10.450 | Gs/kg | CAPACO Listado julio-2025 |
| Losa maciza 24 cm + pilares (0,267 m³/m², 26 kg/m²) | 632.525 | Gs/m² | CYPE EHL020 |
| Losa unidireccional c/vigas (vigueta T-12 + bovedilla 60×20×25, canto 30=25+5, 0,143 m³/m², 11 kg/m²) | 350.546 | Gs/m² | CYPE EHU010 |
| Viga HA 40×60 (fck250, 150 kg/m³, con encofrado) | 2.785.362 | Gs/m³ | CYPE |
| Encofrado continuo de losa (recuperable) | ~100.000 | Gs/m² | derivado CYPE EHL020 |
| Postensado no adherido (suministro+instalación+tensado) | 12–14 | USD/m² | rango mercado; estudio comparativo Ecuador (torón 270 ksi instalado 5-6 USD/kg × ~3 kg/m²) |
| Tipo de cambio | 6.100 | Gs/USD | BCP referencial 09-06-2026 = 6.183,88; promedio 90 días ≈ 6.048 |

### Referencias
- CYPE Ingenieros — Generador de Precios de la Construcción, Paraguay:
  `https://paraguay.generadordeprecios.info/`
- CAPACO — Listado de Precios de Insumos, Asunción, 20/07/2025.
- BCP — Cotización referencial de monedas: `https://www.bcp.gov.py/webapps/web/cotizacion/monedas`
- ABC Color, "Evolución de la construcción…", 02/09/2026: costo m² PY vivienda
  estándar USD 500–800; edificios en altura > USD 1.000.
- Arias & Naranjo (2022, Quito, DOI 10.33386/593dp.2022.4-2.1084): losa
  postensada ~17% más barata que alivianada (ratios PT ~3 kg/m²).

## 3. Resultado del módulo (68.611 m² de losa, TC 6.100)

| # | Sistema | USD/m² | Total MMUSD | Ahorro vs A | Peso propio kN/m² |
|---|---|---|---|---|---|
| 1 | D) Losa nervurada/reticular | 68,8 | 4,72 | 7,0% | 4,7 |
| 2 | E) Vigueta+bovedilla (solo P01-P18) | 69,1 | 4,74 | 6,5% | 4,3 |
| 3 | A) Losa PT + vigas perimetrales (actual) | 73,9 | 5,07 | — | 5,4 |
| 4 | B) Losa plana armada | 93,3 | 6,40 | +26% | 6,6 |
| 5 | C) Losa + vigas interiores | 104,0 | 7,14 | +41% | 6,6 |

**Hallazgo:** el pórtico convencional (C) y la losa plana armada (B) son los
**más caros**; la nervurada (D) y las viguetas (E) los más baratos; la losa
postensada (A) queda en el medio (~7% más cara que D/E).

## 3b. Análisis de sensibilidad y decisión (2026-09-10)

Se varió el costo del postensado (10–16 USD/m²) y los materiales (±15%) en 11
escenarios (`outputs/comparativa_sensibilidad.csv` / `.png`):

- **La losa PT (A) NUNCA gana:** es superada por D entre +2% (mejor caso para
  PT: materiales +15%, PT 10 USD/m²) y +16% (peor caso).
- **D (nervurada) gana 8/11 escenarios**; E (viguetas) gana solo cuando el
  concreto es barato (−15%) o el acero/encofrado son caros (+15%).
- **DECISIÓN ADOPTADA:** sistema **D — losa nervurada/reticular alivianada**
  (canto 35 cm plantas tipo/azotea, 45 cm PB/subsuelos; nervios 10 cm c/60 cm,
  capa 10 cm; vigas de borde). Actualizado en AGENTS.md §10.0 y checklist 14.2 #9.
- `losas_postensadas.py` queda como referencia histórica; el diseño del nuevo
  sistema se desarrolla en `losas_nervuradas.py` (⏳).

## 4. Regla de oro
Antes de rehacer el análisis, revisar si los precios cambiaron:
- Repetir búsquedas en CYPE Paraguay y CAPACO.
- Actualizar el tipo de cambio BCP.
- Ajustar la sensibilidad de PT (12-18 USD/m²) si cambia el mercado.