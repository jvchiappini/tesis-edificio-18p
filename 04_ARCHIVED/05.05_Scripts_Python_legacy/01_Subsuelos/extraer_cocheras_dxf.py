"""
====================================================================
 EXTRACTOR DE COCHERAS DESDE DXF — SUBSUELO 3
 Edificio de Uso Mixto 18P + 2 Subsuelos | Ciudad del Este, Paraguay
 Metodología BIM ISO 19650 | Flujo manual en AutoCAD
====================================================================

 Lee un archivo DXF (generado por generar_dxf_subsuelo.py y editado en
 AutoCAD 2024) y extrae TODOS los rectángulos dibujados en la capa
 TESIS-COCHERAS. Genera:

   outputs/cocheras_dxf.json    → lista de bounding boxes (editable)
   outputs/cocheras_dxf.py      → STALLS_MANUALES listo para usar
                                   en ga_subsuelo_3.py
   outputs/cocheras_extraidas.png → verificación visual

 USO:
   python extraer_cocheras_dxf.py [ruta_al_dxf]

 NOTA: los rectángulos deben haberse dibujado con el comando RECTANG
 (LWPOLYLINE cerrada de 4 vértices) en la capa TESIS-COCHERAS.
 También soporta POLYLINE y 4 líneas sueltas cerrando el rectángulo.

 REQUIERE: ezdxf (pip install ezdxf)

 OUTPUT: outputs/cocheras_dxf.json, cocheras_dxf.py, cocheras_extraidas.png
====================================================================
"""

import os
import sys
import json

import ezdxf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ga_subsuelo_3 as ga

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
DEFAULT_DXF = os.path.join(OUT_DIR, "subsuelo_3_base.dxf")
JSON_PATH = os.path.join(OUT_DIR, "cocheras_dxf.json")
PY_PATH = os.path.join(OUT_DIR, "cocheras_dxf.py")
PNG_PATH = os.path.join(OUT_DIR, "cocheras_extraidas.png")

CAPA_TARGET = "TESIS-COCHERAS"


# ------------------------------------------------------------------
# Extracción de rectángulos (LWPOLYLINE / POLYLINE / LINE)
# ------------------------------------------------------------------
def bbox_polilinea(entidad):
    """Devuelve bbox (x0,y0,x1,y1) de una polilínea cerrada o None."""
    if not entidad.closed:
        return None
    if entidad.dxftype() == "LWPOLYLINE":
        puntos = [p[:2] for p in entidad.get_points()]
    elif entidad.dxftype() == "POLYLINE":
        puntos = [tuple(v.dxf.location[:2]) for v in entidad.vertices]
    else:
        return None
    if len(puntos) < 3:
        return None
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]
    return (min(xs), min(ys), max(xs), max(ys))


def rect_desde_lineas(lineas):
    """Agrupa 4 líneas en un rectángulo cerrado (bbox) o None."""
    from collections import defaultdict
    # construir grafo de puntos -> vecinos
    vecinos = defaultdict(set)
    for (x1, y1, x2, y2) in lineas:
        a, b = (round(x1, 4), round(y1, 4)), (round(x2, 4), round(y2, 4))
        vecinos[a].add(b)
        vecinos[b].add(a)
    # un rectángulo simple = 4 puntos únicos, cada uno con grado 2
    if len(vecinos) != 4:
        return None
    if any(len(v) != 2 for v in vecinos.values()):
        return None
    xs = [p[0] for p in vecinos]
    ys = [p[1] for p in vecinos]
    return (min(xs), min(ys), max(xs), max(ys))


