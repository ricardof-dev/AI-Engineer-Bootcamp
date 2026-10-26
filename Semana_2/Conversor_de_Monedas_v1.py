print("=" * 40)
print("     CONVERSOR DE MONEDAS")
print("=" * 40)
moneda = int(input(' 1. COP → USD   2. USD → COP   Seleccione una opción:'))
if  moneda <1 or moneda >2:
    print (f'Opción no válida.')
elif moneda == 1:
    pesos = float(input("Ingrese la cantidad en pesos: "))
    tasa_cambio = float(input("Ingrese la tasa de cambio: "))
    if pesos <= 0 or tasa_cambio <= 0:
        print(f"Error: los valores deben ser mayores que cero.")
    else:
        print(f"Resultado: {pesos / tasa_cambio}")
elif moneda == 2:
    dolares = float(input("Ingrese la cantidad en dólares: "))
    tasa_cambio = float(input("Ingrese la tasa de cambio: "))
    if tasa_cambio <= 0 or dolares <= 0:
          print(f"Error: los valores deben ser mayores que cero.")
    else:
       print(f"Resultado: {dolares * tasa_cambio}")
     
       

