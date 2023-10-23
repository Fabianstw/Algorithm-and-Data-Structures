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


def bfs(graph_s, s, t):
    """
    Find a s-t path
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
            if 0 < weight < math.inf and neighbour not in visited:
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


def capacity_scaling():
    global delta
    s = 1
    t = len(graph)
    count = 0
    max_flow = 0
    """
    FOREACH edge e∈E: f(e)←0.
    """
    f_e = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    graph_f = copy.deepcopy(graph)
    while True:
        count += 1
        if count > 10:
            break
        visited = bfs(graph_f, s, t)
        if visited:
            path, bottleneck = backtrack_path(visited, s, t)
        else:
            break
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]

            graph_f[u][v] -= bottleneck
            graph_f[v][u] += bottleneck

    return max_flow


if __name__ == '__main__':
    read_input()
    f = capacity_scaling()
    summe = 0
    for a in f:
        summe += a[-1]

    print(summe)

