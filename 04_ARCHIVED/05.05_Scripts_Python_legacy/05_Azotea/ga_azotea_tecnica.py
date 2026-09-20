"""
====================================================================
 AZOTEA TÉCNICA + TERRAZA DE EVENTOS + PISCINA (NIVEL AZ, cota 58.00)
 Edificio de Uso Mixto 18P + 2 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | AGENTS.md §13
====================================================================

 Bounding box de la azotea (idéntico a PB/Planta Tipo/Subsuelos):
   X: 2.5 → 87.5 m  (Frente = 85.0 m)  |  Y: 3.0 → 40.0 m  (Prof = 37.0 m)
   Área total huella: 3.145 m²

 PROGRAMA ARQUITECTÓNICO (DEFINITIVO — AGENTS.md §13):
   - BANDA FRENTE (Y:3→17):        Terraza mirador + jardineras + barandas
   - BANDA CENTRAL (Y:17→26):      Salas de máquinas ascensores (sobre N1/N2),
                                   shafts del pasillo técnico, pozos de luz A/B
                                   como claraboyas (voids con baranda)
   - BANDA FONDO (Y:26→40):
       · Ala izquierda (X:2.5→34):   PISCINA RECREATIVA 8×16m + SOLÁRIUM +
                                     vestuarios/duchas + cuarto de filtros
       · Centro (X:34→56):           ZONA TÉCNICA — tanque elevado potable +
                                     tanque PCI + sala HVAC/PTE + tableros
       · Ala derecha (X:56→87.5):    TERRAZA DE EVENTOS + quincho cubierto

 CRITERIOS DE DISEÑO:
   - Un solo nivel conjunto (técnica + amenities) sobre P18 (azotea conjunta).
   - Tanques elevados apoyados sobre los núcleos N1/N2 (columnas continuas).
   - Los pozos de luz A/B quedan como voids abiertos (no se cubren).
   - Piscina recreativa 8×16m = 128 m², profundidad 1.2–1.8m; carga viva
     + volumen de agua gobernados por losa de azotea postensada reforzada.

 SALIDA:
   - Plano:    outputs/plano_azotea_tecnica.png
   - Datos:    outputs/zones_azotea.csv  (id, zona, bbox, área, categoría)
====================================================================
"""

import os
import csv
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ──────────────────────────────────────────────────────────────────
# GEOMETRÍA (idéntica a modelo_estructural.py)
# ──────────────────────────────────────────────────────────────────
X_MIN, X_MAX = 2.5, 87.5
Y_MIN, Y_MAX = 3.0, 40.0
ANCHO = X_MAX - X_MIN      # 85.0 m
PROF = Y_MAX - Y_MIN       # 37.0 m
HUELLA = dict(x0=X_MIN, x1=X_MAX, y0=Y_MIN, y1=Y_MAX, area=ANCHO * PROF)

NUCLEOS = [
    dict(id="N1", x0=34.0, x1=41.0, y0=17.0, y1=26.0, area=63.0),
    dict(id="N2", x0=49.0, x1=56.0, y0=17.0, y1=26.0, area=63.0),
]
PASILLO_TECNICO = dict(x0=41.0, x1=49.0, y0=17.0, y1=26.0, area=72.0)
POZOS = [
    dict(id="A", x0=5.0,  x1=19.0, y0=18.0, y1=25.0, area=98.0),
    dict(id="B", x0=71.0, x1=85.0, y0=18.0, y1=25.0, area=98.0),
]
XS = [2.50, 10.38, 18.25, 26.13, 34.00, 41.00, 49.00, 56.00,
      63.88, 71.75, 79.63, 87.50]
YS = [3.00, 10.00, 17.00, 26.00, 33.00, 40.00]

