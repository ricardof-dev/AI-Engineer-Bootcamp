comidas = ["Atún", "Pollo", "Pescado"]



def comidas_mayusculas(comidas): #.upper() mayusculas
    resultado = []
    return [comida.upper() for comida in comidas]  #[ QUÉ QUIERO HACER  for ELEMENTO in LISTA ] "Devuelve una lista con comida.upper() por cada comida que exista en comidas."
    
  

    for comida in comidas:
        resultado.append(comida.upper())   #.append() agrega

    return resultado



print(comidas_mayusculas(comidas))

