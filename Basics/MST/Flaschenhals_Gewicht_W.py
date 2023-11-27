"""Prüfe ob es einen Weg gibt der höchsten die breite w hat"""


def modified_bfs(graph, s, t, w):
    """
    :param s: start node
    :param t: end node
    :param w: weight of the minimum edge on the way from s to t
    :return: return of the weight was possible to find way
    """
    visited, queue = set(), [s]
    while queue:
        curr_queue = queue
        queue = []
        for node in curr_queue:
            if node not in visited:
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour[1] > w:
                        if neighbour[0] not in visited:
                            queue.append(neighbour[0])

    if t in visited:
        return False
    return True


if __name__ == '__main__':
    graph = {
        0: [(1, 1), (2, 11)],
        1: [(0, 1), (2, 6), (3, 4), (4, 5)],
        2: [(0, 11), (1, 6), (3, 3), (5, 9)],
        3: [(1, 4), (2, 3), (4, 10), (5, 12), (6, 7)],
        4: [(1, 5), (3, 10), (6, 8)],
        5: [(2, 9), (3, 12), (6, 2)],
        6: [(4, 8), (5, 2), (3, 7)]
    }
    print(modified_bfs(graph, 0, 4, 8))


