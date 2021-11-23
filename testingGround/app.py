# declaring a string variable
statement = "All Around the World"

# "one-liner" method (old)
print("8th Letter:", "All Around the World"[7].upper())

# using a variable instead of the string in our print statement
print(f'8th Letter: {statement[7].upper()}')
# dot notation using the built-in .format method
# this is built-in to string variables
print('8th Letter: {}'.format(statement[7].upper())
      )

my_name = "Dan M"
my_age = 31
my_student_status = True

user = {"name": my_name, "age": my_age, "isStudent": my_student_status}

print(
    "{} loves the fact that he is {}"
    .format(
        my_name, my_age
    )
)
print(
    f"{my_name} loves the fact that he is {my_age}"
)


def user(user={"name": "Dan M", "age": 31, "isStudent": True}):
    # Assigning variables names within a list
    return user


details = {"name": "Curious George", "age": 83, "isStudent": False}

# create a user object
User = user(details)

print(User)

print(f"User's name: {User['name']}")


def app():
    print('Hello World!')


if __name__ == '__main__':
    app()
