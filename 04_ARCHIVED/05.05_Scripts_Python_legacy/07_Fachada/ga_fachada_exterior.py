"""
====================================================================
 ARQUITECTURA EXTERIOR EXÓTICA — FACHADA Y VOLUMETRÍA
 Torre 18P + PB + 2 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | Enfoque híbrido (algorítmico + manual)
====================================================================

 Estrategias de piel/volumetría implementadas (todas compatibles con
 losas planas postensadas — la fachada es libre, sin vigas/pilares):

 1. VOLUMETRÍA VERTICAL UNIFORME (torre de muros cortina rectos):
    - SIN retranqueos: la misma huella (85m) se mantiene de P01 a P18.
    - La "exoticidad" vertical se logra con el damero de balcones y el
      ritmo de celosía que cambia por tramo de layout (A/C/B).

 2. PIEL ENVOLVENTE PERFORADA (brise-soleil paramétrico):
    - Celosía metálica / paneles perforados frente a los balcones con
      patrón generativo (densidad por radiación solar: más denso en
      fachada Norte, abierto en Sur).

 3. RITMO ÁUREO / FIBONACCI EN BALCONES (no periódico):
    - El vuelo de cada balcón NO sigue un damero binario (pares/impares),
      sino la secuencia de baja discrepancia  {k·φ} (parte fraccionaria),
      con φ = 1.6180339887… (número áureo).
    - Propiedad clave: la secuencia {k·φ} es CUASI-ALEATORIA y NO PERIÓDICA:
      la repetición existe pero NUNCA es exacta → el ojo no detecta patrón.
    - Cada balcón k (barriendo x e y) toma un vuelo en [0.6, 1.8] m según
      v(k) = 0.6 + 0.9 · frac(k·φ). Determinista y reproducible (tesis).

 4. CORNISAS / PARASOLES HORIZONTALES ONDULADOS:
    - Láminas curvas de metal en las líneas de losa que ondulan en
      curva sinusoidal suave (patrón "ola").

 5. ESQUINAS REDONDEADAS / PANTALLAS LATERALES:
    - Pantallas curvas de H°A° visto en los bordes Este/Oeste que
      envuelven las esquinas (referencia torres premium).

 6. DOBLE FACHADA VEGETAL:
    - Enrejado metálico perimetral en los pozos de luz y bandas de
      transición + vegetación colgante → "torre viva".

 Geometría del edificio:
   X: [2.5 → 87.5 m] (85m) · Y: [3.0 → 40.0 m] (37m)
   PB 4.00m · P01-P18 3.00m c/u · Subsuelos 3.50m c/u
   Altura total ≈ PB(4.0) + 18×3.0 = 58.0 m (+ 2 subsuelos 10.5m)

 OUTPUT: outputs/fachada_sur_estrategias.png
         outputs/volumetria_3d_huella_uniforme.png
         outputs/piel_envolvente_patron.png
====================================================================
"""

import os
import numpy as np
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
import matplotlib.patches as patches

# ──────────────────────────────────────────────────────────────────
# PARÁMETROS DEL EDIFICIO
# ──────────────────────────────────────────────────────────────────
X_MIN, X_MAX = 2.5, 87.5
ANCHO = X_MAX - X_MIN               # 85 m
PROF = 37.0                         # profundidad Y
H_PB = 4.0
H_PISO = 3.0
N_PISOS = 18
ALTURA_TOTAL = H_PB + N_PISOS * H_PISO   # 58.0 m
NIVEL_SUB = 3
ALTURA_SUB = 3.5

# Pisos con layout B (grandes) — NO hay retranqueo, huella constante
PISOS_RETRANQUEO = []

# Número áureo para el ritmo de balcones (secuencia no periódica)
PHI = (1 + 5 ** 0.5) / 2      # 1.6180339887...
VUELO_MIN, VUELO_MAX = 0.6, 1.8   # rango de vuelo de balcones [m]


