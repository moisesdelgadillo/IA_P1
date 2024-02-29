#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

import re #Se importa modulo de expresiones regulares (Regular Expressions)

text = "tres tristes tigres comen trigo en un trigal"
buscar = re.findall("e", text) #Al usar el metodo findall() te devuelve una lista con todas las 'e' que encontró
print(buscar)

buscar = re.findall("osos", text) #Si no encuentra ningun elemento devolvera una lista vacia []
print(buscar)
