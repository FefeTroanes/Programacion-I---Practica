# 1. Imprimir los primeros 20 números naturales.
for i in range(20):
    print(i + 1)


# 2. Imprimir la tabla de multiplicar del número 5
for i in range(10):
    print(f"5x{(i+1)} =", 5*(i+1))


# 3. Imprima los números de -10 a -1.
for i in range(-10, 0):
    print(i)


# 4. Dada la siguiente secuencia de números:  = [12 , 75 , 150 , 180 , 145 , 525 , 50]
for i in [12 , 75 , 150 , 180 , 145 , 525 , 50]:
    if i < 150 and (i % 5) == 0:
        print(f'{i} es divisible por 5 y menor que 150')


# 5. Imprimir los primeros 10 valores de la secuencia de Fibonacci. La secuencia de Fibonacci es una serie
#    de números en la cual los dos primeros números son 0 y 1, y el siguiente número se corresponde a la
#    suma de los dos números anteriores. Resultado esperado: 0 1 1 2 3 5 8 13 21 34
aux1 = 0
aux2 = 1
for i in range(10):
    print(aux1)
    suma = aux1 + aux2
    aux1 = aux2
    aux2 = suma


# 6. Imprimir el valor factorial del número 5 usando un bucle. El valor factorial (símbolo: !) se obtiene de
#    multiplicar todos los números enteros desde el número elegido hasta 1. Resultado esperado: 120
aux = 1
for i in range(1,6):
    aux *= i
print(aux)


# 7. Explique el resultado de los siguientes programas
#    a. lista = []
#       for j in lista:
#           print(j) # Es un array vacio, por lo que si le pido que me imprima lo que tiene dentro
#                      no va a imprimir nada

#    b. i = 1
#       for i in [1 , 2 , 3]:
#           print ( i ) # Esto primero imprime los valores del for: 1, 2, 3
#       print ( i )     # En este punto i = 3, por lo cual lo vuelve a imprimir
#                         Resultado de los prints: 1, 2, 3, 3

# 8. Resuelva los siguientes ejercicios:
# a. Calcular el cuadrado de los primeros 10 números enteros.
for i in range(1, 11):
    print(pow(i, 2))

# b. Calcular la suma de los números enteros entre 0 y 100 inclusive.
aux = 0
for i in range(101):
    aux += i
print(aux)

# c. Calcular la suma de los números pares menores a 100. ¿Cuántos números pares hay menores a 100?
aux = 0
contador = 0
for i in range(0, 100, 2):
    aux += i
    contador += 1
print(f'Suma de los números pares menores a 100: {aux}')
print(f'Cantidad de números pares menores a 100: {contador}')

# d. Calcular la suma de los números impares menores a 100. ¿Cuántos números impares hay menores a 100?
aux = 0
contador = 0
for i in range(1, 100, 2):
    aux += i
    contador += 1
    print(i)
print(f'Suma de los números impares menores a 100: {aux}')
print(f'Cantidad de números impares menores a 100: {contador}')

# 9. ¿Cuál es el problema asociado al siguiente programa?
#    No hace falta ejecutarlo para responder esta pregunta.
x = 0
while x < 5:
    print(x)
# Esto produce un bucle infinito ya que como el valor de x no cambia, siempre va a ser < 5

# 10. Escriba un programa que dada una secuencia de números y un valor de umbral vaya sumando los
#     números de la secuencia hasta que la suma alcance el umbral. Utilice break para terminar la ejecución
#     del bucle cuando la suma alcance el umbral.

#     Resultados esperados:

#     umbral = 21
#     valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]    suma -> 21

#     umbral = 34
#     valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]    suma -> 34

#     umbral = 100
#     valores = [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]    suma -> 43

umbral = int(input('Ingrese el umbral: '))
suma = 0
for i in [3 , 5 , 4 , 4 , 5 , 5 , 3, 5 , 2 , 7]:
    if (suma < umbral):
        suma += i
print(suma)

# 11. Escriba un programa que dada una secuencia numérica compute la suma de los números pares. Utilice
#     un bucle while y la sentencia continue para saltear los casos donde el número no sea par.

#     Resultados esperados:
#     valores = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8 , 9 , 10]  suma -> 30
#     valores = [1 , 4 , 7 , 10]                         suma -> 14
suma = 0
while True:
    entrada = int(input('Ingrese un numero para sumar. Ingrese 0 para terminar: '))
    if entrada == 0:
        break
    elif (entrada % 2) == 0:
        suma += entrada
    else:
        continue
print(f'La suma de los numeros ingresados es: {suma}')

# 12. Escriba un programa que solicite un numero entero al usuario y compute la suma de todos los numeros
#     naturales menores a él. Este programa debe ser interactivo. Es decir, el programa solicita un numero al
#     usuario, devuelve la suma, y solicita un nuevo número. Esto continúa así hasta que el usuario ingresa
#     "salir", determinando que el programa debe terminar. Utilice un bucle while para resolver este
#     problema. Tenga en cuenta la sentencia break para determinar la interrupción del bucle. Ejemplos:

#     Ingrese un numero o 'salir ' para terminar : 10
#     La suma es 45

#     Ingrese un numero o 'salir ' para terminar : 50
#     La suma es 1225

#     Ingrese un numero o 'salir ' para terminar : salir
suma = 0
while True:
    entrada = input('Ingrese un numero entero a sumar. Ingrese "salir" para terminar: ')
    if entrada == 'salir':
        print('Salio')
        break
    else:
        entrada = int(entrada)
        for i in range(entrada+1):
            suma += i
        print(f'La suma de los numeros anteriores al ingresado es: {suma}')
        suma = 0
    continue

# 13. Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. A partir de ahí, cada
#     día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que
#     la pila de billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar
#     a resolver el problema:

#     billete_grosor = 0.11 * 0.001 # grosor de un billete en metros
#     altura_monumento = 70 # altura en metros
#     billetes_n = 1
#     dia = 1

billeteGrosor = 0.11 * 0.001
alturaMonumento = 70
dia = 1
billetes = 1
alturaBilletes = billeteGrosor
while alturaBilletes < alturaMonumento:
    dia += 1
    billetes *= 2
    alturaBilletes = billeteGrosor * billetes
print(f'Pasaron {dia} dias.')

# 14. Escriba un programa reciba dos números como parámetros, y compute cuántos múltiplos del primero
#     hay, que sean menores que el segundo.
#     a. Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# numero1 = int(input('Ingrese el primer numero'))
# numero2 = int(input('Ingrese el segundo numero'))
# if numero1 > numero2:

#     b. Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea mayor
#     que el segundo.


#     c. Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?