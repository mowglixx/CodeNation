from os import system as s
from time import sleep
from sys import stdout as term
from .assets.dialogue import affirmative_words, negative_words
from .assets.artwork import artwork as a


# default globals
text_speed = 0.03
screen_width = 60

def choice(question="What is your answer?"):
    while True:
        typewriter('\n'+question)
        choice = input('\n')
        if choice.lower() in affirmative_words:
            return True
        elif choice.lower() in negative_words:
            return False
        else:
            typewriter("\nAnswer not recognised, try again")


def format_lines(dialogue_lines: str = ""):
    global screen_width
    # used for to represent \n
    literally_a_new_line = """
    """
    # split the string into words[word,word...]
    words = dialogue_lines.split(" ")
    
    # create a current line string for appending to 
    current_line = ""

    # manual char_count to have a max line length not based on len(str())
    char_count = 0
    # do this for each word in words
    for next_word in words:
        # if the length of the line + the length of the
        # next word in the dialogue is less than the target 
        # screen width -2 add the word to the string with 
        # a space else newline THEN the next word
        if char_count + len(next_word+" ") < screen_width-2:
            # add the length of the next word to the char_count plus a space
            char_count+=len(next_word+" ")
            current_line += next_word+" "
        elif next_word == "\n" or next_word == literally_a_new_line:
            current_line += next_word+" "
            char_count = len(next_word)+1
        else:
            current_line += next_word+"\n"
            char_count = 0
    # when the lines have been
    return current_line


def clear_screen():
    s('cls||clear')


def typewriter(line):
    global text_speed
    for char in line:
        if char != " ":
            sleep(text_speed)
        term.write(char)
        term.flush()

def dialogue_box(
    artwork="blank", 
    actor="", 
    dialogue="""You missed the dialogue in this call""", 
    clear=True):

    global screen_width
    
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
    typewriter(format_lines(dialogue)+'\n')
    if clear:
        input("Press Enter ⏩")
        clear_screen()

def game_over(reason):
    clear_screen()
    dialogue_box("dazed", "YOU DIED!", reason)
    exit()