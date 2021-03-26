"""
5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras,
y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir
entre mayúsculas y minúsculas
"""
frase = input('Ingresar una frase: ')
cadena = input('Ingresar un string: ')
for caracter in frase:
    if not caracter.isalpha():
        frase = frase.replace(caracter, ' ')
contador = 0
for elemento in frase.split():
    if elemento.lower().startswith(cadena.lower()):
        contador = contador + 1
print(f'Palabra: {cadena} ; Resultado: {contador}.')
