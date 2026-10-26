animales = ["Firulais", "Michi", "Luna"]

'''
FileNotFoundError

"Si el problema específicamente es que no encontramos el archivo, haz esto."

except FileNotFoundError:
    print("El archivo no existe")

---- ejemp  --- 
'''
try:
    archivo = open("perros.txt", "r")
except FileNotFoundError:
    print("El archivo no existe")
'''

-----
La idea es:

except:
        → cualquier error

except FileNotFoundError:
        → específicamente "no encontré el archivo"
'''

try:
    archivo = open("animales.txt", "r")
    contenido = archivo.read()
    archivo.close()

    print(contenido)

except FileNotFoundError:
    print("El archivo no existe")

print("Programa terminado")



try:
    archivo =open("perros.txt", "r") #creando el error ***
    contenido = archivo.read()
    archivo.close()
    print (contenido)

except FileNotFoundError:
    print ("El archivo no existe")

'''
Y aquí quiero hacer una pausa porque ya estás empezando a conectar varias piezas del puzzle:

open() → acceder al archivo
read() → obtener contenido
split() → convertirlo en lista
for → recorrer datos
index() → localizar
[] → modificar
"w" → persistir cambios
try/except → evitar que un problema tumbe el programa

Eso ya es un flujo de datos, no solamente comandos aislados.
'''









