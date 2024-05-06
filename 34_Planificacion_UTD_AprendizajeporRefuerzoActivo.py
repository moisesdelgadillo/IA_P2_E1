# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class AprendizajePorRefuerzoActivo:
    def __init__(self, num_estados, num_acciones, epsilon=0.1, gamma=0.9, valor_inicial=0):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.epsilon = epsilon  # Factor de exploración
        self.gamma = gamma  # Factor de descuento
        self.valor_estados_acciones = np.full((num_estados, num_acciones), valor_inicial)  # Valores estimados de los estados-acciones

    def seleccionar_accion(self, estado):
        if np.random.rand() < self.epsilon:
            # Exploración: seleccionar una acción aleatoria
            return np.random.randint(self.num_acciones)
        else:
            # Explotación: seleccionar la mejor acción según los valores estimados
            return np.argmax(self.valor_estados_acciones[estado])

    def actualizar_valor_estados_acciones(self, estado, accion, recompensa, proximo_estado):
        mejor_siguiente_accion = np.argmax(self.valor_estados_acciones[proximo_estado])
        valor_objetivo = recompensa + self.gamma * self.valor_estados_acciones[proximo_estado, mejor_siguiente_accion]
        error = valor_objetivo - self.valor_estados_acciones[estado, accion]
        self.valor_estados_acciones[estado, accion] += error

# Ejemplo de uso
num_estados = 5
num_acciones = 2
epsilon = 0.1
gamma = 0.9
valor_inicial = 0

agente = AprendizajePorRefuerzoActivo(num_estados, num_acciones, epsilon, gamma, valor_inicial)

# Ejemplo de interacción con el entorno y actualización de valores
estado_actual = 0
accion = agente.seleccionar_accion(estado_actual)
recompensa = 1
proximo_estado = 1

agente.actualizar_valor_estados_acciones(estado_actual, accion, recompensa, proximo_estado)

print("Valores estimados de los estados-acciones:")
print(agente.valor_estados_acciones)
