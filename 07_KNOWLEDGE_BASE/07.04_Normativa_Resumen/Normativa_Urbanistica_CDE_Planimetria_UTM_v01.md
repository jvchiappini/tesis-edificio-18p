# Normativa Urbanística de Ciudad del Este (CDE) y Planimetría Terreno UTM Zona 21J

> **Categoría:** Base de Conocimiento Normativo · **Código:** `07.04_Normativa_Resumen`
> **Ubicación del Terreno:** Ciudad del Este, Departamento de Alto Paraná, República del Paraguay.
> **Sistema Geodésico:** UTM Zona 21J, Dátum WGS84 / SIRGAS2000.
> **Metodología de Relevamiento:** Digitalización y Teledetección Satelital (Google Earth Pro v7.3).

---

## 1. Planimetría y Delimitación de Vías Públicas / Linderos

El terreno se define mediante los vértices de mensura extraídos mediante herramientas de teledetección y fotointerpretación satelital (**Google Earth Pro**):

| Vértice | Coordenada Este X (m) | Coordenada Norte Y (m) | Lado | Longitud (m) | Azimut Norte (°) | Denominación de Vía Pública / Lindero Predial |
|---|---|---|---|---|---|---|
| **P1** | 737.721,76 | 7.176.185,26 | P1 → P2 | 117,271 | 80,82° | **Calle Los Lapachos** (Frente Principal N 80°49' E) |
| **P2** | 737.837,53 | 7.176.203,96 | P2 → P3 | 45,043 | 20,58° | **Calle Los Sauces** (Frente Secundario / Acceso N 20°35' E) |
| **P3** | 737.853,36 | 7.176.246,13 | P3 → P4 | 103,940 | 290,15° | **Inmueble Residencial Privado** (Lindero Posterior / Predio Vecino) |
| **P4** | 737.755,78 | 7.176.281,93 | P4 → P1 | 102,481 | 199,39° | **Avenida Itaipú Oeste** (Frente Secundario / Lindero S 19°23' W) |

### 1.1 Nota Metodológica Académica — Origen de Coordenadas
- **Fuente de Datos:** Digitalización de alta resolución sobre ortofotos satelitales en Google Earth Pro v7.3.
- **Incertidumbre Posicional:** Se adopta una tolerancia de precisión planimétrica relativa de $\pm 1,5\text{ m}$ a $\pm 2,5\text{ m}$, propia del sensamiento remoto satelital en entorno urbano.
- **Justificación de Tesis:** Dado que el trabajo consiste en un anteproyecto académico de grado en ingeniería civil, el modelo planimétrico derivado de Google Earth Pro satisface la delimitación del polígono edificable. En una fase ejecutiva real de obra, se exigirá la mensura catastral de precisión milimétrica mediante receptores **GNSS RTK / Estación Total**.

### 1.2 Métricas Fundamentales
- **Perímetro Total:** $P = 368,735\text{ m}$
- **Superficie Bruta Exacta (Regla de Gauss / Shoelace):** $A = 7.618,487\text{ m}^2 \approx \mathbf{7.618,49\text{ m}^2}$
- **Error de Cierre Linear/Angular:** $0,00\text{ m}$ (Cierre perfecto de la poligonal cartográfica).
- **Declinación Magnética (CDE 2026):** $\text{Dec} = -13,8^\circ\text{ W}$ (El Norte magnético se encuentra $13,8^\circ$ al Oeste del Norte verdadero).

### 1.3 Ángulos Interiores del Polígono
$$\text{Suma de ángulos interiores} = (n - 2) \times 180^\circ = (4 - 2) \times 180^\circ = 360,00^\circ$$
- $\alpha_{P1} = \mathbf{61,44^\circ}$ ($61,4365^\circ$) $\to$ **Intersección Av. Itaipú Oeste / Calle Los Lapachos** (Vértice Agudo Severo)
- $\alpha_{P2} = \mathbf{119,75^\circ}$ ($119,7510^\circ$) $\to$ Intersección Calle Los Lapachos / Calle Los Sauces
- $\alpha_{P3} = \mathbf{89,57^\circ}$ ($89,5716^\circ$) $\to$ Esquina Calle Los Sauces / Lindero Privado Vecino
- $\alpha_{P4} = \mathbf{89,24^\circ}$ ($89,2409^\circ$) $\to$ Esquina Lindero Privado Vecino / Av. Itaipú Oeste

---

## 2. Análisis del Vértice Agudo P1 (Intersección Av. Itaipú Oeste y Calle Los Lapachos)

1. **Restricción Geométrica:** El ángulo de $61,44^\circ$ en la esquina $P_1$ impide inscribir directamente la huella rectangular del edificio ($37,0\text{ m}$ de ancho con retiros laterales de $2,0\text{ m}$) sin invadir las líneas de edificación municipal.
2. **Límite del Rectángulo Edificable:** El rectángulo edificable de $85,0\text{ m} \times 37,0\text{ m}$ ($3.145\text{ m}^2$) inicia a una distancia de $u = 27,00\text{ m}$ desde el vértice $P_1$ sobre la **Calle Los Lapachos**.
3. **Geometría de la Cuña:**
   - Altura perpendicular a Calle Los Lapachos: $h = 27,00 \times \tan(61,44^\circ) = 49,60\text{ m}$.
   - Hipotenusa sobre Av. Itaipú Oeste: $L_{hyp} = 27,00 / \cos(61,44^\circ) = 56,47\text{ m}$.
   - **Área de la Cuña Triangular No Edificable:** $A_{cuña} = \frac{1}{2} \times 27,00 \times 49,60 = \mathbf{669,55\text{ m}^2}$.
4. **Destino Arquitectónico:** Plaza seca de acceso peatonal principal, control de acceso y jardín urbano con especies nativas.

---

## 3. Normativa Urbanística de Ciudad del Este (FOS, FOT y Retiros)

### 3.1 Marco Legal
- **Ordenanzas Aplicables:** Ordenanza Municipal CDE N° 030/2000 y N° 024/2014 (Plan Regulador y Código de Edificación y Ordenamiento Urbano de Ciudad del Este).

### 3.2 Indicadores Urbanísticos
1. **Factor de Ocupación del Suelo (FOS):**
   - $FOS_{máx} = 0,70$
   - $A_{huella,máx} = 0,70 \times 7.618,49\text{ m}^2 = \mathbf{5.332,94\text{ m}^2}$
   - Huella Proyectada ($85\text{m} \times 37\text{m}$): $A_{huella} = 3.145,00\text{ m}^2$
   - $FOS_{real} = \frac{3.145,00}{7.618,49} = \mathbf{41,28\% \le 70,00\%}$ (**CUMPLE AMPLIAMENTE**).

2. **Factor de Ocupación Total (FOT):**
   - $FOT_{máx} = 4,0$
   - $A_{construible,máx} = 4,0 \times 7.618,49\text{ m}^2 = \mathbf{30.473,96\text{ m}^2}$
   - Superficie Sobre Rasante Proyectada: Planta Baja Comercial ($3.145\text{ m}^2$) + 18 Pisos Residenciales ($18 \times 3.145\text{ m}^2 = 56.610\text{ m}^2$) = $\mathbf{59.755,00\text{ m}^2}$.
   - **Exención de Subsuelos:** Los 3 subsuelos de estacionamientos y servicios ($3 \times 3.145 = 9.435\text{ m}^2$) están exentos del cómputo FOT según la ordenanza municipal.
   - **Justificación de Varianza Urbanística:** Debido a que $59.755,00\text{ m}^2 > 30.473,96\text{ m}^2$, el proyecto requiere una **varianza urbanística formal por régimen de desarrollo inmobiliario de alto impacto económico**, tramitada ante la Junta Municipal de CDE.

3. **Retiros Reglamentarios Adoptados:**
   - Retiro Frontal ($R_f$): $3,0\text{ m}$ sobre el frente Calle Los Lapachos ($117,27\text{ m}$).
   - Retiro Posterior / Fondo ($R_p$): $3,0\text{ m}$ sobre el lindero del inmueble residencial privado ($103,94\text{ m}$).
   - Retiros Laterales ($R_l$): $2,0\text{ m}$ c/u sobre Calle Los Sauces ($45,04\text{ m}$) y Av. Itaipú Oeste ($102,48\text{ m}$).
