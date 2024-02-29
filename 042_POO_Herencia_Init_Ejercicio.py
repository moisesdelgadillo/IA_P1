#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

# Esta es la superclase
class Usuarios:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def datos(self):
        print("Tienes acceso ordinario", self.nombre, self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios): #Aqui se indica que hereda de Usuarios
    
    def __init__(self, nombre, apellidos, instagram): #Aqui se crea su propio constructor para poder añadir más atributos
        Usuarios.__init__(self, nombre, apellidos) #Aqui se pasan los atributos que se desean heredar en esta clase
        self.instagram = instagram #Aqui se crea el nuevo atributo que se desea añadir
    
    def vip(self):
        print("Tienes acceso VIP", self.nombre, self.apellidos, "@" + self.instagram)

usuario1 = Usuarios("Erick", "Delgadillo")
#Erick al ser usuario normal no podra usar la funcion vip()
usuario2 = UsuariosPremium("Moises", "Lara", "moydelgaa")
#En cambio como Moises es UsuarioPremium si la podrá usar

usuario1.datos()
usuario2.vip()
