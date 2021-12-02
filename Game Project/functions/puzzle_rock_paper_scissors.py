import random as r

RPS = ["ROCK", "PAPER", "SCISSORS"]


def rps():
    comp = computer_move()
    player = player_move()
    winner, tie = calc_winner(comp, player)
    disp_winner(winner, tie)


def computer_move():
    comp = r.choice(RPS)
    return comp


def player_move():
    player = ""
    while not player in RPS:
        player = input("Choose your weapon(rock, paper, or scissors: ").upper()
    return player


def calc_winner(comp, player):
    print("The computer chooses {0}.".format(comp))
    winner = None
    tie = False

    if player == comp:
        print("No winner.... Restarting....\n")
        rps()
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
        print("")
    elif winner == True:
        print("You beat the computer!")
    elif winner == False:
        print("The computer beat you!")


