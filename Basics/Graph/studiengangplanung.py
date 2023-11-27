"""Studiengangplanung ALgo Blatt"""


class Studiengangplanung:

    def __init__(self, classes):
        self.classes = classes
        self.plan = self.fastest_way(self.classes)

    def fastest_way(self, grid):
        # find nodes without any edges going in
        calc = set()
        for node in grid:
            for g in grid[node]:
                calc.add(g)

        res = []
        for node in grid:
            if node not in calc:
                res.append(self.bfs_for_else(grid, node))

        final_dict = dict()

        for re in res:
            for r in re:
                if r in final_dict:
                    if final_dict[r] < re[r]:
                        final_dict[r] = re[r]
                else:
                    final_dict[r] = re[r]

        return final_dict

    def bfs_for_else(self, grid, start):
        visited, counter = dict(), 0
        queue = [start]

        while queue:
            counter += 1
            curr_queue = queue
            queue = []
            for curr_node in curr_queue:
                visited[curr_node] = counter
                for neighbour in grid[curr_node]:
                    queue.append(neighbour)

        return visited

    def print_plan(self):
        print(self.plan)


if __name__ == '__main__':
    # create a graph for studiengangplanung
    graph = {
        "E1": ["E2"],
        "E2": [],
        "DE1": ["DE2", "M2"],
        "DE2": ["DE3"],
        "DE3": [],
        "M1": ["M2"],
        "M2": ["M3"],
        "M3": [],
        "G1": ["M1"],
    }

    planung = Studiengangplanung(graph)
    planung.print_plan()
