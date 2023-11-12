# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = []
        while True:
            dummy = None
            tmp = head
            counter = 0
            for i in range(k):
                if head:
                    counter += 1
                    curr = ListNode(head.val)
                    curr.next = dummy
                    dummy = curr
                    head = head.next
            if head:
                res.append(dummy)
            else:
                print(counter)
                if counter % k == 0:
                    res.append(dummy)
                else:
                    res.append(tmp)
                break

        new_node = ListNode()
        curr = ListNode()
        new_node.next = curr

        for re in res:
            while re:
                curr.next = re
                curr = curr.next
                re = re.next

        return new_node.next.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(5)

    c = Solution()
    ans = c.reverseKGroup(l1, 2)

    print(ans.next.next.val)
