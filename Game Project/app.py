from time import sleep
from functions.puzzle_missing_word import missing_word_puzzle
import functions.textutils as t
from functions.assets.dialogue import lines as l, villan_name as meg, player_name as p
from functions.assets.artwork import artwork as a

title = a['title']
d = t.dialogue_box

# switches
PLAYER_HAS_NAME, TEXT_SPEED_SET, NEW_GAME_CONFIRM = 0, 0, 0

text_speed = 0.1
screen_width = 60
if __name__ == '__main__':
    print(title)
    sleep(3)
    t.clear_screen()
    d('blank', meg, l[0])
    d('blank', 'narrator', l[1])
    t.choice('Do you ask them for help?')
    d("old_lady" 'Old Lady', l[2])
    missing_word_puzzle()
    d("old_lady" 'Old Lady', l[3])
    d[4] = player // going toward village [village art]
    t.choice('Pick it up and take a look?')
    d[5] = player // dog poo 💩 [dazed art]
    d[6] = ??? // WAIT who goes there? [forest art] 
    d[7] = Narrator // You stop dead in your tracks [forest art]
    d[8] = Black Knight // What are you doing here? [black_kight_pre art]
    d[9] = player // ... 
    d[10] = Black Knight // I see [black_kight_pre art]
    rock paper scissors puzzle
    d[11] = Black Knight // What? [black_kight_post art]
    d[12] = Black Knight // No! [black_kight_pre art]
    d[13] = Black Knight // How??? [black_kight_pre art]
    d[14] = Black Knight // whole life purpose... [black_kight_pre art]
    d[15] = Black Knight // take sword [black_kight_post art]
    d[16] = Black Knight // take sword acknol [sword art]
    d[17] = narrator // go toward village [village art]
    choice 3 [sit next to lion]
    d[18] = Lion // Take a seat, mon amis [lion art]
    choice 4 [Would you like my help?]
    d[19] = Lion // Marvellous. Of course [lion art]
    RIDDLE CHALLENGE
    d[20] = Lion // You're not as stupid as you look [phone art]
    d[21] = Narrator // You go to the phonebox and step inside [spiral art]
    MATHS CHALLENGE
    d[22] = Lion // Carol Vorderman [castle art]
    d[23] = ??? // Everthing Blurry [dazed art]
    d[24] = Footstool // Help me [princess art]
    d[25] = Narrator // Thats her [dazed art]
    d[26] = Meg // pathetic worm [dazed art]
    choice 5 [Do you have any last requests?]
    d[27] = Meg // hangman, cancelled [blank art]
    RPS 2 - Electric Boogaloo
    d[28] = Meg // Curses! [sword art]
    choice 6 [Do you have it, yes or no?]
    d[29] = Meg // Hand it over! [sword art]
    d[30] = Meg // Never Mind [blank art]
    d[31] = Meg // Take waman [princess art]
    d[32] = Narator // You grab the Princess [princess art]
    d[33] = Princess Stasuma // I'm Princess Stasuma [princess art]
    d[34] = player // You must be nuts [princess art]
    dialogue_box()