"""leet"""

from typing import List


class Solution:

    def numDecodings(self, s: str, index=0) -> int:
        res = [0 for _ in range(len(s))]

        for i in range(len(s)):
            if int(s[i]) > 0 and i == 0:
                res[i] = 1
            elif 0 < int(s[i-1]) < 3 and 0 < int(s[i]) < 3:
                if res[i-1] == 1:
                    res[i] = 2
                else:
                    res[i] = res[i - 1] * 2 - 1
            elif 0 < int(s[i - 1]) < 3 and 3 < int(s[i]) < 7:
                res[i] = res[i - 1] + 1
            elif 0 < int(s[i - 1]) < 3 and 6 < int(s[i]):
                res[i] = res[i - 1]
            elif 3 > int(s[i - 1]) > 0 == int(s[i]):
                res[i] = res[i - 1]

        print(res)
        return res[len(res) - 1]


if __name__ == '__main__':
    c = Solution()
    print(c.numDecodings("10"))
