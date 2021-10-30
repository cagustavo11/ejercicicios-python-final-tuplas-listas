"""
20. Escribir un programa que permita gestionar la “base de datos” de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su DNI, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
• Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
• Preguntar por el DNI del cliente y eliminar sus datos de la base de datos.
• Preguntar por el DNI del cliente y mostrar sus datos.
• Mostrar lista de todos los clientes de la base datos con su DNI y
nombre.
• Mostrar la lista de clientes preferentes de la base de datos con su DNI
y nombre.
• Terminar el programa.
"""

users = {}


while True:
    opcion = int(input("Ingrese una opcion: \n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige => "))

    if opcion == 1:
        dni = input("ingrese su clave(DNI): ")
        nombre = input("ingrese su nombre: ")
        direccion = input("ingrese su direccion: ")
        telefono = input("ingrese su telefono: ")
        correo = input("ingrese su correo: ")
        preferente = input("ingrese su preferente(si o no): ")

        if preferente.lower() == 'no':
            preferente = False
        else:
            preferente = True

        users.update({dni: {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'preferente': preferente,
        }})

    if opcion == 2:
        dni = input("ingrese su clave(DNI): ")
        del users[dni]
    if opcion == 3:
        dni = input("ingrese su clave(DNI): ")
        for key in users[dni]:
            print(users[dni][key])
    if opcion == 4:
        for dni in users:
            print(f'El dni es: { dni }')
            print(f"Su nombre es: { users[dni]['nombre'] }")
            print('**********')
    if opcion == 5:
        for dni in users:
            if users[dni]['preferente'] == True:
                print(f'El dni es: { dni }')
                print(f"Su nombre es: { users[dni]['nombre'] }")
                print('**********')
    if opcion == 6:
        break
