"""algo exam task"""


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_stack:

    def __init__(self):
        self.stack = None

    def push(self, value):
        if self.stack:
            new_node = Node(value)
            new_node.next = self.stack
            self.stack = new_node
        else:
            self.stack = Node(value)

    def pop(self):
        if self.stack:
            if self.stack.next:
                self.stack = self.stack.next
            else:
                self.stack = None
        else:
            raise IndexError("Not available")

    def get_head(self):
        if self.stack:
            print(self.stack.value)
        else:
            raise IndexError("Not available")


if __name__ == '__main__':
    listNode = Linked_stack()
    listNode.push(1)
    listNode.push(2)
    listNode.get_head()
    listNode.pop()
    listNode.push(3)
    listNode.get_head()
    listNode.pop()
    listNode.get_head()
