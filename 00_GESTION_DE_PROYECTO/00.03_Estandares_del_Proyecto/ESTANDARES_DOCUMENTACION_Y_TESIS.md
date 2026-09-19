# Estándar de Redacción Académica y Documentación Técnica de Tesis

> **Documento de Gestión:** `00_GESTION_DE_PROYECTO/00.03_Estandares_del_Proyecto/ESTANDARES_DOCUMENTACION_Y_TESIS.md`  
> **Estado:** Obligatorio · **Versión:** 2.0

---

## 1. Formato General del Documento de Tesis (Word / LaTeX)

- **Extensión Objetivo:** **~200–300 Páginas** de contenido técnico riguroso.
- **Idioma:** Español técnico impersonal (tercera persona: *"se calculó"*, *"se determinó"*).
- **Tipografía:** Arial 11 pt o Times New Roman 12 pt.
- **Interlineado:** 1.5 líneas.
- **Márgenes:** Izquierdo 3.0 cm, Superior 2.5 cm, Inferior 2.5 cm, Derecho 2.5 cm.

---

## 2. Rigor Matemático y Formulación (KaTeX / LaTeX)

- Todas las ecuaciones deben estar numeradas correlativamente por capítulo:
  $$\gamma_z = \frac{1}{1 - \frac{\Delta M_{2a}}{M_{1a}}} \le 1.10 \tag{6.12}$$
- Declarar siempre las unidades en el Sistema Internacional (SI): kN, MPa, m, s, kg, °C.

---

## 3. Estándar de Figuras y Gráficos

- **Salidas Python:** Resolución mínima 300 DPI (`dpi=300`), formato PNG con paleta de colores legibles en modo impreso y oscuro.
- **Epígrafes:** *"Figura X.Y — Título descriptivo completo"*. Fuente citada al pie de cada figura.

---

## 4. Trazabilidad de Datos (Excel ↔ Word)

- **Cero datos inventados:** Todo número citado en la tesis escrita debe provenir de un script Python o de una celda de las planillas de cálculo oficiales en `06_Estructura/calculo/outputs/`.
