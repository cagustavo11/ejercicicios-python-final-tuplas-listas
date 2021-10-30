"""
11.Generar dos listas de 5 enteros generados en forma aleatoria, deberán ser ordenados en forma creciente. Copiar (fusionar) las dos listas en una tercera, de forma que sigan ordenados. (no utilizar funciones) 
Ejemplo:
    Lista 1 = [1, 3, 6, 10, 11] 
    Lista 2 = [2, 4, 12, 13, 16]
    Lista 3 = [1, 2, 3, 4, 6, 10, 11, 12, 13, 16]
"""
import random

lista1 = []
lista2 = []

while len(lista1) <= 5:
    lista1.append(random.randint(1, 25))
    lista2.append(random.randint(1, 25))

lista1.sort()
lista2.sort()

print(f'Lista 1 = { lista1 }')
print(f'Lista 2 = { lista2 }')

lista3 = []

lista3.extend(lista1)
lista3.extend(lista2)

lista3.sort()
print(f'Lista 3 = { lista3 }')
