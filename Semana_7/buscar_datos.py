animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]

def buscar_animal(animales): #BUSQUEDA ESPECIFICA
    return [animal["nombre"] for animal in animales if animal["nombre"] == "Firulais"]
print (buscar_animal(animales))

def buscar_animal(animales, nombre):  #BUSQUEDA POR NOMBRE EN PRINT
    return [animal["nombre"] for animal in animales if animal["nombre"] == nombre]
print (buscar_animal(animales, "Michi"))
print (buscar_animal(animales, "Luna"))

'''
nombre es un parámetro, así que puedes cambiarlo cada vez que llamas la función:
buscar_animal(animales, "Michi")
buscar_animal(animales, "Luna")
buscar_animal(animales, "Firulais")
💡 La función ya no tiene un dato fijo: recibe el dato que necesita. dato fijo → parámetro → función reutilizable 🚀
'''
def buscar_animal_completo(animales, nombre): #BUSQUEDA COMPLETA ESPECIFICA  X NOMBRE
    return [animal for animal in animales if animal["nombre"] == nombre]
print (buscar_animal_completo(animales, "Firulais"))

def buscar_por_edad(animales, edad):  #BUSQUEDA COMPLETA ESPECIFICA  X  EDAD
    return [animal for animal in animales if animal["edad"] == edad]
print(buscar_por_edad(animales, 3))

def obtener_un_animal(animales, nombre): #BUSQUEDA COMPLETA ESPECIFICA  con FOR Y RETURN  SIN [].
    for animal in animales:
        if animal["nombre"] == nombre:
            return (animal)
print(obtener_un_animal(animales, "Luna"))
'''Aquí ya diferencias:

for → recorrer animales uno por uno.
if → comprobar la condición.
return animal → devolver el diccionario completo.
comprensión de listas → cuando quieres construir una lista rápidamente.

Eso de mezclar for, return y las comprensiones es parte del proceso. No estás perdido; estás conectando piezas.
'''




