"""
Implementierung einer Queue mit 2 Stacks und
anschließendem Beweis, dass die amortisierten Kosten konstant sind
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, new_value):
        add_val = Node(new_value)
        add_val.next = self.head
        self.head = add_val


    def pop(self):
        if self.head:
            re_val = self.head.value
            self.head = self.head.next
        else:
            re_val = None
        return re_val
