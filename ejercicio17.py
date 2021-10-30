"""
17.Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). 
Ejemplo: 
[("Rosa Perez", "40431888", "Liverpool"), ("Silvia Paredes", "40431855", "Buenos Aires"), ("Mariela Nina", "15151510", "Glasgow"), ("Luciana Hernandez", "75252520", "Lisboa")]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. 
Ejemplo: 
[("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")]

Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
a) Agregar pasajeros a la lista de viajeros.
b) Agregar ciudades a la lista de ciudades.
c) Dado el DNI de un pasajero, ver a qué ciudad viaja.
d) Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
e) Dado el DNI de un pasajero, ver a qué país viaja.
f) Dado un país, mostrar cuántos pasajeros viajan a ese país.
g) Salir del programa.
"""

nombre_dni_destino = [
    ("Rosa Perez", "40431888", "Liverpool"),
    ("Silvia Paredes", "40431855", "Buenos Aires"),
    ("Mariela Nina", "15151510", "Glasgow"),
    ("Luciana Hernandez", "75252520", "Lisboa")
]

ciudad_pais = [
    ("Buenos Aires", "Argentina"),
    ("Glasgow", "Escocia"),
    ("Lisboa", "Portugal"),
    ("Liverpool", "Inglaterra"),
    ("Madrid", "España")
]


while True:
    opcion = input("Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:\na) Agregar pasajeros a la lista de viajeros.\nb) Agregar ciudades a la lista de ciudades.\nc) Dado el DNI de un pasajero, ver a qué ciudad viaja.\nd) Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.\ne) Dado el DNI de un pasajero, ver a qué país viaja.\nf) Dado un país, mostrar cuántos pasajeros viajan a ese país.\ng) Salir del programa.\nElige => ")
    if opcion.lower() == 'a':
        nombre = input("ingrese su nombre: ")
        dni = input("ingrese su dni: ")
        destino = input("ingrese su destino: ")
        nombre_dni_destino.append((
            nombre, dni, destino
        ))
    if opcion.lower() == 'b':
        pais = input("ingrese su pais: ")
        ciudad = input("ingrese su ciudad: ")
        ciudad_pais.append((
            ciudad, pais
        ))
    if opcion.lower() == 'c':
        dni = input("ingrese su dni: ")

        for dni_user in nombre_dni_destino:
            if dni_user[1] == dni:
                print(f"Usted viaja a { dni_user[2] }")
        print('Su dni no esta en nuestra base de datos')

    if opcion.lower() == 'd':
        ciudad_a_buscar = input("ingrese el nombre de la ciudad: ")
        cantidad_de_ocurrencias = 0
        for ciudad in nombre_dni_destino:
            if ciudad_a_buscar == ciudad[2]:
                cantidad_de_ocurrencias += 1
        print(
            f'La cantidad de veces que se repite la ciudad es { cantidad_de_ocurrencias }')

    if opcion.lower() == 'e':
        dni = input("ingrese su dni: ")
        for dni_user in nombre_dni_destino:
            if dni == dni_user[1]:
                print(f"Usted viaja a: { dni_user[2] }")

    if opcion.lower() == 'f':
        ciudad_a_buscar = input("ingrese el nombre de la ciudad: ")
        cantidad_de_ocurrencias = 0
        for ciudad in nombre_dni_destino:
            if ciudad_a_buscar == ciudad[2]:
                cantidad_de_ocurrencias += 1
        print(
            f'La cantidad de veces que se repite la ciudad es { cantidad_de_ocurrencias }')
    if opcion.lower() == 'g':
        break
