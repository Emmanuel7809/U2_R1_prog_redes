#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron 
import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)
    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())
if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))

