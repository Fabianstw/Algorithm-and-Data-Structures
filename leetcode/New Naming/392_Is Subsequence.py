"""l"""

from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for letter in t:
            if s[0] == letter:
                s = s[1:]
            if len(s) == 0:
                return True
        return False


if __name__ == '__main__':
    c = Solution()
    print(c.isSubsequence("abc", "abcde"))
