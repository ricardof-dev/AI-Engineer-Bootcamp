nombre = input ('Cual es tu nombre ?? ' ) .strip()
edad = int(input ('Cuantos anos tienes? ')) 
ciudad = input ('Donde Vives? ') .strip()
profesión = input ('Cual es tu Profesión? ') .strip()

print ('----------------------------------------')
print ('TARJETA DE PRESENTACIÓN')
print ('----------------------------------------')

print (f'Nombre: {nombre}')
print (f'Edad:{edad}')
print (f'Ciudad: {ciudad}')
print (f'Profesión : {profesión}')

print (f'Tu nombre en Mayuscula :{nombre.upper()}')


print  (f'tu nombre tiene {len(nombre)} letras.')

print ('----------------------------------------')
print ('Gracias por usar el programa.')
print ('----------------------------------------')

