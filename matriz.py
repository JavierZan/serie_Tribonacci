# -*- coding: utf-8 -*-

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

posicion = 1000000

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
    if matriz_temp == matriz_identidad:
        print("Encontrado posición: ", n+5)
        print(matriz_temp[0])
        print(matriz_temp[1])
        print(matriz_temp[2])

