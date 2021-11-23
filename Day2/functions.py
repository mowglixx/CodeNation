# define the function
def my_function_name(my_hypothetical_variable):
    print(my_hypothetical_variable)


# After the function definition we can "call"
# the function and hand it some data

my_function_name("This prints a String")


# more functional example below
def add_three_to_this(num):
    # take num and add 3
    num += 3
    # return new num
    return num


# print() is now needed becuase we
# are "returning" a value instead of printing it to the terminal
#
# prints 13 after it is "returned" by the "add_three_to_this" function
print(add_three_to_this(10))
