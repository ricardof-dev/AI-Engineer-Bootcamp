animal = {
    "nombre": "Gato",
    "edad": 13,
    "especie":  "Persa",
    "peso": 4.5,
    "comidas": ["Atún", "Pollo","Pescado"],
    "juguetes": ["Pelota", "Ratón", "Cuerda"]
}
print(animal)
for comidas in animal["comidas"]:
    if comidas == "Pollo":
        print('El gato come Pollo')

for juguetes in animal["juguetes"]:
    if juguetes == "Ratón":
        print('Su juguete favorito es Ratón')

