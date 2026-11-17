def factorial(numero):
    if numero < 0:
        raise ValueError("el numero no debe ser negativo")
    elif numero==0:
        return 1
    else:
        return numero*factorial(numero-1)
try:
    factorial((-3))
except ValueError as e:
    print("ocurrio un error:")
print(factorial(0))
print(factorial(1))