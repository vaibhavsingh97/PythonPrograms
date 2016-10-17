# Write a program to convert lists into a dictionaries.
def process(list1, list2):
    dict = {}
    if len(list1) == len(list2):
        j = 0
        for i in range(len(list1)):
            dict[list1[i]] = list2[j]
            j = j + 1
        return dict
    else:
        print(
            "The number of items of list is not matching, hence operation is not possible.")

print process([1, 2, 3], ["a", "b", "c"])
print process([1, 2, 3], ["a", "b", "c", "d"])
