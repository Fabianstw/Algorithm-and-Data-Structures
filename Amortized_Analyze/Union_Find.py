"""
Aufgabe 2 Blatt 4 Algorithmen und Datenstrukturen 2
"""


class Node:

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
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A != root_B:
            if self.size[root_A] < self.size[root_B]:
                self.parent[root_A] = root_B
                self.size[root_B] += self.size[root_A]
            else:
                self.parent[root_B] = root_A
                self.size[root_A] += self.size[root_B]

    def sameSet(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    test = UnionFind(10)
    test.union(1, 2)
    test.union(2, 3)
    print(test.parent)
