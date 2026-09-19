# Estándar de Modelado BIM y Coordinación (ISO 19650)

> **Documento de Gestión:** `00_GESTION_DE_PROYECTO/00.03_Estandares_del_Proyecto/ESTANDARES_BIM_Y_MODELADO.md`  
> **Estado:** Obligatorio · **Versión:** 2.0

---

## 1. Software y Entorno BIM

- **BIM Autoría:** Autodesk Revit 2024 (Build `24.3.60.12`, Update 3, x64).
- **Idioma de Interfaz:** Inglés (`US English`). Todos los parámetros y nombres de familias deben mantenerse en terminología técnica internacional.
- **Coordinación y Federación:** Autodesk Navisworks Manage 2024.
- **Formato Intercambio Abierto:** IFC4 Reference View (ISO 16739).

---

## 2. Sistema de Coordenadas y Georreferenciación

- **Origen de Coordenadas Compartidas (Project Base Point / Survey Point):**
  - **Sistema de Proyección:** UTM WGS84 - Zona 21J (Hemisferio Sur).
  - **Coordenadas de Referencia Terreno (P1):** $E = 737.721,76 \text{ m}, N = 7.176.185,26 \text{ m}$.
  - **Cota De Nivel Vereda (±0.00 m):** Relativa a nivel del mar (IGAC).
  - **Rotación respecto al Norte Verdadero:** Alineado al eje longitudinal del polígono P1→P2 (Declinación -14°).

---

## 3. Matriz de Nivel de Desarrollo (LOD - Level of Development)

| Disciplina | Elemento BIM | LOD Objetivo | Tolerancia Geométrica |
|---|---|---|---|
| **Estructura** | Pilares H°A°, losas nervadas, vigas spandrel, núcleos | **LOD 350** | $\pm 5 \text{ mm}$ |
| **Arquitectura** | Cerramientos, tabiquería, carpinterías, revestimientos | **LOD 300** | $\pm 10 \text{ mm}$ |
| **Sanitaria / Cloacal** | Tuberías Ø>50mm, cisternas, bombas, colectores | **LOD 350** | $\pm 10 \text{ mm}$ |
| **Eléctrica** | Subestación ANDE, grupo electrógeno, bandejas | **LOD 300** | $\pm 15 \text{ mm}$ |
| **PCI / HVAC** | Rociadores, hidrantes, bombas, ductos de extracción | **LOD 350** | $\pm 10 \text{ mm}$ |

---

## 4. Reglas de Modelado por Disciplina

### 4.1 Estructura (EST)
- **Continuidad Vertical:** Pilares modelados tramo a tramo nivel por nivel (sin elementos continuos multisectoriales).
- **Geometría de Losas Nervadas:** Modelado con casetones plásticos 25/35 cm y capa de compresión 10 cm. Los ábacos se modelan como zonas macizas de H°A°.
- **Vigas Spandrel:** Modeladas como vigas perimetrales continuas bordeando las fachadas y pozos de luz.

### 4.2 Arquitectura (ARQ)
- Muros cerámicos y divisores modelados delimitando los recintos.
- Respetar el ancho libre de pasillos ($\ge 1.20\text{ m}$) y accesibilidad PMR.

### 4.3 Instalaciones MEP
- Cañerías con pendiente mínima (Cloacal 1.5–2.0%, Pluvial 1.0%).
- Pases técnicos en losas y nervios coordinados antes de la emisión de modelos compartidos.
