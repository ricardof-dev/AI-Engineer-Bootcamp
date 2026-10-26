'''animales = [
    ["Michi", "3", "Gato", "Bogotá", "True"],
    ["Firulais", "5", "Perro", "Medellín", "False"]
]'''
'''' se pone lo que viene par ave ry modificar y no guardar'''
import csv

archivo = open("Semana_10/animales.csv", "r", newline="")
lector = csv.reader(archivo)

next(lector)
animales = list(lector)

archivo.close()

'''------------'''

nombre_buscar = input("¿Qué animal buscas? ")

encontrado = False

for animal in animales:
    if animal[0] == nombre_buscar:
        encontrado = True
        print("Animal encontrado:", animal)

        valido = False

        while not valido:

            try:
                nuevo_valor = input("Nueva edad: ")
                edad = int(nuevo_valor)

                if edad < 1 or edad > 120:
                    print("Edad no válida")
                else:
                    animal[1] = edad
                    valido = True
                    print( animal)       

            except ValueError:
                print("Edad no válida")

if not encontrado:
    print("Animal no encontrado")

''' Se pone lo q viene para sobre escribir '''

archivo = open("Semana_10/animales.csv", "w", newline="")
escritor = csv.writer(archivo)

escritor.writerow(["nombre", "edad", "especie", "ciudad", "vacunado"])

for animal in animales:
    escritor.writerow(animal)

archivo.close()


