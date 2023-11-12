# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy.next
        while fast:
            if fast.next and fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next

        return dummy.next



if __name__ == '__main__':
    c = Solution()
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(2)
    node1.next, node2.next, node3.next = node2, node3, node4
    res = c.deleteDuplicates(node1)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)