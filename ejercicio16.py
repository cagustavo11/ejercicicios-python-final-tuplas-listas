"""
16.Generar una lista con números 10 números aleatorios menores a 10, luego generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
Por ejemplo, si la lista original es [4, 6, 7, 2, 2, 9, 6, 9, 6, 4] la nueva lista 
contendrá: [(4, 2), (6, 3), (7, 1), (2, 2), (9, 2)]
"""

import random


lista = [4, 6, 7, 2, 2, 9, 6, 9, 6, 4]

# for i in range(10):
#     lista.append(random.randint(1, 9))


nuevaListaTupla = []

nuevaCopia = nuevaListaTupla.copy()
for i in range(len(lista) // 2):
    nuevaListaTupla.append((lista[i], lista.count(lista[i])))
    if lista[i] == lista[i + 1]:
        lista.remove(lista[i])

print(nuevaListaTupla)
