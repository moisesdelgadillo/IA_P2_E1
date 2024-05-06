# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

def consistencia_arco(variables, dominios, restricciones):
    arcos = [(variable1, variable2) for variable1 in variables for variable2 in variables if (variable1, variable2) in restricciones]

    def revisar_arco(variable1, variable2):
        dominio_variable1 = dominios[variable1]
        dominio_variable2 = dominios[variable2]
        restriccion = restricciones[(variable1, variable2)]

        removidos = False
        for valor1 in dominio_variable1[:]:
            compatible = False
            for valor2 in dominio_variable2:
                if restriccion(valor1, valor2):
                    compatible = True
                    break
            if not compatible:
                dominio_variable1.remove(valor1)
                removidos = True
        return removidos

    arcos_restantes = list(arcos)
    while arcos_restantes:
        variable1, variable2 = arcos_restantes.pop(0)
        if revisar_arco(variable1, variable2):
            if not dominios[variable1]:
                return False
            for variable3 in variables:
                if (variable3 != variable1 and variable3 != variable2) and ((variable1, variable3) in restricciones or (variable3, variable1) in restricciones):
                    arcos_restantes.append((variable3, variable1))
    return True

# Ejemplo de uso
variables = ['A', 'B', 'C']
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
restricciones = {('A', 'B'): lambda x, y: x != y, ('B', 'C'): lambda x, y: x != y}

if consistencia_arco(variables, dominios, restricciones):
    print("Las restricciones son consistentes.")
else:
    print("Las restricciones no son consistentes.")
