import heapq
import math
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = dict()
        for i in range(n+1):
            graph[i] = []
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        # try with brute force bfs
        # while loop and then for loop over each queue element


if __name__ == '__main__':
    g = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    c = Solution()
    print(c.findCheapestPrice(4, g, 0, 3, 1))
