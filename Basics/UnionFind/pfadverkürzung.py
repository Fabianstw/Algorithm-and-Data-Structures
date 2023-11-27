"""Pfadverkürzung"""


class Pfadverkürzung:

    def __init__(self, length):
        self.id, self.size = [], []
        for x in range(length):
            self.id.append(x)
            self.size.append(1)

    def find(self, i):
        tmp = []
        while i != self.id[i]:
            tmp.append(i)
            i = self.id[i]
        for value in tmp:
            self.id[value] = i
        return i

    def union(self, i, j):
        id_i = self.find(i)
        id_j = self.find(j)
        if id_i != id_j:
            if self.size[id_i] < self.size[id_j]:
                self.id[id_i] = id_j
                self.size[id_j] += self.size[id_i]
            elif self.size[id_i] > self.size[id_j]:
                self.id[id_j] = id_i
                self.size[id_i] += self.size[id_j]
            else:
                self.id[id_i] = id_j
                self.size[id_j] += self.size[id_i]

    def print(self):
        print(self.id)


if __name__ == '__main__':
    qu = Pfadverkürzung(10)
    qu.print()
    qu.union(6, 3)
    qu.print()
    qu.union(7, 6)
    qu.print()
    qu.union(0, 1)
    qu.print()
    qu.union(0, 6)
    qu.print()
    print(qu.find(0))
    qu.print()