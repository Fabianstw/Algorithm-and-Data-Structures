"""Implement a Stack as a linked list"""
from typing import Optional


class Node:
    """
    Node for linked list
    """
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


class Stack:

    def __init__(self, head=None):
        self.head = head

    def print_all(self):
        print("Linked List:")
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end=" --> ")
            current_node = current_node.next
        print("")

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # pop
    def pop(self):
        if self.head is None:
            return False
        else:
            curr_node = self.head
            while curr_node.next.next is not None:
                curr_node = curr_node.next
            curr_node.next = None


class Stack_2:

    def __init__(self):
        self.head = None

    def push(self, value):
        tmp = self.head
        self.head = Node(value)
        self.head.next = tmp

    def pop(self):
        if self.head is None:
            return None
        else:
            tmp = self.head
            self.head = self.head.next
            return tmp.val

    def print_all(self):
        print("Linked List:")
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end=" --> ")
            current_node = current_node.next
        print("")


def reverse_linked_list(stack_list1: Optional[Node]):

    res = None
    while stack_list1 is not None:
        new_node = Node(stack_list1.val)
        if res is None:
            res = new_node
        else:
            new_node.next = res
            res = new_node
        stack_list1 = stack_list1.next

    return res

if __name__ == '__main__':
    # crete a linked list with nodes only
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)

    a = reverse_linked_list(node1)

    print(a.val)
    print(a.next.val)
    print(a.next.next.val)