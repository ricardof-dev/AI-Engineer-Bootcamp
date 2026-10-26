class Animal: # CLASS
    def __init__(self, nombre, edad, especie, ciudad, vacunado): #MOLDE 
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.ciudad = ciudad
        self.vacunado = vacunado

    def mostrar_info(self): #seleccion de atributo selectivo METHOD
        print(self.nombre)
        print(self.edad)
        print(self.especie)
        print(self.ciudad)
        print(self.vacunado)

    def vacunar(self):  

        if self.vacunado : # true 
           print("Ya está vacunado")
        else: # false
            print("No estaba vacunado") 
            self.vacunado = True # cambiar false a  True
            print("Ahora está vacunado")

michi = Animal("Michi", 9, "Gato", "Bogotá", False)
firulais = Animal("Firulais", 5, "Perro", "Medellín", True)
Luna = Animal("Luna", 3, "Perro", "Cali", False)


print(michi.nombre)
print(michi.edad)

michi.edad = 10 #cambia atributos

'''  CAMBIOS CON REGLAS 
    def cambiar_ciudad(self, nueva_ciudad): # cambia atributos con reglas 1
        if nueva_ciudad != "":
        self.ciudad = nueva_ciudad
-----------------------

    def cambiar_ciudad(self, nueva_ciudad): # cambia atributos con reglas 2 mas complejo
    ciudades_validas = ["Bogotá", "Medellín", "Cali"]

    if nueva_ciudad in ciudades_validas:
        self.ciudad = nueva_ciudad
    else:
        print("Ciudad no válida")

Atributo directo → cambio sencillo.
Método (def) → cambio/acción donde podemos meter reglas, validaciones o lógica.

'''

print(michi.edad)

firulais.nombre = "Firu" # cambia atributo 
print(firulais.nombre)

michi.mostrar_info() #METHOD

michi.vacunar()
michi.mostrar_info()

Luna.mostrar_info()
Luna.vacunar()
Luna.mostrar_info()


'''

class        → molde
__init__     → inicializa el objeto
self         → objeto actual
atributos    → datos
def          → métodos/acciones
if/else      → reglas
objeto       → instancia de una clase

'''




