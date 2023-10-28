"""
Algo 2 - Übung 3 - Weihnachtsbäume
"""
import copy
import math


class ChristmasTree:

    def __init__(self):
        self.matrix = []
        self.read_input()

        self.graph = []
        self.create_graph()

        self.s = 0
        self.t = len(self.graph)

        output = self.capacity_scaling()
        print(output)

    def matrix_to_adjacency_list(self, matrix):
        adjacency_list = {}
        for i in range(len(matrix)):
            neighbors = []
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    neighbors.append(j)
            adjacency_list[i] = neighbors
        return adjacency_list

    def create_graph(self):
        """
        Creates the graph
        """
        if len(self.matrix) > 0:
            size_of_graph = 2 + len(self.matrix) * len(self.matrix[0]) + len(self.matrix[0]) + len(self.matrix)
        else:
            size_of_graph = 2 + len(self.matrix)
        self.graph = [[0 for _ in range(size_of_graph)] for _ in range(size_of_graph)]

        for i in range(len(self.matrix)):
            self.graph[0][i+1] = 2

        if len(self.matrix) > 0:
            for i in range(len(self.matrix[0])):
                self.graph[size_of_graph - 2 - i][size_of_graph - 1] = 1

        if len(self.matrix) > 0:
            num_list = self.create_matrix(len(self.matrix), len(self.matrix[0]))
        else:
            num_list = []

        if len(self.matrix) > 0:
            for n in range(len(self.matrix)):
                for m in range(len(self.matrix[0])):
                    if self.matrix[n][m] == 0:
                        self.graph[n + 1][1 + len(self.matrix) + num_list[n][m]] = 1
                        self.graph[1 + len(self.matrix) + num_list[n][m]][size_of_graph - len(self.matrix[0]) + m - 1] = 1

    def create_matrix(self, n, m):
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        num = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = num
                num += 1
        return matrix

    def read_input(self):
        """
        Reads the input from the console and returns the values
        """
        first_line = input().split()
        self.matrix = [[0 for _ in range(int(first_line[1]))] for _ in range(int(first_line[0]))]
        whole_input = []
        for i in range(int(first_line[0])):
            whole_input.append(input().split())

        for i in range(len(whole_input)):
            for j in range(len(whole_input[i][0])):
                if whole_input[i][0][j] == "*":
                    self.matrix[i][j] = 1

        return self.matrix

    def bfs(self, graph_s, s, t, min_w=0):
        """
        Find a s-t path
        :param min_w:
        :param graph_s: The graph
        :param s: Starting node
        :param t: End Node terminate if found
        :return: Return a path from s to t if exists
        """
        visited, queue = dict(), [s - 1]
        visited[s - 1] = (None, math.inf)

        while queue:
            node = queue.pop(0)
            for neighbour, weight in enumerate(graph_s[node]):
                if min_w < weight < math.inf and neighbour not in visited:
                    visited[neighbour] = (node, weight)
                    queue.append(neighbour)
                    if neighbour == t - 1:
                        return visited
        if t - 1 in visited:
            return visited
        return None

    def backtrack_path(self, visited, s, t):
        s -= 1
        t -= 1
        path = []
        bottleneck = visited[t][1]
        while True:
            # find the path from s to t in visited
            path.append(t)
            if t == s:
                break
            t = visited[t][0]
            if visited[t][1] < bottleneck:
                bottleneck = visited[t][1]
        return path[::-1], bottleneck

    def find_lowest_2_power(self, n):
        """
        Find the lowest power of 2 that is greater than n
        :param n: The number
        :return: The lowest power of 2 that is greater than n
        """
        if n > 0:
            return 2 ** math.ceil(math.log(n, 2))
        return 0

    def capacity_scaling(self):
        delta = 2
        s = 1
        t = len(self.graph)
        max_flow = 0
        graph_f = copy.deepcopy(self.graph)
        while delta >= 1:
            visited = self.bfs(graph_f, s, t, delta - 1)
            if visited:
                path, bottleneck = self.backtrack_path(visited, s, t)
                max_flow += bottleneck
                for i in range(len(path) - 1):
                    u = path[i]
                    v = path[i + 1]
                    graph_f[u][v] -= bottleneck
                    graph_f[v][u] += bottleneck
            else:
                delta //= 2

        return max_flow

    def print_output(self):
        for gr in self.graph:
            print(gr)


if __name__ == '__main__':

    christmas_tree = ChristmasTree()
