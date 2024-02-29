#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

# el término "scope" (puedes traducirlo cómo alcance en español).
#Bien, cuando veas en algún lado este término, debes saber que se refiere al
#alcance que tiene una variable, si es local o global.

def funcion1():
    global num1 #Aqui se declara que aunque esté dentro del scope de la funcion, la variable "num1" será global
    num1 = 10

funcion1()

print(num1)

#He igual se pueden anidar funciones de la siguiente forma:
def funcion2():
    def funcion3():
        print("FUNCION 3")


    funcion3() #De esta forma estas diciendo que quieres hablar a la funcion 3 desde la funcion 2
funcion2()
