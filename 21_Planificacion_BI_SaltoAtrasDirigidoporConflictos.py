# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def conflicto_mas_comun(asignacion_actual, conflictos):
    # Encuentra la variable que más contribuye a los conflictos
    contador_conflictos = {}
    for conflicto in conflictos:
        for variable in conflicto:
            if variable not in asignacion_actual:
                if variable not in contador_conflictos:
                    contador_conflictos[variable] = 1
                else:
                    contador_conflictos[variable] += 1
    if contador_conflictos:
        return max(contador_conflictos, key=contador_conflictos.get)
    else:
        return None

def salto_atras_dirigido_por_conflictos(variables, dominios, restricciones):
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

    while len(asignacion) < len(variables):
        conflictos = []
        while True:
            if len(asignacion) == len(variables):
                return asignacion
            variable = conflicto_mas_comun(asignacion, conflictos)
            if variable is None:
                variable = [v for v in variables if v not in asignacion][0]
            if variable not in asignacion:
                break
            conflictos.append(variable)
            del asignacion[variable]
        for valor in dominios[variable]:
            if consistente(variable, valor, asignacion):
                asignacion[variable] = valor
                dominios_reducidos = {v: list(dominios[v]) for v in variables}
                if not reducir_dominio(variable, valor, dominios_reducidos, asignacion):
                    continue
                break
    return asignacion

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
restricciones = {('A', 'B'): lambda x, y: x != y, ('B', 'C'): lambda x, y: x != y}

solucion = salto_atras_dirigido_por_conflictos(variables, dominios, restricciones)
print("Solución encontrada:", solucion)
