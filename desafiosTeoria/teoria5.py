import csv
import json

archivo = open("netflix_titles.csv", "r", encoding='utf-8')
csvreader = csv.reader(archivo, delimiter=',')

# para saber cómo está organizado el archivo.
print(next(csvreader))
# ['show_id', 'type', 'title', 'director',
# 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']


# ------------- CONSIGNA 1 -----------------------------------------------------------------
# queremos guardar en otro archivo las peliculas agregadas en 2020 (date_added: 6; type: 1)
archivo_nuevo = open("netflix_agregados2020.json", "w", encoding='utf-8')

# quiero saber como acceder al campo para filtrar por año "2020"
print(type(next(csvreader)[6]))  # es un string
print(next(csvreader)[6])  # ejemplo: August 14, 2020
# como esta separado por coma, puedo aprovechar esto para discriminar solo el año
anio_solo = next(csvreader)[6].split(',')
print(anio_solo[1].strip())

shows_2020 = filter(lambda x: x[1] == "Movie" and x[6].split(',')[1].strip() == "2020", csvreader)
# en la lista "datos" voy a guardar lo que tenga que poner en el json
datos = []
for elem in shows_2020:
    print(f"{elem[2]:<40} {elem[6]}")  # sólo para comprobar que ande bien

    # la lista de "datos", contendra UN diccionario POR CADA ELEMENTO que quiero agregar
    # en el que cada campo corresponde a un valor. La clave la obtuve sabiendo cómo esta organizado el archivo csv
    # no incluyo el "tipo" porque ya sabemos que son todas peliculas;
    # y de la fecha de agregado excluyo el año que ya sé que es "2020"
    datos.append({"show_id": f"{elem[0]}", "titulo": f"{elem[2]}", "director": f"{elem[3]}", "casting": f"{elem[4]}",
                  "pais": f"{elem[5]}", "agregado en": f"{elem[6].split(',')[0]}", "lanzamiento": f"{elem[7]}",
                  "rating": f"{elem[8]}", "duracion": f"{elem[9]}", "listado en": f"{elem[10]}", "descripcion": f"{elem[11]}"})

json.dump(datos, archivo_nuevo)
archivo_nuevo.close()
archivo.close()
# FIN DE LA CONSIGNA 1 -------------------------------------------------------------------------------------------------
archivo = open("netflix_titles.csv", "r", encoding='utf-8')
csvreader = csv.reader(archivo, delimiter=',')

# CONSIGNA 2:
# los cinco (5) países con más producciones en Netflix.
# puedo hacer un diccionario con clave entero y valor "pais", luego ordenarlo e imprimir los 5 mayores
# un collections.counter() sirve para acumular valores. En este caso, automaticamente las CLAVES son los paises y los
# VALORES son las ocurrencias.

import collections

coleccion = collections.Counter()

for linea in csvreader:
    pais = linea[5]
    # ojo: si pongo coleccion.update(pais), me acumula las letras. tengo que acumular una ocurrencia
    # de cada String completo, por ello debo especificar que al diccionario que crea el collections.counter() le
    # agrego la clave "variable pais" : 1 para agregar el string completo como una ocurrencia.
    coleccion.update({pais: 1})

print(coleccion) # coleccion completa, ya esta ordenada
print('5 paises con mas cantidad de peliculas en netflix: ')
# hay una funcion que ayuda a imprimir aquellas claves cuyos valores son mas altos
print(coleccion.most_common(5))



archivo.close()

