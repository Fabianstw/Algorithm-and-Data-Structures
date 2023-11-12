"""Adding numbers presented als linked lists"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_1 = 0
        res_2 = 0
        i = 1
        while l1 is not None:
            res_1 += l1.val*i
            l1 = l1.next
            i *= 10
        i = 1
        while l2 is not None:
            res_2 += l2.val*i
            l2 = l2.next
            i *= 10

        res = res_2 + res_1
        digits = list(str(res))

        res_lst = ListNode(digits[0])
        for i in range(1, len(digits)):
            new_node = ListNode(digits[i])
            new_node.next = res_lst
            res_lst = new_node

        return res_lst



if __name__ == '__main__':
    # create a listnode which looks like this [2,4,3]
    l1_a = ListNode(2, ListNode(4, ListNode(3)))
    l2_a = ListNode(5, ListNode(6, ListNode(4)))

    sol = Solution()
    sol.addTwoNumbers(l1_a, l2_a)
