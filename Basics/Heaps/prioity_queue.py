"""Trying prioity queue in python"""

class double_linked_list:

    def __init__(self, key):
        self.key = key
        self.value = "idc"
        self.next = None
        self.prev = None


class priority_queue:

    def __init__(self):
        self.head = None

    def max(self):
        return self.head.key

    def extract_max(self):
        max = self.head
        self.head = self.head.next
        return max

    def insert(self, key):
        # keep a decreasing order
        new_node = double_linked_list(key)
        if self.head is None:
            self.head = new_node
            return
        if self.head.key < key:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None and curr.next.key > key:
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        curr.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        return

    def print(self):
        # print in one line with arrow
        curr = self.head
        while curr is not None:
            print(curr.key, end=" <--> ")
            curr = curr.next
        print("None")


if __name__ == '__main__':
    c = priority_queue()
    c.insert(1)
    c.insert(2)
    c.insert(3)
    c.insert(4)
    c.insert(1)
    c.insert(5)
    c.insert(10)
    c.insert(7)
    c.print()
    print(c.max())
    print(c.extract_max().key)
    c.print()
