numeros = [5, 12, 8, 25, 3, 18]

def duplicar_grandes (numeros):
    return [numero * 2  if numero > 10 else numero for numero in numeros]
'''duplica'''
def clasificar_numeros(numeros):
    return ["GRANDE"  if numero >= 20 else "NORMAL" for numero in numeros] 
'''clasifica'''

        

print(duplicar_grandes(numeros))
print(clasificar_numeros(numeros))

