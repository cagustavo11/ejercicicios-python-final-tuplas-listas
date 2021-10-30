"""
14.Solicitar al usuario que ingrese números, los cuales se guardarán en una lista, finalizar al ingresar el número 0, el cual no debe guardarse. A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia, mostrar la lista; Mostrar un mensaje si no es posible eliminar. Ejemplo
Ingresar números en la lista: 
Numero: 5
Numero: 2
Numero: 0
[5, 2]
Ingresa el número a eliminar: 5
Numero eliminado...
"""
# Lista vacia
numbers = []

while True:
    num = int(input("ingrese un numero: "))
    if num == 0:
        break
    numbers.append(num)

# Pedimos el numero a eliminar
newNum = int(input("ingrese el numero a eliminar: "))

newNumbers = numbers.copy()
for num in newNumbers:
    if newNum == num:
        numbers.remove(newNum)
        print("Numero eliminado...")
        print(numbers)
        break
    else:
        print("No se pudo eliminar...")
        break
