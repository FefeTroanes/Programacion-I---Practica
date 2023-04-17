# PRACTICA 3

# 1. Dada una contraseña verificar que su longitud es superior a 8 caracteres.
print('Verificar si una contrasenia tiene mas de 8 caracteres')
contrasenia = input('Ingrese su contraseña')
if len(contrasenia) > 8:
    print('La pass tiene mas de 8 caracteres')
else:
    print('Contrasenia muy corta. Debe tener mas de 8 caracteres')

# O con operador ternario
print('La pass tiene mas de 8 caracteres' if len(contrasenia) > 8 else 'Contrasenia muy corta. \
Debe tener mas de 8 caracteres' )


# 2. Escribir un programa que verifique si un numero es divisible por 4
print('Verificar si un numero es divisible por 4.')
numeroIngresado = int(input('Ingrese el numero a verificar: '))
if numeroIngresado % 4:
  print(numeroIngresado, 'no es divisible por 4')
else:
  print(numeroIngresado, 'es divisible por 4')

print('no es divisible por 4' if numeroIngresado % 4 else 'es divisible por 4')


# 3. Determinar e informar el mayor valor de 3 numeros enteros. ¿Que cambiarıas en el algoritmo si
#    se trataran de 3 numeros reales o de 3 caracteres o de 3 palabras?.
#    ¿Y si se buscara el menor valor?
print('Este programa verifica el mayor o menor de tres numeros.')
while True:
  num1 = input('Ingrese el primer numero: ')
  num2 = input('Ingrese el segundo numero: ')
  num3 = input('Ingrese el tercer numero: ')

  try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    break # while True genera un bucle infinito hasta que se cumplan estas condiciones
          # y este break hace que salga del bucle si todo es correcto.
  except:
    print('Alguno no es un numero, no te quieras hacer el qa lcdtm. Ingresa numeros.')

mayorBoolean = input('Queres el mayor? Y/n: ')
if mayorBoolean == 'Y' or 'y':
  if num1 >= num2:
    mayorNumber = num1
  else:
    mayorNumber = num2
  if mayorNumber <= num3:
    mayorNumber = num3
  print('El mayor numero es:', mayorNumber)
else:
  if num1 >= num2:
    menorNumber = num2
  else:
    menorNumber = num1
  if menorNumber >= num3:
    menorNumber = num3
  print('El menor numero es:', menorNumber)


# 4. Dados 3 lados de un triangulo, informar si el mismo es equilatero, isosceles o escaleno.
print('Verificar si un triangulo es equilatero, isosceles o escaleno segun la medida de sus lados.')
lado1 = float(input('Ingrese el primer lado: '))
lado2 = float(input('Ingrese el segundo lado: '))
lado3 = float(input('Ingrese el tercer lado: '))
ladosIguales = 1

if lado1 == lado2:
  ladosIguales += 1
if lado1 == lado3:
  ladosIguales += 1
if lado2 == lado3:
  ladosIguales += 1

if ladosIguales == 1:
  print('Es un triangulo escaleno')
elif ladosIguales == 2:
  print('Es un triangulo isosceles')
else:
  print('Es un triangulo equilatero')


# 5. Convertir las calificaciones alfabeticas ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’ en calificaciones
#    numericas 5, 6, 7, 8, 9 y 10 respectivamente. Ingresar una calificacion alfabetica e informar
#    por pantalla la calificacion numerica correspondiente, en caso de ingresar cualquier otra letra
#    mostrar ((error calificacion inexistente)).
print('Este programa convierte las calificaciones alfabeticas ‘I’, ‘A’, ‘B’, ‘M’, ‘D’ y ‘E’ en \
      calificaciones numericas 5, 6, 7, 8, 9 y 10 respectivamente')
calificacion = input('Ingrese la calificacion que desea convertir: ')
print(calificacion)
if calificacion == 'I' or calificacion == 'i':
  print('La calificacion es: 5')
elif calificacion == 'A' or calificacion == 'a':
  print('La calificacion es: 6')
elif calificacion == 'B' or calificacion == 'b':
  print('La calificacion es: 7')
elif calificacion == 'M' or calificacion == 'm':
  print('La calificacion es: 8')
elif calificacion == 'D' or calificacion == 'd':
  print('La calificacion es: 9')
elif calificacion == 'E' or calificacion == 'e':
  print('La calificacion es: 10')
else:
  print('Error. Calificacion inexistente. (Pelotudo)')


# 6. Escribir un programa que le pregunte a las personas su fecha de cumpleanos y en base a eso
#    imprimir su signo zodıaco. Recomendacion, pedirle a la persona ingresar la fecha con cierto
#    formato, por ejemplo DD/MM y si la persona no lo respeta, imprimir un mensaje de error.
print('Signo zodiacal en base a la fecha de nacimiento')
print('Ingrese la fecha en el orden DD/MM')
dia = int(input('Ingrese el dia: '))
mes = int(input('Ingrese el mes: '))

if mes <= 0 or mes > 12:
  print('Mes invalido')
elif dia <= 0 or dia > 31:
  print('Dia invalido')
else:
  if (mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 10) and dia > 30:
    print('Fecha invalida')
  else:
    if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
      print('Aries')
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
      print('Tauro')
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
      print('Geminis')
    elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
      print('Cancer')
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
      print('Leo')
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
      print('Virgo')
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
      print('Libra')
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
      print('Escorpio')
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
      print('Sagitario')
    elif (dia >= 22 and mes == 12) or (dia <= 20 and mes == 1):
      print('Capricornio')
    elif (dia >= 21 and mes == 1) or (dia <= 19 and mes == 2):
      print('Acuario')
    elif (dia >= 20 and mes == 2) or (dia <= 20 and mes == 3):
      print('Piscis')


