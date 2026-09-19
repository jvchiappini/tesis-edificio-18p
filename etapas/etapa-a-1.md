# A.1 — Formalización del Terreno

> **Etapa A › Sub-etapa 1** · **Tareas:** 4 · **Estado:** 🔲 Sin iniciar
> Normativa: Municipalidad CDE · Código Urbanístico · NOMENCLATURA.md

---

## 📋 SECCIÓN 1 — GESTIÓN Y TRABAJO

### Checklist de tareas

- [ ] **eA-1** · **Planimetría del polígono real con coordenadas UTM**
  - Trazar el polígono: P1(737721.76, 7176185.26) → P2(737837.53, 7176203.96) → P3(737853.36, 7176246.13) → P4(737755.78, 7176281.93)
  - Calcular área exacta (7.618,49 m²) por método de coordenadas
  - Verificar cierre de poligonal (error de cierre ≤ 1:5000)
  - Obtener plano catastral municipal
  - Archivo de referencia: `modelo_estructural.py` · `NOMENCLATURA.md`

- [ ] **eA-2** · **Identificación de calles y orientación geográfica**
  - Confirmar nombre de la calle correspondiente al frente P1→P2 (117,27 m)
  - Determinar Norte verdadero vs. Norte magnético (declinación magnética en CDE ≈ -14°)
  - Fotografía aérea / Google Maps con escala y escuadra de orientación
  - Relevamiento de construcciones linderas y servidumbres de paso

- [ ] **eA-3** · **Análisis del vértice agudo P1 (61,44°) y definición de la cuña**
  - Demarcar la zona no edificable en el vértice agudo
  - El rectángulo edificable comienza en ~u=27 m desde P1
  - Proponer el límite del chaflán o jardín frontal
  - Documentar el polígono edificable reducido como **hipótesis formal de tesis** con retiros adoptados: 3 m frente, 3 m fondo, 2 m laterales
  - ⚠️ El vértice P1 de 61,44° impide estructura regular hasta esa esquina — debe declararse explícitamente en la tesis

- [ ] **eA-4** · **Certificado de uso de suelo y normativa municipal**
  - Gestionar ante la Municipalidad de CDE o documentar explícitamente como hipótesis declarada
  - FOS = 0,70 → área máxima de huella = 5.332 m²
  - FOT = 4,0 → área total construible = 30.474 m²
  - Verificar si los subsuelos quedan exentos del cómputo FOT según ordenanza
  - ⚠️ Con huella de ~3.520 m² y 18 pisos: área construida = 63.360 m² > FOT (30.474 m²). Requiere varianza municipal

### Decisiones tomadas

| Fecha | Decisión | Fundamento |
|---|---|---|
| — | Retiros adoptados: 3m frente / 3m fondo / 2m laterales | Hipótesis de tesis |
| — | FOS = 0,70 / FOT = 4,0 | Hipótesis de tesis — verificar ante Municipalidad CDE |

### Archivos de referencia

| Archivo | Descripción | Estado |
|---|---|---|
| `00_GESTION_DE_PROYECTO/NOMENCLATURA.md` | Convención de nombres | Existente |
| `05_RECURSOS/05.05_Scripts_Python/06_Estructura/modelo_estructural.py` | Script de modelado | Revisar |

### Notas de trabajo

> *(Espacio libre para anotaciones, dudas y recordatorios)*

---

## 📝 SECCIÓN 2 — BORRADOR ACADÉMICO

### 1.1 Descripción del predio y planimetría

El terreno objeto de estudio se ubica en la ciudad de **Ciudad del Este**, departamento de Alto Paraná, República del Paraguay. El polígono del predio fue relevado mediante sistema GPS diferencial con referencia al sistema de coordenadas **UTM Zona 21J, dátum WGS84**, obteniéndose los siguientes vértices:

| Vértice | Este (m) | Norte (m) |
|---|---|---|
| P1 | 737.721,76 | 7.176.185,26 |
| P2 | 737.837,53 | 7.176.203,96 |
| P3 | 737.853,36 | 7.176.246,13 |
| P4 | 737.755,78 | 7.176.281,93 |

El área del predio calculada por el método de coordenadas cartesianas resulta en **7.618,49 m²**, con un perímetro total de *(completar)*. El frente principal, correspondiente al lado P1→P2, tiene una longitud de **117,27 m**.

#### Restricción geométrica — vértice agudo P1

El vértice P1 presenta un **ángulo interior de 61,44°**, clasificándose como vértice agudo severo. Esta condición geométrica impide inscribir una estructura rectangular regular hasta dicha esquina. La zona triangular resultante *(completar área en m²)* se destina a:
- Acceso peatonal desde la vía pública
- Jardín de borde y arbolado ornamental
- Chaflán de fachada con tratamiento arquitectónico

El rectángulo edificable neto comienza en una distancia aproximada de **27 m** desde el vértice P1 medida sobre el eje del frente P1→P2.

*(Insertar: figura del polígono real con vértices etiquetados, Norte, escala gráfica y acotado del rectángulo edificable)*

### 1.2 Parámetros urbanísticos y uso del suelo

De acuerdo con la consulta ante la Dirección de Planificación y Urbanismo de la Municipalidad de Ciudad del Este *(o en su defecto, como hipótesis de tesis declarada)*, los indicadores urbanísticos aplicables a la parcela son:

| Indicador | Valor | Observación |
|---|---|---|
| Factor de Ocupación del Suelo (FOS) | 0,70 | Área máx. huella = 5.332 m² |
| Factor de Ocupación Total (FOT) | 4,0 | Área total construible = 30.474 m² |
| Retiro frontal | 3,0 m | Adoptado como hipótesis |
| Retiro de fondo | 3,0 m | Adoptado como hipótesis |
| Retiros laterales | 2,0 m c/u | Adoptado como hipótesis |
| Altura máxima | Sin restricción / *(verificar)* | Confirmar ante Municipalidad |

> **Nota de hipótesis:** El edificio proyectado de 18 pisos + 3 subsuelos origina un área construida sobre rasante de aproximadamente 63.360 m², valor que excede el FOT=4,0 (máximo 30.474 m²). El proyecto se desarrolla bajo la hipótesis de obtención de una **varianza urbanística** o clasificación como "proyecto de interés económico especial", figura que deberá tramitarse ante la Junta Municipal de Ciudad del Este según lo establecido en el Código Urbanístico vigente.

---

### Referencias bibliográficas — A.1

- Municipalidad de Ciudad del Este — Código de Ordenamiento Urbano y Territorial (vigente)
- INTN — Instituto Nacional de Tecnología y Normalización: normas paraguayas aplicables
- IGM Paraguay — Instituto Geográfico Militar: sistema de referencia geodésico nacional
