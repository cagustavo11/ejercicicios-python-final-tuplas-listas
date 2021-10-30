"""
10.Leer N enteros y guardarlos en una lista. Guardar en otra lista los elementos 
pares de la primera, y a continuación los elementos impares. Ejemplo
    N = 5
    Lista 1 = [5, 2, 6, 8, 1]
    Lista 2 = [ 2, 6, 8, 5, 1]
"""

lista1 = [5, 2, 6, 8, 1]


lista2 = []
i = 3
for el in lista1:
    if el % 2 == 0:
        lista2.append(el)

for el in lista1:
    if el % 2 != 0:
        lista2.append(el)
print(f'Lista 1: { lista1 }')
print(f'Lista 2: { lista2 }')
# n = int(input("ingrese la cantidad de números a introducir: "))

# for i in range(n):
#     num = int(input("introduce un número: "))
#     lista.append(num)
