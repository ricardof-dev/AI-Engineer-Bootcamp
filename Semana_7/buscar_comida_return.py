comidas = ["Atún", "Pollo", "Pescado"]


def buscar_comida(comidas, buscada): ## BUSQUEDA CON RETURN 
    if buscada.lower() in [comida.lower() for comida in comidas]:
        return f"{buscada} está registrada."
    else:
        return f"{buscada} no está registrada."


resultado = buscar_comida(comidas, "Pollo") ##  primera manera de mostrar
print(resultado)
resultado = buscar_comida(comidas, "Arroz")
print(resultado)
resultado = buscar_comida(comidas, "atún")
print(resultado)
resultado = buscar_comida(comidas, "PESCADO")
print(resultado)
resultado = buscar_comida(comidas, "Pollo")
print(resultado)

print(buscar_comida(comidas, "Pescado")) ##  segunda manera de mostrar (mas corta) ##
print(buscar_comida(comidas, "Arroz"))