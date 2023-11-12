"""Rerverse Linked List"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = None
        while head is not None:
            new_node = ListNode(head.val)
            new_node.next = new_list
            head = head.next

