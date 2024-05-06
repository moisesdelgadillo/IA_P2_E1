# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

class POMDP:
    def __init__(self, estados, acciones, observaciones, recompensas, transiciones, observaciones_transiciones, gamma):
        self.estados = estados  # Conjunto de estados
        self.acciones = acciones  # Conjunto de acciones
        self.observaciones = observaciones  # Conjunto de observaciones
        self.recompensas = recompensas  # Función de recompensas
        self.transiciones = transiciones  # Función de transiciones
        self.observaciones_transiciones = observaciones_transiciones  # Función de transiciones de observaciones
        self.gamma = gamma  # Factor de descuento

    def obtener_transicion(self, estado, accion):
        # Devuelve las probabilidades de transición para un estado y acción dados
        return self.transiciones[(estado, accion)]

    def obtener_recompensa(self, estado, accion, proximo_estado):
        # Devuelve la recompensa para un estado, acción y próximo estado dados
        return self.recompensas[(estado, accion, proximo_estado)]

    def obtener_transicion_observacion(self, estado, accion, observacion):
        # Devuelve las probabilidades de transición de observaciones para un estado, acción y observación dados
        return self.observaciones_transiciones[(estado, accion, observacion)]

# Ejemplo de uso
estados = ['s1', 's2']
acciones = ['a1', 'a2']
observaciones = ['o1', 'o2']
recompensas = {('s1', 'a1', 's2'): 10, ('s1', 'a2', 's2'): 0, ('s2', 'a1', 's2'): 50}
transiciones = {('s1', 'a1'): {'s2': 0.6, 's1': 0.4}, ('s1', 'a2'): {'s2': 0.3, 's1': 0.7}, ('s2', 'a1'): {'s2': 0.8, 's1': 0.2}}
observaciones_transiciones = {('s1', 'a1', 'o1'): {'s2': 0.7, 's1': 0.3}, ('s1', 'a1', 'o2'): {'s2': 0.2, 's1': 0.8}, 
                              ('s1', 'a2', 'o1'): {'s2': 0.4, 's1': 0.6}, ('s1', 'a2', 'o2'): {'s2': 0.1, 's1': 0.9},
                              ('s2', 'a1', 'o1'): {'s2': 0.5, 's1': 0.5}, ('s2', 'a1', 'o2'): {'s2': 0.3, 's1': 0.7}}
gamma = 0.9

pomdp = POMDP(estados, acciones, observaciones, recompensas, transiciones, observaciones_transiciones, gamma)

# Ejemplo de cómo acceder a las funciones de transiciones y recompensas
estado = 's1'
accion = 'a1'
proximo_estado = 's2'
observacion = 'o1'

prob_transicion = pomdp.obtener_transicion(estado, accion)[proximo_estado]
recompensa = pomdp.obtener_recompensa(estado, accion, proximo_estado)
prob_transicion_obs = pomdp.obtener_transicion_observacion(estado, accion, observacion)[proximo_estado]

print(f"Probabilidad de transición de {estado} a {proximo_estado} con acción {accion}: {prob_transicion}")
print(f"Recompensa al moverse de {estado} a {proximo_estado} con acción {accion}: {recompensa}")
print(f"Probabilidad de observación {observacion} dada la transición de {estado} a {proximo_estado} con acción {accion}: {prob_transicion_obs}")
