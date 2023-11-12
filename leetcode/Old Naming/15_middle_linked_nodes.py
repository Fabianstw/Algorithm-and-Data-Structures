"""Find the middle of a linked nodes"""
from typing import Optional


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

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow.next



if __name__ == '__main__':
    # generate a linked list with nodes only
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    #node.next.next.next.next.next = ListNode(5)

    new_node = middleNode(node)
    new_node.print_all()
