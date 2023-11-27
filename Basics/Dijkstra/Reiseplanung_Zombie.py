"""Aufgabe Algo Reiseplanung zu Zombiezeiten Abgabe"""
import copy

"""Wir können davon ausgehen, dass der Graph azyklisch ist, da es keinen Sinn macht, auf dem Weg von einer Stadt in
eine andere im Kreis zu laufen."""


def topological_sorting(adj_nc, order=None):
    adj = copy.deepcopy(adj_nc)
    if order is None:
        order = []
    in_degree = set()
    for neighbours in adj:
        for node in adj[neighbours]:
            in_degree.add(node[0])

    dict_key = list(adj.keys())
    for key in dict_key:
        if key not in in_degree:
            order.append(key)
            del adj[key]
            if len(adj) > 0:
                topological_sorting(adj, order)
                return order
            else:
                return order


def heaviest_way(adj,topo_order, start_node):
    longest = [[-1, 0] for _ in range(len(adj) + 1)]

    for order in topo_order:
        # get neighbours of current node
        neighbours = adj[order]
        for neigh in neighbours:
            if longest[neigh[0]][0] < longest[order][0] * neigh[1]:
                if longest[order][0] == -1:
                    longest[neigh[0]][0] = neigh[1]
                else:
                    longest[neigh[0]][0] = longest[order][0] * neigh[1]
                longest[neigh[0]][1] = order

    print(longest)


if __name__ == '__main__':

    graph = {
        0: [(2, 0.1)],
        1: [(4, 0.5)],
        2: [(1, 0.2), (3, 0.7), (4, 0.5)],
        3: [(1, 0.1), (4, 0.9)],
        4: []
    }
    order = topological_sorting(graph)
    heaviest_way(graph, order, 2)
