"""
8. Crear un programa que lea por teclado una lista de 10 números enteros y desplace N posiciones en una segunda lista (N es digitado por el usuario). 
Ejemplo
    N=2
    Lista 1: [2, 3, 5, 9, 0, 7, 0, 1, 8, 4] 
    Lista 2: [8, 4, 2, 3, 5, 9, 0, 7, 0, 1]
"""
lista1 = []

for i in range(10):
    num = int(input("ingrese un número: "))
    lista1.append(num)

N = int(input("ingrese n: "))

lista2 = []
j = N
for el in lista1:

    if el == lista1[-1]:
        lista2.insert(N-1, el)
    elif el == lista1[-2]:
        lista2.insert(N-2, el)
    else:
        lista2.insert(j, el)
    j += N
print(lista2)
