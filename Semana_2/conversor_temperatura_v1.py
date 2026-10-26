print("=" * 40)
print("     CONVERSOR DE TEMPERATURA")
print("=" * 40)
escala_de_temperatura = int(input('1. Celsius → Fahrenheit 2. Fahrenheit → Celsius Seleccione una opción: '))
if  escala_de_temperatura <1 or escala_de_temperatura >2:
    print (f'Opción no válida.')
elif escala_de_temperatura == 1:
    Celsius = float(input("Ingrese los grados Celsius:"))
    Fahrenheit = (Celsius * 9 / 5) + 32 
    print (f'{Celsius} °C son {Fahrenheit}°F.')
elif escala_de_temperatura == 2:
    Fahrenheit= float(input("Ingrese los grados Fahrenheit:"))
    Celsius  = (Fahrenheit -32) * 5 / 9 
    print (f'{Fahrenheit}°F son {Celsius} °C.')








