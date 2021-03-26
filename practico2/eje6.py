""" 6. Dada una frase donde las palabras pueden estar repetidas e indistintamente
en mayúsculas y minúsculas, imprimir una lista con todas las palabras sin repetir
y en letra minúscula.
"""
frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
# RESUELTO CON LISTA porque todavía no se vio en clase el set.
for caracter in frase:
    # recorre toda la frase eliminando simbolos que no sean letras
    if not caracter.isalpha():
        frase = frase.replace(caracter, ' ')
lista_frase = frase.lower().split()
# ya bajo a minusculas porque el resultado se imprimira en minuscula
lista_compacta = []
for x in lista_frase:
    if x not in lista_compacta:
        lista_compacta.append(x)
    # solo crea entradas nuevas en el diccionario si la clave no existía
print(lista_compacta)