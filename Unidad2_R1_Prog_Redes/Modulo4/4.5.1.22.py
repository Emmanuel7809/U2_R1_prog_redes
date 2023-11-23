#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez

from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53, 00)

print(dt.strftime('%Y/%m/%d %H:%M:%S')) # 2020/11/04 14:53:00
print(dt.strftime('%y/%B/%d %I:%M:%S %p')) # 20/November/04 02:53:00 PM
print(dt.strftime('%a, %Y %b %d')) # Wed, 2020 Nov 04
print(dt.strftime('%A, %Y %B %d')) # Wednesday, 2020 November 04

print("Día de la semana:", dt.strftime('%w')) # 3

print("Día del año:", dt.strftime('%j')) # 309

print("Número de semana en el año:", dt.strftime('%W')) # 44