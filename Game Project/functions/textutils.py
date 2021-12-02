from os import system as s
from time import sleep
from sys import stdout as term
from typing import Literal
from assets.dialogue import affirmative_words, negative_words
from assets.artwork import artwork as a
from math import floor
# default globals
text_speed = 0.03
screen_width = 60

def choice(question="What is your answer? "):
    while True:
        choice = input(question+'[Y/N] ')
        if choice.lower() in affirmative_words:
            return True
        elif choice.lower() in negative_words:
            return False
        else:
            print("Answer not recognised, try again")


# def format_lines(dialogue_lines: str = ""):
#     global screen_width
#     # split the string into words
#     words = dialogue_lines.split()
#     current_line = ""
#     lines = []
#     # do this for each word in words
#     for next_word in words:
#         # if the length of the line + the length of the
#         # next word in the dialogue is less than 40 add
#         # the word to the string with a space else
#         # newline THEN the next word
#         if len(current_line)+len(next_word) <= screen_width:
#             current_line += next_word+" "
#         else:
#             lines.append(current_line)
#             current_line = next_word+" "
#     # when the lines have been
#     return lines


def clear_screen():
    s('cls||clear')


def typewriter(line):
    global text_speed
    punctuation = [".", "?", "!"]
    for char in line:
        if char != " ":
            sleep(text_speed)
        term.write(char)
        if (
            char in punctuation 
            and prev_char != char):
            term.write("\n")
        term.flush()
        prev_char = char

def dialogue_box(artwork="blank", actor="", dialogue="""...You should have wrote something here, lazy developer..."""):

    global screen_width
    dialogue2 = dialogue

    # check for actor
    if actor:
        solid_line = f"***[ {actor} ]***"
        num_stars_needed = screen_width - len(solid_line)
        solid_line += "*"*num_stars_needed
    else:
        solid_line = "*"*screen_width

    # while there is lines print 4 at a time
    print(a[artwork])
    print(solid_line)
    typewriter(dialogue2)
    input("\nPress Enter ⏩\n")
    clear_screen()
