# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1
#la búsqueda en anchura es un algoritmo simple pero potente para encontrar la ruta más corta en un grafo no dirigido o dirigido con costos uniformes.

from collections import defaultdict, deque  # Importa defaultdict de la biblioteca collections y deque de la biblioteca collections

class Grafo:  # Define una clase Grafo
    def __init__(self):  # Define el método __init__ para inicializar la clase
        self.grafo = defaultdict(list)  # Crea un diccionario predeterminado con valores de lista para almacenar el grafo

    def agregar_arista(self, u, v):  # Define el método para agregar aristas al grafo
        self.grafo[u].append(v)  # Añade el vértice v a la lista de adyacencia del vértice u

    def bfs(self, inicio):  # Define el método para la búsqueda en anchura
        visitado = set()  # Crea un conjunto para almacenar los vértices visitados
        cola = deque([inicio])  # Crea una cola (deque) con el vértice de inicio
        visitado.add(inicio)  # Añade el vértice de inicio al conjunto de visitados

        while cola:  # Inicia un bucle mientras la cola no esté vacía
            vertice = cola.popleft()  # Elimina y devuelve el primer elemento de la cola (FIFO)
            print(vertice, end=" ")  # Imprime el vértice actual sin cambiar de línea

            for vecino in self.grafo[vertice]:  # Itera sobre los vecinos del vértice actual
                if vecino not in visitado:  # Verifica si el vecino no ha sido visitado
                    cola.append(vecino)  # Añade el vecino a la cola
                    visitado.add(vecino)  # Añade el vecino al conjunto de visitados

# Ejemplo de uso
g = Grafo()  # Crea una instancia de la clase Grafo
g.agregar_arista(0, 1)  # Agrega una arista del vértice 0 al vértice 1
g.agregar_arista(0, 2)  # Agrega una arista del vértice 0 al vértice 2
g.agregar_arista(1, 2)  # Agrega una arista del vértice 1 al vértice 2
g.agregar_arista(2, 0)  # Agrega una arista del vértice 2 al vértice 0
g.agregar_arista(2, 3)  # Agrega una arista del vértice 2 al vértice 3
g.agregar_arista(3, 3)  # Agrega una arista del vértice 3 al vértice 3

print("Recorrido en anchura empezando desde el vértice 2:")  # Imprime un mensaje
g.bfs(2)  # Realiza la búsqueda en anchura desde el vértice 2 y muestra el resultado
