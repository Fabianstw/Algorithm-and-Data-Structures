import math

graph = []
pred = []


def read_input():
    first_line = input()
    num_vertices, num_lines = int(first_line.split()[0]), int(first_line.split()[1])

    for _ in range(num_vertices):
        graph.append([math.inf for _ in range(num_vertices)])
        pred.append([None for _ in range(num_vertices)])

    for i in range(len(graph)):
        graph[i][i] = 0
        pred[i][i] = i+1

    for i in range(num_lines):
        get_input = input()
        start, end, weight = int(get_input.split()[0]), int(get_input.split()[1]), int(get_input.split()[2])
        graph[start-1][end-1] = weight

        pred[start-1][end-1] = start


def basic_dynamic_programming():
    # initialize the matrix
    # not possible to pass the last test on the moodle page
    dist = [[math.inf for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(len(graph)):
        dist[i][i] = 0

    # algo
    for _ in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if u != v:
                    tmp_distance = [dist[u][v]]
                    for x in range(len(graph)):
                        tmp_distance.append(dist[u][x] + graph[x][v])
                    dist[u][v] = min(tmp_distance)

    return dist


def FloydWarshall():

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                current = graph[i][j]
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                if current != graph[i][j]:
                    pred[i][j] = pred[k][j]


def read_file():
    file_path = "/Users/fabian/Desktop/Coding/Semester 3/Algorithm-and-Data-Structures/APSP/aves-wildbird-network-6/aves-wildbird-network-6.edges"
    all_lines = []
    max_number = 0
    with open(file_path, "r") as f:
        # read all lines
        for line in f:
            all_lines.append(line)
            # get the max number
            if int(line.split()[0]) > max_number:
                max_number = int(line.split()[0])
            if int(line.split()[1]) > max_number:
                max_number = int(line.split()[1])

    for _ in range(max_number):
        graph.append([math.inf for _ in range(max_number)])
        pred.append([None for _ in range(max_number)])

    for i in range(len(graph)):
        graph[i][i] = 0
        pred[i][i] = i + 1

    for line in all_lines:
        start, end, weight = int(line.split()[0]), int(line.split()[1]), float(line.split()[2])
        graph[start-1][end-1] = weight

        pred[start - 1][end - 1] = start


if __name__ == '__main__':
    # read_input()
    read_file()
    FloydWarshall()
    for gra in graph:
        for g in gra:
            print(g, end=" ")
        print()
    print()
    for pre in pred:
        for p in pre:
            print(p, end=" ")
        print()
