import csv

archivo = open("Semana_10/animales.csv", "r")

lector = csv.reader(archivo) ## csv.reader() ya hace esa separación por nosotros:

cabecera = next(lector) # quita la cabecera de la lista 1/2 **

for fila in lector:
    #print(fila)  #1/1
#for fila in lector: 2/2
#   print(fila[2])

    if fila [2] == "Perro" and fila[4] == "False":
       print(fila[0])


archivo.close()
    
''' IMPORTANTE ** 


Con nuestro método anterior necesitábamos:

contenido = archivo.read()
animales = contenido.split("\n")

for animal in animales:
    datos = animal.split(",")

Con csv.reader() ya no necesitamos hacer esos split() manualmente.

Podemos llegar directamente a:

for fila in lector:

Y cada fila será una lista.

Por ejemplo:

["Firulais", "5", "Perro", "Bogotá", "True"]

🔥 Es decir, Python ya hizo por nosotros la separación de las columnas.

'''

