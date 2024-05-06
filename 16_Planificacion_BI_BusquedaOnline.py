# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def busqueda_en_linea(raiz, objetivo):
    # Inicializa una lista para almacenar los nodos que se van a explorar
    nodos_por_explorar = [raiz]

    # Mientras haya nodos por explorar
    while nodos_por_explorar:
        # Toma el siguiente nodo de la lista
        nodo_actual = nodos_por_explorar.pop(0)

        # Verifica si el nodo actual contiene el valor objetivo
        if nodo_actual.valor == objetivo:
            return True

        # Agrega los nodos hijos a la lista de nodos por explorar
        if nodo_actual.izquierda:
            nodos_por_explorar.append(nodo_actual.izquierda)
        if nodo_actual.derecha:
            nodos_por_explorar.append(nodo_actual.derecha)

    # Si no se encontró el objetivo en el árbol
    return False

# Ejemplo de uso
# Construcción del árbol binario de búsqueda
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)
raiz.derecha.izquierda = Nodo(12)
raiz.derecha.derecha = Nodo(18)

# Busqueda en linea
objetivo = 7
if busqueda_en_linea(raiz, objetivo):
    print(f"El valor {objetivo} se encontró en el árbol.")
else:
    print(f"El valor {objetivo} no se encontró en el árbol.")
