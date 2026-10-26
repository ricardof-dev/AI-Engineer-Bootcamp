productos = ["Arroz", "Carne", "Yuca", "Papa", "Tomate"]
'''
Quiero que hagas estas tres operaciones, en este orden:

Agregar "Leche" al final.
Insertar "Huevos" en la posición 1.
Ordenar la lista alfabéticamente.
'''
productos.append("Leche")
productos.insert(0, "Huevos")

for lista in range (len(productos)):
    print(f"{lista+1} - {productos[lista]}")


productos.sort()

for lista in range (len(productos)):
    print(f"{lista+1} - {productos[lista]}")




