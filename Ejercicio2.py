'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>”. '''

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu número de teléfono: ")
diccionario = {'Nombre':nombre, 'Edad':edad, 'Direccion':direccion, 'Telefono':telefono}
print(diccionario['Nombre'], "tiene", diccionario['Edad'], "años, vive en", diccionario['Direccion'], "y su número de teléfono es", diccionario['Telefono'])