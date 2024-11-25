'''Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés 
separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, hasta que el usuario introduzca la palabra “terminar”. 
El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario 
para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.'''

diccionario = {}
n = True
while n == True:
    palabra = input("Introduce la palabra: ")
    if palabra == "terminar":
        break
    traduccion = input("Introduce la traducción: ")
    diccionario[palabra] = traduccion
frasetraducida = ""
frase = input("Introduce una frase en español: \n")
for i in frase.split():
    if i in diccionario.keys():
        frasetraducida += diccionario[i] + " "
    else:
        frasetraducida += i + " "
print(frasetraducida)
