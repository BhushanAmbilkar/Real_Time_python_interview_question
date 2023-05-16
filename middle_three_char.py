# Write a function to take string as an argument and return the middle 3 characters.

def string(str1):
    string_length = len(str1)

    if string_length % 2 != 0 and string_length >= 3 and isinstance(str1, str):
        middle_three_char = str1[(string_length // 2 - 1):(string_length // 2 + 2)]
        return middle_three_char
    else:
        raise Exception