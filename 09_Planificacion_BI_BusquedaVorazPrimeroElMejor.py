# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import math

def distancia_euclidiana(ciudad1, ciudad2):
    # Calcula la distancia euclidiana entre dos ciudades en un plano 2D
    return math.sqrt((ciudad1[0] - ciudad2[0]) ** 2 + (ciudad1[1] - ciudad2[1]) ** 2)

def buscar_camino_voraz(grafo, inicio, objetivo):
    # Estructura de datos para almacenar los nodos por visitar
    por_visitar = [(inicio, distancia_euclidiana(inicio, objetivo))]
    padres = {inicio: None}  # Diccionario para almacenar el nodo padre de cada nodo

    while por_visitar:
        # Selecciona el nodo con la menor heurística (distancia a la meta)
        nodo_actual, _ = min(por_visitar, key=lambda x: x[1])

        # Si el nodo actual es el objetivo, reconstruye el camino y devuelve
        if nodo_actual == objetivo:
            camino = []
            while nodo_actual:
                camino.insert(0, nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino

        # Elimina el nodo actual de la lista por_visitar
        por_visitar.remove((nodo_actual, distancia_euclidiana(nodo_actual, objetivo)))

        # Explora los vecinos del nodo actual
        for vecino, _ in grafo[nodo_actual].items():
            # Si el vecino no ha sido visitado
            if vecino not in padres:
                # Actualiza el padre del vecino y agrega el vecino a la lista por_visitar
                padres[vecino] = nodo_actual
                por_visitar.append((vecino, distancia_euclidiana(vecino, objetivo)))

    # Si no se encontró un camino
    return None

# Ejemplo de uso
grafo = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 8},
    'C': {'A': 10, 'B': 3, 'D': 2},
    'D': {'B': 8, 'C': 2}
}

inicio = 'A'
objetivo = 'D'

print(f"Buscando el camino más corto desde '{inicio}' hasta '{objetivo}' utilizando Búsqueda Voraz Primero el Mejor:")
camino = buscar_camino_voraz(grafo, inicio, objetivo)
if camino:
    print("El camino encontrado es:", camino)
else:
    print("No se encontró ningún camino.")
