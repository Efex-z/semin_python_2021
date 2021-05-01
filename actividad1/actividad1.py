import csv
import json
import PySimpleGUI as sg


# los datasets estan en:
# Vacunacion COVID19 por provincia:
# http://datos.salud.gob.ar/dataset/vacunas-contra-covid-19-dosis-aplicadas-en-la-republica-argentina

# Chocolates:
# https://www.kaggle.com/rtatman/chocolate-bar-ratings
#

def procesar_vacunas():
    """ abre el csv de las vacunas y procesa la informacion, mostrandola y guardandola en un json """
    # trato de salvar errores de no encontrar el archivo
    try:
        archivo = open("Covid19Arg.csv", "r")
    except FileNotFoundError:
        try:
            # pruebo con el nombre original del archivo como queda luego de descargarlo
            archivo = open("Covid19VacunasAgrupadas.csv")
        except FileNotFoundError:
            print("Intente renombrar el archivo de las vacunas de covid19 en Argentina a 'Covid19Arg.csv',"
                  "o colocar el archivo .csv en la misma carpeta en la que se encuentra el modulo .py")

    csvreader = csv.reader(archivo)
    print(next(csvreader))
    # ['jurisdiccion_codigo_indec', 'jurisdiccion_nombre', 'vacuna_nombre', 'primera_dosis_cantidad',
    # 'segunda_dosis_cantidad']
    # en este archivo hay informacion de varias vacunas diferentes para las mismas jurisdicciones, por lo que
    # se tomará la sumatoria de las vacunas para cada jurisdiccion

    # qué intento informar: las provincias con mejor relacion entre segundas dosis / primeras dosis de vacunas
    # por lo tanto, antes de procesarlo debo acumular los datos por nombre de provincia
    jurisdicciones = {}  # diccionario que va a tener {"jurisdiccion":[1dosis, 2dosis]}
    linea1 = next(csvreader)
    jur_actual = linea1[1]
    v1_actual = int(linea1[3])
    v2_actual = int(linea1[4])
    for linea in csvreader:
        # para apilar cantidad de dosis de vacunas por jurisdiccion
        if linea[1] == jur_actual:
            v1_actual = v1_actual + int(linea[3])  # sumo la dosis 1 (esta en string por eso el casteo a int)
            v2_actual = v2_actual + int(linea[4])  # sumo la dosis 2
            jurisdicciones.update({linea[1]: [v1_actual, v2_actual]})
        else:
            jur_actual = linea[1]
            v1_actual = int(linea[3])
            v2_actual = int(linea[4])
            jurisdicciones.update({linea[1]: [v1_actual, v2_actual]})

    # en este momento, en jurisdicciones tenemos un diccionario con clave "jurisdiccion" y valor una lista con
    # 2 elementos: total de primeras dosis administradas y total de segundas dosis administradas.
    # ahora queda procesar la informacion para realizar el filtro del maximo
    lis_radio = []
    for clave in jurisdicciones:
        v1, v2 = jurisdicciones[clave][0], jurisdicciones[clave][1]
        radio = (v2 * 100) / v1
        lis_radio.append((clave, radio))
    # en lis_radio tenemos finalmente los datos deseados por jurisdiccion: el radio de qué tantas aplicaciones de
    # segundas dosis de vacuna hay con respecto a las aplicaciones de primeras dosis anteriores.
    # esta en forma de tuplas

    # ahora vamos a poner los datos en una ventana y en el json

    lis_radio = sorted(lis_radio, key=lambda x: x[1],
                       reverse=True)  # en x[1] esta el valor numerico, por ese valor ordeno

    archivo_guardar = open("dato_vacunas.json", "w")
    datos = []
    for elemento in lis_radio[:15]:  # vamos a tomar los 15 mejores radios en provincias
        datos.append(elemento)
    json.dump(datos, archivo_guardar)
    archivo_guardar.close()

    layout = [
        [sg.Text(f"{'Las 15 provincias que más segundas dosis de vacunas contra COVID19':^90}")],
        [sg.Text(f"{' dieron en relación a la cantidad de primeras dosis dadas son:':^90}", pad=(0, 10))],
        [sg.Text(f"{datos[0][0]:^90}")],
        [sg.Text(f"{datos[1][0]:^90}")],
        [sg.Text(f"{datos[2][0]:^90}")],
        [sg.Text(f"{datos[3][0]:^90}")],
        [sg.Text(f"{datos[4][0]:^90}")],
        [sg.Text(f"{datos[5][0]:^90}")],
        [sg.Text(f"{datos[6][0]:^90}")],
        [sg.Text(f"{datos[7][0]:^90}")],
        [sg.Text(f"{datos[8][0]:^90}")],
        [sg.Text(f"{datos[9][0] :^90}")],
        [sg.Text(f"{datos[10][0]:^90}")],
        [sg.Text(f"{datos[11][0]:^90}")],
        [sg.Text(f"{datos[12][0]:^90}")],
        [sg.Text(f"{datos[13][0]:^90}")],
        [sg.Text(f"{datos[14][0]:^90}")],
        [sg.Button("Ok", key="-OK-", s=(35, 2), pad=(90, 5),)]
        ]
    window = sg.Window("Datos de vacunacion", layout)
    while True:
        event, values = window.read()
        if event == "-OK-" or event == sg.WINDOW_CLOSED:
            break
    window.close()


