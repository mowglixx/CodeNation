# Challenge 0
#
# Compare variables to numbers (intergers) to
# satisfy an if condition, num > 18 in this
# example age has to be greater than 18 and
# the valid country is "uk"


def drinking_age_checker():
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
        if age < LEGAL_AGE:
            print(
                f"\"{age}\" is not old enough, You need to be {LEGAL_AGE} or above."
            )
        # Function Complete
        return False
