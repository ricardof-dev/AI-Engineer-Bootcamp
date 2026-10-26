class Animal:
    def __init__(self, nombre, edad, especie, ciudad, vacunado):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.ciudad = ciudad
        self.vacunado = vacunado

    def cambiar_edad(self, nueva_edad):
        if 1 <= nueva_edad <= 120:
            self.edad = nueva_edad
            return "Edad actualizada"
        else:
            return "Edad no válida"
    def vacunar(self):  
        if self.vacunado : 
            print("Ya está vacunado")
        else: # false
            print("No estaba vacunado") 
            self.vacunado = True 
            print("Ahora está vacunado")
    def mostrar_info(self): 
        print(self.nombre)
        print(self.edad)
        print(self.especie)
        print(self.ciudad)
        print(self.vacunado)

def buscar_animal(animales, nombre):
        for animal in animales:
            if animal.nombre.strip().lower() == nombre.strip().lower():
                return animal

        return None

def buscar_vacunados(animales):
    encontrados = []

    for animal in animales:
        if animal.vacunado:
           encontrados.append(animal)

    return encontrados

def buscar_por_especie(animales, especie):
    encontrados = []

    for animal in animales:
        if animal.especie.lower() == especie.lower():
            encontrados.append(animal)

    return encontrados

def buscar_perros_vacunados(animales):
    encontrados = []

    for animal in animales:
        if animal.especie.lower() == "perro" and animal.vacunado:
            encontrados.append(animal)

    return encontrados

def buscar_mayores(animales, edad_minima):
    encontrados = []

    for animal in animales:
        if animal.edad >= edad_minima:
            encontrados.append(animal)

    return encontrados

def buscar_perros_mayores(animales, edad_minima):
    encontrados = []

    for animal in animales:
        if animal.especie.lower() == "perro" and animal.edad >= edad_minima and animal.vacunado:
            encontrados.append(animal)

    return encontrados

def buscar_por_ciudad(animales, ciudad):
    encontrados = []

    for animal in animales:
        if animal.ciudad.strip().lower() == ciudad.strip().lower(): #espacios y mayusculas par ala busquedad strip lower
            encontrados.append(animal)

    return encontrados

def buscar_por_ciudad_y_vacunados (animales, ciudad):
    encontrados = [] 
 
    for animal in animales:
        if animal.ciudad.strip().lower() == ciudad.strip().lower() and animal.vacunado:
            encontrados.append(animal)

    return encontrados

def buscar_animales_jovenes(animales, edad_maxima):
    encontrados = [] 

    for animal in animales:
        if animal.edad <= edad_maxima:
            encontrados.append(animal)

    return encontrados

def buscar_gatos_o_perros_mayores(animales, edad_minima):
    encontrados = [] 

    for animal in animales:
        if (animal.especie.lower() == "perro" or animal.especie.lower() =="gato") and animal.edad >= edad_minima:
            encontrados.append(animal)

    return encontrados

def buscar_vacunados_jovenes(animales, edad_maxima):
    encontrados = [] 
    
    for animal in animales:
        if animal.vacunado and animal.edad <= edad_maxima:
            encontrados.append(animal)

    return encontrados

def buscar_animales_completos(animales, edad_maxima, edad_minima, ciudad):
    encontrados = [] 
    
    for animal in animales:
        if animal.vacunado and (animal.edad >= edad_minima and animal.edad <= edad_maxima) and animal.ciudad.strip().lower() == ciudad.strip().lower():
            encontrados.append(animal)

    return encontrados



michi = Animal("Michi", 9, "Gato", "Bogotá", False)
firulais = Animal("Firulais", 5, "Perro", "Medellín", True)
Luna = Animal("Luna", 3, "Perro", "Cali", False)

animales = [michi, firulais, Luna]

resultado = buscar_por_especie(animales, "Perro")
print(resultado)

for animal in resultado:
    print(animal.nombre)

'''----------------------------------------------------'''

animal_encontrado = buscar_animal(animales, "Michi")
print(animal_encontrado)

if animal_encontrado != None:
    print(animal_encontrado.nombre)
else:
    print("Animal no encontrado")
'''----------------------------------------------------'''

for animal in resultado:
    animal.vacunar()
    animal.mostrar_info()
'''------------------------------------------------------'''
resultado_vacunados = buscar_vacunados(animales)
for animal in resultado_vacunados:
    print(animal.nombre)

'''-----------------------------------------------------'''
resultado = buscar_perros_vacunados(animales)
for animal in resultado:
    print(animal.nombre)

'''----------------------------------------------------'''

resultado_mayores = buscar_mayores(animales, 5)

for animal in resultado_mayores:
    print(animal.nombre, animal.edad)

'''----------------------------------------------------'''

resultado = buscar_perros_mayores(animales, 5)
for animal in resultado:
    print(animal.nombre, animal.edad, animal.vacunado)

'''---------------------------------------------------'''

resultado = buscar_por_ciudad(animales, "Cali")

for animal in resultado:
    print(animal.nombre)

''' --------------------------------------------------'''

resultado = buscar_por_ciudad_y_vacunados(animales, "Medellín")

for animal in resultado:
    print(animal.nombre)

''' --------------------------------------------------'''


animal_encontrado = buscar_animal(animales, "Michi") #cambiar edad por meido de nombre 


if animal_encontrado != None:
    animal_encontrado.cambiar_edad(12)
    print(animal_encontrado.nombre, animal_encontrado.edad)
else:
    print("Animal no encontrado")
  

print(michi.edad) # prueba

''' --------------------------------------------------'''

resultado = buscar_animales_jovenes(animales, 5)

for animal in resultado:
    print(animal.nombre)

'''---------------------------------------------------'''

resultado = buscar_gatos_o_perros_mayores(animales, 5)

for animal in resultado:
    print(animal.nombre, animal.edad)

'''----------------------------------------------------'''

resultado = buscar_vacunados_jovenes(animales, 5)

for animal in resultado:
    print(animal.nombre, animal.edad, animal.vacunado)

'''---------------------------------------------------'''

resultado = buscar_animales_completos(animales, 8, 3, "Medellín")

for animal in resultado:
    print(animal.nombre, animal.edad, animal.ciudad, animal.vacunado)






''' 
animal_encontrado.cambiar_edad(11)
animal_encontrado.mostrar_info()
animal_encontrado.vacunar()
'''
'''  ------ OTROS EJEMLOS ****---- 
animal_encontrado = buscar_animal("Michi")
print(animal_encontrado)

animal_encontrado = buscar_animal("Michi")

resultado = animal_encontrado.cambiar_edad(10)

print(resultado)
print(animal_encontrado.edad)

print(michi.edad)

animal_encontrado = buscar_animal("Rex")
animal_encontrado = buscar_animal("  mIcHi  ")
#buscar_animal(animales, "  mIcHi  ")


if animal_encontrado != None:
    animal_encontrado.cambiar_edad(7)
    
else:
    print("Animal no encontrado")

print(michi.edad)
'''
