from pila import Pila

#Crear un objeto de la clase PILA
p = Pila()

#Apilar 9, 8 y 7
p.push(9)
p.push(8)
p.push(7)

print("\n-> Pila Inicial: ")
while p.size() > 0: 
    #Salida -> 7, 
    #          8, 
    #          9
    print(p.pop())

print("\n-> La pila ya esta vacía\n-> Se vuelven a agregar datos a la pila\n")

# Mostrar el tope de la pila
print("-> Se agrega un nuevo dato:")
p.push(-1)

print("-> Tope de la pila: ", p.top())#Salida -> -1
#Desapilamos
print("-> Desapilar: ", p.pop(), "\n")# Salida -> -1

print("-> La pila se volvió a quedar vacía\n-> Se vuelven a agregar datos a la pila\n")

print("-> Se agregan nuevos datos:")
p.push(3)
p.push(2)
p.push(1)

#Mostrar el tope de la pila
print("-> Tope de la pila: ", p.top())#Salida -> 1

print("\n-> Se agrega un nuevo dato:")
p.push(0)

print("-> Tope de la pila: ", p.top())#Salida -> 0

# #Desapilamos todos loe elementos con un while
print("\n-> Pila Final: ")
while p.size() > 0:
    #Salida -> 0
    #          1
    #          2
    #          3
    print(p.pop())