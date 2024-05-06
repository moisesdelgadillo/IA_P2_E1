# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

class NodoDecision:
    def __init__(self, nombre, decisiones):
        self.nombre = nombre
        self.decisiones = decisiones

    def __str__(self):
        return f"Nodo de decisión: {self.nombre}"

class NodoProbabilidad:
    def __init__(self, nombre, distribucion):
        self.nombre = nombre
        self.distribucion = distribucion

    def __str__(self):
        return f"Nodo de probabilidad: {self.nombre}"

class NodoResultado:
    def __init__(self, nombre, valores):
        self.nombre = nombre
        self.valores = valores

    def __str__(self):
        return f"Nodo de resultado: {self.nombre}"

class RedDecision:
    def __init__(self):
        self.nodos_decision = []
        self.nodos_probabilidad = []
        self.nodos_resultado = []

    def agregar_nodo_decision(self, nodo):
        self.nodos_decision.append(nodo)

    def agregar_nodo_probabilidad(self, nodo):
        self.nodos_probabilidad.append(nodo)

    def agregar_nodo_resultado(self, nodo):
        self.nodos_resultado.append(nodo)

    def iteracion_valores(self):
        # Inicializar utilidades a 0
        utilidades = {nodo: 0 for nodo in self.nodos_resultado}

        # Iteración de valores
        convergencia = False
        while not convergencia:
            utilidades_nuevas = utilidades.copy()
            for nodo_resultado in self.nodos_resultado:
                utilidad_maxima = float('-inf')
                for valor in nodo_resultado.valores:
                    utilidad = 0
                    for nodo_decision in self.nodos_decision:
                        utilidad_decision = 0
                        for valor_decision, probabilidad in zip(nodo_decision.decisiones, nodo_decision.probabilidades):
                            if valor_decision == valor:
                                utilidad_decision += probabilidad * utilidades_nuevas[nodo_decision]
                        utilidad += utilidad_decision
                    utilidad_maxima = max(utilidad_maxima, utilidad)
                utilidades[nodo_resultado] = utilidad_maxima

            # Verificar convergencia
            convergencia = all(abs(utilidades[nodo] - utilidades_nuevas[nodo]) < 0.01 for nodo in self.nodos_resultado)

        return utilidades

# Ejemplo de uso
red = RedDecision()
nodo_decision = NodoDecision("Tomar paraguas", ["Sí", "No"])
nodo_probabilidad = NodoProbabilidad("Lluvia", {"Sí": 0.4, "No": 0.6})
nodo_resultado = NodoResultado("Estar mojado", {"Sí": "Sí", "No": "No"})
red.agregar_nodo_decision(nodo_decision)
red.agregar_nodo_probabilidad(nodo_probabilidad)
red.agregar_nodo_resultado(nodo_resultado)

utilidades = red.iteracion_valores()
print("Utilidades finales:", utilidades)
