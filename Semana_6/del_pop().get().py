animal = {
    "nombre": "Gato",
    "edad": 13,
    "especie": "Persa",
    "color": "Blanco",
    "peso": 4.5
}

del animal["color"] #elimina clave +valor
print(animal)

animal["color"] = "Blanco" #variable par aagregar 
color_eliminado = animal.pop("color") #elimina valor y vuelve
print(color_eliminado)



'''clave = input("¿Qué dato quieres eliminar? ")  ### mini reto 1 , borrar el q se elija
eliminado = animal.pop (clave)
print(f"Eliminé {clave}: {eliminado}")
'''
   
clave = input("¿Qué dato quieres eliminar? ")  ### mini reto 2 , borrar el q se elija y mostrar mensaje si no existe
if clave in animal:
        eliminado = animal.pop (clave)
        print(f"Eliminé {clave}: {eliminado}")
else :
    print(f"No existe.")

print(animal.get("edad")) #.GET CONSULTA una cLAVE SIN KEYERROR
print(animal.get("altura")) #Muestra none valor por defecto 
print(animal.get("edad", "No existe")) #igual pero en este caso muere porq si hay valor 
print(animal.get("altura", "No existe")) #muetsra si no esta inmediatamente , ahorrase muchos if,else 

import json
      

