nombre = input("ingresa el nombre del cliente:")

lapiz = input("ingresa el precio del lapiz:")
mochila = input("ingresa el precio de la mochila:")
lapicero = input("ingresa el precio del lapicero:")
lapiz = float(lapiz)
mochila = float(mochila)
lapicero = float(lapicero)
total = lapiz + mochila + lapicero
print("\n------TICKET DE LA COMPRA------")
print("Nombre del cliente:", nombre)
print("Lápiz: $", lapiz)
print("Cuaderno: $", mochila)
print("Mochila: $", lapicero)
print("Total de la compra: $", total)


