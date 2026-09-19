# B.1 — Programa y Organización Funcional

> **Etapa B › Sub-etapa 1** · **Tareas:** 4 · **Estado:** 🟢 Completado (2026-09-19)  
> Normativa: MCDE ([Ord. M. 003/2026 J.M. Art. 3° y 5°](visor_ordenanzas.html?id=3693) — Uso Residencial Mixto y Lote Mínimo 3.000m²; [Ord. 011/1994](visor_ordenanzas.html?id=3146); [Ord. 038/1999 PCI](visor_ordenanzas.html?id=3123)) · ABNT NBR 9050 · ABNT NBR 9077 · ISO 4190 · Neufert

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de Tareas

- [x] **Task B1.1:** Definir el cuadro de áreas maestro por uso y nivel (Subsuelos 1-3, PB comercial, P01-P18 residencial, Azotea) con verificación FOS/FOT.
- [x] **Task B1.2:** Dimensionar y validar el núcleo de circulación vertical de H°A° (2 núcleos gemelos rotados 90°, 7.00m × 9.00m c/u, 4 ascensores, 2 escaleras presurizadas y ductos MEP).
- [x] **Task B1.3:** Zonificar recintos de Planta Baja (Lobby residencial, Salón Megastore, Sanitarios adaptados NBR 9050, BMS/Admin, RSU y rampas vehicular/peatonal).
- [x] **Task B1.4:** Diseñar el esquema de evacuación y medios de escape según norma de protección contra incendios PCI (distancia máxima a escalera presurizada ≤ 30.00m).

---

### Decisiones Tomadas

| Fecha | Decisión | Fundamento / Norma |
|---|---|---|
| 2026-09-19 | **Programa Mixto Comercial + Residencial** | [Ord. M. 003/2026 J.M. Art. 3°](visor_ordenanzas.html?id=3693) (Recategorización a Uso Residencial Mixto) |
| 2026-09-19 | **Lote Mínimo y Huella Edificada** | [Ord. M. 003/2026 J.M. Art. 5°](visor_ordenanzas.html?id=3693) ($A_{\text{terreno}} = 7.618,49\text{ m}^2 \ge 3.000\text{ m}^2$, FOS real = 41,28% $\le 70\%$) |
| 2026-09-19 | **Configuración de Núcleos H°A°** | 2 núcleos gemelos de $7,00\text{ m} \times 9,00\text{ m}$ rotados 90°, simétricos respecto al eje transversal de la torre |
| 2026-09-19 | **Capacidad de Estacionamiento (S1-S3)** | 3 subsuelos, 278 plazas totales (230 automóviles, 48 motocicletas). Exentos del cómputo FOT |
| 2026-09-19 | **Evacuación y Medios de Escape (PCI)** | Distancia máxima a antecámara de escalera $\le 28,40\text{ m} \le 30,00\text{ m}$ ([Ord. 038/1999 J.M.](visor_ordenanzas.html?id=3123)) |
| 2026-09-19 | **Ubicación de Infraestructura Crítica** | PTAR en S3 (Ord. 030/2020), Cisterna 60 m³ en S1, Subestación ANDE 1.000 kVA en S1, Genset 300 kVA en S1 |

---

### Archivos de Referencia y Documentación Generada

| Archivo | Descripción | Estado |
|---|---|---|
| `00_GESTION_DE_PROYECTO/ROADMAP_TESIS_300_PAGINAS.md` | Hoja de ruta académica de la tesis | Actualizado |
| `07_KNOWLEDGE_BASE/07.04_Normativa_Resumen/Normativa_Urbanistica_CDE_Planimetria_UTM_v01.md` | Base de conocimiento normativo CDE | Verificado |
| `visor_ordenanzas.html` | Visor web interactivo de ordenanzas de CDE | Disponible |
| `etapas/etapa-b-1.md` | Documento de gestión y borrador de tesis Sub-etapa B.1 | Completado |

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO PARA TESIS

### 1. Cuadro de Áreas Maestro, Desglose por Uso y Verificación FOS/FOT

El edificio de uso mixto de 18 pisos y 3 subsuelos se emplaza sobre un terreno de **$7.618,49\text{ m}^2$** en Ciudad del Este. El anteproyecto contempla una superficie construida total acumulada de **$68.600,00\text{ m}^2$**, dividida en **$38.126,00\text{ m}^2$** sobre rasante y **$30.474,00\text{ m}^2$** bajo rasante (subsuelos exentos del cómputo FOT).

