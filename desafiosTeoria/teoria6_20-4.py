import csv
import collections

# desafio 1 ----------------------------------------------------------------------------------------------------
archivo = open('appstore_games.csv', "r", encoding='utf-8')
csvreader = csv.reader(archivo, delimiter=',')

print(next(csvreader)) # solo para saber el formato:

# ['URL', 'ID', 'Name', 'Subtitle', 'Icon URL', 'Average User Rating', 'User Rating Count', 'Price',
# 'In-app Purchases', 'Description', 'Developer', 'Age Rating', 'Languages', 'Size', 'Primary Genre', 'Genres',
# 'Original Release Date', 'Current Version Release Date']

lista_gratuitos_espanol = filter(lambda x: (x[7] == '0') and 'ES' in x[12], csvreader)
print('Juegos gratuitos en español: ')
for elemento in lista_gratuitos_espanol:
   print(elemento)
print()
# fin de desafio 1 -----------------------------------------------------------------------------------------------
# nota: lo que está arriba lo agregue antes de las 11. lo que sigue a continuacion lo tuve que rehacer:

contador = collections.Counter()
juegos = {} # vamos a hacer un diccionario que contenga como clave los juegos y como valor el puntaje

for linea in csvreader:
    if linea[6] != '':
        juegos.update({linea[2]: int(linea[6])})
contador.update(juegos)
# pongo en el contador todos los datos del diccionario (por esto los castee a int, para poder ordenarlos por ocurrencia)
# imprimiendo entonces los 10 primeros del contador, automaticamente ya tengo lo solicitado.
print (contador.most_common(10))

