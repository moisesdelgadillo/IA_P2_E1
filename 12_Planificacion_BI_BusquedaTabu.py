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
    # Genera vecinos intercambiando dos reinas
    vecinos = []
    for i in range(len(estado)):
        for j in range(i + 1, len(estado)):
            vecino = list(estado)
            vecino[i], vecino[j] = vecino[j], vecino[i]
            vecinos.append(vecino)
    return vecinos

def busqueda_tabu(iteraciones_maximas):
    # Genera un estado inicial aleatorio
    estado_actual = generar_estado_inicial()
    mejor_estado = list(estado_actual)
    mejor_costo = calcular_costo(mejor_estado)
    lista_tabu = []  # Lista tabú para almacenar los movimientos prohibidos

    iteraciones = 0
    while iteraciones < iteraciones_maximas:
        vecinos = generar_vecinos(estado_actual)

        # Encuentra el mejor vecino que no esté en la lista tabú
        mejor_vecino = None
        mejor_costo_vecino = float('inf')
        for vecino in vecinos:
            costo_vecino = calcular_costo(vecino)
            if costo_vecino < mejor_costo_vecino and vecino not in lista_tabu:
                mejor_vecino = vecino
                mejor_costo_vecino = costo_vecino

        # Actualiza el mejor estado y su costo
        if mejor_vecino:
            mejor_estado = list(mejor_vecino)
            mejor_costo = mejor_costo_vecino

        # Agrega el movimiento a la lista tabú
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > 5:  # Límite de la lista tabú
            lista_tabu.pop(0)

        # Actualiza el estado actual
        estado_actual = list(mejor_vecino)

        iteraciones += 1

    return mejor_estado

# Ejemplo de uso
solucion = busqueda_tabu(1000)
print("Solución encontrada:", solucion)
