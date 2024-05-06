# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def buscar_camino(grafo, inicio, objetivo):
    # Lista para almacenar el camino encontrado
    camino = []
    # Cola para realizar la búsqueda en anchura
    cola = [[inicio]]

    # Verificar si el nodo de inicio es igual al objetivo
    if inicio == objetivo:
        return "El nodo de inicio es igual al objetivo."

    # Búsqueda en anchura
    while cola:
        # Obtener el camino más corto desde la cola
        camino_actual = cola.pop(0)
        # Obtener el último nodo en el camino actual
        nodo_actual = camino_actual[-1]

        # Si el nodo actual es igual al objetivo, se ha encontrado un camino
        if nodo_actual == objetivo:
            return camino_actual

        # Verificar si el nodo actual tiene vecinos
        if nodo_actual in grafo:
            # Recorrer los vecinos del nodo actual
            for vecino in grafo[nodo_actual]:
                # Verificar si el vecino ya ha sido visitado
                if vecino not in camino_actual:
                    # Crear un nuevo camino agregando el vecino al final del camino actual
                    nuevo_camino = list(camino_actual)
                    nuevo_camino.append(vecino)
                    # Agregar el nuevo camino a la cola para explorar más adelante
                    cola.append(nuevo_camino)

    # Si no se encuentra ningún camino entre el inicio y el objetivo
    return "No se encontró ningún camino."

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
objetivo = 'F'

print(f"Buscando un camino desde '{inicio}' hasta '{objetivo}':")
resultado = buscar_camino(grafo, inicio, objetivo)
print(resultado)
