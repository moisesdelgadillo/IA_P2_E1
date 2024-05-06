# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

class MDP:
    def __init__(self, estados, acciones, recompensas, transiciones, gamma):
        self.estados = estados  # Conjunto de estados
        self.acciones = acciones  # Conjunto de acciones
        self.recompensas = recompensas  # Función de recompensas
        self.transiciones = transiciones  # Función de transiciones
        self.gamma = gamma  # Factor de descuento

    def obtener_transicion(self, estado, accion):
        # Devuelve las probabilidades de transición para un estado y acción dados
        return self.transiciones[(estado, accion)]

    def obtener_recompensa(self, estado, accion, proximo_estado):
        # Devuelve la recompensa para un estado, acción y próximo estado dados
        return self.recompensas[(estado, accion, proximo_estado)]

# Ejemplo de uso
estados = ['s1', 's2']
acciones = ['a1', 'a2']
recompensas = {('s1', 'a1', 's2'): 10, ('s1', 'a2', 's2'): 0, ('s2', 'a1', 's2'): 50}
transiciones = {('s1', 'a1'): {'s2': 0.6, 's1': 0.4}, ('s1', 'a2'): {'s2': 0.3, 's1': 0.7}, ('s2', 'a1'): {'s2': 0.8, 's1': 0.2}}
gamma = 0.9

mdp = MDP(estados, acciones, recompensas, transiciones, gamma)

# Ejemplo de cómo acceder a la función de transiciones y recompensas
estado = 's1'
accion = 'a1'
proximo_estado = 's2'
prob_transicion = mdp.obtener_transicion(estado, accion)[proximo_estado]
recompensa = mdp.obtener_recompensa(estado, accion, proximo_estado)

print(f"Probabilidad de transición de {estado} a {proximo_estado} con acción {accion}: {prob_transicion}")
print(f"Recompensa al moverse de {estado} a {proximo_estado} con acción {accion}: {recompensa}")
