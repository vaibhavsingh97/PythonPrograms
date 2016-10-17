# You are given a string and you want to count how many times each letter
# appears. Write a  Python program to accomplish this task using
# dictionaries.
letterCounts = {}
input = input("Enter string: ")
for letter in input:
    letterCounts[letter] = letterCounts.get(letter, 0) + 1
print letterCounts
