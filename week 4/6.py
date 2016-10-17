# Take a dictionary as input and return another dictionary as output , but the values of first
# dictionary are now the keys of second dictionary and vice versa
dict1 = {"a": "A", "b": "B", "c": "C"}
dict2 = {}
for i in dict1:
    dict2[dict1.get(i)] = i
print dict2
