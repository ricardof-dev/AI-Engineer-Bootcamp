

animales = ["Firulais", "", "Michi", "", "Luna"]



archivo = open("animales.txt", "r")
contenido = archivo.read()
archivo.close()
print(contenido)

animales = contenido.split("\n")

for animal in animales:
    if animal:
        print(animal)
        
'''
split("\n")

Aquí NO quita espacios.

Lo que hace es:

✂️ Separar el texto en elementos usando cada salto de línea.
-----------------
🔥 Así que el concepto importante queda:

split() → SEPARA
strip() → LIMPIA
if      → FILTRA
'''