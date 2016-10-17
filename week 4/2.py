# Write a program to implement Parenthesis matching algorithm.


def parenthesisChecker(symbolsString):
    stack = []
    balanced = True
    for index in range(len(symbolsString)):
        symbol = symbolsString[index]
        if symbol == "(":
            stack.append(symbol)
        else:
            if len(stack) == 0:
                balanced = False
            else:
                stack.pop()
    if len(stack) == 0 and balanced:
        return True
    else:
        return False

print (parenthesisChecker('((()))'))
print (parenthesisChecker('(()'))
print (parenthesisChecker('())()))()))'))
