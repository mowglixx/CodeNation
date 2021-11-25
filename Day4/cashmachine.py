
#
#
# Dan's 2-in-1 Cash Machine Example
#
#

# which account would you like to check?
acc_number = int(input('which account would you like to check?'))
pin = input('Please input your PIN: ')


cust_data=[
    {'name': 'Mr Thoretical Jones O.B.E.',
    'acc_number': 10000000,
    'pin': '0001',
    'balance': 23.80,
    },
    {'name': 'Miss Sally Smith O.B.E.',
    'acc_number': 10000001,
    'pin': '0002',
    'balance': 923.53,
    },
    {'name': 'Mrs Pat Jones',
    'acc_number': 10000002,
    'pin': '0003',
    'balance': 9.56,
    },
]



def check_for_account():
    global acc_number
    global cust_data
    # if user input a number
    for cust in cust_data:
        if cust['acc_number'] == acc_number:
            return True
    return False

def check_pin():
    global pin
    global cust_data
    global acc_number
    for cust in cust_data:
        if pin == cust['pin'] and acc_number == cust['acc_number']:
            return True
    return False

def show_balance():
    global acc_number
    if check_pin():
        print(1)
        for cust in cust_data:
            print(2)
            if acc_number == cust['acc_number']:
                print(3)
                print(cust['balance'])
    else:
        print('incorrect pin')

def cash_machine():
    global cust_data
    global pin
    global acc_number
    show_balance()
    

cash_machine()