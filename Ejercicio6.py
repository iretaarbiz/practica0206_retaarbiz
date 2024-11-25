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
    print("Ingresa el número correspondiente a la acción que quieres realizar: \n")
    print("(1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar")
    accion = int(input(""))
    if accion == 1:
        diccionarioalumnos = {}
        nif = input("Introduce el NIF del alumno: ")
        print("Introduce el nombre, apellidos, teléfono, correo y si esta aprobado o no el alumno.")
        for i in range(5):
            if i == 0:
                nombre= input("Introduce el nombre: ")
                diccionarioalumnos["nombre"] = nombre
            elif i == 1:
                apellidos = input("Introduce los apellidos: ")
                diccionarioalumnos["apellidos"] = apellidos
            elif i == 2:
                telefono = input("Introduce el teléfono: ")
                diccionarioalumnos["teléfono"] = telefono
            elif i == 3:
                correo = input("Introduce el correo: ")
                diccionarioalumnos["correo"] = correo
            else:
                aprobado = input("Introduce si esta aprobado o no (Si/No): ")
                if diccionarioalumnos[aprobado] == "Si" or "si":
                    aprobadobool = True
                elif diccionarioalumnos[aprobado] == "No" or "no":
                    aprobadobool = False
                diccionarioalumnos["aprobado"] = aprobadobool
        diccionario[nif] = diccionarioalumnos
    elif accion == 2:
        nif = input("Introduce el NIF del alumno: ")
        del diccionario[nif]
        print("El alumno con NIF", nif, "ha sido eliminado")
    elif accion == 3:
        nif = input("Introduce el NIF del alumno: ")
        print(diccionario[nif])
    elif accion == 4:
        for i in diccionario.keys():
            print(diccionario[i]['nombre'])
    elif accion == 5:
        for i in diccionario.keys():
            if diccionario[i]['aprobado'] == True:
                print(diccionario[i]['nombre'])   
    elif accion == 6:
        terminar = False