# ──────────────────────────────────────────────────────────────────
# PROGRAMA — ZONAS DE LA AZOTEA
#   (zona, x0, x1, y0, y1, categoría, color_fc, color_ec, hatch)
# ──────────────────────────────────────────────────────────────────
ZONAS = [
    # --- Banda frente: mirador ---
    dict(id="MIR", nombre="TERRAZA MIRADOR\n+ jardineras",
         x0=2.5, x1=87.5, y0=3.0, y1=17.0, cat="Deck mirador",
         fc="#ecfccb", ec="#65a30d", hatch=None),

    # --- Banda central: técnica ---
    dict(id="SMAQ1", nombre="SALA MÁQ. ASC.\nN1 (2 asc)",
         x0=34.0, x1=41.0, y0=17.0, y1=26.0, cat="Técnica",
         fc="#334155", ec="#0f172a", hatch=None),
    dict(id="SMAQ2", nombre="SALA MÁQ. ASC.\nN2 (2 asc)",
         x0=49.0, x1=56.0, y0=17.0, y1=26.0, cat="Técnica",
         fc="#334155", ec="#0f172a", hatch=None),
    dict(id="SHFT", nombre="SHAFTS + VENTILACIÓN\n(ducto RSU Ø500)",
         x0=41.0, x1=49.0, y0=17.0, y1=26.0, cat="Técnica",
         fc="#a5b4fc", ec="#4338ca", hatch=".."),

    # --- Banda fondo — ala izquierda: piscina + solárium ---
    dict(id="PISC", nombre="PISCINA RECREATIVA\n8×16 m · 128 m²",
         x0=10.25, x1=26.25, y0=29.0, y1=37.0, cat="Piscina",
         fc="#38bdf8", ec="#0369a1", hatch="oo"),
    dict(id="VEST", nombre="VESTUARIOS +\nduchas + baños",
         x0=2.5, x1=8.5, y0=26.0, y1=32.0, cat="Amenities",
         fc="#99f6e4", ec="#0d9488", hatch=None),
    dict(id="FILT", nombre="CUARTO FILTROS\npiscina",
         x0=2.5, x1=8.5, y0=32.0, y1=38.0, cat="Técnica",
         fc="#cffafe", ec="#0891b2", hatch=None),
    dict(id="SOLA", nombre="SOLÁRIUM / DECK\n(resto del ala)",
         x0=2.5, x1=34.0, y0=26.0, y1=40.0, cat="Amenities",
         fc="#fef9c3", ec="#ca8a04", hatch="..."),

    # --- Banda fondo — centro: zona técnica ---
    dict(id="TANQ1", nombre="TANQUE ELEVADO\nPOTABLE ~45 m³",
         x0=34.0, x1=41.0, y0=26.0, y1=33.0, cat="Técnica",
         fc="#bae6fd", ec="#0284c7", hatch="//"),
    dict(id="TANQ2", nombre="TANQUE ELEVADO\nPCI ~45 m³",
         x0=49.0, x1=56.0, y0=26.0, y1=33.0, cat="Técnica",
         fc="#bae6fd", ec="#0284c7", hatch="//"),
    dict(id="HVAC", nombre="SALA HVAC +\nPTE pluvial",
         x0=41.0, x1=49.0, y0=26.0, y1=33.0, cat="Técnica",
         fc="#cbd5e1", ec="#475569", hatch=None),
    dict(id="TABL", nombre="CUARTO DE\nTABLEROS AZOTEA",
         x0=41.0, x1=49.0, y0=33.0, y1=40.0, cat="Técnica",
         fc="#fde68a", ec="#ca8a04", hatch=None),
    dict(id="LIBT", nombre="ACCESO TANQUES\n(espacio técnico)",
         x0=34.0, x1=41.0, y0=33.0, y1=40.0, cat="Técnica",
         fc="#e2e8f0", ec="#64748b", hatch=None),
    dict(id="LIBT2", nombre="ACCESO TANQUES\n(espacio técnico)",
         x0=49.0, x1=56.0, y0=33.0, y1=40.0, cat="Técnica",
         fc="#e2e8f0", ec="#64748b", hatch=None),

    # --- Banda fondo — ala derecha: terraza de eventos ---
    dict(id="QUIN", nombre="QUINCHO CUBIERTO\n+ parrilla (pérgola)",
         x0=56.0, x1=71.0, y0=26.0, y1=33.0, cat="Amenities",
         fc="#fed7aa", ec="#c2410c", hatch="..."),
    dict(id="EVEN", nombre="TERRAZA DE EVENTOS\n(deck abierto)",
         x0=56.0, x1=87.5, y0=26.0, y1=40.0, cat="Amenities",
         fc="#ffedd5", ec="#ea580c", hatch=None),
]


def area_de(z):
    return round((z["x1"] - z["x0"]) * (z["y1"] - z["y0"]), 1)


