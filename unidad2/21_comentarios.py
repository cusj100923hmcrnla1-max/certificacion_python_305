def costo_emvio(subtotal):
    if subtotal >=500:
        return 0
    return 80
print(costo_emvio(499))
print(costo_emvio(500))