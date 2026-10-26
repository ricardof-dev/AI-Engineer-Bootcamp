productos = ["Arroz", "Carne", "Yuca", "Ensalada", "Tomate"]
def ver_productos():
    for lista in range(len(productos)):
        print(f"{lista+1}. {productos[lista]}")
def buscar_producto():
    busqueda = input("¿Qué producto buscas? ").lower()

    encontrado = False

    for producto in productos:
        if producto.lower() == busqueda:
            print(f"Encontré {producto}")
            encontrado = True
    if encontrado == False:
        print(f"{busqueda} no está disponible")           
def agregar_producto():
    nuevo_producto = input("¿Qué producto quieres agregar? ")
    productos.append(nuevo_producto)
    print(f"Producto {nuevo_producto} agregado.")
def eliminar_producto():
    producto_eliminado = input("¿Qué producto quieres eliminar? ").lower()
    encontrado = False
    for producto in productos:
        if producto.lower() == producto_eliminado:
            print(f"Producto {producto_eliminado} eliminado.")
            encontrado = True
            productos.remove(producto)
    if encontrado == False:
        print(f"{producto_eliminado} no está disponible")
def menu_principal():
    opcion = 0
    while opcion != 5:
        print("=" * 20)
        print("    INVENTARIO  ") 
        print("=" * 20)
        print("1. Ver productos ")
        print("2. Buscar producto")
        print("3. Agregar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion <1 or opcion >5:
            print (f'Opción no válida.') 
        elif opcion == 1:
            ver_productos()
        elif opcion == 2: 
            buscar_producto()
        elif opcion == 3: 
            agregar_producto()
        elif opcion == 4: 
            eliminar_producto()
        elif opcion == 5: 
            print (f'Vuelva Pronto.')

menu_principal()            
'''          
ver_productos()
buscar_producto()
agregar_producto()
ver_productos()
eliminar_producto()
ver_productos()
'''
