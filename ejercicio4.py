"""
4. Leer N números enteros, guardarlos en una lista. Debemos mostrarlos en el 
siguiente orden: el primero, el último, el segundo, el penúltimo, el tercero, 
etc.
"""


numeros_a_ingresar = int(input("¿Cuántos números desea ingresar?: "))

# listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaNumeros = []

for i in range(numeros_a_ingresar):
    num = int(input("Ingrese un número: "))
    listaNumeros.append(num)


print(f"Antes del reposicionamiento: { listaNumeros }")

i = 1
j = 1
for _ in range(numeros_a_ingresar):
    listaNumeros.insert(j, listaNumeros[-i])
    i += 1
    j += 2


print(f'Después del reposicionamiento: { listaNumeros[0:10] }')
