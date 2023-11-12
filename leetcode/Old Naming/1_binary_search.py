"""Binary search"""
from typing import List


def search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)
    while start < end:
        mid = (start + end) // 2
        print(start, end)
        print(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            if start == mid:
                start += 1
            else:
                start = mid
        else:
            if end == mid:
                end += 1
            else:
                end = mid

    return -1


print(search([-1, 0, 3, 5, 9, 12], 100))
