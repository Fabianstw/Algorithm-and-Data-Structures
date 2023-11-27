

class Stack_avg:

    def __init__(self):
        self.avg = 0
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.avg += value
        self.size += 1

    def avg_func(self):
        return self.avg / self.size

    def pop(self):
        value = self.stack.pop()
        self.size -= 1
        self.avg -= value
        return value
    