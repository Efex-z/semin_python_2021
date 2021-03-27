minas = [
    '-*-*-',
    '--*--',
    '----*',
    '*----',
]
# dimensiones : 5 ancho * 4 alto

minasNum = ['' for item in minas]
# lista que contendra las respuestas. solo le reemplazare los guiones

topealto = len(minas) - 1
topeancho = len(minas[0]) - 1
# valores que usare como INDICE LIMITE (por eso -1)


def chequearCeldasIxD(cadena, indice, tope):
    """ recibe una cadena, un indice de la misma y un tope posible de indice, y devuelve
    cuantas minas hay en total a izquierda y a derecha de ese indice, y si hay una
    mina en ese indice """
    contMina = 0
    if cadena[indice] == '*':
        contMina = contMina + 1
    if 0 < indice < tope:
        # si no estoy en la primera ni ultima celda, debo mirar a izq y derecha
        if cadena[indice - 1] == '*':
            # chequeo espacio anterior
            contMina = contMina + 1
        if cadena[indice + 1] == '*':
            # chequeo espacio siguiente
            contMina = contMina + 1
    elif indice == 0:
        # si es la primer celda, debo ver solo a derecha
        if cadena[indice + 1] == '*':
            contMina = contMina + 1
    else:
        # la unica opcion disjunta es que esté en el extremo derecho del string
        if cadena[indice - 1] == '*':
            contMina = contMina + 1
    return contMina


def chequearCeldasID(cadena, indice, tope):
    """ recibe una cadena, un indice de la misma y un tope posible de indice, y devuelve
    cuantas minas hay en total a izquierda y a derecha de ese indice"""
    contMina = 0
    if 0 < indice < tope:
        # si no estoy en la primera ni ultima celda, debo mirar a izq y derecha
        if cadena[indice - 1] == '*':
            # chequeo espacio anterior
            contMina = contMina + 1
        if cadena[indice + 1] == '*':
            # chequeo espacio siguiente
            contMina = contMina + 1
    elif indice == 0:
        # si es la primer celda, debo ver solo a derecha
        if cadena[indice + 1] == '*':
            contMina = contMina + 1
    else:
        # la unica opcion disjunta es que esté en el extremo derecho del string
        if cadena[indice - 1] == '*':
            contMina = contMina + 1
    return contMina

indice_elemento = 0
for elemento in minas:
    indice_celda = 0
    for celda in elemento:
        if celda != '*':
            # solo voy a poner un numero en donde no haya una mina
            contMina = 0
            # contador para la cantidad de minas alrededor de 1 punto
            contMina = contMina + chequearCeldasID(elemento, indice_celda, topeancho)
            if indice_elemento == 0:
                # si estoy en el primer renglon, solo debo mirar abajo
                contMina = contMina + chequearCeldasIxD(minas[indice_elemento + 1], indice_celda,topeancho)
            elif 0 < indice_elemento < topealto:
                # si estoy en un renglon que no es primero ni ultimo
                contMina = contMina + chequearCeldasIxD(minas[indice_elemento + 1], indice_celda,topeancho)
                contMina = contMina + chequearCeldasIxD(minas[indice_elemento - 1], indice_celda,topeancho)
            else:
                # la unica opcion que queda es que estoy en el ultimo string
                contMina = contMina + chequearCeldasIxD(minas[indice_elemento - 1], indice_celda,topeancho)
            minasNum[indice_elemento] = minasNum[indice_elemento] + str(contMina)
            # coloco el valor calculado de las minas que rodean la celda
        else:
            minasNum[indice_elemento] = minasNum[indice_elemento] + '*'
        indice_celda = indice_celda + 1
    indice_elemento = indice_elemento + 1
print(minasNum)

