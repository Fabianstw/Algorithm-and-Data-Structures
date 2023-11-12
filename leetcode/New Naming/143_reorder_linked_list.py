"""
Reoder a linked list 0 , 1, ..., n  als follows
0 , n , 1, n - 1 , ....
Not Modififed in place
"""


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
        head_rev, length = self.reverseList(head)
        new_list = None
        i = 0
        while i < length:
            if i % 2 == 0:
                new_node = ListNode(head.val)
                new_node.next = new_list
                head = head.next
            else:
                new_node = ListNode(head_rev.val)
                new_node.next = new_list
                head_rev = head_rev.next
            new_list = new_node
            i += 1

        l, _ = self.reverseList(new_list)
        return l


    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = None
        counter = 0
        while head is not None:
            counter += 1
            new_node = ListNode(head.val)
            new_node.next = new_list
            new_list = new_node
            head = head.next

        return new_list, counter


if __name__ == '__main__':
    c = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next, node2.next, node3.next = node2, node3, node4

    n = c.reorderList(node1)
    print(n)
    print(n.val)
    print(n.next.val)
    print(n.next.next.val)
    print(n.next.next.next.val)
