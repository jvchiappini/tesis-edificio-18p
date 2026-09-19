"""
====================================================================
 VERIFICACIÓN POR EMPARRILLADO (GRID) DE LA LOSA NERVADA RETICULAR
 Edificio de Uso Mixto 18P + 3 Subsuelos | Ciudad del Este, Paraguay
====================================================================

 Verifica con PyNite (emparrillado de nervios) el reparto BIDIRECCIONAL
 de cargas de la losa reticular, comparando el momento de tramo por
 nervio con el metodo manual (reparto qx+qy con regla L^4).

 Modelo: panel rectangular (Lx x Ly) con nervios cada ~0.60 m en las
 dos direcciones, apoyado simplemente en los 4 bordes, carga ultima
 qu aplicada en los nodos (tributaria). Se extrae el momento positivo
 maximo en la direccion X y en la direccion Y.

 SALIDA: calculo/outputs/grillage_paneles.csv + JSON
====================================================================
"""

import csv
import json
import math
import os

from Pynite import FEModel3D

FC = 30.0
FY = 500.0
GAMMA = 25.0
PHI_FLEX = 0.90
PHI_CORT = 0.75
REC = 0.025
EST = 0.008
SEP = 0.60
NERVIO_W = 0.10
CAPA = 0.10
CANTO = 0.35

EC = 4700.0 * math.sqrt(FC)  # MPa
IG_T = 0.00072               # inercia bruta seccion T (m4), de losas_nervadas.py
A_RIB = NERVIO_W * CANTO     # m2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")


def area_tributaria(px, py, dx, dy, Lx, Ly):
    """Factor de tributaria para un nodo: 1 interior, 0.5 borde, 0.25 esquina."""
    fx = 1.0
    if abs(px) < 1e-9 or abs(px - Lx) < 1e-9:
        fx = 0.5
    fy = 1.0
    if abs(py) < 1e-9 or abs(py - Ly) < 1e-9:
        fy = 0.5
    return dx * dy * fx * fy


def emparrillado(Lx, Ly, qu, n_x=None, n_y=None):
    """Empanillado de nervios del panel; devuelve Mx+ y My+ maximos."""
    n_x = n_x or max(5, round(Lx / SEP))
    n_y = n_y or max(5, round(Ly / SEP))
    dx = Lx / n_x
    dy = Ly / n_y

    e = EC * 1e6                       # kPa
    gmod = e / (2.0 * (1 + 0.2))
    model = FEModel3D()
    nodes = {}
    nid = 0
    for i in range(n_x + 1):
        for j in range(n_y + 1):
            x, y = i * dx, j * dy
            nodes[(i, j)] = f"N{nid}"
            model.add_node(f"N{nid}", x, y, 0.0)
            nid += 1

    model.add_material("CONC", e, gmod, 0.2, 24.0)
    model.add_section("RIB", A_RIB, IG_T, 1e-6, 1e-5)

    # vigas en X
    for j in range(n_y + 1):
        for i in range(n_x):
            model.add_member(f"X{i}_{j}", nodes[(i, j)], nodes[(i + 1, j)],
                             "CONC", "RIB")
    # vigas en Y
    for i in range(n_x + 1):
        for j in range(n_y):
            model.add_member(f"Y{i}_{j}", nodes[(i, j)], nodes[(i, j + 1)],
                             "CONC", "RIB")

    # apoyos simples en los 4 bordes (solo traslacion vertical, restar rot
    # fuera de plano para estabilidad 2D en el plano XY)
    for (i, j), name in nodes.items():
        if i in (0, n_x) or j in (0, n_y):
            model.def_support(name, True, True, True, True, True, False)

    # cargas nodales (qu x area tributaria)
    q_total = 0.0
    for (i, j), name in nodes.items():
        at = area_tributaria(i * dx, j * dy, dx, dy, Lx, Ly)
        model.add_node_load(name, "FZ", -qu * at, case="ELU")
        q_total += qu * at

    model.add_load_combo("C-ELU", {"ELU": 1.0})
    model.analyze()

    mxs = [model.members[m].max_moment("My", "C-ELU")
           for m in model.members if m.startswith("X")]
    mys = [model.members[m].max_moment("My", "C-ELU")
           for m in model.members if m.startswith("Y")]
    mnegx = [model.members[m].min_moment("My", "C-ELU")
             for m in model.members if m.startswith("X")]
    mnegy = [model.members[m].min_moment("My", "C-ELU")
             for m in model.members if m.startswith("Y")]
    return dict(Lx=Lx, Ly=Ly, qu=qu, nx=n_x, ny=n_y,
                q_aplicada=q_total, Mx_pos=max(mxs), My_pos=max(mys),
                Mx_neg=min(mnegx), My_neg=min(mnegy))


