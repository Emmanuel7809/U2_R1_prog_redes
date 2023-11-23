#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.items = []

    def put(self, elem):
        self.items.insert(0, elem)

    def get(self):
        if not self.items:
            raise QueueError("La cola está vacía")
        return self.items.pop()


que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except QueueError as e:
    print(f"Error de Cola: {e}")

