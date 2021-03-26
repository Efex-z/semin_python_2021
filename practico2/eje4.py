"""
Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
parte de una palabra ingresada

[ ]: cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣
,→contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
cant = 0
for car in cadena:
    if car == "@" or car == "!":
        cant = cant + 1
if cant >= 1:
    print("Ingresaste alguno de estos símbolos: @ o !" )
else:
    print("Ingreoo OK")

Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@
y !):@@ggg@@!!!
Ingresaste alguno de estos símbolos: @ o !
¿Cómo podemos simplificarlo?
"""
cadena = input('Ingresar una clave (hasta 10 caracteres y sin "@" o "!"): ')
termine = False
while not termine:
    if len(cadena) > 10:
        print('HASTA 10 caracteres.')
        cadena = input('Ingresar una clave (hasta 10 caracteres y sin "@" o "!"): ')
    elif "@" in cadena or "!" in cadena:
        print('Ingresaste @ o !.')
        cadena = input('Ingresar una clave (hasta 10 caracteres y sin "@" o "!"): ')
    else:
        termine = True