def vuelo_balcon(k):
    """Vuelo del balcón k según secuencia áurea {k·φ} (no periódica).
    k barre globalmente todos los balcones de la fachada (x, piso)."""
    frac = (k * PHI) % 1.0
    return VUELO_MIN + (VUELO_MAX - VUELO_MIN) * frac


def layout_de_piso(p):
    """Devuelve el layout (A/C/B) según patrón intercalado P01-P18."""
    return ["A", "C", "B"][(p - 1) % 3]


# ──────────────────────────────────────────────────────────────────
# 1. FACHADA SUR — ESTRATEGIAS DE PIEL
# ──────────────────────────────────────────────────────────────────
def generar_fachada_sur():
    fig, ax = plt.subplots(figsize=(22, 13))
    fig.patch.set_facecolor('#f8fafc')
    ax.set_facecolor('#0f172a')

    # Coordenada vertical: 0 = nivel PB, +58 = azotea
    Y0 = -NIVEL_SUB * ALTURA_SUB     # -10.5 m (fondo subsuelos)

    # --- Terreno / línea de calle ---
    ax.plot([X_MIN - 3, X_MAX + 3], [0, 0], color='#fbbf24', lw=2.5, zorder=3)
    ax.text(X_MAX + 1.5, 0.6, "NIVEL CALLE ±0.00", fontsize=8, color='#fbbf24',
            ha='right', fontweight='bold')

    # --- Subsuelos (recortados bajo nivel) ---
    _rect_ax(ax, X_MIN, Y0, ANCHO, -Y0, '#1e293b', '#0f172a', lw=1.0, hatch='///', zorder=2)
    ax.text((X_MIN + X_MAX) / 2, Y0 + 1.2, "3 SUBS. COCHERAS (S1-S2-S3, -10.50 m)",
            fontsize=8, color='#94a3b8', ha='center', fontweight='bold', zorder=4)

    # --- Volumetría VERTICAL UNIFORME: misma huella en todos los pisos ---
    ancho_por_piso = {p: ANCHO for p in range(1, N_PISOS + 1)}

    # --- Dibujo piso por piso (PB + P01-P18) ---
    y_inf = 0.0
    # PB
    _rect_ax(ax, X_MIN, y_inf, ANCHO, H_PB, '#334155', '#1e293b', lw=1.2, zorder=4)
    ax.text((X_MIN + X_MAX) / 2, y_inf + H_PB / 2, "PB COMERCIAL · 4.00 m",
            fontsize=8, color='white', ha='center', fontweight='bold', zorder=6)

    y_inf = H_PB
    for p in range(1, N_PISOS + 1):
        w = ancho_por_piso[p]
        x0 = (X_MIN + X_MAX) / 2 - w / 2
        y_sup = y_inf + H_PISO
        layout = layout_de_piso(p)

        # Colores por layout
        colores = {
            'A': '#0e7490',   # pequeños — cian oscuro
            'C': '#047857',   # combinados — verde
            'B': '#b45309',   # grandes — ámbar
        }
        color = colores[layout]

        # Volumetría vertical uniforme — huella constante (sin retranqueo)
        # Resaltar línea de losa (parasol horizontal en cada piso)
        ax.plot([x0, x0 + w], [y_inf, y_inf], color='#94a3b8', lw=0.8, alpha=0.5, zorder=6)

        # Cuerpo del piso
        _rect_ax(ax, x0, y_inf, w, H_PISO, color, '#1e293b', lw=1.2, zorder=4)

        # Balcones con RITMO ÁUREO {k·φ} (no periódico, sin patrón)
        n_mod = 16 if layout == 'A' else (24 if layout == 'C' else 16)
        mod_w = w / n_mod
        for i in range(n_mod):
            bx0 = x0 + i * mod_w
            k = (p - 1) * n_mod + i          # índice global del balcón
            sob = vuelo_balcon(k)            # vuelo áureo en [0.6, 1.8] m
            ax.add_patch(patches.FancyBboxPatch(
                (bx0 + 0.03, y_inf - sob), mod_w - 0.06, sob + 0.15,
                boxstyle="round,pad=0.02", facecolor='#fef3c7', edgecolor='#b45309',
                lw=0.6, zorder=5))
        ax.text(x0 + w / 2, y_inf - 0.6, f"P{p:02d} · {layout} · {w:.0f}m",
                fontsize=6.5, color='white', ha='center', fontweight='bold', zorder=8)

        # Celosía brise-soleil (piel perforada) — cada 2 pisos sobre balcones
        if p % 2 == 1:
            # Densidad: más densa al Oeste (soleado) → gradiente
            nx = 40
            for i in range(nx):
                fx = x0 + (i + 0.5) * (w / nx)
                dens = 0.5 + 0.5 * (fx - x0) / w   # gradiente Este→Oeste
                h = H_PISO * (0.7 + 0.3 * dens)
                alpha = 0.15 + 0.35 * dens
                ax.plot([fx, fx], [y_inf + 0.15, y_inf + h],
                        color='#fde68a', lw=1.1, alpha=alpha, zorder=6)

        # Parasol horizontal ondulado (cornisa) en línea superior del piso
        xs_line = np.linspace(x0, x0 + w, 120)
        ys_line = y_sup + 0.15 + 0.25 * np.sin(np.linspace(0, 2 * np.pi * 3, 120))
        ax.plot(xs_line, ys_line, color='#94a3b8', lw=1.6, alpha=0.8, zorder=6)

        # Vegetación (doble fachada vegetal) en pisos de transición (C)
        if layout == 'C':
            for vx in np.linspace(x0 + 2, x0 + w - 2, 6):
                ax.add_patch(patches.Circle((vx, y_inf + 0.5), 0.45,
                              facecolor='#22c55e', edgecolor='#14532d', lw=0.6, zorder=7))
            ax.text(x0 + w / 2, y_inf + 1.1, "▲ vegetación", fontsize=5,
                    color='#4ade80', ha='center', fontweight='bold', zorder=7)

        y_inf = y_sup

    # --- Pantallas laterales curvas (esquinas Este/Oeste) ---
    for sx0 in [X_MIN, X_MAX - 2.0]:
        xs_c = np.linspace(sx0, sx0 + 2.0, 40)
        ys_c = 4.0 + (ALTURA_TOTAL - 4.0) * (np.sin(np.linspace(0, np.pi, 40)))
        ax.fill_between(xs_c, ys_c, 4.0, color='#0f172a', alpha=0.55, zorder=3)
    ax.text(X_MAX + 0.5, ALTURA_TOTAL / 2, "PANTALLA\nLATERAL\nCURVA H°A°",
            fontsize=6.5, color='#cbd5e1', ha='left', va='center', fontweight='bold', zorder=6)

    # --- Núcleos (sombras interiores, se marcan como volumen central) ---
    ax.fill_between([X_MIN + 32.5, X_MIN + 52.5], H_PB, ALTURA_TOTAL,
                    color='#0f172a', alpha=0.25, zorder=4)
    ax.text((X_MIN + 42.5), H_PB + 1.0, "NÚCLEOS N1/N2\n(shafts verticales)",
            fontsize=6.5, color='#94a3b8', ha='center', fontweight='bold', zorder=8)

    # --- Azotea (misma huella) ---
    w_az = ancho_por_piso[18]
    ax.add_patch(patches.FancyBboxPatch(
        ((X_MIN + X_MAX) / 2 - w_az / 2 - 1, ALTURA_TOTAL - 0.6), w_az + 2, 2.2,
        boxstyle="round,pad=0.1", facecolor='#64748b', edgecolor='#0f172a', lw=1.5, zorder=6))
    ax.text((X_MIN + X_MAX) / 2, ALTURA_TOTAL + 1.0, "AZOTEA TÉCNICA + TANQUES",
            fontsize=7.5, color='#94a3b8', ha='center', fontweight='bold', zorder=8)

    # --- Leyenda ---
    leyenda = [
        mpatches.Patch(fc='#0e7490', label='Layout A — pequeños (32 aptos)'),
        mpatches.Patch(fc='#047857', label='Layout C — combinados (24 aptos, +vegetación)'),
        mpatches.Patch(fc='#b45309', label='Layout B — grandes (16 aptos)'),
        mpatches.Patch(fc='#fef3c7', ec='#b45309', label='Balcones con ritmo áureo {k·φ} (0.6-1.8m)'),
        patches.Patch(fc='#fde68a', ec='#b45309', label='Celosía brise-soleil paramétrica'),
        mpatches.Patch(fc='#22c55e', label='Vegetación (doble fachada)'),
        mpatches.Patch(fc='#0f172a', alpha=0.55, label='Pantallas laterales curvas H°A°'),
        mpatches.Patch(fc='#94a3b8', label='Parasoles horizontales ondulados'),
    ]
    ax.legend(handles=leyenda, loc='lower right', fontsize=7, framealpha=0.9,
              edgecolor='#0f172a', title="ESTRATEGIAS DE FACHADA", title_fontsize=8)

    ax.set_xlim(X_MIN - 8, X_MAX + 12)
    ax.set_ylim(Y0 - 2, ALTURA_TOTAL + 5)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("FACHADA SUR — ARQUITECTURA EXTERIOR EXÓTICA (huella vertical uniforme P01-P18)\n"
                 "Ritmo áureo {k·φ} · Brise-soleil · Parasoles ondulados · Pantallas curvas · Vegetación",
                 fontsize=12, fontweight='bold', color='white')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, "fachada_sur_estrategias.png")
    plt.tight_layout()
    plt.savefig(p, dpi=160, facecolor='#0f172a')
    plt.close()
    print(f"[OK] {p}")


