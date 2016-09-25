# Write a function,isharshad that determines whether a number is a
# Harshadnumber(for number base 10).
# A Harshad number is an integer that is divisible by the sum of its digits. Example: 81!8 +
# 1 = 9!81=9 = 9!Harshad!


def digit_sum(x):
    sum = 0
    while x > 0:
        rem = x % 10
        sum = sum + rem
        x = x // 10
    return sum


def is_harshadNumber(x):
    if(x % digit_sum(x) == 0):
        return True
    return False

print(is_harshadNumber(18))
print(is_harshadNumber(19))
