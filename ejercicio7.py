"""
7. Crear un programa que lea por teclado una lista de N números enteros y la desplace una posición hacia adelante: el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente. El último pasa a ser el 
primero. 
Ejemplo
    N = 4
    Lista 1: [5, 4, 3, 9]
    Lista resultante: [9, 5, 4, 3]
"""
lista1 = [5, 4, 3, 9]

# for i in range(10):
#     num = int(input("ingrese un número: "))
#     lista1.append(num)

# N = int(input("ingrese n: "))
print(f'Antes { lista1 }')

lista2 = []

i = 1

for el in lista1:
    if el == lista1[-1]:
        # le quito -1 porque los arrays se cuentan desce 0
        lista2.insert(0, el)
    else:
        lista2.insert(i, el)
    i += 1
print(f'Despúes { lista2 }')
