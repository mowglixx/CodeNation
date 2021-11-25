def coffee_order(size: str, drink: str):
    VALID_SIZES = ['XS', 'S', 'M', 'L', 'XL']
    VALID_DRINKS = ['Tea', 'Intant Coffee', 'Latte', 'Cappuccino', 'Oasis']

    size = str.uppersize()
    drink = drink.title()

    if size in VALID_SIZES and drink in VALID_DRINKS:
        return f'Your {drink.title} is a {size.upper} size.'
    else:
        return 'Invalid Selection Please Try Again'


# Valid order
print(coffee_order('m', 'Tea'))
# Valid order
print(coffee_order('L', 'instant coffee'))
# Invalid order
print(coffee_order('L', 'Magic Juice'))