# 7. En el centro de la ciudad de Rosario el estacionamiento en vıa se encuentra tarifado y esta
#    dividido en tres zonas con tarifas diferenciadas. El vehıculo puede estacionarse como maximo
#    por 3 horas en el mismo sitio, luego de este tiempo, para renovar el servicio, hay que mover el
#    vehıculo. La siguinte tabla muestra los costos por hora en cada una de las zonas:

#       Zona    Primer hora    Segunda hora    Tercer Hora
#         A     $57,00         $71,20          $85,50
#         B     $47,00         $58,70          $70,50
#         C     $37,00         $46,20          $55,50
#    Escribir un programa que dada la zona, A, B o C, y la cantidad de horas que el vehıculo estara
#    estacionado, devuelva el costo a pagar. En caso de que el tiempo de estacionamiento supere las
#    3 horas, imprimir un mensaje de error acorde.
zona = input('Ingrese la zona en la cual va a estacionar: ')
if (zona != 'A') and (zona != 'a') and (zona != 'B') and (zona != 'b') and (zona != 'C') and (zona != 'c'):
  print('Zona invalida.')
else:
  horas = float(input('Ingrese la cantidad de tiempo que pretende estacionar: '))
  costo = 0

  if horas > 3:
    print('No esta permitido estacionar mas de tres horas.')
  else:
    if zona == 'A' or zona == 'a':
      if horas <= 1:
        costo = 57
      elif horas <= 2:
        costo = 57 + 71.2
      else:
        costo = 57 + 71.2 + 85.5
    elif zona == 'B' or zona == 'b':
      if horas <= 1:
        costo = 47
      elif horas <= 2:
        costo = 47 + 58.7
      else:
        costo = 47 + 58.7 + 70.5
    elif zona == 'C' or zona == 'c':
      if horas <= 3:
        costo = 37
      elif horas <= 2:
        costo = 37 + 46.2
      else:
        costo = 37 + 46.2 + 55.5
    print('Total: $', costo, ' peronios.')


# 8. Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local:
#
#    Item        Rosario  Funes  Roldan
#    Zapatillas  30 %     40 %   25 %
#    Remeras     20 %     30 %   15 %
#    Pantalones  10 %     5 %    20 %
#    Dado un item y la sede del local, devolver el descuento que se recibira.
print('Productos:')
print('1. Zapatillas')
print('2. Remeras')
print('3. Pantalones')
item = int(input('Ingrese el numero del producto que quiere comprar: '))
print('Localidad:')
print('1. Rosario')
print('2. Funes')
print('3. Roldan')
localidad = int(input('Ingrese el codigo de la localidad: '))

if item == 1:           # Zapatillas
  if localidad == 1:    # Rosario
    print('Descuento: 30%')
  elif localidad == 2:  # Funes
    print('Descuento: 40%')
  elif localidad == 3:  # Roldan
    print('Descuento: 25%')
  else:
    print('Localidad invalida.')
elif item == 2:         # Remeras
  if localidad == 1:    # Rosario
    print('Descuento: 20%')
  elif localidad == 2:  # Funes
    print('Descuento: 30%')
  elif localidad == 3:  # Roldan
    print('Descuento: 15%')
  else:
    print('Localidad invalida.')
elif item == 3:         # Pantalones
  if localidad == 1:    # Rosario
    print('Descuento: 10%')
  elif localidad == 2:  # Funes
    print('Descuento: 5%')
  elif localidad == 3:  # Roldan
    print('Descuento: 20%')
  else:
    print('Localidad invalida.')
else:
  print('Item invalido')


# 9. Ahora, supongamos que ademas dependiendo del dıa de la semana se puede recibir un descuento
#    adicional acumulable. Es decir, si se recibio un descuento del 10 % segun el ıtem y la sede y
#    la compra se realiza un lunes, el descuento total sera un 20 % . Escribir un programa en el
#    que la persona pueda ingresar el dıa de la semana, el item a comprar y la sede del local.
#    Luego, informar el descuento total a recibir. Utilizar la siguiente tabla de descuentos
#               Lunes Miercoles Jueves
#    Descuento  10 %  8 %       5 %

print('Productos: 1.Zapatillas 2.Remeras 3.Pantalones')
item = int(input('Ingrese el codigo del producto que quiere comprar: '))
print('Localidad: 1.Rosario 2.Funes 3.Roldan')
localidad = int(input('Ingrese el codigo de la localidad: '))
print('Dia: 1.Lunes 2.Miercoles 3.Jueves')
dia = int(input('Ingrese el codigo del dia.'))
descuento = 0
flag = 0
if item == 1:           # Zapatillas
  if localidad == 1:    # Rosario
    descuento += 30
  elif localidad == 2:  # Funes
    descuento += 40
  elif localidad == 3:  # Roldan
    descuento += 25
  else:
    print('Localidad invalida.')
    flag += 1
elif item == 2:         # Remeras
  if localidad == 1:    # Rosario
    descuento += 20
  elif localidad == 2:  # Funes
    descuento += 30
  elif localidad == 3:  # Roldan
    descuento += 15
  else:
    print('Localidad invalida.')
    flag += 1
elif item == 3:         # Pantalones
  if localidad == 1:    # Rosario
    descuento += 10
  elif localidad == 2:  # Funes
    descuento += 5
  elif localidad == 3:  # Roldan
    descuento += 20
  else:
    print('Localidad invalida.')
    flag += 1
else:
  print('Item invalido')

if flag == 0:
  if dia == 1:    # Lunes
    descuento += 10
  elif dia == 2:  # Miercoles
    descuento += 8
  elif dia == 3:  # Jueves
    descuento += 5
  else:
    print('Dia invalido.')
    flag += 1
  print('Descuento total: ', descuento, '%')
