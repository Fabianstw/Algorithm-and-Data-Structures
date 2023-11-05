"""
Aufgabe 2 Blatt 4 Algorithmen und Datenstrukturen 2
"""


class Node:
    """
    Node class
    """
    def __init__(self, value, head):
        self.value = value
        self.head = head
        self.size = 1
        self.next = None


class UnionFind:
    """
    Union Find data structure with Node class
    """
    def __init__(self, n):
        self.nodes = [Node(i, None) for i in range(n)]
        for i in range(n):
            self.nodes[i].head = self.nodes[i]

    def find(self, x):
        """
        Find the head of the union
        :param x:
        :return:
        """
        return self.nodes[x].head

    def union(self, A, B):
        """
        Change all heads of the smaller union to the bigger union
        :param A:
        :param B:
        :return:
        """
        if self.nodes[A].head.size > self.nodes[B].head.size:
            self.nodes[B].head = self.nodes[A].head
            self.nodes[A].head.size += self.nodes[B].head.size
            # change all heads of the smaller union to the bigger union
            while self.nodes[B].next:
                self.nodes[B].head = self.nodes[A].head
                self.nodes[B] = self.nodes[B].next
        else:
            self.nodes[A].head = self.nodes[B].head
            self.nodes[B].head.size += self.nodes[A].head.size
            # change all heads of the smaller union to the bigger union
            while self.nodes[A].next:
                self.nodes[A].head = self.nodes[B].head
                self.nodes[A] = self.nodes[A].next

    def sameSet(self, x, y):
        """
        Check if two nodes are in the same union
        :param x:
        :param y:
        :return:
        """
        return self.nodes[x].head == self.nodes[y].head


if __name__ == '__main__':
    test = UnionFind(10)
    test.union(1, 2)
    test.union(2, 3)
    test.union(3, 4)
    test.union(6, 5)
    test.union(6, 3)
    print(test.nodes[6].head.value)

