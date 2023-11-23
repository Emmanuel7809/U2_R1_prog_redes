#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        if weekday < 0 or weekday > 6:
            raise ValueError("El valor de 'weekday' debe estar entre 0 y 6.")

        all_weeks = self.yeardays2calendar(year)
        count = 0

        for month in all_weeks:
            for week in month:
                if any(day[weekday] != 0 for day in week):
                    count += 1

        return count

my_cal = MyCalendar()
result = my_cal.count_weekday_in_year(2019, 0)
print(f"En 2019, el lunes (día 0) aparece {result} veces en el año.")

