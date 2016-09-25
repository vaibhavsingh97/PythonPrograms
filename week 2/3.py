# Determine if two strings match (without using comparison operators or

# the cmp() built-in function) by scanning each string. Add case-
# insensitivity to your script


def compare(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    for i, s in enumerate(string1):
        if string2[i] != s:
            return False
    return True

print(compare("abc", "dcv"))
print(compare("abc", "abc"))
