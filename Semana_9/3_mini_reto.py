animales = ["Firulais", "Michi", "Luna"]

''' 
cambio y resscripcion de nombre .. apend agrega al final 
'''

archivo = open("animales.txt", "w")

posicion = animales.index("Michi")
animales[posicion] = "Toby"

for animal in animales:
    archivo.write(animal + "\n")

archivo.close()

########

''' archivo = open("animales.txt", "w")

posicion = animales.index("Toby")
animales[posicion] = "Rocky"

for animal in animales:
    archivo.write(animal + "\n")
archivo.close() '''

print(animales) 

####### LEER ##### 

archivo = open("animales.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)

