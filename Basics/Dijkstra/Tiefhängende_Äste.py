"""Algo Blatt 10 Aufgabe 6 b"""


class Queue:
    """Data Structure for the queue to optimize Dijkstra for this task"""

    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def get_first(self):
        value = self.queue.pop(0)
        return value

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def print(self):
        print(self.queue)


def shortest_way_to_all_other(adj, start):
    """
    Find the shortest way from one to alle other nodes
    Using Dijkstra but not using a heap, instead using a queue
    :param adj:
    :param start:
    :return:
    """
    length, seen = [[0, 0] for _ in range(len(adj))], set()
    queue = Queue()
    queue.add(start)
    seen.add(start)
    while queue.is_empty() is False:
        current_node = queue.get_first()
        seen.add(current_node)
        for node in adj[current_node]:
            if node[0] not in seen:
                queue.add(node[0])
            if node[0] not in seen:
                length[node[0]][0] = length[current_node][0] + node[1]
                length[node[0]][1] = current_node

    return length


if __name__ == '__main__':
    graph = {
        0: [(1, 5), (2, 8)],
        1: [(3, 17), (4, 0)],
        2: [(5, 1)],
        3: [(6, 23)],
        4: [(0, 16)],
        5: [(7, 9), (8, 14)],
        6: [(0, 4)],
        7: [(0, 7)],
        8: [(0, 8)]
    }

    print(shortest_way_to_all_other(graph, 3))
