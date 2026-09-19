"""
====================================================================
 SUBSUELO 3 (S3) — COCHERAS (Nivel más profundo, -10.50m)
 Edificio de Uso Mixto 18P + 3 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | GA de Distribución de Cocheras
====================================================================

 Bounding Box Edificio por Nivel (idéntico a PB):
   X: [2.5 → 87.5 m]   (Frente Urbano = 85.0 m)
   Y: [3.0 → 40.0 m]   (Profundidad Total = 37.0 m)

Programa Arquitectónico S3 (solo cocheras, el más profundo):
   - 98 plazas: 80 autos (2.5×5.0 m) + 18 motos (1.2×2.5 m)
   - Ubicadas manualmente en AutoCAD (DXF capa TESIS-COCHERAS)
     y extraídas con extraer_cocheras_dxf.py → STALLS_MANUALES.
   - Módulo cochera: 2.50 m (ancho) × 5.00 m (fondo) | Moto: 1.2×2.5 m
   - Pasillo circul.: 6.00 m entre filas enfrentadas

 2 NÚCLEOS H°A° GEMELOS ROTADOS 90° (continúan desde PB):
   N1 Oeste: X: 34.0→41.0 / Y: 17.0→26.0 (7m × 9m) — cara larga al Este
   N2 Este : X: 49.0→56.0 / Y: 17.0→26.0 (7m × 9m) — cara larga al Oeste
   Cada uno con puerta cortafuego hacia cocheras.

 Pasillo técnico central entre núcleos (X: 41.0→49.0 / Y: 17→26):
   - Ducto RSU Ø500mm + shafts de servicios (8m de ancho).

 DOBLE RAMPA ESQUINA-ESQUINA (todos los niveles, entrada+salida):
   - Rampa ENTRADA (bajada): Esquina SE X: 81.5→87.5 / Y: 3.0→10.0 (6m, 2 carriles)
   - Rampa SALIDA (subida): Esquina NO X: 2.5→8.5 / Y: 33.0→40.0 (6m, 2 carriles)
   - Circulación en diagonal SE→NO que recorre todo el subsuelo.
   - Cada rampa con giro interior de 90° en la esquina.

 GRILLA ESTRUCTURAL ÓPTIMA (alineada a núcleos, continua S3→Azotea):
   Ejes X: [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
            63.88, 71.75, 79.63, 87.50]
     → Alas: 4 vanos de 7.875m | N1: 7m | Pasillo: 8m | N2: 7m | Alas: 7.875m
   Ejes Y: [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]
     → Frente: 2 vanos de 7m | Núcleos: 9m | Fondo: 2 vanos de 7m
   Los 4 bordes de núcleos (X:34,41,49,56 / Y:17,26) son ejes exactos.

 Criterio de Distribución (determinista, no NSGA-II):
   El layout de cocheras es un empaquetado geométrico con módulo
   fijo y pasillo mínimo de 6.0m. La grilla de pilares y la posición
   de los núcleos ya fueron optimizadas (se mantienen fijas).

 OUTPUT: outputs/planta_subsuelo_3.png
====================================================================
"""

import os
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# BOUNDING BOX Y ELEMENTOS FIJOS
# ------------------------------------------------------------------
X_MIN, X_MAX = 2.5, 87.5
Y_MIN, Y_MAX = 3.0, 40.0

# 2 Núcleos gemelos H°A° rotados 90° (fijos, mismos que PB)
NUCLEOS = [
    dict(x0=34.0, x1=41.0, y0=17.0, y1=26.0, nombre="N1 OESTE"),
    dict(x0=49.0, x1=56.0, y0=17.0, y1=26.0, nombre="N2 ESTE"),
]

# Pasillo técnico entre núcleos (ducto RSU + servicios) — 8m
PASILLO_TECNICO = dict(x0=41.0, x1=49.0, y0=17.0, y1=26.0)

# DOBLE RAMPA ESQUINA-ESQUINA (todos los niveles): entrada SE + salida NO
# Circulación en diagonal que recorre todo el subsuelo (configuración clásica).
# Cada rampa de 6.0m (2 carriles) con giro interior de 90° en la esquina.
RAMPA_ENTRADA = dict(x0=81.5, x1=87.5, y0=3.0, y1=10.0)    # Esquina SE — bajada (desde nivel superior)
RAMPA_SALIDA  = dict(x0=2.5,  x1=8.5,  y0=33.0, y1=40.0)   # Esquina NO — subida (hacia nivel superior)

