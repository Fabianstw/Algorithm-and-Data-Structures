"""
Today: 25.11.2023
274. H-Index
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i+1 >= citations[i]:
                return max(i, citations[i])
        return len(citations)

    def hIndex2(self, citations: List[int]) -> int:

        l, r = 0, len(citations)
        while l < r:
            m = (l + r + 1) // 2

            cnt = 0
            for c in citations:
                if c >= m:
                    cnt += 1

            if cnt >= m:
                l = m
            else:
                r = m - 1

        return l


if __name__ == '__main__':
    c = Solution()
    print(c.hIndex([3,0,6,1,5]))