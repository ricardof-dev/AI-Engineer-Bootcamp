'''

def mostrar_animales(lista):
lista es un parámetro. Es como una variable temporal que recibirá la lista que le pasemos.
-----
PARÁMETRO = nombre que recibe el dato dentro de la función
---
mostrar_animales(animales)

👉 animales = argumento que le estamos pasando

'''

animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]

def nombre_edad(lista_animales):
    for animal in lista_animales:
        print(animal["nombre"], "tiene", animal["edad"], "años.")

nombre_edad (animales)

def buscar_por_edad(dato, edad): # 2/2 VARIABLES Q SE TOMAN D ELA LISTA 
    for animal in dato:
        if animal["edad"] >= edad:
            print(animal["nombre"])


buscar_por_edad(animales, 3) #CAMBIA EL PARAMETRO EN LA VARIABLE DE ARRIBA 1/2 
buscar_por_edad(animales, 5)
buscar_por_edad(animales, 2)

def mostrar_vacunados(dato, vacunado):
    for animal in dato:
        if animal["vacunado"] == vacunado:
            print(animal["nombre"])

mostrar_vacunados(animales, True)
mostrar_vacunados(animales, False)

''' 
Con una sola función puedes buscar ambos grupos:

True  → vacunados
False → no vacunados
'''

''' -------------- dos condiciones + parámetros ---------- 
AND → las dos condiciones deben cumplirse
OR  → mínimo una condición debe cumplirse
'''

def filtrar_animales (dato,edad, vacunado): 
    for animal in dato: 
        if animal["edad"] >= edad and animal ['vacunado'] == vacunado: 
            print(animal["nombre"]) 

filtrar_animales(animales, 3, True)
filtrar_animales(animales, 2, False)