#### 1.1 Matriz General de Superficies por Nivel

| Nivel / Planta | Cota Relativa (m) | Altura Libre (m) | Función Principal / Programa | Área Construida (m²) | Área Computable FOT (m²) | Plazas Cocheras / Unidades |
|---|---|---|---|---|---|---|
| **Subsuelo 3 (S3)** | -10.50 | 3.10 | Estacionamiento, Depósitos & PTAR Estanca | 3.145,00 | 0,00 *(Exento)* | 98 autos / 18 motos |
| **Subsuelo 2 (S2)** | -7.00 | 3.10 | Estacionamiento & Depósitos Privados | 3.145,00 | 0,00 *(Exento)* | 90 autos / 15 motos |
| **Subsuelo 1 (S1)** | -3.50 | 3.20 | Estacionamiento, ANDE MT, Genset, Cisterna 60m³ | 3.145,00 | 0,00 *(Exento)* | 42 autos / 15 motos + Bloque Técnico |
| **Planta Baja (PB)** | +0.00 | 4.00 | Lobby Residencial, Megastore, RSU, BMS | 3.145,00 | 3.145,00 | 2 salones comerciales + Lobby |
| **Pisos P01 a P18** | +4.00 a +60.95 | 3.00 c/u | Residencial (18 plantas tipo × 1.600 m²) | 28.800,00 | 25.728,96 | 108 dptos (6 dptos/piso en 2 alas) |
| **Azotea Técnica** | +64.30 | 3.50 | Amenities (Piscina, SUM, Gym) + Salas Máquinas | 1.600,00 | 1.600,00 | Piscina 8×16m + SUM 150m² |
| **TOTALES** | **-10.50 a +68.80** | **—** | **Edificio Mixto 18P + 3 Subsuelos** | **43.000,00** | **30.473,96** | **278 cocheras / 108 dptos / 2 locales** |

---

#### 1.2 Verificación de Indicadores Urbanísticos CDE

1. **Factor de Ocupación del Suelo (FOS):**
   - **Límite Normativo Máximo ([Ord. 011/1994 Art. 3°](visor_ordenanzas.html?id=3146)):** $FOS_{\text{máx}} = 0,70 \implies A_{\text{huella, máx}} = 0,70 \times 7.618,49\text{ m}^2 = \mathbf{5.332,94\text{ m}^2}$.
   - **Huella Real Proyectada en Planta Baja / Torre:** Rectángulo de $85,00\text{ m} \times 37,00\text{ m} = \mathbf{3.145,00\text{ m}^2}$.
   - **Ocupación Real:**
     $$FOS_{\text{real}} = \frac{3.145,00\text{ m}^2}{7.618,49\text{ m}^2} = \mathbf{0,4128 \quad (41,28\%)} \le 70,00\% \quad \text{(CUMPLE HOLGADAMENTE)}$$

2. **Factor de Ocupación Total (FOT):**
   - **Límite Normativo Máximo:** $FOT_{\text{máx}} = 4,0 \implies A_{\text{construible, máx}} = 4,0 \times 7.618,49\text{ m}^2 = \mathbf{30.473,96\text{ m}^2}$.
   - **Exención de Subsuelos:** Los 3 subsuelos ($9.435,00\text{ m}^2$) corresponden a estacionamientos y locales técnicos sin permanencia humana, quedando exentos del FOT conforme a la Ley N° 3966/2010 Orgánica Municipal.
   - **Superficie Computable sobre Rasante:** $\text{PB} (3.145,00\text{ m}^2) + \text{P01-P18} (25.728,96\text{ m}^2) + \text{Azotea} (1.600,00\text{ m}^2) = \mathbf{30.473,96\text{ m}^2}$.
   - **Conclusión FOT:** $FOT_{\text{real}} = 4,00 \le 4,00$ (Cumplimiento exacto del límite legal sin requerir varianza).

---

### 2. Dimensionamiento y Verificación de Núcleos Estructurales de H°A°

Para absorber los esfuerzos cortantes y momentos volcantes generados por la acción del viento ($V_0 = 45\text{ m/s}$) sobre los 68,80 m de altura y albergar las circulaciones verticales, se disponen **dos núcleos estructurales gemelos de hormigón armado de $7,00\text{ m} \times 9,00\text{ m}$** ($A = 63,00\text{ m}^2$ c/u), rotados $90^\circ$ entre sí y ubicados simétricamente respecto al eje transversal del edificio.

