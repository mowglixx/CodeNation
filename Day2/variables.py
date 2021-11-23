# "one-liner" method
print("8th Letter:", "All Around the World"[7].upper())

# declaring a string variable
statement = "All Around the World"

# using a variable instead of the string in our print statement
print(f'8th Letter: {statement[7].upper()}')
print(
    '8th Letter: {}'
    .format(
        statement[7].upper()
    )
)

my_name = "Dan M"
my_age = 31
my_student_status = True

user= {"name": my_name, "age": my_age, "isStudent": my_student_status}

print("{} loves the fact that he is {}".format(my_name, my_age))
print(f"{my_name} loves the fact that he is {my_age}")


def user(user={"name": "Dan M", "age": 31, "isStudent": True}):
    # Assigning variables names within a list
    return user


details = {"name": "Curious George", "age": 83, "isStudent": False}

# create a user object
User = user(details)
# print the User touple
print(User)
# print
print(f"Georges name: {User['name']}")
