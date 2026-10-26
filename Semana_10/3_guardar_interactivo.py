import csv

archivo = open("Semana_10/animales2.csv", "r", newline="")

lector = csv.reader(archivo)

animales = list(lector)

nombre_buscar = input("¿Qué animal quieres modificar? ")

encontrado = False

for animal in animales:
    if animal and animal[0] == nombre_buscar:
        encontrado = True
        print(animal)

        opcion = input("¿Qué quieres modificar? (edad/especie/ciudad/vacunado): ")
            
        if opcion == "vacunado": # primera para modificar 
            nuevo_valor = input("¿Cuál es el nuevo valor? ")


            if nuevo_valor == "True":
                animal[4] = True #se usa BOOL y lo tranforma 


            elif nuevo_valor == "False":
                animal[4] = False


        elif opcion == "edad": #segunda para modificar
            nuevo_valor = input("¿Cuál es la nueva edad? ")
            animal[1] = int(nuevo_valor) #se usa INT
            print(animal)

        elif opcion == "especie":
            nuevo_valor = input("¿Cuál es la nueva especie? ")
            animal[2] = nuevo_valor #se usa STR
            print(animal)

        elif opcion == "ciudad":
            nuevo_valor = input("¿Cuál es la nueva ciudad? ")
            animal[3] = nuevo_valor
            print(animal)      
        

if not encontrado:
        print("Animal no encontrado")

archivo.close()

if encontrado == True:
    archivo = open("Semana_10/animales2.csv", "w", newline="")

    escritor = csv.writer(archivo)

    for animal in animales:
        escritor.writerow(animal)

    

archivo.close()

'''
archivo = open("Semana_10/animales2.csv", "w", newline="") # abre el archivo para escribir/reemplazar su contenido en el disco.

escritor = csv.writer(archivo)

for animal in animales:
    escritor.writerow(animal)

archivo.close()
'''