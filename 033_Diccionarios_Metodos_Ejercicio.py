#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

teclado = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

print(len(teclado)) #Te devuelve cuantos keys tienes en tu diccionario
###########
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
del teclado1["Precio"] #Te elimina la key "Precio" (Si no especificas que key se eliminaría todo el diccionario)
print(teclado1)
############
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2['Color'] = 'Negro' #Al hacer esto estas agregando una nueva key con su valor
print(teclado2)
#############
#E igual se pueden crear diccionarios de diccionarios
teclados = { #Asi deberia de ser la sintaxis
    "teclado1": {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
    },
    "teclado2": {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
    }

}

#Tambien existe el metodo keys() que te muestra todas las keys de un diccionario
print(teclado1.keys())
#Igual si quieres copiar un diccionario lo puedes hacer de la siguiente forma
teclado4 = dict(teclado1)
print(teclado4)

print("\n\nEjercicio python")

#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves
#'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la
#consola.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
del teclado1
del teclado2["Categoría"]
del teclado2["Precio"]
print(teclado2)
