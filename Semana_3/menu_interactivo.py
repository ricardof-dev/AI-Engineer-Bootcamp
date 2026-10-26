
opcion = 1

while opcion != 3:
    print("=" * 40)
    print("   MENÚ  ")
    print("=" * 40)

    print("1. Saludar")
    print("2. Contar hasta 5")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))


    if  opcion <1 or opcion >3:
        print (f'Opción no válida.')   
    elif opcion == 1:
        print (f'Hola Ricardo')        
    elif opcion == 2:
        conteo = 1
        while conteo <= 5:
            print(conteo)
            conteo = conteo + 1  
    elif opcion == 3:
        print (f'Hasta luego.')

    















