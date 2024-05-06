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

    def __str__(self):
        resultado = "Red de Decisión:\n"
        resultado += "Nodos de Decisión:\n"
        for nodo in self.nodos_decision:
            resultado += str(nodo) + "\n"
        resultado += "Nodos de Probabilidad:\n"
        for nodo in self.nodos_probabilidad:
            resultado += str(nodo) + "\n"
        resultado += "Nodos de Resultado:\n"
        for nodo in self.nodos_resultado:
            resultado += str(nodo) + "\n"
        return resultado

# Ejemplo de uso
red = RedDecision()
nodo_decision = NodoDecision("Tomar paraguas", ["Sí", "No"])
nodo_probabilidad = NodoProbabilidad("Lluvia", {"Sí": 0.4, "No": 0.6})
nodo_resultado = NodoResultado("Estar mojado", {"Sí": "Sí", "No": "No"})

red.agregar_nodo_decision(nodo_decision)
red.agregar_nodo_probabilidad(nodo_probabilidad)
red.agregar_nodo_resultado(nodo_resultado)

print(red)
