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

resultado = buscar_animales(animales, 3, True)

print("Cantidad encontrada:", len(resultado))
if len(resultado) == 0:
    print("No se encontraron animales")
elif len(resultado) == 1:
    print("Se encontró exactamente un animal")
else:
    print("Se encontraron varios animales")