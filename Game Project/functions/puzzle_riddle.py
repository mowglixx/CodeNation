from .textutils import typewriter
from random import randint


def riddle_puzzle():
    typewriter("Welcome to your riddle PLAYER")
    typewriter("What do T and an island have in common?")

    guess = ""

    tries = 0

    while guess.lower() != "water":
        guess = input("Take a guess: ")
        tries += 1
        if tries == 2:
            break
        elif tries < 2:
            typewriter("Nearly, try again...")

    if guess.lower() == "water" and tries < 3:
        typewriter("You guessed it! The answer is - They are both in the middle of water")
        typewriter("And it only took you", tries, "tries!\n")
        return True
    typewriter("Sorry, you're out of guesses!")
    return False