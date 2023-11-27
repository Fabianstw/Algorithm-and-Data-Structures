"""First Implementation of Prims Algorithm"""


import heapq


import heapq


class WeightedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, start_vertex, end_vertex, weight):
        self.add_vertex(start_vertex)
        self.add_vertex(end_vertex)
        self.adj_list[start_vertex].append((end_vertex, weight))
        self.adj_list[end_vertex].append((start_vertex, weight))

    def prim(self):
        min_spanning_tree = {}
        visited = set()
        no_edge = 0
        pq = []

        # Select a random starting vertex
        start_vertex = list(self.adj_list.keys())[0]

        # Initialize priority queue with the starting vertex
        heapq.heappush(pq, (0, None, start_vertex))
        # no edge = no of vertices - 1
        while no_edge < len(self.adj_list) - 1 :
            weight, prev_vertex, vertex = heapq.heappop(pq)

            if vertex not in visited:
                visited.add(vertex)

                if prev_vertex is not None:
                    min_spanning_tree[(prev_vertex, vertex)] = weight
                    no_edge += 1

                for neighbor, edge_weight in self.adj_list[vertex]:
                    if neighbor not in visited:
                        heapq.heappush(pq, (edge_weight, vertex, neighbor))

        return min_spanning_tree


# Example usage
graph = WeightedGraph()
graph.add_edge('A', 'B', 4)
graph.add_edge('B', 'C', 24)
graph.add_edge('A', 'D', 6)
graph.add_edge('D', 'C', 23)
graph.add_edge('A', 'E', 16)
graph.add_edge('E', 'D', 8)
graph.add_edge('E', 'F', 10)
graph.add_edge('E', 'F', 21)
graph.add_edge('D', 'F', 5)
graph.add_edge('C', 'F', 18)
graph.add_edge('C', 'G', 9)
graph.add_edge('H', 'G', 7)
graph.add_edge('G', 'F', 11)
graph.add_edge('H', 'F', 14)

minimum_spanning_tree = graph.prim()
print(minimum_spanning_tree)