def extraer(path):
    doc = ezdxf.readfile(path)
    msp = doc.modelspace()

    rects = []
    lineas = []
    for e in msp:
        if e.dxf.layer != CAPA_TARGET:
            continue
        if e.dxftype() in ("LWPOLYLINE", "POLYLINE"):
            r = bbox_polilinea(e)
            if r is not None:
                rects.append(r)
        elif e.dxftype() == "LINE":
            s, t = e.dxf.start, e.dxf.end
            lineas.append((s[0], s[1], t[0], t[1]))

    # Agrupar líneas sueltas en rectángulos (método greedy por extremos)
    if lineas:
        usadas = set()
        for i in range(len(lineas)):
            if i in usadas:
                continue
            grupo = [lineas[i]]
            usadas.add(i)
            crece = True
            while crece:
                crece = False
                for j in range(len(lineas)):
                    if j in usadas:
                        continue
                    for (a1, b1, a2, b2) in grupo:
                        if ((lineas[j][0] == a1 and lineas[j][1] == b1) or
                                (lineas[j][2] == a1 and lineas[j][3] == b1) or
                                (lineas[j][0] == a2 and lineas[j][1] == b2) or
                                (lineas[j][2] == a2 and lineas[j][3] == b2)):
                            grupo.append(lineas[j])
                            usadas.add(j)
                            crece = True
                            break
                    if crece:
                        break
            if len(grupo) == 4:
                r = rect_desde_lineas(grupo)
                if r is not None:
                    rects.append(r)

    # Normalizar: redondear, eliminar duplicados, descartar fuera de rango
    vistos = set()
    norm = []
    descartados = []
    for (x0, y0, x1, y1) in rects:
        x0, y0 = round(min(x0, x1), 3), round(min(y0, y1), 3)
        x1, y1 = round(max(x0, x1), 3), round(max(y0, y1), 3)
        clave = (x0, y0, x1, y1)
        if clave in vistos:
            continue
        vistos.add(clave)
        w, h = x1 - x0, y1 - y0
        if w < 0.8 or h < 0.8:
            descartados.append((x0, y0, x1, y1, "menor a 0.8 m"))
            continue
        if w > 12 or h > 12:
            descartados.append((x0, y0, x1, y1, "mayor a 12 m (zona, no cochera?)"))
            continue
        norm.append(dict(x0=x0, y0=y0, w=round(w, 3), h=round(h, 3)))

    # Ordenar: por fila (Y) luego columna (X)
    norm.sort(key=lambda s: (round(s["y0"], 1), s["x0"]))
    return norm, descartados


# ------------------------------------------------------------------
# Verificación de solapes (con pilares, núcleos, rampas, otras cocheras)
# ------------------------------------------------------------------
def rect_overlap(a, b):
    return not (a["x1"] <= b["x0"] or b["x1"] <= a["x0"] or
                a["y1"] <= b["y0"] or b["y1"] <= a["y0"])


def verificar(stalls):
    avisos = []

    pilares, _ = ga.generar_pilares()
    bloques = []
    bloques += [dict(x0=c["x0"], x1=c["x1"], y0=c["y0"], y1=c["y1"], nombre="NUCLEO " + c["nombre"])
                for c in ga.NUCLEOS]
    bloques += [dict(x0=ga.RAMPA_ENTRADA["x0"], x1=ga.RAMPA_ENTRADA["x1"],
                     y0=ga.RAMPA_ENTRADA["y0"], y1=ga.RAMPA_ENTRADA["y1"], nombre="Rampa Entrada SE")]
    bloques += [dict(x0=ga.RAMPA_SALIDA["x0"], x1=ga.RAMPA_SALIDA["x1"],
                     y0=ga.RAMPA_SALIDA["y0"], y1=ga.RAMPA_SALIDA["y1"], nombre="Rampa Salida NO")]
    for (px0, py0, w, h) in pilares:
        bloques.append(dict(x0=px0, x1=px0 + w, y0=py0, y1=py0 + h, nombre="Pilar"))

    for i, s in enumerate(stalls):
        r = dict(x0=s["x0"], x1=s["x0"] + s["w"], y0=s["y0"], y1=s["y0"] + s["h"])
        for b in bloques:
            if rect_overlap(r, b):
                avisos.append(f"Cochera {i} (x={s['x0']:.2f}, y={s['y0']:.2f}) SOLAPA con {b['nombre']}")

    # Solapes entre cocheras
    for i in range(len(stalls)):
        ri = dict(x0=stalls[i]["x0"], x1=stalls[i]["x0"] + stalls[i]["w"],
                  y0=stalls[i]["y0"], y1=stalls[i]["y0"] + stalls[i]["h"])
        for j in range(i + 1, len(stalls)):
            rj = dict(x0=stalls[j]["x0"], x1=stalls[j]["x0"] + stalls[j]["w"],
                      y0=stalls[j]["y0"], y1=stalls[j]["y0"] + stalls[j]["h"])
            if rect_overlap(ri, rj):
                avisos.append(f"Cocheras {i} y {j} se SOLAPAN")

    return avisos