# ──────────────────────────────────────────────────────────────────
# 2. VOLUMETRÍA 3D CON HUELLA UNIFORME
# ──────────────────────────────────────────────────────────────────
def generar_volumetria_3d():
    from mpl_toolkits.mplot3d import Axes3D  # noqa

    fig = plt.figure(figsize=(16, 12))
    ax = fig.add_subplot(111, projection='3d')
    fig.patch.set_facecolor('#f8fafc')

    # Volumetría VERTICAL UNIFORME: misma huella en todos los pisos
    w = ANCHO
    x0 = 0.0
    for p in range(0, N_PISOS + 1):
        if p == 0:
            y0b, y1b = 0.0, H_PB
            col = '#334155'
        else:
            y0b, y1b = H_PB + (p - 1) * H_PISO, H_PB + p * H_PISO
            layout = layout_de_piso(p)
            col = {'A': '#0e7490', 'C': '#047857', 'B': '#b45309'}[layout]

        # Caja 3D del piso
        _box3d(ax, x0, y0b, w, PROF, y1b - y0b, col, alpha=0.9, zorder=5)

        # Balcones con ritmo áureo {k·φ} (franja exterior sur)
        n_mod = 16
        mod_w = w / n_mod
        for i in range(n_mod):
            k = (p - 1) * n_mod + i
            sob = vuelo_balcon(k)
            bx0 = x0 + i * mod_w
            _box3d(ax, bx0, y0b, mod_w - 0.05, sob, y1b - y0b - 0.2,
                   '#fef3c7', alpha=0.9, zorder=6)

        ax.text(x0 + w / 2, -2, y0b + 1.5, f"P{p:02d}", fontsize=6,
                ha='center', color='#0f172a', fontweight='bold')

    # Azotea
    _box3d(ax, x0, ALTURA_TOTAL, w, PROF, 0.8, '#64748b', alpha=1.0)

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Altura [m]")
    ax.set_xlim(-5, ANCHO + 8)
    ax.set_ylim(-5, PROF + 5)
    ax.set_zlim(0, ALTURA_TOTAL + 3)
    ax.view_init(elev=25, azim=-60)
    ax.set_box_aspect([ANCHO, PROF, ALTURA_TOTAL])
    ax.set_title("VOLUMETRÍA 3D — HUELLA VERTICAL UNIFORME (P01-P18) + BALCONES CON RITMO ÁUREO\n"
                 "La misma huella de 85m se mantiene en todos los pisos (sin retranqueos) — "
                 "vuelos de balcón según {k·φ} (no periódico)",
                 fontsize=11, fontweight='bold')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    p = os.path.join(out, "volumetria_3d_huella_uniforme.png")
    plt.tight_layout()
    plt.savefig(p, dpi=160)
    plt.close()
    print(f"[OK] {p}")


