from time import sleep
import random as r

from .textutils import typewriter
from .assets.dialogue import player_name


RPS = ["ROCK", "PAPER", "SCISSORS"]


def rock_paper_scissors_puzzle():
    comp = computer_move()
    player = player_move()
    winner, tie = calc_winner(comp, player)
    disp_winner(winner, tie)
    return winner


def computer_move():
    comp = r.choice(RPS)
    return comp


def player_move():
    player = ""
    while not player in RPS:
        player = input("Choose your weapon (rock, paper, or scissors): ").upper()
    return player


def calc_winner(comp, player):
    typewriter("\n\nYour opponent chooses {0}.".format(comp))
    winner = None
    tie = False

    if player == comp:
        typewriter("\n\nNo winner.... Restarting....\n")
        rock_paper_scissors_puzzle()
        tie = True
    elif (((comp == "ROCK") and (player == "PAPER")) or
          ((comp == "PAPER") and (player == "SCISSORS")) or
          ((comp == "SCISSORS") and (player == "ROCK"))):
        winner = True
    else:
        winner = False

    return winner, tie


def disp_winner(winner, tie):
    if tie == True:
        typewriter("")
    elif winner == True:
        typewriter("\n\nYou beat your opponent!")
    elif winner == False:
        typewriter("\n\nYour opponent beat you!")


