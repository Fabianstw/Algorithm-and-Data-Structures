from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}

        def helper(zahlen, goal, index):
            if (goal, index) in cache:
                return cache[(goal, index)]
            if index == len(zahlen) - 1:
                if zahlen[index] == 0 and target == 0:
                    return 2
                if zahlen[index] == goal or zahlen[index] == (-goal):
                    return 1
                return 0

            cache.update({(goal, index): helper(zahlen, goal - zahlen[index], index + 1) +
                                         helper(zahlen, goal + zahlen[index], index + 1)})
            return cache[goal, index]

        return helper(nums, target, 0)


if __name__ == '__main__':
    c = Solution()
    print(c.findTargetSumWays([1,1,1,1,1], 3))
