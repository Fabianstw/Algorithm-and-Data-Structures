"""Merge two sorted link lists"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        curr = self
        while curr:
            print(curr.val)
            curr = curr.next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    res_node = ListNode(0)
    tmp = res_node

    while list1 and list2:
        if list1.val < list2.val:
            new_node = ListNode(list1.val)
            tmp.next = new_node
            tmp = tmp.next
            list1 = list1.next
        else:
            new_node = ListNode(list2.val)
            tmp.next = new_node
            tmp = tmp.next
            list2 = list2.next

    if list1:
        tmp.next = list1
    else:
        tmp.next = list2
    return res_node.next


if __name__ == '__main__':
    # Test mergeTwoLists
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    res = mergeTwoLists(list1, list2)
    res.print_all()
