cadena1='hola'
cadena2="mundo"
multilinea="""esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
eco="ja"*3
print(eco)
tu_nombre='saul'
print(tu_nombre.upper())
print(tu_nombre.lower())
frace="me gusta programacion"
print(frace.replace("programacion","matematicas"))
edad=17
nombre='saul'
mensaje=f"hola me llamo {nombre} y tengo\n{edad}años"
print(mensaje)
texto="¡felicidades por aun continuar en el cecy!!!"
cantidad_caracteres=len(texto)
oracion="aprender python es divertido"
if "java" in oracion:
    print("encontrado")
else:
    print("no esta")
    ncadena="aaa"
    print(ncadena.isalpha())#TRUE
    print(ncadena.isdigit())#false