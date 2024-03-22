import random
import difficulties


def main():                                                 
    words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]  # Lista de palabras posibles
    chosen_difficultiy = int(input( "~~~~~~~~~Menú~~~~~~~~~~ \n 1) Jugar en Facil \n 2) Jugar en Normal \n 3) Jugar en Dificil \n 4) Cerrar el juego \n " ))

    while True:
        match chosen_difficultiy:
            case 1:
                secret_word = random.choice(words) # Elegir una palabra al azar
                difficulties.easy_mode(secret_word)                                            
            case 2:
                secret_word = random.choice(words) # Elegir una palabra al azar
                difficulties.normal_mode(secret_word)
            case 3:
                secret_word = random.choice(words) # Elegir una palabra al azar
                difficulties.hard_mode(secret_word)
            case 4:
                print("Gracias por jugar nuestro juego :)")
                break
            case _:
                print("Por favor ingrese una opcion valida!!!!!")
        chosen_difficultiy = int(input( "~~~~~~~~~Menú~~~~~~~~~~ \n 1) Jugar en Facil \n 2) Jugar en Normal \n 3) Jugar en Dificil \n 4) Cerrar el juego \n " ))


main()