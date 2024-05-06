# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import math

def distancia_euclidiana(ciudad1, ciudad2):
    # Calcula la distancia euclidiana entre dos ciudades en un plano 2D
    return math.sqrt((ciudad1[0] - ciudad2[0]) ** 2 + (ciudad1[1] - ciudad2[1]) ** 2)

def a_estrella(grafo, inicio, objetivo):
    # Estructuras de datos para almacenar los nodos visitados y los nodos por visitar
    visitados = set()
    por_visitar = [(inicio, 0, distancia_euclidiana(inicio, objetivo))]
    padres = {inicio: None}  # Diccionario para almacenar el nodo padre de cada nodo
    costos = {inicio: 0}  # Diccionario para almacenar los costos acumulados desde el inicio

    while por_visitar:
        # Selecciona el nodo con el menor costo total estimado de la lista por_visitar
        nodo_actual, costo_acumulado, estimacion = min(por_visitar, key=lambda x: x[1] + x[2])

        # Si el nodo actual es el objetivo, reconstruye el camino y devuelve
        if nodo_actual == objetivo:
            camino = []
            while nodo_actual:
                camino.insert(0, nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino

        # Marca el nodo actual como visitado y lo elimina de la lista por_visitar
        visitados.add(nodo_actual)
        por_visitar.remove((nodo_actual, costo_acumulado, estimacion))

        # Explora los vecinos del nodo actual
        for vecino, costo in grafo[nodo_actual].items():
            # Calcula el costo acumulado hasta el vecino
            nuevo_costo = costo_acumulado + costo
            # Si el vecino ya ha sido visitado y el nuevo costo es mayor que el costo existente, omite este vecino
            if vecino in visitados and nuevo_costo >= costos.get(vecino, math.inf):
                continue
            # Actualiza el costo acumulado y el nodo padre si se encuentra un camino mejor
            padres[vecino] = nodo_actual
            costos[vecino] = nuevo_costo
            estimacion = distancia_euclidiana(vecino, objetivo)
            por_visitar.append((vecino, nuevo_costo, estimacion))

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

print(f"Buscando el camino más corto desde '{inicio}' hasta '{objetivo}' utilizando A*:")
camino = a_estrella(grafo, inicio, objetivo)
if camino:
    print("El camino encontrado es:", camino)
else:
    print("No se encontró ningún camino.")
