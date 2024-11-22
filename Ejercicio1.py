'''Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce la divisa de la que quieres obtener el símbolo: ")
divisamayus = divisa[0].upper() + divisa[1:len(divisa)]
print(divisa)
if divisamayus in diccionario:
    print("El símbolo de la divisa",divisa, "es", diccionario[divisamayus])
else:
    print("La divisa no está en el diccionario")