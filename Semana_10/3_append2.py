import csv

archivo = open("Semana_10/animales2.csv", "a")

escritor = csv.writer(archivo)

animales_nuevos = [
    ["Michi", 3, "Gato", "Bogotá", True],
    ["Luna", 2, "Perro", "Mosquera", False],
    ["Toby", 4, "Perro", "Bogotá", True]
]
for animal in animales_nuevos:
    if animal[2] == "Perro":
        escritor.writerow(animal)

archivo.close()

'''
animales[fila][columna]
*** para cambiar contenido dentro d elas listas **
'''
