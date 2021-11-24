# Take the string
# 'jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi'.
# Find the index of a last vowel in the string.


def last_vowel():
    query_string = 'jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi'
    query_string_reversed = query_string[::-1]
    vowels = ['a', 'e', 'i', 'o', 'u']

    # print(letter)

    for vowel in vowels:
        print(query_string_reversed.index(vowel))
        break
