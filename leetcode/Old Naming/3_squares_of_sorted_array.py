"""Square each array and sort it afterwards again"""
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    result = []
    for num in nums:
        result.append(num**2)

    result.sort()
    return result
