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
#for elemento in lista_gratuitos_espanol:
#    print(elemento)
# nota: lo deje comentado para no imprimir todo (lleva tiempo porque son muchos) y poder testear la segunda consigna
print()
# fin de desafio 1 -----------------------------------------------------------------------------------------------

contador = collections.Counter()
mejorpuntaje = []
for linea in csvreader:
    contador.update(linea)

# no llego a pensar como filtrar primero los elementos que tengan mas user rating count


print(contador.most_common(10))
