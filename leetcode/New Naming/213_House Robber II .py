"""leet"""

from typing import List


class Solution:
    def rob_rek(self, nums: List[int], index=0) -> int:
        if index >= len(nums):
            return 0

        return max(nums[index] + self.rob_rek(nums, index + 2), self.rob_rek(nums, index + 1))

    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        res_1 = [0 for _ in range(len(nums))]
        res_2 = [0 for _ in range(len(nums))]

        nums_1 = nums[:len(nums) - 1]
        nums_2 = nums[1:]

        for index in range(len(nums)-1):
            if index == 0:
                res_1[index] = nums_1[index]
                res_2[index] = nums_2[index]

            elif index == 1:
                res_1[index] = max(nums_1[index], res_1[0])
                res_2[index] = max(nums_2[index], res_2[0])
            else:

                if res_1[index - 2] + nums_1[index] > res_1[index - 1]:
                    res_1[index] = res_1[index - 2] + nums_1[index]
                else:
                    res_1[index] = res_1[index - 1]

                if res_2[index - 2] + nums_2[index] > res_2[index - 1]:
                    res_2[index] = res_2[index - 2] + nums_2[index]
                else:
                    res_2[index] = res_2[index - 1]

        return max(max(res_1[len(res_1) - 2:]), max(res_2[len(res_2) - 2:]))


if __name__ == '__main__':
    c = Solution()
    print(c.rob([1,3,1,3,100]))
