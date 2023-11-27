"""Maximaler Spannbaum"""


class Union_Find:

    def __init__(self, length):
        self.id = [i for i in range(length)]
        self.size = [1 for _ in range(length)]

    def find(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, i, j):
        id_i = self.find(i)
        id_j = self.find(j)
        if id_i != id_j:
            if self.size[id_i] == self.size[id_j]:
                self.id[i] = id_j
                self.size[id_j] += 1
            else:
                if self.size[id_i] < self.size[id_j]:
                    self.id[i] = id_j
                    self.size[id_j] += 1
                else:
                    self.id[j] = id_i
                    self.size[id_i] += 1


def maximaler_spannbaum(graph):
    union, edges, e, i, result = Union_Find(length=len(graph)+1), [], 0, 0, []
    for i in graph:
        for edge in graph[i]:
            edges.append((i, edge[0], edge[1]))

    sorted_edges = sorted(edges, key=lambda item: -item[2])
    i = 0
    while e < len(graph)-1:
        vert_1, vert_2, weight = sorted_edges[i][0], sorted_edges[i][1], sorted_edges[i][2]
        i += 1
        union_1 = union.find(vert_1)
        union_2 = union.find(vert_2)

        if union_1 != union_2:
            e += 1
            result.append(sorted_edges[i-1])
            union.union(union_1, union_2)

    return result


if __name__ == '__main__':
    # create a graph als adjency list
    # first value in the vertex and second is the weight
    graph = {0: [(1, 7), (2, 2)],
             1: [(0, 1), (2, 4)]}

    print(maximaler_spannbaum(graph))
