saldo =  500
opcion = 0

while opcion != 4:
    print("=" * 40)
    print("   ATM   ")
    print("=" * 40)

    print("1. Saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if  opcion == 1 :
        print(f"Su saldo es ${saldo}") 
    elif opcion == 2:
          deposito = float(input("¿Cuánto desea depositar? $"))   
          saldo = saldo + deposito
          print("Depósito realizado con éxito.")
    elif opcion == 3:
         retiro = float(input("¿Cuánto desea Retirar? $")) 
         if retiro > saldo:
                     print (f'no permite retirar más dinero del disponible.')  
         else:
            saldo = saldo - retiro  
            print("Retiro se realizado con éxito.")      
    elif opcion == 4:
               print (f'Vuelva Pronto.')

     

