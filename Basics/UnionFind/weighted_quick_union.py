"""Weighted Quick Union"""


class Weighted_Quick_Union:

    def __init__(self, length):
        self.id, self.size = [], []
        for x in range(length):
            self.id.append(x)
            self.size.append(1)

    def find(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, i, j):
        id_i = self.find(i)
        id_j = self.find(j)
        if id_i != id_j:
            if self.size[id_i] < self.size[id_j]:
                self.id[id_i] = id_j
                self.size[id_j] += self.size[id_i]
            else:
                self.id[id_j] = id_i
                self.size[id_i] += self.size[id_j]

    def print(self):
        print(self.id)


if __name__ == '__main__':
    qu = Weighted_Quick_Union(10)
    qu.print()
    qu.union(3, 2)
    qu.print()
    qu.union(2, 7)
    qu.print()
    qu.union(5, 4)
    qu.print()
    qu.union(8, 3)
    qu.print()
    qu.union(1, 0)
    qu.print()
    qu.union(6, 1)
    qu.print()
    qu.union(7, 3)
    qu.print()
    qu.union(5, 1)
    qu.print()
    qu.union(6, 3)
    qu.print()
    # passthrough