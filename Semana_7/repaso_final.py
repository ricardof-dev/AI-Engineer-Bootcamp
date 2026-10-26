animal = {
    "nombre": "Michi",
    "edad": 3,
    "vacunado": True
}

print(animal.keys())
print(animal.values()) 
print(animal.items())

''' llamado normal 
clave      valor
──────     ─────
nombre  →  Michi
edad    →  3
vacunado→  True
'''
for clave, valor in animal.items():
    print(clave, ':', valor)

for valor in animal.values():
    print(valor)

for clave in animal.keys():      
    print(clave)  

''' llamado con FOR '''