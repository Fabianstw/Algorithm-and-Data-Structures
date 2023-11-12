"""Remove the nth node from the end of a linked list"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        print("Linked List: ")
        current_node = self
        while current_node is not None:
            if current_node.next is not None:
                print(current_node.val, end=" --> ")
            else:
                print(current_node.val)
            current_node = current_node.next


def removeNthFromEnd_2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    tmp = head
    counter = 0
    while tmp:
        tmp = tmp.next
        counter += 1

    current_node = None

    i = 0
    while head:
        if i != counter - n:
            new_node = ListNode(head.val)
            new_node.next = current_node
            current_node = new_node
        head = head.next
        i += 1

    # reverse
    res_list = None
    while current_node:
        new_node = ListNode(current_node.val)
        new_node.next = res_list
        res_list = new_node
        current_node = current_node.next

    return res_list


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


if __name__ == '__main__':
    # create linked list
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    res = removeNthFromEnd(node, 2)
    res.print_all()
