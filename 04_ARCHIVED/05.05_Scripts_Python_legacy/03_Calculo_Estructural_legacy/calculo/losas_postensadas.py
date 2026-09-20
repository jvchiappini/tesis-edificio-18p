"""
====================================================================
 LOSAS POSTENSADAS — DISEÑO POR TIPO DE LOSA (AZ · PB · PT-A/B/C · S1/S2/S3)
 Edificio 18P + 2 Subsuelos | CDE, Paraguay
 Normas: ACI 318-19 (§8.10/§8.11 EFM/DDM, §19 presfuerzo, §22.6 punzonamiento)
         NBR 6118 (§14.7.6 losas macizas, §19.5 punzonamiento, ELS)
         PTI (postensado no adherido)
====================================================================

 Cada tipo de losa se diseña por separado con sus cargas y espesor:

   | Caso  | Uso            | h (m) | g+q (kN/m²) | Notas |
   |-------|----------------|-------|-------------|-------|
   | S1/S2/S3 | cocheras    | 0.24  | 9.50  | capitel 0.40 |
   | PB    | comercial      | 0.23  | 10.25 | drop panel 0.40 |
   | PT-A/B/C | residencial | 0.19  | 8.75  | pozos A/B (bordes) |
   | AZ    | azotea         | 0.30  | 10.50 | piscina 15 + tanques 10 (locales) |

 ETAPAS POR CASO (camino de cargas de arriba hacia abajo):
   1. Verificación de espesor (PT: L/45–L/48 · ACI 318 §8.3.1.1)
   2. Momento estático total  Mo = q·l2·ln²/8  (EFM, ACI §8.10.3)
   3. Distribución de momentos (DDM, ACI Tabla 8.10.5.1) → franja de
      columna / franja central, por metro de franja
   4. Postensado: carga balanceada (PTI), presfuerzo requerido, tendones
   5. Punzonamiento losa-pilar (ACI §22.6.5.2 / NBR 6118 §19.5)
   6. Flechas ELS (L/480 ACI / L/250 NBR)
   7. Reacción al pilar: N = q·Atrib (acumulada) + momento desbalanceado

 OBSERVACIÓN ESTRUCTURAL:
   - PT-A, PT-B y PT-C comparten la MISMA losa estructural (misma grilla
     y mismas cargas): los layouts difieren solo arquitectónicamente.
     Se calcula cada caso y el resultado es idéntico (se documenta).
   - S1, S2 y S3 comparten el mismo diseño de losa (se documenta).

 SALIDAS:
   - outputs/losas_resultados.csv    (resumen por caso)
   - outputs/losas_momentos_por_caso.png  (comparativa Mo/Md)
   - outputs/losas_por_caso.txt      (memoria detallada por caso)
====================================================================
"""

import os
import csv
import numpy as np
import matplotlib
if __name__ == "__main__":
    matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
os.makedirs(OUT, exist_ok=True)

# ──────────────────────────────────────────────────────────────────
# PARÁMETROS DE MATERIAL (H-30 · CA-50 · tendones 0,6")
# ──────────────────────────────────────────────────────────────────
FC = 30.0            # f'c MPa (H-30)
FCI = 0.70 * FC      # f'ci a transferencia (típico 0.7 f'c)
FPU = 1860.0         # MPa (tendón baja relajación)
APS = 140.0          # mm² (tendón 0,6" = 15,2 mm)
F_TENDON = 150.0     # kN efectivos por tendón (tras pérdidas ~0,7·fpu·Aps)
PHI_CORTANTE = 0.75  # φ cortante (ACI 318)

