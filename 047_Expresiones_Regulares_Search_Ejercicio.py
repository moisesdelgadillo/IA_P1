#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

import re #Se importa modulo de expresiones regulares (Regular Expresions)

texto = "Bienvenidos a Programación fácil"
#El metodo search() busca lo que le pongas en la variable buscada
busqueda = re.search("i", texto) #Aqui busca la 'i' en la variable texto y cuando la encuentre devolverá en que posición la encontró en la cadena de texto
print(busqueda)

busqueda = re.search("bienvenidos", texto) #Aqui buscará toda la palabra 'bienvenidos' pero al no ser la palabra exacta devolvera un none de que no econtró la palabra buscada
#El metodo search() es exacto asi que tambien tomará en cuenta los acentos
print(busqueda)
