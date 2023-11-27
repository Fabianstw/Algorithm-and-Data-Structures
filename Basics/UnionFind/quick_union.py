"""Implementation of the quick union algorithm for dynamic connectivity problem."""


class QuickUnion:

    def __init__(self, length):
        self.id = list(range(length))

    def find(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, i, j):
        id_i = self.find(i)
        id_j = self.find(j)
        if id_i != id_j:
            self.id[id_i] = id_j

    def print(self):
        print(self.id)


if __name__ == '__main__':
    qu = QuickUnion(10)
    qu.print()
    qu.union(3, 2)
    qu.print()
    qu.union(2, 7)
    qu.print()
    qu.union(5, 4)
    qu.print()
    qu.union(8, 3)
    qu.print()
    # passthrough
