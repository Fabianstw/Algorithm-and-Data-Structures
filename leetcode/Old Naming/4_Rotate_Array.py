"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative."""
import copy
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        res = nums[len(nums) - k:] + nums[:len(nums) - k]
        nums.clear()
        nums.extend(res)
        return nums


if __name__ == '__main__':
    test = [1,2,3,4,5,6,7]
    test2 = test[len(test) - 3:] + test[:len(test) - 3]
    
    print(test2)

