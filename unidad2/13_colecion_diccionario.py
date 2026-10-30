#creando un diccionario en python
persona={
    "nombre":"saul",
    "edad":16,
    "profecion":"programacon",
    "estudiante":False
}
print(persona)
print(persona["profecion"])
print(persona.get("edad"))
persona["edad"]=16
print(persona.get("edad"))
persona["ciudad"]="san pepe ranch"
print(persona)
for clave,valor in persona.items():
    print(f"{clave}:{valor}")