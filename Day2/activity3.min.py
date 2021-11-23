#!/usr/bin/env python3

#
# --------------
# Activity3.min.py
# --------------
#
# Print a Naughts and Crosses game to the terminal/shell
# Minified for fun
# Author: Daniel Monaghan
# Tutor: Tim Finch

game = [
    [
        ['x', 'o', ' '],
        ['x', 'x', ' '],
        ['o', ' ', ' ']],
    '-----------'
]
game_loops = 3
count = 0
for row in game[0]:
    count += 1
    print(f' {row[0]} | {row[1]} | {row[2]} ')
    if count < game_loops:
        print(game[1])
