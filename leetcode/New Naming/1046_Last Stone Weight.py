import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            secon = heapq.heappop(stones)
            if first != secon:
                new_value = -abs(secon - first)
                heapq.heappush(stones, new_value)

        return -stones[0]



if __name__ == '__main__':
    c = Solution()
    print(c.lastStoneWeight([2,7,4,1,8,1]))