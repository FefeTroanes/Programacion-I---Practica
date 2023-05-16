#  PRACTICA 1
# 1. Proponga un algoritmo (en lenguaje natural) para resolver cada uno de los siguientes problemas.
# a. Dada la base y altura de un rectangulo, informar el area y su perımetro.
base = int(input('Ingrese la medida de la base '))
altura = int(input('Ingrese la medida de la altura '))
area = base * altura
print('El area del cuadrado es ', area, 'metros cuadrados')

# b. Calcular la nota final de un alumno que se obtiene de promediar las 3 notas de sus parciales.
nota1 = int(input('Ingrese la primer nota: '))
nota2 = int(input('Ingrese la segunda nota: '))
nota3 = int(input('Ingrese la tercer nota: '))
promedio = (nota1 + nota2 + nota3) / 3
print('Su promedio es: ', promedio)

# c. Calcular la distancia de dos puntos en el plano.
print('Este programa es para calcular la distancia entre dos puntos en el plano.')
x1 = int(input('Por favor ingrese la coordenada X del primer punto: '))
y1 = int(input('Ahora ingrese la coordenada y del mismo: '))
x2 = int(input('Ahora ingrese la coordenada X del segundo punto: '))
y2 = int(input('Por ultimo su coordenada Y: '))

distancia_x = x2 - x1
distancia_y = y2 - y1

distancia = (( distancia_x ** 2 ) + (distancia_y ** 2) ) ** 1/2
