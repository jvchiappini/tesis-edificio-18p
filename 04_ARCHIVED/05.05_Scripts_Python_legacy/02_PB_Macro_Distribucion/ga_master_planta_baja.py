"""
====================================================================
 MASTERPLAN PLANTA BAJA (PB) — MACRO DISTRIBUCIÓN DEFINITIVA v2
 CON RED DE PASILLOS | Edificio de Uso Mixto 18P | CDE, Paraguay
====================================================================

 Bounding Box Edificio (idéntico a todos los niveles):
   X: [2.5 → 87.5 m]   (Frente Urbano = 85.0 m)
   Y: [3.0 → 40.0 m]   (Profundidad Total = 37.0 m)

 2 NÚCLEOS H°A° GEMELOS ROTADOS 90° (DEFINITIVOS):
   N1 Oeste: X: 34.0→41.0 / Y: 17.0→26.0 (7m × 9m)
   N2 Este : X: 49.0→56.0 / Y: 17.0→26.0 (7m × 9m)
   Pasillo técnico central (ducto RSU Ø500 + shafts): X: 41.0→49.0 / Y: 17→26

 GRILLA ESTRUCTURAL ÓPTIMA (continua S3→Azotea):
   Ejes X: [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
            63.88, 71.75, 79.63, 87.50]
   Ejes Y: [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

 RED DE PASILLOS (NUEVA — conecta todo el PB):
   P1 ACCESO:     X:41→49 / Y:3→17 (112 m²) — entrada principal desde calle
   P2 TÉCNICO:    X:41→49 / Y:17→26 (72 m²) — ducto RSU + shafts (ya existente)
   P3 LONGITUDINAL: X:2.5→87.5 / Y:26→29 (255 m²) — atraviesa TODO el edificio,
                  conecta Núcleos ↔ Administración ↔ Depósito RSU ↔ Business Ctr.
                  Se accede desde P2 (subiendo en X:41→49). Desde P3 se entra
                  a los Baños (ala oeste) y al Coworking (ala este). ✓

 ZONIFICACIÓN (área real calculada):
   FRENTE (fachada comercial):
     SALONES 1-4 (OESTE, X:2.5→34 / Y:3→21, vanos 7.875m):
       Salón 1 X:2.5→10.38 | Salón 2 X:10.38→18.25 | Salón 3 X:18.25→26.13 | Salón 4 X:26.13→34
       (141.75 m² c/u, libres)
     Comercio menor X:34→41 Y:3→17 (98) | Comercio menor X:49→56 Y:3→17 (98)
     SALONES 5-8 (ESTE, X:56→87.5 / Y:3→21, vanos 7.875m):
       Salón 5 X:56→63.88 | Salón 6 X:63.88→71.75 | Salón 7 X:71.75→79.63 | Salón 8 X:79.63→87.5
       (141.75 m² c/u, libres)
   CENTRO: N1 (63) | P2 (72) | N2 (63)
   ALA OESTE (X:2.5→34):
     Sanitarios + PMR + Lactario: X:2.5→34 / Y:21→26 (157.5) [acceso desde P3]
     Administración & BMS: X:2.5→34 / Y:29→40 (346.5) [acceso desde P3]
   ALA ESTE (X:56→87.5):
     Business Center + Coworking: X:56→87.5 / Y:21→26 (157.5) [acceso desde P3]
     GIMNASIO / SUM: X:56→81.5 / Y:29→40 (280.5, era Megastore)
   FONDO CENTRAL (X:34→56, Y:29→40):
     Depósito RSU central (contenedor basculante ~10 m³): X:34→49 / Y:29→40 (165)
     Subestación ANDE: X:49→56 / Y:29→33 (49) | Reservorio PCI: X:49→56 / Y:33→40 (49)
   LADO ESTE — INGRESO VEHICULAR + RAMPA → S1:
     Pasaje vehicular (ingreso desde el ESTE): X:81.5→87.5 / Y:26→33 (6m, 2 carriles)
     Rampa de acceso al subsuelo S1: X:81.5→87.5 / Y:33→40 (6m, 2 carriles)
     Los vehículos ingresan por el lado ESTE, circulan por el pasaje vehicular
     y descienden por la rampa NE hacia S1 (rampa única NE de S1, mirando al Oeste).

 Sistema RSU (DEFINITIVO §9.2): ducto central X:41→49 desciende a PB →
 tramo horizontal Ø500 1.5% hasta Depósito RSU central (acceso camión por
 pasillo vehicular desde el frente, sin entrar al subsuelo).

 SALONES COMERCIALES 1-5: espacios flexibles libres (el inquilino define).
 NO crear scripts de micro-distribución para salones comerciales.

 OUTPUT: outputs/masterplan_planta_baja.png
====================================================================
"""

