def precio_final(precio,descuento=0.10):
    return precio*(1-descuento)
print(precio_final(200))
print(precio_final(200,0.20))