# ──────────────────────────────────────────────────────────────────
# 3. PATRÓN DE PIEL ENVOLVENTE (brise-soleil paramétrico)
# ──────────────────────────────────────────────────────────────────
def generar_piel_envolvente():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
    fig.patch.set_facecolor('#f8fafc')

    # Panel perforado paramétrico: densidad por radiación
    for ax, titulo, n_pan in [(ax1, "CELOSÍA ESTE→OESTE (gradiente de densidad)", 40),
                              (ax2, "CELOSÍA PATRÓN SINUSOIDAL (ola)", 40)]:
        ax.set_facecolor('#0f172a')
        ax.set_xlim(0, 20)
        ax.set_ylim(0, 10)
        for i in range(n_pan):
            fx = (i + 0.5) * (20 / n_pan)
            if titulo.startswith("CELOSÍA ESTE"):
                h = 10 * (0.3 + 0.7 * (fx / 20))
                alpha = 0.15 + 0.45 * (fx / 20)
            else:
                h = 10 * (0.5 + 0.5 * np.abs(np.sin(fx * 0.8)))
                alpha = 0.5
            ax.plot([fx, fx], [0.3, h], color='#fde68a', lw=2.0, alpha=alpha)
            # perforaciones
            ax.add_patch(patches.Circle((fx, h + 0.4), 0.25, fc='#0f172a',
                          ec='#fde68a', lw=0.8, alpha=alpha))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(titulo, fontsize=10, fontweight='bold')

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    p = os.path.join(out, "piel_envolvente_patron.png")
    plt.tight_layout()
    plt.savefig(p, dpi=160)
    plt.close()
    print(f"[OK] {p}")


