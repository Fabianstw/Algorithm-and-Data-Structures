"""Find all ways from one point to another in a graph"""


def find_all_ways(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    ways = []
    for node in graph[start]:
        if node not in path:
            new_ways = find_all_ways(graph, node, end, path)
            for new_way in new_ways:
                ways.append(new_way)
    return ways


if __name__ == '__main__':
    graph = {
        "A": ["B", "S", "H"],
        "B": ["A", "C", "G"],
        "C": ["B", "E"],
        "D": ["E", "F", "S"],
        "E": ["C", "D", "I"],
        "F": ["D", "G", "T"],
        "G": ["B", "F", "H", "T"],
        "H": ["A", "G", "I"],
        "I": ["E", "H", "J"],
        "J": ["I", "T"],
        "S": ["A", "D", "T"],
        "T": ["F", "G", "J", "S"]
    }

    print(find_all_ways(graph, "A", "T"))
    
    