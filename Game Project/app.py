from time import sleep


# local librarys
import functions.textutils as t
from functions.puzzle_missing_word import missing_word_puzzle
from functions.puzzle_maths import maths_puzzle
from functions.puzzle_riddle import riddle_puzzle
from functions.puzzle_rock_paper_scissors import rock_paper_scissors_puzzle as rps
from functions.puzzle_missing_word import missing_word_puzzle
from functions.assets.dialogue import lines as l, villan_name as meg, player_name as p
from functions.assets.artwork import artwork as a
from functions.assets.gameovers import gameovers as gameover_reasons

# make it faster to write main with a few aliases
d = t.dialogue_box
cls = t.clear_screen
lion_name = 'Prof. Lion \'Mittens\' McNaulty IV'



def show_title():
    # clear the screen and show the title for 3 seconds 
    # then clear the screen and start the game 
    cls()
    print(a['title'])
    sleep(3)
    cls()

if __name__ == '__main__':
    try:
        show_title()
        d('blank', meg, l[0])
        d('home', '', l[1], False)
        
        # ask the old lady for help? else gameover
        if t.choice('Do you ask them for help?') == False: t.game_over(gameover_reasons[0])

        cls()
        d('old_lady', 'Old Lady', l[2], False)
        print('\n')

        # if you fail... you will die.
        if missing_word_puzzle() == False: t.game_over(gameover_reasons[1])
        cls() 

        d('old_lady', 'Old Lady', l[3]) 


        # going toward village
        d('village', '', l[4], False)

        if t.choice('Pick it up and take a look?'):
            cls() 
            d('dazed','💩',l[5]) # dog poo [dazed art]
        else:
            cls()
            d('dazed','💩','That\'s probably for the best... Moving on...') # dog poo [dazed art]    
        
        d('forest','???',l[6]) # ??? // WAIT who goes there? [forest art] 
        d('forest','',l[7]) # Narrator // You stop dead in your tracks [forest art]
        d('black_knight_pre','Black Knight',l[8]) # Black Knight // What are you doing here? [black_kight_pre art]
        d('black_knight_pre',p,l[9]) # player // ...
        d('black_knight_pre','Black Knight',l[10], False) # Black Knight // I see
        if rps() == False: 
            t.game_over(gameover_reasons[3])
        cls()
        
        d('black_knight_pre','Black Knight',l[11])
        d('black_knight_pre','Black Knight',l[12])
        d('black_knight_pre','Black Knight',l[13])
        d('black_knight_pre','Black Knight',l[14])
        d('black_knight_post','Black Knight',l[15])
        d('sword','Black Knight',l[16])
        d('village','',l[17], False)
        
        # sit next to the lion?
        if t.choice('Do you go and sit next to him?') == False:
            t.game_over(gameover_reasons[3])
        cls()

        d('lion',lion_name,l[18], False)
        # help from the lion?
        if t.choice('Would you like my help?') == False:
            t.game_over(gameover_reasons[4])
        cls()
        
        # Lion Help
        d('lion',lion_name,l[19], False)
        if riddle_puzzle() == False:
            t.game_over(gameover_reasons[5])
        cls()
        
        d('lion',lion_name,l[20])
        
        d('phone','',l[21], False)
        # Maths Challenge
        if maths_puzzle() == False:
            t.game_over(gameover_reasons[6])
        cls()

        d('castle', 'Lion', l[22])
        d('dazed', '???', l[23])
        d('princess', 'Princess Footstool', l[24])
        d('dazed', '', l[25])
        d('dazed', meg, l[26], False)
        # Maths Challenge
        if t.choice('Do you have any last requests?') == False:
            t.game_over(gameover_reasons[7])
        cls()
        
        # RPS 2 - Electric Boogaloo
        # - Cancelled Hangman Challenge
        d('blank', meg, l[27], False)
        if rps() == False:
            t.game_over(gameover_reasons[8])
        cls()
        
        d('sword', meg,l[28], False)
        if t.choice('Do you have it?, theif!') == False:
            t.game_over(gameover_reasons[9])
        cls()
        d('sword', meg,l[29])
        d('blank', meg,l[30])
        d('princess', meg,l[31])
        d('princess', 'Princess Satsuma',l[32])
        d('sunset', p,l[33])
        
        d('sunset', 'Dan, James and Ste', l[34], False)
        exit()
    except:
        t.typewriter('\nExiting...\nThanks for playing, this game was made by: \nDaniel Monaghan \nJames Christie \nStephen McCoy\nin 2021 for CodeNation\n')