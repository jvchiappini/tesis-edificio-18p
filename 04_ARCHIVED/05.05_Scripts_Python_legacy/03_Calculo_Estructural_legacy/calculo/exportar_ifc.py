"""
====================================================================
 EXPORTADOR IFC — MODELO ESTRUCTURAL 3D → Revit 2024 / Navisworks
 Edificio 18P + 3 Subsuelos | Metodología BIM ISO 19650
====================================================================

 Convierte el inventario 3D (elementos_3d.json) a un archivo IFC4:
   - IfcColumn (pilares H°A°, secciones por grupo de niveles)
   - IfcSlab   (losas planas postensadas por nivel)
   - IfcWall   (núcleos H°A° N1/N2 como pantallas)
   - IfcBuildingElementProxy (masas de azotea: tanques + piscina)
   - IfcBuildingStorey (23 niveles: S3…AZ)

 Uso:
   python exportar_ifc.py [ruta_elementos_json]

 Salida:
   outputs/edificio_18p_estructura.ifc  (abrir en Revit 2024 → Import/IFC)
====================================================================
"""

import os
import sys
import json
import time
import ifcopenshell
import ifcopenshell.guid as guid
from ifcopenshell import file as IfcFile

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")


def _cp(f, x, y, z=0.0):
    return f.createIfcCartesianPoint([float(x), float(y), float(z)])


def _cp2(f, x, y):
    return f.createIfcCartesianPoint([float(x), float(y)])


def _axis3(f, x, y, z):
    return f.createIfcAxis2Placement3D(_cp(f, x, y, z), None, None)


def _local_placement(f, rel_to, x, y, z):
    if rel_to is None:
        return f.createIfcLocalPlacement(None, _axis3(f, x, y, z))
    return f.createIfcLocalPlacement(rel_to, _axis3(f, x, y, z))


def _extruded_box(f, dx, dy, height):
    """Representación de cuerpo: extrusión de perfil rectangular (caja).
    dx, dy = dimensiones del perfil (centrado), height = altura de extrusión.
    NOTA: el IfcAxis2Placement2D del perfil debe usar un punto 2D (IfcCartesianPoint
    de 2 coordenadas). Un punto 3D aquí es inválido según IFC y hace que el
    importador de Revit 2024 falle con un error irrecuperable (crash .NET)."""
    prof = f.createIfcRectangleProfileDef(
        "AREA", None, f.createIfcAxis2Placement2D(_cp2(f, 0, 0)),
        float(dx), float(dy))
    solid = f.createIfcExtrudedAreaSolid(
        prof, _axis3(f, 0, 0, 0),
        f.createIfcDirection([0.0, 0.0, 1.0]), float(height))
    ctx = f.by_type("IfcGeometricRepresentationContext")[0]
    shape_rep = f.createIfcShapeRepresentation(
        ctx, "Body", "SweptSolid", (solid,))
    return f.createIfcProductDefinitionShape(None, None, (shape_rep,))


