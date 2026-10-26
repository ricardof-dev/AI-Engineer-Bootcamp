opcion = 0
while opcion != 7:
    print("=" * 40)
    print("     BOT CERO V1  ")
    print("=" * 40)
    print("1. Calculadora")
    print("2. Conversor de temperaturar")
    print("3. Conversor de monedas")
    print("4. IMC")
    print("5. Cajero ATM")
    print("6. Adivina el número")
    print("7. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion <1 or opcion >7:
        print (f'Opción no válida.') 
    elif opcion == 1:
        print("Aquí irá el Conversor de calculadora")   
    elif opcion == 2:
        print("Aquí irá el Conversor de temperaturar")
    elif opcion == 3:
        print("Aquí irá el Conversor de monedas")
    elif opcion == 4:
        print("Aquí irá IMC")
    elif opcion == 5:
        print("Aquí irá EL Cajero ATM")
    elif opcion == 6:
        print("Aquí irá el juego: Adivina el número")
    elif opcion == 7:
        print (f'Vuelva Pronto.')

  
