def convertToOtherBase(number, base):
    stack = []
    while number > 0:
        stack.append(number % base)
        number = number // base

    while stack:
        print(stack.pop(), end=',')


convertToOtherBase(233, 2)