def manual(Lx, Ly, qu):
    """Metodo manual: reparto L^4. Devuelve valores SIMPLE (wL2/8) y
    CONTINUO (M-=wL2/8, M+=9wL2/128) para comparar con el emparrillado."""
    Lx4, Ly4 = Lx ** 4, Ly ** 4
    qx = qu * Ly4 / (Lx4 + Ly4)
    qy = qu * Lx4 / (Lx4 + Ly4)
    wx = qx * SEP
    wy = qy * SEP
    return dict(qx=qx, qy=qy,
                s_Mx_pos=wx * Lx ** 2 / 8.0, s_My_pos=wy * Ly ** 2 / 8.0,
                Mx_pos=9 * wx * Lx ** 2 / 128.0,
                My_pos=9 * wy * Ly ** 2 / 128.0,
                Mx_neg=wx * Lx ** 2 / 8.0, My_neg=wy * Ly ** 2 / 8.0)


def main():
    os.makedirs(OUT, exist_ok=True)
    casos = [
        dict(id="ALA-SUR", Lx=7.875, Ly=7.0, qu=12.95),
        dict(id="CUADRADO", Lx=7.0, Ly=7.0, qu=12.95),
        dict(id="LARGO-9", Lx=7.875, Ly=9.0, qu=12.95),
    ]
    filas = []
    for c in casos:
        gr = emparrillado(c["Lx"], c["Ly"], c["qu"])
        ma = manual(c["Lx"], c["Ly"], c["qu"])
        fila = dict(id=c["id"], **{k: round(v, 3) if isinstance(v, float) else v
                                   for k, v in gr.items()},
                    **{f"m_{k}": round(v, 3) for k, v in ma.items()})
        filas.append(fila)
        print(f"[{c['id']}] panel {c['Lx']}x{c['Ly']} m, qu={c['qu']}")
        print(f"   Carga aplicada: {gr['q_aplicada']:.1f} kN "
              f"(esperada {c['qu']*c['Lx']*c['Ly']:.1f})")
        print(f"   Mx+ simple: emparrillado={gr['Mx_pos']:.2f} | "
              f"manual={ma['s_Mx_pos']:.2f} | "
              f"diff {100*(gr['Mx_pos']-ma['s_Mx_pos'])/ma['s_Mx_pos']:+.1f}%")
        print(f"   My+ simple: emparrillado={gr['My_pos']:.2f} | "
              f"manual={ma['s_My_pos']:.2f} | "
              f"diff {100*(gr['My_pos']-ma['s_My_pos'])/ma['s_My_pos']:+.1f}%")
        print(f"   qx={ma['qx']:.2f} qy={ma['qy']:.2f} "
              f"(manual continuo: Mx-={ma['Mx_neg']:.2f} Mx+={ma['Mx_pos']:.2f})")

    with open(os.path.join(OUT, "grillage_paneles.csv"), "w", newline="",
              encoding="utf-8") as f:
        cols = ["id", "Lx", "Ly", "qu", "nx", "ny", "q_aplicada",
                "Mx_pos", "My_pos", "Mx_neg", "My_neg",
                "m_qx", "m_qy", "s_Mx_pos", "s_My_pos",
                "m_Mx_pos", "m_My_pos", "m_Mx_neg", "m_My_neg"]
        w = csv.DictWriter(f, fieldnames=cols, delimiter=";",
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    with open(os.path.join(OUT, "grillage_paneles.json"), "w",
              encoding="utf-8") as f:
        json.dump(filas, f, ensure_ascii=False, indent=2)
    print("CSV:", os.path.join(OUT, "grillage_paneles.csv"))


if __name__ == "__main__":
    main()