"""Verkette Liste mit Stack"""

class Node:
    def __init__(self, data):
        self.head = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def pop(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def print_all_nodes(self):
        print("Linked List:")
        current_node = self.head
        while current_node is not None:
            if current_node.next is not None:
                print(current_node.head, end=" --> ")
            else:
                print(current_node.head)
            current_node = current_node.next



# examples
linked_list = Linked_list()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.print_all_nodes()
linked_list.pop()
linked_list.print_all_nodes()
linked_list.push(10)
linked_list.print_all_nodes()
linked_list.pop()
linked_list.pop()
linked_list.print_all_nodes()
linked_list.pop()
linked_list.print_all_nodes()