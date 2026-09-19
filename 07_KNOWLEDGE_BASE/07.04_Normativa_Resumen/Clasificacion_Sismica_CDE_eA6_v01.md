# Clasificación Sísmica del Sitio y Espectro de Respuesta Elástica (eA-6)
> **Proyecto:** Edificio de Uso Mixto 18P + 3 Subsuelos — Ciudad del Este, Paraguay  
> **Documento:** KB-07.04-002 · **Versión:** 1.0 · **Fecha:** 2026-09-19  
> **Normas de referencia:** ABNT NBR 15421:2023 · ASCE 7-22 (§11, §20) · Eurocódigo 8 (EN 1998-1)

---

## 1. Contexto Geológico y Zonificación Sísmica

### 1.1 Emplacement Geográfico y Sustrato Geológico
Ciudad del Este, Departamento de Alto Paraná, Paraguay, se asienta sobre la **Formación Serra Geral** (Basalto toleítico de la Provincia Magmática del Paraná, Cretácico Inferior, ~134 Ma). El sustrato rocoso consiste en coladas basálticas masivas de alta rigidez y baja alteración geotécnica a poca profundidad (típicamente < 3–6 m en la zona urbana de CDE).

### 1.2 Peligrosidad Sísmica de Paraguay y CDE
Paraguay se ubica en el interior estable de la Placa Sudamericana (entorno intraplaca de muy baja actividad sismotectónica). Conforme al mapa de amenazas sísmicas de la NBR 15421:2023 y estudios regionales (p. ej., USGS Global Seismic Hazard Map), el departamento de Alto Paraná clasifica en la **Zona de Baja Sismicidad**.

| Parámetro Sísmico | Valor Adoptado | Referencia |
|---|---|---|
| Aceleración pico del suelo ($a_g$ / PGA) | **$0{,}05\text{ g}$ a $0{,}08\text{ g}$** | NBR 15421:2023 (Tr = 475 años, 10% prob. exc. 50 años) |
| Aceleración espectral a período corto ($S_s$) | $0{,}125\text{ g}$ ($a_g = 0{,}05\text{g}$) / $0{,}200\text{ g}$ ($a_g = 0{,}08\text{g}$) | $S_s = 2{,}5 \cdot a_g$ (ASCE 7-22 / NBR 15421) |
| Aceleración espectral a 1 s ($S_1$) | $0{,}0625\text{ g}$ ($a_g = 0{,}05\text{g}$) / $0{,}100\text{ g}$ ($a_g = 0{,}08\text{g}$) | $S_1 = 1{,}25 \cdot a_g$ |
| Perfil de suelo por velocidad de onda de corte ($V_{s30}$) | **$> 760\text{ m/s}$** | Hipótesis — Sustrato rocoso de basalto sano/poco meteorizado |
| Clasificación del sitio (ASCE 7-22) | **Site Class B** (Rock) | Table 20.3-1 ASCE 7-22 |
| Clasificación del sitio (NBR 15421:2023) | **Classe A** (Rocha sã ou muito rígida) | Tabela 2 NBR 15421 |
| Factores de amplificación de sitio ($F_a, F_v$) | $F_a = 1{,}00 \quad F_v = 1{,}00$ | No hay amplificación dinámica por suelo blando |

---

## 2. Espectro de Respuesta Elástica de Diseño

### 2.1 Ecuaciones de Pseudo-Aceleración $S_a(T)$
Para una amortiguación viscosa equivalente del 5% ($\xi = 5\%$), las aceleraciones espectrales de diseño se definen como:

$$S_{DS} = \frac{2}{3} F_a S_s = \begin{cases} 0{,}0833\text{ g} & \text{para } a_g = 0{,}05\text{g} \\ 0{,}1333\text{ g} & \text{para } a_g = 0{,}08\text{g} \end{cases}$$

$$S_{D1} = \frac{2}{3} F_v S_1 = \begin{cases} 0{,}0417\text{ g} & \text{para } a_g = 0{,}05\text{g} \\ 0{,}0667\text{ g} & \text{para } a_g = 0{,}08\text{g} \end{cases}$$

Los períodos característicos del espectro son:

$$T_0 = 0{,}2 \frac{S_{D1}}{S_{DS}} = 0{,}100\text{ s} \qquad T_s = \frac{S_{D1}}{S_{DS}} = 0{,}500\text{ s} \qquad T_L = 4{,}00\text{ s}$$

La rama descendente para el período fundamental estimado del edificio ($T_1 \approx 1{,}10$–$1{,}80\text{ s}$, medio $\approx 1{,}45\text{ s}$) proporciona:

$$S_a(T_1 = 1{,}45\text{ s}) = \frac{S_{D1}}{T_1} = \begin{cases} 0{,}0287\text{ g} \quad (0{,}282\text{ m/s}^2) & \text{para } a_g = 0{,}05\text{g} \\ 0{,}0460\text{ g} \quad (0{,}451\text{ m/s}^2) & \text{para } a_g = 0{,}08\text{g} \end{cases}$$

---

## 3. Justificación Técnica: Dominancia del Viento sobre el Sismo

Para un edificio esbelto de 18 pisos (~64 m de altura sobre rasante) con masa sísmica estimada de $W_{total} \approx 200.000\text{ kN}$ (~20.000 toneladas):

1. **Cortante basal por sismo elástico ($V_{basal,sismo}$):**
   $$V_{basal,sismo} = C_s \cdot W_{total} = \frac{S_a(T_1)}{R/I_e} \cdot W_{total}$$
   Para un sistema dúctil de pórticos/pantallas ($R \approx 5$, $I_e = 1{,}0$):
   $$C_s = \frac{0{,}0287\text{ g}}{5} \approx 0{,}00574 \quad \Rightarrow \quad V_{basal,sismo} \approx 0{,}00574 \times 200.000\text{ kN} \approx \mathbf{1.150\text{ kN}}$$

2. **Cortante basal por viento ($V_{basal,viento}$):**
   Con $V_0 = 45\text{ m/s}$, la fuerza estática equivalente acumulada del viento sobre la fachada expuesta ($64\text{ m} \times 37\text{ m} \approx 2.368\text{ m}^2$) alcanza:
   $$V_{basal,viento} \approx \mathbf{3.500\text{ kN a } 4.800\text{ kN}}$$

> 💡 **Conclusión de Rigor Estructural:** El cortante basal y el momento volcante producidos por la acción del viento superan a los sísmicos por un factor de **3 a 4 veces**. En consecuencia, **las combinaciones con viento ($1{,}2G + 1{,}0Q + 1{,}4W$) gobiernan el dimensionamiento elástico y el estado límite de servicio (derivas laterales $\Delta/H \leq 1/500$)**. El sismo solo requerirá verificaciones de detallamiento constructivo dúctil mínimo según ACI 318-19 / NBR 6118.

---

## 4. Entregables y Scripts
- **Script:** `05_RECURSOS/05.05_Scripts_Python/02_Ingenieria_Viento/ea6_clasificacion_sismica_espectro.py`
- **Figura:** `etapas/img/figura_1_6_espectro_sismico_cde.png`
