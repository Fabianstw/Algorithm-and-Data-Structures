"""
Versuch 2
Reiseplanung in Zombiezeiten Algo Abgabe
"""


class Prio_queue:

    def __init__(self):
        self.heap = [(-9999, -9999)]
        self.size = 0

    def insert(self, key, value):
        self.heap.append((key, value))
        self.size += 1
        self.bubble_up(self.size)

    def increase_key(self, i, key):
        if key < self.heap[i][0]:
            raise ValueError("New key is smaller than current key")
        self.heap[i] = (key, self.heap[i][1])
        self.bubble_up(i)

    def increase_key_2(self, i, key):
        # increase the key, where the second value is i
        for values in self.heap:
            if values[1] == i:
                self.increase_key(self.heap.index(values), key)

    def get_max(self):
        return self.heap[1]

    def extract_max(self):
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.bubble_down(1)
        return max

    def bubble_down(self, i):
        while i * 2 <= self.size:
            child = self.max_child(i)
            if self.heap[i][0] < self.heap[child][0]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child

    def bubble_up(self, i):
        while i // 2 > 0:
            if self.heap[i][0] > self.heap[i // 2][0]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i * 2][0] > self.heap[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def print_heap(self):
        print(self.heap)


def heaviest_way(graph, start_node):
    longest = [[-1, 0] for _ in range(len(graph))]
    max_heap = Prio_queue()
    max_heap.insert(-1, start_node)

    max_heap.increase_key_2(start_node, 1)
    while len(max_heap.heap) > 1:
        current_node = max_heap.extract_max()
        for neighbour in graph[current_node[1]]:
            longest, max_heap = relax(current_node[1], neighbour, longest, max_heap)

    print(longest)


def relax(current_node, neighbour, longest, max_heap):
    if longest[neighbour[0]][0] <= longest[current_node][0] * neighbour[1]:
        if longest[current_node][0] == -1:
            longest[neighbour[0]][0] = longest[current_node][0] * neighbour[1] * (-1)
        else:
            longest[neighbour[0]][0] = longest[current_node][0] * neighbour[1]

        longest[neighbour[0]][1] = current_node

        max_heap.insert(longest[neighbour[0]][0], neighbour[0])

    return longest, max_heap


if __name__ == '__main__':
    graph1 = {
        0: [(2, 0.1)],
        1: [(4, 0.9)],
        2: [(1, 0.2), (3, 1), (4, 0.5), (7, 0.9)],
        3: [(1, 0.1), (4, 1), (5, 0.4)],
        4: [(5, 0.1), (7, 1)],
        5: [(6, 0.1)],
        6: [(7, 0.5)],
        7: [(9, 0.7)],
        8: [],
        9: []
    }

    heaviest_way(graph1, 2)
