animal = {
    'nombre' :'Gato',   # str
    'edad': 13, #int
    'especie': 'Persa',   #str
    'color': 'Blanco' #str
}
print(animal['nombre'])
print(animal['edad'])
print(animal['especie'])
print(animal['color'])

animal['edad'] = 14 # int
print(animal['edad'])

animal['peso'] = 4.5 #float 
print(animal['peso'])

animal['comida favorita'] = 'Atun'
animal['vacunado'] = True #bool siempre mayuscula **
print(f"El gato esta vacunado: {animal['vacunado']}")
print(f"Comida favorita: {animal['comida favorita']}")

if animal['vacunado']: 
    print('vacunado correctamente.')
else: 
    print('Necesita vacunacion urgente.')

animal['vacunado'] = False #bool
if animal['vacunado']: 
    print('vacunado correctamente.')
else: 
    print('Necesita vacunacion urgente.')






