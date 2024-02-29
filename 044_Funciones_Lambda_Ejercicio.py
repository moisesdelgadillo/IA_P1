#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

import math  #Al poner import y el nombre del fichero se importan sus propiedades

def area(radio):
	resultado = math.pi * radio**2 #Aqui se está elevando al cuadrado
	print(round(resultado,4)) #Con el metodo round() redondeamos los decimales

area(10)

#Con las funciones lambda se veria de esta manera:

#Las funciones lambda sirven para hacer calculos rapidos y se una sola linea
area = lambda radio: (round(math.pi * radio * radio,2))
# (Nombre de la funcion) = lambda (Parametros): (La operacion a ejecutar)

print(area(10))
