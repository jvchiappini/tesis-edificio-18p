# Diseño de Losa Nervada / Reticular Alivianada — ACI 318-19 y NBR 6118:2014

**Fuente:** búsquedas web verificadas 2026-09-10 + módulo `losas_nervadas.py` (validado vs PyNite).
**Terminología obligatoria:** **"losa nervada"** (no "nervurada"); equivalencias: *reticular alivianada*
(2 direcciones) / *alivianada-aligerada* (1 dirección). Nervios = "nervaduras" o "nervios".

## 1. Límites dimensionales (verificados)

### ACI 318-19 (§8.8 two-way joist / §9.8 one-way joist)
| Requisito | Límite |
|---|---|
| Ancho de nervio `b_w` | ≥ 4 in (101,6 mm) |
| Peralte de nervio | ≤ 3,5 × `b_w` |
| Claro libre entre nervios | ≤ 30 in (762 mm) |
| Capa de compresión (casetones recuperables) | ≥ max(2 in = 50,8 mm; claro/12) |
| Corte del hormigón en nervios | +10 % permitido (§8.8.1.5 / §9.8.1.5) |

### ABNT NBR 6118:2014 (§13.2.4.1 lajes nervuradas)
| Requisito | Límite |
|---|---|
| Espesor de nervio | ≥ 5 cm |
| Capa de compresión | ≥ max(4 cm; claro/15) |
| Ejes de nervios ≤ 65 cm | se dispensa verificación de flexión de la mesa; corte como losa |
| Ejes 65–110 cm | verificar flexión de mesa; corte como viga (como losa si ≤ 90 cm y ancho medio > 12 cm) |
| Ejes > 110 cm | mesa como losa maciza sobre grilla |
| Nervio < 8 cm | no usar armadura de compresión |

## 2. Geometría adoptada en el edificio (validada ✅)
- Canto `h`: 35 cm (P01–P18 y azotea), 45 cm (PB y subsuelos)
- Capa de compresión: 10 cm · Nervios: 10 cm × cada 60 cm (ejes) · claro libre 50 cm
- Peso propio (espesor equivalente 0,19 m × 25 kN/m³) = **4,75 kN/m²** (tipo)

## 3. Verificación cruzada con programa
- Instalar SIEMPRE `PyNiteFEA` (import `from Pynite import FEModel3D`). El paquete PyPI `pynite`
  es un wrapper de la API de Fortnite (impostor) → colisión de nombres `pynite` en site-packages.
- Modelo: franja de 0,60 m como viga continua de 2 vanos (L = 7,875 m), apoyos simples,
  sección T (I_g), cargas ELU/ELS. Apoyos: fijar DX/DY/DZ/RX/RY, liberar RZ.
  `add_section(name, A, Iy, Iz, J)` → ¡el orden es A, Iy, Iz, J!
  `add_member_dist_load(member, 'FY', w1, w2, case=...)` → dirección como 'FY'.
- Resultados manual vs PyNite (losas_nervadas_compare.csv): M⁻ 60,23 = 60,23 kN·m · M⁺ 33,88 = 33,88 ·
  Vmax 38,24 = 38,24 · flecha 6,21 vs 6,23 mm (diferencia < 0,5 %).
- Vmax en viga continua 2 vanos = 5wL/8 (no wL/2).

## 4. Dónde queda documentado
- Módulo: `05_RECURSOS/05.05_Scripts_Python/06_Estructura/calculo/losas_nervadas.py`
- Outputs: `calculo/outputs/losas_nervadas_resultados.json` + `losas_nervadas_compare.csv`
- Anexo LaTeX: `06_ANEXOS_TESIS/06.01_Capitulos_Documento_Escrito/anexo_calculo_latex/` (main.pdf)

## 5. Diseño panel por panel (módulo `losas_nervadas_paneles.py`)
Enumeración de TODOS los paneles de la grilla (12 ejes X × 6 ejes Y = **55 celdas por piso**) para S1, S2, S3, PB, P01–P18 y AZ (23 niveles → **1.265 paneles**).

- **Clasificación de cada borde (punto medio)**: `S`=spandrel (viga perimetral 25×50), `N`=núcleo H°A° (muro), `P`=hueco (viga de borde de pozo 20×40), `C`=continuo (losa hacia el panel vecino). Orden del código: W, E, S, N.
- **Huecos por nivel**: núcleos N1/N2 (siempre); pozos A/B (P01–P18 y AZ); **vacío central X:41→49/Y:17→26 en P01–P18** (decisión 2026-09-11: hueco real entre los núcleos).
- **Tipos**: NORMAL · ANILLO (panel con hueco interior) · VACIO (sin losa) · NUCLEO (ocupado por muro).
- **Cargas por zona**: residencial 2,0 · cocheras 3,0 · comercial 3,0 · azotea 2,0 kN/m² (+ acabados 1,0 + tabiquería 1,5 residencial / 1,0 otros).
- **Diseño**: reparto bidireccional `qx+qy=q` con `qx=q·Ly⁴/(Lx⁴+Ly⁴)`; franja de un módulo (0,60 m) como viga continua de 2 vanos (coeficientes conservadores `M⁻=wL²/8`, `M⁺=9wL²/128`); As por nervio en ambas direcciones; corte `V=5wL/8`; estribos si `Vu>φVc`.
- **Outputs**: `paneles_losas.csv` (panel por panel) + `mapa_paneles_planta_tipo.png` + `paneles_losas_resultados.json`.
- **Verificación 2026-09-11** (banda de núcleos P18): N1 y N2 = NUCLEO; celda X:41→49 = VACIO con bordes NNPP; celdas vecinas con borde N hacia núcleo; pozos A/B = ANILLO. Correcto.
- **Pendiente (v2)**: diseño exacto del anillo alrededor de huecos (franjas perimetrales) y verificación por emparrillado (PyNite/CYPE) por panel.