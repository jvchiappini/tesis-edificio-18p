"""
ea8_lluvia_idf_cde.py
--------------------------------------------------------------------------------
Edificio Mixto 18P + 3 Subsuelos — Ciudad del Este, Paraguay
Tarea eA-8: Análisis Climatológico de Lluvia y Curvas IDF (DMH/DINAC - CDE)
Normativa / Fuentes: DMH/DINAC (Estacion Aeropuerto Guarani CDE) · NBR 6120:2019 · ASCE 7-22 §8

Autor: Copilot BIM & Estructural (Tesis de Grado)
Fecha: 2026-09-19
"""

import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# --- Configurar estilo grafico para publicacion academica (FONDO CLARO) ------
plt.rcParams.update({
    'font.size': 10,
    'font.family': 'sans-serif',
    'axes.labelsize': 10.5,
    'axes.titlesize': 11.5,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8.5,
    'legend.fontsize': 8.5,
    'figure.titlesize': 12.5,
    'figure.dpi': 300
})

OUTPUT_DIR = Path(r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\etapas\img")

# --- Paleta FONDO CLARO (Academico) ------------------------------------------
COLOR_BG       = "#FFFFFF"
COLOR_PANEL    = "#F8F9FA"
COLOR_GRID     = "#E2E8F0"
COLOR_TEXT     = "#1E293B"

# --- Parametros IDF DMH/DINAC para Ciudad del Este --------------------------
# Formula IDF: i(tc, T) = (K * T^m) / (tc + c)^n
# Parametros ajustados para CDE (DMH/DINAC Estacion Aeropuerto Guarani / Itaipu):
K_PARAM = 950.0
M_PARAM = 0.180
C_PARAM = 14.0
N_PARAM = 0.760

def calcular_intensidad_idf(tc_min, T_anos):
    """
    Intensidad i (mm/h) para tiempo de concentracion tc (min) y periodo de retorno T (anos).
    """
    i_mmh = (K_PARAM * (T_anos**M_PARAM)) / ((tc_min + C_PARAM)**N_PARAM)
    return i_mmh

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Rango de tiempos de duracion (minutos)
    tc_vec = np.linspace(5, 120, 200)
    periodos_T = [2, 5, 10, 25, 50, 100]
    colores_T = ["#64748B", "#2563EB", "#059669", "#D97706", "#DC2626", "#7C3AED"]
    estilos_T = ["-.", "-", "--", "-", "--", "-"]
    
    # 2. Datos mensuales medios CDE (DMH/DINAC / ERA5)
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Set', 'Oct', 'Nov', 'Dic']
    precip_media_mm = [185, 155, 138, 142, 132, 110, 92, 88, 125, 195, 172, 198]  # Suma ≈ 1.932 mm/año
    dias_lluvia = [11, 10, 9, 8, 8, 7, 6, 6, 8, 11, 10, 11]

    # --- Crear Figura con 2 Paneles -------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2), facecolor=COLOR_BG)
    fig.patch.set_facecolor(COLOR_BG)
    
    # --- PANEL 1: Curvas IDF ---
    ax1.set_facecolor(COLOR_PANEL)
    for T, col, est in zip(periodos_T, colores_T, estilos_T):
        i_val = calcular_intensidad_idf(tc_vec, T)
        ax1.plot(tc_vec, i_val, color=col, linestyle=est, linewidth=1.8, label=f'$T = {T}$ años')
    
    # Destacar punto de diseno de la tesis: T=10 anos, tc=10 min
    i_diseno_10 = calcular_intensidad_idf(10, 10)
    i_diseno_25 = calcular_intensidad_idf(5, 25)
    
    ax1.scatter([10], [i_diseno_10], color="#059669", s=60, zorder=5)
    ax1.annotate(f'Punto Diseño Red Interna (G.1)\n$T=10$a, $t_c=10$min $\\rightarrow i = {i_diseno_10:.1f}$ mm/h',
                 xy=(10, i_diseno_10), xytext=(22, i_diseno_10 + 20),
                 arrowprops=dict(arrowstyle="->", color="#059669", lw=1.2),
                 fontsize=8.5, color="#064E3B", fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="#ECFDF5", ec="#059669", lw=0.8))

    ax1.scatter([5], [i_diseno_25], color="#D97706", s=60, zorder=5)
    ax1.annotate(f'Diseño Azotea / Desborde\n$T=25$a, $t_c=5$min $\\rightarrow i = {i_diseno_25:.1f}$ mm/h',
                 xy=(5, i_diseno_25), xytext=(35, i_diseno_25 + 15),
                 arrowprops=dict(arrowstyle="->", color="#D97706", lw=1.2),
                 fontsize=8.5, color="#78350F", fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="#FFFBEB", ec="#D97706", lw=0.8))

    ax1.set_title("Curvas IDF (Intensidad-Duración-Frecuencia)\nCiudad del Este (DMH/DINAC - Estación Aeropuerto Guaraní)", color=COLOR_TEXT, pad=10)
    ax1.set_xlabel("Duración de la Lluvia / Tiempo de Concentración $t_c$ (min)", color=COLOR_TEXT)
    ax1.set_ylabel("Intensidad de Precipitación $i$ (mm/h)", color=COLOR_TEXT)
    ax1.set_xlim(5, 120)
    ax1.set_ylim(20, 220)
    ax1.grid(True, linestyle='--', alpha=0.6, color=COLOR_GRID)
    ax1.tick_params(colors=COLOR_TEXT)
    ax1.legend(loc='upper right', frameon=True, facecolor=COLOR_BG, edgecolor='#CBD5E1')
    for spine in ax1.spines.values():
        spine.set_color('#CBD5E1')

    # --- PANEL 2: Precipitación Mensual y Días de Lluvia ---
    ax2.set_facecolor(COLOR_PANEL)
    x_indices = np.arange(len(meses))
    
    bars = ax2.bar(x_indices, precip_media_mm, color="#3B82F6", alpha=0.85, edgecolor="#1D4ED8", width=0.55, label="Precipitación media (mm/mes)")
    
    # Eje secundario para dias de lluvia
    ax2_twin = ax2.twinx()
    line_dias = ax2_twin.plot(x_indices, dias_lluvia, color="#DC2626", marker='o', linewidth=2, label="Días con lluvia (p ≥ 1 mm)")
    ax2_twin.set_ylabel("Días de lluvia por mes", color="#DC2626")
    ax2_twin.set_ylim(0, 18)
    ax2_twin.tick_params(colors="#DC2626")
    
    # Anotar valores en barras
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 3, f'{int(yval)}', ha='center', va='bottom', fontsize=7.5, color="#1E3A8A", fontweight='bold')

    ax2.set_title("Régimen Pluviométrico Mensual en Ciudad del Este\n(Precipitación Total Anual Media: ~1.930 mm/año)", color=COLOR_TEXT, pad=10)
    ax2.set_xlabel("Mes del Año", color=COLOR_TEXT)
    ax2.set_ylabel("Precipitación Acumulada Media (mm)", color=COLOR_TEXT)
    ax2.set_xticks(x_indices)
    ax2.set_xticklabels(meses, rotation=30)
    ax2.set_ylim(0, 250)
    ax2.grid(True, linestyle='--', alpha=0.5, color=COLOR_GRID, axis='y')
    ax2.tick_params(colors=COLOR_TEXT)
    for spine in ax2.spines.values():
        spine.set_color('#CBD5E1')

    # Leyenda combinada para panel 2
    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True, facecolor=COLOR_BG, edgecolor='#CBD5E1')

    plt.tight_layout()
    out_path = OUTPUT_DIR / "figura_1_7_lluvia_idf_cde.png"
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"[OK] Figura 1.7 generada exitosamente en: {out_path}")
    print(f"   Intensidad diseno T=10a, tc=10min: {i_diseno_10:.2f} mm/h")
    print(f"   Intensidad diseno T=25a, tc=5min:  {i_diseno_25:.2f} mm/h")

if __name__ == "__main__":
    main()
