def calculadora():
    print("=" * 40)
    print("     CALCULADORA INTELIGENTE")
    print("=" * 40)
    operación = int(input('¿Qué operación deseas? 1. Sumar 2.Restar 3. Multiplicar 4. Dividir  Ingrese una opción:'))
    if  operación <1 or operación >4:
        print (f'Opción no válida.') 
    
    elif operación == 1:
        Numero1 = int(input('Ingresa numero 1:'))
        Numero2 = int(input('Ingresa numero 2:'))
        print(f"Resultado: {Numero1 + Numero2}")
        
    elif operación == 2:
        Numero1 = int(input('Ingresa numero 1:'))
        Numero2 = int(input('Ingresa numero 2:'))
        print(f"Resultado: {Numero1 - Numero2}")
    elif operación == 3:
        Numero1 = int(input('Ingresa numero 1:'))
        Numero2 = int(input('Ingresa numero 2:'))
        print(f"Resultado: {Numero1* Numero2}")
    elif operación == 4:
        Numero1 = int(input("Ingresa numero 1: "))
        Numero2 = int(input("Ingresa numero 2: "))
        if Numero2 == 0:
            print(f"Error: no se puede dividir entre cero.")
        else:
            print(f"Resultado: {Numero1 / Numero2}")
def imc():
    print("=" * 40)
    print("     CALCULADORA IMC")
    print("=" * 40)
    peso = int(input('Ingrese su peso (kg): '))
    estatura = float(input('Ingrese su estatura (m): '))
    if peso <= 0 or estatura <= 0:
        print (f"error debe ser mayor a 1.") 
    else :
     resultado = peso / (estatura * estatura)
     print (f'Tu IMC es de {resultado}')
def conversor():
    print("=" * 40)
    print("     CONVERSOR DE MONEDAS")
    print("=" * 40)


    pesos = float(input("Ingrese la cantidad en pesos: "))
    dolares = float(input("Ingrese el precio del dólar: "))


    print(f"Resultado: {pesos / dolares}")
def saludar():
   
    print(f"Hola, bienvenido al Bootcamp AI Engineer")
def menu_principal():
    opcion = 0
    while opcion != 5:
        print("=" * 40)
        print("     BOT CERO V2.0  ")
        print("=" * 40)
        print("1. Calculadora")
        print("2. IMC")
        print("3. Conversor de monedas")
        print("4. saludar")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion <1 or opcion >5:
            print (f'Opción no válida.') 
        elif opcion == 1:
           calculadora()
        elif opcion == 2:
            imc()
        elif opcion == 3:
            conversor()
        elif opcion == 4:
            saludar()
        elif opcion == 5:
            print (f'Vuelva Pronto.')
menu_principal()