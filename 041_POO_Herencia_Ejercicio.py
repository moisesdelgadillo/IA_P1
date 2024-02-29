#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

# Esta es la superclase
class Usuarios:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios): #Aqui se indica que hereda de Usuarios
    def vip(self):
        print("Tienes acceso VIP")

usuario1 = Usuarios("Erick", "Delgadillo")
#Erick al ser usuario normal no podra usar la funcion vip()
usuario2 = UsuariosPremium("Moises", "Lara")
#En cambio como Moises es UsuarioPremium si la podrá usar

usuario1.datos()
print("\n")
usuario2.datos()
usuario2.vip()
