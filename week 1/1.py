# Write a function is_member() that takes a value (i.e. a number, string, etc) x
# and a list of values a, and returns True if x is a member of a, False
# otherwise. (Note that this is exactly what the in operator does)


def is_member(value, list):
    for i in range(len(list)):
        if value == list[i]:
            return True
    return False

x = ['a', 'b', 'c', 'd']
print(is_member('d', x))
print(is_member('o', x))

x = [1, 2, 3, 4, 5]
print(is_member(1, x))
print(is_member(8, x))
