nombre = input("¿Cuál es tu nombre? ")
edad = int (input ('Que edad Tienes?'))

def saludar(nombre, edad):
    print(f"Hola, bienvenido al Bootcamp AI Engineer {nombre},")
    print(f"Actualmente tienes {edad} anos.")

saludar(nombre,edad)
