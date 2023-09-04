# -*- coding: utf-8 -*-

import time

posicion = int(input("Ingrese posición buscada: "))

inicio_t = time.time()

resultado = " "

if posicion <= 0:
    print("Posición inválida")
    
elif posicion == 1:
    resultado = 2023
    
elif posicion == 2:
    resultado = 2024
    
elif posicion == 3:
    resultado = 2025
    
# ~ Desde posición 4 hasta 124000 resuelvo por iteración sumando los últimos 3 elementos de la serie (últimas 4 cifras) hasta llegar a la posición buscada
elif posicion <= 124003:
    serie = [2023, 2024, 2025]
    for j in range(posicion-3):
        
        nuevo = serie[0] + serie[1] + serie[2]
        nuevo = str(nuevo)[-4:]
        nuevo = int(nuevo)
        
        resultado = nuevo
        
        serie = [serie[1], serie[2], nuevo]
        
else: 
    # ~ Este es el punto de inflexión donde la serie (últimas 4 cifras) comienza a repetirse, ejemplo 248003, 372003
    # ~ posición 248001 -> 2023
    # ~ posición 248002 -> 2024
    # ~ posicion 248003 -> 2025 -> esta posición da resto cero y la capturo aquí       
    if (posicion-3) % 124000 == 0:
        resultado = 2025
        
    # ~ Las posiciones arriba de 124003 (exceptuando las que dan resto cero) se calculan aquí
    # ~ Posición 124010 -> es igual a la posición 10
    else:
        posicion = (posicion-3) % 124000 + 3
        serie = [2023, 2024, 2025]
        for j in range(posicion-3):
            nuevo = serie[0] + serie[1] + serie[2]
            nuevo = str(nuevo)[-4:]
            nuevo = int(nuevo)
            
            resultado = nuevo
            
            serie = [serie[1], serie[2], nuevo]
            
fin_t = time.time()
tiempo_total =  fin_t - inicio_t

print("Tiempo total (seg): ", tiempo_total)
print("Resultado: ", resultado)
