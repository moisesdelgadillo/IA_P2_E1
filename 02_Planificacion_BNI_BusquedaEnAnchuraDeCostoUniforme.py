# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1
# La búsqueda en anchura de costo uniforme es una variante de la búsqueda en anchura en la que se tiene en cuenta el costo de las aristas. En este caso, se garantiza que la búsqueda encuentre la ruta más corta en términos de costo entre el nodo inicial y cualquier otro nodo alcanzable.

import heapq  # Importa el módulo heapq para utilizar colas de prioridad

class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializa el grafo como un diccionario vacío

    def agregar_arista(self, u, v, costo):
        # Agrega la arista al grafo junto con su costo asociado
        # Añade la arista en ambas direcciones ya que el grafo no dirigido se está considerando
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append((v, costo))
        self.grafo[v].append((u, costo))

    def busqueda_anchura_costo_uniforme(self, inicio, objetivo):
        cola = [(0, inicio)]  # Inicializa una cola de prioridad con el costo 0 y el nodo inicial
        visitado = set()  # Crea un conjunto para almacenar los nodos visitados

        while cola:  # Mientras la cola no esté vacía
            costo, vertice = heapq.heappop(cola)  # Extrae el nodo de la cola con el menor costo

            if vertice == objetivo:  # Si el nodo extraído es el objetivo
                return costo  # Retorna el costo acumulado hasta ese momento

            if vertice not in visitado:  # Si el nodo no ha sido visitado
                visitado.add(vertice)  # Agrega el nodo al conjunto de visitados
                for vecino, costo_arista in self.grafo[vertice]:  # Itera sobre los vecinos del nodo actual
                    if vecino not in visitado:  # Si el vecino no ha sido visitado
                        # Añade el vecino a la cola de prioridad junto con el costo acumulado
                        heapq.heappush(cola, (costo + costo_arista, vecino))

# Ejemplo de uso
g = Grafo()  # Crea una instancia de la clase Grafo
g.agregar_arista('A', 'B', 1)  # Agrega una arista del nodo 'A' al nodo 'B' con costo 1
g.agregar_arista('A', 'C', 3)  # Agrega una arista del nodo 'A' al nodo 'C' con costo 3
g.agregar_arista('B', 'C', 1)  # Agrega una arista del nodo 'B' al nodo 'C' con costo 1
g.agregar_arista('B', 'D', 5)  # Agrega una arista del nodo 'B' al nodo 'D' con costo 5
g.agregar_arista('C', 'D', 2)  # Agrega una arista del nodo 'C' al nodo 'D' con costo 2

# Realiza la búsqueda en anchura de costo uniforme desde el nodo 'A' al nodo 'D' y muestra el costo mínimo
costo_minimo = g.busqueda_anchura_costo_uniforme('A', 'D')
print("El costo mínimo desde el nodo A al nodo D es:", costo_minimo)
