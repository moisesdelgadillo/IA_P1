#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

class User:
	nombre = ''
	apellidos = ''

	def imprimir_datos(self): #el self lo que hace es referirse a los datos del mismo objeto
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario1 = User()

usuario1.nombre = 'Moises'
usuario1.apellidos = 'Delgadillo Lara'

usuario1.imprimir_datos()
