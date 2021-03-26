"""
dado un texto solicita por teclado una letra e imprime las palabras que comienzan con
dicha letra. Si no se ingresa una letra, indica error
"""
import string

texto = """
Vuelvo a casa,
después de haber andado tanto,
después de haber querido el mundo a mis pies,
vuelvo a anclar en mi lugar.

Vuelvo a casa,
sin tantos delirios de grandeza,
habiendo masticado la miseria,
vuelvo a anclar en mi lugar.

Y el grito desesperado
por buscar mi identidad,
lejos de aquí, quedó atrás.
Y en mis manos
sólo traigo dedos,
y en el alma ganas de cantar.

Y el grito desesperado
por buscar mi identidad,
lejos de aquí, quedó atrás.
Y en mis manos
sólo traigo dedos,
y en el alma ganas de cantar.

Y hoy vuelvo a casa,
después de haber andado tanto,
después de haber querido el mundo a mis pies,
vuelvo a anclar en mi lugar.
Vuelvo a anclar en mi lugar.
Hoy vuelvo a anclar en mi lugar.
"""
letra = input('Ingresar una letra: ')
condicion = False

while not condicion:
    if len(letra) > 1:
        letra = (input('Ingresar UNA letra'))
    elif letra not in string.ascii_letters:
        #   para usar el modulo
        letra = (input('Ingresar una LETRA'))
    else:
        condicion = True

# como solo importa con qué comienza el string, no hace falta separarle las comas o puntos.
# en este string en particular ninguna palabra comienza con un simbolo.
listaPalabras = []
for caracter in texto:
    if caracter not in "áÁéÉíÍóÓúÚ" and caracter not in string.ascii_letters:
        # ascii_letters no considera tildes!
        texto = texto.replace(caracter, ' ')
        # limpio todo_ el texto de símbolos no deseados

for elemento in texto.split():
    if elemento.lower().startswith(letra.lower()) and elemento.lower() not in listaPalabras:
        # para no imprimir más de una vez
        print(elemento)
        listaPalabras.append(elemento.lower())
