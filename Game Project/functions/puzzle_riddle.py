from random import randint


def riddle_game():
    print("Welcome to your riddle PLAYER")
    print("What do T and an island have in common?")

    guess = ""

    tries = 0

    while guess.lower() != "water":
        guess = input("Take a guess: ")
        tries += 1
        if tries == 2:
            break
        elif tries < 2:
            print("Nearly, try again...")

    if guess.lower() == "water" and tries < 3:
        print("You guessed it! The answer is - They are both in the middle of water")
        print("And it only took you", tries, "tries!\n")
        return True
    print("Sorry, you're out of guesses!")
    return False