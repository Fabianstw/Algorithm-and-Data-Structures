"""Top k frequency"""
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    nums_set = set(nums)
    res = []
    for num_s in nums_set:
        res.append((nums.count(num_s), num_s))

    print(res)
    res_sorted = sorted(res, key=lambda x: x[0])
    print(res_sorted)
    res = []
    for i in range(k):
        res.append(res_sorted[len(res_sorted) - i - 1][1])

    return res


print(topKFrequent([1,1,1,2,2,3], 2))