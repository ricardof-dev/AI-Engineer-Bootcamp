animales = [
    {"nombre": "Michi", "edad": 3, "vacunado": True},
    {"nombre": "Firulais", "edad": 5, "vacunado": False},
    {"nombre": "Luna", "edad": 2, "vacunado": True}
]
def buscar_por_edad(dato, edad):
    encontrados = []
    for animal in dato:
        if animal["edad"] >= edad:
            encontrados.append(animal)        
    return encontrados

resultado = buscar_por_edad(animales, 3)
print(resultado)

resultado = buscar_por_edad(animales, 5)
print(resultado)

for animal in resultado:
    print(animal["nombre"])

resultado = buscar_por_edad(animales, 10)

if resultado:   #La clave que acabas de descubrir 🔑 if decide SI hay resultados. for recorre CUÁLES resultados hay.
    for animal in resultado:
        print(animal["nombre"])
else:
    print("No se encontraron animales") #ENCONTRAR EN VACIO DANDO UN RESLTADO 

if animal["vacunado"] == True:
    print("Sí")
else:
    print("No")
print(animal["nombre"], "tiene", animal["edad"], "años.")





''' 
print(resultado)
👉 muestra la variable completa, aunque esté vacía:
[]
---------------------------------------------------------
FOR busca un elemento
        ↓
No hay ninguno
        ↓
No entra al bloque
        ↓
No muestra nada


'''


'''
print() = mostrar /// print("Hola") 
---------------------------------------------------
return = devolver  /// def sumar(a, b):
                             return a + b
                        resultado = sumar(2, 3) /// mostraria 5 

        append() → va guardando animales en encontrados
return   → entrega encontrados
resultado → recibe lo que la función entregó                

'''