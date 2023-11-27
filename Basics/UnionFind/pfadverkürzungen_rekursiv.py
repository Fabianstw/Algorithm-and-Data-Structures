"""Pfadverkürzungen Rekursiv"""


class Pfadverkürzung_rek:

    def __init__(self, length):
        self.id, self.size = [], []
        for x in range(length):
            self.id.append(x)
            self.size.append(1)

    def find(self, i):

        def find_i(i_def):
            tmp_2 = []
            if i_def != self.id[i_def]:
                tmp_2.append(i_def)
                new_values = find_i(self.id[i_def])
                tmp_2.extend(new_values[0])
                i_def = new_values[1]
            return tmp_2, i_def

        def reset(tmp_2, new_i_def):
            if len(tmp_2) > 0:
                value = tmp_2.pop()
                self.id[value] = new_i_def
                reset(tmp, new_i_def)

        tmp, new_i = find_i(i)
        print(new_i)
        reset(tmp, new_i)

        # keep the return
        return new_i

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
    qu = Pfadverkürzung_rek(10)
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