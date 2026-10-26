animales = [
    {"nombre": "Firulais", "edad": 5, "vacunado": True},
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Luna", "edad": 2, "vacunado": False}
]
def buscar_animales(lista_animales, edad_minima, vacunado):

    encontrados = []

    for animal in lista_animales:
        if animal["edad"] >= edad_minima and animal["vacunado"] == vacunado:
            encontrados.append(animal)

    return encontrados

resultado1 = buscar_animales (animales, 4 , True)
resultado2 = buscar_animales(animales, 2, False)
'''---------------------------------------'''
if resultado2:
        for animal in resultado2:
            print(animal["nombre"])
else:
    print("No se encontraron animales")
'''--------------------------------'''
if resultado1:
        for animal in resultado1:
            print(animal["nombre"])
else:
    print("No se encontraron animales")

'''---------------------------'''
print("Cantidad encontrada:", len(resultado2))

if len(resultado2) ==0:
    print("No se encontraron animales")

elif len(resultado2) == 1: # eemlo ar aprintiar algo dif
    for animal in resultado2:
        print("Nombre:", animal["nombre"])
else:
    print("Se encontraron varios animales")
'''
if resultado2:  #Recorrer los animales encontrados y mostrar el nombre de cada uno.
    for animal in resultado2:
        print(animal["nombre"])

'''



''' =    → asignar un valor
    ==   → comparar si es igual
'''