"""
====================================================================
 PLANTA TIPO RESIDENCIAL — LAYOUT A: MUCHOS APARTAMENTOS PEQUEÑOS
 Pisos P01, P04, P07, P10, P13, P16 (6 pisos) | Edificio 18P + 3 Subsuelos
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

 LAYOUT A — MUCHOS APARTAMENTOS PEQUEÑOS:
   • 16 unidades por banda (Sur + Norte) = 32 aptos/piso
   • Ancho por unidad ≈ 5.31 m (normalizado a 85m total)
   • Área: Sur 12.0m prof → ≈63.7 m² | Norte 11.5m prof → ≈61.1 m²
   • Tipología dominante: TIPO A (Studio / 1 Dorm.) con algunos TIPO B
   • Balcón corrido en toda la fachada (Sur y Norte) + esquinas con lateral

 OUTPUT: outputs/planta_tipo_layout_A.png
====================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _planta_tipo_common import normalizar, generar_plano_layout


def layout_a_anchos():
    """16 unidades por banda, anchos ~5.3m con leve variación alternada."""
    n = 16
    base = 85.0 / n
    w_sur = normalizar([base * (1 + 0.03 * ((-1) ** i)) for i in range(n)])
    w_nor = normalizar([base * (1 + 0.03 * ((-1) ** i)) for i in range(n)])
    return w_sur, w_nor


def main():
    print("=" * 72)
    print("  LAYOUT A — MUCHOS APARTAMENTOS PEQUEÑOS (32 aptos/piso)")
    print("=" * 72)
    w_sur, w_nor = layout_a_anchos()
    generar_plano_layout(
        "A",
        "MUCHOS APARTAMENTOS PEQUEÑOS",
        w_sur,
        w_nor,
        "planta_tipo_layout_A.png",
    )
    print("=" * 72)
    print("  Pisos con Layout A: P01, P04, P07, P10, P13, P16")
    print("  Total Layout A: 6 pisos × 32 = 192 apartamentos")
    print("=" * 72)


if __name__ == "__main__":
    main()