PROBLEMA

Una computadora inicia su proceso imprimiendo las cifras 2023, 2024 y 2025. 
A continuación, no se detiene y prosigue imprimiendo la suma de los tres 
números más recientes que ha impreso: 6072, 10121, 18218, etc. ¿Podrías 
decir cuáles son las últimas cuatro cifras del número impreso en el puesto 
2023202320232023? Para ilustrar, en la posición 50, el número impreso es 
8188013234823360, que concluye en 3360.

--------------------------------------------------------------------------------------------------

Las últimas 4 cifras del número impreso en la posición 2023202320232023 es:

    3363

Los fundamentos usados para resolverlo son 2:

    * Últimas 4 cifras -> para obtener las últimas 4 cifras de un número de la serie, 
      sólo es necesario sumar las últimas 4 cifras de los 3 elementos anteriores
    * Repetición de la serie (últimas 4 cifras): llegando al elemento 124000 se comienza a repetir,
        124001 -> 2023
        124002 -> 2024
        124003 -> 2025
        Por tanto el siguiente es 2023 + 2024 + 2025 y sigue al igual que al inicio
        O sea, sólo necesito iterar un número acotado de veces.

Script "respuesta.py" contiene el código para resolver el problema.

Para llegar a estos fundamentos se pasó por varias etapas, pruebas y error. 
Por orden cronológico.

Primero hice un script iterando, para probar -> "iteracion.py"
Fui haciendo modificaciones y saqué 2 conclusiones:

    1- Sólo necesito iterar sobre los últimos 4 dígitos.
    2- Calculé que la posición 2023202320232023 la alcanzaría en aproximadamente 38 días, 
       evidentemente no es el camino
    
También aproveché para chequear las posición 50 -> 3360, y tomar tiempos:

    * Pocición 100,000 -> 0.16 seg
    * Posición 1,000,000 -> 1.5 seg
    * Posición 10,000,000 -> 15 seg
    * Posición 100,000,000 -> 2.4 min
    * Posición 1,000,000,000 -> 27 min

En este momento empiezo a desmenuzar la serie y ver si encuentro un camino alternativo... 

Como empiezo con 2023, 2024 y 2025, los siguientes elementos van a ser la suma de múltiplos de 2023, 2024 y 2025.

x . 2023 + y . 2024 + z . 2025 -> forma genérica de escribir cualquier elemento de la serie

Veamos cómo va desde el comienzo

    1-  -> 1 . 2023 + 0 . 2024 + 0 . 2025
    2-  -> 0 . 2023 + 1 . 2024 + 0 . 2025
    3-  -> 0 . 2023 + 0 . 2024 + 1 . 2025

Sumar los elementos 1, 2 y 3 es equivalente a sumar sus coeficientes 

(x1 + x2 + x3) . 2023 + (y1 + y2 + y3) . 2024 + (z1 + z2 + z3) . 2025

    4-  -> 1 . 2023 + 1 . 2024 + 1 . 2025
    5-  -> 1 . 2023 + 2 . 2024 + 2 . 2025
    6-  -> 2 . 2023 + 3 . 2024 + 4 . 2025
    7-  -> 4 . 2023 + 6 . 2024 + 7 . 2025
    8-  -> 7 . 2023 + 11 . 2024 + 13 . 2025
    9-  -> 13 . 2023 + 20 . 2024 + 24 . 2025
    10- -> 24 . 2023 + 37 . 2024 + 44 . 2025

Aquí noto que (igual que antes) sólo necesito los últimos 4 dígitos de x, y, z

Veo algo interesante, podría escribir, siendo n la posición enésima

    x(n) = z(n-1)
    y(n) = x(n-1) + z(n-1)
    z(n) = y(n-1) + z(n-1)

También queda,

    (x(n-1), y(n-1), z(n-1)) .  (0 1 0) = (z(n-1), x(n-1) + z(n-1), y(n-1) + z(n-1)) = (x(n), y(n), z(n))
                                (0 0 1) 
                                (1 1 1) 

Si multiplico la matriz por sí misma, voy obteniendo los coeficientes del siguiente elemento de la serie

        (0 1 0) . (0 1 0) = (0 0 1)  
        (0 0 1)   (0 0 1)   (0 1 1)
        (1 1 1)   (1 1 1)   (1 2 2)    -> por ejemplo x=1, y=2, z=2 corresponde al elemento 5
        
O sea, si hago la matriz a la potencia (n-3) obtendría la enésima posición.
Empiezo a ver cómo podría lograrse, pero no encuentro forma que no sea iterando

Vuelvo a lo siguiente,

    x(n) = z(n-1)
    y(n) = x(n-1) + z(n-1)
    z(n) = y(n-1) + z(n-1) 

... y reescribo,

    x(n) = z(n-1)
    y(n) = z(n-2) + z(n-1)
    z(n) = z(n-3) + z(n-2) + z(n-1)

Podría reducir el problema a encontrar el coeficiente z.
Acá llego a un impás.
Hasta que googleo la serie de z -> 0 0 1 1 2 4 7 13 24 44 y para mi sorpresa es una serie conocida, la serie de Tribonacci.
Investigo y llego a que tiene una constante (k = 1.83929...) y puedo escribir,

    z(n) = z(n-1) . k -> es a lo que tiende al avanzar con la serie

    z(n) = k^n / (4.k - k^2 -1) 

