#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53, 00)
formatted_date_time = dt.strftime('%Y/%m/%d %H:%M:%S')
print(formatted_date_time)
formatted_date_time_long = dt.strftime('%y/%B/%d %I:%M:%S %p')
print(formatted_date_time_long)
formatted_date_short = dt.strftime('%a, %Y %b %d')
print(formatted_date_short)
formatted_date_long = dt.strftime('%A, %Y %B %d')
print(formatted_date_long)
weekday_number = dt.strftime('%w')
print("Día de la semana:", weekday_number)
day_of_year = dt.strftime('%j')
print("Día del año:", day_of_year)
week_number = dt.strftime('%W')
print("Número de semana en el año:", week_number)
