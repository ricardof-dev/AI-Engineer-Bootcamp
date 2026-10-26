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


#print("=" * 40)
#print("     SI TIENE ENTRE 18.5 Y 24.9 IMC ERES UNA PERSONA SALUDABLE")
#print("=" * 40)

   