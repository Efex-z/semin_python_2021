nombres = """
'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
"""

eval1 = """
81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
"""

eval2 = """
30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
"""


def limpiarString(cad):
    """ quita cualquier caracter no letra o numero de un string """
    for caracter in cad:
        if not caracter.isalnum():
            cad = cad.replace(caracter, ' ')
    return cad


listaNom = limpiarString(nombres).split()
listaEval1 = limpiarString(eval1).split()
listaEval2 = limpiarString(eval2).split()
# tengo 3 listas con strings (TODAS)

listaUnica = zip(listaNom, listaEval1, listaEval2)
# hago una lista porque un diccionario no admite 2 nombres iguales (y no usamos apellido)
# esta lista unica es una lista de tuplas, dentro de las cuales hay 3 string: 1 nombre y 2 num

listaUnica2 = zip(listaNom, listaEval1, listaEval2)
# hago una copia porque, para trabajar con el zip, una vez que lo recorro no lo puedo volver a hacer.

suma = 0
for cadalista in listaUnica:
    suma = suma + (int(cadalista[1])+int(cadalista[2]))
    # la nota de cada uno está en la posicion 1 y 2 de cada lista elemento de la lista unica;
    # como son strings los debo convertir a enteros para sumarlos
promedio = suma / len(listaNom)
print(f' Promedio (para constatar): {promedio}')
# solo para comprobar

for cadalista in listaUnica2:
    if (int(cadalista[1])+int(cadalista[2])) < promedio:
        print(f' El alumno {cadalista[0]} obtuvo menos que el promedio. Nota: {int(cadalista[1])+int(cadalista[2])}. ')
