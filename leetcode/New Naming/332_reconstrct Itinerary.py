import copy
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = self.create_graph(tickets)
        stack = ["JFK"]
        edges = len(tickets)
        path = ["" for _ in range(edges)]
        while stack:
            current = stack[-1]
            if current in graph:
                if len(graph[current]) != 0:
                    next_node = graph[current][0]
                    stack.append(next_node)
                    graph[current].remove(next_node)
                else:
                    path[edges-1] = stack.pop()
                    edges -= 1
            else:
                path[edges-1] = stack.pop()
                edges -= 1
        return path[::-1]

    def create_graph(self, tickets: List[List[str]]) -> dict[str, List[str]]:
        graph = dict()
        for ticket in tickets:
            if ticket[0] in graph:
                graph[ticket[0]].append(ticket[1])
            else:
                graph[ticket[0]] = [ticket[1]]
        for key in graph.keys():
            graph[key].sort()
        return graph


if __name__ == '__main__':
    c = Solution()
    print(c.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
