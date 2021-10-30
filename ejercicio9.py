"""
9. Leer 5 números enteros que se introducirán ordenados de forma creciente (si no los ingresa en forma creciente deberá solicitar nuevamente el ingreso de números). Posteriormente ingresar un número N, e insertarlo en el lugar adecuado para que la tabla continúe ordenada (repetir hasta que se ingrese 
el número 0 o un negativo). Ejemplo
Ingresar números:
        1, 2, 4, 3 (volver a ingresar), 5, 10
    Lista: [1, 2, 4, 5, 10]
    N = 7
    Lista resultante: [1, 2, 4, 5, 7, 10]
"""


# numbers = []
# for i in range(5):
#     num = int(input("ingrese un número: "))
#     numbers.append(num)

# copyNumbers = numbers.copy()

# copyNumbers.sort()
# while True:

#     if numbers == copyNumbers:
#         print('---------------')
#         print("correcto, están ordenados")
#         break
#     else:
#         print(f'No están ordenados, ingrese los números nuevamente :)')
#         numbers.clear()
#         for i in range(5):
#             num = int(input("ingrese un número: "))
#         numbers.append(num)


while True:
    numbers = []

    for i in range(5):
        num = int(input("ingrese un número: "))
        numbers.append(num)

    copyNumbers = numbers.copy()
    copyNumbers.sort()
    if numbers != copyNumbers:
        print(f'No están ordenados, ingrese los números nuevamente :)')
        numbers.clear()
        for i in range(5):
            num = int(input("ingrese un número: "))
            numbers.append(num)
        copyNumbers = numbers.copy()
        copyNumbers.sort()
    else:
        break

print('---------------')
print("correcto, están ordenados")
# lack
