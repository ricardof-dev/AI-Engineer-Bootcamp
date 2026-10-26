animales = [

    {"nombre": "Michi", "edad": 3, "vacunado": True},

    {"nombre": "Firulais", "edad": 5, "vacunado": False},

    {"nombre": "Luna", "edad": 2, "vacunado": True},

    {"nombre": "Loki", "edad": 6, "vacunado": False}

]

def animales_no_vacunados(animales):
    return [animal["nombre"] for animal in animales if not animal["vacunado"]]

print(animales_no_vacunados(animales))