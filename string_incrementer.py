import re
import keyboard

def increment_string(word: str) -> None:
    regex = r'\d'  # Verificando com RE

    number = re.search(regex, word)
        
    if number:  # Checando se é um número      
        number_in_word = int(number.group())  #Convertendo para inteiro
        print("The string ends with the number:", number_in_word)
        incremented_number = number_in_word + 1
        return print(f"The new word: {re.sub(regex, str(incremented_number), word)}")
    else:
        return print("The string does not end with a number.")

word: str = input('Enter a word that may or may not have a number at the end. If it does, it will be incremented by 1: ')

# Verificando se foi adicionado algum espaço.
if ' ' in word:
    keyboard.is_pressed('space')
    print("You pressed the spacebar! The program will be terminated.")
else:
    increment_string(word)
