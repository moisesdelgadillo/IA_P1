#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

#       Tip no.1
x1 = 100
y1 = 200

if x1 < y1: print('x1 es menor que y1.') #Si solo tendra una instruccion el if se puede poner en la misma linea

#       Tip no.2
x2 = 10000
y2 = 200

#Igual si solo es una linea en el if y en el else se puede usar esta forma de acomodo
print('x2 es menor que y2.') if x2 < y2 else print('x2 no es menor que y2')

#       Tip no.3
x3=1
y3=2

if x3<y3 and x3>y3: print("Los dos argumentos son true") #En el and deben de ser todos true para cumplirse
if x3<y3 or x3>y3: print("Minimo un argumento es true") #En el or minimo uno debe de ser true para cumplirse
