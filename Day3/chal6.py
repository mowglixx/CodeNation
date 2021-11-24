# Create two variables called num1 and num2.
# Create an if statement that checks if the
# result of the sum is even. If it is, return
# a success message.

def is_even():
    # cast int data type as input returns str
    num1 = int(input('num1:'))
    num2 = int(input('num2:'))

    # get the sum
    sum = num1 + num2

    # if sum is divisable by 2 it's even
    # also 0 is even...
    if sum % 2 == 0 or sum == 0:
        print(f'{sum} is Even')
    else:
        print(f'{sum} is Odd')
