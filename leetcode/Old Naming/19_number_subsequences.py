"""Number of Subsequences That Satisfy the Given Sum Condition"""
from typing import List
import itertools


def numSubseq(nums: List[int], target: int) -> int:
    nums.sort()
    start = 0
    end = len(nums) - 1
    res = 0
    while start <= end:
        if nums[start] + nums[end] > target:
            end -= 1
        else:
            res += 2 ** (end - start) % (10**9 + 7)
            start += 1

    return res % (10**9 + 7)


if __name__ == '__main__':
    print(numSubseq([2,3,3,4,6,7], 12))

    print(numSubseq([4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11,
                    12, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 16, 17, 17, 17, 17, 18, 18,
                    19, 20, 20], 22))
