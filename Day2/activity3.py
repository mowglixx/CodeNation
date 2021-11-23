#!/usr/bin/env python3

#
# --------------
# Activity3.py
# --------------
#
# Print a Naughts and Crosses game to the terminal/shell
# Author: Daniel Monaghan
# Tutor: Tim Finch
#

# top row
space1 = 'x'
space2 = 'o'
space3 = ' '

# middle row
space4 = 'x'
space5 = 'x'
space6 = ' '

# bottom row
space7 = 'o'
space8 = ' '
space9 = ' '

# 2nd line is 3 dashes with 2 dashes to offset the vertical
# lines due to monospace characters, we can re-use this so
# why not make a variable?
line_row = '-----------'

# spaced row will act as a container for each spaceX value ('x'/'o'/' ')
spaced_row = ' {} | {} | {} '

# format a spaced_row string to have the correct values
top_row = spaced_row.format(space1, space2, space3)
mid_row = spaced_row.format(space4, space5, space6)
bot_row = spaced_row.format(space7, space8, space9)

# gross .format notation that shows why this is the old way of
# doing things see below for cooler version
board = "{}\n{}\n{}\n{}\n{}\n".format(
    top_row, line_row, mid_row, line_row, bot_row)
# print functional .format() method
print(board)

# cleaner syntax and easier to read
# list the screen lines in a list data type
screen_lines = [top_row, line_row, mid_row, line_row, bot_row]

# then create a 'line' variable for each item in the
# 'screen_lines' list and print it to the screen on a newline
print("Looping method (same result but easier to read)")
for line in screen_lines:
    # gotta love a good loop
    print(line)
