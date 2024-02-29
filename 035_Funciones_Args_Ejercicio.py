#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

def alumnos(*args): #Al usar args no espera un limite de argumentos
	print('El primer alumno es ' + args[0] + ' y el último es ' + args[3] + '.')

alumnos('Andrés', 'Ana', 'Andrea', 'Antonio')

#Igual podemos poner cuales son obligatorios (sin *) y cuando es con el * no puede ni esperar ni uno

###############
#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')
#En el primer llamado serian 4 argumentos
#En el segundo llamado serian 3 argumentos
#En el tercer llamado serian 1 argumento
#En el cuarto llamado serian 2 argumentos

#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("negro", "gris")

#Crea una función que realice la suma de cinco números utilizando solo *args.
#Debes imprimir el resultado en la consola. La suma no se realizará directamente
#sobre el print().

def suma(*args):
    r = 0
    for x in args:
        r+=x
    print(r)

suma(2, 4, 6, 8, 10)
