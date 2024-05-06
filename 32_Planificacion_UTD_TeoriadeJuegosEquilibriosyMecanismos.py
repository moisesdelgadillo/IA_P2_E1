# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np
from scipy.optimize import minimize

class Juego:
    def __init__(self, jugadores, utilidades):
        self.jugadores = jugadores  # Lista de jugadores
        self.utilidades = utilidades  # Matriz de utilidades

    def calcular_equilibrio_nash(self):
        num_jugadores = len(self.jugadores)
        estrategias_iniciales = [np.zeros(len(utilidades_jugador)) for utilidades_jugador in self.utilidades]

        def funcion_objetivo(estrategias):
            utilidades_jugadores = [np.dot(utilidades_jugador, estrategia) for utilidades_jugador, estrategia in zip(self.utilidades, estrategias)]
            return -np.prod(utilidades_jugadores)

        restricciones = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1} for _ in range(num_jugadores)]
        resultado = minimize(funcion_objetivo, estrategias_iniciales, constraints=restricciones)
        return resultado.x

# Ejemplo de uso
jugadores = ['A', 'B']
utilidades = [np.array([[3, 0], [5, 1]]), np.array([[3, 5], [0, 1]])]

juego = Juego(jugadores, utilidades)
equilibrio_nash = juego.calcular_equilibrio_nash()

print("Equilibrio de Nash:")
for jugador, estrategia in zip(jugadores, equilibrio_nash):
    print(f"Jugador {jugador}: {estrategia}")
