"""
2. Leer 5 números, guardarlos en una lista y mostrarlos en el orden inverso al introducido.
"""

nums = []
for i in range(5):
    num = int(input("ingrese un número: "))
    nums.append(num)

print('************')
nums.reverse()
for num in nums:
    print(num)
