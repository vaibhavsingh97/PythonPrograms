# Define a function max_of_three() that takes three numbers as arguments

# and returns the largest of them


def get_max(x, y, z):
    if(x > y & x > z):
        return x
    elif(y > x & y > z):
        return y
    else:
        return z

print(get_max(1, 2, 3), "is maximum")
print(get_max(5, 4, 2), "is maximum")
