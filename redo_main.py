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
    text = [
        'Lorem Ipsum dolor sit Amet, consectetur Adipiscing elit.↵',
        'Ut enim ad minim Veniam, quis nostrud Exercitation ullamco Laboris.↵',
    ]
    current_line = '[bright_black italic]' + text[sentence_nr] + '[/bright_black italic]'

    print_ui(mistakes, wpm, accuracy, time, current_line, used_os)
    while sentence_nr <= len(text):
        typed, sentence_nr, idx = input(text, sentence_nr, idx, typed)
        mistakes, typed, mistake_pos = spellcheck(typed, sentence_nr, text, mistakes)
        current_line = merge(text, sentence_nr, idx, typed, mistake_pos)
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
        Mistakes: {mistakes} | WPM: {wpm} | Accuracy: {accuracy} | Time: {time}
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


def merge(text, sentence_nr, idx, typed, mistake_pos):
    sentence = text[sentence_nr]
    current_line = '[bright_black italic]' + sentence[idx:] + '[/bright_black italic]'
    current_line = typed + current_line
    current_line = current_line[:idx] + '[bright_cyan]|[/bright_cyan]' + current_line[idx:]
    pos = 0
    for i in mistake_pos:
        x = current_line[pos]
        if i == 0:
            pos += 1
        elif i == 2:
            current_line = current_line[:pos] + f'[bright_red]_[/bright_red]' + current_line[pos + 1 :]
            pos += 26
        else:
            current_line = current_line[:pos] + f'[bright_red]{x}[/bright_red]' + current_line[pos + 1 :]
            pos += 26

    return current_line


def spellcheck(typed, sentence_nr, text, mistakes):
    idx = 0
    mistakes = 0
    mistake_pos = []
    for i in typed:
        if i == text[sentence_nr][idx]:
            mistake_pos.append(0)
            idx += 1
        else:
            if i == ' ':
                mistakes += 1
                mistake_pos.append(2)
                idx += 1
            else:
                mistakes += 1
                mistake_pos.append(1)
                idx += 1

    return mistakes, typed, mistake_pos


if __name__ == '__main__':
    main()
