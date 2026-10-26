animal = {
    "nombre": "Gato",
    "edad": 13,
    "especie": "Persa",
    "peso": 4.5,
    "comidas": ["Atún", "Pollo", "Pescado"],
    "juguetes": ["Pelota", "Ratón", "Cuerda"]
}


busqueda = input("¿Qué quieres buscar? ").lower() #pendiente para busca todos sin tilde ** 

if busqueda in [comida.lower() for comida in animal["comidas"]]:
    print("Sí, está registrado como comida.")

elif busqueda in [juguete.lower() for juguete in animal["juguetes"]]:
    print("Sí, está registrado como juguete.")

else:
    print("No encontramos ese dato.")

    
print(repr(busqueda))
print([repr(juguete.lower()) for juguete in animal["juguetes"]])
