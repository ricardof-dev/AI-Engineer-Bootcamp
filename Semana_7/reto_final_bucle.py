'''animal = {
    "nombre": "Michi",
    "edad": 3,
    "vacunado": True
}
for clave, values in animal.items():
    print(clave, ":", values)
'''
''' en bucle mostrando listas separadas 
'''
animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]

for animal in animales: 
    print("---", animal["nombre"], "---") #con titulo antes del 1 FOR y recorre en orden
    for clave, valor in animal.items(): # Segundo FOR 
        print(clave, ":", valor)
    if animal["vacunado"] == True:
        print("Está vacunado")
    else : 
        print ('no vacunado')


'''Una vez tiene un animal, mira todo lo que hay dentro de ese diccionario.

Es como:

LISTA DE ANIMALES
      ↓
   🐱 Michi
      ↓
 nombre - edad - vacunado

   🐶 Firulais
      ↓
 nombre - edad - vacunado

🔥 Esto se llama un for anidado: un bucle dentro de otro.

---

El primer for toma un animal.
El segundo for revisa todo lo que tiene ese animal.
Cuando termina el segundo for, hacemos el espacio.
El primer for pasa al siguiente animal. 🐱➡️🐶➡️🐱

'''
