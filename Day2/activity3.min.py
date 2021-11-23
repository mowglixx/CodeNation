#!/usr/bin/env python3
import os
import time
import random

# Print a Naughts and Crosses game to the terminal/shell
# Minified for fun
# Author: Daniel Monaghan
# Tutor: Tim Finch


def clear_screen():
    os.system('cls||clear')


def rng():
    # Define RNG behaviour
    return random.randrange(0, 3)


def translate_cells(old_row=[0, 0, 0]):
    # define the translated_row variable as a list type
    translated_row = []
    # loop through the rng based cells and change them to their new values
    for cell in old_row:
        if cell == 0:
            cell = ' '
        if cell == 1:
            cell = 'x'
        if cell == 2:
            cell = 'o'
        # add the new value to the translated_row list
        translated_row += cell
    return translated_row


def new_game(game=''):
    if (game != ''):
        game = game
    else:
        game = [
            [rng(), rng(), rng()],
            [rng(), rng(), rng()],
            [rng(), rng(), rng()],
        ]
    # define what each game looks like
    AMOUNT_OF_ROWS = 3
    translated_cells = []
    for row in game:
        translated_cells += [translate_cells(row)]
    print(
        f' {translated_cells[0][0]} | {translated_cells[0][1]} | {translated_cells[0][2]}',
        f' {translated_cells[1][0]} | {translated_cells[1][1]} | {translated_cells[1][2]}',
        f' {translated_cells[2][0]} | {translated_cells[2][1]} | {translated_cells[2][2]}',
        sep=f'\n-----------\n')


# start our main function if this file is being executed
if __name__ == '__main__':
    try:
        while True:
            time_between_games = 0.5
            # wait for a bit before clearing the screen and starting a new game
            time.sleep(time_between_games)
            clear_screen()
            new_game()
            print('This will continue forever...')
            print('Press Ctrl+C to when you\'re... done? *shudders*')
    except:
        clear_screen()
        print('Oh! Go on! one more...')
        time.sleep(time_between_games)
        new_game()
        time.sleep(time_between_games)
        print('All done...')
