def fizzbuzz():
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
