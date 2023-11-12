from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for index in range(len(cost)):
            if index >= 2:
                if cost[index - 1] < cost[index - 2]:
                    cost[index] += cost[index - 1]
                else:
                    cost[index] += cost[index - 2]
        return min(cost[len(cost) - 1], cost[len(cost) - 2])


if __name__ == '__main__':
    c = Solution()
    print(c.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))