print("=" * 40)
print("     CALCULADORA INTELIGENTE")
print("=" * 40)
operación = int(input('¿Qué operación deseas? 1. Sumar 2. Restar 3. Multiplicar 4. Dividir  Ingrese una opción:'))
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
    













####