"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for pre in range(len(nums) - 2):
            start, end = pre + 1, len(nums) - 1
            while start < end:
                if nums[pre] + nums[start] + nums[end] == 0:
                    if [nums[pre], nums[start], nums[end]] not in res:
                        res.append([nums[pre], nums[start], nums[end]])
                    start += 1
                elif nums[pre] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    end -= 1

        return res


if __name__ == '__main__':
    c = Solution()
    print(c.threeSum([-1,0,1,2,-1,-4]))
