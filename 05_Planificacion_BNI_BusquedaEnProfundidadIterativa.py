# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def agregar_conexion(grafo, ciudad1, ciudad2):
    """
    Agrega una conexión entre dos ciudades en el grafo.

    Args:
    - grafo: diccionario que representa el grafo.
    - ciudad1: nombre de la primera ciudad.
    - ciudad2: nombre de la segunda ciudad.
    """
    if ciudad1 not in grafo:
        grafo[ciudad1] = []
    if ciudad2 not in grafo:
        grafo[ciudad2] = []
    grafo[ciudad1].append(ciudad2)
    grafo[ciudad2].append(ciudad1)

def dls_util(grafo, ciudad, visitado, profundidad_max, profundidad_actual):
    """
    Función utilitaria para la búsqueda en profundidad iterativa (IDDFS).

    Args:
    - grafo: diccionario que representa el grafo.
    - ciudad: nombre de la ciudad actual.
    - visitado: conjunto que contiene las ciudades visitadas.
    - profundidad_max: profundidad máxima permitida para la búsqueda.
    - profundidad_actual: profundidad actual en la búsqueda.
    """
    visitado.add(ciudad)
    print(ciudad, end=" ")

    if profundidad_actual < profundidad_max:
        for vecino in grafo[ciudad]:
            if vecino not in visitado:
                dls_util(grafo, vecino, visitado, profundidad_max, profundidad_actual + 1)

def iddfs(grafo, ciudad_inicial, profundidad_max):
    """
    Realiza la búsqueda en profundidad iterativa (IDDFS) en el grafo, comenzando desde la ciudad inicial.

    Args:
    - grafo: diccionario que representa el grafo.
    - ciudad_inicial: nombre de la ciudad inicial.
    - profundidad_max: profundidad máxima permitida para la búsqueda.
    """
    for profundidad_actual in range(profundidad_max + 1):
        visitado = set()
        print(f"Profundidad máxima: {profundidad_actual}")
        dls_util(grafo, ciudad_inicial, visitado, profundidad_actual, 0)

# Ejemplo de uso
mapa = {}
agregar_conexion(mapa, "Ciudad A", "Ciudad B")
agregar_conexion(mapa, "Ciudad A", "Ciudad C")
agregar_conexion(mapa, "Ciudad B", "Ciudad D")
agregar_conexion(mapa, "Ciudad C", "Ciudad E")
agregar_conexion(mapa, "Ciudad D", "Ciudad F")
agregar_conexion(mapa, "Ciudad E", "Ciudad F")

print("Búsqueda en profundidad iterativa desde 'Ciudad A' con profundidad máxima de 2:")
iddfs(mapa, "Ciudad A", 2)
