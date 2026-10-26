animal = {"juguetes": ["Pelota", "Ratón", "Cuerda"]}


print(animal["juguetes"]) #llama

for juguetes in animal["juguetes"]: #llamam odos en lista
    print(juguetes)

for juguetes in animal["juguetes"]: #diferencia *** 
    if juguetes == "Ratón":
        print(juguetes)
    if juguetes == "Cuerda":
     print(juguetes)


