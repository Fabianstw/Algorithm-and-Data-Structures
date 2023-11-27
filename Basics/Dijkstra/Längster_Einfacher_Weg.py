"""Längster Einfacher Weg in einem DAG"""
import copy
from typing import List


def topological_search(adj: dict, topo_order=None):
    if topo_order is None:
        topo_order = []
    in_degree = set()
    for i in adj:
        for j in adj[i]:
            in_degree.add(j[0])

    dict_keys = list(adj.keys())
    for key in dict_keys:
        if key not in in_degree:
            topo_order.append(key)
            del adj[key]
            if len(adj) > 0:
                topological_search(adj, topo_order)
                return topo_order
            else:
                return topo_order


def find_longest_way(adj: dict, topo_order: List[int]):
    longest = [[0, 0] for _ in range(len(adj))]

    for order in topo_order:
        # get neighbours of current node
        neighbours = adj[order]
        for neigh in neighbours:
            if longest[neigh[0]][0] < longest[order][0] + neigh[1]:
                longest[neigh[0]][0] = longest[order][0] + neigh[1]
                longest[neigh[0]][1] = order

    print(longest)


if __name__ == '__main__':
    graph = {
        0: [(1, 1), (2, 11)],
        1: [(2, 6), (3, 4), (4, 5)],
        2: [(3, 3), (5, 9)],
        3: [(4, 10), (5, 12), (6, 7)],
        4: [(6, 8)],
        5: [(6, 2)],
        6: []
    }
    new_g = copy.deepcopy(graph)

    topo = topological_search(new_g)
    find_longest_way(graph, topo)