def exportar_csv(zonas, ruta):
    """Exporta zonas a CSV con id, bbox y área."""
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "zona", "x0", "y0", "x1", "y1", "area_m2", "categoria"])
        for z in zonas:
            w.writerow([z["id"], z["nombre"].replace("\n", " "),
                        z["x0"], z["y0"], z["x1"], z["y1"],
                        area_de(z), z["cat"]])
    return ruta


def dibujar_grilla(ax):
    for x in XS:
        ax.plot([x, x], [Y_MIN - 1.0, Y_MAX + 1.0], color="#94a3b8", lw=0.7,
                ls="--", zorder=1)
    for y in YS:
        ax.plot([X_MIN - 1.0, X_MAX + 1.0], [y, y], color="#94a3b8", lw=0.7,
                ls="--", zorder=1)

    # Pilares estructurales (grilla continua S3→Azotea)
    S_PILAR = 0.6  # sección orientativa en AZ (m) — AGENTS.md §12.2
    for x in XS:
        for y in YS:
            ax.add_patch(patches.Rectangle((x - S_PILAR / 2, y - S_PILAR / 2),
                                           S_PILAR, S_PILAR, facecolor="#334155",
                                           edgecolor="#0f172a", lw=0.8, zorder=14))


def dibujar_pozos(ax):
    for pz in POZOS:
        ax.add_patch(patches.Rectangle((pz["x0"], pz["y0"]),
                                       pz["x1"] - pz["x0"], pz["y1"] - pz["y0"],
                                       facecolor="#e0f2fe", edgecolor="#0369a1",
                                       hatch="////", lw=1.5, zorder=4))
        ax.text((pz["x0"] + pz["x1"]) / 2, (pz["y0"] + pz["y1"]) / 2,
                f"POZO {pz['id']}\nCLARABOYA / VOID\ncon baranda\n(14×7 m · 98 m²)",
                fontsize=6.0, color="#0369a1", ha="center", va="center",
                fontweight="bold", zorder=6)


