productos = ["Arroz", "Carne", "Yuca", "Ensalada", "Tomate"]
'''¿Está "Tomate" en la lista?'''
busqueda = input("¿Qué producto buscas? ").lower()
'''
if'Tomate' in productos:
    print('Encontre Tomate')
else:
    print('Tomate no está disponible')

if 'Leche' in productos:
    print('Encontre Leche')
else:
    print('Leche no está disponible')
'''
encontrado = False
for producto in productos:
    if producto.lower() == busqueda:
        print(f"Encontré {producto}")
        encontrado = True

if encontrado == False:
    print(f"{busqueda} no está disponible")











