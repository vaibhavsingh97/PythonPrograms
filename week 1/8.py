# Define a function sum() and a function multiply() that sums and multiplies

#(respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4])

# should return 10, and multiply([1, 2, 3, 4]) should return 24


def sum(num):
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    return sum


def multiply(num):
    mul = 1
    for i in range(len(num)):
        mul *= num[i]
    return mul

print(sum([1, 2, 3]))
print(multiply([1, 2, 3, 4]))
