# Given an integer value, return a string with the equivalent English text of

# each digit. For example, an input of 89 results in "eight nine" being

# returned. Return English text with proper usage, i.e., "eighty-nine."

# Restrict values to be between zero and a thousand


def textnumber(num):
    if num < 0 or num > 1000:
        print("Please enter number between 0 and 1000")
        exit(1)

    store = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': "four",
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    num_str = str(num)
    return ' '.join([store[i]for i in num_str])

print(textnumber(100))
print(textnumber(342))
