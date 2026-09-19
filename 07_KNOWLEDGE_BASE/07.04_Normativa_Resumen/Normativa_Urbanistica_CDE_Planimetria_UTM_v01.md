# Normativa Urbanística de Ciudad del Este (CDE) y Planimetría Terreno UTM Zona 21J

> **Categoría:** Base de Conocimiento Normativo · **Código:** `07.04_Normativa_Resumen`
> **Ubicación del Terreno:** Ciudad del Este, Departamento de Alto Paraná, República del Paraguay.
> **Sistema Geodésico:** UTM Zona 21J, Dátum WGS84 / SIRGAS2000.
> **Metodología de Relevamiento:** Digitalización y Teledetección Satelital (Google Earth Pro v7.3).

---

## 1. Planimetría y Delimitación del Terreno Irregular

El terreno se define mediante los vértices de mensura extraídos mediante herramientas de teledetección y fotointerpretación satelital (**Google Earth Pro v7.3**), conformando un **cuadrilátero de geometría irregular de 4 lados desiguales**:

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

### 1.3 Ángulos Interiores del Polígono Irregular
$$\text{Suma de ángulos interiores} = (n - 2) \times 180^\circ = (4 - 2) \times 180^\circ = 360,00^\circ$$
- $\alpha_{P1} = \mathbf{61,44^\circ}$ ($61,4365^\circ$) $\to$ **Intersección Av. Itaipú Oeste / Calle Los Lapachos** (Vértice Agudo Severo)
- $\alpha_{P2} = \mathbf{119,75^\circ}$ ($119,7510^\circ$) $\to$ Intersección Calle Los Lapachos / Calle Los Sauces (Vértice Obtuso)
- $\alpha_{P3} = \mathbf{89,57^\circ}$ ($89,5716^\circ$) $\to$ Esquina Calle Los Sauces / Lindero Privado Vecino
- $\alpha_{P4} = \mathbf{89,24^\circ}$ ($89,2409^\circ$) $\to$ Esquina Lindero Privado Vecino / Av. Itaipú Oeste

---

## 2. Análisis del Vértice Agudo P1 y Cuña Frontal

1. **Restricción Geométrica:** El ángulo de $61,44^\circ$ en la esquina $P_1$ impide proyectar estructuras sólidas hasta esa intersección sin invadir líneas de edificación municipal.
2. **Geometría de la Cuña:**
   - Altura perpendicular a Calle Los Lapachos: $h = 27,00 \times \tan(61,44^\circ) = 49,60\text{ m}$.
   - Hipotenusa sobre Av. Itaipú Oeste: $L_{hyp} = 27,00 / \cos(61,44^\circ) = 56,47\text{ m}$.
   - **Área de la Cuña Triangular No Edificable:** $A_{cuña} = \frac{1}{2} \times 27,00 \times 49,60 = \mathbf{669,55\text{ m}^2}$.
3. **Destino Arquitectónico:** Plaza seca de acceso peatonal principal, control de acceso y jardín urbano sustentable.

---

## 3. Normativa Urbanística de Ciudad del Este y Envolvente Máxima

### 3.1 Marco Legal Oficial (Fuente: Repositorio Municipal MCDE)
- **Uso de Suelo y Retiros:** **Ordenanza Municipal CDE N° 011/1994 J.M.** (Reglamentación del Uso del Suelo) y modificatoria **Ordenanza N° M. 003/2026 J.M.**
- **Instalaciones Sanitarias y Efluentes (PTAR):** **Ordenanza Municipal CDE N° 030/2020 J.M.** (Art. 5° y 9°) y modificatoria **Ordenanza N° 033/2023 J.M.**
- **Reglamento General de Edificaciones (Código Base):** **Ordenanza Municipal CDE N° 005/1976 J.M.** y modificatorias (Ord. 022/1998, 031/1998).
- **Dimensiones Mínimas de Lotes:** **Ordenanza Municipal CDE N° 027/2022 J.M.** (Reglamentación Arts. 227 y 229 Ley 3966/2010 Orgánica Municipal).
- **Prevención y Protección contra Incendios (PCI):** **Ordenanzas CDE N° 038/1999 J.M., 026/1990 J.M. y 024/2005 J.M.**

### 3.2 Indicadores Urbanísticos y Evaluación Normativa vs. Hipótesis de Tesis

1. **Factor de Ocupación del Suelo (FOS):**
   - $FOS_{máx, adoptado} = 0,70$ (Hipótesis proyectual de anteproyecto de tesis).
   - $A_{huella,máx} = 0,70 \times 7.618,49\text{ m}^2 = \mathbf{5.332,94\text{ m}^2}$.
   - **Huella Real Proyectada (Etapa B):** Rectángulo simplificado de $85,0\text{ m} \times 37,0\text{ m} = 3.145,00\text{ m}^2$ ($FOS_{real} = 0,4128 = 41,28\%$), cumpliendo holgadamente el límite.

2. **Factor de Ocupación Total (FOT):**
   - $FOT_{máx, adoptado} = 4,0$ (Hipótesis proyectual de anteproyecto de tesis).
   - $A_{construible,máx} = 4,0 \times 7.618,49\text{ m}^2 = \mathbf{30.473,96\text{ m}^2}$.
   - **Exención de Subsuelos:** Los 3 subsuelos de estacionamientos y servicios ($\approx 9.435\text{ m}^2$) quedan exentos del cómputo FOT conforme a la Ley 3966/2010 Orgánica Municipal y el régimen urbanístico municipal.

3. **Retiros Reglamentarios (Norma vs. Hipótesis Proyectual):**
   - **Exigencia Legal Directa (Ord. 011/1994 J.M. Art. 4°):** Retiro mínimo de **5,0 m sobre calles** y **6,0 m sobre avenidas**. En esquinas/terrenos con dos frentes, se permite aplicar el retiro de 5,0 m sobre al menos una de las arterias principales.
   - **Hipótesis Académica Adoptada:** Retiro Frontal $R_f = 3,0\text{ m}$ (Calle Los Lapachos), Retiro Posterior $R_p = 3,0\text{ m}$ (predio vecino), y Retiros Laterales $R_l = 2,0\text{ m}$ (Av. Itaipú Oeste y Calle Los Sauces). *Se mantendrá la justificación explícita de este ajuste proyectual en las memorias de cálculo.*
   - **Veredas (Ord. 011/1994 J.M. Art. 5°):** Ancho mínimo de **2,0 m** desde la línea de edificación.

4. **Tratamiento de Efluentes y Licencia Ambiental (OBLIGATORIO por Ord. 030/2020 J.M.):**
   - **Art. 5°:** Toda obra civil con cobertura $\ge 2.000\text{ m}^2$ debe instalar una **Planta de Tratamiento de Efluentes (PTAR)** propia para posterior vertido a red o cuerpo receptor.
   - **Art. 9°:** Se exige la obtención de la **Declaración de Impacto Ambiental (DIA)** y el **Plan de Gestión Ambiental (PGA)** aprobados por el MADES (Ley 294/93). El proyecto ($\approx 68.600\text{ m}^2$ edificados) debe incorporar la PTAR en los subsuelos técnicos.
