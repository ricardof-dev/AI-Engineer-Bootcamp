productos = ["Arroz", "Carne", "Yuca", "Ensalada", "Tomate"]
 
#len(lista)   → cantidad de elementos
#len(texto)   → cantidad de caracteres
len(productos)
print(f"Tenemos {len(productos)} en stock.")

productos.append("Leche") #agrega***
print(f"Tenemos {len(productos)} en stock.")

productos[len(productos) - 1]
print(f"Tenemos {len(productos)} en stock.")

for lista in range (len(productos)):
    print(f"{lista} ) {productos[lista]}") #inicia en 0  / Es necesario en este caso porque nosotros mostramos al usuario una numeración desde 1, mientras que Python usa índices desde 0.

for indice in range (len(productos)):
    print(f"Producto {indice + 1} : {productos[indice]}")  # para  no inicie en 0

eleccion = int (input("¿Qué producto quieres? "))
print(productos[eleccion - 1]) #seleccionar produc3to especifico en lista //// siempre -1 para q quite el incio en 0.



