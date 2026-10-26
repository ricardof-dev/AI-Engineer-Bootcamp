 
''' Se puede eliminar la lisa opr toma desde la memoria le resultado !!!! '''

archivo = open("Semana_9/animales.txt", "r")
contenido = archivo.read()
animales = contenido.strip().split("\n") #quita el esacio en la lista 
archivo.close()

animal_buscar = input("¿Qué animal quieres modificar? ")

try:
    posicion = animales.index(animal_buscar)

    nuevo_nombre = input("¿Cuál es el nuevo nombre? ")  # pregunta y cambia segun lista

    animales[posicion] = nuevo_nombre

    archivo = open("Semana_9/animales.txt", "w")

    for animal in animales:
        archivo.write(animal + "\n") # GUARDADO EN DISCO   IMPORTANTE !! NO OLVIDAR ESTA LINEA 

    archivo.close()

except ValueError:
    print("El animal no existe") # maneja el error y permite continuar el programa

print(animales)