def generar_plano():
    fig, ax = plt.subplots(figsize=(25, 13))
    fig.patch.set_facecolor("#f8fafc")
    ax.set_facecolor("#f1f5f9")

    # Huella
    ax.add_patch(patches.Rectangle((HUELLA["x0"], HUELLA["y0"]),
                                   ANCHO, PROF, facecolor="#ffffff",
                                   edgecolor="#0f172a", lw=3.0, zorder=2))

    dibujar_grilla(ax)
    dibujar_pozos(ax)

    # Zonas
    for z in ZONAS:
        w = z["x1"] - z["x0"]
        h = z["y1"] - z["y0"]
        ax.add_patch(patches.Rectangle((z["x0"], z["y0"]), w, h,
                                       facecolor=z["fc"], edgecolor=z["ec"],
                                       lw=1.4, hatch=z["hatch"], zorder=3))
        cx, cy = (z["x0"] + z["x1"]) / 2, (z["y0"] + z["y1"]) / 2
        txt_color = "#ffffff" if z["cat"] == "Técnica" and z["fc"] == "#334155" \
            else "#0f172a"
        ax.text(cx, cy + 0.55, z["nombre"], fontsize=5.6, color=txt_color,
                ha="center", va="center", fontweight="bold", zorder=5)
        ax.text(cx, cy - 1.35, f"{area_de(z)} m²", fontsize=5.8,
                color=txt_color, ha="center", va="center",
                fontweight="bold", zorder=5)

    # Huella de los núcleos (borde destacado sobre salas de máquinas)
    for c in NUCLEOS:
        ax.add_patch(patches.Rectangle((c["x0"], c["y0"]),
                                       c["x1"] - c["x0"], c["y1"] - c["y0"],
                                       facecolor="none", edgecolor="#fbbf24",
                                       lw=2.2, ls="--", zorder=7))
        ax.text((c["x0"] + c["x1"]) / 2, c["y1"] - 0.9,
                f"HUECO {c['id']}", fontsize=4.5, color="#d97706",
                ha="center", fontweight="bold", zorder=7)

    # Baranda perimetral (símbolo)
    for x in (X_MIN, X_MAX):
        ax.plot([x, x], [Y_MIN, Y_MAX], color="#0f172a", lw=3.5, zorder=6)
    for y in (Y_MIN, Y_MAX):
        ax.plot([X_MIN, X_MAX], [y, y], color="#0f172a", lw=3.5, zorder=6)

    # Leyenda
    ax.legend(handles=[
        patches.Patch(fc="#38bdf8", ec="#0369a1", hatch="oo",
                      label="Piscina recreativa 8×16m (128 m²)"),
        patches.Patch(fc="#fef9c3", ec="#ca8a04", hatch="...",
                      label="Solárium / deck"),
        patches.Patch(fc="#ffedd5", ec="#ea580c", label="Terraza de eventos"),
        patches.Patch(fc="#fed7aa", ec="#c2410c", hatch="...",
                      label="Quincho cubierto + parrilla"),
        patches.Patch(fc="#bae6fd", ec="#0284c7", hatch="//",
                      label="Tanques elevados (potable + PCI)"),
        patches.Patch(fc="#334155", ec="#0f172a", label="Salas máquinas ascensores"),
        patches.Patch(fc="#cbd5e1", ec="#475569", label="Sala HVAC / PTE / tableros"),
        patches.Patch(fc="#99f6e4", ec="#0d9488", label="Vestuarios + duchas"),
        patches.Patch(fc="#e0f2fe", ec="#0369a1", hatch="////",
                      label="Pozos de luz A/B (claraboyas, void con baranda)"),
        patches.Patch(fc="#ecfccb", ec="#65a30d", label="Terraza mirador + jardineras"),
        patches.Patch(fc="#a5b4fc", ec="#4338ca", hatch="..",
                      label="Shafts / ventilación (pasillo técnico)"),
    ], loc="lower right", fontsize=7.0, framealpha=0.98, edgecolor="#0f172a")

    # Panel informativo
    areas_tec = sum(area_de(z) for z in ZONAS if z["cat"] == "Técnica")
    areas_amen = sum(area_de(z) for z in ZONAS if z["cat"] != "Técnica")
    info = (
        "AZOTEA CONJUNTA (técnica + amenities) — nivel AZ, cota 58.00:\n"
        "────────────────────────────────────────────────────────────\n"
        f"• Superficie huella: {HUELLA['area']:.0f} m²  (85 m × 37 m)\n"
        f"• Área técnica total: {areas_tec:.0f} m²  |  Amenities: {areas_amen:.0f} m²\n"
        f"• Piscina recreativa 8×16 m = 128 m² (prof. 1.2–1.8 m)\n"
        "• Tanques elevados: potable ~45 m³ + PCI ~45 m³ (sobre N1/N2)\n"
        "• Salas de máquinas ascensores sobre N1 y N2 (2 asc + esc. RF c/u)\n"
        "• Pozos de luz A/B = claraboyas/voids con baranda (no se cubren)\n"
        "• Losa azotea postensada reforzada (piscina + tanques) · ACI 318-19\n"
        "• Acceso: escaleras RF de los núcleos + montacargas de mantenimiento"
    )
    ax.text(X_MIN + 0.5, Y_MAX - 0.5, info, fontsize=7.0, color="#0f172a",
            va="top", ha="left", zorder=10,
            bbox=dict(boxstyle="round,pad=0.6", fc="#ffffff", ec="#2563eb", lw=1.5))

    ax.set_xlim(X_MIN - 5, X_MAX + 3)
    ax.set_ylim(Y_MIN - 6, Y_MAX + 5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(
        "AZOTEA TÉCNICA + TERRAZA DE EVENTOS + PISCINA — EDIFICIO 18P + 2 Subsuelos\n"
        "Nivel AZ (cota 58.00 m) · CDE, Paraguay  |  Huella 85×37 m = 3.145 m²  |  "
        "Zona técnica central + amenities en alas y frente",
        fontsize=11, fontweight="bold", pad=12)

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_png = os.path.join(out_dir, "plano_azotea_tecnica.png")
    out_csv = os.path.join(out_dir, "zones_azotea.csv")
    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close()
    exportar_csv(ZONAS, out_csv)
    print(f"[OK] {out_png}")
    print(f"[OK] {out_csv}")
    print(f"     Zonas: {len(ZONAS)} | Técnica {areas_tec:.0f} m² | "
          f"Amenities {areas_amen:.0f} m² | Piscina 128 m²")
    return ZONAS


if __name__ == "__main__":
    generar_plano()