# ──────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────
def _rect_ax(ax, x, y, w, h, fc, ec, lw=1.0, hatch=None, zorder=3):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec,
                               linewidth=lw, hatch=hatch, zorder=zorder))


def _box3d(ax, x, y, w, d, h, color, alpha=1.0, zorder=5):
    """Caja 3D simple (8 caras) con mpl_toolkits.mplot3d."""
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    verts = [
        [(x, y, 0), (x + w, y, 0), (x + w, y + d, 0), (x, y + d, 0)],
        [(x, y, h), (x + w, y, h), (x + w, y + d, h), (x, y + d, h)],
        [(x, y, 0), (x, y + d, 0), (x, y + d, h), (x, y, h)],
        [(x + w, y, 0), (x + w, y + d, 0), (x + w, y + d, h), (x + w, y, h)],
        [(x, y, 0), (x + w, y, 0), (x + w, y, h), (x, y, h)],
        [(x, y + d, 0), (x + w, y + d, 0), (x + w, y + d, h), (x, y + d, h)],
    ]
    poly = Poly3DCollection(verts, facecolor=color, edgecolor='#0f172a',
                            linewidths=0.3, alpha=alpha, zorder=zorder)
    ax.add_collection3d(poly)


# ──────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────
def main():
    print("=" * 72)
    print("  ARQUITECTURA EXTERIOR EXÓTICA — GENERACIÓN DE IMÁGENES")
    print("=" * 72)
    generar_fachada_sur()
    generar_volumetria_3d()
    generar_piel_envolvente()
    print("=" * 72)
    print("  Estrategias: ritmo aureo {k*PHI} + brise-soleil + parasoles +")
    print("  pantallas curvas + vegetacion (huella uniforme, sin patron)")
    print("=" * 72)


if __name__ == "__main__":
    main()
