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
    
else:
    serie = [2023, 2024, 2025]
    for j in range(posicion-3):
        
        nuevo = serie[0] + serie[1] + serie[2]
        
        nuevo_cortado = str(nuevo)[-4:]
        nuevo_cortado = int(nuevo_cortado)
        
        resultado = nuevo_cortado
        
        # ~ Corroboro que utilizando las últimas 4 cifras es suficiente para calcular las últimas 4 cifras del elemento siguiente
        # ~ print(nuevo, "    ", nuevo_cortado)

        serie = [serie[1], serie[2], nuevo_cortado]

fin_t = time.time()
tiempo_total =  fin_t - inicio_t

print("Tiempo total (seg): ", tiempo_total)
print("Resultado: ", resultado)
