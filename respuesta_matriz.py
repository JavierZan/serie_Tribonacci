# -*- coding: utf-8 -*-

import time

posicion = int(input("Ingrese posición buscada: "))

inicio_t = time.time()

resultado = " "

matriz = [ [0, 1, 0],
           [0, 0, 1], 
           [1, 1, 1] ]

matriz_cero = [ [0, 0, 0],
                [0, 0, 0], 
                [0, 0, 0] ]

matriz_temp = matriz

matriz_identidad = [ [1, 0, 0],
                     [0, 1, 0], 
                     [0, 0, 1] ]
                     
if posicion <= 0:
    print("Posición inválida")
    
elif posicion == 1:
    resultado = 2023
    
elif posicion == 2:
    resultado = 2024
    
elif posicion == 3:
    resultado = 2025
elif posicion <= 124003:
    for n in range(posicion-4):
              
        # ~ Multiplico matriz x matriz
        for fila in range(3):
            for col in range(3):
                for i in range(3):
                    a = str(matriz_temp[fila][i])[-4:]
                    a = int(a)
                    b = str(matriz[i][col])[-4:]
                    b = int(b)
                    matriz_cero[fila][col] += int(str(a * b)[-4:])
                    matriz_cero[fila][col] = int(str(matriz_cero[fila][col])[-4:])
                    
        matriz_temp = matriz_cero
        matriz_cero = [ [0, 0, 0],
                        [0, 0, 0], 
                        [0, 0, 0] ]
                        
    resultado = int(str(matriz_temp[2][0] * 2023 + matriz_temp[2][1] * 2024 + matriz_temp[2][2] * 2025)[-4:])
else:
    if (posicion-3) % 124000 == 0:
        resultado = int(str(matriz_temp[1][0] * 2023 + matriz_temp[1][1] * 2024 + matriz_temp[1][2] * 2025)[-4:])
    else:
        posicion = (posicion-3) % 124000 + 3
        for n in range(posicion-4):
                  
            # ~ Multiplico matriz x matriz
            for fila in range(3):
                for col in range(3):
                    for i in range(3):
                        a = str(matriz_temp[fila][i])[-4:]
                        a = int(a)
                        b = str(matriz[i][col])[-4:]
                        b = int(b)
                        matriz_cero[fila][col] += int(str(a * b)[-4:])
                        matriz_cero[fila][col] = int(str(matriz_cero[fila][col])[-4:])
                        
            matriz_temp = matriz_cero
            matriz_cero = [ [0, 0, 0],
                            [0, 0, 0], 
                            [0, 0, 0] ]
                            
        resultado = int(str(matriz_temp[2][0] * 2023 + matriz_temp[2][1] * 2024 + matriz_temp[2][2] * 2025)[-4:])
        
fin_t = time.time()
tiempo_total =  fin_t - inicio_t

print("Tiempo total (seg): ", tiempo_total)
print("Resultado: ", resultado)
