precios = [5000, 12000, 8000, 25000, 3000, 18000]

def aplicar_descuento(precios, descuento=0.20):
    return [precio - (precio * 0.20) if precio > 10000 else precio for precio in precios] 

'''alplicar  dos valores if and else ✅ Usaste if / else dentro de una list comprehension 
                return permite devolver un resultado para utilizarlo después. '''

print(aplicar_descuento(precios))