# ------------------------------------------------------------------
# Exportación
# ------------------------------------------------------------------
def exportar(stalls, path):
    os.makedirs(OUT_DIR, exist_ok=True)
    n = len(stalls)
    area = sum(s["w"] * s["h"] for s in stalls)
    lines = [
        "#" + "=" * 79,
        f"# COCHERAS EXTRAIDAS DEL DXF — {n} plazas | área {area:.1f} m2",
        "#" + "=" * 79,
        "# Para usar en ga_subsuelo_3.py:",
        "#   from cocheras_dxf import STALLS_MANUALES",
        "#   (reemplazar la lógica de generar_stalls por esta lista)",
        "STALLS_MANUALES = [",
    ]
    for s in stalls:
        lines.append(f"    dict(x0={s['x0']:.3f}, y0={s['y0']:.3f}, "
                     f"w={s['w']:.3f}, h={s['h']:.3f}),")
    lines.append("]")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def graficar(stalls, path):
    """Genera PNG de verificación sobre el esqueleto del subsuelo."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    fig, ax = plt.subplots(figsize=(22, 12))
    ax.set_facecolor('#f1f5f9')
    ax.add_patch(Rectangle((ga.X_MIN, ga.Y_MIN), ga.X_MAX - ga.X_MIN, ga.Y_MAX - ga.Y_MIN,
                           facecolor='#e2e8f0', edgecolor='#0f172a', lw=2.5, zorder=2))

    for z in ga.ZONAS_PARKING:
        ax.add_patch(Rectangle((z['x0'], z['y0']), z['x1'] - z['x0'], z['y1'] - z['y0'],
                               facecolor='none', edgecolor='#94a3b8', ls=':', lw=1.2, zorder=3))

    pilares, _ = ga.generar_pilares()
    for (px0, py0, w, h) in pilares:
        ax.add_patch(Rectangle((px0, py0), w, h, facecolor='#f8fafc',
                               edgecolor='#0f172a', lw=0.8, zorder=6))

    for rampa, nombre in [(ga.RAMPA_ENTRADA, "R ENTRADA SE"), (ga.RAMPA_SALIDA, "R SALIDA NO")]:
        ax.add_patch(Rectangle((rampa['x0'], rampa['y0']),
                               rampa['x1'] - rampa['x0'], rampa['y1'] - rampa['y0'],
                               facecolor='#f97316', edgecolor='#c2410c', hatch='//',
                               alpha=0.85, zorder=5))

    p = ga.PASILLO_TECNICO
    ax.add_patch(Rectangle((p['x0'], p['y0']), p['x1'] - p['x0'], p['y1'] - p['y0'],
                           facecolor='#a5b4fc', edgecolor='#4338ca', hatch='..', alpha=0.7, zorder=5))

    for c in ga.NUCLEOS:
        ax.add_patch(Rectangle((c['x0'], c['y0']), c['x1'] - c['x0'], c['y1'] - c['y0'],
                               facecolor='#334155', edgecolor='#0f172a', lw=2.5, zorder=7))

    for x in ga.XS:
        ax.plot([x, x], [ga.Y_MIN - 1.5, ga.Y_MAX + 1.5], color='#64748b', lw=0.8, ls='--', zorder=1)
    for y in ga.YS:
        ax.plot([ga.X_MIN - 1.5, ga.X_MAX + 1.5], [y, y], color='#64748b', lw=0.8, ls='--', zorder=1)

    for s in stalls:
        ax.add_patch(Rectangle((s['x0'] + 0.05, s['y0'] + 0.05), s['w'] - 0.1, s['h'] - 0.1,
                               facecolor='#86efac', edgecolor='#166534', lw=1.0, zorder=4))

    ax.set_xlim(ga.X_MIN - 7, ga.X_MAX + 4)
    ax.set_ylim(ga.Y_MIN - 6, ga.Y_MAX + 3)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title(f"COCHERAS EXTRAIDAS DEL DXF — {len(stalls)} plazas", fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


# ------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DXF
    if not os.path.exists(path):
        print(f"[ERROR] No existe el DXF: {path}")
        print(f"        Ejecute primero: python generar_dxf_subsuelo.py")
        sys.exit(1)

    stalls, descartados = extraer(path)
    avisos = verificar(stalls)

    exportar(stalls, PY_PATH)
    with open(JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(stalls, fh, ensure_ascii=False, indent=1)
    graficar(stalls, PNG_PATH)

    print(f"[OK] DXF leído: {path}")
    print(f"[OK] Cocheras extraídas: {len(stalls)}")
    area = sum(s['w'] * s['h'] for s in stalls)
    print(f"[OK] Área total: {area:.1f} m2")
    print(f"[OK] JSON  -> {JSON_PATH}")
    print(f"[OK] PY    -> {PY_PATH}")
    print(f"[OK] PNG   -> {PNG_PATH}")

    if descartados:
        print("\n[AVISO] Rectángulos descartados:")
        for (x0, y0, x1, y1, razon) in descartados:
            print(f"   ({x0:.2f},{y0:.2f})-({x1:.2f},{y1:.2f}): {razon}")

    if avisos:
        print("\n[AVISO] Posibles problemas:")
        for a in avisos:
            print(f"   {a}")
    else:
        print("\nSin solapes detectados (pilares, núcleos, rampas ni otras cocheras).")


if __name__ == "__main__":
    main()