# ──────────────────────────────────────────────────────────────────
# DEFINICIÓN DE CASOS DE LOSA
#   l1, l2 = luces (m) del panel representativo (mayor exigencia)
#   h      = espesor losa (m) · h_cap = altura capitel/drop (m)
#   g, q   = carga permanente y variable (kN/m²)  (NBR 6120, §14.3)
#   notas  = particularidades (piscina, tanques, pozos, capiteles)
# ──────────────────────────────────────────────────────────────────
CASOS = [
    dict(id="S1", uso="cocheras",     h=0.24, h_cap=0.40, g=6.50, q=3.00,
         l1=7.875, l2=7.0, notas="capitel 0.40 en cada pilar"),
    dict(id="S2", uso="cocheras",     h=0.24, h_cap=0.40, g=6.50, q=3.00,
         l1=7.875, l2=7.0, notas="idéntica a S1 (se documenta)"),
    dict(id="S3", uso="cocheras",     h=0.24, h_cap=0.40, g=6.50, q=3.00,
         l1=7.875, l2=7.0, notas="idéntica a S1 (se documenta)"),
    dict(id="PB", uso="comercial",    h=0.23, h_cap=0.40, g=7.25, q=3.00,
         l1=7.875, l2=7.0, notas="drop panel 0.40 (gran luz)"),
    dict(id="PT-A", uso="residencial", h=0.19, h_cap=0.0, g=7.25, q=1.50,
         l1=7.875, l2=7.0, notas="pozos de luz A/B en bordes"),
    dict(id="PT-B", uso="residencial", h=0.19, h_cap=0.0, g=7.25, q=1.50,
         l1=7.875, l2=7.0, notas="misma losa estructural que PT-A"),
    dict(id="PT-C", uso="residencial", h=0.19, h_cap=0.0, g=7.25, q=1.50,
         l1=7.875, l2=7.0, notas="misma losa estructural que PT-A"),
    dict(id="AZ", uso="azotea",       h=0.30, h_cap=0.0, g=9.50, q=1.00,
         l1=7.875, l2=7.0, notas="piscina 15 + tanques 10 kN/m² (zonas locales)"),
]

# Cargas locales AZOTEA (kN/m² sobre su huella)
PISCINA_q = 15.0     # agua 1,5 m × 10 kN/m³
TANQUE_q = 10.0      # agua 9,2 + estructura

# Columnas (ancho c para punzonamiento) — provisional 90 cm
C_COL = 0.90


