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
                                                                                                                               
                                                                                                                               