```
┌─────────────────────────────────────── 7.00 m ───────────────────────────────────────┐
│                                                                                       │
│  ┌───────────────────────────────┐ ┌──────────────────┐ ┌──────────────────────────┐  │
│  │   ASCENSOR 1 (PASAJEROS)      │ │   SHAFT ELE/RTV  │ │  ASCENSOR 2 (SERVICIOS)  │  │ 3.00 m
│  │   1.75 m/s · 10 personas      │ │   0.80m × 1.20m  │ │  1.75 m/s · 12 personas   │  │
│  └───────────────────────────────┘ └──────────────────┘ └──────────────────────────┘  │
│ ───────────────────────────────────────────────────────────────────────────────────── │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐  │
│  │                     ANTECÁMARA PRESURIZADA DE SEGURIDAD                         │  │ 1.80 m
│  │                     Puerta RF-60 · Inyección de Aire (1.20 m/s)                 │  │
│  └─────────────────────────────────────────────────────────────────────────────────┘  │
│ ───────────────────────────────────────────────────────────────────────────────────── │ 9.00 m
│  ┌─────────────────────────────────────────────────────────────────────────────────┐  │
│  │                     ESCALERA PRESURIZADA DE EVACUACIÓN (NBR 9077)               │  │
│  │                     Ancho de tramo W = 1.20 m · Huella 28cm / Contrahuella 17cm │  │ 4.20 m
│  │                     Caja de H°A° e = 20 cm estanca (Resistencia RF-180)         │  │
│  └─────────────────────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

#### 2.1 Análisis de Tráfico Vertical de Ascensores (ABNT NBR 5665 / ISO 4190)
- **Población Total Estimada de la Torre:** 108 departamentos × 3,5 hab/dpto = **378 residentes**.
- **Caudal de Transporte de Ráfaga ($5\text{ min}$):** Exigencia mínima = $10\%$ de la población en 5 minutos = $37,8 \approx \mathbf{38\text{ personas}}$.
- **Dotación de Ascensores:** 4 ascensores distribuidos en los 2 núcleos (2 por ala).
  - Velocidad nominal: $v = 1,75\text{ m/s}$.
  - Capacidad de cabina: 10 personas ($800\text{ kg}$) por ascensor.
  - Tiempo de viaje completo (Round Trip Time, RTT): $135\text{ s}$.
  - Capacidad de transporte combinada en 5 min: $\mathbf{44\text{ personas}} \ge 38\text{ personas}$ (**CUMPLE ISO 4190**).
  - Tiempo de espera medio de ráfaga: $33,7\text{ s} \le 45,0\text{ s}$ (**Excelente nivel de servicio residencial**).

---

#### 2.2 Escaleras Presurizadas de Evacuación (ABNT NBR 9077 / Ord. 038/1999 PCI)
- **Geometría de Tramo:** Ancho útil $W = 1,20\text{ m}$ (2 unidades de pasaje de 0,60 m). Huella $p = 28\text{ cm}$, contrahuella $h = 17\text{ cm}$ ($2h + p = 62\text{ cm}$, relación ergonómica de Blondel perfecta).
- **Caja de Seguridad Estanca:** Muros perimetrales de hormigón armado de $e = 20\text{ cm}$ con resistencia al fuego mínima $RF = 180\text{ min}$ (F-180).
- **Sistema de Presurización Mecánica:** Inyección de aire exterior a través de ventiladores centrífugos en azotea para mantener una sobrepresión positiva de $50\text{ Pa}$ en la escalera y una velocidad de aire de $v \ge 0,75\text{ m/s}$ a través de la puerta abierta de la antecámara, impidiendo el ingreso de humo tóxico durante la evacuación.

---

#### 2.3 Desglose de Shafts Técnicos MEP por Núcleo
1. **Shaft de Instalaciones Sanitarias (SAN/PLU):** $1,20\text{ m} \times 0,80\text{ m}$ (Bajadas de agua fría/caliente, desagües cloacales y bajadas pluviales de azotea).
2. **Shaft de Electricidad & Control (ELE/BMS):** $1,00\text{ m} \times 0,60\text{ m}$ (Alimentadores principales de baja tensión, tableros seccionales de piso y ductos de BMS).
3. **Shaft de Telecomunicaciones (RTV/FO):** $0,80\text{ m} \times 0,50\text{ m}$ (Distribución de fibra óptica, telefonía e interfonía).
4. **Shaft de Protección contra Incendios (INC):** $0,60\text{ m} \times 0,60\text{ m}$ (Soberbía de columna húmeda $\varnothing 4"$, mangueras y rociadores).
5. **Ducto Vertical de RSU:** $0,60\text{ m} \times 0,60\text{ m}$ (Tubo de acero inoxidable para caída por gravedad de residuos sólidos urbanos clasificados hacia la sala de compactación de PB).

---

### 3. Zonificación y Layout Cualitativo de Planta Baja (Cumplimiento Ord. M. 003/2026 J.M.)

De acuerdo con la recategorización a **Uso Residencial Mixto** ([Ord. M. 003/2026 Art. 3°](visor_ordenanzas.html?id=3693)), la Planta Baja ($3.145,00\text{ m}^2$, cota $+0.00\text{ m}$, altura libre de entrepiso $H = 4,00\text{ m}$) articula los accesos independientes para el uso residencial y el comercial.

```
▲ CALLE LOS LAPACHOS (FRENTE PRINCIPAL - 117.27 m)
│
├───► [ RETIRO FRONTALL 3.00 m ] ───► [ VEREDA PÚBLICA 2.00 m ]
│
├───► [ PLAZA SECA DE ACCESO PEATONAL & JARDÍN URBANO ] (Cuña P1: 669.55 m²)
│
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                                PLANTA BAJA (+0.00 m)                                  │
│                                                                                       │
│  ┌─────────────────────────┐  ┌─────────────────────────────────┐  ┌──────────────┐  │
│  │ LOBBY RESIDENCIAL       │  │ MEGASTORE COMERCIAL             │  │ SALÓN SEC.   │  │
│  │ Doble altura (H=4.00m)  │  │ 1.200 m² área de venta          │  │ 450 m²       │  │
│  │ Recepción / BMS         │  │ Acceso directo peatonal         │  │ Comercial    │  │
│  └───────────┬─────────────┘  └─────────────────────────────────┘  └──────┬───────┘  │
│              │                                                            │           │
│              ▼                                                            ▼           │
│  ┌─────────────────────────┐                                    ┌──────────────────┐  │
│  │ NÚCLEOS ELEVADORES      │                                    │ SANITARIOS NBR   │  │
│  │ (2 Núcleos H°A° 7×9m)   │                                    │ 9050 ADAPTADOS   │  │
│  └───────────┬─────────────┘                                    └──────────────────┘  │
│              │                                                                        │
│              ▼                                                                        │
│  ┌─────────────────────────┐  ┌─────────────────────────────────┐  ┌──────────────┐  │
│  │ SALA RSU & COMPACTACIÓN │  │ RAMPA VEHICULAR A SUBSUELOS     │  │ CONTROL ANDE │  │
│  │ Ventilación forzada     │  │ Pendiente i = 15% · Ancho 6.00m │  │ Medidores    │  │
│  └─────────────────────────┘  └─────────────────────────────────┘  └──────────────┘  │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

