# -*- coding: utf-8 -*-

import time

posicion = int(input("Ingrese posición buscada: "))

inicio_t = time.time()

resultado = " "
resultado_corto = " "

if posicion <= 0:
    print("Posición inválida")
    
elif posicion == 1:
    resultado = 2023
    resultado_corto = 2023
    
elif posicion == 2:
    resultado = 2024
    resultado_corto = 2024
    
elif posicion == 3:
    resultado = 2025
    resultado_corto= 2025
    
else:
    serie = [2023, 2024, 2025]
    serie_corta = [2023, 2024, 2025]
    
    for j in range(posicion-3):
        
        # ~ nuevo = serie[0] + serie[1] + serie[2]
        # ~ resultado = nuevo
        # ~ serie = [serie[1], serie[2], nuevo]
        
        nuevo_cortado = serie_corta[0] + serie_corta[1] + serie_corta[2]
        nuevo_cortado = str(nuevo_cortado)[-4:]
        nuevo_cortado = int(nuevo_cortado)
        resultado_corto = nuevo_cortado
        serie_corta = [serie_corta[1], serie_corta[2], nuevo_cortado]
        
        # ~ Corroboro que iterar utilizando las últimas 4 cifras es suficiente 
        # ~ para calcular las últimas 4 cifras del elemento siguiente
        # ~ print(resultado, " " , resultado_corto)

fin_t = time.time()
tiempo_total =  fin_t - inicio_t

print("Tiempo total (seg): ", tiempo_total)
# ~ print("Resultado: ", resultado)
print("Resultado últimas 4 cifras: ", resultado_corto)
