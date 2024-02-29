#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

def colores (**kwargs): #Se usa para utilizar argumentos arbitrarios y puedes pasar diccionarios en ellos
	print("Este es el mes de " + kwargs['mes1'] + '.')

colores(mes1='enero', mes2='febrero')