# ──────────────────────────────────────────────────────────────────
# CÁLCULO POR CASO
# ──────────────────────────────────────────────────────────────────
def calcular_caso(c):
    res = dict(c)
    g, q, h = c["g"], c["q"], c["h"]
    l1, l2 = c["l1"], c["l2"]

    # ---- 1. Verificación de espesor (PT: L/45–L/48) ----
    h_lim = l1 / 45.0
    res["h_L45"] = round(h_lim, 3)
    res["h_ok"] = h >= h_lim

    # ---- 2. Cargas de diseño ----
    res["gq_s"] = round(g + q, 2)                     # servicio
    res["U_nbr"] = round(1.4 * g + 1.4 * q, 2)        # NBR 8681
    res["U_asce"] = round(1.2 * g + 1.6 * q, 2)       # ASCE 7-22

    # ---- 3. Momentos (EFM/DDM) — dirección X (l1) ----
    ln = l1 - C_COL                                  # luz libre
    Mo_s = (g + q) * l2 * ln ** 2 / 8.0              # servicio (kN·m)
    Mo_u = (1.4 * (g + q)) * l2 * ln ** 2 / 8.0      # mayorada NBR (kN·m)
    res["ln"] = round(ln, 3)
    res["Mo_servicio"] = round(Mo_s, 1)
    res["Mo_mayorado_NBR"] = round(Mo_u, 1)

    # Distribución DDM (interior, sin vigas) — ACI Tabla 8.10.5.1
    M_neg_int = 0.75 * Mo_u
    M_pos = 0.63 * Mo_u
    res["M_neg_int"] = round(M_neg_int, 1)
    res["M_pos"] = round(M_pos, 1)

    # Franja de columna (ancho l2/2) vs franja central (l2/2)
    col_neg = 0.75 * M_neg_int                      # % franja columna
    col_pos = 0.60 * M_pos
    res["m_col_neg"] = round(col_neg / (l2 / 2), 1)   # kN·m/m franja columna
    res["m_col_pos"] = round(col_pos / (l2 / 2), 1)
    res["m_mid_neg"] = round((M_neg_int - col_neg) / (l2 / 2), 1)
    res["m_mid_pos"] = round((M_pos - col_pos) / (l2 / 2), 1)

    # ---- 4. Postensado (PTI — método de carga balanceada) ----
    # Drape máx. en losa plana ≈ h − 2·recubrimiento − Øtendón ≈ h − 0,055 m
    sag = max(0.10, h - 0.055)                       # flecha del tendón (m)
    w_bal = 0.50 * g                                 # balancear 50% del peso propio
    F_req = w_bal * l2 * l1 ** 2 / (8.0 * sag)       # kN (por dirección X)
    n_tend = F_req / F_TENDON
    sigma_pc = F_req / (l2 * h) / 1000.0             # MPa (precompresión)
    res["w_bal"] = round(w_bal, 2)
    res["sag"] = round(sag, 3)
    res["F_req"] = round(F_req, 1)
    res["n_tendones"] = round(n_tend, 1)
    res["separacion"] = round(l2 / max(n_tend, 1.0), 2)   # m
    res["sigma_pc"] = round(sigma_pc, 2)
    res["sigma_ok"] = sigma_pc <= 0.45 * FC          # σ ≤ 0.45 f'c

    # ---- 5. Punzonamiento (ACI §22.6.5.2) ----
    d = h + (c["h_cap"] if c["h_cap"] else 0.0) - 0.04   # d efectivo en el pilar
    Vu = res["U_nbr"] * (l1 * l2 - C_COL ** 2)       # kN
    bo = 4.0 * (C_COL + d)                           # perímetro crítico (m)
    beta_c = 1.0                                     # pilar cuadrado
    lam = 1.0
    vc1 = (0.17 + 0.33 / beta_c) * lam * np.sqrt(FC)   # MPa
    vc3 = 0.33 * lam * np.sqrt(FC)
    # vc2 (interior, αs=40):
    alpha_s = 40
    vc2 = (0.17 + 0.083 * alpha_s * d / bo) * lam * np.sqrt(FC)
    vc = min(vc1, vc2, vc3)                          # MPa
    Vc = vc * bo * d * 1000.0                        # kN (bo,d en m → ×1000)
    res["d_efectivo"] = round(d, 3)
    res["Vu"] = round(Vu, 1)
    res["bo"] = round(bo, 2)
    res["vc"] = round(vc, 2)
    res["Vc"] = round(Vc, 0)
    res["phiVc"] = round(PHI_CORTANTE * Vc, 0)
    res["punzonamiento_ok"] = PHI_CORTANTE * Vc >= Vu
    res["ratio_punz"] = round(Vu / (PHI_CORTANTE * Vc), 3)

    # ---- 6. Flechas ELS (L/480) ----
    res["L480"] = round(l1 / 0.48, 2)                # = 100·l1/480... en cm
    res["flecha_limite_m"] = round(l1 / 480.0, 4)
    res["flecha_ok"] = h >= l1 / 480.0

    # ---- 7. Reacción al pilar (N acumulada) ----
    res["N_servicio_pilar"] = round((g + q) * l1 * l2, 1)   # kN (un nivel)

    # Cargas locales azotea (para la zona de piscina/tanques)
    if c["id"] == "AZ":
        res["q_zona_piscina"] = round(g + q + PISCINA_q, 1)  # 25,5 kN/m²
        res["q_zona_tanque"] = round(g + q + TANQUE_q, 1)    # 20,5 kN/m²
    return res


