def aplicar_operacion(numeros,operacion):
    resultado=[]
    for numero in numeros:
        resultado.append(operacion(numero))
        return resultado
def cuadrado(numero):
    return numero **2
print(aplicar_operacion([2,3,4], cuadrado))