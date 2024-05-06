# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def funcion_utilidad(resultado):
    # Esta función de utilidad asigna un valor numérico a un resultado
    if resultado == "Éxito":
        return 100
    elif resultado == "Fracaso":
        return 0
    else:
        return 50

# Ejemplo de uso
resultado = "Éxito"
valor_utilidad = funcion_utilidad(resultado)
print(f"La utilidad del resultado '{resultado}' es: {valor_utilidad}")
