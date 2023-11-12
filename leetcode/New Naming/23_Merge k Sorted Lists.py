# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = ListNode(0)
        head.next = curr

        while True:
            minimal = 999999
            index = None
            for i, list_k in enumerate(lists):
                if list_k:
                    if list_k.val < minimal:
                        minimal = list_k.val
                        index = i
            if minimal == 999999:
                break

            new_node = ListNode(lists[index].val)
            curr.next = new_node
            curr = curr.next
            lists[index] = lists[index].next

        return head.next.next


if __name__ == '__main__':
    c = Solution()
    res = c.mergeKLists([[1,4,5],[1,3,4],[2,6]])
    print(res.val)
