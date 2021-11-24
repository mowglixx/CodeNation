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
    # cast num into int
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
        elif is_div(3) and is_div(7) != True:
            print('fizz')
        elif is_div(7) and is_div(3) != True:
            print('buzz')
        else:
            print(num)
    print(f'{num} Divisible by 3: {is_div(3)}')
    print(f'{num} Divisible by 7: {is_div(7)}')
