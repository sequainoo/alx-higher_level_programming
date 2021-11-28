#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    roman_string = roman_string.upper()
    mapping = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    i = 0
    # for each roman letter get the integer correspondence
    while i < len(roman_string):
        letter = roman_string[i]
        number = mapping[letter]

        # get the next number
        next_number = 0
        # if index is less than the last index
        if i < len(roman_string) - 1:
            next_number = mapping[roman_string[i+1]]

        # if the current letter >= the next
        if number >= next_number:
            integer += number
        else:
            integer -= number
        i += 1
    return integer
