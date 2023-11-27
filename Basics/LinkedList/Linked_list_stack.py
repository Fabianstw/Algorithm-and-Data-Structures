"""Stack as Linked List"""

class Node:
    """
    Node for linked list
    """
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Linked_Stack:

    def __init__(self):
        self.head = None

    def push(self, value):
        current_node = self.head
        self.head = Node(value)
        self.head.next = current_node

    def pop(self):
        if self.head:
            self.head = self.head.next

    def insert_element(self, value):
        """Use instead of push to maintain order of sorted linked list"""
        if self.head.val > value:
            self.push(value)
        else:
            curr_node = self.head
            while curr_node.next:
                if curr_node.next.val > value:
                    tmp = curr_node.next
                    curr_node.next = Node(value)
                    curr_node.next.next = tmp
                    return
                else:
                    curr_node = curr_node.next

            curr_node.next = Node(value)

    def print_all(self):
        print("Linked List:")
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end=" --> ")
            current_node = current_node.next
        print("")


class Linked_Queue:

    def __init__(self):
        self.head = None

    def push(self, value):
        current_node = self.head
        self.head = Node(value)
        self.head.next = current_node

    def pop(self):
        """Pop Last element"""
        cur_node = self.head
        while cur_node.next.next:
            cur_node = cur_node.next
        cur_node.next = None
        self.print_all()

    def print_all(self):
        print("Linked List:")
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end=" --> ")
            current_node = current_node.next
        print("")


if __name__ == '__main__':
    ls = Linked_Stack()
    ls.push(10)
    ls.push(5)
    ls.push(3)
    ls.print_all()
    ls.insert_element(1)
    ls.insert_element(7)
    ls.insert_element(20)
    ls.print_all()
