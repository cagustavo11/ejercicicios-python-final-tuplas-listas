"""
3. Leer 10 números, almacenarlos en una lista y a continuación realizar la 
media de los números positivos, la media de los negativos y contar el número 
de ceros.
"""


def calcularMediaPositivos(lista):
    suma_positivos = 0
    total_positivos = 0
    for el in lista:
        if el > 0:
            suma_positivos += el
            total_positivos += 1

    mediaPositivos = suma_positivos / total_positivos
    return mediaPositivos


def calcularMediaNegativos(lista):
    suma_negativos = 0
    total_negativos = 0
    for el in lista:
        if el < 0:
            suma_negativos += el
            total_negativos += 1

    mediaNegativos = suma_negativos / total_negativos
    return mediaNegativos


def contarCeros(lista):
    total_ceros = 0
    for el in lista:
        if el == 0:
            total_ceros += 1
    return total_ceros


listaNumeros = []

for i in range(10):
    num = int(input("ingrese un numero: "))
    listaNumeros.append(num)
listaNumeros.sort()
print(listaNumeros)
print(
    f'La media de los números positivos es: { calcularMediaPositivos(listaNumeros) }')
print(
    f'La media de los números negativos es: { calcularMediaNegativos(listaNumeros) }')
print(f'La cantidad de ceros es: { contarCeros(listaNumeros) }')
