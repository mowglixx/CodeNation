from os import system as s
from time import sleep
from sys import stdout as term

dialogue = [
    "Good morning PLAYER. Did you slept well?",
    "There’s a note over there on the side.",
    "Would you like to read it? Now I’m just",
    "Padding to make an extra line."
    ]

ascii_art = """           .          .           .     .                .       .
  .      .      *           .       .          .                       .
                 .       .   . *            "Go where you will...
  .       ____     .      . .            .    I'll always love you, Tammy."
         >>         .        .               .
 .   .  /WWWI; \  .       .    .  ____               .         .     .         
  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             .
  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .
     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .
 . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .
  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .
 /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *
/WWWWWWWWWIIIIIWIIii;;::;..;\WWWWWWIII;;;:::...    ;IMIII;;     ::  \     .
WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :    \   
WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWWWWIIII;::; :::::::::.....::      \\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXX
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%XXXXXXXXXXXXXXXXXXXXXXXXXX"""

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

dialogue_box(ascii_art, "Character Name here", dialogue)