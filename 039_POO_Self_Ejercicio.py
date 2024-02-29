#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

#¿Qué significa self de Python?
#Cambiando un poco de tema, self es como el this en otros lenguajes de programación.
#Es simplemente una palabra reservada de Python para referirse "a si mismo",
#de esa forma no tenemos que escribir por ejemplo NombreDeClase.atributo1,NombreDeClase.atributo2.

class User:
	def __init__(self, nombre, apellidos):
	    self.nombre = nombre
	    self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = User('Moises', 'Delgadillo')

usuario002 = User('Erick', 'Lara')

usuario002.nombre = 'Kevin'

usuario002.imprime_datos()
