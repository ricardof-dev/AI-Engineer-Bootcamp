comidas = ["Atún", "Pollo", "Pescado", "Arroz", "Pan"]
numeros = [2, 5, 8, 11, 14, 17]
precios = [5000, 12000, 8000, 25000, 3000, 18000]

def precios_caros(precios):
    return [caro for caro in precios if (caro) > 10000]
def precios_disc(precios):
    return [caro - (caro * 0.10)for caro in precios if (caro) > 10000]
def precios_economicos(precios):
    return [barato for barato in precios if (barato) <= 10000]
def aplicar_descuento(precios, descuento=0.20):
    return [precio - (precio * descuento) for precio in precios if (precio) > 10000]

def numeros_mayores(numeros):
    return [numero for numero in numeros if (numero) > 10] 
def buscar_comidas(comidas):
    return [comida for comida in comidas if len(comida) > 5] 
'''se lee:
"Devuelve comida, por cada comida de comidas, si comida tiene más de 5 caracteres.
[comida for comida in comidas]
   ↑          ↑
   │          └── cada elemento que voy recorriendo
   └───────────── lo que quiero guardar
   "'''

print(buscar_comidas(comidas))
print(numeros_mayores(numeros))
print(precios_caros(precios))
print(precios_disc(precios))
print(precios_economicos(precios))
print(aplicar_descuento(precios))
print(aplicar_descuento(precios, 0.10))