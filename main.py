'''this is a symple typing trainer rnning in the terminal'''

from colorama import init, Fore, Style
import readchar
from readchar import key
import sys


def print_line(text,GREY):
    print(GREY + text, end="\r")
    sys.stdout.flush()

def keyboard_input(text,RED,RESET):
    for i in text:
        k = readchar.readkey()
        if k == i:
            print(RESET + k, end="")
        elif k == key.BACKSPACE:

        else:
            print(RED + k, end="")
        sys.stdout.flush()


def main():
    GREEN = Fore.GREEN
    RED = Fore.RED
    GREY = Fore.LIGHTBLACK_EX
    RESET = Style.RESET_ALL
    text = 'Heute suche ich meine USB Sticks und drücke auf jede Taste.'
    print_line(text,GREY)
    keyboard_input(text,RED,RESET)







if __name__ == '__main__':
     main()
