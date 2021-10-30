"""
15.Solicitar al usuario que ingrese números, los cuales se guardarán en una lista, finalizar al ingresar el número 0, el cual no debe guardarse. realizar las siguientes acciones con los datos de la lista: 
a) Recorrer la lista para imprimir la sumatoria de todos los elementos. 
b) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
"""

lista_numeros = []

i = 0

while 1:
    num = int(input("ingrese un número: "))
    if num == 0:
        break
    lista_numeros.append(num)

sumatoria = 0
for el in lista_numeros:
    sumatoria += el

print(f'La sumatoria de todos los elementos es: { sumatoria }')

nuevoNumero = int(input("ingrese un nuevo nuevo: "))

listaCopiada = lista_numeros.copy()

for el in lista_numeros:
    if el > nuevoNumero:
        listaCopiada.remove(el)
print(listaCopiada)
