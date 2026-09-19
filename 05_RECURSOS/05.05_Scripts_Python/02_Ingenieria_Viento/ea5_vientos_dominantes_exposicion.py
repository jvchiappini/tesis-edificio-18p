#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
TESIS-EST-GEN-SCRIPT-002 - eA-5: Vientos Dominantes y Clasificacion de Exposicion
================================================================================
Proyecto  : Tesis de Grado - Edificio Mixto 18P+3S - Ciudad del Este, Paraguay
Etapa     : A - Sub-etapa A.2 - Tarea eA-5
Autor     : Jose Valentino Chiappini Vergara
Fecha     : 2026-09-19
Normativa : NP 196:1991 (INTN) - ABNT NBR 6123:2023 - ASCE 7-22 SS26 - EN 1991-1-4:2010

Descripcion:
    Este script genera las Figuras 1.4 y 1.5 del capitulo de Analisis de Sitio:
      - Figura 1.4: Rosa de Vientos estadistica anual de Ciudad del Este (Paraguay)
                    basada en datos modelos climatologicos (fuente: WeatherSpark /
                    ERA5/ECMWF 1991-2020), representando la distribucion direccional
                    de frecuencias de viento.
      - Figura 1.5: Perfiles comparativos de velocidad de viento con la altura
                    segun NP 196:1991, NBR 6123:2023, ASCE 7-22 y EN 1991-1-4,
                    para la categoria de exposicion urbana correspondiente al
                    entorno de Ciudad del Este.

Archivos de salida:
    etapas/img/figura_1_4_rosa_de_vientos_cde.png
    etapas/img/figura_1_5_perfiles_velocidad_multinormativos.png

NOTA ACADEMICA:
    Los datos de frecuencia direccional adoptados corresponden a estadisticas
    climatologicas modeladas (ERA5 / reanalis ECMWF) para lat=-25.50, lon=-54.62
    (Ciudad del Este). La fuente oficial primaria para datos instrumentales es la
    DMH/DINAC (estacion meteorologica CDE / Aeropuerto Internacional Guarani).
    Para la tesis, se declaran como "hipotesis de anteproyecto".

================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path

