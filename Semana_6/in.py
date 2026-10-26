comidas = ["Atún", "Pollo", "Pescado"]

print("Pollo" in comidas)
print("Arroz" in comidas)

busqueda = input("¿Qué comida buscas? ").lower()


if busqueda in [comida.lower() for comida in comidas]: ##.lower() soluciona mayúsculas/minúsculas, pero no elimina tildes.
    print("Sí, está registrada.")

else:
    print("No está registrada.")