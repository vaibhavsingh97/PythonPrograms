# To sort the strings in reverse alphabetical order
def sort(string):
    sorted_string = sorted(list(string))
    for i in range(len(sorted_string)):
        return ''.join(sorted_string[::-1])
print(sort("dacb"))
