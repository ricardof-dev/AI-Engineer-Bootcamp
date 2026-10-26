import csv
archivo = open("Semana_10/animales.csv", "r")

lector = csv.DictReader (archivo)

for fila in lector: 
    if int(fila["edad"]) > 3 and fila["especie"] == "Perro" :
        print(fila["nombre"] , fila["edad"] )

archivo.close()

'''
Modo	Qué hace
"r"	📖 Leer
"w"	🧨 Escribir/reemplazar
"a"	➕ Agregar al final

'''