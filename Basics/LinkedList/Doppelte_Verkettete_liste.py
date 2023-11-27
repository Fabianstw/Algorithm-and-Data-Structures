"""Klasse für verkette Liste"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_element(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node

    # insert element at the beginning of the list
    def insert_element(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_fist_element(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_last_element(self):
        if self.head is not None:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.prev.next = None

    def delete_element(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
            current_node = current_node.next

    def print_all_nodes(self):
        print("Linked List: ")
        current_node = self.head
        while current_node is not None:
            if current_node.next is not None:
                print(current_node.data, end=" --> ")
            else:
                print(current_node.data)
            current_node = current_node.next


# make a example linked list
linked_list = LinkedList()
linked_list.append_element(1)
linked_list.append_element(2)
linked_list.append_element(3)
linked_list.append_element(20)
linked_list.append_element(5)
linked_list.append_element(10)

linked_list.print_all_nodes()

linked_list.append_element(0)

linked_list.print_all_nodes()

linked_list.delete_element(20)

linked_list.print_all_nodes()

linked_list.delete_fist_element()

linked_list.print_all_nodes()

linked_list.delete_last_element()

linked_list.print_all_nodes()

linked_list.insert_element(100)

linked_list.print_all_nodes()



linked_list.print_all_nodes()
