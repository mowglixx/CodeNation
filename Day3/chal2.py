# Challenge 2
#
# Create a variable called num. Check if the
# variable is divisible by 3 or 5. If it is
# print "This number is divisible by 3 or 5”
# to the console.
# Otherwise log “This number is not divisible
# by 3 or 5”.

def precursor_to_fizzbuzz():
    # use a random number generator
    from random import randrange

    num = int(input('Please Choose a number [1-9000]: '))
    if num:
        print('Number Chosen: ', num)
        if num % 3 == 0 or num % 5 == 0:
            print('✅ This number is divisible by 3 or 5')
        else:
            print('❌ This number is not divisible by 3 or 5')