def crear_ifc(elementos, schema="IFC4"):
    f = IfcFile(schema=schema)

    # ── OwnerHistory (estándar IFC; mejora la compatibilidad con Revit) ──
    persona = f.createIfcPerson(None, "BIM", "Copilot", None, None, None)
    org = f.createIfcOrganization(None, "Tesis Edificio 18P", None, None, None)
    rel_owner = f.createIfcPersonAndOrganization(persona, org, None)
    aplicacion = f.createIfcApplication(org, "0.8.5", "IfcOpenShell 0.8.5",
                                        "IFC")
    owner_history = f.createIfcOwnerHistory(
        rel_owner, aplicacion, "READWRITE", "ADDED", None, None, None,
        int(time.time()))

    # ── Unidades (m, m², m³, N, Pa) ───────────────────────────────
    units = [
        f.createIfcSIUnit(None, "LENGTHUNIT", None, "METRE"),
        f.createIfcSIUnit(None, "AREAUNIT", None, "SQUARE_METRE"),
        f.createIfcSIUnit(None, "VOLUMEUNIT", None, "CUBIC_METRE"),
        f.createIfcSIUnit(None, "FORCEUNIT", None, "NEWTON"),
        f.createIfcSIUnit(None, "PRESSUREUNIT", None, "PASCAL"),
    ]
    unit_assign = f.createIfcUnitAssignment(units)

    # ── Contexto geométrico ────────────────────────────────────────
    ctx = f.createIfcGeometricRepresentationContext(
        None, "Model", 3, 1.0e-5, _axis3(f, 0, 0, 0), None)

    # ── Proyecto ───────────────────────────────────────────────────
    project = f.createIfcProject(guid.new(), owner_history,
                                 "Edificio 18P + 3 Subsuelos",
                                 "Edificio de Uso Mixto", None, None, None,
                                 (ctx,), unit_assign)

    # ── Sitio y edificio ───────────────────────────────────────────
    site = f.createIfcSite(guid.new(), owner_history, "Site CDE",
                           "Terreno 90×40 m",
                           None, _local_placement(f, None, 0, 0, 0), None,
                           "CDE", "ELEMENT", None, None, None, None, None)
    building = f.createIfcBuilding(
        guid.new(), owner_history, "Edificio Torre",
        "Edificio 18P + 3 Subsuelos",
        None, _local_placement(f, site.ObjectPlacement, 0, 0, 0), None,
        "Torre", "ELEMENT", None, None, None)
    f.createIfcRelAggregates(guid.new(), owner_history, None, None,
                             project, (site,))
    f.createIfcRelAggregates(guid.new(), owner_history, None, None,
                             site, (building,))

    # ── Niveles (storeys) ──────────────────────────────────────────
    storeys = {}
    for nid, cota in elementos["cotas"].items():
        st = f.createIfcBuildingStorey(
            guid.new(), owner_history, nid, f"Nivel {nid}", None,
            _local_placement(f, building.ObjectPlacement, 0, 0, cota),
            None, "Nivel", "ELEMENT", float(cota))
        storeys[nid] = st
    f.createIfcRelAggregates(guid.new(), owner_history, None, None, building,
                             tuple(storeys.values()))

    def crear_elem(tipo_ifc, nombre, x, y, z0, dx, dy, altura, storey):
        """Crea un elemento tipo con caja (dx×dy×altura) en (x, y, z0)."""
        z_local = float(z0) - float(elementos["cotas"][storey.Name])
        placement = _local_placement(f, storey.ObjectPlacement, x, y, z_local)
        rep = _extruded_box(f, dx, dy, altura)
        el = f.create_entity(tipo_ifc, guid.new(), owner_history, nombre,
                             None, None, placement, rep, None)
        f.createIfcRelContainedInSpatialStructure(
            guid.new(), owner_history, None, None, (el,), storey)
        return el

    # ── Losas ──────────────────────────────────────────────────────
    for L in elementos["losas"]:
        crear_elem("IfcSlab", L["id"],
                   (L["x0"] + L["x1"]) / 2, (L["y0"] + L["y1"]) / 2,
                   L["z_top"] - L["espesor"],
                   L["x1"] - L["x0"], L["y1"] - L["y0"], L["espesor"],
                   storeys[L["nivel"]])

    # ── Pilares ────────────────────────────────────────────────────
    for P in elementos["pilares"]:
        st_key = "S3"
        for n, c in elementos["cotas"].items():
            if abs(float(c) - float(P["z0"])) < 0.01:
                st_key = n
        crear_elem("IfcColumn", P["id"], P["x"], P["y"], P["z0"],
                   P["ancho"], P["ancho"], P["z1"] - P["z0"], storeys[st_key])

    # ── Núcleos (muros) ────────────────────────────────────────────
    for C in elementos["nucleos"]:
        crear_elem("IfcWall", f"MURO_{C['id']}",
                   (C["x0"] + C["x1"]) / 2, (C["y0"] + C["y1"]) / 2,
                   C["z0"], C["x1"] - C["x0"], C["y1"] - C["y0"],
                   C["z1"] - C["z0"], storeys["S3"])

    # ── Vigas (sistema híbrido: spandrel perimetral + bordes de pozos) ──
    for B in elementos["vigas"]:
        st_key = "S3"
        for n, c in elementos["cotas"].items():
            if abs(float(c) - float(B["z1"])) < 0.01:
                st_key = n
        crear_elem("IfcBeam", B["id"],
                   (B["x0"] + B["x1"]) / 2, (B["y0"] + B["y1"]) / 2,
                   B["z0"], B["x1"] - B["x0"], B["y1"] - B["y0"],
                   B["z1"] - B["z0"], storeys[st_key])

    # ── Masas de azotea (proxy genérico) ───────────────────────────
    for M in elementos["masas"]:
        crear_elem("IfcBuildingElementProxy", M["id"],
                   (M["x0"] + M["x1"]) / 2, (M["y0"] + M["y1"]) / 2,
                   M["z0"], M["x1"] - M["x0"], M["y1"] - M["y0"],
                   M["z1"] - M["z0"], storeys["AZ"])

    return f


def main(ruta_json=None, schema="IFC4"):
    if ruta_json is None:
        ruta_json = os.path.join(OUT_DIR, "elementos_3d.json")
    with open(ruta_json, "r", encoding="utf-8") as fh:
        elementos = json.load(fh)
    modelo = crear_ifc(elementos, schema)
    os.makedirs(OUT_DIR, exist_ok=True)
    sufijo = "_v2x3" if schema == "IFC2X3" else ""
    salida = os.path.join(OUT_DIR, f"edificio_18p_estructura{sufijo}.ifc")
    modelo.write(salida)
    n_col = len(modelo.by_type("IfcColumn"))
    n_losa = len(modelo.by_type("IfcSlab"))
    n_muro = len(modelo.by_type("IfcWall"))
    n_viga = len(modelo.by_type("IfcBeam"))
    n_niv = len(modelo.by_type("IfcBuildingStorey"))
    n_proxy = len(modelo.by_type("IfcBuildingElementProxy"))
    print(f"[OK] {salida}  (schema={schema})")
    print(f"     IfcColumn={n_col} | IfcSlab={n_losa} | IfcWall={n_muro} | "
          f"IfcBeam={n_viga} | Proxy={n_proxy} | IfcBuildingStorey={n_niv}")
    return salida


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    schema = "IFC2X3" if "--ifc2x3" in sys.argv[1:] else "IFC4"
    main(args[0] if args else None, schema)