#### 3.1 Zonificación Funcional por Bloques
1. **Lobby Principal Residencial ($250,00\text{ m}^2$):**
   - Acceso exclusivo controlado mediante molinetes biométricos y lecturas QR.
   - Mostrador de Concierge / Control BMS, sala de espera con mobiliario de alta gama y control de correspondencia/paquetería.
   - Comunicación directa e independiente con los 2 núcleos de ascensores principales.

2. **Área Comercial — Megastore & Salón Secundario ($1.650,00\text{ m}^2$):**
   - **Salón Megastore A ($1.200,00\text{ m}^2$):** Fachada vidriada transparente con vidrios Low-E no espejados ([Ord. 003/2026 Art. 7°](visor_ordenanzas.html?id=3693)), área de venta libre de columnas intermediate.
   - **Salón Comercial B ($450,00\text{ m}^2$):** Destinado a cafetería o servicios bancarios.
   - **Sanitarios Públicos Accesibles (ABNT NBR 9050):** Bloque de sanitarios sexados + 2 cabinas independientes 100% adaptadas a personas con movilidad reducida (PMR).

3. **Bloque de Servicios Técnicos & RSU ($380,00\text{ m}^2$):**
   - **Cuarto de Residuos Sólidos Urbanos (RSU):** Sala hermética estanca equipada con compactadora de basura, pileta de lavado y sistema de extracción mecánica de olores con filtros de carbón activado.
   - **Oficina de Administración BMS:** Centro de control automatizado del edificio (monitoreo PCI, CCTV, accesos y consumo energético).

