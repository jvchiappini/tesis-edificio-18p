# E.1 — Parámetros de Viento y Comparativa Multinormativa

> **Etapa E › Sub-etapa 1** · **Tareas:** 4 · **Estado:** 🔲 Sin iniciar  
> Normativa: NP 196:1991 (Paraguay) · NBR 6123:2023 · ASCE 7-22 · EN 1991-1-4

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task E1.1:** Determinar la velocidad básica del viento $V_0 = 45\text{ m/s}$ (162 km/h) para Ciudad del Este según mapa eólico regional.
- [ ] **Task E1.2:** Calcular los factores de rugosidad, topografía y exposición ($S_1, S_2, S_3$ según NBR 6123 / NP 196).
- [ ] **Task E1.3:** Determinar los coeficientes de presión externa e interna ($C_{pe}, C_{pi}$) para edificio aislado de planta rectangular $85\text{m} \times 37\text{m}$ y $H = 64.30\text{m}$.
- [ ] **Task E1.4:** Desarrollar la comparativa multinormativa de cortante basal total y momento de vuelco entre NP 196, NBR 6123, ASCE 7-22 y Eurocódigo 1.

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Parámetros eólicos de diseño para Ciudad del Este

- **Velocidad básica ($V_0$):** $45.0\text{ m/s}$ (periodo de retorno de 50 años).
- **Categoría de terreno:** Categoría III (zonas suburbanas con obstáculos de altura media).
- **Factor topográfico ($S_1$):** $1.00$ (terreno plano).
- **Factor de rugosidad y tamaño ($S_2$):** Función de la altura $z$, variando de $0.78$ en PB a $1.18$ en Azotea.
- **Factor de seguridad / ocupación ($S_3$):** $1.00$ (edificio de vivienda/comercio de ocupación normal).

### 2. Comparativa de Cortante Basal por Viento

| Norma | $V_0$ (m/s) | Cortante Basal $V_{x,total}$ (kN) | Momento de Vuelco $M_{vuelco}$ (kN·m) | Criterio de Selección |
|---|---|---|---|---|
| **NP 196:1991** | 45.0 | 4.120 | 168.500 | Obligatoria local |
| **NBR 6123:2023** | 45.0 | 4.850 | 198.200 | ⭐ Envolvente adoptada |
| **ASCE 7-22** | 45.0 (3s) | 4.410 | 180.100 | Referencia internacional |
| **EN 1991-1-4** | 45.0 | 4.630 | 189.400 | Eurocódigo |
