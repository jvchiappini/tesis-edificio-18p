# D.1 — Caracterización de Cargas por Nivel

> **Etapa D › Sub-etapa 1** · **Tareas:** 3 · **Estado:** 🔲 Sin iniciar  
> Normativa: NBR 6120 (Cargas en Edificaciones) · CIRSOC 101

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task D1.1:** Realizar el avalúo detallado de cargas muertas ($g$) por m² según rubro (losa nervada, contrapiso, carpeta, revestimiento, tabiquería, cielorraso).
- [ ] **Task D1.2:** Establecer las sobrecargas de uso ($q$) por ambiente según NBR 6120 / CIRSOC 101 (residencial 2.0 kN/m², comercial 3.0-5.0 kN/m², cocheras 2.5 kN/m²).
- [ ] **Task D1.3:** Formular las combinaciones de acciones para Estados Limites Últimos (ELU: $1.4G + 1.4Q$) y Estados Limites de Servicio (ELS: $G + Q$).
- [ ] **Task D1.4:** 🌧️ **LLUVIA — Carga pluvial sobre losa de azotea (no omitir)**
  - Carga de lluvia sobre cubierta plana: **$q_{lluvia} = 0{,}25\text{ kN/m}^2$** (NBR 6120:2019 §5.3 — Cobertura inacessível) como **mínimo**.
  - Verificación de **acumulación de agua (ponding)**: si la pendiente de la azotea es $< 2\%$ o si el desagüe puede taponarse, calcular la altura de agua represada $h_w$ (ASCE 7-22 §8.3: $p_r = 0{,}0098 \cdot h_w$ kN/m²).
  - La intensidad pluvial para dimensionar el sistema de drenaje viene de **eA-8** (Curva IDF DMH/DINAC, CDE: $i \approx 80\text{–}120\text{ mm/h}$, T=10 años).
  - Esta tarea conecta con **Task G1.3** (Etapa G.1) para el diseño de bajadas pluviales PVC Ø150mm.
  - Normativa: `NBR 6120:2019 §5.3` · `ASCE 7-22 §8` · `NBR 10844:1989` (Instalações prediais de águas pluviais)

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Resumen de Cargas Permanentes ($g$)

- **Losa Nervada H=35cm (P01-P18):** $g_{propio} = 4.70\text{ kN/m}^2$.
- **Cielorraso + Revestimientos + Solados:** $g_{acabados} = 1.35\text{ kN/m}^2$.
- **Tabiquería distribuida (muros cerámicos huecos):** $g_{tab} = 1.20\text{ kN/m}^2$.
- **Carga permanente total en planta residencial:** $g_{total} = 7.25\text{ kN/m}^2$.

### 2. Sobrecargas de Uso ($q$)

- Residencias (habitaciones y estares): $2.00\text{ kN/m}^2$.
- Balcones y voladizos: $3.00\text{ kN/m}^2$.
- Escaleras y pasillos comunes: $3.00\text{ kN/m}^2$.
- Salones comerciales PB y gimnasio: $4.00\text{ kN/m}^2$.
- Subsuelos de cocheras: $2.50\text{ kN/m}^2$.
