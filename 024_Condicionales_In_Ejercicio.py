#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

#Ejercicios de python
#Haz una tupla que contenga cuatro colores de tu elección. Tendrás que poner una condición
#con el condicional if para cada color que le avise al usuario que el color está en la
#tupla con un mensaje como este: print('El color rojo está admitido') y una condición False
#para contemplar cualquier color que no esté en la tupla con un mensaje como este: print('Color
#no admitido'). No puedes utilizar el operador ==.Además tendrás que hacer esto con un input()
#que permita introducir un color al usuario.

tupla = ("blanco", "gris", "negro", "azul")
color = input("Escribe un color:    ")

if color in tupla[0]: #El metodo in te dice si un dato esta dentro de una lista o dupla
    print("El color blanco esta admitido")
elif color in tupla[1]:
    print("El color gris esta admitido")
elif color in tupla[2]:
    print("El color negro esta admitido")
elif color in tupla[3]:
    print("El color azul esta admitido")
else:
    print('Color no admitido')

