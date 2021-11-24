from random import randrange
from os import system


def run_challenge(chal):
    from time import sleep

    def clear():
        print('✅ Test Complete')
        sleep(3)
        # CLEAR SCREEN HAPPENS HERE
        system('cls || clear')

    def print_challenge(chal_no, chal_desc: str):
        print(f'Challenge {chal_no}')
        print('-------------')
        print(chal_desc)
        print('')  # adda blank line

    print_challenge(chal["chal_no"], str(chal["chal_desc"]))
    chal = chal["chal_fn"]  # run the callback to start the challenge
    chal()
    clear()


if __name__ == '__main__':
    system('cls || clear')
    try:
        from chals_list import chals
        for chal in chals:
            run_challenge(chal)
        print('✅ All Challenges Complete')
        exit()
    except:
        print('\n')
        print('🤯 OK leaving')
        exit()
