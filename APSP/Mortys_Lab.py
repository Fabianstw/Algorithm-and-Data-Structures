"""
Algo2 Task to program Mortys Labyrinth
"""
import math

# graph with 11 vertices
graph = [
    [0, 15, 10, 20, math.inf, 31, math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, 0, math.inf, math.inf, 57, 11, math.inf, math.inf, math.inf, math.inf, math.inf],
    [5, -5, 0, math.inf, 15, math.inf, 10, math.inf, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, 0, 10, 1, math.inf, math.inf, math.inf, 200, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 0, math.inf, 8, math.inf, math.inf, math.inf, 100],
    [math.inf, math.inf, math.inf, 20, -1, 0, math.inf, 142, 150, math.inf, math.inf],
    [math.inf, math.inf, math.inf, 15, math.inf, -5, 0, math.inf, math.inf, math.inf, 510],
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf, math.inf, -10],
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0, 5, math.inf],
    [math.inf, 100, 100, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf],
    [math.inf, math.inf, 1, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0]
]

# declare the vertices of fleeb and plumb
start_opts = [1, 2, 3]
fleebs = [8, 9, 10, 11]
plumbs = [4, 5, 6, 7]


def FloydWarshall(matrix):
    """
    Floyd Warshall Algorithm
    """
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix


# calculate the distance for all the vertices
dis_mat = FloydWarshall(graph)

current_min = [math.inf, [None]]

for start_opt in start_opts:
    for fleeb in fleebs:
        for plumb in plumbs:
            if dis_mat[plumb-1][fleeb-1] <= 137:
                tmp_distance = dis_mat[start_opt-1][plumb-1] + dis_mat[plumb-1][fleeb-1] + dis_mat[fleeb-1][start_opt-1]
                if tmp_distance < current_min[0]:
                    current_min = [tmp_distance, [start_opt, plumb, fleeb]]

print(current_min)
print(10-5-1+100+1)
