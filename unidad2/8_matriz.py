# listas colores{"azul","rojo"}
matriz=[
    [5,8,1],
    [3,9,2]
]
filas=len(matriz)
columnas=len(matriz[0])
for i in range(0,2):
    for j in range(0,3):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")