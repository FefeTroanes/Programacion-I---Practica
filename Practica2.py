# PRACTICA 2
# 1. Considerar los siguientes fragmentos de código, y verificar si son correctos o no. En caso de no serlo,
# proponer un cambio para arreglarlo

# 1.a
# print( saludo + " " + destino + puntuacion ) # En este punto las variables aun no fueron declaradas, por lo que estan
# saludo = " Hola "                            # fuera del scope. Lo correcto seria poner el print() luego de las
# destino = " Mundo "                          # declaraciones.
# puntuacion = "!"

# 1.b Este esta bien
# cateto1 = 3
# cateto2 = 4
# hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5
# del cateto1
# del cateto2
# print(hipotenusa)

# 1.c
# del tengo_hambre      # Aca el error esta en querer borrar una variable que aun no fue declarada, lo mismo que el primero
# tengo_hambre = False
# del tengo_hambre
# tengo_hambre = True


# 2 . En Python podemos usar el operador == para preguntarnos si dos cosas son iguales o no. Si a == b
# nos devuelve True, entonces a y b se consideran iguales. En otro caso nos devolverá False. Verificar
# qué pares de las siguientes expresiones son iguales
# a. 3    => Esto es 3
# b. 3.0  => Esto es 3.0; 3 == 3.0 da True
# c. (0.1 + 0.2) * 10 => Esto es 3.0000000000000004
# d. 22 / 7   => Esto da 3.142857142857143
# e. 22 // 7  => Esto da 3 ya que es la parte entera de lo de arriba, comparado con 3 da True

# 3. ¿Cuáles son las diferencias y similitudes entre las siguientes expresiones?
# a. 1) 10 + 5    => 15
#    2) 10 + 5.0  => 15.0 se convierte el resultado implicitamente a float
#    3) 10 + 5.   => En este caso lo mismo de arriba
# b. 1) 11 / 2    => 5.5
#    2) 11 // 2   => 5
#    3) 11.0 // 2 => 5.0 😱

# 4. En Python los operadores de suma y de resta, + y -, pueden ser utilizados con un único argumento (u
# operando). Ejecutar cada una de las siguientes expresiones e interpretar los resultados.
# a. +1  => 1
# b. -1  => -1
# c. +-1 => -1 => +(-1)


# 5. Modelar los siguientes problemas, nombrando los datos relevantes y el resultado, junto con la forma
#    que tendrán sus representaciones internas en Python. Luego programar la solución.
# a. Se tienen dos habitaciones dentro de un hogar, cada una con una temperatura ambiente. Se quiere
#    saber a qué temperatura estarán las habitaciones, dado suficiente tiempo para que se transmita
#    el calor de una a la otra. Se conoce que en este caso es válido promediar temperaturas.
# tempHab1 = float(input('Ingrese la temperatura de la primera habitacion: '))
# tempHab2 = float(input('Ingrese la tempratura de la segunda habitacion: '))
# promedio = (tempHab1 + tempHab2) /2
# print('Si se da el suficiente tiempo para que se transmitan las temperaturas las habitaciones tendran ' \
#       + str(promedio) + ' grados.')

# b. Se tiene una multitud afuera, cada persona le dirá su nombre a cada otra persona en la multitud.
#    Se quiere saber cuánto tiempo llevará hacer esto, dado que decir una vez tu nombre lleva
#    aproximádamente 4 segundos y medio.

# c. Hay dos personas con nombres muy largos, pero similares. Se quiere conocer, por un lado, si tienen
#    el mismo tamaño, y por otro lado si son iguales. Ayuda para el programa: buscar la función len
# nombre1 = input('Ingrese el primer nombre: ')
# nombre2 = input('Ingrese el segundo nombre: ')
# sonIguales = nombre1 == nombre2
# mismoTamanio = len(nombre1) == len(nombre2)
# print('Son iguales?: ' + str(sonIguales))
# print('Tienen el mismo largo? : ' + str(mismoTamanio))

# 6. Traducir las siguientes expresiones del lenguaje natural a expresiónes booleanas en equivalentes en
#    Python. Determinar su veracidad o falsedad corriendo la expresión en el intérprete.

# a. La longitud de la cadena "Hola, mundo" es 14.
# a = len('Hola, mundo') == 14
# print('La longitud de la cadena "Hola, mundo" es 14: ' + str(a))

# b. El área de un cuadrado de lado 5 es igual a la raíz cudrada de 625.
# b = (5 ** 2) == 625 ** (1/2)
# print('El área de un cuadrado de lado 5 es igual a la raíz cudrada de 625: ' + str(b))

# c. El diametro de un circulo de radio 3,25 es menor que 7 y mayor a 6.
# diametro = 3.25 * 2
# c = diametro < 7 and diametro > 6
# print('El diametro de un circulo de radio 3,25 es menor que 7 y mayor a 6: ' + str(c))

# d. La apromixación de Pi = 22 / 7 es un número mayor que 3, y 2 + 2 es igual a 5.


# e. El numero 10 es mayor a 5 o 0 dividido 0 es igual 0.
# f. La cadena "Python" tiene longitud 5 y 1+"1" es igual a 2