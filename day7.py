# hangman
import os
import random

lives = -1


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def image_handeler():
    global lives
    if lives ==4:
        print(HANGMANPICS[0])

def call_Guess():
    print("Guess a single letter (a-z): ")
    w = input()
    w = w.lower()
    return w


def find_match():
    flag = 0
    for i in range(0, len(word)):
        if w == word[i] and guess[i]=='_':
            guess[i] = word[i]
            print("Well done Guess the next letter for")
            print(''.join(guess))
            flag = 1
            break
    if flag == 0:
        global lives
        lives = lives + 1
        print(''.join(guess))
        print(HANGMANPICS[lives])
        print(f"Wrong answer! {6 - lives} chances left")



print('''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  |
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
''')

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

single_word = random.choice(words)


print("Do you want to Challange a person or Play the game right away?")
print("1. Play \n2.Challange")
option = input()


if option == '2':
    single_word = input("Input Your word: ").lower()
    os.system('cls')


print("Welcome to the game hangman")


word = []
guess = []

for word_word in single_word:
    word.append(word_word)
    guess.append('_')



while word != guess and lives !=6:
    w = call_Guess()
    os.system('cls')
    find_match()



if lives == 6:
    print("Game over")
    print(f"Right answer was [{''.join(word)}] \n Better luck next time")
else:
    print("You win!!!")



