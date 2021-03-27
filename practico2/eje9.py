while True:
    palabra = input('Ingresar una palabra o frase: ')
    listaLetras = []
    for letra in palabra:
        if not letra.isalpha():
            palabra = palabra.replace(letra, '')
        else:
            if letra not in listaLetras:
                listaLetras.append(letra)
    if len(palabra) == len(listaLetras):
        print('Se ingresó un heterograma')
    else:
        print('No se ingresó un heterograma')
    opcion = input('Se desea seguir operando? (s/n): ')
    if opcion == "n":
        break


