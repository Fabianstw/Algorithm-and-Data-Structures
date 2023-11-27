"""Creating a Gittergraph for a labyrinth and check if it is nice"""


def pretty_graph(grid, start=1):

    visited = {start: {"round: ": 0}}
    parents = {start: None}
    queue = [start]
    counter = 0

    while queue:
        counter += 1
        curr_queue = queue
        queue = []
        for q in curr_queue:
            for neighbour in grid[q]:
                if neighbour not in visited:
                    visited[neighbour] = {"round: ": counter}
                    parents[neighbour] = q
                    queue.append(neighbour)
                elif parents[q] != neighbour:
                    return False

    # repeat why parents is the key, rest was easy
    print(parents)

    if len(visited) != len(grid):
        return False

    if max(grid) not in visited:
        return False

    return True


if __name__ == '__main__':
    # create an adjacency list based on the labyrinth
    graph_ugly = {
        1: [2, 7],
        2: [1, 3, 8],
        3: [2],
        4: [5, 10],
        5: [4, 6],
        6: [5],
        7: [1, 13],
        8: [2, 9, 14],
        9: [8, 10],
        10: [4, 9, 16],
        11: [12, 17],
        12: [11, 18],
        13: [7, 19],
        14: [8],
        15: [21],
        16: [10, 22],
        17: [11, 23],
        18: [12, 24],
        19: [13, 20, 25],
        20: [19, 21],
        21: [15, 20],
        22: [16, 28],
        23: [17, 29],
        24: [18, 30],
        25: [19, 31],
        26: [27],
        27: [26, 28],
        28: [22, 27, 34],
        29: [23, 35],
        30: [24, 36],
        31: [25, 32],
        32: [31, 33],
        33: [32, 34],
        34: [28, 33],
        35: [29],
        36: [30]
    }

    # tasked based a nice labyrinth
    graph_pretty = {
        1: [2],
        2: [1, 3, 8],
        3: [2],
        4: [5, 10],
        5: [4, 6],
        6: [5],
        7: [13],
        8: [2, 9, 14],
        9: [8, 10],
        10: [4, 9, 16],
        11: [12, 17],
        12: [11, 18],
        13: [7, 19],
        14: [8],
        15: [21],
        16: [10, 22],
        17: [11, 23],
        18: [12, 24],
        19: [13, 20, 25],
        20: [19, 21],
        21: [15, 20],
        22: [16, 28],
        23: [17, 29],
        24: [18, 30],
        25: [19, 31],
        26: [27],
        27: [26, 28],
        28: [22, 27, 34],
        29: [23, 35],
        30: [24, 36],
        31: [25, 32],
        32: [31, 33],
        33: [32, 34],
        34: [28, 33, 35],
        35: [29],
        36: [30]
    }

    print(pretty_graph(graph_pretty))
