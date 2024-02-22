from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_idx = 0
        index = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            if tank < min_idx:
                min_idx = tank
                index = i+1

        if tank < 0:
            return -1
        return index


if __name__ == '__main__':
    c = Solution()
    print(c.canCompleteCircuit([2,3,4], [3,4,3]))
    print(c.canCompleteCircuit([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    print(c.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
