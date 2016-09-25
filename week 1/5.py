# Write a function that takes a character (i.e. a string of length 1) and
# returns

# True if it is a vowel, False otherwise


def is_vowel(string):
    v = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(v)):
        if string == v[i]:
            return True
    return False

print(is_vowel("e"))
print(is_vowel("z"))
