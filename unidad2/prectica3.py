def crear_perfil(numero_control,**datos):
    return{"numero_control":numero_control, **datos}
perfil=crear_perfil("0015297738",nombre="saul",semestre="3",carrera="programacion")
print(perfil["numero_control"],perfil["nombre"],perfil["semestre"],perfil["carrera"])