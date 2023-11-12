class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = []
        for i in range(n):
            if i == 0:
                cache.append(1)
            elif i == 1:
                cache.append(2)
            else:
                cache.append(cache[i-1] + cache[i-2])

        return cache[len(cache) - 1]


if __name__ == '__main__':
    c = Solution()
    print(c.climbStairs(4))
    