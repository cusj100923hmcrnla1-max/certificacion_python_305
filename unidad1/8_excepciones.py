try:
    #ejemplo 1 sin manejo de excepciones 
    numero1=float(input("ingresa el primer numero"))
    numero2=float(input("ingresa el sugundo numero"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("divion entre cero fallida")
except ValueError:
    print("solo introduce numeros")
    