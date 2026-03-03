"""this is a symple typing trainer rnning in the terminal"""

import platform
import os
from colorama import init, Fore, Style, Cursor
import readchar
from readchar import key
import sys
import time


def clear_terminal(used_os):
    if used_os == 'windows':
        os.system('cls')


def spell_check(typed, sentence_nr, idx, current, mistakes):
    should_be = current[:idx]
    idx = 0
    mistakes = 0
    for i in typed:
        if i == should_be[idx]:
            idx += 1
        else:
            mistakes += 1
            idx += 1
    return mistakes


def print_line(text, GREY, sentence_nr):
    sys.stdout.write('\r\033[K')
    sys.stdout.flush()
    print(GREY + text[sentence_nr], end='\r')
    sys.stdout.flush()


def keyboard_input(text, RED, RESET, GREY, sentence_nr, mistakes):
    current = text[sentence_nr]
    idx = 0
    typed = ''
    while idx < len(current):
        i = current[idx]
        k = readchar.readkey()
        typed += k

        if i == '↵':
            if k == key.ENTER:
                exit
            else:
                continue

        if k == key.BACKSPACE:
            if idx > 0:
                idx -= 1
                print(Cursor.BACK(1), end='')
                print(GREY + current[idx], end='')
                print(Cursor.BACK(1), end='')
                sys.stdout.flush()
            continue

        if k == i:
            print(RESET + k, end='')
            idx += 1
        else:
            if k == ' ':
                print(RED + '_', end='')
                idx += 1

            else:
                print(RED + k, end='')
                idx += 1

        spell_check(typed, sentence_nr, idx, current, mistakes)

        sys.stdout.flush()
    return mistakes


def main():
    used_os = platform.system().lower()
    GREEN = Fore.GREEN
    RED = Fore.RED
    GREY = Fore.LIGHTBLACK_EX
    RESET = Style.RESET_ALL
    sentence_nr = 0
    mistakes = 0
    text = ['Heute suche ich meine USB Sticks und drücke auf jede Taste.↵', 'I hope this shit works.↵']
    for i in text:
        clear_terminal(used_os)
        print_line(text, GREY, sentence_nr)
        keyboard_input(text, RED, RESET, GREY, sentence_nr, mistakes)
        mistakes += mistakes
        sentence_nr += 1
    print(mistakes)


if __name__ == '__main__':
    main()
