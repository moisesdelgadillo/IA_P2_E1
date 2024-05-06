# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def agregar_conexion(grafo, ciudad1, ciudad2):
    if ciudad1 not in grafo:
        grafo[ciudad1] = []
    if ciudad2 not in grafo:
        grafo[ciudad2] = []
    grafo[ciudad1].append(ciudad2)
    grafo[ciudad2].append(ciudad1)

def dfs_util(grafo, ciudad, visitado):
    visitado.add(ciudad)
    print(ciudad, end=" ")

    for vecino in grafo[ciudad]:
        if vecino not in visitado:
            dfs_util(grafo, vecino, visitado)

def busqueda_profundidad(grafo, ciudad_inicial):
    visitado = set()
    dfs_util(grafo, ciudad_inicial, visitado)

# Ejemplo de uso
mapa = {}
agregar_conexion(mapa, "Ciudad A", "Ciudad B")
agregar_conexion(mapa, "Ciudad A", "Ciudad C")
agregar_conexion(mapa, "Ciudad B", "Ciudad D")
agregar_conexion(mapa, "Ciudad C", "Ciudad E")
agregar_conexion(mapa, "Ciudad D", "Ciudad F")
agregar_conexion(mapa, "Ciudad E", "Ciudad F")

print("Ciudades conectadas a partir de 'Ciudad A':")
busqueda_profundidad(mapa, "Ciudad B")
