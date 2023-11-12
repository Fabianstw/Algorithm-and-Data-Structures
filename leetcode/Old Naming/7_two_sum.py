"""Find a sum in a list with two numbers their addition is the target"""
import math
from typing import List



def twoSum(nums: List[int], target: int) -> List[int]:
    start, end = 0, len(nums) - 1
    new_nums = nums.copy()
    new_nums.sort()
    while start <= end:
        if new_nums[start] + new_nums[end] == target:
            first_val = nums.index(new_nums[start])
            nums[first_val] = math.inf
            sec_val = nums.index(new_nums[end])
            return [first_val, sec_val]
        elif new_nums[start] + new_nums[end] < target:
            start += 1
        else:
            end -= 1


print(twoSum([10,1,2,3,3,4,5,6,7], 3))