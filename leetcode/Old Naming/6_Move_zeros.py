"""Move all Zeros to the end of the list, while remaining the rest order of the list"""
from typing import List


def moveZeroes(nums: List[int]) -> List[int]:
    rest = []
    zeros = []

    for i in range(len(nums)):
        if nums[i] == 0:
            zeros.append(0)
        else:
            rest.append(nums[i])
    res = rest + zeros
    nums.clear()
    nums.extend(res)

    return res


print(moveZeroes([1,2,0,4,0,10]))
