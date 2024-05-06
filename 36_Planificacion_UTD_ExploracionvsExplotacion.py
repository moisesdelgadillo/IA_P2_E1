# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class EstrategiaEpsilonGreedy:
    def __init__(self, num_acciones, epsilon):
        self.num_acciones = num_acciones
        self.epsilon = epsilon  # Factor de exploración

    def seleccionar_accion(self, valores_acciones):
        if np.random.rand() < self.epsilon:
            # Exploración: seleccionar una acción aleatoria
            return np.random.randint(self.num_acciones)
        else:
            # Explotación: seleccionar la mejor acción según los valores estimados
            return np.argmax(valores_acciones)

# Ejemplo de uso
num_acciones = 3
epsilon = 0.1

estrategia = EstrategiaEpsilonGreedy(num_acciones, epsilon)

# Ejemplo de selección de acción
valores_acciones = [1, 2, 3]
accion_seleccionada = estrategia.seleccionar_accion(valores_acciones)

print("Acción seleccionada:", accion_seleccionada)
