from os import system as s
from time import sleep
from sys import stdout as term
from assets.dialogue import affirmative_words, negative_words

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


def format_lines(dialogue_lines: str = ""):
    global screen_width
    # split the string into words
    words = dialogue_lines.split()
    current_line = ""
    lines = []
    # do this for each word in words
    for next_word in words:
        # if the length of the line + the length of the
        # next word in the dialogue is less than 40 add
        # the word to the string with a space else
        # newline THEN the next word
        if len(current_line)+len(next_word+" ") < screen_width:
            current_line += next_word+" "
        else:
            lines.append(current_line)
            current_line = ""
            current_line += next_word+" "
    # when the lines have been
    return lines


def clear_screen():
    s('cls||clear')


def typewriter(line):
    global text_speed
    for char in line:
        if char != " ":
            sleep(text_speed)
        term.write(char)
        term.flush()
    term.write("\n")
    term.flush()


def dialogue_box(artwork: str, actor: str, dialogue=[]):

    global screen_width

    number_of_dialogue_lines = len(dialogue)
    dialogue_index = 0

    # check for a multiple of 4 lines in dialogue,
    # if there is remaining lines that will cause
    # an index error add an empty string to the array
    # for the ammout of lines that are "spare"
    if number_of_dialogue_lines % 4 != 0:
        spare_lines = 4-(len(dialogue) % 4)
        while spare_lines > 0:
            dialogue.append('')
            spare_lines -= 1

    # check for actor
    if actor:
        solid_line = f"***[ {actor} ]***"
        num_stars_needed = screen_width - len(solid_line)
        solid_line += "*"*num_stars_needed
    else:
        solid_line = "*"*screen_width

    # while there is lines print 4 at a time
    while len(dialogue) > 0 and dialogue_index < len(dialogue):
        print(artwork)
        print(solid_line)
        typewriter(dialogue[dialogue_index])
        typewriter(dialogue[dialogue_index+1])
        typewriter(dialogue[dialogue_index+2])
        typewriter(dialogue[dialogue_index+3])

        # increase the index by 4 to bring the next "page" of dialogue
        if dialogue_index < number_of_dialogue_lines:
            dialogue_index += 4

        input("\nPress Enter to continue ⏩\n")
        if dialogue_index > number_of_dialogue_lines:
            clear_screen()
            break
        else:
            clear_screen()
