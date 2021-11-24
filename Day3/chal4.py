#
# Challenge 4
#
# Create a variable called word that takes a string.
# Create an if statement that checks if the last letter is the same as the first.
# If it is return true, otherwise return false

def comparing_letters_from_a_word():

    word = input('Enter a word:')

    first_letter = word[0]
    last_letter = word[::-1][0]

    print('First Letter:', first_letter)
    print('Last Letter:', last_letter)
    if first_letter == last_letter:
        result = True
    else:
        result = False

    print(f'Is {first_letter} different to {last_letter} in {word.upper()}?')
    print(f'Result: {result}')
