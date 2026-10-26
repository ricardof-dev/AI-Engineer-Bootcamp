import csv

archivo = open("Semana_10/animales.csv", "r", newline="")
lector = csv.reader(archivo)

next(lector)
animales = list(lector)

archivo.close()

'''' hasa aqui lee y abre con 'r' '''

modificar = input("¿Qué animal quieres modificar? ")

encontrado = False
actualizado = False

for animal in animales:
    if animal[0] == modificar:
        encontrado = True
        print("Animal encontrado:", animal)

        opcion = input("¿Qué quieres modificar? (nombre/edad/especie/ciudad/vacunado): ")

        if opcion == "edad": 
            try:
                nuevo_valor = input("¿Cuál es la nueva edad? ")
                edad = int(nuevo_valor)
                
                if edad < 1 or edad> 120:
                    print("Edad no válida")
                else:
                    animal[1] = edad
                    actualizado = True

            except ValueError:
                print("No puedes utilizar letras o simbolos")
        
        elif opcion == "especie":
            nuevo_valor = input("¿Cuál es la nueva especie? ")
            animal[2] = nuevo_valor 
            actualizado = True
        elif opcion == "ciudad":
            nuevo_valor = input("¿Cuál es la nueva ciudad? ")
            animal[3] = nuevo_valor
            actualizado = True
        elif opcion == "vacunado":  
            nuevo_valor = input("¿Cuál es el nuevo valor?")
            if nuevo_valor == "True":
                animal[4] = True 
                actualizado = True
            elif nuevo_valor == "False":
                animal[4] = False
                actualizado = True
            else:
                print("Valor no válido")

        print(animal)

if not encontrado:
    print("Animal no encontrado")

if actualizado:
    archivo = open("Semana_10/animales.csv", "w", newline="")
    escritor = csv.writer(archivo)

    escritor.writerow(["nombre", "edad", "especie", "ciudad", "vacunado"])
    for animal in animales:
        escritor.writerow(animal)

    archivo.close()

''' print("💾 CSV guardado")'''