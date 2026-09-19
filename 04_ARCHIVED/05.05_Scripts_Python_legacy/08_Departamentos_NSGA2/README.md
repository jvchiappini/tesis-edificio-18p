# 08_Departamentos_NSGA2

Módulo (a desarrollar) para la **micro-distribución de departamentos** mediante **NSGA-II**,
incorporando la **simulación de recorridos peatonales** y las **reglas lógicas de arquitectura**.

## Estado

**⏳ Especificación lista, código pendiente.**

## Documentación de referencia (leer antes de programar)

- Especificación completa: `07_KNOWLEDGE_BASE/07.05_Optimizacion_Algoritmica/NSGA2_Microdistribucion_Departamentos_v01.md`
- Catálogo de ideas algorítmicas: `07_KNOWLEDGE_BASE/07.05_Optimizacion_Algoritmica/Ideas_Algoritmos_Tesis_v01.md`

## Puntos clave (no olvidar)

1. **La puerta de entrada del departamento es un dato FIJO** del que parte toda la distribución.
2. Se respetan las **reglas duras** de arquitectura (p. ej. el baño no enfrenta al comedor; la cocina no abre a los dormitorios; todo ambiente habitable ilumina y ventila).
3. La **circulación peatonal** es un objetivo del algoritmo (recorridos desde la entrada a cada ambiente).
4. Las salidas (`outputs/`) son planos PNG + métricas CSV/JSON + genotipo para Revit/Dynamo.

## Uso previsto

```
python ga_departamento_tipo.py        # (por crear)
```

Guardar figuras y datos en `outputs/`.
