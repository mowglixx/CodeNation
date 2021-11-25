from os import system
from time import sleep

time_between_challenges = int(input('Time Between Challenges (in seconds): '))


def clear():
    system('cls || clear')


def run_challenge(chal):
    def print_challenge(chal_no, chal_desc: str):
        sleep(time_between_challenges)
        # CLEAR SCREEN HAPPENS HERE
        clear()
        print(f'🧪 Challenge {chal_no}')
        print('---------------')
        print(chal_desc)
        print('\n')  # adda blank line

    print_challenge(chal["chal_no"], str(chal["chal_desc"]))
    chal = chal["chal_fn"]  # run the callback to start the challenge
    chal()
    print('✅ Test Complete')


if __name__ == '__main__':
    system('cls || clear')
    try:
        from chals_list import chals
        for chal in chals:
            run_challenge(chal)
        print()
        Exception('✅ All Challenges Complete')
    except:
        print('\n')
        print('🤯 OK leaving')
        exit()
