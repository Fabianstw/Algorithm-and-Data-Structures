"""Find a palindromic way from one point to another"""

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_colors = {}

    def add_edge(self, u, v, color):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

        self.edge_colors[(u, v)] = color
        self.edge_colors[(v, u)] = color

    def get_neighbors(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        return []

    def get_edge_color(self, u, v):
        return self.edge_colors.get((u, v), None)

    def print_graph(self):
        print(self.adjacency_list)
        print(self.edge_colors)


if __name__ == '__main__':
    # create a graph for palindrom_way
    graph = Graph()
    graph.add_edge("A", "B", "red")
    graph.add_edge("B", "C", "red")
    graph.add_edge("A", "S", "red")
    graph.add_edge("S", "C", "blue")
    graph.add_edge("S", "D", "blue")
    graph.add_edge("D", "E", "blue")
    graph.add_edge("E", "F", "blue")
    graph.add_edge("F", "G", "red")
    graph.add_edge("G", "H", "red")
    graph.add_edge("G", "I", "blue")
    graph.add_edge("I", "J", "blue")
    graph.add_edge("J", "T", "red")
    graph.add_edge("T", "H", "red")
    graph.add_edge("A", "H", "blue")
    graph.add_edge("B", "G", "blue")
    graph.add_edge("C", "E", "blue")
    graph.add_edge("G", "T", "blue")
    graph.add_edge("E", "I", "red")

    graph.print_graph()
    