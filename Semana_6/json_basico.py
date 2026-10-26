import json

animal = {
    "nombre": "Gato",
    "edad": 13,
    "especie":  "Persa",
    "peso": 4.5,
    "salud": {
        "vacunado": True,
        "ultima_vacuna": "2026-05-10"
    },
    "comidas": [
        "Atún", 
        "Pollo",
        "Pescado"
    ]
}

print(json.dumps(animal))

datos_json = json.dumps(animal) ###datos

print(datos_json)
print(type(datos_json)) ##tipos sr,bool,int

datos_python = json.loads(datos_json)  ##diccionario normal:

print(datos_python)
print(type(datos_python))

print(datos_python["nombre"])
print(datos_python["edad"])
print(datos_python["peso"])

print(datos_python["salud" ]) #imprime valor mas datos 

print(animal["salud"]["vacunado"])  #imprime valores separados 
print(animal["salud"]["ultima_vacuna"])

print(animal["comidas"])   #anadir indices nevos con valores

for comida in animal["comidas"]:  #imprime valores separados 
    print(comida)














'''importantísimo para APIs, porque normalmente 
recibiremos datos en JSON y luego Python los convertirá 
en estructuras que podamos manipular.'''