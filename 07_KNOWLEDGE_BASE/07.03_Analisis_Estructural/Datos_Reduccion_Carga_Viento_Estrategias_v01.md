# Reducción de carga de viento por modificación aerodinámica — Datos publicados (v01)

> Área: Análisis estructural — cargas de viento en edificios en altura.
> Fecha de búsqueda: 2026-08-19. Versión Revit: n/a (datos bibliográficos).
> Objetivo: valores reportados en la literatura para respaldar la Figura 2 de la Tarea 1 y su posterior verificación en la tesis.

## Valores reportados (rango de reducción de carga/respuesta)

| Estrategia | Reducción reportada | Magnitud medida | Fuente |
|------------|--------------------|-----------------|--------|
| Esquina achaflanada (chamfer ~5–15%) | 25–40% | fuerza / momento / movimiento (along- y across-wind) | Kwok 1988 (citado en Elshaer et al. 2014): chamfer ~10% del ancho → 30–40% en movimientos along- y across-wind; Al-Masoodi et al. 2024 (CFD): 5% → 25,97%; 15% → 35,50% |
| Esquina redondeada (round ~5–20%) | 21–41% | coeficiente de fuerza (CFD) | Al-Masoodi et al. 2024: 5% → 21,15%; 10% → 33,85%; 15% → 38,20%; 20% → 40,73% (la mejor a mayor reducción) |
| Retranqueo / escalonado (setback, tapered) | 25–40% | base moment / fuerza de sustentación fluctuante | Taipei 101: 25% de reducción de base moment (Elshaer et al. 2014); Kim & You 2002: ~40% en fuerza de sustentación fluctuante en flujo suburbano; Tanaka et al. 2012: mejor comportamiento en o.t.m. fluctuante |
| Giro / torsión (helical, twist ≥90–180°) | 45–50% | fuerza de viento / o.t.m. fluctuante across-wind | Elshaer et al. 2016 y Orbay et al. 2017: 45% along- y across-wind vs. prisma cuadrado; Tanaka et al. 2012: la o.t.m. fluctuante across-wind se reduce a la mitad (~50%) con ángulo de giro ≥180° |

## Referencias completas (formato IEEE)

1. A. Elshaer, G. Bitsuamlak, and A. El Damatty, "Enhancing wind performance of tall buildings using corner aerodynamic optimization," Engineering Structures, vol. 136, pp. 133–148, 2017, doi: 10.1016/j.engstruct.2017.01.019.
2. A. Elshaer, G. Bitsuamlak, and A. El Damatty, "Wind load reductions due to building corner modifications," in Proc. 6th Int. Conf. Computational Methods (ICCM), 2014.
3. Y. M. Kim and K. P. You, "Dynamic responses of a tapered tall building to wind loads," J. Wind Eng. Ind. Aerodyn., vol. 90, no. 14, pp. 1771–1782, 2002.
4. H. Tanaka, Y. Tamura, K. Ohtake, M. Nakai, and Y. C. Kim, "Experimental investigation of aerodynamic forces and wind pressures acting on tall buildings with various unconventional configurations," J. Wind Eng. Ind. Aerodyn., vol. 107–108, pp. 179–189, 2012.
5. A. H. Al-Masoodi et al., "CFD analysis of the impact of corner adjustments in tall square buildings for wind load mitigation," Engineering Research Express, 2024, doi: 10.1088/2631-8695/ad8b11.
6. J. Xie, "Aerodynamic optimization of super-tall buildings and its effectiveness assessment," J. Wind Eng. Ind. Aerodyn., vol. 130, pp. 88–98, 2014, doi: 10.1016/j.jweia.2014.04.004.
7. A. Sharma, H. Mittal, and A. Gairola, "Mitigation of wind load on tall buildings through aerodynamic modifications: Review," J. Build. Eng., vol. 18, pp. 180–194, 2018, doi: 10.1016/j.jobe.2018.03.005.

## Notas importantes para la tesis

- **Los rangos dependen de la magnitud medida** (coeficiente de fuerza, base moment, movimientos, aceleraciones) y de la condición de flujo (suburbano/urbano). No son directamente comparables entre sí sin especificar la magnitud.
- Existen **resultados contradictorios**: Li et al. 2018 reportaron que el redondeo fue la peor de las tres modificaciones de esquina, mientras que Al-Masoodi et al. 2024 (CFD) y Mandal et al. 2021 lo reportan como el más efectivo. Discutir esta dispersión en la tesis fortalece el marco teórico.
- Xie 2014 advierte que taper y setback pueden **empeorar** la respuesta para vientos de retorno corto (reduced velocity baja); no siempre es beneficioso.
- Cao et al. 2013 (túnel de viento Tongji): las modificaciones de sección no siempre son efectivas; taper ratio 1% disminuye el amortiguamiento aerodinámico, pero taper 3–5% lo aumenta.
- **Verificación propia pendiente**: cuantificar la reducción para el edificio de 15 plantas con el análisis estructural comparativo (NBR 6123 / ASCE 7 / Eurocódigo 1) y, eventualmente, CFD en etapas posteriores.