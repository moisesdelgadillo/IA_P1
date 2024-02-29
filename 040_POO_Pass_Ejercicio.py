#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

class Clase:
    pass #Al poner pass se puede dejar una clase vacia

class User:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Bienvenido |",self.nombre, self.apellido)

usuario1 = User("Moises", "Delgadillo")
usuario1.saludo()
del usuario1.nombre   #Aqui se elimina el atributo nombre en el objeto
