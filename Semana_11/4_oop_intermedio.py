class Animal:                                                  
    def __init__(self, nombre, edad, especie, ciudad, vacunado,peso):
        self.nombre = nombre                                    
        self.edad = edad                                      
        self.especie = especie                                  
        self.ciudad = ciudad  

        if type(vacunado) != bool:                             
            raise ValueError("Vacunado debe ser True o False.")

        self._vacunado = vacunado   
        self.peso = peso       
        
  #  def envejecer(self):  #cuenta un ano automatizado
        #if self.edad < 120:
           # self.edad +=1 #representa cuánto queremos sumar += 

           # return "Ahora tiene " + str(self.edad) + " años"   
      #  else:

           # return "Edad máxima alcanzada"  

 

#-------- versión de prueba ---------------
    #def envejecer2(self, años):
       # edad_nueva = self.edad + años

       # if años > 0 and edad_nueva <= 120:
          #  self.edad = edad_nueva
      #      return "Edad actualizada"
     #   else:                       
    #        return "Edad no válida" 

#----- versión mejor diseñada -----

    def envejecer(self, años=1):  #“Si no me das años, usaré 1.”

        if type(años) != int:                     
            raise ValueError("Tiene que ser un número.")
        
        elif años <= 0:
            raise ValueError("Los años deben ser positivos.")     
        
        nueva_edad = self.edad + años
        self.edad = nueva_edad


#encapsulación en acción.

    @property
    def edad(self):
         return self._edad

    @edad.setter
    def edad(self, edad_nueva):
        if type(edad_nueva) != int:
            raise ValueError("Tiene que ser un número.")
        elif 1 <= edad_nueva <= 120:  # mas limpia  poner if edad_nueva >= 1 and edad_nueva <= 120:
            self._edad = edad_nueva
        else:
            raise ValueError("Edad no válida")
        
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

    def es_mayor(self):
        # -- opcion 1  -- 
        '''if self.edad >=18:
            return True   
        else:             
            return False ''' 
        # -- opcion 2  --  mas limpia
        return self.edad >= 18

    @property   #### MISMO NOMBRE
    def especie(self): 
        return self._especie
    
    @especie.setter #### MISMO ESPECIE
    def especie(self, nueva_especie):

            if type(nueva_especie) != str:
                raise ValueError("La especie debe ser texto.")
            
            nueva_especie = nueva_especie.strip()

            if nueva_especie != "":
                self._especie = nueva_especie
        
            else :
                raise ValueError("Especie no válida")

        
    def vacunar(self):
        if self._vacunado:
            return "Ya está vacunado"
        else:
            self._vacunado = True
            return "Ahora está vacunado"

    @property
    def vacunado(self):
        return self._vacunado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if type(nuevo_nombre) != str:
            raise ValueError("El nombre debe ser texto.")

        nuevo_nombre = nuevo_nombre.strip()

        if nuevo_nombre == "":
            raise ValueError("Nombre no válido")

        self._nombre = nuevo_nombre

    @property
    def peso(self):
        return self._peso



    @peso.setter
    def peso(self, nuevo_peso):
        

        if type(nuevo_peso) != int: 
            raise ValueError("Tiene que ser un número.")
        
        elif nuevo_peso <= 0:
            raise ValueError("El peso debe ser positivo.") 
        elif 1 <= nuevo_peso <= 200:
                self._peso = nuevo_peso       
        else:                                 
            raise ValueError("Peso no válida")

    def ganar_peso(self, kg):

        if type(kg) != int:
            raise ValueError("Tiene que ser un número.")

        elif kg <= 0:
            raise ValueError("El peso debe ser positivo.")

        nuevo_peso = self.peso + kg
        self.peso = nuevo_peso

    def perder_peso(self, kg):

        if type(kg) != int:                               
            raise ValueError("Tiene que ser un número.")  

        elif kg <= 0:                                     
            raise ValueError("El peso debe ser positivo.")
        
        nuevo_peso = self.peso - kg
        self.peso = nuevo_peso

    def puede_adoptarse(self):

        if self._vacunado and self.edad >=18 and self.peso >= 5 :
            return True
        else:
            return False

    def resumen(self):
        texto = f"{self.nombre} | {self.edad} años | {self.especie} | {self.ciudad} | {self.peso} | Vacunado: {self.vacunado} "
        return texto

michi = Animal("Michi", 9, "Gato", "Bogotá", False, 5)        
firulais = Animal("Firulais", 5, "Perro", "Medellín", True, 20)
Luna = Animal("Luna", 3, "Perro", "Cali", False, 8 )           
                                                                                                        
animales = [michi, firulais, Luna]    

print(michi.edad)
print(michi.envejecer())
print(michi.edad)

