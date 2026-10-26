animales = [
    {"nombre": "Firulais", "edad": 5},
    {"nombre": "Michi", "edad": 3}
]

archivo = open("animales.txt", "w")

for animal in animales:
    archivo.write(animal + "\n")
    archivo.write(animal["nombre"] + "\n") #leyendo el diccionario directo 

archivo.close()

open("animales.txt", "r")
open("animales.txt", "w")

''' 
La lógica queda:
open("animales.txt", "r")  # leer
open("animales.txt", "w")  # escribir

"r" → read → leer 📖
"w" → write → escribir ✍️
----
open()  → abre el archivo
read()  → trae su contenido
contenido → queda como texto
--
Porque split("-") corta el texto cada vez que encuentra -.

"A-B-C".split("-")

-------
archivo = open("animales.txt", "r")
contenido = archivo.read()
animales = contenido.split("\n")
=
archivo → es el archivo abierto 📄
contenido → es texto (str) 📝
animales → es una lista (list) 📋
-----
write() → escribe texto
\n      → salto de línea
read()  → recupera texto
split() → convierte ese texto en partes/lista

-----

'''