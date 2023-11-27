"""Dynamische Zusammenhangskomponente und Suche in Graphen"""

from typing import List


class Datastructure_Graph:

    def __init__(self, length):
        self.graph = {x: [] for x in range(length)}

    def insert(self, i, j):
        if self.connected(i, j) is False:
            self.graph[i].append(j)
            self.graph[j].append(i)

    def connected(self, i, j):
        """Do BFS to check if i and j are connected"""
        visited, queue = {}, [i]
        while len(queue) > 0:
            curr_queue = queue
            queue = []
            for node in curr_queue:
                if node not in visited:
                    visited[node] = 0
                    for neighbour in self.graph[node]:
                        print(neighbour)
                        if neighbour not in visited:
                            if neighbour == j:
                                return True
                            else:
                                queue.append(neighbour)
        return False


if __name__ == '__main__':
    structure = Datastructure_Graph(10)
    structure.insert(1, 2)
    structure.insert(3, 2)
    print(structure.graph)
    print(structure.connected(1, 3))
