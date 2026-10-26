class Animal:                                                        
    def __init__(self, nombre, edad, especie, ciudad, vacunado,peso):
        self.nombre = nombre                                         
        self.edad = edad                                             
        self.especie = especie                                       
        self.ciudad = ciudad

        self.vacunado = vacunado                                            
        self.peso = peso  

    def resumen(self):                                                                                                                  
        texto = f"{self.nombre} | {self.edad} años | {self.especie} | {self.ciudad} | {self.peso} | Vacunado: {self.vacunado} "
        return texto     

    def cambiar_ciudad(self, nueva_ciudad):
        self.ciudad = nueva_ciudad         

    def puede_adoptarse(self):                                   
        if self.vacunado and self.edad >=18 and self.peso >= 5 :
            return True                                          
        else:                                                    
            return False  

    def ganar_peso(self, kg):                             
        if type(kg) != int:                               
            raise ValueError("Tiene que ser un número.")  
        elif kg <= 0:                                     
            raise ValueError("El peso debe ser positivo.")
        nuevo_peso = self.peso + kg                       
        self.peso = nuevo_peso                            
       
def buscar_animal(animales, nombre):                                  
        for animal in animales:                                       
            if animal.nombre.strip().lower() == nombre.strip().lower():
                return animal                                         
                                                                                                                          
        return None 

def buscar_adoptables(animales):
    encontrados = []
    
    for animal in animales:
        if animal.puede_adoptarse():
            encontrados.append(animal)

    return encontrados      
                      
@property                                            
def ciudad(self):                                        
        return self._ciudad                              
                                  
@ciudad.setter                                       
def ciudad(self, nueva_ciudad):                      
                                                        
        if type(nueva_ciudad) != str:                    
            raise ValueError("La ciudad debe ser texto.")
        nueva_ciudad = nueva_ciudad.strip()              
        if nueva_ciudad == "":                              
            raise ValueError("Ciudad no válida")         
        self._ciudad = nueva_ciudad                      

##############################################################
michi = Animal("Michi", 9, "Gato", "Bogotá", False, 5)   
animales = [michi]

firulais = Animal("Firulais", 7, "Perro", "Medellín", True, 10)
animales.append(firulais)

luna = Animal("Luna", 3, "Gato", "Cali", False, 5)
animales.append(luna)
##############################################################

animales = [michi, firulais, luna]    


for animal in animales:
    print(animal.nombre)
##--------------------------------------
for animal in animales: 
    print(animal.resumen())
##--------------------------------------
resultado = buscar_animal(animales, "firulais")
print(resultado.resumen())

resultado = buscar_animal(animales, "Marie") # negativo 

if resultado is not None:  # None también es un valor válido que debemos saber manejar.
    print(resultado.resumen())
else:
    print("Animal no encontrado")

##-------------------------------------

resultado = buscar_animal(animales, "firulais")

if resultado is not None:    # None también es un valor de cambio ... 
    resultado.cambiar_ciudad("Bogotá")

print(resultado.resumen())         

##-------------------------------------

resultado = buscar_animal(animales, "firulais")

print(resultado.resumen())  

if resultado is not None:   
    resultado.cambiar_ciudad("Chia")      

print(resultado.resumen())  

print(firulais.puede_adoptarse())

##-------------------------------------

resultado = buscar_animal(animales, "luna")
                                                                                                                                                                                      
print(resultado.resumen())                     
                                                                                            
if resultado is not None:                      
    resultado.cambiar_ciudad("Bucaramanga") 

else :
    print("Animal no encontrado")
                                                                                          
print(resultado.resumen())                     
                                                                                           
print(luna.puede_adoptarse())

##-------------------------------------

resultado = buscar_animal(animales, "Marie")   # prueba negaivo  ...  
                                                                                                             
if resultado is not None:                     
    resultado.cambiar_ciudad("Bucaramanga")   
                                                                                          
else :                                        
    print("Animal no encontrado")

##-------------------------------------
 
firulais.edad = 18

print(firulais.resumen())    

##-------------------------------------

adoptables = buscar_adoptables(animales)

for animal in adoptables:
    print(animal.resumen())

##-------------------------------------

nombre = input("¿Qué animal quieres buscar? ")

resultado_2 = buscar_animal(animales, nombre) 

if resultado_2 is not None:  
    print(resultado_2.resumen()) 
    respuesta = (input  ("Escribe cuántos kg quieres aumentar: ")  )

    try: ##El try debe proteger las dos operaciones que pueden producir un error:
        respuesta = int(respuesta)
        resultado_2.ganar_peso(respuesta)
    except ValueError as e:
        print(e)
    
    print(resultado_2.resumen()) 

else:                                                                                            
    print("Animal no encontrado")                                                      
        
        
    
