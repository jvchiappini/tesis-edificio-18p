"""
===============================================================================
TESIS DE GRADO - INGENIERÍA CIVIL
MÓDULO: 01_Geometria_Terreno / geometria_terreno.py
AUTOR: José Valentino Chiappini Vergara
DESCRIPCIÓN: Verificación rigurosa de planimetría, coordenadas UTM WGS84 Zona 21J,
             extraídas mediante teledetección satelital (Google Earth Pro),
             identificación de vías públicas (Calle Los Lapachos, Calle Los Sauces,
             Av. Itaipú Oeste), lindero privado residencial P3-P4, cálculo de área 
             por regla de Gauss/Shoelace, azimuts, ángulos interiores, cuña P1 y FOS/FOT.
===============================================================================
"""

import math

def calcular_geometria_terreno():
    # Coordenadas UTM WGS84 Zona 21J (Ciudad del Este, Paraguay)
    # Fuente: Teledetección / Digitalización Satelital (Google Earth Pro)
    vertices = {
        "P1": (737721.76, 7176185.26),
        "P2": (737837.53, 7176203.96),
        "P3": (737853.36, 7176246.13),
        "P4": (737755.78, 7176281.93)
    }

    nombres_vias = {
        "P1->P2": "Calle Los Lapachos (Frente Principal)",
        "P2->P3": "Calle Los Sauces (Acceso Secundario)",
        "P3->P4": "Inmueble Residencial Privado (Lindero Posterior / Predio Vecino)",
        "P4->P1": "Av. Itaipú Oeste (Frente Secundario / Lindero Lateral)"
    }

    nombres = ["P1", "P2", "P3", "P4"]
    pts = [vertices[k] for k in nombres]
    n = len(pts)

    # 1. Distancias de Lados (m)
    lados = {}
    for i in range(n):
        p_actual = pts[i]
        p_siguiente = pts[(i + 1) % n]
        nombre_lado = f"{nombres[i]}->{nombres[(i + 1) % n]}"
        dist = math.hypot(p_siguiente[0] - p_actual[0], p_siguiente[1] - p_actual[1])
        lados[nombre_lado] = dist

    perimetro_total = sum(lados.values())

    # 2. Área por Algoritmo de Shoelace (Gauss) en coordenadas relativas a P1
    p1 = pts[0]
    area_shoelace = 0.5 * abs(sum(
        (pts[i][0] - p1[0]) * (pts[(i + 1) % n][1] - p1[1]) -
        (pts[(i + 1) % n][0] - p1[0]) * (pts[i][1] - p1[1])
        for i in range(n)
    ))

    # 3. Azimuts (grados sexagesimales desde el Norte verdadero en sentido horario)
    azimuts = {}
    for i in range(n):
        p_actual = pts[i]
        p_siguiente = pts[(i + 1) % n]
        dx = p_siguiente[0] - p_actual[0]
        dy = p_siguiente[1] - p_actual[1]
        az = math.degrees(math.atan2(dx, dy)) % 360.0
        azimuts[f"{nombres[i]}->{nombres[(i + 1) % n]}"] = az

    # 4. Ángulos Interiores Vectoriales (grados)
    angulos = {}
    for i in range(n):
        p_ant = pts[(i - 1) % n]
        p_act = pts[i]
        p_sig = pts[(i + 1) % n]

        v1 = (p_sig[0] - p_act[0], p_sig[1] - p_act[1])
        v2 = (p_ant[0] - p_act[0], p_ant[1] - p_act[1])

        dot = v1[0] * v2[0] + v1[1] * v2[1]
        det = v1[0] * v2[1] - v1[1] * v2[0]

        ang = math.degrees(math.atan2(det, dot))
        if ang < 0:
            ang += 360.0
        angulos[nombres[i]] = ang

    suma_angulos = sum(angulos.values())

    # 5. Geometría de la Cuña en P1
    alpha_p1_rad = math.radians(angulos["P1"])
    u_cuña = 27.0
    h_cuña = u_cuña * math.tan(alpha_p1_rad)
    hyp_cuña = u_cuña / math.cos(alpha_p1_rad)
    area_cuña = 0.5 * u_cuña * h_cuña

    # 6. Indicadores Urbanísticos CDE (FOS y FOT)
    fos_max = 0.70
    fot_max = 4.0
    area_huella_max = fos_max * area_shoelace
    area_construible_max = fot_max * area_shoelace

    huella_adoptada = 85.0 * 37.0
    fos_real = huella_adoptada / area_shoelace
    
    pisos_residenciales = 18
    area_sobre_rasante = (pisos_residenciales + 1) * huella_adoptada

    # Reporte
    print("=" * 85)
    print("REPORTE TÉCNICO DE PLANIMETRÍA Y GEOMETRÍA DEL TERRENO (ETAPA A.1)")
    print("=" * 85)
    print("MÉTODO DE OBTENCIÓN: Teledetección Satelital / Digitalización (Google Earth Pro v7.3)")
    print("SISTEMA DE REFERENCIA: UTM Zona 21J - Dátum WGS84 / SIRGAS2000")
    print("-" * 85)
    print(f"Superficie Bruta (Gauss/Shoelace): {area_shoelace:.2f} m² (7.618,49 m² nominal)")
    print(f"Perímetro Total: {perimetro_total:.3f} m")
    print("-" * 85)
    print("DELIMITACIÓN DE VÍAS PÚBLICAS Y LINDEROS:")
    for k, v in lados.items():
        print(f"  Lado {k} ({nombres_vias[k]}):")
        print(f"    - Longitud: {v:.3f} m | Azimut: {azimuts[k]:.2f}°")
    print("-" * 85)
    print("ÁNGULOS INTERIORES:")
    for k, v in angulos.items():
        print(f"  Vértice {k}: {v:.4f}°")
    print(f"Suma de Ángulos Interiores: {suma_angulos:.2f}° (Cierre teórico = 360,00°)")
    print("-" * 85)
    print("CUÑA NO EDIFICABLE EN INTERSECCIÓN P1 (Av. Itaipú Oeste / Calle Los Lapachos - 61,44°):")
    print(f"  Distancia sobre Calle Los Lapachos (P1->P2): {u_cuña:.2f} m")
    print(f"  Altura perpendicular: {h_cuña:.2f} m")
    print(f"  Hipotenusa sobre Av. Itaipú Oeste (P1->P4): {hyp_cuña:.2f} m")
    print(f"  Superficie de Cuña/Jardín: {area_cuña:.2f} m²")
    print("-" * 85)
    print("INDICADORES URBANÍSTICOS (MUNICIPALIDAD CDE):")
    print(f"  Área Máxima FOS (0,70): {area_huella_max:.2f} m²")
    print(f"  Huella Adoptada: {huella_adoptada:.2f} m² (FOS Real = {fos_real*100:.2f}% <= 70,00% -> CUMPLE)")
    print(f"  Área Máxima FOT (4,0): {area_construible_max:.2f} m²")
    print(f"  Superficie Sobre Rasante Proyectada (PB+18P): {area_sobre_rasante:.2f} m²")
    print(f"  Estado FOT: Requiere Varianza Municipal por {area_sobre_rasante - area_construible_max:.2f} m² excedentarios")
    print("=" * 85)

if __name__ == "__main__":
    calcular_geometria_terreno()
