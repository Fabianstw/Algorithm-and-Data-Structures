def ReverseString(input):
    stack = []
    for i in input:
        stack.append(i)

    while stack:
        print(stack.pop(), end='')


if __name__ == '__main__':
    ReverseString("Hello")  # Output: "olleH"