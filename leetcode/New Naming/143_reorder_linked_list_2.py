"""
Reoder a linked list 0 , 1, ..., n  als follows
0 , n , 1, n - 1 , ....
Not Modififed in place
"""
import copy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        arr = []
        current, length = head, 0
        while current:
            arr.append(current)
            current = current.next
            length += 1

        left, right = 0, length-1
        last = head
        while left < right:
            arr[left].next = arr[right]
            left += 1
            if left == right:
                last = arr[right]
                break

            arr[right].next = arr[left]
            right -= 1

            last = arr[left]

        if last:
            last.next = None

        return head



if __name__ == '__main__':
    c = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next, node2.next, node3.next = node2, node3, node4
    print(node1)
    print(node2)
    print(node3)
    print(node4)
    n = c.reorderList(node1)

    print(n)
    print(n.next)
    print(n.next.next)
    print(n.next.next.next)
