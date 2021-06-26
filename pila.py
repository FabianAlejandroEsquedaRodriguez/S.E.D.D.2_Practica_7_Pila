#Clase PILA

class Pila:
    def __init__(self):
        self.pila = []

    #Metodo PUSH
    def push(self, dato):
        self.pila.append(dato)

    #Metodo POP
    def pop(self):
        return self.pila.pop()

    #Metodo TOP
    def top(self):
        return self.pila[-1]#Retorna el tope de la pila

    def size(self):
        return len(self.pila)
