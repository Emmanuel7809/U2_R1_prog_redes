#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
class WeekDayError(Exception):
    pass

class Weeker:
    DAYS_OF_WEEK = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        if day not in self.DAYS_OF_WEEK:
            raise WeekDayError("Día de la semana no válido")
        self.__current_day = day

    def __str__(self):
        return self.__current_day

    def add_days(self, n):
        index = self.DAYS_OF_WEEK.index(self.__current_day)
        new_index = (index + n) % len(self.DAYS_OF_WEEK)
        self.__current_day = self.DAYS_OF_WEEK[new_index]

    def subtract_days(self, n):
        index = self.DAYS_OF_WEEK.index(self.__current_day)
        new_index = (index - n) % len(self.DAYS_OF_WEEK)
        self.__current_day = self.DAYS_OF_WEEK[new_index]

if __name__ == "__main__":
    try:
        weekday = Weeker('Lun')
        print(weekday)
        weekday.add_days(15)
        print(weekday)
        weekday.subtract_days(23)
        print(weekday)
        weekday = Weeker('Lun')
    except WeekDayError:
        print("Lo siento, no puedo atender tu solicitud.")
