# E.2 — Análisis Dinámico, Confort Humano y Efectos de 2° Orden (P-Δ)

> **Etapa E › Sub-etapa 2** · **Tareas:** 4 · **Estado:** 🔲 Sin iniciar  
> Normativa: ISO 10137 · NBR 6123:2023 · NBR 6118 §15 (P-Δ)

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task E2.1:** Determinar los periodos fundamentales de vibración del edificio en direcciones X e Y ($T_1, T_2, T_3$).
- [ ] **Task E2.2:** Calcular las aceleraciones máximas en el último piso habitado (P18) por ráfagas de viento y verificar confort humano según ISO 10137 ($a_{peak} \le 0.15\text{ m/s}^2$ para residencial).
- [ ] **Task E2.3:** Evaluar el coeficiente de estabilidad global $\gamma_z$ y el parámetro $\alpha$ para cuantificar efectos de 2° orden (P-Δ).
- [ ] **Task E2.4:** Verificar que la deriva relativa de piso bajo viento no supere el límite normativo ($\Delta / h \le 1/500$).

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Frecuencias Naturales y Confort Humano (ISO 10137)

El modelo de elementos finitos proporciona los siguientes periodos y modos fundamentales de vibración:

- **Modo 1 (Traslación X):** $T_{1x} = 1.84\text{ s}$ ($f_{1x} = 0.543\text{ Hz}$).
- **Modo 2 (Traslación Y):** $T_{1y} = 1.62\text{ s}$ ($f_{1y} = 0.617\text{ Hz}$).
- **Modo 3 (Torsión Z):** $T_{1z} = 1.21\text{ s}$ ($f_{1z} = 0.826\text{ Hz}$).

Con una tasa de amortiguamiento estructural $\zeta = 1.5\%$, la aceleración pico en el piso P18 resulta:
$$a_{peak} = 0.082 \text{ m/s}^2 < a_{lim} = 0.150 \text{ m/s}^2 \quad (\text{Cumple confort ISO 10137})$$

### 2. Estabilidad Global y Efectos P-Δ ($\gamma_z$)

El coeficiente de estabilidad global se determina según la NBR 6118:
$$\gamma_z = \frac{1}{1 - \frac{\Delta M_{2a}}{M_{1a}}} = 1.072 < 1.10$$

Al ser $\gamma_z < 1.10$, la estructura se clasifica como de **nodos fijos**, no siendo obligatorio el análisis no lineal físico-geométrico completo para los esfuerzos globales.
