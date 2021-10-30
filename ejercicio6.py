"""
6. Leer por teclado una serie de 10 números enteros. El algoritmo debe 
indicarnos si los números están ordenados de forma creciente, decreciente, 
o si están desordenados
"""

lista = []

for i in range(10):
    num = int(input("ingrese un número: "))
    lista.append(num)

nuevaListaCreciente = lista.copy()
nuevaListaCreciente.sort()

nuevaListaDrecreciente = lista.copy()
nuevaListaDrecreciente.sort()
nuevaListaDrecreciente.reverse()

if nuevaListaCreciente == lista:
    print("Los números están ordenados de forma creciente!")

if nuevaListaDrecreciente == lista:
    print("Los números están de forma decreciente")

if nuevaListaCreciente != lista and nuevaListaDrecreciente != lista:
    print("Los números están desordenados")