import os
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ------------------------------------------------------------------
# Geometría base
# ------------------------------------------------------------------
X_MIN, X_MAX = 2.5, 87.5
Y_MIN, Y_MAX = 3.0, 40.0

NUCLEOS = [
    dict(x0=34.0, x1=41.0, y0=17.0, y1=26.0, nombre="N1"),
    dict(x0=49.0, x1=56.0, y0=17.0, y1=26.0, nombre="N2"),
]
PASILLO_TECNICO = dict(x0=41.0, x1=49.0, y0=17.0, y1=26.0)

XS = [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00, 63.88, 71.75, 79.63, 87.50]
YS = [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

# ------------------------------------------------------------------
# PASILLOS (se dibujan encima, zorder alto)
# ------------------------------------------------------------------
PASILLOS = [
    dict(nombre="P1 ACCESO", x0=41.0, x1=49.0, y0=3.0, y1=17.0),
    dict(nombre="P2 TÉCNICO\n(ducto RSU)", x0=41.0, x1=49.0, y0=17.0, y1=26.0),
    dict(nombre="P3 LONGITUDINAL", x0=2.5, x1=81.5, y0=26.0, y1=29.0),
]

# ------------------------------------------------------------------
# ZONAS DEL MASTERPLAN
# ------------------------------------------------------------------
ZONAS = [
    # Frente comercial — 8 SALONES (vanos 7.875m)
    dict(nombre="SALÓN 1\n(142 m², libre)", x0=2.5,   x1=10.38, y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    dict(nombre="SALÓN 2\n(142 m², libre)", x0=10.38, x1=18.25, y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    dict(nombre="SALÓN 3\n(142 m², libre)", x0=18.25, x1=26.13, y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    dict(nombre="SALÓN 4\n(142 m², libre)", x0=26.13, x1=34.0,  y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    dict(nombre="COMERCIO\nMENOR (libre)",  x0=34.0,  x1=41.0,  y0=3.0,  y1=17.0, color='#fde68a', edge='#b45309'),
    dict(nombre="COMERCIO\nMENOR (libre)",  x0=49.0,  x1=56.0,  y0=3.0,  y1=17.0, color='#fde68a', edge='#b45309'),
    dict(nombre="SALÓN 5\n(142 m², libre)", x0=56.0,  x1=63.88, y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    dict(nombre="SALÓN 6\n(142 m², libre)", x0=63.88, x1=71.75, y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    dict(nombre="SALÓN 7\n(142 m², libre)", x0=71.75, x1=79.63, y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    dict(nombre="SALÓN 8\n(142 m², libre)", x0=79.63, x1=87.5,  y0=3.0, y1=21.0, color='#fcd34d', edge='#b45309'),
    # Ala oeste
    dict(nombre="SANITARIOS PÚBLICOS\n+ PMR + LACTARIO\n(157.5 m²)", x0=2.5, x1=34.0, y0=21.0, y1=26.0, color='#f9a8d4', edge='#be185d'),
    dict(nombre="ADMINISTRACIÓN\n& BMS (346.5 m²)", x0=2.5, x1=34.0, y0=29.0, y1=40.0, color='#67e8f9', edge='#0e7490'),
    # Ala este
    dict(nombre="BUSINESS CENTER\n+ COWORKING (157.5 m²)", x0=56.0, x1=87.5, y0=21.0, y1=26.0, color='#86efac', edge='#15803d'),
    dict(nombre="GIMNASIO / SUM\n(280.5 m²)", x0=56.0, x1=81.5, y0=29.0, y1=40.0, color='#86efac', edge='#15803d'),
    # Rampa vehicular → S1 (esquina NE, conecta PB con S1)
    dict(nombre="RAMPA\nVEHICULAR → S1\n(6m, 2 carriles)", x0=81.5, x1=87.5, y0=33.0, y1=40.0, color='#fb923c', edge='#c2410c'),
    # Pasaje vehicular (ingreso desde el ESTE hacia la rampa NE)
    dict(nombre="PASAJE\nVEHICULAR\n(ingreso ESTE)", x0=81.5, x1=87.5, y0=26.0, y1=33.0, color='#fdba74', edge='#ea580c'),
    # Fondo central (MEP)
    dict(nombre="DEPÓSITO RSU\n(contenedor basculante ~10 m³)\n(165 m²)", x0=34.0, x1=49.0, y0=29.0, y1=40.0, color='#cbd5e1', edge='#334155'),
    dict(nombre="SUBESTACIÓN\nANDE (49 m²)", x0=49.0, x1=56.0, y0=29.0, y1=33.0, color='#fca5a5', edge='#b91c1c'),
    dict(nombre="RESERVORIO\nPCI+POTABLE (49 m²)", x0=49.0, x1=56.0, y0=33.0, y1=40.0, color='#93c5fd', edge='#1d4ed8'),
]


def area(z):
    return (z['x1'] - z['x0']) * (z['y1'] - z['y0'])


def generar():
    fig, ax = plt.subplots(figsize=(22, 12))
    fig.patch.set_facecolor('#f8fafc')
    ax.set_facecolor('#f1f5f9')

    ax.add_patch(Rectangle((X_MIN, Y_MIN), X_MAX - X_MIN, Y_MAX - Y_MIN,
                           facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.5, zorder=2))

    # Zonas
    for z in ZONAS:
        ax.add_patch(Rectangle((z['x0'], z['y0']), z['x1'] - z['x0'], z['y1'] - z['y0'],
                               facecolor=z['color'], edgecolor=z['edge'], lw=1.2, zorder=3))
        cx, cy = (z['x0'] + z['x1']) / 2, (z['y0'] + z['y1']) / 2
        ax.text(cx, cy, z['nombre'], fontsize=7, fontweight='bold',
                color='#0f172a', ha='center', va='center', zorder=4)

    # Pasillos (se dibujan encima de las zonas)
    for p in PASILLOS:
        ax.add_patch(Rectangle((p['x0'], p['y0']), p['x1'] - p['x0'], p['y1'] - p['y0'],
                               facecolor='#f1f5f9', edgecolor='#64748b', hatch='///', lw=1.5, zorder=8))
        cx, cy = (p['x0'] + p['x1']) / 2, (p['y0'] + p['y1']) / 2
        ax.text(cx, cy, p['nombre'], fontsize=7, fontweight='bold',
                color='#334155', ha='center', va='center', zorder=9)

    # Flechas de conexión desde el pasillo técnico
    ax.annotate("", xy=(34.0, 27.5), xytext=(41.0, 27.5),
                arrowprops=dict(arrowstyle='->', color='#0e7490', lw=2), zorder=9)
    ax.annotate("", xy=(56.0, 27.5), xytext=(49.0, 27.5),
                arrowprops=dict(arrowstyle='->', color='#15803d', lw=2), zorder=9)
    ax.text(37.5, 28.2, "→ Baños", fontsize=6.5, color='#0e7490', ha='center', fontweight='bold', zorder=9)
    ax.text(52.5, 28.2, "→ Coworking", fontsize=6.5, color='#15803d', ha='center', fontweight='bold', zorder=9)

    # Núcleos
    for c in NUCLEOS:
        ax.add_patch(Rectangle((c['x0'], c['y0']), c['x1'] - c['x0'], c['y1'] - c['y0'],
                               facecolor='#334155', edgecolor='#0f172a', lw=2.5, zorder=10))
        ax.text((c['x0'] + c['x1']) / 2, (c['y0'] + c['y1']) / 2,
                f"NÚCLEO {c['nombre']}\n2 asc + escalera RF\n(continúa desde subsuelos)",
                color='white', fontsize=7, fontweight='bold', ha='center', va='center', zorder=11)

    # Ducto RSU (descarga al depósito)
    ax.annotate("", xy=(41.5, 29.5), xytext=(41.5, 25.5),
                arrowprops=dict(arrowstyle='->', color='#334155', lw=2.5), zorder=9)
    ax.text(41.5, 29.8, "ducto RSU ↓\ndescarga", fontsize=6, color='#334155',
            ha='center', va='bottom', fontweight='bold', zorder=9)

    # Grilla
    for x in XS:
        ax.plot([x, x], [Y_MIN - 1.5, Y_MAX + 1.5], color='#94a3b8', lw=1.0, ls='--', zorder=1)
    for y in YS:
        ax.plot([X_MIN - 1.5, X_MAX + 1.5], [y, y], color='#94a3b8', lw=1.0, ls='--', zorder=1)

    # Pilares estructurales (grilla completa XS×YS, continuidad S3→Azotea)
    S_PILAR = 0.9  # sección orientativa en PB (m) — AGENTS.md §12.2
    for x in XS:
        for y in YS:
            ax.add_patch(Rectangle((x - S_PILAR / 2, y - S_PILAR / 2), S_PILAR, S_PILAR,
                                   facecolor='#334155', edgecolor='#0f172a', lw=0.8, zorder=14))

    for i, x in enumerate(XS):
        ax.text(x, Y_MIN - 1.9, f"{i+1}", fontsize=8, fontweight='bold', color='#0f172a',
                ha='center', va='top', zorder=12)
    for i, y in enumerate(YS):
        ax.text(X_MIN - 1.9, y, chr(65 + i), fontsize=8, fontweight='bold', color='#0f172a',
                ha='right', va='center', zorder=12)

    total_zonas = sum(area(z) for z in ZONAS)
    total_pasillos = sum(area(p) for p in PASILLOS)
    resumen = (
        "MASTERPLAN PLANTA BAJA (PB) v2 — CON RED DE PASILLOS:\n"
        "────────────────────────────────────────────────\n"
        f"• HUELTA: 85m × 37m = {85*37} m² | Zonas: {total_zonas:.0f} m² + Pasillos: {total_pasillos:.0f} m²\n"
        "• SIN LOBBY CENTRAL — solo pasillos de circulación\n"
        "• RED: P1 Acceso (calle) → P2 Técnico (ducto RSU) → P3 Longitudinal\n"
        "• P3 conecta: Núcleos ↔ Baños ↔ Administración ↔ Depósito RSU ↔ Coworking\n"
        "• 8 SALONES COMERCIALES (142 m² c/u = 1,134 m²) — libres\n"
        "• GIMNASIO / SUM: X:56→81.5 / Y:29→40 (280.5 m²)\n"
        "• RAMPA VEHICULAR esquina NE (X:81.5→87.5 / Y:33→40) → desciende a S1\n"
        "• INGRESO VEHICULAR LADO ESTE: pasaje vehicular X:81.5→87.5 / Y:26→33 (6m, 2 carriles)\n"
        "• DUCTO RSU central X:41→49 → Depósito RSU central (contenedor basculante)\n"
        "• MEP fondo central: subestación ANDE + reservorio PCI/potable\n"
        "• NÚCLEOS N1/N2 continúan desde subsuelos (63 m² c/u)\n"
        "• Altura PB libre: 4.00 m | Cielorraso 3.20 m (pleno técnico ≥0.80 m)"
    )
    ax.text(X_MIN, Y_MIN - 5.5, resumen, fontsize=8.5, fontweight='bold', va='top',
            bbox=dict(boxstyle='round,pad=0.6', facecolor='white', edgecolor='#0284c7', lw=1.5), zorder=20)

    ax.set_xlim(X_MIN - 7, X_MAX + 4)
    ax.set_ylim(Y_MIN - 14, Y_MAX + 3)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title("MASTERPLAN PLANTA BAJA (PB) v2 — CON RED DE PASILLOS",
              fontsize=13, fontweight='bold')

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "masterplan_planta_baja.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Masterplan PB v2 generado: {out_path}")
    print(f"Zonas: {total_zonas:.0f} m² | Pasillos: {total_pasillos:.0f} m² | Total: {total_zonas + total_pasillos:.0f} m²")
    return total_zonas


if __name__ == "__main__":
    generar()