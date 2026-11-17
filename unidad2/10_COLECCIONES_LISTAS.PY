carrito=[]
n_productos=int(input("ingresa el numero de productos"))
for i in range(n_productos):
    producto=input("ingresa elproducto a tu carrito")
    carrito.append(producto)
print("lista creada correctamente")
carrito[0]="chetos"
print(f"tu carrito contiene{carrito}")