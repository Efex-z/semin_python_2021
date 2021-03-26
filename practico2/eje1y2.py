"""
1: tomando el texto del readme.md de numpy, imprime todas las lineas que contienen 'http' o 'https'
2: indica la palabra que aparece mayor cantidad de veces en el texto readme de numpy.
"""

texto = """
NumPy is the fundamental package needed for scientific computing with Python.

- **Website:** https://www.numpy.org
- **Documentation:** https://numpy.org/doc
- **Mailing list:** https://mail.python.org/mailman/listinfo/numpy-discussion
- **Source code:** https://github.com/numpy/numpy
- **Contributing:** https://www.numpy.org/devdocs/dev/index.html
- **Bug reports:** https://github.com/numpy/numpy/issues
- **Report a security vulnerability:** https://tidelift.com/docs/security

It provides:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires `pytest`.  Tests can then be run after installation with:

    python -c 'import numpy; numpy.test()'


Call for Contributions
----------------------

The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good
first issue" may be a good starting point. If you are considering larger
contributions to the source code, please contact us through the [mailing
list](https://mail.python.org/mailman/listinfo/numpy-discussion) first. 

Writing code isn’t the only way to contribute to NumPy. You can also: 
- review pull requests
- triage issues
- develop tutorials, presentations, and other educational materials
- maintain and improve [our website](https://github.com/numpy/numpy.org)
- develop graphic design for our brand assets and promotional materials
- translate website content
- help with outreach and onboard new contributors
- write grant proposals and help with other fundraising efforts

If you’re unsure where to start or how your skills fit in, reach out! You can
ask on the mailing list or here, on GitHub, by opening a new issue or leaving a
comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to
speak to us in private first, contact our community coordinators at
numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for
an invite).

We also have a biweekly community call, details of which are announced on the
mailing list. You are very welcome to join. 

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved.

"""
#   ejercicio1
for linea in texto.split("\n"):
    if ('http' or 'https') in linea.lower():
        # al hacer el lower en este paso, no modifico el texto en sí, ya que afecto
        # otra variable que es la que se compara, no la variable "linea" original
        print(linea)

#   ejercicio2

# SOLUCION 1: lo primero que me salio

dicc = {}
#   en este diccionario se guardaran todas las palabras como keys y sus
#   valores serán la cantidad de veces que aparece esa palabra en total

for elemento in texto.lower().split():
    # paso el texto a minuscula porque no pretendo distinguir la misma palabra en mayus
    for caracter in elemento:
        if not caracter.isalpha():
            elemento = elemento.replace(caracter, ' ')
            # discrimino cualquier simbolo que no sea letra del string,
    elemento = elemento.split()
    # separo ese string en los espacios que creó el reemplazo
    # algunos elementos serán listas, por lo que debo meterme en cada una de ellas:
    if type(elemento) == list:
        for subelemento in elemento:
            if subelemento not in dicc:
                dicc[subelemento] = 1
                # si el string no estaba en el diccionario, lo agrego
            else:
                dicc[subelemento] = dicc[subelemento] + 1
                # si ya estaba, sumo al contador (el valor de esa clave string)
    else:
        # trabajo directamente con el string
        if elemento not in dicc:
            dicc[elemento] = 1
        else:
            dicc[elemento] = dicc[elemento] + 1


def maximoDic(diccionario):
    max = -1
    claveMax = ''
    for clave in diccionario:
        if diccionario.get(clave) > max:
            max = diccionario.get(clave)
            claveMax = clave
    return (claveMax, max)


claveMax, apariciones = maximoDic(dicc)
print( "ejercicio 2:")
print(
    f'La palabra {claveMax} es la que aparece más veces en el texto, con {apariciones} apariciones')

# SOLUCION 2: primero despejo el texto y luego trabajo con la lista
dicc2 = {}
for car in texto:
    if not car.isalpha():
        texto = texto.replace(car, ' ')

for elemento in texto.lower().split():
    if elemento not in dicc2:
        dicc2[elemento] = 1
    else:
        dicc2[elemento] = dicc2[elemento] + 1

claveMax, apariciones = maximoDic(dicc)
print( "ejercicio 2:")
print(
    f'La palabra {claveMax} es la que aparece más veces en el texto, con {apariciones} apariciones')