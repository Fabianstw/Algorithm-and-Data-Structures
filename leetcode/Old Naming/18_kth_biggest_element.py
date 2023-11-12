"""Find the kth biggest element in O(n)"""
import math
from typing import List


def findKthLargest_2(nums: List[int], k: int) -> int:
    res = []
    for num in nums:
        if len(res) < k:
            res = insert_in_list(res, num)
        else:
            if res[0] < num:
                res.pop(0)
                res = insert_in_list(res, num)

    print(res)
    return res[0]


def insert_in_list(res: List[int], num: int) -> List[int]:
    left = 0
    right = len(res) - 1
    while left <= right:
        mid = (left + right) // 2
        if res[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    res.insert(left, num)
    return res


def findKthLargest(nums: List[int], k: int) -> int:
    new_list = []
    n = math.ceil(len(nums)/k)
    print(n)
    for i in range(k):
        if n*i > len(nums)-1:
            break
        new_list.append(max(nums[n*i:n*(i+1)]))

    return min(new_list)


if __name__ == '__main__':
    print(findKthLargest([3,2,1,5,6,4], 2))
