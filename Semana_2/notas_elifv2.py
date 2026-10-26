nombre = input('Ingrese su nombre:') .strip()
nota = int(input("Ingrese su nota:"))
if nota > 101 or nota < 0:
    print (f"{nombre}, La nota debe estar entre 0 y 100.")   
elif nota >= 90:
    print (f"{nombre}, tu nota fue {nota}. ")
    print (f"Calificación: A")
    print (f"¡Excelente!")
elif nota >= 60:
     print (f"{nombre}, tu nota fue {nota}.")  
     print (f"Calificación: B") 
     print (f"Aprobado.") 
else:
    print (f"{nombre}, tu nota fue {nota}.")
    print (f"Calificación: C")
    print (f"Reprobado.")
