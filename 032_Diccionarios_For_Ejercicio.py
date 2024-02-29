#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

teclado1 = {
	'Objeto': 'Teclados',
	'Modelo': 'HyperX',
	'Precio': '60'
}

teclado2 = {
	'Objeto': 'Teclados',
	'Modelo': 'Corsair K55',
	'Precio': '42'
}

teclado1['Precio'] = '85' #Al querer editar un valor en un diccionario solo se tendrá que hacer esto
print(teclado1['Precio'])
print("\n")
#Al usar un bucle for en diccionarios se imprimira solo las categorias y no
#sus valores

for x in teclado1:
    print(x)
print("\n")
#Pero al hacer un for especificando que quieres que imprima saldran los respectivos
#valores:

for x in teclado2: #Igual se puede usar 'teclado2.values()' e imprimirá directamente solo los valores
    print(teclado2[x])
print("\n")

#Itera el diccionario teclado1 con un solo
#bucle for que muestre esto en la consola:
for x in teclado1:
    print(x, "=", teclado1[x])
