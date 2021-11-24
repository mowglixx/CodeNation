# import some simple assists
from random import randrange  # random number generator
from os import system
import types


def run_challenge(chal):
    from time import sleep

    def clear():
        print('✅ Test Complete')
        sleep(3)
        print('# CLEAR SCREEN HAPPENS HERE #')
        # system('cls || clear')

    def print_challenge(chal_no, chal_desc: str):
        print(f'Challenge {chal_no}')
        print('-------------')
        print(chal_desc)
        print('')  # adda blank line

    print_challenge(chal["chal_no"], str(chal["chal_desc"]))
    chal = chal["callback"]  # run the callback to start the challenge
    chal()
    clear()
# -------------------------------------------------------------------
# define the challenge


def chal0_callback():
    # variables needed
    LEGAL_AGE = 18
    VALID_COUNRTY = "UK"
    print('Please enter your information')
    age = int(input('Age: '))
    country = input("Country: ")

    if (
        age >= LEGAL_AGE  # Legal Age Doesn't Change
        and country.upper() == VALID_COUNRTY  # only valid in "UK"
    ):
        print("Yes, I can serve you.")
        return True

    else:
        print("I can't serve you.")
        # print the reasons why
        print('Reasons:')
        if country.upper() != VALID_COUNRTY:
            print(
                f"{country.upper()} is not a valid country, Valid countries: {VALID_COUNRTY}"
            )
            return False
        if age < LEGAL_AGE:
            print(
                f"\"{age}\" is not old enough, You need to be {LEGAL_AGE} or above."
            )
            return False


chal0 = {
    "chal_desc": 'Compare variables to numbers (intergers) to satisfy an if condition, num > 18 in this example age has to be greater than 18 and the valid country is "uk"',
    "chal_no": 0,
    "callback": chal0_callback}

# -------------------------------------------------------------------
# define the challenge


def chal1_callback():
    LOOP_SWITCH = 1

    def check_password(password):
        PASSWORD_LENGTH = 8
        if len(password) > PASSWORD_LENGTH:
            return True
        return False
    while LOOP_SWITCH != 0:
        print('please type a password')
        password = input('Password: ')
        if password and check_password(password) == True:
            print('✅ The chosen password is longer than 8 characters')
            # I want to go on record that this is not something that you should do ever
            print(f'Password given: {password}')
            # the only way out
            LOOP_SWITCH = 0
        elif password and check_password(password) == False:
            print('😲 password too short')
        else:
            print('⛔ No Password given')
    # function complete
    return True


chal1 = {
    "chal_desc": 'Create a variable called password. Check how many letters are in the password, if there are less than 8 print that the password is too short. Otherwise print the password.',
    "chal_no": 1,
    "callback": chal1_callback}
# ---------------------------------------------------------------------------
# define the challenge


def chal2_callback():
    num = input('Please Choose a number [1-9000]: ')
    num = int(num)
    while num:
        if num:
            print('Number Chosen:', num)
            if num % 3 or num % 5:
                print('✅ This number is divisible by 3 or 5')
                if num % 3:
                    print('...3, to be exact.')
                if num % 5:
                    print('...5, honstly.')
                return True
            elif num % 3 and num % 5:
                print('✅ This number is divisible by 3 AND 5!!')
                return True
            else:
                print('❌ This number is not divisible by 3 or 5')
            print('❌ No usable Number detected, using Random Number Generator')
            num = randrange(1, 9000)
    # function complete
    return True


# define the challenge to be displayed
chal2 = {"chal_desc": 'Create a variable called num. Check if the variable is divisible by 3 or 5. If it is print "This number is divisible by 3 or 5” to the console. Otherwise log “This number is not divisible by 3 or 5”.',
         "chal_no": 2,
         "callback": chal2_callback}

# ---------------------------------------------------------------------------
# define the challenge

chal3 = {
    "chal_desc": 'Create a variable called num. If num is divisible by 3 print “fizz”, if it’s divisible by 7 print “buzz”, if it’s divisible by both 3 and 7 print “fizz buzz”. Otherwise print num.',
    "chal_no": 3
}


def fizz_buzz():
    # cast num into int
    num = int(input('enter a number: '))
    # setup

    def is_div(div):
        # import floor for handeling floats
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
    print('Divisible by 3?', is_div(3))
    print('Divisible by 7?', is_div(7))


# define the challenge to be displayed
chal3.update({"callback": fizz_buzz})

# ---------------------------------------------------------------------------
# define the challenge


def chal4_callback():
    word = input('Enter a word:')
    word_count = word.count()
    print('word count:', word_count)
    if word[word.count]:
        print('word:', word)


        # define the challenge to be displayed
chal4 = {"chal_desc": 'Create a variable called word that takes a string. Create an if statement that checks if the last letter is the same as the first. If it is return true, otherwise return false',
         "chal_no": 4,
         "callback": chal4_callback}

# ---------------------------------------------------------------------------
# define the challenge


def chal5_callback():
    print('Not Done Yet')


# define the challenge to be displayed
chal5 = {"chal_desc": 'Create a variable called `time`, a variable called `place_of_work` and a variable called `town_of_home`. Create an if statement that prints where someone is at times of the day. E.g. if the time is 7 I’m at home, at 8 I’m commuting, at 9 I’m at work.',
         "chal_no": 5,
         "callback": chal5_callback}
# ---------------------------------------------------------------------------
# define the challenge


def chal6_callback():
    print('Not Done Yet')


# define the challenge to be displayed
chal6 = {"chal_desc": 'Create two variables called num1 and num2. Create an if statement that checks if the result of the sum is even. If it is, return a success message.',
         "chal_no": 6,
         "callback": chal6_callback}

# ---------------------------------------------------------------------------

# define the challenge


def chal7_callback():
    print('Not Done Yet')


# define the challenge to be displayed
chal7 = {"chal_desc": 'Create a variable called num. Check if the number is a palindrome (looks the same forward as it does backwards e.g. 1001 or 20202).',
         "chal_no": 7,
         "callback": chal7_callback}

if __name__ == '__main__':
    system('cls || clear')
    try:
        chals = [
            # chal0,
            # chal1,
            # chal2,
            chal3,
            chal4,
            # chal5,
            # chal6,
            # chal7
        ]
        for single_challenge in chals:
            run_challenge(single_challenge)
        print('✅ All Challenges Complete')
        exit()
    except:
        print('\n')
        print('🤯 OK leaving')
        exit()
