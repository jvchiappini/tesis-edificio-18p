"""
===============================================================================
TESIS DE GRADO - INGENIERÍA CIVIL
MÓDULO: 01_Geometria_Terreno / generar_figuras_terreno.py
AUTOR: José Valentino Chiappini Vergara
DESCRIPCIÓN: Generador de figuras técnicas con datos reales (satelitales y vectoriales)
             usando Matplotlib, PIL y APIs de mapas para la tesis y visor web:
             - Figura 1.1: Ortomapa satelital real (Esri World Imagery) + Polígono UTM 21J
             - Figura 1.2: Plano técnico CAD de implantación (Terreno Irregular P1-P4 + Envolvente de Retiros + Cuña P1 + Nota Arquitectura a Definir en Etapa B)
             - Figura 1.3: Mapa de contexto urbano OpenStreetMap (OSM)
===============================================================================
"""

import os
import math
import io
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines
from PIL import Image

OUTPUT_DIRS = [
    os.path.join("etapas", "img"),
    os.path.join("06_ANEXOS_TESIS", "img")
]

for d in OUTPUT_DIRS:
    os.makedirs(d, exist_ok=True)

# Coordenadas UTM WGS84 Zona 21J (Ciudad del Este, Paraguay)
VERTICES_UTM = {
    "P1": (737721.76, 7176185.26),
    "P2": (737837.53, 7176203.96),
    "P3": (737853.36, 7176246.13),
    "P4": (737755.78, 7176281.93)
}

# Conversión UTM Zona 21S a Latitud/Longitud (WGS84)
def utm_to_latlon(easting, northing, zone=21, northern=False):
    a = 6378137.0
    f = 1 / 298.257223563
    b = a * (1 - f)
    e = math.sqrt(a**2 - b**2) / a
    e_prime_sq = (a**2 - b**2) / (b**2)
    k0 = 0.9996

    x = easting - 500000.0
    y = northing if northern else northing - 10000000.0
    lon0 = (zone - 1) * 6 - 180 + 3

    M = y / k0
    mu = M / (a * (1 - (e**2)/4 - 3*(e**4)/64 - 5*(e**6)/256))
    e1 = (1 - math.sqrt(1 - e**2)) / (1 + math.sqrt(1 - e**2))

    phi1 = mu + (3*e1/2 - 27*(e1**3)/32)*math.sin(2*mu) + (21*(e1**2)/16 - 55*(e1**4)/32)*math.sin(4*mu) + (151*(e1**3)/96)*math.sin(6*mu)
    N1 = a / math.sqrt(1 - (e*math.sin(phi1))**2)
    T1 = math.tan(phi1)**2
    C1 = e_prime_sq * (math.cos(phi1)**2)
    R1 = a * (1 - e**2) / ((1 - (e*math.sin(phi1))**2)**1.5)
    D = x / (N1 * k0)

    lat = phi1 - (N1 * math.tan(phi1) / R1) * (
        (D**2)/2 - (5 + 3*T1 + 10*C1 - 4*(C1**2) - 9*e_prime_sq)*(D**4)/24 +
        (61 + 90*T1 + 298*C1 + 45*(T1**2) - 252*e_prime_sq - 3*(C1**2))*(D**6)/720
    )
    lon = (
        D - (1 + 2*T1 + C1)*(D**3)/6 +
        (5 - 2*C1 + 28*T1 - 3*(C1**2) + 8*e_prime_sq + 24*(T1**2))*(D**5)/120
    ) / math.cos(phi1)

    return math.degrees(lat), lon0 + math.degrees(lon)

VERTICES_LATLON = {k: utm_to_latlon(v[0], v[1]) for k, v in VERTICES_UTM.items()}

