''' 
PRIMERA PIEZA: try / except
try:
    # código que podría producir un error
except:
    # qué hacer si ocurre el error

example
'''
try:
    archivo = open("animales.txt", "r")
except:
    print("No se pudo abrir el archivo")
#------
try:
    archivo = open("perros.txt", "r")
    print("Archivo abierto correctamente")
except:
    print("No se pudo abrir el archivo")
print("El programa continúa")  #-------------------- Ahí está la magia de la robustez.
#------
'''
sin try
''' 
archivo = open("perros.txt", "r")
print("Hola")

#Se produce el error y "Hola" no llega a ejecutarse.
    
    
    
    
    
    
