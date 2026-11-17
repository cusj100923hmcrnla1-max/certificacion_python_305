def crear_perfil(nombre,**datos):
    return{"nombre":nombre, **datos}
perfil=crear_perfil("ana",ciudad="san pepe",nivel="basico")
print(perfil["nombre"],perfil["ciudad"],perfil["nivel"])