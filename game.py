import random
                                                # Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]
                                                # Lista de letras con acento
letters_with_accent_mark = ('á', 'é', 'í', 'ó', 'ú')
                                                # Elegir una palabra al azar
secret_word = random.choice(words)
                                                # Número máximo de intentos permitidos
max_attempts = 10
                                                # Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
                                                # Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
for i in range(max_attempts):
                                                # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
                                               # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
                                                # Verificar que el caracter sea una letra valida
    if  (not(letter in letters_with_accent_mark)) and (letter < 'a' or letter > 'z'):
        print("El caracter ingresado no es una letra. Intente nuevamente")
        continue
                                                # Agregar la letra a la lista de letras adivinadas
                                                #Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique el cambio.
    guessed_letters.append(letter)
                                                # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
                                                # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
                                                # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
        print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
        print(f"La palabra secreta era: {secret_word}")