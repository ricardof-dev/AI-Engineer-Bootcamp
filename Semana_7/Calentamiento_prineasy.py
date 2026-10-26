animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]
def obtener_nombres(animales):
    return [animal["nombre"] for animal in animales]
def obtener_por_edad(animales, edad_minima): #escoger por edad segun la orden 
    return [animal["nombre"] for animal in animales if animal["edad"]>=5]
def obtener_por_edad_dos(animales, edad_minima):
    return [animal["nombre"] for animal in animales if animal["edad"]<=3]
def obtener_por_edad_tres(animales, edad_minima):
    return [animal["nombre"] for animal in animales if animal["edad"] >= edad_minima] #forma mas facil escogiendo ene el print 1/2 
def obtener_por_vacunado(animales, estado):
    return [animal["nombre"] for animal in animales if animal["vacunado"]== estado] #BOOL estado 
def filtrar_animales(animales, edad_minima, estado):
    return [animal["nombre"] for animal in animales if animal["edad"] >= edad_minima and animal["vacunado"]== estado ] #clasificacion de 2 

print(obtener_nombres(animales))
print(obtener_por_edad(animales,obtener_por_edad))
print(obtener_por_edad_dos(animales,obtener_por_edad))
print(obtener_por_edad_tres(animales, 2)) # 2/2  Eso es hacer una función reutilizable.
print(obtener_por_edad_tres(animales, 5))  # 2/2  Eso es hacer una función reutilizable.
print(obtener_por_vacunado(animales,True)) #BOOL estado  llamado
print(obtener_por_vacunado(animales, False)) #BOOL estado  llamado 2 
print(filtrar_animales(animales,3,True)) #parámetros + diccionarios + listas + comprensión de listas + and.
 






'''
animal["nombre"]     # ← lo que guardamos
for animal           # ← cada animal
in animales          # ← recorremos la lista

Por cada animal dentro de animales, guarda su "nombre" en una nueva lista.

'''