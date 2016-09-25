# Define a function that computes the length of a given list or string.
# (without

# using any built in function)


def strlen(string):
    count = 0
    for i in string:
        count += 1
    return count

print(strlen("vaibhav singh"))
print(strlen("BML Munjal University"))
