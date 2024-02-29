#ERICK MOISES DELGADILLO LARA
#21310139 - 6E1

import datetime, locale #El modulo locale hace que se cambie el lenguaje a español
#locale.setlocale(locale.LC_ALL, "es-ES") #Esto es lo que hace que cambie a español

ahora = datetime.datetime.now()
#strftime() = STRING FORMAT TIME
#El metodo obj.strftime() indica que formato quieres usar con el texto del print

print(ahora.strftime("Día de la semana abreviado: %a "))
print(ahora.strftime("Día de la semana completo: %A "))
print(ahora.strftime("Mes abreviado: %b "))
print(ahora.strftime("Mes completo: %B "))
print(ahora.strftime("Fecha completa: %c "))
print(ahora.strftime("Siglo (empieza a contar desde cero): %C "))
print(ahora.strftime("Día del mes (01 - 31): %d "))
print(ahora.strftime("Día/hora/año: %D "))
print(ahora.strftime("Día del mes (1 - 31): %e "))
print(ahora.strftime("Año en dos dígitos: %g "))
print(ahora.strftime("Año en cuatro dígitos: %G "))
print(ahora.strftime("Mes abreviado: %h "))
print(ahora.strftime("Hora (00 - 23): %H "))
print(ahora.strftime("Hora (01 - 12): %I "))
print(ahora.strftime("Día del año: %j "))
print(ahora.strftime("Mes del 01 al 12: %m "))
print(ahora.strftime("Minuto: %M "))
print(ahora.strftime("Salto de línea: %n"))
print(ahora.strftime("AM o PM: %p "))
print(ahora.strftime("Hora + AM o PM: %r"))
print(ahora.strftime("Hora y minutos: %R"))
print(ahora.strftime("Segundos: %S"))
print(ahora.strftime("Tabulación: %t"))
print(ahora.strftime("Hora, minutos y segundos: %T"))
print(ahora.strftime("Día de la semana (número): %u"))
print(ahora.strftime("Semana del año (empieza en domingo): %U"))
print(ahora.strftime("Semana del año(Condiciones especiales): %V"))
print(ahora.strftime("Semana del año (empieza en lunes): %W"))
print(ahora.strftime("Día de la semana (empieza en domingo): %w"))
print(ahora.strftime("Día/mes/año de dos dígitos: %x"))
print(ahora.strftime("Hora/minutos/segundos: %X"))
print(ahora.strftime("Año corto: %y"))
print(ahora.strftime("Año largo: %Y"))
