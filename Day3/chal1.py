# Challenge 1
#
# Create a variable called password.
# Check how many letters are in the password,
# if there are less than 8 print that the
# password is too short. Otherwise print the
# password.

def password_length():
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