# GRILLA ESTRUCTURAL ÓPTIMA (12 ejes X, 6 ejes Y)
XS = [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00, 63.88, 71.75, 79.63, 87.50]
YS = [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

# ------------------------------------------------------------------
# MÓDULO DE COCHERA Y PASILLO (OBLIGATORIO)
# ------------------------------------------------------------------
STALL_W, STALL_D, AISLE_D = 2.5, 5.0, 6.0

# ------------------------------------------------------------------
# PILARES ESTRUCTURALES H°A° (grilla óptima — continúan S3→Azotea)
# TAMAÑO PARAMÉTRICO: se recalcula por nivel (ver sección 10.6 AGENTS.md).
# Orientativo S3 (carga axial ~11,300 kN): 90×90 cm.
# ------------------------------------------------------------------
ANCHO_PILAR = 0.90   # 90 cm (base S3/PB; se reduce en altura: 80→70→60)


def generar_pilares():
    """Genera los pilares en las intersecciones de la grilla óptima.

    Se crean en CADA intersección (xi, yi) de los ejes X e Y, excepto:
      - Los que caen DENTRO del área maciza de un Núcleo (se retiran:
        el núcleo es una pantalla que absorbe esos puntos).
      - Se MANTIENEN los pilares embebidos en los BORDES de los núcleos
        (perímetro de la pantalla) y en los bordes del pasillo técnico.
    Devuelve (lista de rectángulos (x0,y0,w,h), conteo).
    """
    pilares = []
    for x in XS:
        for y in YS:
            x0, y0 = x - ANCHO_PILAR / 2, y - ANCHO_PILAR / 2
            dentro_de_nucleo = False
            for c in NUCLEOS:
                if (c['x0'] + ANCHO_PILAR) < x < (c['x1'] - ANCHO_PILAR) and \
                   (c['y0'] + ANCHO_PILAR) < y < (c['y1'] - ANCHO_PILAR):
                    dentro_de_nucleo = True
                    break
            if dentro_de_nucleo:
                continue
            pilares.append((x0, y0, ANCHO_PILAR, ANCHO_PILAR))
    return pilares, len(pilares)

# ------------------------------------------------------------------
# ZONAS DE ESTACIONAMIENTO (excluyen Núcleos, pasillo técnico y DOBLE rampa esquina-esquina)
# ------------------------------------------------------------------
ZONAS_PARKING = [
    dict(x0=2.5,  x1=34.0, y0=3.0,  y1=17.8,  nombre="Ala Oeste Frente"),    # 31.5m × 14.8m
    dict(x0=2.5,  x1=34.0, y0=17.8, y1=25.2,  nombre="Ala Oeste Centro"),    # 31.5m × 7.4m
    dict(x0=8.5,  x1=34.0, y0=25.2, y1=40.0,  nombre="Ala Oeste Fondo"),     # 25.5m × 14.8m (excluye rampa NO)
    dict(x0=41.0, x1=49.0, y0=3.0,  y1=17.0,  nombre="Frente Central"),      # 8m × 14m
    dict(x0=41.0, x1=49.0, y0=26.0, y1=40.0,  nombre="Fondo Central"),       # 8m × 14m
    dict(x0=56.0, x1=81.5, y0=3.0,  y1=17.8,  nombre="Ala Este Frente"),     # 25.5m × 14.8m (excluye rampa SE)
    dict(x0=56.0, x1=87.5, y0=17.8, y1=25.2,  nombre="Ala Este Centro"),     # 31.5m × 7.4m
    dict(x0=56.0, x1=87.5, y0=25.2, y1=40.0,  nombre="Ala Este Fondo"),      # 31.5m × 14.8m
]

# ------------------------------------------------------------------
# COCHERAS UBICADAS MANUALMENTE EN AUTOCAD (DXF) — DEFINITIVAS
# Fuente: outputs/subsuelo_3_base_listo.dxf (capa TESIS-COCHERAS)
# Autos: 2.5×5.0 m | Motos: 1.2×2.5 m (intercaladas en filas centrales)
# ------------------------------------------------------------------
STALLS_MANUALES = [
    dict(x0=2.690, y0=3.000, w=2.500, h=5.000),
    dict(x0=5.190, y0=3.000, w=2.500, h=5.000),
    dict(x0=7.690, y0=3.000, w=2.500, h=5.000),
    dict(x0=10.560, y0=3.000, w=2.500, h=5.000),
    dict(x0=13.060, y0=3.000, w=2.500, h=5.000),
    dict(x0=15.560, y0=3.000, w=2.500, h=5.000),
    dict(x0=18.435, y0=3.000, w=2.500, h=5.000),
    dict(x0=20.935, y0=3.000, w=2.500, h=5.000),
    dict(x0=23.435, y0=3.000, w=2.500, h=5.000),
    dict(x0=26.310, y0=3.000, w=2.500, h=5.000),
    dict(x0=28.810, y0=3.000, w=2.500, h=5.000),
    dict(x0=31.310, y0=3.000, w=2.500, h=5.000),
    dict(x0=34.800, y0=3.000, w=2.500, h=5.000),
    dict(x0=37.700, y0=3.000, w=2.500, h=5.000),
    dict(x0=41.250, y0=3.000, w=2.500, h=5.000),
    dict(x0=43.750, y0=3.000, w=2.500, h=5.000),
    dict(x0=46.250, y0=3.000, w=2.500, h=5.000),
    dict(x0=49.800, y0=3.000, w=2.500, h=5.000),
    dict(x0=52.700, y0=3.000, w=2.500, h=5.000),
    dict(x0=56.190, y0=3.000, w=2.500, h=5.000),
    dict(x0=58.690, y0=3.000, w=2.500, h=5.000),
    dict(x0=61.190, y0=3.000, w=2.500, h=5.000),
    dict(x0=64.065, y0=3.000, w=2.500, h=5.000),
    dict(x0=66.565, y0=3.000, w=2.500, h=5.000),
    dict(x0=69.065, y0=3.000, w=2.500, h=5.000),
    dict(x0=71.940, y0=3.000, w=2.500, h=5.000),
    dict(x0=74.440, y0=3.000, w=2.500, h=5.000),
    dict(x0=76.940, y0=3.000, w=2.500, h=5.000),
    dict(x0=34.000, y0=15.800, w=2.500, h=1.200),
    dict(x0=36.700, y0=15.800, w=2.500, h=1.200),
    dict(x0=39.400, y0=15.800, w=2.500, h=1.200),
    dict(x0=48.100, y0=15.800, w=2.500, h=1.200),
    dict(x0=50.800, y0=15.800, w=2.500, h=1.200),
    dict(x0=53.500, y0=15.800, w=2.500, h=1.200),
    dict(x0=10.560, y0=16.300, w=2.500, h=5.000),
    dict(x0=13.060, y0=16.300, w=2.500, h=5.000),
    dict(x0=15.560, y0=16.300, w=2.500, h=5.000),
    dict(x0=18.435, y0=16.300, w=2.500, h=5.000),
    dict(x0=20.935, y0=16.300, w=2.500, h=5.000),
    dict(x0=23.435, y0=16.300, w=2.500, h=5.000),
    dict(x0=64.065, y0=16.300, w=2.500, h=5.000),
    dict(x0=66.565, y0=16.300, w=2.500, h=5.000),
    dict(x0=69.065, y0=16.300, w=2.500, h=5.000),
    dict(x0=71.940, y0=16.300, w=2.500, h=5.000),
    dict(x0=74.440, y0=16.300, w=2.500, h=5.000),
    dict(x0=76.940, y0=16.300, w=2.500, h=5.000),
    dict(x0=26.135, y0=17.550, w=1.200, h=2.500),
    dict(x0=62.665, y0=17.550, w=1.200, h=2.500),
    dict(x0=26.135, y0=20.250, w=1.200, h=2.500),
    dict(x0=62.665, y0=20.250, w=1.200, h=2.500),
    dict(x0=10.560, y0=21.700, w=2.500, h=5.000),
    dict(x0=13.060, y0=21.700, w=2.500, h=5.000),
    dict(x0=15.560, y0=21.700, w=2.500, h=5.000),
    dict(x0=18.435, y0=21.700, w=2.500, h=5.000),
    dict(x0=20.935, y0=21.700, w=2.500, h=5.000),
    dict(x0=23.435, y0=21.700, w=2.500, h=5.000),
    dict(x0=64.065, y0=21.700, w=2.500, h=5.000),
    dict(x0=66.565, y0=21.700, w=2.500, h=5.000),
    dict(x0=69.065, y0=21.700, w=2.500, h=5.000),
    dict(x0=71.940, y0=21.700, w=2.500, h=5.000),
    dict(x0=74.440, y0=21.700, w=2.500, h=5.000),
    dict(x0=76.940, y0=21.700, w=2.500, h=5.000),
    dict(x0=26.135, y0=22.950, w=1.200, h=2.500),
    dict(x0=62.665, y0=22.950, w=1.200, h=2.500),
    dict(x0=34.000, y0=26.000, w=2.500, h=1.200),
    dict(x0=36.700, y0=26.000, w=2.500, h=1.200),
    dict(x0=39.400, y0=26.000, w=2.500, h=1.200),
    dict(x0=48.100, y0=26.000, w=2.500, h=1.200),
    dict(x0=50.800, y0=26.000, w=2.500, h=1.200),
    dict(x0=53.500, y0=26.000, w=2.500, h=1.200),
    dict(x0=10.560, y0=35.000, w=2.500, h=5.000),
    dict(x0=13.060, y0=35.000, w=2.500, h=5.000),
    dict(x0=15.560, y0=35.000, w=2.500, h=5.000),
    dict(x0=18.435, y0=35.000, w=2.500, h=5.000),
    dict(x0=20.935, y0=35.000, w=2.500, h=5.000),
    dict(x0=23.435, y0=35.000, w=2.500, h=5.000),
    dict(x0=26.310, y0=35.000, w=2.500, h=5.000),
    dict(x0=28.810, y0=35.000, w=2.500, h=5.000),
    dict(x0=31.310, y0=35.000, w=2.500, h=5.000),
    dict(x0=34.800, y0=35.000, w=2.500, h=5.000),
    dict(x0=37.700, y0=35.000, w=2.500, h=5.000),
    dict(x0=41.250, y0=35.000, w=2.500, h=5.000),
    dict(x0=43.750, y0=35.000, w=2.500, h=5.000),
    dict(x0=46.250, y0=35.000, w=2.500, h=5.000),
    dict(x0=49.800, y0=35.000, w=2.500, h=5.000),
    dict(x0=52.700, y0=35.000, w=2.500, h=5.000),
    dict(x0=56.190, y0=35.000, w=2.500, h=5.000),
    dict(x0=58.690, y0=35.000, w=2.500, h=5.000),
    dict(x0=61.190, y0=35.000, w=2.500, h=5.000),
    dict(x0=64.065, y0=35.000, w=2.500, h=5.000),
    dict(x0=66.565, y0=35.000, w=2.500, h=5.000),
    dict(x0=69.065, y0=35.000, w=2.500, h=5.000),
    dict(x0=71.940, y0=35.000, w=2.500, h=5.000),
    dict(x0=74.440, y0=35.000, w=2.500, h=5.000),
    dict(x0=76.940, y0=35.000, w=2.500, h=5.000),
    dict(x0=79.820, y0=35.000, w=2.500, h=5.000),
    dict(x0=82.320, y0=35.000, w=2.500, h=5.000),
    dict(x0=84.820, y0=35.000, w=2.500, h=5.000),
]


def generar_stalls(zona):
    """Empaqueta filas de cocheras perpendiculares dentro de la zona.

    Estrategia: fila de cocheras (5.0m) + pasillo (6.0m) + fila (5.0m),
    apilando bahías de 16.0m en el eje Y. El excedente se usa para una
    fila adicional si queda al menos 5.0m.
    Devuelve (lista de rectángulos (x0,y0,w,h), conteo).
    """
    ancho = zona['x1'] - zona['x0']
    n_por_fila = int(ancho // STALL_W)
    if n_por_fila == 0:
        return [], 0

    stalls = []
    y_cursor = zona['y0']
    while True:
        restante = zona['y1'] - y_cursor
        if restante < STALL_D:
            break
        for i in range(n_por_fila):
            x0 = zona['x0'] + i * STALL_W
            stalls.append((x0, y_cursor, STALL_W, STALL_D))
        y_cursor += STALL_D
        restante = zona['y1'] - y_cursor
        if restante >= AISLE_D + STALL_D:
            y_cursor += AISLE_D
        else:
            break
    return stalls, len(stalls)


def generar():
    fig, ax = plt.subplots(figsize=(22, 12))
    fig.patch.set_facecolor('#f8fafc')
    ax.set_facecolor('#f1f5f9')

    # Huella
    ax.add_patch(plt.Rectangle((X_MIN, Y_MIN), X_MAX - X_MIN, Y_MAX - Y_MIN,
                               facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.5, zorder=2))

    # COCHERAS MANUALES (extraídas del DXF AutoCAD)
    total_autos = 0
    total_motos = 0
    for s in STALLS_MANUALES:
        es_moto = s['h'] < 3.0 or s['w'] < 1.8
        if es_moto:
            total_motos += 1
            col, edge = '#fde68a', '#b45309'
        else:
            total_autos += 1
            col, edge = '#bae6fd', '#0369a1'
        ax.add_patch(plt.Rectangle((s['x0'] + 0.05, s['y0'] + 0.05),
                                   s['w'] - 0.1, s['h'] - 0.1,
                                   facecolor=col, edgecolor=edge, lw=0.6, zorder=4))
    total_stalls = total_autos + total_motos
    for zona in ZONAS_PARKING:
        n = sum(1 for s in STALLS_MANUALES
                if zona['x0'] - 0.01 <= s['x0'] <= zona['x1'] + 0.01
                and zona['y0'] - 0.01 <= s['y0'] <= zona['y1'] + 0.01)
        cx = (zona['x0'] + zona['x1']) / 2
        cy = zona['y0'] - 1.0 if zona['y0'] > Y_MIN else zona['y1'] + 0.6
        ax.text(cx, cy, f"{n} plazas", fontsize=8, fontweight='bold',
                color='#0369a1', ha='center', va='center', zorder=6)

    # PILARES ESTRUCTURALES H°A° (grilla óptima, continúan desde cimentación)
    pilares, n_pilares = generar_pilares()
    for (x0, y0, w, h) in pilares:
        ax.add_patch(plt.Rectangle((x0, y0), w, h,
                                   facecolor='#f8fafc', edgecolor='#0f172a', lw=1.0, zorder=6))

    # DOBLE RAMPA ESQUINA-ESQUINA: entrada SE + salida NO (todos los niveles)
    rampas = [
        (RAMPA_ENTRADA, "RAMPA ENTRADA\n(bajada, giro 90°)"),
        (RAMPA_SALIDA,  "RAMPA SALIDA\n(subida, giro 90°)"),
    ]
    for rampa, etiqueta in rampas:
        ax.add_patch(plt.Rectangle((rampa['x0'], rampa['y0']),
                                   rampa['x1'] - rampa['x0'], rampa['y1'] - rampa['y0'],
                                   facecolor='#f97316', edgecolor='#c2410c', hatch='//', alpha=0.85, zorder=5))
        ax.text((rampa['x0'] + rampa['x1']) / 2, (rampa['y0'] + rampa['y1']) / 2,
                etiqueta, fontsize=7.5, fontweight='bold',
                color='white', ha='center', va='center', zorder=6)

    # Pasillo técnico entre núcleos (ducto RSU + servicios)
    ax.add_patch(plt.Rectangle((PASILLO_TECNICO['x0'], PASILLO_TECNICO['y0']),
                               PASILLO_TECNICO['x1'] - PASILLO_TECNICO['x0'],
                               PASILLO_TECNICO['y1'] - PASILLO_TECNICO['y0'],
                               facecolor='#a5b4fc', edgecolor='#4338ca', hatch='..', alpha=0.7, zorder=5))
    ax.text((PASILLO_TECNICO['x0'] + PASILLO_TECNICO['x1']) / 2,
            (PASILLO_TECNICO['y0'] + PASILLO_TECNICO['y1']) / 2,
            "PASILLO TÉCNICO\n(ducto RSU Ø500\n+ servicios)",
            fontsize=6.5, fontweight='bold', color='#312e81', ha='center', va='center', zorder=6)

    # 2 Núcleos H°A° rotados 90° (cara larga mirándose)
    for c in NUCLEOS:
        ax.add_patch(plt.Rectangle((c['x0'], c['y0']),
                                   c['x1'] - c['x0'], c['y1'] - c['y0'],
                                   facecolor='#334155', edgecolor='#0f172a', lw=2.5, zorder=7))
        ax.text((c['x0'] + c['x1']) / 2, (c['y0'] + c['y1']) / 2,
                f"NÚCLEO {c['nombre']}\n(continúa desde PB)\n2 asc + escalera RF",
                color='white', fontsize=7, fontweight='bold', ha='center', va='center', zorder=8)
        ax.scatter((c['x0'] + c['x1']) / 2, c['y0'],
                   marker='s', s=60, color='#22c55e', edgecolor='#166534', zorder=9)
        ax.text((c['x0'] + c['x1']) / 2, c['y0'] - 1.2,
                "Puerta cortafuego", fontsize=5.5, ha='center', color='#166534', fontweight='bold', zorder=9)

    # GRILLA ESTRUCTURAL — líneas de ejes
    for x in XS:
        ax.plot([x, x], [Y_MIN - 1.5, Y_MAX + 1.5], color='#64748b', lw=1.0, ls='--', zorder=1)
    for y in YS:
        ax.plot([X_MIN - 1.5, X_MAX + 1.5], [y, y], color='#64748b', lw=1.0, ls='--', zorder=1)

    # Bordes de núcleos como ejes estructurales (más marcados)
    for bx in [34.0, 41.0, 49.0, 56.0]:
        ax.plot([bx, bx], [Y_MIN - 1.5, Y_MAX + 1.5], color='#0f172a', lw=1.6, zorder=1.5)
    for by in [17.0, 26.0]:
        ax.plot([X_MIN - 1.5, X_MAX + 1.5], [by, by], color='#0f172a', lw=1.6, zorder=1.5)

    # Etiquetas de ejes (como plano estructural)
    for i, x in enumerate(XS):
        ax.text(x, Y_MIN - 1.9, f"{i+1}", fontsize=8, fontweight='bold', color='#0f172a',
                ha='center', va='top', zorder=12)
    for i, y in enumerate(YS):
        ax.text(X_MIN - 1.9, y, chr(65 + i), fontsize=8, fontweight='bold', color='#0f172a',
                ha='right', va='center', zorder=12)

    resumen = (
        "SUBSUELO 3 (S3) — NIVEL -10.50 m (solo cocheras):\n"
        "────────────────────────────────────────────────\n"
        f"• PLAZAS DE ESTACIONAMIENTO: {total_stalls} TOTAL ({total_autos} autos + {total_motos} motos)\n"
        f"• Ubicadas manualmente en AutoCAD (DXF capa TESIS-COCHERAS)\n"
        f"• PILARES H°A° en grilla (90x90 cm en S3, continuos S3→Azotea): {n_pilares}\n"
        f"• Módulo auto: {STALL_W}m x {STALL_D}m | Moto: 1.2m x 2.5m\n"
        "• 2 Núcleos H°A° gemelos rotados: N1 X:34→41 / N2 X:49→56 (Y:17→26)\n"
        "• Pasillo técnico central (X:41→49, 8m): ducto RSU Ø500mm + servicios\n"
        "• GRILLA ÓPTIMA: Ejes X alas 7.875m | núcleos 7m | pasillo 8m\n"
        "• Ejes Y: frente/fondo 7m | núcleos 9m (bordes en ejes exactos)\n"
        "• DOBLE RAMPA ESQUINA-ESQUINA (todos los niveles):\n"
        "• Entrada SE (X:81.5→87.5 / Y:3→10) | Salida NO (X:2.5→8.5 / Y:33→40)\n"
        "• Cada rampa: 6.0m (2 carriles) con giro interior de 90°\n"
        "• Altura de entrepiso: 3.50 m | Cota -10.50 m\n"
        "• S3: sin salas técnicas (quedan en S1)"
    )
    ax.text(X_MIN, Y_MIN - 5.5, resumen, fontsize=8.5, fontweight='bold', va='top',
            bbox=dict(boxstyle='round,pad=0.6', facecolor='white', edgecolor='#0284c7', lw=1.5), zorder=20)

    ax.set_xlim(X_MIN - 7, X_MAX + 4)
    ax.set_ylim(Y_MIN - 12, Y_MAX + 3)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title(f"SUBSUELO 3 (S3) — COCHERAS + PILARES Y GRILLA — {total_stalls} PLAZAS / {n_pilares} PILARES (90x90)",
              fontsize=13, fontweight='bold')

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "planta_subsuelo_3.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Plazas de estacionamiento S3: {total_stalls} ({total_autos} autos + {total_motos} motos)")
    print(f"Generado: {out_path}")
    return total_stalls


if __name__ == "__main__":
    generar()