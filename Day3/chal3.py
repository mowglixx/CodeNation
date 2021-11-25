#
# Challenge 3
#
# Create a variable called num.
# If num is divisible by 3 print “fizz”,
# if it’s divisible by 7 print “buzz”,
# if it’s divisible by both 3 and 7 print
# “fizz buzz”.
# Otherwise print num.

def fizzbuzz():
    # cast num into int becuase input returns a string
    num = int(input('enter a number: '))

    # create a function to check the divisable number and return a boolean for use in if statments
    def is_div(div):
        from math import floor
        if floor(num % div) == 0:
            return True
        return False

    if num > 0:
        if is_div(3) and is_div(7):
            print('fizzbuzz')
            print(f'{num} is divisible by 3 AND 7')
        elif is_div(3):
            print('fizz')
            print(f'{num} is divisible by 3')
        elif is_div(7):
            print('buzz')
            print(f'{num} is divisible by 7')
        else:
            print(num)
            print(f'{num} is not divisible by 3 or 7')
