animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]
'''
SALIDAS CON FOR SELECCIONANDO DATOS EN CONNO O CREANDO 
vARIABLES.
'''
for animal in animales:
    if animal["vacunado"] == True:
        print(animal["nombre"], "está vacunado")

for animal in animales:
    if animal["edad"] >= 3:
        print(animal["nombre"])

'''
no siempre se usa else
'''

for animal in animales:
    if animal["edad"] >= 3 and animal["vacunado"] == False :
        print(animal["nombre"], "tiene", animal["edad"], "años.")

for animal in animales:
    if animal["edad"] <= 3 or animal["vacunado"] == True :
        print(animal["nombre"])

for animal in animales:
    if animal["vacunado"] == True:
        print(animal["nombre"], "está vacunado")
    else :
        print(animal["nombre"], "no está vacunado.")

for animal in animales:
    if animal["edad"] >= 5:
        print("Adulto")
    elif animal["edad"] >= 3 :
        print("Joven")
    else :
        print("Pequeño")


for animal in animales:
    if animal["vacunado"] == True:
        estado = "Vacunado"
    elif animal["vacunado"] == False:
        estado = "No vacunado"
    if animal["edad"] >= 5:
        clasificacion = "Adulto" # crear variable en FOR ***
    elif animal["edad"] >= 3 :
        clasificacion = "Joven"
    else :
        clasificacion = "Pequeño"
    print(animal["nombre"],"|", animal["edad"],"años |", estado,"|", clasificacion)



    
'''
🧠 Resumen:

for animal in animales: → toma un diccionario completo
animal["nombre"] → toma un valor específico
animal.items() → permite recorrer clave + valor
----------------------------------------------------
animal              → diccionario completo
animal["nombre"]    → valor: "Michi"
"nombre"            → clave
-----------------------------------------------------
animal["edad"]
obtiene:
El valor asociado a la clave "edad" ✅
'''







