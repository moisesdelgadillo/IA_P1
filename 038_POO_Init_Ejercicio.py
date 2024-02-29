#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

class Usuario:
	def __init__(self, nombre, apellidos): #El __init__ es un constructor
		self.nombre = nombre #Aqui nos esta diciendo que el nombre que le pasemos al crear el objeto será el nombre que se guarde en el objeto
		self.apellidos = apellidos#Aqui nos esta diciendo que los apellidos que le pasemos al crear el objeto serán los apellidos que se guarde en el objeto

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario1 = Usuario('Moises', 'Delgadillo Lara')
usuario2 = Usuario('Ivan', 'Lara Ruvalcaba')

usuario1.imprime_datos() #Aqui ya no se deben de pasar los parametros del nombre ya que estan guardados en el objeto
usuario2.imprime_datos()
