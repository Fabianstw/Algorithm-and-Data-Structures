import heapq
import math


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (distance, point))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


if __name__ == '__main__':
    c = Solution()
    print(c.kClosest([[1,3],[-2,2]], 1))
