nombre = input('Ingrese su nombre:') .strip()
nota = int(input("Ingrese su nota:"))

print("=" * 40)
print("     CALIFICACION DE NOTAS")


if nota >= 90:
    print (f"{nombre}, tu nota fue {nota}. ¡Excelente, muy orgulloso!")

elif nota >= 60:
     print (f"{nombre}, tu nota fue {nota}. Estas Aprobado, muy bien!")
   
else:
    print (f"{nombre}, tu nota fue {nota}. Reprobaste, suerte la proxima.")




print("=" * 40)
print("     Gracias por usar el programa.")
print("=" * 40)
