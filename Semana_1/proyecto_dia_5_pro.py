nombre = input ('Cual es tu nombre ?? ' ) .strip()
edad = int(input ('Cuantos anos tienes? ')) 
ciudad = input ('Donde Vives? ') .strip()
profesión = input ('Cual es tu Profesión? ') .strip()

print("=" * 40)
print("     TARJETA DE PRESENTACIÓN")
print("=" * 40)

print(f"Nombre     : {nombre}")
print(f"Edad       : {edad}")
print(f"Ciudad     : {ciudad}")
print(f"Profesión  : {profesión}")

print("-" * 40)

print(f"Nombre en mayúsculas: {nombre.upper()}")
print(f"Tu nombre tiene {len(nombre)} letras.")

print("=" * 40)
#Estudiante de AI Engineering