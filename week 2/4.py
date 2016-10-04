# Determine if a string is palindromic (the same backwards as it is for

# wards). Add code to suppress symbols and white space if you want to

# process anything other than strict palindromes


def is_pallindromeString(string):
    String1 = string.lower()
    String2 = is_reverse(string)
    if String1 == String2:
        return True
    return False


def is_reverse(string):
    return string[::-1]

print(is_pallindromeString("radar"))
