#
# Challenge 7
#
# Create a variable called num.
# Check if the number is a palindrome
# (looks the same forward as it does backwards
# e.g. 1001 or 20202)

def is_palindrome():
    num = input('Please input a Number: ')

    print('right way', num)
    print('one way', num[::-1])

    if num == num[::-1]:
        print(f'{num} is a palindrone')
    else:
        print(f'{num} is NOT a palindrone')
