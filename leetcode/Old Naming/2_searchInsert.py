"""Search Insert"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if mid - 1 == 0:
                end = mid
            else:
                end = mid - 1
        else:
            start = mid + 1
    return end


print(searchInsert([1,2,4,6,7], 3))