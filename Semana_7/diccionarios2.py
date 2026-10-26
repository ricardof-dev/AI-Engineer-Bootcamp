persona = {
    "nombre": "Ricardo",
    "edad": 30,
    "ciudad": "Bogotá"
}
animal = {
    "nombre": "Michi",
    "edad": 3
}
''' persona es DICCIONARIO /// nombre es la CLAVE  // Ricardo es el VALOR '''
print(persona)
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
persona["edad"] = 31 #REEMPLAZA VALOR
persona["profesion"] = "Programador" #CREA CLAVE Y VALOR 
persona["apellido"] = "Forero" 
print(persona["edad"])
print(persona)

animal["vacunado"] = True  #CREA CLAVE Y VALOR  2
print(animal)

for dato in animal:  # imprime clave
    print(dato)
    '''animal# claves 
       animal.values()  # valores'''
for dato in animal.values(): # imprime valor 
    print(dato)
for dato, valor in animal.items(): #imprime ambos  
    print(dato, ':', valor)


    