def fetch_tile_mosaic(min_lat, max_lat, min_lon, max_lon, zoom=18, source='esri'):
    def latlon_to_xy(lat, lon, z):
        lat_rad = math.radians(lat)
        n = 2.0 ** z
        x = (lon + 180.0) / 360.0 * n
        y = (1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n
        return x, y

    def xy_to_latlon(x, y, z):
        n = 2.0 ** z
        lon = x / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
        return math.degrees(lat_rad), lon

    x0, y1 = latlon_to_xy(min_lat, min_lon, zoom)
    x1, y0 = latlon_to_xy(max_lat, max_lon, zoom)

    xtile_min, xtile_max = int(math.floor(x0)) - 1, int(math.floor(x1)) + 1
    ytile_min, ytile_max = int(math.floor(y0)) - 1, int(math.floor(y1)) + 1

    width_px = (xtile_max - xtile_min + 1) * 256
    height_px = (ytile_max - ytile_min + 1) * 256
    mosaic = Image.new('RGB', (width_px, height_px))

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) TesisCivilBot/1.0'}

    for i, tx in enumerate(range(xtile_min, xtile_max + 1)):
        for j, ty in enumerate(range(ytile_min, ytile_max + 1)):
            if source == 'esri':
                url = f'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{zoom}/{ty}/{tx}'
            elif source == 'carto_dark':
                url = f'https://a.basemaps.cartocdn.com/dark_all/{zoom}/{tx}/{ty}.png'
            else:
                url = f'https://tile.openstreetmap.org/{zoom}/{tx}/{ty}.png'

            try:
                r = requests.get(url, headers=headers, timeout=5)
                if r.status_code == 200:
                    tile = Image.open(io.BytesIO(r.content))
                    mosaic.paste(tile, (i * 256, j * 256))
            except Exception:
                pass

    top_lat, left_lon = xy_to_latlon(xtile_min, ytile_min, zoom)
    bottom_lat, right_lon = xy_to_latlon(xtile_max + 1, ytile_max + 1, zoom)

    return mosaic, (left_lon, right_lon, bottom_lat, top_lat)

