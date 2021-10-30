"""
12.Escribir un algoritmo que permita calcular el cuadrado de los 5 números 
generados en forma aleatoria números positivos, y almacenar los valores en 
una lista de con sublistas. Ejemplo
    Resultado:
    Lista = [ [2,4], [3,9], [5,25], [10,100], [6,36] ]

Agregar los enteros resultantes de la suma y multiplicación de los primeros 
elementos de las sublistas.

Resultado:
Lista=[ [2,4, 6, 8], [3,9, 12, 27], [5,25, 30, 125], [10,100, 110, 1000], [6,36, 42, 216] ]
"""
import random


def llenarLista(cantidadNumeros):
    lista = []
    for _ in range(cantidadNumeros):
        lista.append(random.randint(2, 10))
    return lista


listaNumeros = [2, 3, 5, 10, 6]


nuevaListaAlCuadrado = []

for el in listaNumeros:
    nuevaListaAlCuadrado.append([el, el ** 2])
print(nuevaListaAlCuadrado)

lista3 = nuevaListaAlCuadrado.copy()
j = 0
for el in nuevaListaAlCuadrado:
    suma = 0
    producto = 1

    for i in range(2):
        suma += el[i]
        producto *= el[i]
    lista3[j].append(suma)
    lista3[j].append(producto)
    j += 1

print(lista3)
