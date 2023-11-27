"""BFS"""


def bfs(grid, start=0):
    print(grid)
    visited, queue = {}, [start]
    round = 0
    while queue:
        round += 1
        curr_queue = queue
        queue = []
        for curr_node in curr_queue:
            if curr_node not in visited:
                visited[curr_node] = {"round": round}
                for neighbour in grid[curr_node]:
                    if neighbour not in visited:
                        queue.append(neighbour)

    print(visited)
    return visited


def convert_matrix_list(matrix):
    adj_lst = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count = i*len(matrix) + j
            curr_letter, curr_num = matrix[i][j], count
            adj_lst.update({count: []})
            if i - 1 >= 0:
                if matrix[i - 1][j] != curr_letter:
                    curr_val = adj_lst[curr_num]
                    curr_val.extend([(i - 1) * len(matrix) + j])
                    adj_lst.update({curr_num: curr_val})
            if i + 1 < len(matrix):
                if matrix[i+1][j] != curr_letter:
                    curr_val = adj_lst[curr_num]
                    curr_val.extend([(i+1)*len(matrix) + j])
                    adj_lst.update({curr_num: curr_val})
            if j - 1 >= 0:
                if matrix[i][j - 1] != curr_letter:
                    curr_val = adj_lst[curr_num]
                    curr_val.extend([i * len(matrix) + j - 1])
                    adj_lst.update({curr_num: curr_val})
            if j + 1 < len(matrix[0]):
                if matrix[i][j+1] != curr_letter:
                    curr_val = adj_lst[curr_num]
                    curr_val.extend([i * len(matrix) + j + 1])
                    adj_lst.update({curr_num: curr_val})
    return adj_lst


if __name__ == '__main__':
    test_list = [["A", "A", "A", "B", "A"],
                 ["B", "B", "B", "B", "B"],
                 ["A", "A", "A", "A", "A"],
                 ["B", "B", "B", "B", "B"],
                 ["A", "B", "A", "B", "A"]]

    graph = convert_matrix_list(matrix=test_list)

    print(graph)

    result = bfs(graph, 0)

    res = result[24]["round"]
    try:
        print(f'''The fastest way is with {res} steps''')
    except KeyError:
        print("no way")