# Ruta de salida - hardcoded para maxima robustez
OUTPUT_DIR = Path(r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\etapas\img")

# --- Paleta de colores FONDO CLARO (tema academico para impresion) -----------
COLOR_BG      = "#FFFFFF"   # Fondo blanco puro
COLOR_PANEL   = "#F5F7FA"   # Gris muy claro para paneles
COLOR_GRID    = "#D1D9E6"   # Gris medio para grillas y bordes
COLOR_ACCENT1 = "#1A56A0"   # Azul oscuro principal (legible en blanco)
COLOR_ACCENT4 = "#B45309"   # Naranja oscuro (contraste en blanco)
COLOR_TEXT    = "#1A202C"   # Texto principal casi negro
COLOR_SUBTEXT = "#4A5568"   # Texto secundario gris oscuro
COLOR_NP196   = "#1A56A0"   # Azul oscuro - NP 196
COLOR_NBR6123 = "#166534"   # Verde oscuro - NBR 6123
COLOR_ASCE722 = "#9B1C1C"   # Rojo oscuro - ASCE 7-22
COLOR_EC1     = "#92400E"   # Naranja/marron oscuro - EC1

plt.rcParams.update({
    "figure.facecolor": COLOR_BG,
    "axes.facecolor":   COLOR_PANEL,
    "axes.edgecolor":   COLOR_GRID,
    "axes.labelcolor":  COLOR_TEXT,
    "xtick.color":      COLOR_TEXT,
    "ytick.color":      COLOR_TEXT,
    "text.color":       COLOR_TEXT,
    "grid.color":       COLOR_GRID,
    "grid.linewidth":   0.6,
    "font.family":      "DejaVu Sans",
})

# =============================================================================
# DATOS CLIMATOLOGICOS - FRECUENCIA DIRECCIONAL DE VIENTOS
# Ciudad del Este, Paraguay (lat=-25.50, lon=-54.62, alt~230 m s.n.m.)
# Fuente: WeatherSpark / ERA5/ECMWF reanalis 1991-2020 (hipotesis de tesis)
# Patron dominante: Vientos del E (max ~39% en agosto) y N (verano dic-feb)
# Referencia: WeatherSpark.com (2026) - https://weatherspark.com/y/28524/
# =============================================================================

DIRECTIONS_16 = [
    "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
    "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"
]

# Frecuencia anual (%) por sector - estimacion modelada ERA5/ECMWF
# Distribucion: predominio E (feb-dic, ~20.5% anual integrado), N (dic-feb)
FREQ_ANUAL = np.array([
    8.5,   # N
    6.0,   # NNE
    5.5,   # NE
    5.5,   # ENE
    20.5,  # E    <- sector dominante anual
    9.5,   # ESE
    6.0,   # SE
    4.5,   # SSE
    6.5,   # S    <- ingresos de frentes frios del S (pampero)
    4.5,   # SSO
    4.0,   # SO
    3.0,   # OSO
    3.5,   # O
    3.0,   # ONO
    4.0,   # NO
    5.5,   # NNO
])

# Velocidad media por sector (km/h) - hipotesis de tesis
VEL_MEDIA_KMH = np.array([
    10.5, 9.5, 9.0, 9.5, 11.0, 10.0, 9.5, 9.0,
    10.0, 9.5, 9.0, 8.5,  8.5,  8.5, 9.0, 9.5
])

# Parametros del edificio y velocidad basica
V0_MS = 45.0   # Velocidad basica de referencia (m/s) - NP 196:1991, Ciudad del Este
H_MAX = 80.0   # Altura de analisis (m) - conservador para 18 pisos (~64 m + azotea)
z = np.linspace(1, H_MAX, 500)


# =============================================================================
# FUNCIONES DE PERFIL DE VELOCIDAD POR NORMA
# =============================================================================

def perfil_np196_cat_iii(z_arr, V0):
    """
    NP 196:1991 - Factor S2 - Categoria III - Clase B (edificio 20-50 m).
    Vk(z) = V0 * S2(z)
    S2(z) = b * (z/10)^p  para z >= z_min
    Categoria III: b=0.85, p=0.175 (Tabla 2 NP 196:1991)
    Ref: Ibarra et al., NewTech 2024 (ICCEIA 132) - parametros publicados FI-UNA.
    NOTA: En ausencia del PDF oficial NP 196, parametros verificados con
    estudios de la Facultad de Ingenieria, Universidad Nacional de Asuncion.
    """
    b, p, z_min = 0.85, 0.175, 5.0
    z_eff = np.maximum(z_arr, z_min)
    return V0 * b * (z_eff / 10.0) ** p


def perfil_nbr6123_cat_iv(z_arr, V0):
    """
    ABNT NBR 6123:2023 - Categoria IV - Classe B (maior dimensao 20-50 m).
    Vk(z) = V0 * S1 * S2 * S3 = V0 * 1.0 * S2(z) * 1.0
    S2(z) = b_m * Fr * (z/10)^p
    Categoria IV: b_m=0.86, p=0.20, Fr=1.00 (Classe B)
    Ref.: ABNT NBR 6123:2023 Tabela 4.
    """
    b_m, p, Fr, z_min = 0.86, 0.20, 1.00, 10.0
    z_eff = np.maximum(z_arr, z_min)
    return V0 * b_m * Fr * (z_eff / 10.0) ** p


def perfil_asce722_exp_b(z_arr, V0):
    """
    ASCE 7-22 SS26.10.1 - Exposure B.
    Kz = 2.01 * (z/z_g)^(2/alpha)  con z_g=365.76 m, alpha=7.0
    V(z) = V0 * sqrt(Kz)
    Exposure B: alpha=7.0, z_g=365.76 m (1200 ft), z_min=4.572 m (15 ft).
    NOTA: ASCE 7-22 usa velocidades de rafaga de 3 s. V0=45 m/s (NP 196) es
    velocidad media 10 min. Para la comparacion cualitativa se mantiene V0 como base.
    Ref.: ASCE 7-22 Table 26.10-1.
    """
    alpha, z_g, z_ref_min = 7.0, 365.76, 4.572
    z_eff = np.minimum(np.maximum(z_arr, z_ref_min), z_g)
    Kz = 2.01 * (z_eff / z_g) ** (2.0 / alpha)
    return V0 * np.sqrt(Kz)


def perfil_ec1_cat_iii(z_arr, V0):
    """
    EN 1991-1-4:2010 SS4.3 - Terrain Category III.
    v_m(z) = c_r(z) * c_o(z) * v_b
    c_r(z) = k_r * ln(z / z0)   para z_min <= z <= 200 m
    k_r = 0.19 * (z0 / 0.05)^0.07
    Cat. III: z0=0.30 m, z_min=5 m.
    c_o = 1.0 (terreno plano, CDE sin efecto orografico relevante).
    Ref.: EN 1991-1-4:2010 Tabla 4.1.
    """
    z0, z_min, z0_II = 0.30, 5.0, 0.05
    k_r = 0.19 * (z0 / z0_II) ** 0.07
    z_eff = np.maximum(z_arr, z_min)
    c_r = k_r * np.log(z_eff / z0)
    return V0 * c_r * 1.0  # c_o = 1.0


# =============================================================================
# FIGURA 1.4 - ROSA DE VIENTOS ANUAL - CIUDAD DEL ESTE, PARAGUAY
# =============================================================================

def generar_rosa_de_vientos():
    """Genera la rosa de vientos estilizada de Ciudad del Este."""
    fig = plt.figure(figsize=(14, 11), facecolor=COLOR_BG)
    fig.suptitle(
        "ROSA DE VIENTOS ANUAL - CIUDAD DEL ESTE, PARAGUAY",
        fontsize=16, fontweight="bold", color=COLOR_ACCENT1, y=0.97
    )
    fig.text(
        0.5, 0.935,
        "Distribucion de frecuencia direccional anual (ERA5/ECMWF 1991-2020)  |  "
        "Hipotesis de tesis - Fuente primaria: DMH/DINAC Paraguay",
        ha="center", fontsize=9, color=COLOR_SUBTEXT
    )

    ax = fig.add_axes([0.12, 0.08, 0.76, 0.82], polar=True)
    ax.set_facecolor(COLOR_PANEL)

    N = len(DIRECTIONS_16)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)  # Sentido horario (N->E->S->O)
    width = (2 * np.pi / N) * 0.88

    vel_norm = (VEL_MEDIA_KMH - VEL_MEDIA_KMH.min()) / (VEL_MEDIA_KMH.max() - VEL_MEDIA_KMH.min())
    cmap_wind = LinearSegmentedColormap.from_list(
        "wind_cmap",
        ["#BFD7ED", "#6BAED6", "#2171B5", "#D94801", "#7F2704"],
        N=256
    )
    colors = [cmap_wind(v) for v in vel_norm]

    ax.bar(
        angles, FREQ_ANUAL,
        width=width, bottom=0.5,
        color=colors, alpha=0.90,
        edgecolor=COLOR_BG, linewidth=0.8, zorder=3
    )

    max_freq = max(FREQ_ANUAL)
    ax.set_rgrids(
        [5, 10, 15, 20],
        labels=["5%", "10%", "15%", "20%"],
        angle=22.5, fontsize=7.5, color=COLOR_SUBTEXT
    )
    ax.set_xticks(angles)
    ax.set_xticklabels(DIRECTIONS_16, fontsize=9.5, fontweight="bold", color=COLOR_TEXT)
    ax.set_ylim(0, max_freq + 3.5)
    ax.set_yticks([5, 10, 15, 20])
    ax.set_yticklabels(["5%", "10%", "15%", "20%"], fontsize=7.5, color=COLOR_SUBTEXT)
    ax.tick_params(axis="y", labelcolor=COLOR_SUBTEXT)
    ax.grid(color=COLOR_GRID, linestyle="--", linewidth=0.8, alpha=0.9)
    ax.spines["polar"].set_edgecolor("#555555")

    # Anotacion sector E dominante
    idx_E = DIRECTIONS_16.index("E")
    ax.annotate(
        f"  Dominante E\n  {FREQ_ANUAL[idx_E]:.1f}%",
        xy=(angles[idx_E], FREQ_ANUAL[idx_E] + 0.5),
        xytext=(angles[idx_E], FREQ_ANUAL[idx_E] + 5.5),
        fontsize=8, color=COLOR_ACCENT1, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=COLOR_ACCENT1, lw=1.2),
        ha="center"
    )
    # Anotacion sector N secundario
    idx_N = DIRECTIONS_16.index("N")
    ax.annotate(
        f"N: {FREQ_ANUAL[idx_N]:.1f}%\n(verano)",
        xy=(angles[idx_N], FREQ_ANUAL[idx_N] + 0.5),
        xytext=(angles[idx_N], FREQ_ANUAL[idx_N] + 7.0),
        fontsize=8, color=COLOR_ACCENT4, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=COLOR_ACCENT4, lw=1.2),
        ha="center"
    )

    # Colorbar
    sm = plt.cm.ScalarMappable(
        cmap=cmap_wind,
        norm=plt.Normalize(vmin=VEL_MEDIA_KMH.min(), vmax=VEL_MEDIA_KMH.max())
    )
    sm.set_array([])
    cax = fig.add_axes([0.91, 0.25, 0.018, 0.45])
    cb = fig.colorbar(sm, cax=cax)
    cb.set_label("Velocidad media\npor sector (km/h)", color=COLOR_TEXT, fontsize=8)
    plt.setp(cb.ax.yaxis.get_ticklabels(), color=COLOR_SUBTEXT, fontsize=7.5)

    # Cuadro de datos tecnicos
    info_text = (
        "DATOS TECNICOS\n"
        "--------------------------\n"
        "Ubicacion: Ciudad del Este, PY\n"
        "Lat: 25deg30'S  |  Lon: 54deg37'W\n"
        "Altitud: ~230 m s.n.m.\n"
        "Periodo: 1991-2020 (ERA5)\n"
        "V0 = 45 m/s  (NP 196:1991)\n"
        "Vel. media anual: ~10,0 km/h\n"
        "--------------------------\n"
        "Sector dominante: E (anual)\n"
        "Sector sec. N: dic-feb\n"
        "Frente frio del S: may-ago"
    )
    fig.text(
        0.015, 0.30, info_text,
        fontsize=7.5, color=COLOR_SUBTEXT,
        va="center", ha="left",
        bbox=dict(
            boxstyle="round,pad=0.5",
            facecolor=COLOR_GRID,
            edgecolor=COLOR_ACCENT1,
            alpha=0.85,
            linewidth=1.2
        )
    )

    fig.text(
        0.5, 0.01,
        "Figura 1.4  |  TESIS-EST-GEN-SCRIPT-002  |  eA-5 - Analisis de Vientos Dominantes  |  "
        "Fuente: ERA5/ECMWF reanalis (hipotesis de tesis). Verificar con DMH/DINAC.",
        ha="center", fontsize=7, color=COLOR_SUBTEXT, style="italic"
    )

    out_path = OUTPUT_DIR / "figura_1_4_rosa_de_vientos_cde.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight", facecolor=COLOR_BG)
    plt.close(fig)
    print(f"[OK] Figura 1.4 guardada: {out_path}")
    return out_path


