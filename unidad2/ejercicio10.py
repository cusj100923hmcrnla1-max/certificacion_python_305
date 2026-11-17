def resumir_calificacion(calificacion):
    menor=min(calificacion)
    mayor=max(calificacion)
    promedio=sum(calificacion)/len(calificacion)
    return menor, mayor, promedio
minima, maxima, media=resumir_calificacion([80,90,100])
print(minima,maxima,media)