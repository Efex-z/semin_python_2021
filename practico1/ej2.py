#----------- primer desafío ----------------
#lee un numero y determina si es par o impar
num = int(input("ingresa un número: "))
if (num%2 == 0):
    print("es par")
else:
    print("NO es par")

#--------------segundo desafío ------------------------
#lee un numero de teclado e imprime si es multiplo de 2, 3 o 5.
#terminé no utilizando elif porque puede ser multiplo de 2 y 5 ó 3 y 5.
num = int(input("ingresa un número más: "))
if (num%2 == 0):
    print("es múltiplo de 2. ")
#puede ser multiplo de 2 y de 5.
if (num%5 == 0):
    print("es múltiplo de 5. ")
#puede ser multiplo de 3 y de 5.
if (num%3 == 0):
    print("es múltiplo de 3. ")
else:
    print("no es múltiplo ni de 2, ni de 3 ni de 5.") 

#--------------tercer desafío -------------------------
#dado una letra ingresada imprime si es mayuscula o minuscula
char = input("Ingresar una letra: ")
if (char >= "A") and (char <= "Z"):
    print("Es mayúscula")
elif (char >= "a") and (char <= "z"):
    print("Es minúscula")
else:
    print("No es una letra!")

#-------------cuarto desafío --------------------------
#imprime si un caracter ingresado es una comilla o no.
char = input("Ingresar un caracter: ")
#envuelvo el caracter de comilla con comillas diferentes (como alternativa a escapatoria con barra invertida)
if (char == "'") or (char == '"'):
    print("es una comilla.")
else:
    print("no es una comilla.")

#-------------quinto desafío ----------------------------
#dadas dos cadenas ingresadas por teclado, imprime la mas larga
str1 = input("Ingresar una cadena de texto: ")
str2 = input("Ingresar otra cadena de texto: ")
if (len(str1) > len(str2)):
    print(str1)
elif (len(str1) < len(str2)):
    print(str2)
else:
    print("las dos cadenas ingresadas tienen igual longitud.")


#-------------sexto desafio -------------------------------
#imprime cuantas letras "a" contiene una cadena de caracteres
str1 = input("Ingresar una nueva cadena de texto: ")
total_a = 0
for c in str1:
    if c == "a":
        total_a = total_a + 1

print ("la cadena tiene "+ str(total_a) +" letras 'a'.")
