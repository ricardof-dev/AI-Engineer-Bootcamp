
animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]

def filtrar_con_or(animales):
    return [animal["nombre"] for animal in animales if animal["edad"] >= 5 or animal["vacunado"] == True]
def reto(animales):
    return[animal["nombre"] for animal in animales if (animal["vacunado"] == True and animal["edad"] >= 3) or animal["edad"] >= 5]
def reto_dos(animales):
        return[animal['nombre'] for animal in animales if animal["vacunado"] == False or animal["edad"] < 3]
def reto_tres(animales):
        return[animal["nombre"] for animal in animales if (animal["vacunado"] == True and animal["edad"] < 5) or animal["edad"] ==5 ]


'''
Ejemplos del or y como hacen condicion y se pueden mezclar con el and 
'''

print (filtrar_con_or(animales))
print (reto(animales))
print (reto_dos(animales))
print (reto_tres(animales))