'''
print(michi.edad)       
michi.envejecer2(120)
print(michi.envejecer2(120))
print(michi.edad)       

michi.envejecer2(3)
print(michi.edad)

michi.envejecer2(-3)
print(michi.envejecer2(-3))
print(michi.edad)

michi.envejecer2(200)
print(michi.envejecer2(200))
print(michi.edad)
'''
##--------------------------------------
print(michi.edad)
print(michi.envejecer())
print(michi.edad)

print(michi.envejecer(5))
print(michi.edad)
##--------------------------------------
print(michi.edad)
michi.edad = 15
print(michi.edad)

try:
    michi.edad = -5
except ValueError as e:
    print(e)

print(michi.edad)

##--------------------------------------
print(michi.ciudad)
michi.ciudad = "Medellín"
print(michi.ciudad)

try:
    michi.ciudad = ""
except ValueError as e:
    print(e)

print(michi.ciudad)

#---------------------------------------
michi.edad = 20

print(michi.es_mayor())
print(firulais.es_mayor())
print(Luna.es_mayor())

#---------------------------------------
'''
print(michi._especie)
michi.cambiar_especie("Perro")
print(michi._especie)
                   
try:
    michi.cambiar_especie("   ")
except ValueError as e:
    print(e)
'''
#---------------------------------------
michi.especie = "Perro"
print(michi.especie)

#---------------------------------------

print(michi.vacunado)
print(michi.vacunar())
print(michi.vacunado)

print(michi.vacunar())
print(michi.vacunado)

#---------------------------------------

print(michi.nombre)

try:
    michi.nombre = ""
except ValueError as e:
    print(e)

print(michi.nombre)

#---------------------------------------


try:
    michi.edad = True
except ValueError as e:
    print(e)

michi.edad = 25
print(michi.edad)


try:
    michi.edad = "veinte"
except ValueError as e:
    print(e)

print(michi.edad)

#---------------------------------------

try:
    michi.ciudad = 123
except ValueError as e:
    print(e)

try:
    michi.ciudad = "     "
except ValueError as e:
    print(e)

michi.ciudad = "   Bogotá   "
print(michi.ciudad)

#---------------------------------                                

try:
    michi.especie = 123
except ValueError as e:
    print(e)

try:
    michi.especie = "     "
except ValueError as e:
    print(e)

michi.especie = "   Perro   "
print(michi.especie)

#---------------------------------  

try:
    michi.nombre = 123
except ValueError as e:
    print(e)

try:
    michi.nombre = "     "
except ValueError as e:
    print(e)

michi.nombre = "   Firulais   "
print(michi.nombre)

#---------------------------------  

try:
    prueba = Animal("Firulais", 5, "Perro", "Medellín", "SI",20 )
except ValueError as e:
    print(e)
 

prueba = Animal("Firulais", 5, "Perro", "Medellín", True,20)
print(prueba.vacunado)

#---------------------------------  

firulais = Animal("Firulais", 5, "Perro", "Medellín", False,20)

print(firulais.nombre)
print(firulais.edad)
print(firulais.especie)
print(firulais.ciudad)
print(firulais.vacunado)

firulais.envejecer(3)
print(firulais.edad)


try:
    firulais.envejecer(200)
except ValueError as e:
    print(e)

print(firulais.edad)

try:
    firulais.envejecer(-2)
except ValueError as e:
    print(e)

print(firulais.edad)


try:
    prueba = Animal("Firulais", 5, "Perro", "Medellín", "SI", 20)
except ValueError as e:
    print(e)

#---------------------------------  

michi.peso = 50
print(michi.peso)

try:
    michi.peso = 250
except ValueError as e:
    print(e)

print(michi.peso)

michi.peso = 50
michi.ganar_peso(10)
print(michi.peso)

try:
    michi.ganar_peso(150)
except ValueError as e:
    print(e)

print(michi.peso)

try:
    michi.ganar_peso(-10)
except ValueError as e:
    print(e)

print(michi.peso)

try:
    michi.ganar_peso(150)
except ValueError as e:
    print(e)

print(michi.peso)

#---------------------------------  

michi.peso = 50

michi.perder_peso(10)
print(michi.peso)

try:
    michi.perder_peso(50)
except ValueError as e:
    print(e)

print(michi.peso)

try:
    michi.perder_peso(-5)
except ValueError as e:
    print(e)

print(michi.peso)

#---------------------------------  

print(michi.puede_adoptarse())

print(firulais.puede_adoptarse())

#---------------------------------  

michi = Animal("Michi", 17, "Gato", "Bogotá", False, 40)
firulais = Animal("Firulais", 20, "Perro", "Medellín", True, 20)

print(michi.puede_adoptarse())
print(firulais.puede_adoptarse())

#---------------------------------  

print(firulais.resumen())
print(michi.resumen())