import platform
import os
from rich import print
import readchar
from readchar import key
import sys
import time


def main():
    used_os = platform.system().lower()
    mistakes = 0
    wpm = 0
    accuracy = 0
    time = 0
    current_line = 0
    idx = 0
    sentence_nr = 0
    typed = ''
    text = ['Heute suche ich meine USB Sticks und drickest auf jede Taste.↵', 'I hope this shit works.↵']

    while sentence_nr <= len(text) - 1:
        typed, sentence_nr, idx = input(text, sentence_nr, idx, typed)
        current_line = merge(text, sentence_nr, idx, typed)
        print_ui(mistakes, wpm, accuracy, time, current_line, used_os)


def clear_terminal(used_os):
    if used_os == 'windows':
        os.system('cls')
    else:
        os.system('clear')


def print_ui(mistakes, wpm, accuracy, time, current_line, used_os):
    clear_terminal(used_os)
    print(
        f"""
        [red]Mistakes:[/red] {mistakes} | WPM: {wpm} | Accuracy: {accuracy} | Time: {time}
        {current_line}
            """
    )


def input(text, sentence_nr, idx, typed):
    k = readchar.readkey()
    sentence = text[sentence_nr]
    current_letter = sentence[idx]
    if k == key.BACKSPACE:
        if idx > 0:
            typed = typed[:-1]
            idx -= 1
        else:
            return typed, sentence_nr, idx
    elif k == key.ENTER:
        if current_letter == '↵':
            idx = 0
            sentence_nr += 1
            typed = ''
        else:
            return typed, sentence_nr, idx
    else:
        typed += k
        idx += 1

    return typed, sentence_nr, idx


def merge(text, sentence_nr, idx, typed):
    sentence = text[sentence_nr]
    current_line = '[bright_black italic]' + sentence[idx - 1 :] + '[/bright_black italic]'
    current_line = typed + current_line
    current_line = current_line[:idx] 

    return current_line


if __name__ == '__main__':
    main()
