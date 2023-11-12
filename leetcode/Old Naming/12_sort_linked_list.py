"""Sort Linked List in ascending order"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all_nodes(self):
        print("Linked List: ")
        current_node = self
        while current_node is not None:
            if current_node.next is not None:
                print(current_node.val, end=" --> ")
            else:
                print(current_node.val)
            current_node = current_node.next


def sortList_2(head: Optional[ListNode]) -> Optional[ListNode]:
    to_sort_lst = []
    while head is not None:
        # sort via insertion sort directly
        value = head.val
        if len(to_sort_lst) == 0:
            to_sort_lst.append(value)
        else:
            start = 0
            end = len(to_sort_lst)
            while start < end:
                mid = (start + end) // 2
                if to_sort_lst[mid] == value:
                    to_sort_lst.insert(mid, value)
                    break
                elif to_sort_lst[mid] < value:
                    start += 1
                else:
                    end -= 1
                if start == end:
                    to_sort_lst.insert(start, value)
                    break
        head = head.next

    if len(to_sort_lst) > 0:
        res = ListNode(to_sort_lst[len(to_sort_lst) - 1])
        i = len(to_sort_lst) - 2
        while i >= 0:
            new_node = ListNode(to_sort_lst[i])
            new_node.next = res
            res = new_node
            i -= 1
    else:
        res = []

    return res


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head
    if head.next is None:
        return ListNode(head.val)

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    right_node = slow.next
    slow.next = None

    left_node = sortList(head)
    right_node = sortList(right_node)

    dummy = ListNode(0)
    curr = dummy
    while left_node and right_node:
        if left_node.val < right_node.val:
            curr.next = left_node
            left_node = left_node.next
        else:
            curr.next = right_node
            right_node = right_node.next
        curr = curr.next
    # Append the remaining nodes of the left or right half to the end of the sorted list
    curr.next = left_node or right_node

    return dummy.next


def reverse_linked_list(stack_list1: Optional[ListNode]):
    res = None
    while stack_list1 is not None:
        new_node = ListNode(stack_list1.val)
        if res is None:
            res = new_node
        else:
            new_node.next = res
            res = new_node
        stack_list1 = stack_list1.next

    return res


if __name__ == '__main__':
    # create listnode with values [-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115]
    node = ListNode(-84)
    node.next = ListNode(142)
    node.next.next = ListNode(41)
    node.next.next.next = ListNode(-17)
    node.next.next.next.next = ListNode(-71)
    node.next.next.next.next.next = ListNode(170)
    node.next.next.next.next.next.next = ListNode(186)
    node.next.next.next.next.next.next.next = ListNode(183)
    node.next.next.next.next.next.next.next.next = ListNode(-21)
    node.next.next.next.next.next.next.next.next.next = ListNode(-76)
    node.next.next.next.next.next.next.next.next.next.next = ListNode(76)


    a = sortList(node)
    a.print_all_nodes()

    # do it again but without any normal list
    # do merge sort on the linked list
