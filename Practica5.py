# ################ LISTAS ################

# 1. Escriba los siguientes programas. Nota: No utilice los metodos index, min, max, reverse.
#    a. Dada una lista de números list y un número n, determine en qué índice de la lista list se
#       encuentra el número n. En caso de no encontrarlo, el programa mostrará -1. Ejemplos:
#       list = [11 ,25 ,3 , -4 ,95]
#       n = 3  => El programa debería mostrar 2
# lista = []
# while True:
#   entrada = input('Ingrese un valor. Ingrese x para terminar: ')
#   if entrada == 'x':
#     break
#   else:
#     lista.append(entrada)
# n = input('Ingrese el valor que desea buscar en la lista: ')
# if (n in lista):
#   for index, value in enumerate(lista):
#     if value == n:
#       print(index)
#     else:
#       continue
# else:
#   print(-1)

# b. Dada una lista de números, calcule el mínimo y el máximo de la lista. Nota: es posible hacerlo
#    recorriendo una única vez la lista o recorriéndola dos veces. Piense las ventajas y desventajas de
#    ambos métodos.
#    numeros = [11 ,25 ,3 , -4 ,95]
#    El programa debería mostrar
#    El mínimo es -4
#    El máximo es 95
# lista = []
# while True:
#   entrada = input('Ingrese un numero para agregar a la lista. x para terminar: ')
#   if entrada == 'x':
#     break
#   else:
#     lista.append(entrada)
# minimo = lista[0]
# maximo = lista[1]
# for elemento in lista:
#   if minimo > elemento:
#     minimo = elemento
#   elif maximo < elemento:
#     maximo = elemento
#   else:
#     pass
# print(f'El minimo es {minimo}')
# print(f'El maximo es {maximo}')

# c. Dada una lista de números, cree una nueva lista sumando 1 a cada elemento.
#    numeros = [0 ,1 ,2 ,3 ,4]
#    El programa deber ía mostrar [1 ,2 ,3 ,4 ,5]
# listaOriginal = []
# listaMas1 = []
# while True:
#   entrada = input('Ingrese numeros. x para terminar: ')
#   if entrada == 'x':
#     break
#   else:
#     entrada = int(entrada)
#     listaOriginal.append(entrada)
# for elemento in listaOriginal:
#   listaMas1.append(elemento + 1)
# print(listaMas1)

# d. Dada una lista palabras de cadenas de texto, devuelva una nueva lista formada sólo por las
#    cadenas de palabras que empiezan con "a".
#    palabras = ["arbol", "barco", "artificial", "casa", "dado", "a"]
#    # El programa debería mostrar => [" arbol ", " artificial ", "a"]
# listaDePalabritas = []
# listaDePalabritas2 = []
# while True:
#   entrada = input('Ingrese palabritas. Ingrese 1 para terminar: ')
#   if entrada == '1':  # antes puse entrada == 1 y no funciono
#     break
#   else:
#     listaDePalabritas.append(entrada)
# for element in listaDePalabritas:
#   if element[0] == 'a':
#     listaDePalabritas2.append(element)
# print(listaDePalabritas2)

# e. Dada una lista de números, calcule:
#    1. la suma de los elementos que se encuentran en un índice par en la lista
#    2. el producto de los elementos de posiciones con índice impar.
#    numeros = [0 ,1 ,2 ,3 ,4 ,5]
#    # El programa debería mostrar
#    La suma de índices pares es 6
#    El producto de índices impares es 15
# listaDeNumeros = []
# sumaDePares = 0
# productoDeImpares = 1
# while True:
#   entrada = input('Ingrese numeritos. Ingrese x para terminar: ')
#   if entrada == 'x':
#     break
#   else:
#     listaDeNumeros.append(entrada)
# for index, value in enumerate(listaDeNumeros):
#   if (index % 2) == 0:
#     sumaDePares += value
#   else:
#     productoDeImpares *= value
# print(f'La suma de índices pares es {sumaDePares}')
# print(f'El producto de índices impares es {productoDeImpares}')

# f. Dada una lista cualquiera, cree una nueva lista con los mismos elementos pero en el orden inverso.
#    numeros = [0 ,1 ,2 ,3 ,4 ,5]
#    El programa deber ía mostrar => [5 ,4 ,3 ,2 ,1 ,0]
# listita = []
# listitaInvertida = []
# while True:
#   entrada = input('Ingrese numeritos. Ingrese x para terminar: ')
#   if entrada == 'x':
#     break
#   else:
#     listita.append(entrada)
# for elemento in listita:
#   listitaInvertida.insert(0, elemento)
# print(listitaInvertida)


# 2. Escriba un programa que dada una lista de números list devuelva otra lista cuyos elementos sean las
#    sumas acumuladas de los elementos de list en cada posición. Es decir, una nueva lista donde el primer
#    elemento es el mismo que en la lista original list, el segundo elemento es la suma del primer y segundo
#    elementos de list, el tercer elemento es la suma del resultado anterior con el tercer elemento de la
#    lista original y así sucesivamente. Por ejemplo, dada la lista [1, 2, 3], la suma acumulada debería
#    ser [1, 3, 6].
# lista1 = []
# lista2 = []
# aux = 0
# while True:
#   entrada = input('Ingrese numeritos. Ingrese x para terminar: ')
#   if entrada == 'x':
#     break
#   else:
#     lista1.append(int(entrada))
# for elemento in lista1:
#   aux += elemento
#   lista2.append(aux)
# print(lista2)


# 3. Escriba un programa que dada una lista determine si tiene algún elemento repetido e imprimirlos.
#    Puede asumir que un numero se repite a lo sumo una vez. Pista: Utilice slicing de listas.
# lista = []
# listaDeRepetidos = []
# while True:
#   entrada = input('Ingrese numeritos. Ingrese x para terminar: ')
#   if entrada == 'x':
#     break
#   else:
#     lista.append(int(entrada))
# for index1, value1 in enumerate(lista):
#   for index2, value2 in enumerate(lista):
#     if (index1 != index2) and (value1 == value2):
#       if (value1 in lista):
#         pass
#       else:
#         listaDeRepetidos.append(value1)
# print(f'Los repetidos son: {listaDeRepetidos}')


# 4. Calcule los n primeros números de la secuencia de Fibonacci en una lista. Es decir, el programa
#    comenzara con la lista [0,1] y computará iterativamente el siguiente número de la secuencia.
# 0 1 1 2 3 5 8 13 21 34
# lista = [0, 1]
# secuencia = []
# anterior = 0
# n = int(input('Ingrese la cantidad de numeros que quiere para la secuencia: '))
# for i in range(n):
#   suma = lista[i] + lista[i+1]
#   anterior = lista[i]
#   lista.append(suma)
#   secuencia.append(anterior)
# print(secuencia)


# 5. El objetivo de este ejercicio es recolectar datos de personas y almacenarlos en una especie de base de
#    datos. A través de lo diferentes ítems, los iremos guiando en la creación de la misma.
# a. Escribir un programa que le pida al usuario ingresar por consola los siguientes datos por separado:
#    Nombre, Apellido, Localidad, Edad, DNI, Carrera universitaria en curso, año de inicio de la
#    carrera. Guardar los datos en una lista llamada datos_personales e imprimirlos en pantalla.
