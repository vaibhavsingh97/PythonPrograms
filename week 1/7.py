# Define a function is_palindrome() that recognizes palindromes (i.e. words

# that look the same written backwards). For example, is_palindrome("radar")

# should return True


def is_reverse(string):
    list(string)
    for i in range(len(string)):
        return string[::-1]


def is_palindrome(string):
    if is_reverse(string) == string:
        return True
    return False

print(is_palindrome("radar"))
print(is_palindrome("date"))
