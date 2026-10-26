animales = [
    {
        "nombre": "Michi",
        "edad": 3,
        "vacunado": True
    },
    {
        "nombre": "Firulais",
        "edad": 5,
        "vacunado": False
    },
    {
        "nombre": "Luna",
        "edad": 2,
        "vacunado": True
    }
]
'''
animales (lista)
├── diccionario → Michi
├── diccionario → Firulais
└── diccionario → Luna
'''
print(animales)
for animal in animales: #imprime en orden
    print(animal)
for animal in animales:
    print(animal["nombre"])  #La clave es nombre 
for animal in animales:
    print(animal["edad"])
for animal in animales:
    print(animal["vacunado"])

for animal in animales: #combinando
    print(animal["nombre"],", tiene", animal["edad"], "años.") 

for animal in animales:
    if animal["vacunado"]:  #bool - true 
        print(animal["nombre"])

for animal in animales:
    if not animal["vacunado"]: #bool -  false IF NOT***
        print(animal["nombre"]) 

    