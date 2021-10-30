"""
1. Calcular el promedio, la mediana y la moda de una lista de N números, N es 
ingresado por el usuario. No utilizar funciones.
"""
import random


def llenarLista(cantidadNumeros):
    lista = []
    for _ in range(cantidadNumeros):
        lista.append(random.randint(1, 10))
    return lista


def calcularModa(lista):
    mayor = 0
    for el in lista:
        if lista.count(el) > mayor:
            mayor = el
    return mayor


def calcularPromedio(totalDatos, sumaDatos):

    promedio = sumaDatos / totalDatos
    return promedio


def calcularMediana(lista):
    return lista[(len(lista) // 2)] + lista[(len(lista) // 2) - 1] / 2


n = int(input("ingrese un número n: "))

listaNumeros = llenarLista(n)

sumaNumeros = 0
for el in listaNumeros:
    sumaNumeros += el

listaNumeros.sort()
print(listaNumeros)
print(f"La mediana es: { calcularMediana( listaNumeros ) }")
print(
    f"El promedio es: { calcularPromedio( len(listaNumeros), sumaNumeros ) }")
print(
    f"La moda es: { calcularModa( listaNumeros ) }")
