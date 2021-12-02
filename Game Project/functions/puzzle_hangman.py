from random import randrange as r

from textutils import typewriter, clear_screen

from assets.hangman import state

from assets.hangman_wordlist import words as wordlist

def hangman_puzzle():

    word=wordlist[r(0,len(wordlist))]
    tries = 0
    guesses = []

    def print_tries():
        print("Attempts:",tries)
    def print_dashes():
        dashes = ""
        for char in word:
            dashes += "_ "
        typewriter(dashes)

    while word and tries <= 7 :
        clear_screen()
        print(state[tries])
        print_dashes()
        print_tries()
        for attempt in guesses:
            print(attempt)
        typewriter("Guess the word")
        guess  = input("\n")
        if guess.lower() in word or guess.lower() == word:
            if guess.lower() == word:
                word = None
                tries = 7
                print("winner")
                return True
        elif guess in guesses:
            pass
        elif tries < 7:
            guesses += guess
            tries += 1
        if tries >= 7:
            clear_screen()
            print_tries()
            print("game over")
            break    
    return False