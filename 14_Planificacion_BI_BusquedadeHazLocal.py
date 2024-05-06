# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

def generar_estado_inicial():
    # Genera un estado inicial aleatorio
    return [random.randint(1, 8) for _ in range(8)]

def calcular_costo(estado):
    # Calcula el costo de un estado, que es el número de conflictos de reinas
    costo = 0
    for i in range(len(estado)):
        for j in range(i + 1, len(estado)):
            if estado[i] == estado[j] or abs(i - j) == abs(estado[i] - estado[j]):
                costo += 1
    return costo

def generar_vecinos(estado):
    # Genera todos los vecinos intercambiando dos reinas
    vecinos = []
    for i in range(len(estado)):
        for j in range(1, 9):
            if estado[i] != j:
                vecino = list(estado)
                vecino[i] = j
                vecinos.append(vecino)
    return vecinos

def busqueda_haz_local(beam_width, iteraciones_maximas):
    # Genera un estado inicial aleatorio
    estado_actual = generar_estado_inicial()
    mejor_estado = list(estado_actual)
    mejor_costo = calcular_costo(mejor_estado)

    for _ in range(iteraciones_maximas):
        vecinos = generar_vecinos(estado_actual)
        vecinos.sort(key=calcular_costo)  # Ordena los vecinos por costo

        # Actualiza el estado actual con el mejor vecino
        estado_actual = vecinos[0]
        costo_actual = calcular_costo(estado_actual)

        # Actualiza el mejor estado si es necesario
        if costo_actual < mejor_costo:
            mejor_estado = list(estado_actual)
            mejor_costo = costo_actual

        # Termina si todos los vecinos tienen el mismo costo
        if len(set(map(tuple, vecinos))) == 1:
            break

        # Selecciona los mejores vecinos para la siguiente iteración
        estado_actual = random.sample(vecinos[:beam_width], 1)[0]

    return mejor_estado

# Ejemplo de uso
beam_width = 5
iteraciones_maximas = 1000

solucion = busqueda_haz_local(beam_width, iteraciones_maximas)
print("Solución encontrada:", solucion)
