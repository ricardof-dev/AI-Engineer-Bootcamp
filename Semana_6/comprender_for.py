comidas = ["Atún", "Pollo", "Pescado"]

comidas_minusculas = []

for comida in comidas:
    comidas_minusculas.append(comida.lower())

print(comidas_minusculas)

### es esto mismo  
'''
[comida.lower() for comida in comidas] ###list comprehension.
#QUÉ QUIERO HACER  for  ELEMENTO  in  LISTA]'''

resultado = [comida.lower() for comida in comidas]

resultado = [comida for comida in comidas if comida != "Pollo"] ##La clave está en que el if se aplica a cada elemento de la lista:

print(resultado)