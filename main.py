'''this is a symple typing trainer rnning in the terminal'''

from colorama import init, Fore, Style, Cursor
import readchar
from readchar import key
import sys


def print_line(text,GREY,sentence_nr):
    print(GREY + text[sentence_nr], end="\r")
    sys.stdout.flush()

def keyboard_input(text,RED,RESET, GREY, sentence_nr):
    current = text[sentence_nr]
    idx = 0
    while idx < len(current):
        i = current[idx]
        k = readchar.readkey()

        if i == '↵':
            if k == key.ENTER:
                print(sentence_nr)
            else:
                continue

        if k == key.BACKSPACE:
            if idx > 0:
                idx -= 1
                print(Cursor.BACK(1), end="")
                print(GREY + current[idx], end="")
                print(Cursor.BACK(1), end="")
                sys.stdout.flush()
            continue

        if k == i:
            print(RESET + k, end="")
            idx += 1
        else:
            if k == ' ':
                print(RED + '_', end="")
                idx += 1
            else:
                print(RED + k, end="")
                idx += 1

        sys.stdout.flush()


def main():
    GREEN = Fore.GREEN
    RED = Fore.RED
    GREY = Fore.LIGHTBLACK_EX
    RESET = Style.RESET_ALL
    sentence_nr = 0
    text = ['Heute suche ich meine USB Sticks und drücke auf jede Taste.↵']
    print_line(text,GREY,sentence_nr)
    keyboard_input(text,RED,RESET, GREY, sentence_nr)







if __name__ == '__main__':
     main()
