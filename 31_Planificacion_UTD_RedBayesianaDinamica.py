# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

class RedBayesianaDinamica:
    def __init__(self, estados, transiciones, evidencias):
        self.estados = estados  # Lista de nombres de los estados
        self.transiciones = transiciones  # Matriz de transiciones entre estados
        self.evidencias = evidencias  # Lista de evidencias

    def calcular_probabilidad(self, estado_actual, estado_siguiente, evidencia):
        # Calcular la probabilidad condicional P(estado_siguiente | estado_actual, evidencia)
        prob_transicion = self.transiciones[estado_actual][estado_siguiente]
        prob_evidencia_dado_estado = self.evidencias[estado_siguiente][evidencia]
        probabilidad = prob_transicion * prob_evidencia_dado_estado
        return probabilidad

# Ejemplo de uso
estados = ['Soleado', 'Lluvioso']
transiciones = {'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2}, 'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}}
evidencias = {'Soleado': {'Buen_tiempo': 0.9, 'Mal_tiempo': 0.1}, 'Lluvioso': {'Buen_tiempo': 0.2, 'Mal_tiempo': 0.8}}

red_bayesiana_dinamica = RedBayesianaDinamica(estados, transiciones, evidencias)

# Ejemplo de cálculo de probabilidad
estado_actual = 'Soleado'
estado_siguiente = 'Lluvioso'
evidencia = 'Mal_tiempo'
probabilidad = red_bayesiana_dinamica.calcular_probabilidad(estado_actual, estado_siguiente, evidencia)
print(f"La probabilidad de que el estado siguiente sea '{estado_siguiente}' dado que el estado actual es '{estado_actual}' y la evidencia es '{evidencia}' es: {probabilidad}")
