from time import sleep
from .textutils import typewriter
from random import randint


def riddle_puzzle():
    typewriter("Welcome to your riddle!")
    typewriter("\n\nWhat do \"T\" and an island have in common?")
    
    tries = 0
    
    while tries < 3:
        guess = input("\nTake a guess:\n")

        if guess.lower() != "water":
            tries += 1
            if tries == 2:
                typewriter("\n\nSorry, you're out of guesses!")
                return False
            elif tries < 2:
                typewriter("\nNearly, try again...")
        elif guess.lower() == "water" :
            typewriter("You guessed it! The answer is - They are both in the middle of water!")
            sleep(2)
            return True
