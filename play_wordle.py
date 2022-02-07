from random import random
from typing import List
from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
import random

def main():

    wordset = load_word_set("data/wordle_words.txt")
    print('Hello')
    secret = random.choice(list(wordset))

    wordle = Wordle(secret)
    while wordle.can_attempt:
        x = input('\nType Your Guess: ')

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f'Word Must Be {wordle.WORD_LENGTH} characters long' + Fore.RESET)
            continue


        if not x in wordset:
            print(Fore.RED + f'{x} is not a valid word' + Fore.RESET)
            continue
        
        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print('You"ve Solved it')
    else:
        print(f"You've Failed word was {wordle.secret.lower()}")



def display_results(wordle: Wordle):
    lines = []
    print('\nYour Results so far...')
    print(f'You Have {wordle.remaining_attempts} remaining! \n')
    for word in wordle.attempts:
        result =wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    
    for _ in range(wordle.remaining_attempts):
        lines.append(' '.join(['_'] * Wordle.WORD_LENGTH))

    draw_border_around(lines)



def load_word_set(path):
    word_set = set()
    with open(path, 'r') as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set




def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.LIGHTBLACK_EX
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int=9, padding: int=1 ):
    content_length = size + padding * 2
    top_border = "┌" + '─' * content_length + '┐'
    bottom_border = "└" + '─' * content_length + '┘ '
    space = " " * padding

    print(top_border)

    for line in lines:
        print('│'+ space + line + space + '│')

    print(bottom_border)

if(__name__ == '__main__'):
    main()

