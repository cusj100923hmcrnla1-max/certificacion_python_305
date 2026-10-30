mapa=[
    [".",".",".","."],
    [".","b",".","."],
    [".",".",".","."],
    [".",".","x","."]
]
filas=len(mapa)
columnas=len(mapa[0])
for i in range(filas):
    for j in range(columnas):
        if mapa[i][j]=="x":
            print(f"tesoro encontrado en la posicion[{i}][{j}]")
        if mapa[i][j]=="b":
            print(f"tesoro encontrado en la posicion[{i}][{j}]")