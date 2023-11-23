#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise QueueError("Queue is empty")

class SuperQueue(Queue):
    def is_empty(self):
        return super().is_empty()

if __name__ == "__main__":
    que = SuperQueue()

    que.put(1)
    que.put("perro")
    que.put(False)

    for i in range(4):
        if not que.is_empty():
            print(que.get())
        else:
            print("Cola vacía")
