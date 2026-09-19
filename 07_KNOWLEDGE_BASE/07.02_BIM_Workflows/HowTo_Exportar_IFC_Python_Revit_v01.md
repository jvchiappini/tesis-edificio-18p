# HowTo — Exportar Modelo Estructural Python a IFC4 para Revit 2024

**Versión:** v02 (2026-09-10) · **Software:** Python 3.13 + ifcopenshell 0.8.5 · **Revit:** 2024

> Flujo BIM (ISO 19650): geometría de cálculo (Python) → IFC4 → Revit 2024 / Navisworks.
> Script de referencia: `05_RECURSOS/05.05_Scripts_Python/06_Estructura/calculo/exportar_ifc.py`

## Resumen

Con `ifcopenshell` (API de bajo nivel) se genera un `.ifc` IFC4 con `IfcColumn`,
`IfcSlab`, `IfcWall` y `IfcBuildingStorey`, listo para `Import/IFC` en Revit 2024
(ribbon *Insert* → *Import* → *IFC*).

## Pasos

1. **Instalar:** `python -m pip install ifcopenshell` (trae también shapely, lark, isodate…).
2. **Estructura del archivo IFC4:**
   - `IfcProject` (con `IfcUnitAssignment` y `IfcGeometricRepresentationContext`).
   - `IfcSite` → `IfcBuilding` → `IfcBuildingStorey` (relaciones `IfcRelAggregates`).
   - Elementos con `ObjectPlacement` (relativo al storey) + `Representation` (caja extruida).
   - `IfcRelContainedInSpatialStructure` asigna cada elemento a su nivel (para que Revit lo ubique bien).
3. **Geometría de caja (perfil rectangular extruido):**
   - `IfcRectangleProfileDef` (XDim, YDim) → `IfcExtrudedAreaSolid` (Depth) → `IfcShapeRepresentation` → `IfcProductDefinitionShape`.
   - El perfil queda CENTRADO en el origen; la posición la define el `IfcLocalPlacement` del elemento.

## Trampas (importante)

| Trampa | Solución |
|---|---|
| `IfcCartesianPoint` rechaza int/tuple | Pasar `[float(x), float(y), float(z)]` |
| **`IfcAxis2Placement2D.Location` DEBE ser un punto 2D** | Usar `IfcCartesianPoint([x, y])` (2 coords). Un punto 3D hace que **Revit 2024 crashee** (error irrecuperable, excepción .NET `0xe0434352`) al abrir el IFC. `ifcopenshell` lo tolera pero Revit NO. |
| `IfcExtrudedAreaSolid.ExtrudedDirection` es OBLIGATORIO | Crear `IfcDirection([0,0,1])` (eje Z) |
| `createIfcShapeRepresentation` en ifcopenshell | El primer argumento es **ContextOfItems**, luego "Body", "SweptSolid", items |
| `createIfcProject` y entidades Root | Incluir SIEMPRE el `OwnerHistory` (posición 2); crearlo con `IfcPersonAndOrganization` + `IfcApplication` |
| `IfcOwnerHistory.ChangeAction` | En **IFC2X3** es OBLIGATORIO ("ADDED"); en IFC4 es opcional. Pasar siempre el valor para ambos esquemas |
| Orden de atributos `create_entity("IfcColumn", ...)` | GlobalId, OwnerHistory, Name, Description, ObjectType, ObjectPlacement, Representation, Tag, [PredefinedType]. En IFC2x3 solo 8 (sin PredefinedType); pasar 8 args funciona para ambos |
| Unidades | Registrar m, m², m³, N, Pa en `IfcUnitAssignment` |

## Crash de Revit al abrir IFC (diagnóstico)

Síntoma: Revit 2024 muestra "Se ha producido un error irrecuperable" al abrir el `.ifc`.
Verificado en el journal de Revit (`%LOCALAPPDATA%\Autodesk\Revit\Autodesk Revit 2024\Journals\journal.00XX.txt`):
excepción .NET `ExceptionCode=0xe0434352` justo tras seleccionar el archivo. En Visor de eventos
(Aplicación, Id 1023, .NET Runtime): "el proceso terminó debido a un error interno en el runtime de .NET… 80131506".
Causa raíz en este proyecto: los `IfcAxis2Placement2D` de los perfiles usaban un `IfcCartesianPoint`
**3D** `(0.,0.,0.)` en vez de **2D** `(0.,0.)` (función auxiliar `_cp` reutilizada para ambos).
IfcOpenShell lo acepta (validate = 0 errores), pero el importador de Revit es estricto y crashea.

## Fallback IFC2x3 (recomendado por Autodesk)

Autodesk recomienda **IFC2x3 Coordination View 2.0** para los mejores resultados al ABRIR
en Revit ("Revit IFC Manual"). El script permite exportar ambos esquemas:

```
python exportar_ifc.py            # → edificio_18p_estructura.ifc        (IFC4)
python exportar_ifc.py --ifc2x3   # → edificio_18p_estructura_v2x3.ifc  (IFC2X3)
```

Si el IFC4 aún fallara, probar el IFC2x3. También se recomienda **Insert → Link IFC**
(menos robusto que abrir, y si el crash es del importador, aplicar primero la corrección de arriba).

## Buenas prácticas

- Exportar los pilares por **tramo de sección** (máx. 4 tramos/pilar: 90→80→70→60 cm), NO por cada 3 m, para no saturar Revit (288 vs 1656 instancias).
- Validar siempre reabriendo el `.ifc`: `ifcopenshell.open(ruta)` y contar `by_type(...)`.
- No exportar cargas/masas como elementos estructurales: usar `IfcBuildingElementProxy` (tanques, piscina) solo para visualización.

## Resultado (edificio 18P + 3 subsuelos)

`outputs/edificio_18p_estructura.ifc` → IFC4 · 23 storeys · 288 columnas · 23 losas · 2 muros · 3 proxies.
`outputs/edificio_18p_estructura_v2x3.ifc` → IFC2X3 (fallback para Revit).