# class stack():
#
#     def __init__(self):
#         self.items = []
#
#     def push():
#         self.items.append(item)
#
#     def pop():
#         return self.items.pop()
#
#     def isEmpty():
#         return (self.items == [])
#
#
# def parenthesisChecker(symbolsString):
#     s = stack()
#     balanced = True
#     for index in range(len(symbolsString)):
#         symbol = symbolsString[index]
#         if symbol == "(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 s.pop()
#     if s.isEmpty() and balanced:
#         return True
#     else:
#         return False
#
# print parenthesisChecker('((()))')
# print parenthesisChecker('(()')
import collections

print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)
