# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

def generar_poblacion(tamano_poblacion):
    # Genera una población inicial de estados aleatorios
    poblacion = []
    for _ in range(tamano_poblacion):
        poblacion.append([random.randint(1, 8) for _ in range(8)])
    return poblacion

def calcular_costo(estado):
    # Calcula el costo de un estado, que es el número de conflictos de reinas
    costo = 0
    for i in range(len(estado)):
        for j in range(i + 1, len(estado)):
            if estado[i] == estado[j] or abs(i - j) == abs(estado[i] - estado[j]):
                costo += 1
    return costo

def seleccion_torneo(poblacion, num_participantes):
    # Realiza una selección por torneo para elegir padres
    participantes = random.sample(poblacion, num_participantes)
    return min(participantes, key=calcular_costo)

def cruzar(padre1, padre2):
    # Cruza dos padres para producir un hijo
    punto_cruce = random.randint(1, 7)
    hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
    return hijo

def mutar(estado):
    # Realiza una mutación en un estado
    pos = random.randint(0, 7)
    nuevo_valor = random.randint(1, 8)
    estado[pos] = nuevo_valor
    return estado

def algoritmo_genetico(tamano_poblacion, num_generaciones):
    poblacion = generar_poblacion(tamano_poblacion)

    for _ in range(num_generaciones):
        # Selecciona padres mediante torneo
        padres = [seleccion_torneo(poblacion, 5) for _ in range(tamano_poblacion)]

        # Realiza el cruce para producir la siguiente generación
        nueva_generacion = []
        for i in range(0, tamano_poblacion, 2):
            hijo1 = cruzar(padres[i], padres[i + 1])
            hijo2 = cruzar(padres[i + 1], padres[i])
            nueva_generacion.extend([hijo1, hijo2])

        # Realiza la mutación en la nueva generación
        poblacion = [mutar(estado) for estado in nueva_generacion]

    # Devuelve el mejor estado encontrado
    return min(poblacion, key=calcular_costo)

# Ejemplo de uso
tamano_poblacion = 100
num_generaciones = 100

solucion = algoritmo_genetico(tamano_poblacion, num_generaciones)
print("Solución encontrada:", solucion)
