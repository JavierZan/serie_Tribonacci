# -*- coding: utf-8 -*-

iteraciones = 1000000

z = [0, 0, 1]
matriz_z = [z]

for i in range(iteraciones):
    
    nuevo = z[0] + z[1] + z[2]
    nuevo = str(nuevo)[-4:]
    nuevo = int(nuevo)
    z = [z[1], z[2], nuevo]
    matriz_z.append(z)
    
flag = ""
for i in range(len(matriz_z)):
    if flag != "":
        break
    probar = matriz_z[i]
    fila_str = str(i)
    for j in range((len(matriz_z)-i-1)):
        fila2 = j + i + 1
        print(i, " ",fila2)
        if probar == matriz_z[fila2]:
            fila2_str = str(fila2)
            flag = "Coincidencia en fila " + fila_str + " y " + fila2_str
            break
print(flag)

print(matriz_z[0], " ", matriz_z[124000])

