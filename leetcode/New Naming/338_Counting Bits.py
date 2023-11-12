from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 2]
        res = [0, 1, 2]
        for i in range(3, n+1):
            res.append(str(bin(i)).count('1'))

        return res


if __name__ == '__main__':
    c = Solution()
    print(c.countBits(5))