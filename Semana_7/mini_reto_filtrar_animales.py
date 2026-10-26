animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True},
    {"nombre": "Loki", "edad": 6, "vacunado": False}
]

for animal in animales:
    if not animal["vacunado"] and animal['edad'] >=3: 
        print(animal["nombre"], animal["edad"]) 

resultado = [
    animal["nombre"]
    for animal in animales
    if not animal["vacunado"] and animal["edad"] >= 3]
print(resultado)

resultado2 = [
    animal ['nombre'] for animal in animales if animal['vacunado']]
print(resultado2)




