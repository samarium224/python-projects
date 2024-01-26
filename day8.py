
#Ceaser Cipher
import string
alphabet = list(string.ascii_lowercase)

def cipher(text, shift_amount, direction):
    cipher_text = ""
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                new_position = position + shift_amount
                if new_position > 25:
                    new_position = new_position - 25
            if direction == 'decode':
                new_position = position - shift_amount
                if new_position < 0:
                    new_position = new_position + 25
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char

    print(f"The encoded text is {cipher_text}")



start = True
print('''
                                        _       _
                                       (_)     | |
   ___ __ _  ___  ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __
  / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |
  \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|
                                         | |
                                         |_|
''')
while start:
    direction = input("Type 'encode' to encrypt type 'decode' to decrypt or x to close: \n")

    if direction == 'encode':
        print('''
    ███████ ███    ██  ██████  ██████  ██████  ███████     ███    ███  ██████  ██████  ███████
    ██      ████   ██ ██      ██    ██ ██   ██ ██          ████  ████ ██    ██ ██   ██ ██
    █████   ██ ██  ██ ██      ██    ██ ██   ██ █████       ██ ████ ██ ██    ██ ██   ██ █████
    ██      ██  ██ ██ ██      ██    ██ ██   ██ ██          ██  ██  ██ ██    ██ ██   ██ ██
    ███████ ██   ████  ██████  ██████  ██████  ███████     ██      ██  ██████  ██████  ███████

        ''')

    elif direction == 'decode':
        print('''
    _
    | \  _   _  _   _|  _    ._ _   _   _|  _
    |_/ (/_ (_ (_) (_| (/_   | | | (_) (_| (/_


        ''')

    elif direction == 'x':
        print("Good bye")
        start = False
        break

    else:
        print("invalid option")
        continue

    input_text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(text=input_text,shift_amount=shift, direction= direction)


