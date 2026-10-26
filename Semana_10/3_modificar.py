import csv

archivo = open("Semana_10/animales2.csv", "r",newline="")

lector = csv.reader(archivo)

animales = list(lector)

encontrado = False

for animal in animales:
    if animal[0] == "Luna" and animal[4] == "False":
        animal[4] = True

'''
for animal in animales:
    if animal and animal[0] == "Michi":
        animal[0] = "Toby"
        encontrado = True

if not encontrado:
    print("Michi no fue encontrado") #condicion si es False y no encuentra
 '''      
archivo.close()

archivo = open("Semana_10/animales2.csv", "w", newline="") ### newline="" le dice a Python:"CSV, encárgate tú de los saltos de línea."

escritor = csv.writer(archivo)


for animal in animales:
    if animal: ### evitar escribir las filas vacías [] que ya habían sido leídas.
        escritor.writerow(animal)

    '''if animal: dio False → no la escribió.'''

archivo.close()

print(animales)











