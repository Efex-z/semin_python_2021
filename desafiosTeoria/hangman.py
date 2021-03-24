import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
# ------------- cambio: traduccion a castellano -----------------------------------------------------------------------------
words = {'Colores': 'rojo naranja amarillo verde azul indigo violeta blanco negro marron'.split(),
         # NOTA: el string.split hace que se convierta el string a una lista, separando elementos por cada espacio en el string.
         'Formas': 'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentagono hexagono heptagono octagono'.split(),
         'Frutas': 'manzana naranja limon lima pera melon uva pomelo cereza banana mango frutilla cereza durazno tomate'.split(),
         # elimine cantalope porque no sé que es
         'Animales': 'murcielago oso castor gato jaguar cangrejo ciervo perro burro pato aguila pez rana cabra leon cocodrilo mono alce raton nutria buho panda piton conejo rata tiburon oveja zorro calamar tigre pavo tortuga comadreja ballena lobo zebra'.split()}
# NOTA: words es un diccionario cuyas claves son "colors, shapes, fruits y animals", y sus valores son listas de palabras.

# ------- mi pista va a ser cuantas silabas tiene la palabra. como no lo puedo determinar desde el string lo hago manual ------
# cada cantidad de silabas corresponde en indice con la palabra del diccionario words, para que lo pueda buscar con esos mismos indices.
wordSyl = {'Colores': '2 3 4 2 2 3 3 2 2 2'.split(),
            'Formas': '3 4 3 3 2 4 2 4 4 4 4'.split(),
            'Frutas': '3 3 2 2 2 2 2 3 3 3 2 3 3 3 3'.split(),
            'Animales': '4 2 2 2 2 3 2 2 2 2 3 1 2 2 2 4 2 2 2 2 2 2 2 3 2 3 3 2 3 2 2 3 4 3 2 2'.split()}

def getRandomWord(wordDict):
    ''' This function returns a random string from the passed dictionary of lists of strings, and the key also.
    Tambien ahora devuelve la cantidad de silabas de la palabra'''
    # NOTA: devuelve lo mencionado en ese orden. wordDict[clave][indice] accede a un VALOR (de esa clave en ese indice).

    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey, wordSyl[wordKey][wordIndex]]

def displayBoard(missedLetters, correctLetters, secretWord, secretSyl):
    # missedLetters:    string con las letras correctas en orden de aparicion
    # correctLetters:   string con las letras incorrectas en orden de aparicion
    # secretWord:    string de la palabra a adivinar
    # AGREGADO: secretSyl: contiene la cantidad de silabas de la palabra

    print(HANGMAN_PICS[len(missedLetters)])
    # NOTA: HANGMAN PICS es una lista de strings que conforman cada uno un dibujo COMPLETO del ahorcado
    # por cada letra no adivinada, corresponde un elemento de la lista de dibujos que está armada en orden, de menos a mas completo
    print()

    print('Missed letters:', end=' ')  # el end= ' ' hace que lo siguiente esté en la misma linea
    for letter in missedLetters:
        print(letter, end=' ')
    print()  # print línea para que lo siguiente este aparte

    # ------------ NUEVO CODIGO: pista de sílabas ------------
    # da una pista de silabas solo cuando fallamos 3 intentos (no hace falta darla todo_ el tiempo ya que es siempre igual
    if len(missedLetters) == 3:
        print(f'Pista: la palabra secreta tiene {secretSyl} silabas. ')


    blanks = '_' * len(secretWord)
    # NOTA:  TODOS los espacios en blanco uno por cada letra (por eso len) estan en "blanks"

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
            # NOTA: blanco antes de la letra + la letra adivinada + blanco luego de la letra
            # en cada pasada del for, como se reemplaza el valor de "blanks", en la proxima pasada blanks ya contiene
            # la letra adivinada revelada

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Adivina una letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor ingresa UNA sola letra.')
        elif guess in alreadyGuessed:
            print('Ya adivinaste esa letra. Por favor, ingresa otra.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Queres volver a jugar? (si o no)')
    return input().lower().startswith('s')


print('A H O R C A D O')

difficulty = 'X'
while difficulty not in 'FMD':
    print('Ingresar dificultad: F - Facil, M - Medio, D - Dificil')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    # del elimina por índice un elemento de lista, o por slice [i:i2]
    del HANGMAN_PICS[7]
if difficulty == 'D':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet, secretSyl = getRandomWord(words)
#NOTA: hay una asignacion doble porque la funcion llamada devuelve 2 strings (primero la palabra, luego la clave de esa palabra)
gameIsDone = False

while True: #while true ejecuta siempre el while
    print('La palabra secreta esta en el conjunto: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord, secretSyl)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        #NOTA: correctLetters tiene las letras adivinadas correctas en orden en un string

        # Check if the player has won
        foundAllLetters = True
        # me pregunto si habrá una forma de no tener que establecer constantemente el valor de foundAllLetters
        # ya que es un valor que se matiene durante todo_ el juego salvo al final
        # por ejemplo: establecerlo por fuera del while como FALSE al principio del programa
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Si! la palabra secreta es "' + secretWord + '", Ganaste!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord, secretSyl)
            print('Te quedaste sin intentos!\nLuego de ' + str(len(missedLetters)) + ' intentos fallidos y ' + str(
                len(correctLetters)) + ' letras correctas, la palabra era "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet, secretSyl = getRandomWord(words)
        else:
            break
