#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

import re #Se importa modulo de expresiones regulares (Regular Expressions)

###SPLIT()###
text = "tres tristes tigres comen trigo en un trigal"
buscar = re.split(" ", text) #Aqui busca todos los espacios y los elimina, y todas las palabras que quedaron las agrega a una lista
print(buscar)

#maxsplit() se representa como el tercer argumento de split()
#Al usar ese tercer argumento limita hasta cuantas veces se eliminara el espacio

buscar = re.split(" ", text, 4) #Aqui se especifica con maxsplit que solo se quitaran 4 espacios
print(buscar)

###SUB()###
#método sub() reemplaza las coincidencias por lo que le especifiques en
#el segundo argumento.

text = "tres tristes tigres comen trigo en un trigal"
buscar = re.sub(" ", "-", text) #Aqui busca todos los espacios y los sustituye por un '-', y se crea un texto que en vez de tener espacios tiene -
print(buscar)

#Igual se puede limitar cuantas veces lo hara con el parametro count
#que sería el 4to parametro de la funcion

text = "tres tristes tigres comen trigo en un trigal"
buscar = re.sub(" ", "-", text, 4) #Con el 4 se especifica que solo hara el sub() 4 veces
print(buscar)
