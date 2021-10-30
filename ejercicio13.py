"""
13.Queremos desarrollar una aplicación que nos ayude a gestionar las notas de un centro educativo. Se tiene un grupo compuesto por 5 Estudiantes, almacenar la información en una tupla: Apellidos, Nombres y código. 

Tupla = ( (“Luque”, “Rene”, “41411919”), …. <completar>… )

Se pide leer las notas del primera y segunda unidad de los cinco Estudiantes,
y almacenar en una lista:
Lista = [ [“41411919”, 15, 12] , …<completar> … ]

Calcular el promedio del curso: 

Lista = [ [“41411919”, 15, 12, 13.5] , …<completar> … ]

Al final implementar líneas de código, que solicite un código y muestra los 
nombres y apellidos, y la nota promedio (redondear). Ejemplo

Ingrese un Código: 41411919
Alumno: Rene Luque
Nota Promedio: 14
"""


def calcularPromedio(totalDatos, sumaDatos):

    promedio = sumaDatos / totalDatos
    return promedio


listaTupla = [("Luque", "Rene", "41411919")]

for i in range(5):
    nombre = input("ingrese el nombre: ")
    apellido = input("ingrese el apellido: ")
    codigo = input("ingrese el código: ")
    print('****************')
    listaTupla.append((nombre, apellido, codigo))

listaNotas = [["41411919", 15, 12]]

for i in range(5):
    codigo = input("ingrese su código: ")
    notaUnidad1 = int(input("ingrese la nota dela unidad 1: "))
    notaUnidad2 = int(input("ingrese la nota dela unidad 2: "))
    print('****************')
    listaNotas.append([codigo, notaUnidad1, notaUnidad2])


i = 0
sumarNotas1 = 0


for i in range(len(listaNotas)):
    sumarNotas1 = 0
    for j in range(1, 3):
        sumarNotas1 += listaNotas[i][j]
        # print(sumarNotas1)
    promedioNota = calcularPromedio(2, sumarNotas1)
    listaNotas[i].append(promedioNota)
# print(f'El promedio es: { listaNotas }')


codigo = input("Ingrese su codigo: ")

for el in listaTupla:
    if el[2] == codigo:
        print(f"Alumno: {el[0]} { el[1]}")
        break


for el in listaNotas:
    if el[0] == codigo:
        print(f'Nota promedio: { round(el[3], 0) }')
        break
