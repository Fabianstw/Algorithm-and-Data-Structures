""""""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if mid == 0:
                return 0
            if mid == len(arr) - 1:
                return len(arr) - 1
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        return start

if __name__ == '__main__':
    c = Solution()
    print(c.peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))
