"""
====================================================================
 PLANTA TIPO RESIDENCIAL — LAYOUT B: MUCHOS APARTAMENTOS GRANDES
 Pisos P03, P06, P09, P12, P15, P18 (6 pisos — incluye el ÚLTIMO piso) 
 Edificio 18P + 2 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650
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

 LAYOUT B — MUCHOS APARTAMENTOS GRANDES:
   • 8 unidades por banda (Sur + Norte) = 16 aptos/piso
   • Ancho por unidad ≈ 10.63 m (normalizado a 85m total)
   • Área: Sur 12.0m prof → ≈127.5 m² | Norte 11.5m prof → ≈122.2 m²
   • Tipología dominante: TIPO D (3 Dorm. Premium) — departamentos amplios
   • P18 es este layout SÍ O SÍ (último piso = apartamentos grandes)
   • Balcón corrido en toda la fachada (Sur y Norte) + esquinas con lateral

 OUTPUT: outputs/planta_tipo_layout_B.png
====================================================================
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _planta_tipo_common import normalizar, generar_plano_layout


def layout_b_anchos():
    """8 unidades por banda, anchos ~10.6m con leve variación alternada."""
    n = 8
    base = 85.0 / n
    w_sur = normalizar([base * (1 + 0.05 * ((-1) ** i)) for i in range(n)])
    w_nor = normalizar([base * (1 + 0.05 * ((-1) ** i)) for i in range(n)])
    return w_sur, w_nor


def main():
    print("=" * 72)
    print("  LAYOUT B — MUCHOS APARTAMENTOS GRANDES (16 aptos/piso)")
    print("=" * 72)
    w_sur, w_nor = layout_b_anchos()
    generar_plano_layout(
        "B",
        "MUCHOS APARTAMENTOS GRANDES",
        w_sur,
        w_nor,
        "planta_tipo_layout_B.png",
    )
    print("=" * 72)
    print("  Pisos con Layout B: P03, P06, P09, P12, P15, P18")
    print("  Total Layout B: 6 pisos × 16 = 96 apartamentos")
    print("  IMPORTANTE: P18 (ultimo piso) = apartamentos grandes OK")
    print("=" * 72)


if __name__ == "__main__":
    main()
