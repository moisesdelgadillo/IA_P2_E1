# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class QLearning:
    def __init__(self, num_estados, num_acciones, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Factor de exploración
        self.Q = np.zeros((num_estados, num_acciones))  # Valores Q

    def seleccionar_accion(self, estado):
        if np.random.rand() < self.epsilon:
            # Exploración: seleccionar una acción aleatoria
            return np.random.randint(self.num_acciones)
        else:
            # Explotación: seleccionar la mejor acción según los valores Q
            return np.argmax(self.Q[estado])

    def actualizar_Q(self, estado, accion, recompensa, proximo_estado):
        mejor_siguiente_accion = np.argmax(self.Q[proximo_estado])
        nuevo_valor_Q = self.Q[estado, accion] + self.alpha * (recompensa + self.gamma * self.Q[proximo_estado, mejor_siguiente_accion] - self.Q[estado, accion])
        self.Q[estado, accion] = nuevo_valor_Q

# Ejemplo de uso
num_estados = 3
num_acciones = 2
alpha = 0.5
gamma = 0.9
epsilon = 0.1

agente = QLearning(num_estados, num_acciones, alpha, gamma, epsilon)

# Ejemplo de interacción con el entorno y actualización de valores Q
estado_actual = 0
accion = agente.seleccionar_accion(estado_actual)
recompensa = 1
proximo_estado = 1

agente.actualizar_Q(estado_actual, accion, recompensa, proximo_estado)

print("Valores Q:")
print(agente.Q)
