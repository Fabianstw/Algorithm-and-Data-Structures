"""Balance Algo Abgabe"""


class Stack:
    """
    Implementation of Datastructure Stack (Ger Stapel) in Deutsch
    """

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
            return None

    def is_empty(self):
        if len(self.stack) == 0:
            return True 
        else:
            return False


def verify_data(arr):
    verify_stack = Stack()
    for i in range(len(arr)):
        if verify_stack.top_element() is not None:
            if arr[i] == ")" and verify_stack.top_element() == "(":
                verify_stack.pop_element()
            elif arr[i] == "]" and verify_stack.top_element() == "[":
                verify_stack.pop_element()
            else:
                verify_stack.push_element(arr[i])
        else:
            verify_stack.push_element(arr[i])
    if verify_stack.is_empty():
        return 1
    else:
        return 0


if __name__ == '__main__':
    with open('/Users/fabian/Desktop/Python/Semester 2/Algo 1/final_in.txt', 'r') as f:
        # Read the contents of the file and split it into individual lines
        lines = f.read().splitlines()

    for line in lines:
        line_1 = line.replace("\\", "")
        print(verify_data(list(line_1)))
