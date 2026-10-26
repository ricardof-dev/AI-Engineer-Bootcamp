productos = ["Arroz", "Carne", "Yuca", "Ensalada"]
frutas = ["Manzana", "Banano", "Mango", "Pera"]

######### insert (Cuentan desde 0)
productos.insert(2, "Papa") # uitliza para meter en lista moviendo numero de posicion  hacia adelante ejemplo

######### indice negativo 
'''
índice positivo → empieza desde el principio
índice negativo → empieza desde el final
'''
productos[-1]  #empieza desde el final ahi mostraria *yuca*

######### sort 
productos.sort() #ordena los valores
productos.reverse() #ordena en orden despues d ela accion sort

######### reverse
frutas.reverse() # No significa "ordenar de mayor a menor"; simplemente da vuelta la lista tal como está.

for lista in range (len(frutas)):
    print(f"{lista+1} ) {frutas[lista]}")
for lista in range (len(productos)):
    print(f"{lista+1} - {productos[lista]}")







