from typing import List


class Solution(object):
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        res = [0 for _ in range(len(nums))]
        res[0] = 1
        for i in range(len(nums)):
            print(res)
            if res[i] == 1:
                for j in range(1, nums[i] + 1):
                    if i + j >= len(nums) - 1:
                        return True
                    res[i + j] = 1
        return False

    def canJump(self, nums: List[int]) -> bool:
        # always start at index 0 and want to finish at last index
        visited = [False] * len(nums)
        visited[0] = True
        i = 0
        step = nums[0]
        while i <= step and i < len(nums):
            visited[i] = True
            if nums[i] > step - i:
                step = i + nums[i]
            i += 1

        if visited[-1]:
            return True
        return False




if __name__ == '__main__':
    c = Solution()
    print(c.canJump([2, 3, 1, 1, 4]))
