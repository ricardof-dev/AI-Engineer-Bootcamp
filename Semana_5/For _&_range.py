nombres = ["Ana", "Juan", "María", "Pedro"]
edades = [10, 25,9, 35] #recorre datos que ya existen.
productos = ["Arroz", "Carne", "Papa", "Ensalada"]
numeros = [5, 12, 8, 20, 3]
numers = [15, 22, 7, 40, 13, 8]
animales = ["Perro", "Gato", "Caballo", "Pez"]

for nombre in nombres:
    print(f"Hola mi nombre es {nombre}")
for edad in edades:
     if edad >=18:
        print(f"{edad} es mayor de edad")
     else:
       print(f"{edad} es menor de edad")
for disponible in productos: 
    if disponible =="Carne" or disponible  =="Papa":
     print (f"Encontre {disponible}")
    else:
        print (f"Otro producto")
for numero in numeros:
   if numero >=10:
    print (f"{numero}")    
for conteo in   range (1,6) :   
 print(conteo)

for number in range (1,11):
 print (f"Numero {number}")

for pares in range(2,11,2):
 print(pares)
for impares in range(10,4,-1):
 print(impares)

for numero in range(2, 21):
  if numero % 2 == 0:
    print (f"Par: {numero}")
for numero in range(2, 21):
  if numero % 2 != 0:
    print (f"Impar: {numero}")

for numers in numers:
  if numers %2 == 0:
   print (f'par {numers} ')     ## PENDIENTE MAS A FONDO ###
#for numers in numers:
  #if numers %2 == 0 or numers %2 != 0:
   #print (f'pares e impares {numers} ') 

print(animales[3])

animales[2] = "León, no caballo"
print(animales[2])  #indice y posiion siempre desde 0 **** 

