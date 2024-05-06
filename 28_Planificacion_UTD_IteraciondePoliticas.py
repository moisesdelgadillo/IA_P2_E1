# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

class EntornoMDP:
    def __init__(self, estados, acciones, recompensas, transiciones, gamma):
        self.estados = estados
        self.acciones = acciones
        self.recompensas = recompensas
        self.transiciones = transiciones
        self.gamma = gamma

    def obtener_transicion(self, estado, accion):
        return self.transiciones[(estado, accion)]

    def obtener_recompensa(self, estado, accion, proximo_estado):
        return self.recompensas[(estado, accion, proximo_estado)]

    def obtener_acciones_posibles(self, estado):
        return self.acciones[estado]

class IteracionPoliticas:
    def __init__(self, entorno):
        self.entorno = entorno

    def iterar_politicas(self):
        politica_optima = {estado: None for estado in self.entorno.estados}
        politica_estable = False

        while not politica_estable:
            politica_estable = True
            for estado in self.entorno.estados:
                mejor_accion = politica_optima[estado]
                mejor_valor = float('-inf')
                for accion in self.entorno.obtener_acciones_posibles(estado):
                    valor_accion = 0
                    for proximo_estado, probabilidad in self.entorno.obtener_transicion(estado, accion).items():
                        recompensa = self.entorno.obtener_recompensa(estado, accion, proximo_estado)
                        valor_accion += probabilidad * (recompensa + self.entorno.gamma * politica_optima[proximo_estado])
                    if valor_accion > mejor_valor:
                        mejor_valor = valor_accion
                        mejor_accion = accion
                if politica_optima[estado] != mejor_accion:
                    politica_estable = False
                    politica_optima[estado] = mejor_accion

        return politica_optima

# Ejemplo de uso
estados = [0, 1]
acciones = {0: ['a1', 'a2'], 1: ['a1']}
recompensas = {(0, 'a1', 1): 10, (0, 'a2', 1): 0, (1, 'a1', 1): 50}
transiciones = {(0, 'a1'): {1: 0.6, 0: 0.4}, (0, 'a2'): {1: 0.3, 0: 0.7}, (1, 'a1'): {1: 0.8, 0: 0.2}}
gamma = 0.9

entorno = EntornoMDP(estados, acciones, recompensas, transiciones, gamma)
iteracion_politicas = IteracionPoliticas(entorno)
politica_optima = iteracion_politicas.iterar_politicas()
print("Política óptima:", politica_optima)
