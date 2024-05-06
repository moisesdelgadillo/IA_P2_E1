# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class BusquedaPolitica:
    def __init__(self, num_estados, num_acciones, transiciones, recompensas, gamma=0.9, epsilon=1e-6):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.transiciones = transiciones  # Función de transiciones
        self.recompensas = recompensas  # Función de recompensas
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Umbral de convergencia

    def buscar(self):
        valores_estados = np.zeros(self.num_estados)

        while True:
            delta = 0
            for estado in range(self.num_estados):
                valor_estado_anterior = valores_estados[estado]
                valores_acciones = [sum([prob_transicion * (self.recompensas[(estado, accion, proximo_estado)] + self.gamma * valores_estados[proximo_estado])
                                        for proximo_estado, prob_transicion in self.transiciones[(estado, accion)].items()])
                                    for accion in range(self.num_acciones)]
                valores_estados[estado] = max(valores_acciones)
                delta = max(delta, abs(valor_estado_anterior - valores_estados[estado]))
            if delta < self.epsilon:
                break

        return valores_estados

# Ejemplo de uso
num_estados = 3
num_acciones = 2
transiciones = {
    (0, 0): {0: 0.8, 1: 0.2},
    (0, 1): {1: 0.6, 2: 0.4},
    (1, 0): {0: 0.3, 1: 0.7},
    (1, 1): {0: 0.4, 1: 0.6},
    (2, 0): {1: 0.5, 2: 0.5},
    (2, 1): {2: 0.9, 1: 0.1}
}
recompensas = {
    (0, 0, 0): 1,
    (0, 1, 1): 2,
    (1, 0, 0): 3,
    (1, 1, 0): 4,
    (2, 0, 1): 5,
    (2, 1, 2): 6
}

busqueda_politica = BusquedaPolitica(num_estados, num_acciones, transiciones, recompensas)
valores_optimos = busqueda_politica.buscar()

print("Valores óptimos de los estados:")
print(valores_optimos)
