def saludar():
    print("Hol compañero")
def despedir():
    print("Hola, Hasta luego, compañero")
def saludar_persona(nombre): ## nombre = parámetro
    print(f"Hola, {nombre}")
    #Parámetro = espacio preparado para recibir un dato. Argumento = dato que realmente enviamos.
def presentar(nombre, edad):
    print(f"Me llamo {nombre} y tengo {edad} años")   #nombre → parámetro edad → parámetro "Ricardo" → argumento 39 → argumento
def sumar(a, b):    ## RETURN
    resultado = a + b
    return resultado
def multiplicar(a, b):  ## RETURN 2
    resultado = a * b 
    return resultado
def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"
def calcular_doble(numero):
    resultado = numero * 2
    return resultado
def calcular_promedio(nota1, nota2, nota3):
        resultado = (nota1+nota2+nota3) /3
        return resultado
saludar()
despedir()
saludar_persona("Ricardo")
saludar_persona("Ana")
presentar("Ricardo", 39)
presentar("Ana", 25)
total = sumar(10, 5)
print(total)
resultado = multiplicar(6, 7)
print(resultado)
print(es_mayor_de_edad(39))
print(es_mayor_de_edad(15))
print(calcular_doble(8))
print(calcular_doble(15))
print(calcular_promedio(80, 90, 70))
