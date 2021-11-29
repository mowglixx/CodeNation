from os import system as s
from time import sleep
from sys import stdout as term

def clear_screen():
    s('cls||clear')

clear_screen()

text_speed = 0.1
screen_width = 40

def typewritter(line):
    for char in line:
        sleep(0.03)
        term.write(char)
        term.flush()
    term.write("\n")
    term.flush()

def dialogue_box(artwork, actor, dialogue):
    actor = str(actor)
    global screen_width
    num_stars_needed = screen_width - 10 - len(actor)
    solid_line = f"***[ {actor} ]***"
    solid_line += "*"*num_stars_needed
    print(artwork)
    print('')
    print(solid_line)
    typewritter(dialogue[0])
    typewritter(dialogue[1])
    typewritter(dialogue[2])
    typewritter(dialogue[3])
    input("\n ⏩ Press Enter to continue...")    
    clear_screen()
