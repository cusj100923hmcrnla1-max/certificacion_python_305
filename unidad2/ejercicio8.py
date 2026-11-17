def calcular(producto1, producto2, producto3):
    calcular = (producto1 + producto2 + producto3)
    return calcular
def calcular_iva(calcular):
    calcular_iva = (calcular * 0.16)
    return calcular_iva
def venta_total(calcular, calcular_iva):
    venta_total = (calcular + calcular_iva)
    return venta_total
subtotal = calcular(100, 300, 100)
iva = calcular_iva(subtotal)
total = venta_total(subtotal,iva)
print(f"iva:, {iva}")
print(f"venta con el iva:,{total}")