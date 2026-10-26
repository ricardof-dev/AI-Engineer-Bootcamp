animales = ["Firulais", "Michi", "Luna"]

archivo = open("animales.txt", "w")

for animal in animales:
    archivo.write(animal + "\n") # Se co viere en lista

archivo.close()

######

archivo = open("animales.txt", "r") #devuelve el string 
contenido = archivo.read()
animales = contenido.split("\n") #conviere en lista el string

archivo.close()

######

for animal in animales:
    print(animal)

for animal in animales:
    animal = animal.strip() #quita el espacio final 

    if animal:
        print(animal)

######

animales = ["Firulais", "Michi", "Luna"]  # mira en  osicion esa desde 0 
posicion = animales.index("Michi")
print(posicion)

######

archivo = open("animales.txt", "w")

posicion = animales.index("Michi") #CAMBIO EN MEMORIA
animales[posicion] = "Rocky"

for animal in animales:
    archivo.write(animal + "\n") #rGUARDADO EN DISCO   IMPORTANTE 

archivo.close()

print(animales)

######
archivo = open("animales.txt", "r")
contenido = archivo.read()
animales = contenido.strip().split("\n") #quita el esacio en la lista 
archivo.close()

animal_buscar = input("¿Qué animal quieres modificar? ")  # pregunta y cambia segun lista
try:
    posicion = animales.index(animal_buscar)
    nuevo_nombre = input("¿Cuál es el nuevo nombre? ")
    animales[posicion] = nuevo_nombre

    archivo = open("animales.txt", "w")

    for animal in animales:
        archivo.write(animal + "\n") # GUARDADO EN DISCO   IMPORTANTE !! NO OLVIDAR ESTA LINEA 

    archivo.close()

except ValueError: # maneja el error y permite continuar el programa
    print("El animal no existe")


print(animales)


