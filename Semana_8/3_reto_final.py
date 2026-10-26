animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]

''' función que recibe 3 parámetros y con AND
 '''

def buscar_animales(lista_animales, edad_minima, vacunado):

    encontrados = []

    for animal in lista_animales:
        if animal["edad"] >= edad_minima and animal["vacunado"] == vacunado:
            encontrados.append(animal)

    return encontrados

resultado_1 = buscar_animales(animales, 3, True)
resultado_2 = buscar_animales(animales, 5, True)
'''se pregunta una vez en base a la variable  de q quieres respuesta '''
if resultado_2:
    for animal in resultado_2:
        print(animal["nombre"])
else:
    print("No se encontraron animales")

if resultado_1:
    for animal in resultado_1:
        print(animal["nombre"])
else:
    print("No se encontraron animales")

'''-- con OR ---'''

def buscar_con_or(lista_animales, edad_minima, vacunado):
    encontrados = []

    for animal in lista_animales:
        if animal["edad"] >= edad_minima or animal["vacunado"] == vacunado:
            encontrados.append(animal)

    return encontrados

resultado_con_or = buscar_con_or(animales, 5, True)

if resultado_con_or:
    for animal in resultado_con_or:
        print(animal["nombre"])
else:
    print("No se encontraron animales")
