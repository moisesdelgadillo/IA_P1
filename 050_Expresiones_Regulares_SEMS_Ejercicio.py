#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

import re #Se importa modulo de expresiones regulares (Regular Expressions)

#METACARACTERES
#[]	Un conjunto de caracteres.	"[a-z]"
#{}	Especifican un número determinado de resultados.
#       En el ejemplo el {2} representa dos letras o.	"zo{2}lógico"
#()	Agrupan patrones.	
#\	Se utiliza para especificar una secuencia especial.	"\A"
#|	Se utiliza para especificar que encuentre un resultado u otro.	"par|impar"
#.	Carácter comodín, reemplaza cualquier carácter.	"programa..ón fác.l"
#^	Comienza con lo que le escribas.	"^hola"
#$	Termina con lo que le escribas.	"mundo$"
#*	Ninguno o más resultados.	"es*"
#+	Uno o más resultados.	"es+"

texto = "Bienvenidos a Programación fácil y bienvenidos al curso de Python."
buscar = re.findall("[c-g]", texto) #Devuelve una lista con las coincidencias de caracteres encontrados en el string, en el rango entre la letra c y la g.
print(buscar)

#O igual se podría usar de esta forma
texto = "El futuro es ahora."
buscar = re.findall("pasado|futuro", texto) #Aqui busca, pasado o futuro
if buscar: #Si lo encuentra devolverá true y se cumplirá el if
    print("Hay al menos una coincidencia.")
else:
    print("No hay coincidencias.")

#SECUENCIAS ESPECIALES
#\A	Devuelve una coincidencia si los caracteres especificados se encuentran al principio de la cadena.	"\ABienvenidos"
#\b	Devuelve una coincidencia si los caracteres especificados se encuentran al principio o al final de una palabra.	"Bienvenidos\b"
#\B	Devuelve una coincidencia si los caracteres especificados se encuentran entre una palabra, pero no al principio o al final.	"veni\B"
#\d	Devuelve una coincidencia si el string contiene dígitos del 0 al 9.	"\d"
#\D	Devuelve una coincidencia si en el string no hay ningún dígito.	"\D"
#\s	Devuelve una coincidencia si en el string hay al menos un espacio en blanco.	"\s"
#\S	Devuelve una coincidencia si en el string no hay ningún espacio en blanco.	"\S"
#\w	Devuelve una coincidencia si el string contiene cualquier carácter de la a a la z, dígitos del 0 al 9 o la barra baja "_"	"mundo$"
#\W	Devuelve una coincidencia si el string no contiene cualquier carácter de la letra a a la z.	"es*"
#\Z	Devuelve una coincidencia si los caracteres especificados están al final del string.	"fácil\Z"

#SETS DE PYTHON
#[$]	  Todos estos símbolos +, *, $ ()... lo que quieren decir es literalmente ellos mismos, es decir, si pones en el set el símbolo dólar, buscará ese símbolo literalmente en un string.
#[abc]	  Buscará si están estos caracteres en el string.
#[e-q]	  Buscará en el string si hay los caracteres comprendidos entre el rango de letras de la e a la q.
#[^abc]	  Buscará cualquier carácter excepto a, b y c.
#[2-7]	  Busca cualquier dígito entre el rango de 2 y 7.
#[c-kC-K]  Busca en el string cualquier carácter comprendido en el rango de la letra c a la k independientemente de si es mayúscula o minúscula.
