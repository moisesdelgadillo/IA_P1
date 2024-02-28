#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

#Nombre del operador        Descripcion
#       >                   Mayor que
#       <                   Menor que
#       >=                  Mayor o igual que
#       <=                  Menor o igual que
#       ==                  Igual que (comparando)
#       !=                  Diferente que (comparando)

#Ejercicios de python
#Al siguiente código añádele un par de rangos de edad.
#Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.

edad = int(input('¿Cuál es tu edad?\n')) #El metodo input hace que te pregunte la consola por un dato

if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad > 45 and edad <= 100:
	print('Eres mayor de edad, pero ya no tan joven.')
elif edad > 100 and edad <= 120:
	print('Eres muy mayor.')
else:
	print('Edad no válida.')
