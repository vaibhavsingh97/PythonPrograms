# Write a program which can compute the factorial of given numbers.

# The results should be printed in a comma-separated sequence on a

# single line.


def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)

print(fact(5))