# =============================================================================
# FIGURA 1.5 - PERFILES DE VELOCIDAD CON LA ALTURA - COMPARATIVA MULTINORMATIVA
# =============================================================================

def generar_perfiles_velocidad():
    """Genera la figura comparativa de perfiles de velocidad con la altura."""
    fig, axes = plt.subplots(1, 2, figsize=(16, 10), facecolor=COLOR_BG)
    fig.suptitle(
        "PERFILES COMPARATIVOS DE VELOCIDAD DE VIENTO CON LA ALTURA\n"
        "Clasificacion de Exposicion - Ciudad del Este, Paraguay",
        fontsize=14, fontweight="bold", color=COLOR_ACCENT1, y=0.98
    )

    # --- Panel izquierdo: Perfiles de velocidad --------------------------------
    ax1 = axes[0]
    ax1.set_facecolor(COLOR_PANEL)

    Vk_NP196 = perfil_np196_cat_iii(z, V0_MS)
    Vk_NBR   = perfil_nbr6123_cat_iv(z, V0_MS)
    Vk_ASCE  = perfil_asce722_exp_b(z, V0_MS)
    Vk_EC1   = perfil_ec1_cat_iii(z, V0_MS)

    ax1.plot(Vk_NP196, z, color=COLOR_NP196,  lw=2.5, label="NP 196:1991 - Cat. III, Clase B")
    ax1.plot(Vk_NBR,   z, color=COLOR_NBR6123, lw=2.5, label="NBR 6123:2023 - Cat. IV, Clase B",
             linestyle="--")
    ax1.plot(Vk_ASCE,  z, color=COLOR_ASCE722, lw=2.5, label="ASCE 7-22 - Exposure B (Kz)",
             linestyle="-.")
    ax1.plot(Vk_EC1,   z, color=COLOR_EC1,     lw=2.5, label="EN 1991-1-4 - Cat. III (cr*ln)",
             linestyle=":")

    # Lineas horizontales de referencia por nivel
    niveles_ref = [("PB (+0.00)", 0.0), ("P05 (~18 m)", 18.0),
                   ("P10 (~36 m)", 36.0), ("P18 (~64 m)", 64.0), ("Azotea (~80 m)", 80.0)]
    for lbl, h_val in niveles_ref:
        if h_val > 0:
            ax1.axhline(y=h_val, color=COLOR_GRID, linewidth=0.8, linestyle="--", alpha=0.7)
            ax1.text(V0_MS * 0.62, h_val + 0.8, lbl, fontsize=7.5, color=COLOR_SUBTEXT, alpha=0.9)

    ax1.set_xlabel("Velocidad caracteristica Vk (m/s)", fontsize=10, color=COLOR_TEXT)
    ax1.set_ylabel("Altura sobre el terreno z (m)", fontsize=10, color=COLOR_TEXT)
    ax1.set_title(
        "Perfiles de velocidad media con la altura\n(V0 = 45 m/s - NP 196:1991 - Ciudad del Este)",
        fontsize=10, color=COLOR_TEXT, pad=8
    )
    ax1.set_xlim(V0_MS * 0.60, V0_MS * 1.15)
    ax1.set_ylim(0, H_MAX + 2)
    ax1.legend(loc="lower right", fontsize=8, framealpha=0.85,
               facecolor=COLOR_GRID, edgecolor=COLOR_ACCENT1, labelcolor=COLOR_TEXT)
    ax1.grid(True, color=COLOR_GRID, linewidth=0.6, alpha=0.8)
    ax1.tick_params(colors=COLOR_TEXT)
    for spine in ax1.spines.values():
        spine.set_edgecolor(COLOR_GRID)

    # --- Panel derecho: Tabla y conclusiones -----------------------------------
    ax2 = axes[1]
    ax2.set_facecolor(COLOR_PANEL)
    ax2.axis("off")

    # Tabla comparativa de categorias
    tabla_header = ["Norma", "Cat.\nAdoptada", "Parametros", "Descripcion entorno", "Vk(10m)\n(m/s)"]
    v10 = lambda fn: f"{fn(np.array([10.0]), V0_MS)[0]:.2f}"
    tabla_data = [
        ["NP 196:1991",  "Cat. III\n(Clase B)",   "b=0.85, p=0.175",
         "Zona urbana, obstaculos\nfrecuentes (h~5-15 m)", v10(perfil_np196_cat_iii)],
        ["NBR 6123:2023","Cat. IV\n(Classe B)",    "bm=0.86, p=0.20",
         "Zonas urbanizadas, obstaculos\nnumerosos y poco espaciados", v10(perfil_nbr6123_cat_iv)],
        ["ASCE 7-22",    "Exposure B",             "alpha=7.0, zg=365.76m",
         "Urban/suburban, closely\nspaced obstructions", v10(perfil_asce722_exp_b)],
        ["EN 1991-1-4",  "Cat. III",               "z0=0.30m, zmin=5m",
         "Regular cover vegetation/\nbuildings, suburban terrain", v10(perfil_ec1_cat_iii)],
    ]
    tbl = ax2.table(
        cellText=tabla_data,
        colLabels=tabla_header,
        loc="upper center",
        cellLoc="center",
        bbox=[0.0, 0.54, 1.0, 0.38]
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8.5)
    norm_colors = [COLOR_NP196, COLOR_NBR6123, COLOR_ASCE722, COLOR_EC1]
    for (r, c), cell in tbl.get_celld().items():
        if r == 0:
            cell.set_facecolor(COLOR_GRID)
            cell.set_text_props(color=COLOR_ACCENT1)
        else:
            cell.set_facecolor(COLOR_PANEL)
            cell.set_text_props(color=COLOR_TEXT)
        cell.set_edgecolor(COLOR_GRID)

    # Titulo de conclusion
    ax2.text(0.5, 0.51, "CONCLUSION TECNICA - Clasificacion de Exposicion Adoptada",
             ha="center", fontsize=10, fontweight="bold", color=COLOR_ACCENT1,
             transform=ax2.transAxes)

    conclusiones = [
        ("NP 196:1991",   "CATEGORIA III",  COLOR_NP196,
         "Zona urbana con obstaculos de 5-15 m (factor S1=1.0 terreno plano)"),
        ("NBR 6123:2023", "CATEGORIA IV",   COLOR_NBR6123,
         "Zona urbanizada densa - mayor conservadorismo (bm=0.86, p=0.20)"),
        ("ASCE 7-22",     "EXPOSURE B",     COLOR_ASCE722,
         "Urban/suburban terrain - closely spaced obstructions (alpha=7.0)"),
        ("EN 1991-1-4",   "CATEGORIA III",  COLOR_EC1,
         "Area con cubierta regular de vegetacion/edificios - z0=0.30 m"),
    ]
    y_pos = 0.47
    for norma, cat, color, desc in conclusiones:
        ax2.text(0.03, y_pos, f">> {norma}:",
                 ha="left", fontsize=8.5, fontweight="bold",
                 color=color, transform=ax2.transAxes)
        ax2.text(0.03, y_pos - 0.035, f"   {cat} - {desc}",
                 ha="left", fontsize=8, color=COLOR_TEXT,
                 transform=ax2.transAxes)
        y_pos -= 0.095

    # Nota metodologica
    nota = (
        "NOTA METODOLOGICA:\n"
        "El entorno inmediato del predio (radio 500 m) en Ciudad del Este\n"
        "corresponde a zona urbana de densidad media-alta con edificaciones\n"
        "de 1 a 5 pisos (4-18 m de altura). La eleccion de Cat. III/IV (NBR)\n"
        "y Exp. B (ASCE) es coherente con el entorno consolidado del sector\n"
        "sur de CDE (Av. Itaipu Oeste / Calle Los Lapachos).\n\n"
        "ATENCION - Distintas definiciones de velocidad basica por norma:\n"
        "  NP 196 / NBR 6123: velocidad media de 10 min a 10 m de altura\n"
        "  ASCE 7-22:         velocidad de rafaga de 3 s a 10 m de altura\n"
        "  EN 1991-1-4:       velocidad media de 10 min a 10 m de altura\n\n"
        "La comparacion cuantitativa inter-normativa detallada se realiza\n"
        "en la Etapa E (calculo de presiones y fuerzas por piso)."
    )
    ax2.text(
        0.02, 0.02, nota,
        ha="left", fontsize=7.8, color=COLOR_SUBTEXT,
        transform=ax2.transAxes, style="italic",
        bbox=dict(boxstyle="round,pad=0.5", facecolor=COLOR_GRID,
                  edgecolor=COLOR_ACCENT1, alpha=0.85, linewidth=1.0)
    )

    fig.text(
        0.5, 0.005,
        "Figura 1.5  |  TESIS-EST-GEN-SCRIPT-002  |  eA-5 - Clasificacion de Exposicion  |  "
        "NP 196:1991 / NBR 6123:2023 / ASCE 7-22 / EN 1991-1-4",
        ha="center", fontsize=7, color=COLOR_SUBTEXT, style="italic"
    )

    plt.tight_layout(rect=[0, 0.02, 1, 0.95])
    out_path = OUTPUT_DIR / "figura_1_5_perfiles_velocidad_multinormativos.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight", facecolor=COLOR_BG)
    plt.close(fig)
    print(f"[OK] Figura 1.5 guardada: {out_path}")
    return out_path


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 72)
    print("eA-5 - Analisis de Vientos Dominantes y Clasificacion de Exposicion")
    print("Proyecto: Tesis Edificio 18P - Ciudad del Este, Paraguay")
    print("=" * 72)

    p1 = generar_rosa_de_vientos()
    p2 = generar_perfiles_velocidad()

    print("\n--- RESUMEN DE CLASIFICACION DE EXPOSICION ----------------------------")
    print(f"  NP 196:1991   -> Categoria III  (Zona urbana, obstaculos frecuentes)")
    print(f"  NBR 6123:2023 -> Categoria IV   (Zona urbanizada, obstaculos numerosos)")
    print(f"  ASCE 7-22     -> Exposure B     (Urban/suburban, Kz con alpha=7.0)")
    print(f"  EN 1991-1-4   -> Categoria III  (z0=0.30 m, Regular cover)")
    print(f"\n  Velocidad basica V0 = {V0_MS} m/s  (NP 196:1991 - Ciudad del Este)")
    print(f"\n--- ARCHIVOS GENERADOS ------------------------------------------------")
    print(f"  {p1}")
    print(f"  {p2}")
    print("=" * 72)