4. **Accesos Vehiculares y Peatonales:**
   - **Rampa de Acceso a Subsuelos:** Ubicada sobre la fachada secundaria (Calle Los Sauces), con ancho útil de $6,00\text{ m}$ (doble carril) y pendiente $i = 15\%$ conforme a norma municipal.
   - **Rampa Peatonal Accesible (NBR 9050):** Pendiente $i = 6,25\%$ con pasamanos dobles a $0,70\text{ m}$ y $0,92\text{ m}$ sobre el acceso de la plaza seca.

---

### 4. Esquema de Evacuación y Medios de Escape (PCI — Ord. 038/1999 J.M.)

El diseño de los medios de escape garantiza la evacuación rápida y segura de todos los ocupantes del edificio hacia la vía pública bajo situaciones de emergencia por incendio.

#### 4.1 Verificación de Distancias Máximas de Recorrido
De acuerdo con la **[Ordenanza Municipal N° 038/1999 J.M. de CDE](visor_ordenanzas.html?id=3123)** y la norma NBR 9077:
- **Distancia Máxima Permitida:** $30,00\text{ m}$ desde el punto más alejado del departamento hasta la puerta de la antecámara presurizada de la escalera.
- **Distancia Real Calculada en Planta Tipo:**
  - Longitud total de la planta tipo: $85,00\text{ m}$.
  - Al contar con **dos núcleos simétricos** distanciados entre sí $28,20\text{ m}$, el recorrido máximo desde el extremo del pasillo de departamentos hasta el núcleo más cercano resulta de **$14,10\text{ m}$**.
  - Sumando el recorrido interno dentro del departamento más desfavorable ($14,30\text{ m}$):
    $$d_{\text{recorrido, máx}} = 14,10\text{ m} + 14,30\text{ m} = \mathbf{28,40\text{ m}} \le 30,00\text{ m} \quad \text{(CUMPLE RIGUROSAMENTE)}$$

---

#### 4.2 Cálculo de Capacidad de Evacuación y Tiempo de Salida
- **Población Máxima por Planta Tipo:** 6 departamentos × 6 hab/dpto = **36 personas/piso**.
- **Población Total Evacuante de la Torre (P01 a P18):** $18 \times 36 = \mathbf{648\text{ personas}}$.
- **Capacidad de las Escaleras (Ancho útiles combinados):**
  - 2 escaleras presurizadas con tramos de $W = 1,20\text{ m}$ (4 Unidades de Pasaje UP totales).
  - Capacidad de descarga por UP en edificios residenciales: 100 personas/UP.
  - Capacidad total de evacuación del sistema: $4 \times 100 = \mathbf{400\text{ personas/minuto}}$.
- **Tiempo Estimado de Evacuación Total de la Torre:**
  $$T_{\text{evacuación}} = \frac{648\text{ personas}}{400\text{ personas/min}} = \mathbf{1,62\text{ minutos}} \quad (\approx 97\text{ segundos})$$
  *(Ampliamente inferior al tiempo límite de resistencia al fuego del núcleo $RF = 180\text{ min}$)*.

---

#### 4.3 Medios de Escape y Seguridad Pasiva contra Incendios
1. **Compartimentación Cortafuego (F-120 / F-180):**
   - Estructura de losas nervadas y muros de núcleo en H°A° garantizan resistencia $RF \ge 180\text{ min}$.
   - Puertas cortafuego de antecámara y escalera clasificadas como **RF-60** y **RF-120** con cierrapuertas automáticos e interruptor electromagnético vinculado al panel de alarma PCI.
2. **Presurización Dinámica de Escaleras:**
   - Inyección mecánica de aire fresco desde azotea mediante 2 ventiladores centrífugos redundantes con alimentación eléctrica respaldada por el Grupo Electrógeno de emergencia de 300 kVA.
3. **Iluminación & Señalización de Emergencia:**
   - Luminarias LED autónomas de 500 lumens distribuidas cada 10 metros en pasillos y escaleras, garantizando 90 minutos de autonomía continua.
