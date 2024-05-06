# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class AprendizajePorRefuerzoPasivo:
    def __init__(self, num_estados, num_acciones, epsilon=0.1, gamma=0.9):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.epsilon = epsilon  # Factor de exploración
        self.gamma = gamma  # Factor de descuento
        self.valor_estados = np.zeros(num_estados)  # Valores estimados de los estados

    def actualizar_valor_estados(self, episodios):
        for episodio in episodios:
            estados_visitados = set()
            for estado, _, recompensa in episodio:
                if estado not in estados_visitados:
                    estados_visitados.add(estado)
                    self.valor_estados[estado] += self.gamma * (recompensa - self.valor_estados[estado])

# Ejemplo de uso
num_estados = 5
num_acciones = 2
epsilon = 0.1
gamma = 0.9

agente = AprendizajePorRefuerzoPasivo(num_estados, num_acciones, epsilon, gamma)

# Ejemplo de episodios (datos observados)
episodio_1 = [(0, 0, 1), (1, 0, 2), (2, 1, 0)]
episodio_2 = [(0, 1, 3), (1, 1, 4), (2, 0, 1)]
episodio_3 = [(0, 0, 2), (1, 1, 1), (2, 1, 2)]

episodios = [episodio_1, episodio_2, episodio_3]

# Actualizar los valores estimados de los estados
agente.actualizar_valor_estados(episodios)

print("Valores estimados de los estados:")
print(agente.valor_estados)
