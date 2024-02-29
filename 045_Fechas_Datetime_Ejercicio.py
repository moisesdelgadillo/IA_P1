#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

import datetime #Se importa el modulo de fechas

fecha = datetime.datetime.now() #Aqui guarda los datos del dia y tiempo de hoy
print(fecha)


#Igual se puede poner una fecha en especifico:

fecha = datetime.datetime(2003, 9, 3, 9, 45) #Se especifica de año a minuto
#datetime.datetime(year, month, day, hour, minute, second, microsecond, ZT)

print(fecha)
print("\nSu hijo nació:",
      "\nDia: ", fecha.day,
      "\nMes: ", fecha.month,
      "\nAño: ", fecha.year,
      "\nHora: ", fecha.hour, ":", fecha.minute)
