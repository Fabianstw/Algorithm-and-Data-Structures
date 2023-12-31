# Ford-Fulkerson algorith in Python

from collections import defaultdict

# source
# https://www.programiz.com/dsa/ford-fulkerson-algorithm


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    # Using BFS as a searching algorithm
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * self.ROW
        queue = [s]

        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = []

first_line = input()
num_vertices, num_lines = int(first_line.split()[0]), int(first_line.split()[1])

for _ in range(num_vertices):
    graph.append([0 for _ in range(num_vertices)])

for i in range(len(graph)):
    graph[i][i] = 0

for i in range(num_lines):
    get_input = input()
    start, end, weight = int(get_input.split()[0]), int(get_input.split()[1]), int(get_input.split()[2])
    graph[start - 1][end - 1] = weight

g = Graph(graph)

source = 0
sink = len(graph) - 1

print(g.ford_fulkerson(source, sink))
