# D.2 — Grilla Definitiva de Pilares y Matriz de Transición Estructural

> **Etapa D › Sub-etapa 2** · **Tareas:** 4 · **Estado:** 🔲 Sin iniciar  
> Normativa: NBR 6118:2023 · CIRSOC 201 · ACI 318-19

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [ ] **Task D2.1:** Definir y validar la **Matriz de Superficies y Transición Estructural por Nivel** para todo el edificio (S2 a Azotea).
- [ ] **Task D2.2:** Dimensionar y verificar la variación escalonada de pilares de H°A° ($90\times 90\text{ cm} \to 80\times 80\text{ cm} \to 70\times 70\text{ cm} \to 60\times 60\text{ cm}$) optimizando el consumo de materiales y peso propio.
- [ ] **Task D2.3:** Calcular las **Vigas de Transferencia de H°A° ($80 \times 120\text{ cm}$)** en cota $+4.00\text{ m}$ para la transición estructural entre las 3 torres residenciales y el zócalo libre de Planta Baja.
- [ ] **Task D2.4:** Verificar la compatibilidad del sistema de entrepiso nervado bidireccional ($H=45\text{ cm}$ en subsuelos y $H=35\text{ cm}$ en plantas tipo) y la losa maciza de piscina ($H=30\text{ cm}$) en azotea.

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Matriz de Superficies y Transición Estructural por Nivel

Para garantizar el cumplimiento de los estados límites últimos (ELU) y de servicio (ELS), la estructura adopta una configuración coordinada de secciones de pilares, vigas de transición y tipos de losa según el uso espacial de cada nivel:

| Nivel / Planta | Cota (m) | Altura Libre (m) | Función Principal / Programa | Área Construida (m²) | Área FOT (m²) | Sección Pilares H°A° | Sistema de Entrepiso & Transición |
|---|---|---|---|---|---|---|---|
| **Subsuelo 2 (S2)** | -7.00 | 3.50 | Estacionamiento (140 autos/18 motos) & Depósitos Privados | 4.922,66 | 0,00 *(Exento)* | Pilares $90 \times 90\text{ cm}$ | Losa nervada bidireccional H=45cm con casetones recuperables |
| **Subsuelo 1 (S1)** | -3.50 | 3.50 | Estacionamiento (140 autos/15 motos), ANDE 1.000kVA, Genset, Cisterna | 4.922,66 | 0,00 *(Exento)* | Pilares $90 \times 90\text{ cm}$ | Losa nervada H=45cm + Ábacos refuerzo punzonamiento |
| **Planta Baja (PB)** | +0.00 | 4.00 | Lobby Residencial ($250\text{m}^2$), 3 Locales Comerciales ($1.850\text{m}^2$), RSU, BMS, Rampa | 3.145,00 | 3.145,00 | Pilares $90 \times 90\text{ cm}$ (Perímetro) | **Vigas de Transferencia H°A° ($80 \times 120\text{ cm}$)** en cota +4.00m |
| **Pisos P01 a P06** | +4.00 a +20.75 | 3.00 c/u | 3 Torres Residenciales (6 plantas tipo) | 8.640,00 | 8.640,00 | **Pilares $80 \times 80\text{ cm}$** | Losa nervada bidireccional H=35cm (casetón 25cm + capa 10cm) |
| **Pisos P07 a P12** | +24.10 a +40.85 | 3.00 c/u | 3 Torres Residenciales (6 plantas tipo) | 8.640,00 | 8.640,00 | **Pilares $70 \times 70\text{ cm}$** | Losa nervada bidireccional H=35cm + Vigas de borde $25 \times 50\text{ cm}$ |
| **Pisos P13 a P18** | +44.20 a +60.95 | 3.00 c/u | 3 Torres Residenciales (6 plantas tipo) | 8.640,00 | 8.640,00 | **Pilares $60 \times 60\text{ cm}$** | Losa nervada H=35cm + Balcones en voladizo de 1,50 m |
| **Azotea Técnica** | +64.30 | 3.50 | Amenities (Piscina 8×16m, SUM 150m², Gym) + Salas Máquinas | 1.200,00 | 1.200,00 | Pilares $60 \times 60\text{ cm}$ | Losa maciza de piscina $H=30\text{ cm}$ + Losa nervada H=35cm |
| **TOTALES** | **-7.00 a +68.15** | **—** | **Edificio Mixto 18P + 2 SUBSUELOS (3 Torres / 280 Cocheras)** | **40.110,32** | **30.265,00** | **Optimización Escalonada** | **Análisis Estructural Complejo Avanzado** |

---

### 2. Criterios de Transición Estructural y Reducción Escalonada

1. **Vigas de Transferencia H°A° ($80 \times 120\text{ cm}$):**
   - Dispuestas en cota $+4.00\text{ m}$ para interceptar los pilares de las 3 torres residenciales y liberar las grandes luces comerciales de Planta Baja ($1.850\text{ m}^2$ sin pilares intermediarios molestos).
   - Se verifican a cortante severo y momentos flectores de gran magnitud conforme a NBR 6118 / ACI 318.

2. **Gradación Escalonada de Pilares:**
   - Para reducir peso propio y optimizar consumo de hormigón $f'_c = 30\text{ MPa}$, la sección de los pilares varía cada 6 niveles manteniendo la coincidencia de centroides.
   - **S2-PB:** $90 \times 90\text{ cm}$ ($A_c = 0.81\text{ m}^2$)
   - **P01-P06:** $80 \times 80\text{ cm}$ ($A_c = 0.64\text{ m}^2$)
   - **P07-P12:** $70 \times 70\text{ cm}$ ($A_c = 0.49\text{ m}^2$)
   - **P13-P18 & Azotea:** $60 \times 60\text{ cm}$ ($A_c = 0.36\text{ m}^2$)

3. **Sistemas de Entrepiso y Refuerzos por Punzonamiento:**
   - **Subsuelos:** Losa nervada $H=45\text{ cm}$ con ábacos de macizado sobre pilares para resistir las sobrecargas de tránsito pesado e instalaciones ANDE/Genset.
   - **Torres (P01-P18):** Losa nervada $H=35\text{ cm}$ (casetón de 25 cm + 10 cm capa de compresión).
   - **Piscina Azotea:** Losa maciza de hormigón armado $H=30\text{ cm}$ impermeabilizada para soportar la carga hidrostática del vaso de piscina (lámina de agua de $1.20\text{ m} \implies q \approx 12\text{ kN/m}^2$).


