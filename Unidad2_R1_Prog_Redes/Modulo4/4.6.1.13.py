#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
from calendar import Calendar

class MiCalendario(Calendar):
    def contar_dia_de_la_semana_en_año(self, year, weekday):
        if not (0 <= weekday <= 6):
            raise ValueError("El día de la semana debe ser un número entre 0 y 6.")
        
        count = 0
        for month in range(1, 13):
            for week in self.monthdayscalendar(year, month):
                for day in week:
                    if day == weekday and day != 0:
                        count += 1
        
        return count

mi_calendario = MiCalendario()

print(mi_calendario.contar_dia_de_la_semana_en_año(2019, 0))  # Número de veces que ocurrió el lunes en 2019
print(mi_calendario.contar_dia_de_la_semana_en_año(2000, 6))  # Número de veces que ocurrió el domingo en 2000
