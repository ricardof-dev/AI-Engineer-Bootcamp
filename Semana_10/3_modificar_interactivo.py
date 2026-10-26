import csv

archivo = open("Semana_10/animales2.csv", "r", newline="")

lector = csv.reader(archivo)

animales = list(lector)

nombre_buscar = input("¿Qué animal quieres modificar? ")

for animal in animales:
    if animal and animal[0] == nombre_buscar:
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

        elif opcion == "especie":
            nuevo_valor = input("¿Cuál es la nueva especie? ")
            animal[2] = nuevo_valor #se usa STR

        elif opcion == "ciudad":
            nuevo_valor = input("¿Cuál es la nueva ciudad? ")
            animal[3] = nuevo_valor
                   
            print(animal)

            
        
archivo.close()