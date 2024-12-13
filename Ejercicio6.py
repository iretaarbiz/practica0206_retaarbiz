'''
Escribir un programa que permita gestionar la base de datos de alumnado de un classroom. Los alumnos y alumnas se guardarán en una lista que almacena un 
diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF, y el valor será otro diccionario con los datos del alumno/a 
(nombre, apellidos, teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado el módulo. 
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar. 
En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
Preguntar por el NIF del alumno/a y mostrar sus datos.
Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
Terminar el programa.
'''

diccionario = {}
terminar = True
while terminar == True:
    print("Ingresa el número correspondiente a la acción que quieres realizar:")
    print("(1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar")
    accion = input("")
    if accion == "1" or accion == "2" or accion == "3" or accion == "4" or accion == "5" or accion == "6":
        accion = int(accion)
        if accion == 1:
            print("Has accedido a la opción de 'Añadir alumno/a'")
            diccionarioalumnos = {}
            nif = input("Introduce el NIF del alumno: ")
            print("Introduce el nombre, apellidos, teléfono, correo y si esta aprobado o no el alumno.")
            nombre= input("Introduce el nombre: ")
            diccionarioalumnos["nombre"] = nombre
            apellidos = input("Introduce los apellidos: ")
            diccionarioalumnos["apellidos"] = apellidos
            telefono = input("Introduce el teléfono: ")
            diccionarioalumnos["teléfono"] = telefono
            correo = input("Introduce el correo: ")
            diccionarioalumnos["correo"] = correo
            aprobado = input("Introduce si esta aprobado o no (Si/No): ")
            if aprobado == "Si" or "si":
                aprobadobool = True
            elif aprobado == "No" or "no":
                aprobadobool = False
            diccionarioalumnos["aprobado"] = aprobadobool
            diccionario[nif] = diccionarioalumnos
        elif accion == 2:
            print("Has accedido a la opción de 'Eliminar alumno/a'")
            while True:
                if len(diccionario) == 0:
                    print("La base de datos esta vacia, prueba a usar la acción 'Añadir alumno/a' antes de usar las demas acciones")
                    print("Volviendo al menú principal \n")
                    break
                else:
                    nif = input("Introduce el NIF del alumno o 'salir' para volver al menú principal: ")
                    if nif in diccionario.keys():
                        del diccionario[nif]
                        print("El alumno con NIF", nif, "ha sido eliminado")
                        break
                    elif nif == "salir":
                        break
                    else:
                        print("El NIF introducido no está en nuestra base de datos")
        elif accion == 3:
            print("Has accedido a la opción de 'Mostrar alumno/a'")
            while True:
                if len(diccionario) == 0:
                    print("La base de datos esta vacia, prueba a usar la acción 'Añadir alumno/a' antes de usar las demas acciones")
                    print("Volviendo al menú principal \n")
                    break
                    nif = input("Introduce el NIF del alumno o 'salir' para volver al menú principal: ")
                    if nif in diccionario.keys():
                        print(diccionario[nif])
                        break
                    elif nif == "salir":
                        break
                    else:
                        print("El NIF introducido no está en nuestra base de datos")
        elif accion == 4:
            print("Has accedido a la opción de 'Listar todo el alumnado'")
            if len(diccionario) == 0:
                    print("La base de datos esta vacia, prueba a usar la acción 'Añadir alumno/a' antes de usar las demas acciones")
                    print("Volviendo al menú principal \n")
            for i in diccionario.keys():
                print(diccionario[i]['nombre'])
        elif accion == 5:
            print("Has accedido a la opción de 'Listar alumnado aprobado'")
            if len(diccionario) == 0:
                    print("La base de datos esta vacia, prueba a usar la acción 'Añadir alumno/a' antes de usar las demas acciones")
                    print("Volviendo al menú principal \n")
            for i in diccionario.keys():
                if diccionario[i]['aprobado'] == True:
                    print(diccionario[i]['nombre'])   
        elif accion == 6:
            print("¿Estás seguro de que quieres terminar la ejecución del programa? Todos los datos se borrarán (Si/No)")
            while True:
                acabar = input("")
                if acabar.lower() == "si":
                    print("El programa ha terminado")
                    terminar = False
                    break
                elif acabar.lower() == "no":
                    print("Volviendo al menú principal")
                    break
                else:
                    print("La palabra introducida es diferente a Si y No, vuelve a introducir la palabra")

    else:
        print("Porfavor introduce un número asociado a una función del programa \n")
