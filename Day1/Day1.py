# Day 1 Python Exercise for CodeNation
# rewritten by Daniel Monaghan

# random Library import to give us the modules we need to run the program
import random

# Variables to be used later on in the script
exampleName = 'dan'  # String Variable
exampleLowerLimitNumber = 1  # Interger Variable
exampleUpperLimitNumber = 10

# print 'Hello World!'
print('Hello World!')

# print the byte length of 'hello' (answer: 5)
print(len('hello'))


print('hello'[1])

# using a string literal to define type before manipulation
print(f'Hello {str.upper(exampleName)}')

# using fString to append to the string 'exampleName'
print(f'Hello {exampleName.upper()}')

# printing as 2 arguments (auto spaced), print will
# automatically space argunments when more than one argunment is provided
print('Hello', exampleName.upper())

# same as above but with inline string
print('Hello', 'dan'.upper())

# print random float between 0.0E1-0.9r
print(f'random(): {random.random()}')

# print a random float(number with decimals) number
print(
    f'uniform(): {random.uniform(exampleLowerLimitNumber, exampleUpperLimitNumber)}')

# print a random Interger (whole Number) number
print(
    f'randint(): {random.randint(exampleLowerLimitNumber, exampleUpperLimitNumber)}')

# Bonus exercise

row = "--------------\n"
cols = "    |    |    \n"
print('', cols, row, cols, row, cols)
