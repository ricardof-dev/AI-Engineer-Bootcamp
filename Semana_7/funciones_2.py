comidas = ["Atún", "Pollo", "Pescado"]
juguetes = ["Pelota", "Ratón", "Cuerda"]
def saludar(nombre="compañero"):
    print(f"Hola, {nombre}")
def presentar(nombre, ciudad="Bogotá"): #presentacion doble 
    print(f"Me llamo {nombre} y vivo en {ciudad}")
def calcular_precio(precio, descuento=0):
    resultado = precio - descuento
    return resultado
def mostrar_comidas(lista):
    for comida in lista:
        print(comida)
def mostrar_juguetes(lista): 
    for juguetes in lista:
        print(juguetes)
def buscar_comida(comidas, buscada): ##buscar **** 
    if buscada.lower() in [comida.lower() for comida in comidas]:
        print(f"{buscada}")
    else:
        print(f"No encontramos {buscada} ")

saludar()
saludar("Ricardo")
presentar("Ricardo")
presentar("Ricardo", "Toronto")

print(calcular_precio(100))
print(calcular_precio(100, 20))
resultado = calcular_precio(100, 20) # 1/2
print(resultado) # 2/2
mostrar_comidas(comidas)
mostrar_juguetes(juguetes)
buscar_comida(comidas, "Pollo")
buscar_comida(comidas, "Arroz")

'''
print() → mostrar

return → devolver para poder utilizar
'''

