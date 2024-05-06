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

def busqueda_ascension_colinas():
    # Genera un estado inicial aleatorio
    estado_actual = generar_estado_inicial()
    costo_actual = calcular_costo(estado_actual)

    while True:
        # Si no hay conflictos, se ha encontrado la solución
        if costo_actual == 0:
            return estado_actual

        # Encuentra la mejor vecindad (estado vecino con menor costo)
        mejor_estado = estado_actual
        mejor_costo = costo_actual
        for i in range(len(estado_actual)):
            for j in range(1, 9):
                if estado_actual[i] != j:
                    vecino = list(estado_actual)
                    vecino[i] = j
                    costo_vecino = calcular_costo(vecino)
                    if costo_vecino < mejor_costo:
                        mejor_estado = vecino
                        mejor_costo = costo_vecino

        # Si no hay mejora, se alcanzó un óptimo local
        if mejor_costo >= costo_actual:
            return estado_actual

        # Actualiza el estado actual con el mejor estado encontrado
        estado_actual = mejor_estado
        costo_actual = mejor_costo

# Ejemplo de uso
solucion = busqueda_ascension_colinas()
print("Solución encontrada:", solucion)
