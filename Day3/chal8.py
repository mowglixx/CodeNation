#
# Challenge 8 (Extra)
#
# Take the string
# 'jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi'.
# Find the index of a last vowel in the string.


def last_vowel():
    big_string = 'jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi'
    VOWELS = ['a', 'e', 'i', 'o', 'u']

    # enumerate the string until no more matches
    for letter_index, letter in enumerate(big_string):
        if letter in VOWELS:
            # update the values when a match is found until no more matches
            last_vowel_found = letter
            last_vowel_found_index = letter_index

    print(f'last_vowel: {last_vowel_found.upper()}')
    print(f'last_vowel_index: {last_vowel_found_index}')
    print(
        f'`big_string[{last_vowel_found_index}]` returns: {big_string[last_vowel_found_index].upper()}')
