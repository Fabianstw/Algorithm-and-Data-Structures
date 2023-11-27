"""Create a Graph Class witht the function insert, neighbours and adjenz"""


class Graph:

    def __init__(self):
        self.graph = {}

    def insert(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def conect_nodes(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        else:
            return None

    def neighbours(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return None

    def adjenz(self):
        return self.graph

    def __str__(self):
        return str(self.graph)


if __name__ == '__main__':
    g1 = Graph()
    g1.insert(1)
    g1.insert(2)
    g1.insert(3)
    g1.insert(4)
    g1.insert(4)

    g1.conect_nodes(1, 2)
    g1.conect_nodes(1, 3)
    g1.conect_nodes(3, 4)

    h = g1.adjenz()
    for i in h:
        print(i, " -> ", h[i])

    print()
    print(g1.neighbours(1))
