"""Rollentreppen und Aale als DAG"""


def dfs_to_last_node(grid: dict, start=1):
    start_node, round_counter = start, 0
    queue, visited_nodes = [start_node], {start_node: "round: 0"}

    while len(queue) > 0:
        round_counter += 1
        current_queue = queue
        queue = []
        for node in current_queue:
            for neighbour in grid[node]:
                if neighbour not in visited_nodes:
                    visited_nodes[neighbour] = f"round {round_counter}"
                    queue.append(neighbour)
    return visited_nodes


if __name__ == '__main__':
    graph = {
        1: [2, 3, 13, 5, 6],
        2: [3, 13, 5, 6, 7],
        3: [13, 5, 6, 7, 8],
        4: [5, 6, 7, 8, 17],
        5: [6, 7, 8, 17, 10],
        6: [7, 8, 17, 10, 21],
        7: [8, 17, 10, 21, 12],
        8: [17, 10, 21, 12, 13],
        9: [10, 21, 12, 13, 24],
        10: [21, 12, 13, 24, 15],
        11: [12, 13, 24, 15, 8],
        12: [13, 24, 15, 8, 17],
        13: [24, 15, 8, 17, 18],
        14: [15, 8, 17, 18, 1],
        15: [8, 17, 18, 1, 20],
        16: [17, 18, 1, 20, 21],
        17: [18, 1, 20, 21, 18],
        18: [1, 20, 21, 18, 23],
        19: [20, 21, 18, 23, 24],
        20: [21, 18, 23, 24, 25],
        21: [18, 23, 24, 25],
        22: [23, 24, 25],
        23: [24, 25],
        24: [25],
        25: [],
    }

    result = dfs_to_last_node(graph)
    print(max(result))
    print(result[25])
