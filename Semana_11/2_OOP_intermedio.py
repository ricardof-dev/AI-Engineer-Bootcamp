class Animal:
    def __init__(self, nombre, edad, especie, ciudad, vacunado):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.ciudad = ciudad
        self.vacunado = vacunado

        ''' CON REGLA EJEMPLO 2'''
    def cambiar_edad(self, nueva_edad):
        if 1 <= nueva_edad <= 120:
            self.edad = nueva_edad
            return "Edad actualizada"
        else:
            return "Edad no válida"

    def cambiar_especie(self, nueva_especie):
        if nueva_especie != "":
            self.especie = nueva_especie
            return  "Especie actualizada"
        else:
            return "Ciudad no válida"


    def cambiar_ciudad(self, nueva_ciudad):
        if nueva_ciudad != "":
            self.ciudad = nueva_ciudad
            return "Ciudad actualizada"
        else:
            return "Ciudad no válida"
        
    ''' isinstance(...) → ¿es del tipo correcto?
        != ""           → ¿tiene contenido?'''
    def es_mayor(self):
        if self.edad >=18:
            return True
        else:
            return False

    def actualizar_datos(self, nueva_especie, nueva_ciudad):
        if nueva_ciudad != "" and nueva_especie != "" :
            self.especie = nueva_especie
            self.ciudad = nueva_ciudad
            return "Datos actualizados"
        else:
            return "Datos no válidos"

    def resumen(self):
        return self.nombre, self.edad, self.ciudad ## UNA TUPLA OJO ***
    def mostrar_info(self): 
        print(self.nombre)
        print(self.edad)
        print(self.especie)
        print(self.ciudad)
        print(self.vacunado)

    def coincide_nombre(self, nombre_buscar): # encapsular comportamiento.
        return self.nombre == nombre_buscar

    def vacunar(self):  
        if self.vacunado : 
            print("Ya está vacunado")
        else: # false
            print("No estaba vacunado") 
            self.vacunado = True 
            print("Ahora está vacunado")

''' SIN REGLA EJEMPLO 1'''
    #def cambiar_edad(self, nueva_edad):
    #    if 1 <= nueva_edad <= 120:
    #        self.edad = nueva_edad
    #    else:
    #        print("Edad no válida")


michi = Animal("Michi", 9, "Gato", "Bogotá", False)
firulais = Animal("Firulais", 5, "Perro", "Medellín", True)
Luna = Animal("Luna", 3, "Perro", "Cali", False)

# michi.cambiar_edad(15)
# print(michi.edad)

# michi.cambiar_edad(150)
# print(michi.edad)

resultado = michi.cambiar_edad(15)
print(resultado)

resultado = michi.cambiar_edad(150)
print(resultado)


resultado = michi.cambiar_ciudad("Medellín")
print(resultado)
print(michi.ciudad)

resultado = michi.cambiar_ciudad("")
print(resultado)
print(michi.ciudad)

michi.cambiar_edad(15)
resultado = michi.es_mayor()
print(resultado)

michi.cambiar_edad(20)
resultado = michi.es_mayor()
print(resultado)

resultado = michi.actualizar_datos("Perro", "Cali")
print(resultado)
print(michi.especie)
print(michi.ciudad)

datos = michi.resumen() # TUPLA 
print(datos)

nombre, edad, ciudad = michi.resumen()  # desempaquetar una tupla.
print(nombre)
print(edad)
print(ciudad)

# lista de objetos

animales = []
animales.append(michi)
animales.append(firulais)
animales.append(Luna)
'''
for animal in animales:
    animal.mostrar_info()

for animal in animales:
    if animal.nombre == "Michi":
        #print("Animal encontrado") # muetsra solo msj 
        animal.mostrar_info() # muestra todo 
'''
buscar = input("¿Qué animal buscas? ")

encontrado = False

for animal in animales:
    if animal.coincide_nombre(buscar):
        animal.mostrar_info()
        encontrado = True
        ###animal.cambiar_edad(21) //// cambia directo
        #animal.mostrar_info()

        opcion = input("¿Qué quieres modificar? (edad/especie/ciudad/vacunado): ")

        if opcion == "edad":
         try:
            nuevo_valor = input("¿Cuál es la nueva edad? ")
            edad = int(nuevo_valor)
            animal.cambiar_edad(edad)
            animal.mostrar_info()
         except ValueError:
                print("La edad debe ser un número")
        
        elif opcion == "ciudad":
            nuevo_ciudad = input("¿Cuál es la nueva ciudad? ")
            animal.cambiar_ciudad(nuevo_ciudad)
            animal.mostrar_info()

        elif opcion == "especie":
            nueva_especie = input("¿Cuál es la nueva especie? ")
            animal.cambiar_especie(nueva_especie)
            animal.mostrar_info()
        #3 atributos modificables mediante métodos con reglas:***
        
        elif opcion == "vacunado":
            animal.vacunar()
            animal.mostrar_info()

        else:
            print("Opcion no válida")
    
    
            
if not encontrado:
    print("Animal no encontrado")








