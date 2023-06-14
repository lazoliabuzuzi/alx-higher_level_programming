#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    result = 0
    last_value = 0

    for letter in roman_string:
        if letter not in roman_values:
            return 0

        present_value = roman_values[letter]

        if present_value > last_value:
            result += present_value - 2 * last_value
        else:
            result += present_value

        last_value = present_value

    return result
