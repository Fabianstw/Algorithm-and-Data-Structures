import copy
import math

graph = []
delta = 0


def read_input():
    global delta
    first_line = input()
    num_vertices, num_lines = int(first_line.split()[0]), int(first_line.split()[1])

    for _ in range(num_vertices):
        graph.append([0 for _ in range(num_vertices)])

    for i in range(len(graph)):
        graph[i][i] = 0

    for i in range(num_lines):
        get_input = input()
        start, end, weight = int(get_input.split()[0]), int(get_input.split()[1]), int(get_input.split()[2])
        graph[start-1][end-1] = weight
        if weight > delta:
            delta = weight


def bfs(graph_s, s, t, min_w=0):
    """
    Find a s-t path
    :param min_w:
    :param graph_s: The graph
    :param s: Starting node
    :param t: End Node terminate if found
    :return: Return a path from s to t if exists
    """
    visited, queue = dict(), [s-1]
    visited[s-1] = (None, math.inf)

    while queue:
        node = queue.pop(0)
        for neighbour, weight in enumerate(graph_s[node]):
            if min_w < weight < math.inf and neighbour not in visited:
                visited[neighbour] = (node, weight)
                queue.append(neighbour)
                if neighbour == t-1:
                    return visited
    if t-1 in visited:
        return visited
    return None


def backtrack_path(visited, s, t):
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


def Ford_Fulkerson_Algorithm():
    global delta
    s = 1
    t = len(graph)
    max_flow = 0
    graph_f = copy.deepcopy(graph)
    while True:
        visited = bfs(graph_f, s, t)
        if visited:
            path, bottleneck = backtrack_path(visited, s, t)
        else:
            break
        max_flow += bottleneck
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]
            graph_f[u][v] -= bottleneck
            graph_f[v][u] += bottleneck

    return max_flow


def find_lowest_2_power(n):
    """
    Find the lowest power of 2 that is greater than n
    :param n: The number
    :return: The lowest power of 2 that is greater than n
    """
    if n > 0:
        return 2 ** math.ceil(math.log(n, 2))
    return 0


def capacity_scaling():
    global delta
    delta = find_lowest_2_power(delta)
    s = 1
    t = len(graph)
    max_flow = 0
    graph_f = copy.deepcopy(graph)
    while delta >= 1:
        visited = bfs(graph_f, s, t, delta-1)
        if visited:
            path, bottleneck = backtrack_path(visited, s, t)
            max_flow += bottleneck
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i + 1]
                graph_f[u][v] -= bottleneck
                graph_f[v][u] += bottleneck
        else:
            delta //= 2

    return max_flow


if __name__ == '__main__':
    read_input()
    f = capacity_scaling()
    print(f)
