nombre = input ('Cual es tu nombre ?? ' ) .strip()
edad = int(input ('Cuantos anos tienes? ')) 
ciudad = input ('Donde Vives? ') .strip()
comida_favorita = input ('Cual tu comida favorita? ') .strip()
profesión = input ('Cual es tu Profesión? ') .strip()
año_de_nacimiento = int(input ('Cual es tu Año de nacimiento? '))
print("=" * 40)
print("          PERFIL INTELIGENTE")
print("=" * 40)
print(f"Nombre     : {nombre}")
print(f'Edad Actual: {2026 - año_de_nacimiento}')
print(f'Dentro de 10 años tendrás {edad + 10} años.')
print(f'Hace 5 años tenías {edad - 5} años.')
print(f"Ciudad     : {ciudad}")
print(f"Comida favorita     : {comida_favorita}")
print(f"Profesión     : {profesión}")
print(f"Tu nombre tiene {len(nombre)} letras.")
print(f"Nombre en MAYÚSCULAS   : {nombre.upper()}")
print(f"Nombre en minúsculas  : {nombre.lower()}")
print("-" * 40)
print("Gracias por usar Perfil Inteligente.")
print("-" * 40)
####################





