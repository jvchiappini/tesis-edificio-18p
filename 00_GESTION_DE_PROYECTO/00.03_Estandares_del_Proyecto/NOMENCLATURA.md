# Estándar de Nomenclatura de Archivos del Proyecto (ISO 19650)

> **Documento de Gestión:** `00_GESTION_DE_PROYECTO/00.03_Estandares_del_Proyecto/NOMENCLATURA.md`  
> **Estado:** Obligatorio · **Versión:** 2.0 (Edificio 18P + 3 Subsuelos)

---

## 1. Regla General de Codificación

Todos los archivos generados en este proyecto (modelos 3D, planos DWG/PDF, memorias de cálculo, planillas de cómputo, scripts y documentos académicos) deben nombrarse de manera estricta bajo la convención paramétrica:

$$\text{TESIS-}[DISCIPLINA]-[NIVEL]-[TIPO]-[NUMERO]$$

---

## 2. Códigos de Disciplina (`[DISCIPLINA]`)

| Código | Disciplina | Ámbito / Contenido |
|---|---|---|
| **ARQ** | Arquitectura | Plantas, cortes, fachadas, detalles de albañilería, acabados |
| **EST** | Estructura | Pilares, losas nervadas, vigas spandrel, núcleos H°A°, fundaciones |
| **SAN** | Instalación Sanitaria | Agua fría, agua caliente (ACS), cisternas y presurización |
| **CLO** | Instalación Cloacal | Bajadas cloacales, colectores, cámaras sépticas y EBAR |
| **PLU** | Instalación Pluvial | Drenaje de azotea, bajadas pluviales y pozo de bombeo |
| **ELE** | Instalación Eléctrica | Subestación ANDE 60m², tableros, grupo electrógeno, bandejas |
| **INC** | Protección Contra Incendios | Reserva PCI, rociadores (Sprinklers), hidrantes, presurización |
| **MEC** | Instalación Mecánica / HVAC | Transporte vertical (ascensores), HVAC locales y extracción CO |
| **COORD** | Coordinación BIM | Modelos federados NWD/IFC, matriz de clash detection |

---

## 3. Códigos de Nivel (`[NIVEL]`)

| Código | Nivel del Edificio | Cota de Referencia |
|---|---|---|
| **SUB3** | Subsuelo 3 (Cocheras) | Cota -10.50 m |
| **SUB2** | Subsuelo 2 (Cocheras) | Cota -7.00 m |
| **SUB1** | Subsuelo 1 (Cocheras + Bloque Técnico) | Cota -3.50 m |
| **PB** | Planta Baja (Comercial + Lobby + RSU) | Cota ±0.00 m |
| **P01** – **P18** | Plantas Tipo Residenciales 01 a 18 | Cota +4.00 m a +60.95 m |
| **AZ** | Azotea Técnica + Amenities (Piscina/SUM) | Cota +64.30 m |
| **GEN** | General (Modelos completos, ejes, memorias) | Múltiples niveles |

---

## 4. Códigos de Tipo de Documento (`[TIPO]`)

| Código | Tipo de Entregable | Formatos de Archivo Asociados |
|---|---|---|
| **M3** | Modelo 3D Paramétrico | `.rvt`, `.ifc`, `.nwc`, `.nwd` |
| **DR** | Drawing / Plano 2D | `.dwg`, `.pdf` |
| **SC** | Schedule / Tabla / Cómputo | `.xlsx`, `.csv`, `.json` |
| **RP** | Reporte / Memoria Descriptiva | `.docx`, `.pdf`, `.md` |
| **CALC** | Memoria / Script de Cálculo | `.py`, `.tex`, `.pdf`, `.xlsx` |
| **SCRIPT** | Script de Automatización | `.py`, `.dyn` (Dynamo), `.js` |

---

## 5. Correlativo (`[NUMERO]`)

- Número correlativo de **3 dígitos** (`001`, `002`, `003`, ...) por combinación única de Disciplina, Nivel y Tipo.

---

## 6. Ejemplos de Aplicación Ejecutiva

- `TESIS-EST-GEN-M3-001.rvt`: Modelo estructural 3D completo en Revit 2024.
- `TESIS-ARQ-PB-DR-001.pdf`: Plano de distribución arquitectónica de Planta Baja.
- `TESIS-EST-P05-CALC-001.py`: Script de cálculo de losa nervada para la Planta Tipo P05.
- `TESIS-COORD-GEN-RP-001.pdf`: Informe final de Clash Detection en Navisworks.
- `TESIS-SAN-SUB1-DR-002.dwg`: Plano de distribución sanitaria en Subsuelo 1.
