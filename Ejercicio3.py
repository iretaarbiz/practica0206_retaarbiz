'''Escribir un programa que guarde en un diccionario los precios de los artículos de la tabla, pregunte al usuario por un artículo, 
un número de unidades y muestre por pantalla el precio de esa cantidad de producto. Si el producto no está en el diccionario debe mostrar un mensaje informando de ello.

Producto    Precio
Pan         1.40
Huevo       2.30
Cebolla     0.85
Aceite      4.35 '''

diccionario = {'Pan':1.4, 'Huevo':2.3, 'Cebolla':0.85, 'Aceite':4.35}
producto = input("Introduce el árticulo que quieres comprar: \n")
productoformatodicc = producto[0].upper() + producto[1:len(producto)]
cantidad = int(input("Introduce la cantidad: "))
if productoformatodicc in diccionario:
    print("El valor de", cantidad, producto, "es", diccionario[productoformatodicc] * cantidad)
else:
    print("El producto no está en el diccionario")