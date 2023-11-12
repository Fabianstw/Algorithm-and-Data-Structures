"""Merge two sorted arrays into one sorted array."""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res = []
        start_m, start_n = 0, 0
        while start_m < m and start_n < n:
            print()
            if nums1[start_m] < nums2[start_n]:
                res.append(nums1[start_m])
                start_m += 1
            else:
                res.append(nums2[start_n])
                start_n += 1

        for i in range(start_m, m):
            res.append(nums1[i])

        for i in range(start_n, n):
            res.append(nums2[i])

        nums1.clear()
        nums1.append(res)
        print(nums1)
        

if __name__ == '__main__':
    c = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    c.merge(nums1, m, nums2, n)