Pruebo esta fórmula con un script y veo que sirve para los primeros elementos pero empieza 
a dar error al avanzar, agregando decimales a la constante llego a más elementos correctamente. 
Al avanzar mucho en la serie tendría que agregar decimales infinitamente a la constante y a parte 
elevar la constante a un número muy elevado tampoco me sería posible calcularlo.

Otro impás. Hasta que pienso, "si es una serie que está estudiada, que ya tiene soluciones y no me 
sirven para resolver el problema, no me queda otra que resolverlo iterando", parece poco, pero fue un 
paso importante porque me centré en cómo podría hacer para realizar la iteración. Esto me llevó a lo 
siguiente "¿en algún momento de la serie (usando las últimas 4 cifras), se repetirá?, o dicho de otra 
manera, ¿podré encontrar tres elementos seguidos z(n-2), z(n-1), z(n) que sean iguales a z(m-2), 
z(m-1), z(m) (siendo n y m las posiciones)?"

Manos a la obra, script -> "repeticion.py"

Y se hizo la luz =), me duró todo el día la sonrisa.
Llegué al segundo fundamento nombrado inicialmente.

A partir de acá trabajé en el script que llega al resultado (descrito primero de todo).

Hice algunas pruebas de control, usando los scripts "iteracion.py" vs "respuesta.py"

    iteracion.py                               respuesta.py

    1 -> 2023    t = 0 seg                     1 -> 2023    t = 0 seg
    2 -> 2024    t = 0 seg                     2 -> 2024    t = 0 seg
    3 -> 2024    t = 0 seg                     3 -> 2024    t = 0 seg
    4 -> 6072    t = 0 seg                     4 -> 6072    t = 0 seg
    5 -> 0121    t = 0 seg                     5 -> 0121    t = 0 seg
    6 -> 8218    t = 0 seg                     6 -> 8218    t = 0 seg
    50 -> 3360    t = 0 seg                    50 -> 3360    t = 0 seg
    80,000 -> 3930    t = 0.13 seg             80,000 -> 3930    t = 0.13 seg
    124,001 -> 2023    t = 0.20 seg            124,001 -> 2023    t = 0.20 seg
    124,002 -> 2024    t = 0.20 seg            124,002 -> 2024    t = 0.20 seg
    124,003 -> 2025    t = 0.20 seg            124,003 -> 2025    t = 0.20 seg
    124,004 -> 6072    t = 0.20 seg            124,004 -> 6072    t = 0.00 seg
    200,000 -> 9610    t = 0.33 seg            200,000 -> 9310    t = 0.13 seg
    248,003 -> 2025    t = 0.41 seg            248,003 -> 2025    t = 0.00 seg
    248,004 -> 6072    t = 0.41 seg            248,004 -> 6072    t = 0.00 seg
    372,003 -> 2025    t = 0.59 seg            372,003 -> 2025    t = 0.00 seg
    500,000 -> 2458    t = 0.80 seg            500,000 -> 2458    t = 0.00 seg
    1,000,000 -> 4954    t = 1.58 seg          1,000,000 -> 4954    t = 0.02 seg
    10,000,000 -> 3930    t = 15.75 seg        10,000,000 -> 3930    t = 0.13 seg
    100,000,000 -> 2234    t = 2.7 min         100,000,000 -> 2234    t = 0.10 seg
    1,000,000,000 -> 5450    t = 28 min        1,000,000,000 -> 5450     t = 0.11 seg
    10,000,000,000 -> 8346    t = 4.6 hs       1,000,000,000 -> 8346     t = 0.03 seg

El resultado es positivo, estamos listos para buscar la posción 2023202320232023.

Si llegaste hasta acá, gracias por tu tiempo!

--------------------------------------------------------------------------------------------------

Actualización 5/9/23

Volviendo a 

    (0 1 0)^2  =  (0 1 0) . (0 1 0)  =  (0 0 1)  
    (0 0 1)       (0 0 1)   (0 0 1)     (0 1 1)
    (1 1 1)       (1 1 1)   (1 1 1)     (1 2 2)  -> x=1, y=2, z=2 corresponde al elemento 5 = 1 . 2023 + 2 . 2024 + 2 . 2025
    
O sea, 

    (0 1 0)^(n-3)  ... da como resultado una matriz, cuya tercer fila es x(n), y(n), z(n)    
    (0 0 1)         
    (1 1 1)         

En su momento, había pensado en una forma de resolver potencias enésimas de matrices, que es viendo si son cíclicas.
Este no era el caso, tenemos una matriz que siempre va creciendo.
Pero... si hacemos "trampa" y sólo tomamos las últimas 4 cifras. Ver script -> "matriz.py".

Llamemos M a la matriz. Dio como resultado que M^124000 es la matriz identidad.

Si quiero hacer M^124001 = M^124000 . M^1 (los exponentes se suman) y como M^124000 es la identidad quedaría

    M^124001 = M^1 = (0 1 0) 
                     (0 0 1)
                     (1 1 1)  -> corresponde al elemento 4 = 1 . 2023 + 1 . 2024 + 1 . 2025

Script -> "respuesta_matriz" resuelve el problema aplicando estos conceptos.

Saludos!
