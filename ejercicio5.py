"""
5. Ingresar por teclado dos listas de 10 números enteros y mezclarlas en una tercera lista de la forma: el 1° de A, el 1° de B, el 2° de A, el 2° de B, etc.
"""

lista1 = []
lista2 = []

listaFinal = []

for i in range(5):
    num = int(input("ingrese un número: "))
    lista1.append(num)
    listaFinal.append(num)

print('*******')
j = 1
for i in range(5):
    num = int(input("ingrese un número: "))
    lista2.append(num)
    listaFinal.insert(j, num)
    j += 2

print(listaFinal)
