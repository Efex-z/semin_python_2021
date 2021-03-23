"""
Desafíos de la teoría 2
"""
# ------------ desafío 1 -----------------------------------------
# modificar el siguiente codigo para que se imprima la cadena
# "tiene R" si la palabra contiene la letra r y sino "no tiene r"
print(" Desafío 1: fstring1")
for i in range(4):
    cadena = input('Ingresá una palabra ')
    if "r" in cadena:
        print(f'{cadena} tiene una letra r')
# solucion: (probé utilizar la otra definicion de string format)
print(" Desafío 1: fstring2")
for i in range(4):
    cadena = input('Ingresar una palabra ')
    if ("r" in cadena) or ("R" in cadena):
        print('{} tiene  r'.format(cadena))
    else:
        print('{} no tiene r'.format(cadena))
print('-'* 15)

# ------------ desafío 2 -----------------------------------------
# ingresar palabras desde el teclado hasta ingresar la palabra FIN.
# imprimir aquellas que empiecen y terminen con la misma letra.
# desarrollo 1: imprimir a medida que se van leyendo
# *nota: incluyo las palabras de una sola letra como posible solucion.
print(" Desafío 2: imprimir inmediato")
cadena = input("Ingresá una palabra <'FIN' para salir>")
while cadena != 'FIN':
    if cadena[0] == cadena[-1]:
        print(cadena)
    cadena = input("Ingresá una palabra <'FIN' para salir> ")
print('-' * 15)

# desarrollo 2: leer todo_ y luego imprimir: agrego las cadenas a una lista
print(" Desafío 2: imprimir todo junto al final")
cadena = input("Ingresá una palabra <'FIN' para salir> ")
listaCadenas = []
while cadena != 'FIN':
    if cadena[0] == cadena[-1]:
        listaCadenas.append(cadena)
    cadena = input("Ingresá una palabra <'FIN' para salir> ")
for i in listaCadenas:
    print(i)
print("-" * 15)


# ------------ desafio 3 --------------------------------------------
# procesar las notas de los estudiantes del curso: se desea saber:
# . cuál es el promedio de las notas; - cuántos estudiantes estan por debajo
# ingresar las notas, calcular el promedio, calcular cuantos tienen notas menores
# solucion con funciones:
def crear_dic_notas(dicc):
    """ retorna un diccionario con apellido y nota (entero) de
    estudiantes ingresados por teclado
    """

    alumno = input("Apellido <'0' para salir>: ")
    while alumno != '0':
        nota = int(input(f"Nota de {alumno}: "))
        dicc[alumno] = nota
        alumno = input("Apellido <'0' para salir>: ")
    return dicc

def calcular_promedio_dic(dicc):
    """ retorna el valor promedio de un entero en un diccionario
    cuyos valores sean enteros """

    suma = 0
    for i in dicc:
        suma = suma + dicc[i]
    return suma/len(dicc)

print('Se leerán apellidos de estudiantes y sus notas para el desafio 3: ')
dicc = {}
crear_dic_notas(dicc)
# calcular promedio de un diccionario con integer en segundo campo
prom = calcular_promedio_dic(dicc)
print("Promedio: {:.2f}".format(prom)) #limitar a 2 decimales el decimal
# calcular cuantos estudiantes estan por debajo del promedio
for i in dicc:
    if dicc[i] < prom:
        print(f'{i} Está por debajo del promedio. ')
# ------------------------------------------- fin desafio 3 --------

# *NOTA: el punto 46.0.1 será resuelto en un archivo aparte