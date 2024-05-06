# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import math
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

def generar_vecino(estado):
    # Genera un vecino intercambiando dos reinas
    vecino = list(estado)
    i, j = random.sample(range(8), 2)
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino

def temple_simulado(temperatura_inicial, factor_enfriamiento, iteraciones_maximas):
    # Genera un estado inicial aleatorio
    estado_actual = generar_estado_inicial()
    mejor_estado = list(estado_actual)
    mejor_costo = calcular_costo(mejor_estado)
    temperatura_actual = temperatura_inicial

    for _ in range(iteraciones_maximas):
        vecino = generar_vecino(estado_actual)
        costo_vecino = calcular_costo(vecino)

        # Si el vecino es mejor, acepta el movimiento
        if costo_vecino < calcular_costo(estado_actual):
            estado_actual = list(vecino)
            if costo_vecino < mejor_costo:
                mejor_estado = list(vecino)
                mejor_costo = costo_vecino
        # Si el vecino es peor, acepta el movimiento con una cierta probabilidad
        else:
            probabilidad_aceptacion = math.exp(-(costo_vecino - calcular_costo(estado_actual)) / temperatura_actual)
            if random.random() < probabilidad_aceptacion:
                estado_actual = list(vecino)

        # Enfría la temperatura
        temperatura_actual *= factor_enfriamiento

    return mejor_estado

# Ejemplo de uso
temperatura_inicial = 1000
factor_enfriamiento = 0.95
iteraciones_maximas = 1000

solucion = temple_simulado(temperatura_inicial, factor_enfriamiento, iteraciones_maximas)
print("Solución encontrada:", solucion)
