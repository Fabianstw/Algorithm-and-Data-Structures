"""Find the median of two sorted arrays in the runtime of O(log n+m)"""
import math
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    s = nums1 + nums2
    mid = (len(s) - 1) / 2
    if type(mid) is float:
        mid_1 = math.floor(mid)
        mid_2 = math.ceil(mid)
        res = (s[mid_1] + s[mid_2])/2
    else:
        mid = int(mid)
        res = s[mid]

    return float(res)


if __name__ == '__main__':
    print(findMedianSortedArrays([1, 2], [2, 3]))
