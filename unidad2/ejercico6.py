promedio=[5,10,6,9,7]
#encontrar elpromedio mas bajo uando el ciclo for
#suponemos que el promedo mas bajo es el primer elemento
promedio_bajo=promedio[0]
promedio_alto=promedio[0]
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo=contador
    if contador>promedio_alto:
        promedio_alto=contador
print(promedio_bajo)
print(promedio_alto)