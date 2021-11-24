#
# IfElse Statments / Conditional Branches
#

#####################################################
#                  Basic Syntax                     #
#####################################################
do = print
this = True

print("""Syntax:
do = print
this = True

if this == True:
    do('This')
else:
    do('That')""")
print('Result:')
if this == True:
    do('This')
else:
    do('That')
print('\n\n')

#####################################################
#                 Working Example                   #
#####################################################
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

else:
    print("I can't serve you.")
    # print the reasons why
    print('Reasons:')
    if country.upper() != VALID_COUNRTY:
        print(
            f"{country.upper()} is not a valid country, Valid countries: {VALID_COUNRTY}"
        )
    if age < LEGAL_AGE:
        print(
            f"\"{age}\" is not old enough, You need to be {LEGAL_AGE} or above."
        )
