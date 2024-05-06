# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def calcular_valor_informacion(probabilidad_inicial, probabilidad_actual):
    # Calcula el cambio en la probabilidad
    cambio_probabilidad = abs(probabilidad_actual - probabilidad_inicial)

    # Calcula el valor esperado del cambio en la utilidad
    valor_informacion = cambio_probabilidad * utilidad_esperada

    return valor_informacion

# Ejemplo de uso
probabilidad_inicial = 0.3  # Probabilidad inicial de un evento
probabilidad_actual = 0.7   # Probabilidad actualizada del mismo evento
utilidad_esperada = 100     # Utilidad esperada asociada al evento

valor_informacion = calcular_valor_informacion(probabilidad_inicial, probabilidad_actual)
print("El valor de la información es:", valor_informacion)
