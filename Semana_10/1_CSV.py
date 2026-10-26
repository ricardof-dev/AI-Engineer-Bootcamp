'''
CSV
│
├── columnas → qué tipo de dato tenemos
│
└── filas → registros
      │
      ├── valores
      ├── valores
      └── valores

---------------
nombre   edad   especie   ciudad    vacunado
fila 1  Firulais  5     Perro     Bogotá     True
fila 2  Michi     3     Gato      Bogotá     True
fila 3  Luna      2     Perro     Mosquera   False
🧩 Primera gran idea de CSV

Cada fila = un registro

Cada columna = un atributo/campo
---------------------------

read() → archivo → str
split() → str → list

-----------------------------

se podria 

'''
archivo = open ("Semana_10/animales.csv","r")

contenido = archivo.read()

animales = contenido.split ("\n")

archivo.close() 


for animal in animales [1:]:
    datos = animal.split(",")

    if datos[2] == "Perro":
        #print(datos[0]) ------ para un dato
        print(datos[0], datos[3]) #---- para buscar dos 

'''
Se llama slicing y empieza desde el índice indicado.
'''
#for animal in animales[1:]: #INDICE [x : (“desde la posición 1 hasta el final.”) ] 

for animal in animales[1:]:
    datos = animal.split(",")

    if datos[4] == "False": #esa bscando en Vacnados or  es 4 
        print(datos[0],datos[1] )