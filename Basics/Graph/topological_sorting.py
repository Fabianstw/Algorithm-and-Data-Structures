"""Algorithm for topological sorting on a directed acyclic graph (DAG)"""


def topological_search(adj: dict):

    in_degree = set()
    for i in adj:
        for j in adj[i]:
            in_degree.add(j)
            
    dict_keys = list(adj.keys())
    for key in dict_keys:
        if key not in in_degree:
            print(key)
            del adj[key]
            if len(adj) > 0:
                topological_search(adj)
                return
            else:
                return


if __name__ == '__main__':
    # create a graph as a dictionary based on the current video opened in safari
    graph = {
        0: [1, 2, 3],
        1: [3, 4],
        2: [5],
        3: [2, 5],
        4: [3],
        5: [],
        6: [3, 4, 5]
    }

    topological_search(adj=graph)
