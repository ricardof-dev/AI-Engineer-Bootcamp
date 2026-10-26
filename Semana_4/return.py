a = int(input("Número A: "))
b = int(input("Número B: "))

def sumar (a,b):
    resultado  = a + b 
    return resultado

def multi (a,b):
    resultados  = a * b 
    return resultados


resultados = multi (a, b)
resultado = sumar(a, b)
total = resultado + resultados

print (total)
print(resultado)
print(resultado*2)
if resultado > 50:
    print("Es mayor de 50")  




