#Alan Francisco Emmanuel Aguilar Fuentes
#Recuperacion 1 Unidad 2 Introducción a las REST API
#Programación de Redes 
#Profesor: Gabriel Barron Rodriguez

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        # Llena el constructor con acciones apropiadas.
        super().__init__()  
        self.__counter = 0  

    def get_counter(self):
        # Presenta el valor actual del contador al mundo.
        return self.__counter

    def pop(self):
        # Haz un pop y actualiza el contador.
        val = super().pop()  
        self.__counter += 1  
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
