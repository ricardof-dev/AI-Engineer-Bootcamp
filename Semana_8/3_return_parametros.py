animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]

def buscar_vacunados(lista_animales): 
    encontrados = []

    for animal in lista_animales:
        if animal["vacunado"]:
            encontrados.append(animal)

    return encontrados


resultado = buscar_vacunados(animales)

if resultado:
    for animal in resultado:
        print(animal["nombre"])
else:
    print("No se encontraron animales")

def buscar_por_edad(lista_animales, edad_minima):

    encontrados = []

    for animal in lista_animales:
        if animal["edad"] >= edad_minima:
            encontrados.append(animal)

    return encontrados


resultado = buscar_por_edad(animales, 6)


if resultado:
    for animal in resultado:
        print(animal["nombre"])
else:
    print("No se encontraron animales")

def buscar_por_vacunacion(lista_animales, vacunado):

    vacunados = []

    for animal in lista_animales:
        if animal["vacunado"] == vacunado:
            vacunados.append(animal)

    return vacunados

resultado = buscar_por_vacunacion(animales, False)

if resultado:
    for animal in resultado:
        print(animal["nombre"])
else:
    print("No se encontraron animales")







''' BSCANDO VACNADOS O NO VACNADOS '''
''' BSCANDO edaded ESECIFICAS '''


















'''
[]     → existe una lista, pero está vacía
None   → no hay un valor útil asignado/devuelto
'''
    
    
    















    
    