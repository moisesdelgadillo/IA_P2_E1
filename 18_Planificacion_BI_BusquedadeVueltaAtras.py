# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def backtracking(variables, dominios, restricciones):
    def asignar(variable, valor, asignacion_actual):
        asignacion_actual[variable] = valor

    def desasignar(variable, asignacion_actual):
        del asignacion_actual[variable]

    def esta_completa(asignacion_actual):
        return len(asignacion_actual) == len(variables)

    def todas_asignadas(asignacion_actual):
        return len(asignacion_actual) == len(variables)

    def consistente(variable, valor, asignacion_actual):
        for otra_variable, otro_valor in asignacion_actual.items():
            if (variable, otra_variable) in restricciones:
                if not restricciones[(variable, otra_variable)](valor, otro_valor):
                    return False
            if (otra_variable, variable) in restricciones:
                if not restricciones[(otra_variable, variable)](otro_valor, valor):
                    return False
        return True

    def seleccionar_variable(asignacion_actual):
        for variable in variables:
            if variable not in asignacion_actual:
                return variable
        return None

    def ordenar_valores(variable, dominio):
        return dominio

    def resolver(asignacion_actual):
        if esta_completa(asignacion_actual):
            return asignacion_actual

        variable = seleccionar_variable(asignacion_actual)
        for valor in ordenar_valores(variable, dominios[variable]):
            if consistente(variable, valor, asignacion_actual):
                asignar(variable, valor, asignacion_actual)
                resultado = resolver(asignacion_actual)
                if resultado is not None:
                    return resultado
                desasignar(variable, asignacion_actual)
        return None

    return resolver({})

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
restricciones = {('A', 'B'): lambda x, y: x != y, ('B', 'C'): lambda x, y: x != y}

solucion = backtracking(variables, dominios, restricciones)
print("Solución encontrada:", solucion)
