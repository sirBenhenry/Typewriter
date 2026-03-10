"""sdkhsdfh"""

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
    elapsed_time = 0
    current_line = 0
    mistakes_stored = 0
    idx = 0
    sentence_nr = 0
    typed = ''
    text = [
        'Lorem Ipsum dolor sit Amet, consectetur Adipiscing elit.↵',
        'Ut enim ad minim Veniam, quis nostrud Exercitation ullamco Laboris.↵',
    ]

    clear_terminal(used_os)
    print('press enter to start')
    k = readchar.readkey()
    repeated = 0
    if k == key.ENTER:
        clear_terminal(used_os)
    else:
        while k != key.ENTER:
            clear_terminal(used_os)
            print('thats not enter\ntry again...')
            k = readchar.readkey()
            repeated += 1
            if repeated == 5:
                print('Never touch a computer again.')
                time.sleep(1)
                clear_terminal(used_os)
                sys.exit()

    current_line = '[bright_black italic]' + text[sentence_nr] + '[/bright_black italic]'
    start_time = time.perf_counter()

    print_ui(mistakes, wpm, accuracy, elapsed_time, current_line, used_os)
    while sentence_nr <= len(text):
        typed, sentence_nr, idx, mistakes_stored = input(text, sentence_nr, idx, typed, mistakes_stored, mistakes)
        mistakes, typed, mistake_pos = spellcheck(typed, sentence_nr, text, mistakes, mistakes_stored)
        current_line = merge(text, sentence_nr, idx, typed, mistake_pos)
        elapsed_time = update_time(start_time)
        wpm, accuracy = wpm_accuracy_calculation(typed, sentence_nr, text, mistakes, wpm, accuracy, elapsed_time)
        print_ui(mistakes, wpm, accuracy, elapsed_time, current_line, used_os)


def clear_terminal(used_os):
    if used_os == 'windows':
        os.system('cls')
    else:
        os.system('clear')


def print_ui(mistakes, wpm, accuracy, elapsed_time, current_line, used_os):
    clear_terminal(used_os)
    print(
        f"""
        Mistakes: {mistakes} | WPM: {wpm:.0f} | Accuracy: {accuracy:.1f}% | Time: {elapsed_time:.1f}
        {current_line}
            """
    )


def input(text, sentence_nr, idx, typed, mistakes_stored, mistakes):
    k = readchar.readkey()
    sentence = text[sentence_nr]
    current_letter = sentence[idx]
    if k == key.BACKSPACE:
        if idx > 0:
            typed = typed[:-1]
            idx -= 1
        else:
            return typed, sentence_nr, idx, mistakes_stored
    elif k == key.ENTER:
        if current_letter == '↵':
            idx = 0
            sentence_nr += 1
            mistakes_stored += mistakes
            typed = ''
        else:
            return typed, sentence_nr, idx, mistakes_stored

    else:
        if current_letter == '↵':
            return typed, sentence_nr, idx, mistakes_stored
        else:
            typed += k
            idx += 1

    return typed, sentence_nr, idx, mistakes_stored


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
            current_line = current_line[:pos] + '[bright_red]_[/bright_red]' + current_line[pos + 1 :]
            pos += 26
        else:
            current_line = current_line[:pos] + f'[bright_red]{x}[/bright_red]' + current_line[pos + 1 :]
            pos += 26

    return current_line


def spellcheck(typed, sentence_nr, text, mistakes, mistakes_stored):
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

    mistakes += mistakes_stored

    return mistakes, typed, mistake_pos


def update_time(start_time):
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def health():
    pass


def wpm_accuracy_calculation(typed, sentence_nr, text, mistakes, wpm, accuracy, elapsed_time):
    time_min = elapsed_time / 60
    keypresses = len(typed) / 5
    wpm = keypresses / time_min
    if len(typed) == 0:
        return wpm, accuracy
    else:
        accuracy = ((len(typed) - mistakes) / len(typed)) * 100

    return wpm, accuracy


if __name__ == '__main__':
    main()
