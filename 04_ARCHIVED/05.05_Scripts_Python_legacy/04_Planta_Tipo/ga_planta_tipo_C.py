"""
====================================================================
 PLANTA TIPO RESIDENCIAL — LAYOUT C: COMBINADOS
 Pisos P02, P05, P08, P11, P14, P17 (6 pisos) | Edificio 18P + 3 Subsuelos
 Ciudad del Este, Paraguay | Metodología BIM ISO 19650
====================================================================

 Bounding Box: X [2.5→87.5] · Y [3.0→40.0] (85m × 37m)

 NÚCLEOS GEMELOS H°A° ROTADOS 90° (continúan desde PB/S1):
   N1 Oeste: X: 34.0→41.0 / Y: 17.0→26.0 (7m × 9m)
   N2 Este : X: 49.0→56.0 / Y: 17.0→26.0 (7m × 9m)
   Pasillo técnico central (ducto RSU Ø500): X: 41.0→49.0 / Y: 17→26

 Bandas (AGENTS.md §11.1):
   Balcón Sur Y:3→4.5 | Banda Sur Y:4.5→16.5 (12m) | Corredor Sur Y:16.5→18
   Central Y:18→25 | Corredor Norte Y:25→27 | Banda Norte Y:27→38.5 (11.5m)
   Balcón Norte Y:38.5→40
   Pozos de luz A X:5→19 / B X:71→85 · Y:18→25 (98 m² c/u)

 LAYOUT C — COMBINADOS (pequeños + medianos + grandes):
   • 12 unidades por banda (Sur + Norte) = 24 aptos/piso
   • Patrón de anchos: [5.0, 10.5, 7.0, 5.5, 9.0, 6.5] repetido (normalizado)
   • Áreas Sur (12m): ≈60 · 126 · 84 · 66 · 108 · 78 m²
   • Áreas Norte (11.5m): ≈57.5 · 120.8 · 80.5 · 63 · 103.5 · 74.8 m²
   • Tipologías: A (studio) + C (2 dorm suite) + D (3 dorm) — mezcla completa
   • Balcón corrido en toda la fachada (Sur y Norte) + esquinas con lateral

 OUTPUT: outputs/planta_tipo_layout_C.png
====================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _planta_tipo_common import normalizar, generar_plano_layout


def layout_c_anchos():
    """12 unidades por banda: patrón pequeño/grande/mediano repetido."""
    patron = [5.0, 10.5, 7.0, 5.5, 9.0, 6.5, 5.0, 10.5, 7.0, 5.5, 9.0, 6.5]
    w_sur = normalizar(patron)
    w_nor = normalizar(patron[::-1])
    return w_sur, w_nor


def main():
    print("=" * 72)
    print("  LAYOUT C — COMBINADOS (24 aptos/piso)")
    print("=" * 72)
    w_sur, w_nor = layout_c_anchos()
    generar_plano_layout(
        "C",
        "COMBINADOS (pequeños + medianos + grandes)",
        w_sur,
        w_nor,
        "planta_tipo_layout_C.png",
    )
    print("=" * 72)
    print("  Pisos con Layout C: P02, P05, P08, P11, P14, P17")
    print("  Total Layout C: 6 pisos × 24 = 144 apartamentos")
    print("=" * 72)


if __name__ == "__main__":
    main()