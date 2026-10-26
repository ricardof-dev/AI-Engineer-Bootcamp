'''
@property

se utiliza para controlar la lectura.

@edad.setter


se utiliza para controlar la modificación.
Son dos funciones, pero desde fuera seguimos escribiendo:

-----------
Propiedad/setter → cambiar un dato.
Método → ejecutar una acción o comportamiento.
------------

'''

'''

Situación	Mejor diseño
Cambiar un dato directamente, con reglas	michi.edad = 20
Cambiar una propiedad con validación	michi.ciudad = "Cali"
Ejecutar una acción	michi.vacunar()
Preguntar algo al objeto	michi.es_mayor()


🔥 Esto es justamente lo que estamos buscando con OOP: que los objetos no sean solamente "bolsas de datos", sino que tengan comportamiento y reglas.

'''

'''

SETTERS → controlan datos.
MÉTODOS → ejecutan acciones.

El setter protege el atributo; el método controla la acción.


REGLAAAA IMPORTANTE

Cambio simple de dato
        ↓
@property + setter

Acción / comportamiento
        ↓
método()

'''
'''
La diferencia que estamos aprendiendo
Propiedad + setter → cambio directo de un dato con reglas:
animal.ciudad = "Bogotá"animal.edad = 10animal.peso = 20


Método → acción o comportamiento:
animal.vacunar()animal.ganar_peso(5)animal.perder_peso(2)animal.envejecer(3)

'''

''' 

ganar_peso() vs buscar_adoptables()
✅ También vas bien, pero haría una pequeña precisión.
ganar_peso() es un método del objeto porque representa una acción que realiza un Animal sobre sí mismo:


'''
'''
_atributo = dato interno que la clase controla mediante propiedades/métodos ✅

michi.peso
    ↓
@property / setter
    ↓
michi._peso


"Este atributo es interno de la clase; normalmente accedemos a él mediante la propiedad."

property
def peso(self):
    return self._peso

'''