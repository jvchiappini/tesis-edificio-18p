"""
ea6_clasificacion_sismica_espectro.py
--------------------------------------------------------------------------------
Edificio Mixto 18P + 2 Subsuelos — Ciudad del Este, Paraguay
Tarea eA-6: Clasificacion Sismica del Sitio y Espectro de Respuesta Elastica
Normativa: NBR 15421:2023 / ASCE 7-22 §11 / Eurocodigo 8 (EN 1998-1)

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
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 13,
    'figure.dpi': 300
})

OUTPUT_DIR = Path(r"c:\Users\jvchi\CARPETAS\IngChiappini\00_TESIS_EDIFICIO_18P\etapas\img")

# --- Paleta FONDO CLARO (Academico) ------------------------------------------
COLOR_BG       = "#FFFFFF"
COLOR_PANEL    = "#F8F9FA"
COLOR_GRID     = "#E2E8F0"
COLOR_TEXT     = "#1E293B"

COLOR_PGA_005  = "#2563EB"  # Azul (ag = 0.05g)
COLOR_PGA_008  = "#D97706"  # Ambar (ag = 0.08g)
COLOR_BUILDING = "#DC2626"  # Rojo para periodo estimado del edificio

def calcular_espectro_asce_nbr(ag, site_class="B"):
    """
    Calcula el espectro de respuesta elástica Sa(T) según ASCE 7-22 / NBR 15421.
    Parametros:
      ag: Aceleracion pico del suelo en g (ej. 0.05g o 0.08g)
      site_class: 'B' (Roca - Formacion Serra Geral)
    """
    # Para Site Class B (roca), Fa = 1.0, Fv = 1.0
    Fa = 1.0
    Fv = 1.0
    
    # Parametros espectrales espectro de diseño (5% amortiguamiento)
    Ss = 2.5 * ag
    S1 = 1.25 * ag
    
    SMS = Fa * Ss
    SM1 = Fv * S1
    
    SDS = (2.0 / 3.0) * SMS
    SD1 = (2.0 / 3.0) * SM1
    
    T0 = 0.2 * (SD1 / SDS)
    TS = SD1 / SDS
    TL = 4.0  # s
    
    T_vec = np.linspace(0.001, 4.0, 500)
    Sa_vec = np.zeros_like(T_vec)
    
    for i, T in enumerate(T_vec):
        if T < T0:
            Sa_vec[i] = SDS * (0.4 + 0.6 * (T / T0))
        elif T <= TS:
            Sa_vec[i] = SDS
        elif T <= TL:
            Sa_vec[i] = SD1 / T
        else:
            Sa_vec[i] = (SD1 * TL) / (T**2)
            
    return T_vec, Sa_vec, SDS, SD1, T0, TS

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Periodo fundamental estimado para edificio H=64m (18P)
    # Ta = C_t * H_n^x = 0.0488 * 64^0.75 ≈ 1.10 s (o aproxi T ≈ 0.1*N = 1.8 s)
    T_edificio_min = 1.10
    T_edificio_max = 1.80
    
    T_005, Sa_005, SDS_005, SD1_005, T0_005, TS_005 = calcular_espectro_asce_nbr(0.05, "B")
    T_008, Sa_008, SDS_008, SD1_008, T0_008, TS_008 = calcular_espectro_asce_nbr(0.08, "B")
    
    fig, ax = plt.subplots(figsize=(9.5, 5.5), facecolor=COLOR_BG)
    ax.set_facecolor(COLOR_PANEL)
    
    ax.plot(T_005, Sa_005, color=COLOR_PGA_005, linewidth=2.2, label=r'Espectro $a_g = 0{,}05\text{g}$ (Límite inferior CDE - NBR 15421)')
    ax.plot(T_008, Sa_008, color=COLOR_PGA_008, linewidth=2.2, linestyle='--', label=r'Espectro $a_g = 0{,}08\text{g}$ (Límite conservador CDE)')
    
    # Sombreado zona de periodo del edificio 18P
    ax.axvspan(T_edificio_min, T_edificio_max, color=COLOR_BUILDING, alpha=0.12, label=r'Rango Período Fundamental Edificio 18P ($T_1 \approx 1{,}10$–$1{,}80\text{ s}$)')
    ax.axvline(x=1.45, color=COLOR_BUILDING, linestyle=':', linewidth=1.5, label=r'Período medio estimado $T_1 \approx 1{,}45\text{ s}$')
    
    # Anotaciones de Sa para el edificio
    Sa_edificio_005 = SD1_005 / 1.45
    Sa_edificio_008 = SD1_008 / 1.45
    
    ax.scatter([1.45], [Sa_edificio_005], color=COLOR_PGA_005, s=50, zorder=5)
    ax.scatter([1.45], [Sa_edificio_008], color=COLOR_PGA_008, s=50, zorder=5)
    
    ax.annotate(f'$S_a(T_1) \\approx {Sa_edificio_005:.4f}\\text{{g}}$\n({Sa_edificio_005*9.81:.3f} m/s²)',
                xy=(1.45, Sa_edificio_005), xytext=(1.8, Sa_edificio_005 + 0.015),
                arrowprops=dict(arrowstyle="->", color=COLOR_PGA_005, lw=1.2),
                fontsize=8.5, color=COLOR_PGA_005, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", fc="#EFF6FF", ec=COLOR_PGA_005, lw=0.8))

    ax.annotate(f'$S_a(T_1) \\approx {Sa_edificio_008:.4f}\\text{{g}}$\n({Sa_edificio_008*9.81:.3f} m/s²)',
                xy=(1.45, Sa_edificio_008), xytext=(1.8, Sa_edificio_008 + 0.025),
                arrowprops=dict(arrowstyle="->", color=COLOR_PGA_008, lw=1.2),
                fontsize=8.5, color=COLOR_PGA_008, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3", fc="#FFFBEB", ec=COLOR_PGA_008, lw=0.8))

    ax.set_title("Espectro de Respuesta Elástica de Pseudo-Aceleración $S_a(T)$ — Ciudad del Este\n(NBR 15421:2023 / ASCE 7-22 — Sustrato Rocoso Formación Serra Geral, Site Class B)", color=COLOR_TEXT, pad=12)
    ax.set_xlabel("Período Estructural $T$ (segundos)", color=COLOR_TEXT)
    ax.set_ylabel("Pseudo-Aceleración Espectral $S_a(T)$ / g", color=COLOR_TEXT)
    
    ax.set_xlim(0, 4.0)
    ax.set_ylim(0, 0.16)
    ax.grid(True, linestyle='--', alpha=0.6, color=COLOR_GRID)
    ax.tick_params(colors=COLOR_TEXT)
    for spine in ax.spines.values():
        spine.set_color('#CBD5E1')
        
    ax.legend(loc='upper right', frameon=True, facecolor=COLOR_BG, edgecolor='#CBD5E1')
    
    # Guardar figura
    out_path = OUTPUT_DIR / "figura_1_6_espectro_sismico_cde.png"
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"[OK] Figura 1.6 generada exitosamente en: {out_path}")
    print(f"   Parametros Espectrales ag=0.05g: SDS={SDS_005:.4f}g, SD1={SD1_005:.4f}g, T0={T0_005:.3f}s, TS={TS_005:.3f}s")
    print(f"   Parametros Espectrales ag=0.08g: SDS={SDS_008:.4f}g, SD1={SD1_008:.4f}g, T0={T0_008:.3f}s, TS={TS_008:.3f}s")
    print(f"   Sa(T1=1.45s) ag=0.05g: {Sa_edificio_005:.4f}g (Corta base sismo muy bajo)")

if __name__ == "__main__":
    main()


