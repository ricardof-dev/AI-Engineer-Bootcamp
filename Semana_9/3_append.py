
animales = ["Firulais", "", "Michi", "", "Luna"]



archivo = open("animales.txt", "a")

for animal in animales:
    archivo.write(animal + "\n")

archivo.close()


animales = ["Rocky", "Max"]

'''
"a" → agrega al final, no cambia lo que ya existe.
"w" → reescribe el archivo, reemplazando el contenido anterior.
'''

archivo = open("animales.txt", "w")

posicion = animales.index("Michi")
animales[posicion] = "Toby"

for animal in animales:
    archivo.write(animal + "\n")

archivo.close()



'''
animales.txt
     ↓
leer archivo
     ↓
convertir contenido → lista
     ↓
buscar "Michi"
     ↓
cambiar "Michi" → "Toby"
     ↓
abrir con "w"
     ↓
recorrer lista
     ↓
write()
     ↓
close()
'''
'''
Modificar en memoria:

animales[posicion] = "Toby"

Guardar en archivo:

archivo.write(animal + "\n")
'''
