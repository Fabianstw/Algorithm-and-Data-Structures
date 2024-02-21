from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        pass

    def create_graph(self, pairs: List[List[str]]) -> dict[str, List[str]]:
        graph = dict()
        for pair in pairs:
            if pair[1] in graph:
                graph[pair[1]].append(pair[1])
            else:
                graph[pair[0]] = [pair[1]]
        for key in graph.keys():
            graph[key].sort()
        return graph


if __name__ == '__main__':
    c = Solution()
    print(c.validArrangement([[5,1],[4,5],[11,9],[9,4]]))
