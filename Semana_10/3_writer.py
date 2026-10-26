import csv

archivo = open("Semana_10/animales2.csv", "w") # W: sobreescribir ** ojo 

escritor = csv.writer(archivo)

escritor.writerow (["nombre", "edad", "especie", "ciudad", "vacunado"])
escritor.writerow (["Rocky", 7, "Perro", "Bogotá", True ])


archivo.close()

''' IMPORTANTE
"w" → reemplaza todo
"a" → agrega al final


'''