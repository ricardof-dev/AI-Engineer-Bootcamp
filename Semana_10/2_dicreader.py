
import csv
archivo = open("Semana_10/animales.csv", "r")

lector = csv.DictReader(archivo)

#cabecera = next(lector) --- DictReader usa automáticamente la primera fila del CSV como nombres de las columnas (claves).

####  ejem 1 --

#for fila in lector:
    ##print(fila)
    #print(fila["nombre"], fila["especie"] )

####  ejem 2 --

#for fila in lector:
    #if fila["especie"] == "Perro" and fila["vacunado"] == "False":
     #   print(fila["nombre"])

####  ejem 3 --

for fila in lector:
    if fila["especie"] == "Perro" and int(fila["edad"]) > 4:
        print(fila["nombre"])

archivo.close()

''' csv.DictReader()

csv.reader()
     ↓
fila[0]
fila[1]
fila[2]

⬇️

csv.DictReader()
     ↓
fila["nombre"]
fila["edad"]
fila["especie"]

'''