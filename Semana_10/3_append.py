import csv

archivo = open("Semana_10/animales2.csv", "a")

escritor = csv.writer(archivo)


escritor.writerow (["Michi", 3, "Gato", "Bogotá", True])

archivo.close()

''' IMPORTANTE
"w" → reemplaza todo
"a" → agrega al final

'''