def procesar_chocolates():
    """ abre el csv de los chocolates y procesa la informacion, mostrandola y guardandola en un json """
    # trato de salvar errores de filenotfound
    import collections
    try:
        archivo = open("flavors_of_cacao.csv", "r")
    except FileNotFoundError:
        print("Intente renombrar el archivo de los chocolates a 'flavors_of_cacao.csv',"
              "o colocar el archivo .csv en la misma carpeta en la que se encuentra el modulo .py")

    # informare las 15 compañias cuyos chocolates tienen mayor puntaje (rating) entre especialistas
    csvreader = csv.reader(archivo)
    print(next(csvreader))
    # ['CompanyÂ\xa0\n(Maker-if known)', 'Specific Bean Origin\nor Bar Name', 'REF', 'Review\nDate', 'Cocoa\nPercent',
    # 'Company\nLocation', 'Rating', 'Bean\nType', 'Broad Bean\nOrigin']
    masricos = filter(lambda x: float(x[6]) >= 4.0, csvreader)
    # en masricos (filtro) tenemos aquellos chocolates que tienen un rating mayor a 4 ( el maximo es 5).
    lis_choco = []
    for linea in masricos:
        lis_choco.append((linea[0], float(linea[6])))  # el 1 es para que cuente una ocurrencia de ese elemento luego

    contador_nom, contador_rating, contador_final = collections.Counter(), collections.Counter(), collections.Counter()
    # se genera un contador que acumule la cantidad de veces que aparece una empresa
    # y otro que acumule el rating de todos sus chocolates, para luego sacar un promedio de rating por empresa
    for elemento in lis_choco:
        contador_nom.update({elemento[0]: 1})
        contador_rating.update({elemento[0]: elemento[1]})

    for x in range(len(contador_nom)):
        # para tener en un contador un conteo de (rating total / total de repeticiones de la misma empresa)
        aux = contador_nom.popitem()  # como voy a hacer pops constantes necesito un aux para no perder el elemento
        contador_final.update({aux[0]: float(contador_rating.popitem()[1] / aux[1])})

    datos = contador_final.most_common(15)

    # a guardar en el archivo
    archivo_guardar = open("mejoreschocolates.json", "w")
    json.dump(datos, archivo_guardar)
    archivo_guardar.close()

    # la ventana que mostrará estos datos
    layout = [[sg.Text(f"{'Las 15 empresas de chocolates con mejores ratings':^90}")],
              [sg.Text(f"{'según los especialistas, son: ':^90}", pad=(0, 10))],
              [sg.Text(f"{datos[0][0]:^90}")],
              [sg.Text(f"{datos[1][0]:^90}")],
              [sg.Text(f"{datos[2][0]:^90}")],
              [sg.Text(f"{datos[3][0]:^90}")],
              [sg.Text(f"{datos[4][0]:^90}")],
              [sg.Text(f"{datos[5][0]:^90}")],
              [sg.Text(f"{datos[6][0]:^90}")],
              [sg.Text(f"{datos[7][0]:^90}")],
              [sg.Text(f"{datos[8][0]:^90}")],
              [sg.Text(f"{datos[9][0]:^90}")],
              [sg.Text(f"{datos[10][0]:^90}")],
              [sg.Text(f"{datos[11][0]:^90}")],
              [sg.Text(f"{datos[12][0]:^90}")],
              [sg.Text(f"{datos[13][0]:^90}")],
              [sg.Text(f"{datos[14][0]:^90}")],
              [sg.Button("Ok", key="-OK-", s=(35, 2), pad=(90, 5))]
              ]
    window = sg.Window("Datos de chocolates!", layout)
    while True:
        event, values = window.read()
        if event == "-OK-" or event == sg.WINDOW_CLOSED:
            break
    window.close()


def menuppal():
    """ genera un popup con 2 botones para procesar archivos csv, y un boton para salir
     la x no cierra la ventana """
    sg.theme("DarkGrey2")

    layout = [[sg.Text(f"{'¿Qué datos vamos a analizar?':^45}", text_color="yellow", font=("bold", 18))],
              [sg.Button("Vacunas COVID19 en Argentina", key="-VACUNAS-", s=(35, 3), pad=((90, 90), (2, 20)))],
              [sg.Button(" ¡Chocolates en el mundo! ", key="-CHOCOLATES-", s=(35, 3), pad=((90, 90), (2, 50)))],
              [sg.Button("SALIR", key="-SALIR-",  s=(35, 3), pad=((90, 90), (2, 2)))]]

    window = sg.Window("Actividad 1 x python plus Fede Morlan - TEORIA -", layout, disable_close=True)

    while True:
        event, values = window.read()
        if event == "-VACUNAS-":
            window.hide()
            procesar_vacunas()
            window.un_hide()
        elif event == "-CHOCOLATES-":
            window.hide()
            procesar_chocolates()
            window.un_hide()
        elif event == "-SALIR-":
            window.close()
            break


menuppal()
