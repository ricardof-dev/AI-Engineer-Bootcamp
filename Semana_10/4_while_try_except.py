animal = ["Michi", "3", "Gato", "Bogotá", "True"]


'''
valido = False

while not valido:
    try:
        nuevo_valor = input("Edad: ")
        animal[1] = int(nuevo_valor)
        valido = True
    except ValueError:
        print("Edad no válida")

'''

''' -----------------------  MUY PRESENTE EL WHILE EN BUCLE CON CONTROCL C SE CANCELA '''

valido = False

while not valido:
    nuevo_valor = input("¿Está vacunado? ")
    print("RECIBIDO:", repr(nuevo_valor))

    if nuevo_valor == "True" :
        animal[4] = True
        valido = True
        print("DEBUG:", valido)
    elif nuevo_valor == "False":
        animal[4] = False
        valido = True

    else:
        print("Valor no válido")

print("Valor final:", animal[4])

'''
next(lector) → avanza una fila (normalmente el encabezado).
list(lector) → recoge todas las filas restantes.

'''



