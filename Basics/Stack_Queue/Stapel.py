"""Implementation of Stack in Python"""


class Stack:

    def __init__(self):
        self.stack = []

    def push_element(self, number):
        self.stack.append(number)

    def pop_element(self):
        self.stack.pop()

    def top_element(self):
        if not self.is_empty():
            return self.stack[len(self.stack) - 1]
        else:
            return "is empty"

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


stack = Stack()
print(stack.is_empty())
print(stack.top_element())
stack.push_element(10)
print(stack.is_empty())
stack.push_element(15)
stack.push_element(20)
print(stack.top_element())
stack.pop_element()
print(stack.top_element())
stack.push_element(10)