def linea_memoria(c):
    L = []
    L.append(f"\n{'='*70}")
    L.append(f"CASO {c['id']} — LOSA {c['uso'].upper()}  (h={c['h']} m)")
    L.append(f"{'='*70}")
    L.append(f"  Notas: {c['notas']}")
    L.append(f"  Panel: l1={c['l1']} m × l2={c['l2']} m · ln={c['ln']} m")
    L.append(f"  Espesor: h={c['h']} m ≥ L/45={c['h_L45']} m  →  "
             f"{'OK' if c['h_ok'] else 'NO CUMPLE'}")
    L.append(f"  Cargas: g={c['g']} + q={c['q']} = {c['gq_s']} kN/m² (servicio)")
    L.append(f"          U_NBR={c['U_nbr']} kN/m² · U_ASCE={c['U_asce']} kN/m²")
    L.append(f"  Momentos (dirección X, EFM/DDM):")
    L.append(f"    Mo servicio = {c['Mo_servicio']} kN·m | "
             f"Mo mayorado (NBR) = {c['Mo_mayorado_NBR']} kN·m")
    L.append(f"    M neg int = {c['M_neg_int']} kN·m (col {c['m_col_neg']} "
             f"/ mid {c['m_mid_neg']} kN·m·m⁻¹)")
    L.append(f"    M positivo = {c['M_pos']} kN·m (col {c['m_col_pos']} "
             f"/ mid {c['m_mid_pos']} kN·m·m⁻¹)")
    L.append(f"  Postensado (PTI, balancear {c['w_bal']} kN/m² = 50% g):")
    L.append(f"    F requerido = {c['F_req']} kN → {c['n_tendones']} tendones "
             f"0.6\" a {c['separacion']} m (sag {c['sag']} m)")
    L.append(f"    Precompresión σ = {c['sigma_pc']} MPa "
             f"{'≤ 0.45f\'c ✓' if c['sigma_ok'] else '> 0.45f\'c ✗'}")
    L.append(f"  Punzonamiento (ACI §22.6.5.2):")
    L.append(f"    d={c['d_efectivo']} m · bo={c['bo']} m · vc={c['vc']} MPa")
    L.append(f"    Vu={c['Vu']} kN vs φVc={c['phiVc']} kN → "
             f"{'OK' if c['punzonamiento_ok'] else 'REQUIERE CAPITEL/REFUERZO'}"
             f" (ratio {c['ratio_punz']})")
    L.append(f"  Flechas ELS: h={c['h']} m ≥ L/480={c['flecha_limite_m']} m → "
             f"{'OK' if c['flecha_ok'] else 'AUMENTAR ESPESOR'}")
    if "q_zona_piscina" in c:
        L.append(f"  Zona local AZ: piscina q={c['q_zona_piscina']} kN/m² · "
                 f"tanque q={c['q_zona_tanque']} kN/m² (chequeo local)")
    return "\n".join(L)


if __name__ == "__main__":
    resultados = [calcular_caso(c) for c in CASOS]

    # CSV resumen
    cols = ["id", "uso", "h", "gq_s", "U_nbr", "Mo_mayorado_NBR",
            "m_col_neg", "m_col_pos", "n_tendones", "sigma_pc",
            "Vu", "phiVc", "ratio_punz", "punzonamiento_ok", "flecha_ok"]
    with open(os.path.join(OUT, "losas_resultados.csv"), "w", newline="",
              encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in resultados:
            w.writerow([r[k] for k in cols])
    print(f"[OK] {os.path.join(OUT, 'losas_resultados.csv')}")

    # Memoria detallada por caso
    with open(os.path.join(OUT, "losas_por_caso.txt"), "w", encoding="utf-8") as f:
        for r in resultados:
            f.write(linea_memoria(r) + "\n")
    print(f"[OK] {os.path.join(OUT, 'losas_por_caso.txt')}")

    # Gráfica comparativa de momentos
    ids = [r["id"] for r in resultados]
    mo = [r["Mo_mayorado_NBR"] for r in resultados]
    fig, ax = plt.subplots(figsize=(11, 5))
    b = ax.bar(ids, mo, color="#2563eb", edgecolor="#1e3a8a")
    ax.set_ylabel("Momento estático total mayorado Mo [kN·m]")
    ax.set_xlabel("Tipo de losa")
    ax.set_title("MOMENTO ESTÁTICO TOTAL MAYORADO POR TIPO DE LOSA (EFM/DDM · NBR 8681)\n"
                 "Mo = 1,4·(g+q)·l₂·ln²/8 · panel representativo",
                 fontsize=10, fontweight="bold")
    for rect, v in zip(b, mo):
        ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 2,
                f"{v:.0f}", ha="center", fontsize=8, fontweight="bold")
    ax.grid(True, axis="y", ls=":", alpha=0.5)
    plt.tight_layout()
    png = os.path.join(OUT, "losas_momentos_por_caso.png")
    plt.savefig(png, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[OK] {png}")

    # Resumen por consola
    for r in resultados:
        pz = "OK" if r["punzonamiento_ok"] else "NO"
        fl = "OK" if r["flecha_ok"] else "NO"
        print(f"  {r['id']:5s} h={r['h']:.2f} g+q={r['gq_s']:5.2f} "
              f"Mo={r['Mo_mayorado_NBR']:6.1f} kN·m  tendones={r['n_tendones']:4.1f} "
              f"punz={pz}({r['ratio_punz']}) flecha={fl}")
