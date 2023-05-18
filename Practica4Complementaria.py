# 1. Acciones primitivas
# 1.1 Dada la base B y la altura H de un rectangulo, informar el area y el perımetro.
# b = float(input('Ingrese la base del rectangulo: '))
# h = float(input('Ingrese la altura del rectangulo: '))
# area = b*h
# perimetro = (b+h)*2
# print(f'El area es {area}')
# print(f'El perimetro es {perimetro}')

# 1.2 Pedir el valor de 3 variables, realizar y mostrar el resultado de:
# var1 = int(input('Ingrese el primer valor: '))
# var2 = int(input('Ingrese el segundo valor: '))
# var3 = int(input('Ingrese el tercer valor: '))

# # a. La suma de las dos primeras
# suma = var1 + var2
# print(f'La suma de las dos primeras es {suma}')

# # b. El producto de las dos ultimas
# producto = var2 * var3
# print(f'El producto de las dos ultimas es {producto}')

# # c. Reemplazar el valor de la 3ra. por el triple de la primera
# var3 = var1 * 3
# print(f'El valor de la primera es {var1} y su triple es {var3}')


# # 2. If
# # 2.1 Se ingresa un numero por teclado:
# numero = int(input('Ingrese un numero: '))
# #     a. Informar si es positivo o negativo.
# if numero >=0:
#     print('El numero es positivo')
# else:
#     print('El numero es negativo')

# #     b. Informar si es par o impar.
# if (numero % 2) == 0:
#     print('El numero es par')
# else:
#     print('El numero es impar')

# # 2.2 Dado dos numeros enteros N y M, informar si N es multiplo de M.
# n = int(input('Ingrese un numero: '))
# m = int(input('Ingrese otro numero: '))
# if (n % m) == 0:
#     print('El primer numero es multiplo del segundo')
# else:
#     print('El primer numero NO es multiplo del segundo')


# 3. Elif
# 3.1 Solicitar un numero del 1 al 7 y diga el dıa de la semana correspondiente. Suponga que el lunes es el
#     primer dıa.
# dia = int(input('Ingrese un numero del 1 al 7: '))
# if dia == 1:
#   print('Lunes')
# elif dia == 2:
#   print('Martes')
# elif dia == 3:
#   print('Miercoles')
# elif dia == 4:
#   print('Jueves')
# elif dia == 5:
#   print('Viernes')
# elif dia == 6:
#   print('Sabado')
# elif dia == 7:
#   print('Domingo')
# else:
#   print('Del 1 al 7 te dije pelotudo')

# # 3.2 Solicitar una letra y detecte si es una vocal.
# letra = input('Ingrese una letra: ')
# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#   print('Es una vocal')
# else:
#   print('Es consonante')


# 4. For
# 4.1 Mostrar 10 veces el texto “Estoy probando”.
# for i in range(10):
#   print('Estoy probando')

# 4.2 Modificar el algoritmo anterior para mostrar: “Estoy probando 1”, “Estoy probando 2”, ..., hasta 10.
#     Codificar en lenguaje Python y ejecutar el programa. Verificar los resultados.
# for i in range(10):
#   print(f'Estoy probando {i+1}')

# 4.3 Mostrar los numeros del 0 al 100.
# for i in range(101):
#     print(i)

# 4.4 Pedir 10 numeros y mostrar la suma de los pares y de los impares por separado. Verificar los resultados
#     utilizando la calculadora.
# sumaPares = 0
# sumaImpares = 0
# for i in range(10):
#   numero = int(input(f'Ingrese el numero {i}: '))
#   if (numero % 2) == 0:
#     sumaPares += numero
#   else:
#     sumaImpares += numero
# print(f'Suma de los pares: {sumaPares}')
# print(f'Suma de los impares: {sumaImpares}')

# 4.5 Contar e informar los numeros multiplos de 2 o 3 que hay entre 1 y 100. Verificar el resultado.
# multiplosDe2 = 0
# multiplosDe3 = 0
# for i in range(1, 101):
#   if (i % 2) == 0:
#     multiplosDe2 += 1
#   elif (i % 3) == 0:
#     multiplosDe3 += 1
#   else:
#     pass
# print(f'Cantidad de multiplos de 2 entre 1 y 100: {multiplosDe2}')
# print(f'Cantidad de multiplos de 3 entre 1 y 100: {multiplosDe3}')

# 4.6 Contar e informar los numeros multiplos de 2 y 3 que hay entre 1 y 100. Verificar el resultado.
# multiplosDe2y3 = 0
# for i in range(1, 101):
#   if (i % 2) == 0:
#     multiplosDe2y3 += 1
#   elif (i % 3) == 0:
#     multiplosDe2y3 += 1
#   else:
#     pass
# print(f'Cantidad de multiplos de 2 y 3 entre 1 y 100: {multiplosDe2y3}')

# 4.7 Dado 10 numeros, informar el rango de los mismos [menor, mayor].
# entrada = int(input('Ingrese un numero: '))
# numMenor = numMayor  = entrada
# for i in range(9):
#   entrada = int(input('Ingrese un numero: '))
#   if entrada < numMenor:
#     numMenor = entrada
#   elif entrada > numMayor:
#     numMayor = entrada
#   else:
#     pass
# print(f'Rango: [{numMenor}, {numMayor}]')

# 4.8 Se ingresan 10 numeros. Determinar el promedio de los mismos.
# promedio = 0
# for i in range(10):
#   entrada = int(input('Ingrese un numero: '))
#   promedio += entrada
# promedio /= 10
# print(f'El promedio es: {promedio}')

# 4.9 Dadas las notas de los 85 estudiantes que rindieron un examen, informar el porcentaje de notas superiores a 7.


# 5. While
# 5.1 Programa que pregunte iterativamente “¿Quiere continuar?”, con respuesta S o N.
# while True:
#   entrada = input('Quiere continuar?: S o N ')
#   if entrada == 'S':
#     break

# 5.2 Dadas las notas de los estudiantes que rindieron un examen, informar el porcentaje de notas superiores
#     a 7. El docente desconoce la cantidad que asistio a rendir.

dicc = dict([
  ('jorge ', 4139),
  ('guido ', 4127),
  ('hugo ', 4098)
])