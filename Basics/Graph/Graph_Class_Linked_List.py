"""
Create a Graph Class witht the function insert, neighbours and adjenz
But the do not use a dictionary, use a linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph_Linked:

    def __init__(self):
        self.graph = []

    def add_knoten(self, data):
        if data not in self.graph:
            self.graph.append(Node(data))

        # sort the graph, that the node with the smallest value is at the beginning
        self.graph.sort(key=lambda x: x.data)

    def add_edge(self, node1, node2):
        if node2 == node1:
            return None

        node1 = Node(node1)
        node2 = Node(node2)

        count = 0
        for i in self.graph:
            if i.data == node1.data or i.data == node2.data:
                count += 1

            if count == 2:
                for j in self.graph:
                    if j.data == node1.data:
                        # append node1 to j and keep the other values after j
                        # also check if node1 is already in the list
                        current_node = j.next
                        if current_node is None:
                            j.next = node2
                            break
                        elif current_node.data == node2.data:
                            return None
                        else:
                            while current_node.next is not None:
                                if current_node.data == node2.data:
                                    return None
                                current_node = current_node.next
                            if current_node.data != node2.data:
                                current_node.next = node2
                            else:
                                return None
                            break
                for j in self.graph:
                    if j.data == node2.data:
                        # append node2 to j and keep the other values after j
                        # also check if node2 is already in the list
                        current_node = j.next
                        if current_node is None:
                            j.next = node1
                            break
                        elif current_node.data == node1.data:
                            return None
                        else:
                            while current_node.next is not None:
                                if current_node.data == node1.data:
                                    return None
                                current_node = current_node.next
                            if current_node.data != node1.data:
                                current_node.next = node1
                            else:
                                return None
                            break
                break

    def depth_first_search(self, start_node):
        pass



    def print_full_graph(self):
        for i in self.graph:
            print("Head: ", end="")
            print(i.data, end="  -  Next: ")
            current_node = i.next
            while current_node is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print()


if __name__ == '__main__':
    gl = Graph_Linked()
    gl.add_knoten(1)
    gl.add_knoten(2)
    gl.add_knoten(3)
    gl.add_knoten(4)

    gl.print_full_graph()

    gl.add_edge(2, 3)
    gl.add_edge(1, 2)
    gl.add_edge(2, 4)
    gl.add_edge(2, 5)
    gl.add_edge(2, 4)

    print("")
    print(" ---- ")
    print("")

    gl.print_full_graph()

