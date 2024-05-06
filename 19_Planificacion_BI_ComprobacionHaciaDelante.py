# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def comprobacion_hacia_adelante(variables, dominios, restricciones):
    asignacion = {}

    def consistente(variable, valor, asignacion_actual):
        for otra_variable, otro_valor in asignacion_actual.items():
            if (variable, otra_variable) in restricciones:
                if not restricciones[(variable, otra_variable)](valor, otro_valor):
                    return False
            if (otra_variable, variable) in restricciones:
                if not restricciones[(otra_variable, variable)](otro_valor, valor):
                    return False
        return True

    def reducir_dominio(variable, valor, dominios_reducidos, asignacion_actual):
        for otra_variable in variables:
            if otra_variable != variable and (variable, otra_variable) in restricciones and otra_variable not in asignacion_actual:
                dominio_otra_variable = list(dominios_reducidos[otra_variable])
                for otro_valor in dominio_otra_variable:
                    if not restricciones[(variable, otra_variable)](valor, otro_valor):
                        dominios_reducidos[otra_variable].remove(otro_valor)
                if not dominios_reducidos[otra_variable]:
                    return False
        return True

    for variable in variables:
        if variable not in asignacion:
            for valor in dominios[variable]:
                if consistente(variable, valor, asignacion):
                    asignacion[variable] = valor
                    dominios_reducidos = {v: list(dominios[v]) for v in variables}
                    if not reducir_dominio(variable, valor, dominios_reducidos, asignacion):
                        continue
                    if comprobacion_hacia_adelante(variables, dominios_reducidos, restricciones):
                        return True
                    del asignacion[variable]
    return len(asignacion) == len(variables)

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
restricciones = {('A', 'B'): lambda x, y: x != y, ('B', 'C'): lambda x, y: x != y}

if comprobacion_hacia_adelante(variables, dominios, restricciones):
    print("Es posible encontrar una solución.")
else:
    print("No es posible encontrar una solución.")