# -----------------------------------------------------------------------------
# FIGURA 1.1: PLANIMETRÍA SATELITAL REAL Y POLÍGONO UTM
# -----------------------------------------------------------------------------
def generar_figura_1_1():
    print("Generando Figura 1.1: Planimetría Satelital Real + Polígono UTM...")

    lats = [v[0] for v in VERTICES_LATLON.values()]
    lons = [v[1] for v in VERTICES_LATLON.values()]

    margin = 0.0012
    min_lat, max_lat = min(lats) - margin, max(lats) + margin
    min_lon, max_lon = min(lons) - margin, max(lons) + margin

    mosaic_img, extent = fetch_tile_mosaic(min_lat, max_lat, min_lon, max_lon, zoom=18, source='esri')

    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.imshow(mosaic_img, extent=extent, aspect='equal')

    poly_lons = [VERTICES_LATLON[k][1] for k in ["P1", "P2", "P3", "P4", "P1"]]
    poly_lats = [VERTICES_LATLON[k][0] for k in ["P1", "P2", "P3", "P4", "P1"]]

    ax.plot(poly_lons, poly_lats, color='#00FFFF', linewidth=2.5, linestyle='-', label='Límite del Predio Irregular')
    ax.scatter([VERTICES_LATLON[k][1] for k in VERTICES_LATLON],
               [VERTICES_LATLON[k][0] for k in VERTICES_LATLON],
               color='#FFD700', edgecolor='black', s=80, zorder=5)

    nombres = ["P1", "P2", "P3", "P4"]
    offsets = [(-0.00035, -0.00020), (0.00010, -0.00015), (0.00010, 0.00010), (-0.00035, 0.00010)]
    for i, k in enumerate(nombres):
        lat, lon = VERTICES_LATLON[k]
        easting, northing = VERTICES_UTM[k]
        ox, oy = offsets[i]
        ax.annotate(
            f"{k}\nE: {easting:.2f}\nN: {northing:.2f}",
            xy=(lon, lat), xytext=(lon + ox, lat + oy),
            fontsize=9, fontweight='bold', color='white',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#111111', alpha=0.85, edgecolor='#00FFFF'),
            arrowprops=dict(arrowstyle='->', color='#00FFFF', lw=1.2)
        )

    mid_p12 = ((VERTICES_LATLON["P1"][1] + VERTICES_LATLON["P2"][1])/2, (VERTICES_LATLON["P1"][0] + VERTICES_LATLON["P2"][0])/2)
    mid_p23 = ((VERTICES_LATLON["P2"][1] + VERTICES_LATLON["P3"][1])/2, (VERTICES_LATLON["P2"][0] + VERTICES_LATLON["P3"][0])/2)
    mid_p34 = ((VERTICES_LATLON["P3"][1] + VERTICES_LATLON["P4"][1])/2, (VERTICES_LATLON["P3"][0] + VERTICES_LATLON["P4"][0])/2)
    mid_p41 = ((VERTICES_LATLON["P4"][1] + VERTICES_LATLON["P1"][1])/2, (VERTICES_LATLON["P4"][0] + VERTICES_LATLON["P1"][0])/2)

    ax.text(mid_p12[0], mid_p12[1] - 0.00015, "Calle Los Lapachos (Frente 117.27 m)", color='#00FF66', fontsize=10, fontweight='bold', ha='center', bbox=dict(facecolor='black', alpha=0.7, pad=2, edgecolor='none'))
    ax.text(mid_p23[0] + 0.00015, mid_p23[1], "Calle Los Sauces\n(45.04 m)", color='#00FF66', fontsize=9, fontweight='bold', ha='left', va='center', bbox=dict(facecolor='black', alpha=0.7, pad=2, edgecolor='none'))
    ax.text(mid_p34[0], mid_p34[1] + 0.00015, "Predio Vecino Privado (103.94 m)", color='#FF9999', fontsize=9, fontweight='bold', ha='center', bbox=dict(facecolor='black', alpha=0.7, pad=2, edgecolor='none'))
    ax.text(mid_p41[0] - 0.00015, mid_p41[1], "Av. Itaipú Oeste\n(102.48 m)", color='#00FF66', fontsize=9, fontweight='bold', ha='right', va='center', bbox=dict(facecolor='black', alpha=0.7, pad=2, edgecolor='none'))

    ax.annotate('N', xy=(extent[0] + 0.0002, extent[3] - 0.0003), xytext=(extent[0] + 0.0002, extent[3] - 0.0007),
                arrowprops=dict(facecolor='#FFD700', edgecolor='black', width=4, headwidth=12),
                ha='center', va='center', fontsize=14, fontweight='bold', color='#FFD700')

    info_text = (
        "TESIS DE GRADO - INGENIERÍA CIVIL (UNINTER / ISO 19650)\n"
        "FIGURA 1.1: PLANIMETRÍA CATASTRAL SOBRE ORTOMAPA SATELITAL REAL\n"
        "Polígono del Terreno: Cuadrilátero Irregular (7.618,49 m²)\n"
        "Ubicación: Ciudad del Este, Alto Paraná, Paraguay\n"
        "Sistema: UTM Zona 21J - Dátum WGS84 / SIRGAS2000\n"
        "Fuente: Teledetección Satelital (Esri World Imagery v7.3)\n"
        "Superficie Bruta: 7.618,49 m² | Perímetro: 368,74 m"
    )
    ax.text(0.02, 0.03, info_text, transform=ax.transAxes, fontsize=9, color='white',
            bbox=dict(boxstyle='square,pad=0.5', facecolor='#000000', alpha=0.85, edgecolor='#00FFFF'))

    ax.set_title("FIGURA 1.1 — PLANIMETRÍA CATASTRAL REAL DEL PREDIO IRREGULAR (7.618,49 m²)", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Longitud WGS84 (°)", fontsize=10)
    ax.set_ylabel("Latitud WGS84 (°)", fontsize=10)
    ax.grid(True, linestyle=':', color='white', alpha=0.4)

    for d in OUTPUT_DIRS:
        plt.savefig(os.path.join(d, "figura_1_1_planimetria_satelital_utm.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Figura 1.1 generada con éxito.")

# -----------------------------------------------------------------------------
# FIGURA 1.2: PLANO TÉCNICO CAD DEL TERRENO IRREGULAR Y ENVOLVENTE URBANÍSTICA
# -----------------------------------------------------------------------------
def generar_figura_1_2():
    print("Generando Figura 1.2: Plano Técnico CAD de Terreno Irregular y Envolvente...")

    p1 = (0.0, 0.0)
    p2 = (117.271, 0.0)
    p3 = (139.62, 39.11)
    p4 = (49.00, 90.01)

    fig, ax = plt.subplots(figsize=(15, 10), dpi=300)
    ax.set_facecolor('#F8F9FA')

    # 1. Dibujar Polígono Irregular del Terreno
    poly_x = [p1[0], p2[0], p3[0], p4[0], p1[0]]
    poly_y = [p1[1], p2[1], p3[1], p4[1], p1[1]]

    ax.plot(poly_x, poly_y, color='#1A252C', linewidth=3.2, linestyle='-', label='Límite de Propiedad Irregular (4 Lados Desiguales)')
    ax.fill(poly_x, poly_y, color='#E9ECEF', alpha=0.6)

    # Marcar Vértices
    ax.scatter([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]], color='#C0392B', s=100, zorder=5)

    # 2. Cuña No Edificable en P1 (61,44°)
    alpha_deg = 61.4365
    alpha_rad = math.radians(alpha_deg)
    u_cuña = 27.0
    h_cuña = u_cuña * math.tan(alpha_rad)

    cuña_x = [p1[0], u_cuña, u_cuña, p1[0]]
    cuña_y = [p1[0], 0.0, h_cuña, p1[0]]

    ax.fill(cuña_x, cuña_y, color='#2ECC71', alpha=0.4, label='Cuña / Jardín No Edificable en P1 (669,55 m²)')
    ax.plot(cuña_x, cuña_y, color='#27AE60', linewidth=2.0, linestyle='--')

    # 3. Envolvente Urbanística Máxima con Retiros (Líneas de Trazo de Seguridad)
    # Retiros: 3m frente (P1-P2), 3m fondo (P3-P4), 2m laterales (P2-P3, P4-P1)
    ax.plot([0, 117.27], [3.0, 3.0], color='#E67E22', linestyle=':', lw=2.0, label='Línea de Retiro Frontal (3.0 m)')

    # Área de Envolvente Edificable Indicativa
    env_x = [27.0, 115.0, 132.0, 45.0, 27.0]
    env_y = [3.0, 3.0, 35.0, 85.0, 3.0]
    ax.plot(env_x, env_y, color='#2980B9', linestyle='-.', lw=2.0, label='Envolvente Máxima de Edificación (Con Retiros)')
    ax.fill(env_x, env_y, color='#3498DB', alpha=0.15)

    # Cartel Indicativo Central: ARQUITECTURA A RE-DEFINIR EN ETAPA B
    arch_note = (
        "⏳ EN RE-DEFINICIÓN ARQUITECTÓNICA (ETAPA B)\n"
        "--------------------------------------------------\n"
        "La huella edificada, distribución espacial, grilla\n"
        "de pilares y núcleos H°A° serán calculados desde cero\n"
        "en la ETAPA B (Arquitectura Completa e Implantación)."
    )
    ax.text(75.0, 40.0, arch_note, ha='center', va='center', fontsize=10, fontweight='bold', color='#2C3E50',
            bbox=dict(boxstyle='square,pad=0.8', facecolor='#FFEAA7', edgecolor='#D63031', lw=2, alpha=0.95))

    # Cotas y Etiquetas de Vértices Irregulares
    ax.annotate('P1\nα₁ = 61.44°\n(Cuña Jardín)', xy=p1, xytext=(-12, -12),
                fontsize=9, fontweight='bold', color='#C0392B',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF', edgecolor='#C0392B'))

    ax.annotate('P2\nα₂ = 119.75°', xy=p2, xytext=(120, -12),
                fontsize=9, fontweight='bold', color='#C0392B',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF', edgecolor='#C0392B'))

    ax.annotate('P3\nα₃ = 89.57°', xy=p3, xytext=(142, 42),
                fontsize=9, fontweight='bold', color='#C0392B',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF', edgecolor='#C0392B'))

    ax.annotate('P4\nα₄ = 89.24°', xy=p4, xytext=(35, 94),
                fontsize=9, fontweight='bold', color='#C0392B',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF', edgecolor='#C0392B'))

    # Acotaciones de Lados
    ax.text(58.6, -6, 'Calle Los Lapachos (Frente Principal): 117.27 m', ha='center', fontsize=9.5, fontweight='bold', color='#2980B9')
    ax.text(133, 18, 'Calle Los Sauces\n45.04 m', ha='left', va='center', fontsize=9, fontweight='bold', color='#2980B9', rotation=60)
    ax.text(92, 68, 'Predio Vecino Privado (Fondo): 103.94 m', ha='center', fontsize=9, fontweight='bold', color='#C0392B', rotation=-18)
    ax.text(20, 45, 'Av. Itaipú Oeste\n102.48 m', ha='right', va='center', fontsize=9, fontweight='bold', color='#2980B9', rotation=61)

    # Caja de Indicadores Urbanísticos CDE
    urban_box = (
        "PARÁMETROS DEL TERRENO IRREGULAR Y MARCO URBANÍSTICO (ETAPA A.1)\n"
        "----------------------------------------------------------------------\n"
        "• Geometría del Lote: Cuadrilátero Irregular (7.618,49 m²)\n"
        "• Perímetro Total: 368,74 m (4 Lados Desiguales)\n"
        "• Lado P1-P2: 117,27m · Lado P2-P3: 45,04m\n"
        "• Lado P3-P4: 103,94m · Lado P4-P1: 102,48m\n"
        "----------------------------------------------------------------------\n"
        "• FOS Máximo (0.70): Área máxima de huella = 5.332,94 m²\n"
        "• FOT Máximo (4.0): Área total edificable sobre rasante = 30.473,96 m²\n"
        "• Subsuelos Exentos: Cocheras y Servicios sin permanencia humana\n"
        "• Retiros Obligatorios: Frente 3.0m / Fondo 3.0m / Laterales 2.0m\n"
        "----------------------------------------------------------------------\n"
        "• ESTADO DE ARQUITECTURA: En re-definición completa (Etapa B)"
    )
    ax.text(0.02, 0.97, urban_box, transform=ax.transAxes, fontsize=8.5, family='monospace', va='top',
            bbox=dict(boxstyle='square,pad=0.6', facecolor='#FFFFFF', edgecolor='#2C3E50', alpha=0.95))

    ax.set_title("FIGURA 1.2 — PLANO TÉCNICO CAD: PLANIMETRÍA DEL TERRENO IRREGULAR Y ENVOLVENTE MÁXIMA URBANÍSTICA", fontsize=12.0, fontweight='bold', pad=15)
    ax.set_xlabel("Eje U Local (m) — Alineamiento Calle Los Lapachos", fontsize=10)
    ax.set_ylabel("Eje V Local (m) — Perpendicular de Frente", fontsize=10)
    ax.legend(loc='lower right', fontsize=8.5, framealpha=0.9)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_aspect('equal')

    for d in OUTPUT_DIRS:
        plt.savefig(os.path.join(d, "figura_1_2_rectangulo_edificable_cuña.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Figura 1.2 generada con éxito.")

# -----------------------------------------------------------------------------
# FIGURA 1.3: MAPA REAL DE CONTEXTO URBANO OPENSTREETMAP (OSM)
# -----------------------------------------------------------------------------
def generar_figura_1_3():
    print("Generando Figura 1.3: Mapa Real de Contexto Urbano OpenStreetMap...")

    lats = [v[0] for v in VERTICES_LATLON.values()]
    lons = [v[1] for v in VERTICES_LATLON.values()]

    margin = 0.008
    min_lat, max_lat = min(lats) - margin, max(lats) + margin
    min_lon, max_lon = min(lons) - margin, max(lons) + margin

    mosaic_img, extent = fetch_tile_mosaic(min_lat, max_lat, min_lon, max_lon, zoom=16, source='osm')

    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.imshow(mosaic_img, extent=extent, aspect='equal')

    poly_lons = [VERTICES_LATLON[k][1] for k in ["P1", "P2", "P3", "P4", "P1"]]
    poly_lats = [VERTICES_LATLON[k][0] for k in ["P1", "P2", "P3", "P4", "P1"]]

    ax.fill(poly_lons, poly_lats, color='#E74C3C', alpha=0.6, label='Predio del Proyecto (7.618,49 m²)')
    ax.plot(poly_lons, poly_lats, color='#C0392B', linewidth=3)

    center_lon = sum(lons)/len(lons)
    center_lat = sum(lats)/len(lats)

    ax.annotate(
        "EDIFICIO 18P + 3S\n(CIUDAD DEL ESTE)\n[Arquitectura a definir en Etapa B]",
        xy=(center_lon, center_lat), xytext=(center_lon + 0.002, center_lat + 0.002),
        fontsize=10, fontweight='bold', color='white',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#C0392B', alpha=0.9, edgecolor='white'),
        arrowprops=dict(arrowstyle='->', color='#C0392B', lw=2)
    )

    ax.set_title("FIGURA 1.3 — MAPA DE CONTEXTO URBANO EN CIUDAD DEL ESTE (OPENSTREETMAP REAL)", fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel("Longitud WGS84 (°)", fontsize=10)
    ax.set_ylabel("Latitud WGS84 (°)", fontsize=10)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)
    ax.grid(True, linestyle=':', color='gray', alpha=0.5)

    for d in OUTPUT_DIRS:
        plt.savefig(os.path.join(d, "figura_1_3_mapa_contexto_osm.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("[OK] Figura 1.3 generada con éxito.")

if __name__ == "__main__":
    generar_figura_1_1()
    generar_figura_1_2()
    generar_figura_1_3()
    print("=" * 80)
    print("TODAS LAS FIGURAS TÉCNICAS CON DATOS REALES FUERON GENERADAS CORRECTAMENTE.")
    print("=" * 80)
