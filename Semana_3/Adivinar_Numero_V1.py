import random
numero_ganador =random.randint(1,10)
numero = 0
vidas = 5
while numero != numero_ganador  and vidas > 0 : 
    print("=" * 40)
    print("   ADIVINA ADIVINADOR   :)  ")
    print("=" * 40)
    numero = int(input("Adivina el número: "))
    if  numero > 10 or numero < 1: 
        print(f'numeros no entran en juego.')    
    elif numero < numero_ganador: 
        vidas = vidas - 1
        print(f"Te quedan {vidas} vidas")
        print (f' El número ganador es mayor.')    
    elif numero > numero_ganador: 
        vidas = vidas - 1
        print(f"Te quedan {vidas} vidas")
        print (f'El número ganador es menor')
if vidas == 0 :
    print (f'Game Over. El numero era {numero_ganador}.')
elif numero_ganador:
    print (f'ganaste!') 





  
