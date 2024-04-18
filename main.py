'''
1. choice para elegir al azar una palabra
    - words: [muchas palabras]
2. Funciones:
    - elegir letra
    - si dicha letra es válida
    - check si la letra está en la palabra
    - check si ha ganado
'''
import random

words = ['gato', 'perro', 'python', 'conejo', 'antropología', 'murcielago']
letter_guessed = []
letter_miss = []
trys = 6
success = 0
end_game= False

def random_word(words):
    word_random = random.choice(words)
    word_length = len(set(word_random))

    return word_random, word_length


def user_letter():
    letter_chosen= ''
    is_ok = False
    abc = 'abcdefghijklmnñopqrstuvwxyz'

    while not is_ok:
        letter_chosen = input("Elige una letra: ")
        if letter_chosen in abc and len(letter_chosen) == 1:
            is_ok: True
        else:
            print("No es una letra válida 😡")

    return letter_chosen


def new_board(letter_chosen): #se renueva tras cada intento/letra introducida
    
    hidden_list = [] #todo --------------------------------------- MIRAR
    
    for l in letter_chosen:
        if l in letter_chosen:
            hidden_list.append(l)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list)) #join: añade un espacio entre letras

def check_letter(letter_chosen, hidden_list, trys, coincidence):
    
    end = False

    if letter_chosen in hidden_list and letter_chosen not in letter_guessed:
        letter_guessed.append(letter_chosen)
        coincidence += 1
    elif letter_chosen in hidden_list and letter_chosen in letter_guessed:
        print("Ya has intentado con esta letra, prueba con otra 😁")
    else:
        letter_miss.append(hidden_list)
        trys -= 1
    
    if trys == 0:
        end = lose()
    elif coincidence == word_length:
        end = win(hidden_list)

    return trys, end, coincidence

def lose(): 
    print("Perdiste, ya no tienes vidas ")
    print('La palabra era' + word)

    return True

def win(word_found):
    new_board(word_found)
    print("Ganaste!! 🪅🎉")

    return True


word, word_length = random_word(words)

while not end_game:
    print('\n'+ '👾' * 20 + '\n')
    new_board(word)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letter_miss))
    print(f'Vidas: {trys}')
    print('\n'+ '👾' * 20 + '\n')
    letter = user_letter()

    trys, ended, coincidence = check_letter(word, letter, trys, coincidence)

    end_game= ended
