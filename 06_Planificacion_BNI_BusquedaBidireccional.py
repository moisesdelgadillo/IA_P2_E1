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

def busqueda_bidireccional(grafo, inicio, objetivo):
    """
    Realiza la búsqueda bidireccional en el grafo desde el inicio hasta el objetivo.

    Args:
    - grafo: diccionario que representa el grafo.
    - inicio: nombre de la ciudad de inicio.
    - objetivo: nombre de la ciudad objetivo.
    """
    # Conjuntos para almacenar las ciudades visitadas desde el inicio y el objetivo.
    visitado_inicio = set()
    visitado_objetivo = set()
    # Colas para almacenar las ciudades por visitar desde el inicio y el objetivo.
    cola_inicio = [inicio]
    cola_objetivo = [objetivo]

    while cola_inicio and cola_objetivo:
        # Realiza la búsqueda desde el inicio.
        ciudad_actual_inicio = cola_inicio.pop(0)
        visitado_inicio.add(ciudad_actual_inicio)
        print(f"Búsqueda desde el inicio: {ciudad_actual_inicio}")

        # Verifica si la ciudad actual es un estado objetivo.
        if ciudad_actual_inicio in visitado_objetivo:
            print("¡Se encontró una ruta!")
            return

        for vecino in grafo[ciudad_actual_inicio]:
            if vecino not in visitado_inicio:
                cola_inicio.append(vecino)

        # Realiza la búsqueda desde el objetivo.
        ciudad_actual_objetivo = cola_objetivo.pop(0)
        visitado_objetivo.add(ciudad_actual_objetivo)
        print(f"Búsqueda desde el objetivo: {ciudad_actual_objetivo}")

        # Verifica si la ciudad actual es un estado objetivo.
        if ciudad_actual_objetivo in visitado_inicio:
            print("¡Se encontró una ruta!")
            return

        for vecino in grafo[ciudad_actual_objetivo]:
            if vecino not in visitado_objetivo:
                cola_objetivo.append(vecino)

# Ejemplo de uso
mapa = {}
agregar_conexion(mapa, "Ciudad A", "Ciudad B")
agregar_conexion(mapa, "Ciudad A", "Ciudad C")
agregar_conexion(mapa, "Ciudad B", "Ciudad D")
agregar_conexion(mapa, "Ciudad C", "Ciudad E")
agregar_conexion(mapa, "Ciudad D", "Ciudad F")
agregar_conexion(mapa, "Ciudad E", "Ciudad F")

print("Búsqueda bidireccional desde 'Ciudad A' hasta 'Ciudad F':")
busqueda_bidireccional(mapa, "Ciudad A", "Ciudad F")
