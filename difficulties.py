letters_with_accent_mark = ('á', 'é', 'í', 'ó', 'ú')
max_fails = 10

def display_word(secret_word, guessed_letters):
    letters = []                                           # Mostrarla palabra parcialmente adivinada
    for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
    word_displayed = "".join(letters)
    return word_displayed

def verify_error(letter, guessed_letters):
                                                # Verificar si la letra ya fue ingresada anteriormente
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        return True
                                                # Verificar que el caracter sea una letra valida
    if  (not(letter in letters_with_accent_mark)) and (letter < 'a' or letter > 'z'):
        print("El caracter ingresado no es una letra. Intente nuevamente")
        return True
                                                # Verificar que se ingresa una sola letra
    if len(letter) > 1:
        print("Por favor ingrese una letra sola.")
        return True
    return False

def easy_mode(secret_word):
    fails_counter = 0
                                                # Lista para almacenar las letras adivinadas
    guessed_letters = ['a','e','i','o','u','á', 'é', 'í', 'ó', 'ú']
    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
    word_displayed = "_" * len(secret_word)

    print(f"Palabra: {display_word(secret_word, guessed_letters)}")
                                          # Mostrarla palabra parcialmente adivinada
    while max_fails > fails_counter:
                                                # Pedir al jugador que ingrese una letra
        letter = input("Ingresa una letra: ").lower()
                                               # Verificar posibles errores cuando se ingresa una letra
        if verify_error(letter, guessed_letters):
            fails_counter += 1
            print(f"Te quedan {max_fails - fails_counter} errores.")
            continue
                                                # Agregar la letra a la lista de letras adivinadas
                                                #Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique el cambio.
        guessed_letters.append(letter)
                                                # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            fails_counter += 1
            print(f"Te quedan {max_fails - fails_counter} errores.")
                                                # Mostrar la palabra parcialmente adivinada
        displayed_word = display_word(secret_word, guessed_letters)
        print(displayed_word)
                                                # Verificar si se ha adivinado la palabra completa
        if displayed_word == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
            break
    else:
        print(f"¡Oh no! Has agotado tus {max_fails} errores posibles.")
        print(f"La palabra secreta era: {secret_word}")

def normal_mode(secret_word):
    fails_counter = 0
                                                # Lista para almacenar las letras adivinadas
    guessed_letters = [secret_word[0], secret_word[-1]]
    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
    word_displayed = "_" * len(secret_word)

    word_displayed = word_displayed[:0] + secret_word[0] + word_displayed[1:]
    word_displayed = word_displayed[:-1] + secret_word[-1]
    print(f"Palabra: {word_displayed}")

    while max_fails > fails_counter:
                                                # Pedir al jugador que ingrese una letra
        letter = input("Ingresa una letra: ").lower()
                                               # Verificar posibles errores cuando se ingresa una letra
        if verify_error(letter, guessed_letters):
            fails_counter += 1
            print(f"Te quedan {max_fails - fails_counter} errores.")
            continue
                                                # Agregar la letra a la lista de letras adivinadas
                                                #Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique el cambio.
        guessed_letters.append(letter)
                                                # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            fails_counter += 1
            print(f"Te quedan {max_fails - fails_counter} errores.")
                                                # Mostrar la palabra parcialmente adivinada           
        displayed_word = display_word(secret_word, guessed_letters)
        print(displayed_word)
                                                # Verificar si se ha adivinado la palabra completa
        if displayed_word == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
            break
    else:
        print(f"¡Oh no! Has agotado tus {max_fails} errores posibles.")
        print(f"La palabra secreta era: {secret_word}")

def hard_mode(secret_word):
    fails_counter = 0
    guessed_letters = []
    word_displayed = "_" * len(secret_word)
    print(f"Palabra: {word_displayed}")
    while max_fails > fails_counter:
                                                # Pedir al jugador que ingrese una letra
        letter = input("Ingresa una letra: ").lower()
                                               # Verificar posibles errores cuando se ingresa una letra
        if verify_error(letter, guessed_letters):
            fails_counter += 1
            print(f"Te quedan {max_fails - fails_counter} errores.")
            continue
                                                # Agregar la letra a la lista de letras adivinadas
                                                #Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique el cambio.
        guessed_letters.append(letter)
                                                # Verificar si la letra está en la palabra secreta
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            fails_counter += 1
            print(f"Te quedan {max_fails - fails_counter} errores.")
                                                # Mostrar la palabra parcialmente adivinada
        displayed_word = display_word(secret_word, guessed_letters)
        print(displayed_word)
                                                # Verificar si se ha adivinado la palabra completa
        if displayed_word == secret_word:
            print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
            break
    else:
        print(f"¡Oh no! Has agotado tus {max_fails} errores posibles.")
        print(f"La palabra secreta era: {secret_word}")
                                           # Lista para almacenar las letras adivinadas

if __name__ == "__main__":
    easy_mode("murcielago")
    normal_mode("programando")
    hard_mode("grabación")