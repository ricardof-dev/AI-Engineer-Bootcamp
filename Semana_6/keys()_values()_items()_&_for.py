'''.keys() + .values() + .items() + for'''
animal = {
    'nombre' :'Gato',   # str
    'edad': 13, #int
    'especie': 'Persa',   #str
     'color': 'Blanco', #str
    'peso' : 4.5 #float
}
print(animal.keys())
print(animal.values())
print(animal.items())

for clave, valor in animal.items(): #1 
    print(clave, valor) 

for clave, valor in animal.items(): #mas presentable 2
    print(f'{clave} : {valor}') 

for clave, valor in animal.items():  #uso del if ****
    if clave == 'edad':
        print(f"La edad es: {valor}")

for clave, valor in animal.items():    #mini reto 
    if clave == 'color':
        print(f"El color es: {valor}")

for clave, valor in animal.items(): #qué tipo tiene cada valor.
    print(clave, type(valor))

for clave, valor in animal.items(): #Python nos diga solamente cuándo encuentra un número entero.
    if type(valor) == int:
        print(f"La clave {clave} contiene un entero.")

for clave, valor in animal.items():  #qué tipo tiene cada valor
    if type(valor) == str:
        print(clave, type(valor))
    elif type(valor) == int:
        print(clave, type(valor))
    elif type(valor) == float:
        print(clave, type(valor))

for clave, valor in animal.items(): #minireto
    if type(valor) == str:
        print(f"{clave} → Texto")
    elif type(valor) == int:
        print(f"{clave} → Número entero")
    elif type(valor) == float:
         print(f"{clave} → Número decimal")








